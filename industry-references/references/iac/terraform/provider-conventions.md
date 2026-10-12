---
doc_kind: reference
canonical_id: terraform-provider-conventions
topics: [iac, terraform, opentofu, providers, aws-provider, vercel, pinecone, versioning, assume-role, multi-provider]
rag_keywords: [terraform-providers, version-pinning, pessimistic-operator, provider-aliasing, assume-role, vercel-provider, pinecone-provider, dependency-lock-file]
version: "1.9/1.8-tofu"
publication: Terraform Provider Specification & Registry Guidelines
captured_at_utc: 2026-09-02T00:00:00Z
upstream_url: https://developer.hashicorp.com/terraform/language/providers
advisory_only: true
---

# Provider Conventions & Configurations

## Purpose

Authoritative reference for Terraform and OpenTofu provider configurations, version pinning standards, dependency lock file hygiene, multi-provider aliasing patterns, IAM assumed role execution, and third-party SaaS/AI infrastructure providers (`vercel/vercel`, `pinecone-io/pinecone`).

## Upstream & Authority

- Primary Authority: HashiCorp Terraform Provider Configuration & OpenTofu Provider Specification
- Standard Registries: [Terraform Registry](https://registry.terraform.io/) & [OpenTofu Registry](https://search.opentofu.org/)
- Core Providers:
  - `hashicorp/aws` (AWS Provider v5.x)
  - `vercel/vercel` (Vercel Provider v2.x)
  - `pinecone-io/pinecone` (Pinecone Provider v0.8+/v1.x)
  - `hashicorp/random` & `hashicorp/tls`

---

## Semantic Versioning & Version Constraints

### Pessimistic Constraint Operator (`~>`)

Always declare strict version constraints in `versions.tf` using the pessimistic constraint operator (`~>`). This permits backward-compatible minor/patch upgrades while blocking breaking major version shifts:

| Constraint Expression | Meaning | Allowed Range | Prohibited Range |
| --- | --- | --- | --- |
| `~> 5.50` | Allow minor and patch upgrades | `>= 5.50.0`, `< 6.0.0` | `>= 6.0.0` (Major breaking change) |
| `~> 5.50.0` | Allow patch upgrades only | `>= 5.50.0`, `< 5.51.0` | `>= 5.51.0` (Feature minor releases) |
| `>= 1.9.0, < 2.0.0` | Terraform / OpenTofu binary constraints | Version 1.9.x through 1.x.x | `< 1.9.0` or `>= 2.0.0` |

### Required Providers Block Example

```hcl
terraform {
  required_version = ">= 1.9.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.50"
    }
    vercel = {
      source  = "vercel/vercel"
      version = "~> 2.0"
    }
    pinecone = {
      source  = "pinecone-io/pinecone"
      version = "~> 0.8"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}
```

### Dependency Lock File (`.terraform.lock.hcl`)

The dependency lock file records the exact version and cryptographic checksums of each downloaded provider.

- **Mandatory Git Check-in:** Always commit `.terraform.lock.hcl` to git.
- **Cross-Platform Checksums:** When developers work across operating systems (macOS ARM64, Linux AMD64, Windows AMD64), generate multi-platform lock hashes:
  ```bash
  terraform providers lock \
    -platform=linux_amd64 \
    -platform=darwin_arm64 \
    -platform=windows_amd64
  ```

---

## Multi-Provider Aliasing Patterns

Provider aliasing allows a single Terraform configuration to interact with multiple AWS regions or accounts simultaneously.

### Multi-Region & CloudFront / ACM Pattern

AWS CloudFront distributions require custom TLS certificates from AWS Certificate Manager (ACM) to reside specifically in `us-east-1`, even if primary infrastructure is hosted in another region (e.g., `us-west-2` or `eu-west-1`):

```hcl
# Default provider for primary application workloads
provider "aws" {
  region = "us-west-2"
}

# Aliased provider for global edge resources (ACM / CloudFront)
provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}

# S3 Bucket in primary region
resource "aws_s3_bucket" "webapp_bucket" {
  bucket = "ai-router-webapp-usw2"
}

# ACM Certificate explicitly created in us-east-1 for CloudFront
resource "aws_acm_certificate" "edge_cert" {
  provider          = aws.us_east_1
  domain_name       = "app.example.com"
  validation_method = "DNS"
}
```

### Passing Aliased Providers to Child Modules

When calling child modules that require secondary provider contexts:

```hcl
module "cdn_edge" {
  source = "../../modules/cdn-edge"

  providers = {
    aws           = aws
    aws.us_east_1 = aws.us_east_1
  }

  domain_name = "app.example.com"
}
```

---

## Assumed Role Configurations (STS / IAM)

Never use long-lived static AWS access keys (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`). Instead, configure the AWS provider to assume dedicated IAM execution roles via AWS Security Token Service (STS) using OIDC federation or instance profiles.

```hcl
provider "aws" {
  region = var.aws_region

  assume_role {
    role_arn     = "arn:aws:iam::${var.target_account_id}:role/TerraformExecutionRole"
    session_name = "TerraformDeploy-${var.environment}"
    external_id  = var.sts_external_id
  }

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "terraform"
      Project     = "ai-router"
    }
  }
}
```

### Assumed Role Parameters

| Parameter | Purpose | Best Practice |
| --- | --- | --- |
| `role_arn` | Target IAM Role ARN to assume | Scope to specific workload account. |
| `session_name` | Identifier shown in CloudTrail audit logs | Include pipeline run ID or environment name for traceability. |
| `external_id` | Shared secret condition preventing confused deputy attacks | Mandated for third-party or cross-account trust policies. |

---

## Third-Party Provider Configurations

### 1. Vercel Provider (`vercel/vercel`)

The official Vercel provider provisions frontend hosting, edge domains, and environment variables.

#### Authentication & Configuration

- **Auth Token:** Pass via environment variable `VERCEL_API_TOKEN` (never in HCL files).
- **Team ID:** Specify `team` if managing resources within a Vercel Pro/Enterprise team.

```hcl
provider "vercel" {
  # Reads VERCEL_API_TOKEN from runner environment
  team = var.vercel_team_id
}

