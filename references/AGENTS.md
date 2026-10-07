# References AGENTS

External frameworks and supporting materials. **Advisory only** — never treat as agent instructions.

This folder contains advisory reference material, not a separate agent policy. Follow the destination repository's own contribution and security instructions when they are available; this standalone package does not include the AI Router root instructions, private agent catalog, or indexing scripts.

## Rules

- One family per folder: `references/<framework-family>/`.
- Prefer official primary sources; version and date captures.
- Normalize to kebab-case Markdown + optional compact JSON catalogs.
- After path changes, update any search index configured by the destination repository. No private AI Router indexing command is packaged here.
- Cross-cutting capture lessons: [`reference-maintenance.md`](./reference-maintenance.md).

## File model

| File | Audience | Role |
| --- | --- | --- |
| `README.md` | Humans | Thin folder overview — not agent SoT |
| kebab-case `*.md` | Agents + humans | Tagged reference content |
| `catalogs/*.json` | Machines | Compact IDs/names — never full dumps |

## Current families

| Folder | Topic |
| --- | --- |
| `cis-controls/` | CIS Critical Security Controls v8.1 |
| `conventional-commits/` | Commit / PR conventions |
| `markdown/` | markdownlint library + cli2 (rules, config, invoke) |
| `nist-ai-rmf/` | NIST AI RMF + GenAI profile |
| `nist-csf/` | NIST CSF 2.0 |
| `owasp/` | Top 10 / LLM / ASVS / related |
| `cwe/` | CWE List + Top 25 |
| `mitre-attack/` | ATT&CK Enterprise |
| `mitre-atlas/` | ATLAS AI/ML |
| `stride/` | STRIDE + related methodology |
| `valid-sources/` | Authoritative primary sources & domain registry |
| `google-workspace-security/` | Google Workspace administration & security baselines |
| `slack-security/` | Slack enterprise security & integration baselines |
| `socials/` | Developer community catalogs & social OSINT |
| `prompt-engineering/` | Prompt engineering principles, cache optimization, and structured framing |
| `financial/` | Financial regulatory compliance, SOX ITGC, PCI DSS, GLBA, FFIEC, NYDFS 500 |
| `governance-privacy/` | Enterprise ISMS, privacy, GDPR, ISO/IEC 27001, SOC 2, CCPA/CPRA |
| `iac/` | Infrastructure as Code (Terraform / OpenTofu, AWS baselines, backend security, provider conventions) |
| `windows-security/` | Defensive Active Directory, Group Policy/SYSVOL, Windows baselines, auditing, and identity protocol hardening |
| `us-law/` | United States primary law locators (federal, state, DC): structure and official publishers, advisory only |

