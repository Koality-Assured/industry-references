---
doc_kind: reference
canonical_id: stride-categories
topics: [threat-modeling, secure-design]
rag_keywords: [stride, spoofing, tampering, microsoft, cms, threat-modeling]
captured_at_utc: 2026-08-20T18:05:00Z
upstream_url: https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats
advisory_only: true
---

# STRIDE categories

## Purpose

Paraphrased STRIDE category table for design-time threat enumeration. Not a full threat-modeling playbook or skill.

## Upstream

- <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats>
- Training unit: <https://learn.microsoft.com/en-us/training/modules/tm-use-a-framework-to-identify-threats-and-find-ways-to-reduce-or-eliminate-risk/1b-threat-modeling-framework>
- Also described by the CMS Threat Modeling Handbook (same six categories / properties): <https://security.cms.gov/learn/cms-threat-modeling-handbook> — see [`cms-threat-modeling-handbook.md`](./cms-threat-modeling-handbook.md) for process methodology (do not duplicate this table there).

## Catalog

[`catalogs/stride-categories.json`](./catalogs/stride-categories.json)

| ID | Category | Security property |
| --- | --- | --- |
| S | Spoofing | Authentication |
| T | Tampering | Integrity |
| R | Repudiation | Non-repudiation |
| I | Information Disclosure | Confidentiality |
| D | Denial of Service | Availability |
| E | Elevation of Privilege | Authorization |

## Advisory

Paraphrased from Microsoft Learn; CMS handbook table agrees. Advisory only — not a substitute for a threat-model workflow.
