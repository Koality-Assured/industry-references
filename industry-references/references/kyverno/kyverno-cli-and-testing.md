---
doc_kind: reference
canonical_id: kyverno-cli-and-testing
topics: [kubernetes, kyverno, testing, cli, ci-cd, policy-as-code]
rag_keywords: [kyverno-cli, kyverno-test, test-yaml, unit-tests, admission-testing, assertions, mock-resources]
version: "1.12+"
publication: Kyverno CLI Documentation & Testing Guide
captured_at_utc: 2026-10-10T12:00:00Z
upstream_url: https://kyverno.io/docs/kyverno-cli/test/
advisory_only: true
---

# Kyverno CLI and testing reference

Operational guide for validating and unit-testing Kyverno policies offline in development and CI/CD pipelines using the `kyverno` CLI.

## Purpose

The Kyverno CLI (`kyverno`) enables deterministic, offline evaluation of policies against target Kubernetes manifests without requiring an active Kubernetes cluster or running webhook engine.

## Core CLI subcommands

| Command | Purpose |
| --- | --- |
| `kyverno test <path>` | Runs declarative unit test suites defined in `kyverno-test.yaml`. |
| `kyverno apply <policy> --resource <resource>` | Directly applies a policy to raw manifests and outputs evaluation logs / mutated manifests. |
| `kyverno fmt <path>` | Formats policy manifests to canonical YAML indentation and structure. |
| `kyverno fix <path>` | Migrates deprecated Kyverno schema fields to current API conventions. |

## Unit testing directory layout

A compliant test suite organizes policies, mock resources, and assertions into a single test folder:

```text
supporting/kyverno/policies/
├── disallow-latest-tag.yaml          # Target policy manifest
├── resources.yaml                    # Positive & negative mock resources
└── kyverno-test.yaml                 # Test declaration & assertions
```

## Anatomy of `kyverno-test.yaml`

The test declaration uses `cli.kyverno.io/v1alpha1`:

```yaml
name: disallow-latest-tag-tests
policies:
  - disallow-latest-tag.yaml
resources:
  - resources.yaml
results:
  # Positive test: pinned image tag passes
  - policy: disallow-latest-tag
    rule: validate-image-tag
    resource: good-workload
    kind: Deployment
    result: pass

  # Negative test: latest image tag fails
  - policy: disallow-latest-tag
    rule: validate-image-tag
    resource: bad-workload
    kind: Deployment
    result: fail
```

### Result fields

- **`policy`**: Must match `metadata.name` of the target `ClusterPolicy` or `Policy`.
- **`rule`**: Must match `spec.rules[].name`.
- **`resource`**: Must match `metadata.name` of the mock resource in `resources.yaml`.
- **`kind`**: The resource kind (e.g., `Pod`, `Deployment`, `Service`).
- **`result`**: The expected outcome:
  - `pass`: Resource satisfies the policy or was admitted.
  - `fail`: Resource triggered a validation failure.
  - `skip`: Resource was excluded by policy selectors or pre-conditions.

## Defining mock resources (`resources.yaml`)

Mock resources must provide minimal valid Kubernetes schemas representing both conforming and non-conforming configurations:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: good-workload
  namespace: test-env
spec:
  template:
    spec:
      containers:
        - name: app
          image: registry.example.com/app:v1.2.3
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bad-workload
  namespace: test-env
spec:
  template:
    spec:
      containers:
        - name: app
          image: registry.example.com/app:latest
```

## Running tests

Execute tests against a folder containing `kyverno-test.yaml`:

```bash
# Run test suite in current folder
kyverno test .

# Run test suite across all subdirectories
kyverno test ./supporting/kyverno/policies/
```

### Expected CLI output
```text
Executing disallow-latest-tag-tests...
applying 1 policy to 2 resources... 

│ ---- │ --------------------- │ -------------------- │ ---------------------- │ -------- │
│ ID   │ POLICY                │ RULE                 │ RESOURCE               │ RESULT   │
│ ---- │ --------------------- │ -------------------- │ ---------------------- │ -------- │
│ 1    │ disallow-latest-tag   │ validate-image-tag   │ test-env/Deployment/good-workload │ Pass     │
│ 2    │ disallow-latest-tag   │ validate-image-tag   │ test-env/Deployment/bad-workload  │ Pass     │
│ ---- │ --------------------- │ -------------------- │ ---------------------- │ -------- │
```

## CI/CD pipeline integration

Integrate the Kyverno CLI into GitHub Actions or GitLab CI to prevent non-compliant policies or application manifests from reaching main branches:

```yaml
- name: Install Kyverno CLI
  uses: kyverno/action-install-cli@v0.3.0
  with:
    release: 'v1.12.5'

- name: Run Kyverno Unit Tests
  run: |
    kyverno test ./supporting/kyverno/policies/
```
