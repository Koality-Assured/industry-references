---
doc_kind: reference
canonical_id: kyverno-policy-authoring
topics: [kubernetes, kyverno, policy-as-code, admission-control, security, cel]
rag_keywords: [kyverno, clusterpolicy, policy, validate, mutate, generate, verifyimages, cel, common-expression-language, autogen, anchors]
version: "1.12+"
publication: Kyverno Documentation & CNCF Project Guidelines
captured_at_utc: 2026-10-10T12:00:00Z
upstream_url: https://kyverno.io/docs/writing-policies/
advisory_only: true
---

# Kyverno policy authoring reference

Definitive reference for designing, structuring, and authoring Kyverno policies within Kubernetes clusters.

## CRD scopes

Kyverno provides two Custom Resource Definitions (CRDs) for policy enforcement:

- **`ClusterPolicy` (`kyverno.io/v1`)**: Cluster-wide scope. Evaluates resources across all namespaces unless explicitly filtered.
- **`Policy` (`kyverno.io/v1`)**: Namespaced scope. Evaluates only resources created within the policy's defined namespace.

Every policy consists of metadata, an optional `spec.validationFailureAction` (`Audit` or `Enforce`), an optional `spec.background` evaluation boolean, and an array of `spec.rules`.

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: disallow-privileged-containers
  annotations:
    policies.kyverno.io/title: Disallow Privileged Containers
    policies.kyverno.io/category: Pod Security Standards (Restricted)
    policies.kyverno.io/severity: medium
spec:
  validationFailureAction: Audit
  background: true
  rules:
    - name: check-privileged
      match:
        any:
        - resources:
            kinds:
              - Pod
      validate:
        message: "Privileged containers are prohibited."
        pattern:
          spec:
            containers:
              - =(securityContext):
                  =(privileged): "false"
```

## Match and exclude criteria

Rules match or exclude incoming admission requests using structured filters:

- **`resources`**: Filter by `kinds`, `namespaces`, `names`, `selector` (label matching), and `annotations`.
- **`subjects`**: Filter by RBAC `User`, `Group`, or `ServiceAccount`.
- **`roles` / `clusterRoles`**: Filter by the requesting actor's bound permissions.

Use `any` (logical OR) or `all` (logical AND) blocks to combine multiple match statements:

```yaml
match:
  any:
  - resources:
      kinds:
        - Pod
      namespaces:
        - production
        - staging
exclude:
  any:
  - resources:
      namespaces:
        - kube-system
        - kyverno
```

## Validation rules

### Pattern matching and anchors

Kyverno patterns define the desired state. If a target manifest diverges, admission is blocked or audited. Anchor operators modify evaluation logic:

| Anchor | Name | Behavior |
| --- | --- | --- |
| `(key): value` | **Conditional** | Evaluates target only if `key` is present in the resource. |
| `+(key): value` | **Equality / Add** | If `key` is present, it must equal `value`. If missing, the rule fails (requires existence). |
| `=(key): value` | **Existence** | Verifies `key` exists and matches `value` if parent exists. |
| `!(key): value` | **Negation** | Condition passes only if `key` does not match `value` or is absent. |

#### Example: Drop all capabilities
```yaml
validate:
  message: "All capabilities must be dropped."
  pattern:
    spec:
      containers:
        - securityContext:
            capabilities:
              drop:
                - ALL
```

### AnyPattern

When a resource may satisfy one of several compliant configurations, use `anyPattern`:

```yaml
validate:
  message: "Must either set readOnlyRootFilesystem or mount a dedicated volume."
  anyPattern:
    - spec:
        containers:
          - securityContext:
              readOnlyRootFilesystem: true
    - spec:
        volumes:
          - emptyDir: {}
```

### Common Expression Language (CEL) validation

In Kyverno 1.11+ (aligned with Kubernetes 1.30+ in-tree CEL admission control), rules can execute native CEL expressions via `validate.cel`. CEL runs compiled in-process with minimal CPU overhead:

```yaml
validate:
  cel:
    expressions:
      - expression: "object.spec.containers.all(c, !has(c.securityContext) || !has(c.securityContext.privileged) || c.securityContext.privileged == false)"
        message: "Running privileged containers is disallowed."
```

## Mutation rules

Mutation rules transform incoming manifests before persistence in `etcd`.

### Strategic merge mutation
Overlay structures onto matching resources:

```yaml
mutate:
  patchStrategicMerge:
    metadata:
      labels:
        +(managed-by): "gitops"
    spec:
      +(securityContext):
        runAsNonRoot: true
```

### RFC 6902 JSON patch mutation
Fine-grained array and pointer mutations:

```yaml
mutate:
  patchesJson6902: |-
    - op: add
      path: /metadata/labels/deployed-by
      value: automated-pipeline
```

## Generation rules

Generation rules create supplementary resources upon creation of a trigger resource (e.g., scaffolding a default `NetworkPolicy` whenever a new `Namespace` is created).

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: default-deny-networkpolicy
spec:
  rules:
    - name: create-default-deny
      match:
        any:
        - resources:
            kinds:
              - Namespace
      generate:
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        name: default-deny-all
        namespace: "{{request.object.metadata.name}}"
        synchronize: true
        data:
          spec:
            podSelector: {}
            policyTypes:
              - Ingress
              - Egress
```

- **`synchronize: true`**: Ongoing reconciliation. Changes to the generated resource are overridden back to the policy spec; deleting the policy cascades to the generated resources.
- **`synchronize: false`**: One-time generation on trigger creation.

## Image verification rules

Kyverno verifies cryptographic signatures, attestations, and Software Bills of Materials (SBOMs) using Cosign and Sigstore:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signatures
spec:
  validationFailureAction: Enforce
  webhookTimeoutSeconds: 30
  rules:
    - name: verify-sigstore
      match:
        any:
        - resources:
            kinds:
              - Pod
      verifyImages:
        - imageReferences:
            - "ghcr.io/my-org/*"
          attestors:
            - entries:
                - keyless:
                    issuer: "https://token.actions.githubusercontent.com"
                    subject: "https://github.com/my-org/*"
```

## Autogen controllers

When a policy targets `Pod`, Kyverno automatically generates cloned rules targeting Pod controllers (`Deployment`, `DaemonSet`, `StatefulSet`, `Job`, `CronJob`).

- By default, `spec.rules` written for `Pod` apply to controllers automatically.
- To inspect or override generated rules, check annotations:
  - `pod-policies.kyverno.io/autogen-controllers: "Deployment,StatefulSet"` (restrict targets)
  - `pod-policies.kyverno.io/autogen-controllers: "none"` (disable autogen; rule targets bare pods only)
