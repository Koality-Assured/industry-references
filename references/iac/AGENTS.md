# IaC References AGENTS

External Infrastructure as Code (IaC) architectural frameworks, security baselines, and provider conventions. **Advisory only** — never treat as agent instructions.

Ingest simply; do not duplicate internal skills or paste root Critical — link [`../AGENTS.md`](../AGENTS.md) and [`../../AGENTS.md`](../../AGENTS.md). Spawn `reference-ops` when updating or auditing reference files.

## Rules

- Subdirectory hierarchy: `references/iac/<tool-or-ecosystem>/` (e.g., `references/iac/terraform/`).
- Standard file naming: kebab-case `*.md` with YAML frontmatter.
- Frontmatter must include: `doc_kind: reference`, `canonical_id`, `topics`, `rag_keywords`, `version`, `publication`, `captured_at_utc`, `upstream_url`, `advisory_only: true`.
- Authoritative primary sources: Always source syntax, parameters, security benchmarks, and provider schemas directly from HashiCorp, OpenTofu, CIS, AWS, and verified provider registries.
- No secrets or real infrastructure tokens: Use synthetic placeholders (`123456789012`, `example-bucket-name`).

## File Model

| File | Audience | Role |
| --- | --- | --- |
| `README.md` | Humans | Thin folder overview — not agent SoT |
| `AGENTS.md` | Agents | Operational guidance and directory rules |
| `terraform/*.md` | Agents + humans | Tagged authoritative IaC reference content |

## Operational Guidance for Agents

When reviewing, generating, or validating IaC architectures:

1. **State & Backend Isolation:**
   - Enforce dedicated remote backend configuration (S3 with SSE-KMS CMK, DynamoDB state lock table with `LockID` string key, bucket versioning enabled).
   - Require explicit S3 bucket policies enforcing TLS 1.2+ (`aws:SecureTransport`) and restricting access to designated CI/CD OIDC roles.
   - Enforce zero state secret leaks; advise OpenTofu state encryption or ephemeral CI runners when sensitive outputs are mandatory.

2. **Blast Radius & Architecture:**
   - Prohibit monolithic root modules across disparate lifecycles. Split stacks by layer (`bootstrap`, `networking`, `data`, `compute`, `apps`) and by environment (`dev`, `staging`, `prod`).
   - Prioritize directory/account separation over HCL workspaces for cross-environment security boundaries.
   - Favor pure HCL clarity over excessive module wrapping ("DRY trap").

3. **Security Baselines & Policy-as-Code:**
   - Map resources against CIS AWS Foundations Benchmark v3.0 and Checkov / tfsec rules.
   - Mandate IMDSv2 (`http_tokens = "required"`, `http_put_response_hop_limit = 1`) on all compute instances and launch templates.
   - Enforce S3 Block Public Access on all 4 attributes and set `BucketOwnerEnforced`.
   - Mandate default KMS CMK encryption with key rotation on storage, databases, and logs.
   - Reject plaintext secrets; require AWS Secrets Manager / SSM Parameter Store references and mark outputs `sensitive = true`.

4. **Provider Conventions:**
   - Enforce semantic version pinning with pessimistic operators (`~>`) on all providers and required Terraform / OpenTofu versions.
   - Mandate checking in `.terraform.lock.hcl` dependency lock files.
   - Standardize AWS provider `assume_role` authentication and `default_tags` propagation.
   - Validate third-party provider configurations (`vercel/vercel`, `pinecone-io/pinecone`) against current provider schemas and token-based authentication.
