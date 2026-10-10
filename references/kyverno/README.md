# Kyverno Reference

Official architectural guidance, policy authoring syntax, CLI testing patterns, and operational hardening for Kyverno.

Human entry point only. Agents: start at [`AGENTS.md`](./AGENTS.md) and open specific topic Markdown files (not this README) for operational content.

## Contents

| Document | Focus |
| --- | --- |
| [`AGENTS.md`](./AGENTS.md) | Agent routing and authoring constraints for this tree |
| [`kyverno-policy-authoring.md`](./kyverno-policy-authoring.md) | CRD anatomy (`ClusterPolicy`/`Policy`), validation (pattern & CEL), mutation, generation, and image verification |
| [`kyverno-cli-and-testing.md`](./kyverno-cli-and-testing.md) | Offline unit testing with `kyverno test`, mock manifests, and CI assertion design |
| [`kyverno-best-practices.md`](./kyverno-best-practices.md) | Admission webhook resilience, autogen behavior, `failurePolicy`, and rollout safety |

## Related

- Curated standards: [`../../docs/standards/kubernetes-security.md`](../../docs/standards/kubernetes-security.md)
- PaC research: [`../../research/policy-as-code/`](../../research/policy-as-code/README.md)
- Tooling recipes and starter policies: [`../../supporting/kyverno/`](../../supporting/kyverno/README.md)
- IaC references: [`../iac/`](../iac/README.md)