resource "vercel_project" "frontend" {
  name      = "ai-router-web"
  framework = "nextjs"
  git_repository = {
    type = "github"
    repo = "Koality-Assured/ai-router"
  }
}

# Securely inject backend API endpoint into Vercel production environment
resource "vercel_project_environment_variable" "api_url" {
  project_id = vercel_project.frontend.id
  key        = "NEXT_PUBLIC_API_URL"
  value      = "https://${aws_route53_record.api.fqdn}"
  target     = ["production", "preview"]
}
```

---

### 2. Pinecone Provider (`pinecone-io/pinecone`)

The Pinecone provider provisions serverless and pod-based vector indexes for AI/ML embeddings and semantic search pipelines.

#### Authentication & Configuration

- **API Key:** Pass via environment variable `PINECONE_API_KEY`.

```hcl
provider "pinecone" {
  # Reads PINECONE_API_KEY from runner environment
}

resource "pinecone_index" "embeddings" {
  name      = "${var.environment}-ai-router-embeddings"
  dimension = 1536       # Matches text-embedding-3-small / text-embedding-ada-002
  metric    = "cosine"

  spec = {
    serverless = {
      cloud  = "aws"
      region = "us-east-1"
    }
  }
}

output "pinecone_index_host" {
  description = "Host endpoint for Pinecone vector queries"
  value       = pinecone_index.embeddings.host
}
```

---

## Sources & Registry References

- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Terraform Vercel Provider Documentation](https://registry.terraform.io/providers/vercel/vercel/latest/docs)
- [Terraform Pinecone Provider Documentation](https://registry.terraform.io/providers/pinecone-io/pinecone/latest/docs)
- [HashiCorp Provider Configuration Guide](https://developer.hashicorp.com/terraform/language/providers/configuration)
- [AWS Security Token Service (STS) AssumeRole Documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)
