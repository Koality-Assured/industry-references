---
doc_kind: reference
canonical_id: nist-csf-2.0
topics: [cybersecurity, risk-management, governance]
rag_keywords: [nist, csf, govern, identify, protect, detect, respond, recover]
version: "2.0"
publication: NIST CSWP 29
captured_at_utc: 2026-08-20T17:00:00Z
upstream_url: https://doi.org/10.6028/NIST.CSWP.29
advisory_only: true
---

# NIST CSF 2.0

## Purpose

Compact operational catalog of CSF 2.0 Functions, Categories, and Subcategories for cybersecurity posture assessment, control mapping, and risk discussions.

## Upstream

- DOI: <https://doi.org/10.6028/NIST.CSWP.29>
- PDF: <https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf>
- Reference Tool: <https://csrc.nist.gov/Projects/cybersecurity-framework>
- CPRT (Cybersecurity and Privacy Reference Tool): <https://cprt.nist.gov/>

## Framework Pillars

NIST CSF 2.0 is organized around three primary components:

1. **Framework Core:** A taxonomy of cybersecurity outcomes across 6 Functions, 34 Categories, and 185 Subcategories.
2. **Framework Profiles:** Custom selections of Core outcomes aligned to an organization's requirements, risk tolerance, and resources (Current State vs. Target State).
3. **Framework Tiers:** Characterize the rigor and sophistication of cybersecurity risk governance (Tiers 1 through 4).

## The Six Functions

| Function | ID | Description | Categories | Subcategories |
| --- | --- | --- | --- | --- |
| **Govern** | `GV` | Risk management strategy, expectations, policy, and supply chain governance | 6 | 31 |
| **Identify** | `ID` | Understanding assets, suppliers, risks, and improvement opportunities | 3 | 20 |
| **Protect** | `PR` | Implementing safeguards to contain or limit cybersecurity impacts | 5 | 42 |
| **Detect** | `DE` | Finding and analyzing potential cybersecurity compromises and anomalies | 2 | 18 |
| **Respond** | `RS` | Taking action regarding a detected cybersecurity incident | 4 | 38 |
| **Recover** | `RC` | Restoring assets and operations affected by a cybersecurity incident | 2 | 36 |

## Framework Tiers

- **Tier 1: Partial** — Informal, reactive risk management; limited organizational awareness; ad-hoc external collaboration.
- **Tier 2: Risk Informed** — Approved risk practices exist but are not organization-wide; awareness exists; informal information sharing.
- **Tier 3: Repeatable** — Organization-wide policies and formal practices; consistent reviews; formalized collaboration mechanisms.
- **Tier 4: Adaptive** — Risk-informed dynamic adaptation; predictive posture changes; continuous enterprise-wide feedback loops.

## Topic References

- [`govern-function.md`](./govern-function.md): In-depth breakdown of GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, and GV.SC.
- [`transition-guide-1.1-to-2.0.md`](./transition-guide-1.1-to-2.0.md): Evolution, scope changes, and category mapping.
- Core Catalog: [`catalogs/csf-2.0-core.json`](./catalogs/csf-2.0-core.json) (185 subcategories with full outcome text).

## Advisory

NIST series — cite DOI/PDF. Advisory only.
