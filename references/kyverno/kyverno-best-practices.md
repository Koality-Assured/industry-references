---
doc_kind: reference
canonical_id: kyverno-best-practices
topics: [kubernetes, kyverno, best-practices, performance, failure-policy, admission-control]
rag_keywords: [kyverno-best-practices, failurepolicy, webhooktimeout, audit-to-enforce, policyreport, autogen, admission-latency]
version: "1.12+"
publication: Kyverno Production Hardening & Operational Patterns
captured_at_utc: 2026-10-10T12:00:00Z
upstream_url: https://kyverno.io/docs/installation/best-practices/
advisory_only: true
---

# Kyverno operational best practices

Production guidance for configuring, deploying, and maintaining Kyverno policies without impacting Kubernetes API server availability or deployment velocity.

## Phased policy rollout (Audit to Enforce)

Never deploy a new validation rule directly with `validationFailureAction: Enforce`. Follow a three-stage rollout:

```text
Phase 1: Audit & Baseline  -->  Phase 2: Remediate Existing  -->  Phase 3: Enforce
(Generate PolicyReports)         (Fix non-compliant workloads)    (Block violations at admission)
```

1. **Deploy in Audit mode**: Set `spec.validationFailureAction: Audit` and `spec.background: true`.
2. **Inspect Policy Reports**: Query `PolicyReport` (namespaced) and `ClusterPolicyReport` (cluster-scoped) to identify non-compliant workloads currently running in the cluster.
3. **Notify and Remediate**: Update Helm charts and GitOps repositories to remediate findings.
4. **Transition to Enforce**: Switch `validationFailureAction: Enforce` once existing violations are resolved.

## Webhook failure policies

The admission webhook `failurePolicy` determines cluster behavior when the Kyverno admission webhook fails or times out:

- **`failurePolicy: Ignore` (Default for non-critical/audit rules)**:
  - If Kyverno is unavailable, the API server allows the request through.
  - Prevents cluster deadlocks during control-plane bootstrap or webhook restarts.
- **`failurePolicy: Fail` (Strict enforcement for P0 security controls)**:
  - If Kyverno cannot be reached within `webhookTimeoutSeconds` (default: 10s, recommended: 3-5s), the API server rejects the admission request.
  - **Caution**: Misconfigured `Fail` policies without system exclusions can render the cluster unable to spin up critical CNI or storage pods.

### Webhook timeout tuning
Keep `spec.webhookTimeoutSeconds` short (between `3` and `5` seconds) to prevent cascading API server queue saturation during upstream delays.

## Namespace and system exclusions

Every cluster-wide policy **must** explicitly exclude critical control-plane and infrastructure namespaces from evaluation to prevent cluster bricking:

```yaml
exclude:
  any:
  - resources:
      namespaces:
        - kube-system
        - kube-public
        - kube-node-lease
        - kyverno
```

For workloads with legitimate architectural exceptions, use scoped label or annotation exclusions rather than broad wildcard exemptions:

```yaml
exclude:
  any:
  - resources:
      selector:
        matchLabels:
          policy.internal/bypass-root-check: "approved"
```

## Admission latency and performance

Each admission webhook call adds latency to `kubectl`, Helm, and controller requests. To minimize overhead:

- **Prefer CEL over JMESPath**: CEL expressions compiled in-process execute in microseconds, avoiding JMESPath string interpretation.
- **Minimize API calls**: Rules using `context.apiCall` perform synchronous HTTP queries during admission. Use API calls only when data cannot be obtained from the admission review request or a replicated ConfigMap.
- **Set resource limits**: Run Kyverno with at least 3 replicas in production, spread across availability zones using `podAntiAffinity`, with adequate memory limits (1-2GiB minimum depending on cluster object counts).

## Background scanning and reports

Kyverno periodically scans existing cluster resources against active policies:

- Keep `background: true` enabled for audit rules to generate updated `PolicyReport` objects.
- Disable `background: false` on mutation and generation rules; background scanning only evaluates validation.
- Clean up orphaned reports regularly using Kyverno's built-in cleanup controller.

## Autogen controllers hygiene

When writing rules targeting `Pod`:
- Be aware that Kyverno automatically generates matching rules for `Deployment`, `DaemonSet`, `StatefulSet`, `Job`, and `CronJob`.
- If a rule evaluates fields only set at pod scheduling (such as node placement or ephemeral volumes), restrict autogen controllers using the annotation:
  ```yaml
  metadata:
    annotations:
      pod-policies.kyverno.io/autogen-controllers: "none"
  ```
