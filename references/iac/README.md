# Infrastructure as Code (IaC) Frameworks & References

Normalized external reference materials, security baselines, and architectural patterns for Infrastructure as Code (IaC) tooling, cloud providers, and third-party infrastructure platforms.

> [!NOTE]
> **Advisory Reference**: Content in this directory is advisory reference material derived from HashiCorp Terraform documentation, OpenTofu specifications, CIS AWS Foundations Benchmark v3.0, Checkov/tfsec policy engines, and official provider registries. It is not an agent instruction set.
> 
> Human entry point only. Agents: start at [`AGENTS.md`](./AGENTS.md) and [`../AGENTS.md`](../AGENTS.md), and open specific topic Markdown files for operational content.

## Reference Topics

| Topic | Canonical File | Scope |
| --- | --- | --- |
| Terraform / OpenTofu Best Practices | [`terraform/best-practices.md`](./terraform/best-practices.md) | HashiCorp & OpenTofu architecture, directory hierarchy, blast-radius reduction, dev/stage/prod environment segregation, DRY vs readability trade-offs, resource tagging standards |
| Cloud Security Baselines & Policy-as-Code | [`terraform/security-baselines.md`](./terraform/security-baselines.md) | CIS AWS Foundations Benchmark v3.0 mapping, Checkov & tfsec policy rules, IMDSv2 enforcement, S3 block public access, default KMS CMK encryption, VPC endpoints, zero-plaintext secrets |
| State & Backend Security | [`terraform/state-and-backend-security.md`](./terraform/state-and-backend-security.md) | S3 remote backend hardening, bucket policies, KMS CMK policies, DynamoDB lock schemas, state secret leak mitigation, IAM roles for state access |
| Provider Conventions & Configurations | [`terraform/provider-conventions.md`](./terraform/provider-conventions.md) | Provider version constraints (`~> 5.0`), multi-provider aliasing, assumed role configurations, third-party provider integrations (`vercel/vercel`, `pinecone-io/pinecone`) |

## Primary Sources & Upstream Authorities

- [HashiCorp Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [OpenTofu Documentation](https://opentofu.org/docs/)
- [CIS AWS Foundations Benchmark v3.0](https://www.cisecurity.org/benchmark/amazon_web_services)
- [Checkov Policy Index (Bridgecrew / Palo Alto Networks)](https://www.checkov.io/5.Policy%20Index/all.html)
- [Trivy / tfsec Documentation (Aqua Security)](https://aquasecurity.github.io/trivy/latest/)
- [Terraform AWS Provider Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Vercel Provider Registry](https://registry.terraform.io/providers/vercel/vercel/latest/docs)
- [Terraform Pinecone Provider Registry](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs)
