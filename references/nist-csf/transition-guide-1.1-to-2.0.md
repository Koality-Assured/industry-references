---
doc_kind: reference
canonical_id: nist-csf-transition-guide
topics: [cybersecurity, risk-management, governance, migration]
rag_keywords: [nist, csf, transition, migration, v1.1, v2.0, govern-function, c-scrm, cprt]
version: "2.0"
publication: NIST CSWP 29
captured_at_utc: 2026-08-25T13:40:00Z
upstream_url: https://doi.org/10.6028/NIST.CSWP.29
advisory_only: true
---

# NIST CSF 1.1 to 2.0 Transition Guide

## Executive Summary

NIST Cybersecurity Framework 2.0 (CSWP 29, February 2024) represents the first major overhaul of the framework since CSF 1.1 (2018). While maintaining core backwards conceptual compatibility, CSF 2.0 introduces structural expansion, governance prioritization, and decoupling of dynamic guidance.

## Major Shifts

### 1. Scope Expansion Beyond Critical Infrastructure
- **CSF 1.1:** Titled *Framework for Improving Critical Infrastructure Cybersecurity*.
- **CSF 2.0:** Titled *The NIST Cybersecurity Framework (CSF) 2.0*. Formally broadened to apply to all organizations across all sectors, sizes, and technical maturity levels (small businesses, non-profits, multinational enterprises, state/local governments).

### 2. Addition of the Govern (GV) Function
- **CSF 1.1:** 5 Functions (Identify, Protect, Detect, Respond, Recover).
- **CSF 2.0:** 6 Functions (Govern, Identify, Protect, Detect, Respond, Recover).
- **Impact:** Governance is elevated from a subset of Identify (`ID.GV`) into an overarching function covering strategy, roles, policy, oversight, and supply chain.

### 3. Structural Reorganization of Core

| Area | CSF 1.1 | CSF 2.0 | Key Shift |
| --- | --- | --- | --- |
| **Functions** | 5 | 6 | Added `GV` (Govern) |
| **Categories** | 23 | 34 | Reorganized into granular outcome domains |
| **Subcategories** | 108 | 185 | Clarified outcomes, removed technology specifics |
| **Governance** | Embedded in `ID.GV` | Dedicated `GV` function | Expanded into 6 categories (OC, RM, RR, PO, OV, SC) |
| **Supply Chain** | `ID.SC` (5 subcategories) | `GV.SC` (10 subcategories) | Elevated to dedicated governance domain |
| **Improvement** | Scattered across `RS.IM`, `RC.IM` | `ID.IM` | Consolidated under Identify |

### 4. Decoupled Implementation Examples & Informative References
- In CSF 1.1, informative references were statically embedded in the core document.
- In CSF 2.0, the core focuses purely on taxonomy and outcomes. Practical implementation examples and dynamic mappings (to NIST SP 800-53, ISO/IEC 27001, CIS Controls, etc.) are maintained online via the [NIST Cybersecurity and Privacy Reference Tool (CPRT)](https://cprt.nist.gov/).

### 5. Community and Organizational Profiles
- **Current vs. Target Profiles:** Standardized templates for measuring current posture and planning future investments.
- **Community Profiles:** Public profiles tailored for specific sectors (e.g., healthcare, maritime, financial, AI risk) or use cases.

## Transition Mapping Highlights

| CSF 1.1 Category | CSF 2.0 Destination | Migration Notes |
| --- | --- | --- |
| `ID.AM` (Asset Management) | `ID.AM` | Retained under Identify; clarifies physical/virtual assets |
| `ID.BE` (Business Environment) | `GV.OC` (Organizational Context) | Shifted to Govern |
| `ID.GV` (Governance) | `GV` (Full Function) | Expanded across `GV.RM`, `GV.RR`, `GV.PO`, `GV.OV` |
| `ID.RA` (Risk Assessment) | `ID.RA` | Retained and refined |
| `ID.RM` (Risk Mgmt Strategy) | `GV.RM` | Shifted to Govern |
| `ID.SC` (Supply Chain Risk) | `GV.SC` | Shifted to Govern; expanded from 5 to 10 subcategories |
| `PR.AC` (Access Control) | `PR.AA` (Authentication/Access) | Focused on credential & identity lifecycle |
| `PR.AT` (Awareness & Training) | `PR.AT` | Retained under Protect |
| `PR.DS` (Data Security) | `PR.DS` | Retained under Protect |
| `PR.IP` (Info Protection Processes) | Distributed | Shifted across `PR.PS`, `PR.IR`, `GV.PO` |
| `PR.MA` (Maintenance) | `PR.PS` (Platform Security) | Merged into platform & configuration security |
| `PR.PT` (Protective Technology) | `PR.PS`, `PR.IR` | Reorganized into platform resilience |
| `DE.AE` (Anomalies & Events) | `DE.AE` (Adverse Event Analysis) | Clarified event analysis and escalation |
| `DE.CM` (Continuous Monitoring) | `DE.CM` | Retained under Detect |
| `DE.DP` (Detection Processes) | `DE.AE`, `DE.CM` | Streamlined into monitoring and analysis |
| `RS.RP` / `RS.CO` / `RS.AN` / `RS.MI` | `RS.MA`, `RS.CO`, `RS.AN`, `RS.MI` | Incident response workflow modernized |
| `RS.IM` (Improvement) | `ID.IM` | Moved to Identify continuous improvement |
| `RC.RP` / `RC.IM` / `RC.CO` | `RC.RP`, `RC.CO`, `ID.IM` | Recovery plan execution clarified |

## Advisory

Advisory reference material. Organizations should evaluate existing CSF 1.1 mappings and transition gradually using CPRT tools.
