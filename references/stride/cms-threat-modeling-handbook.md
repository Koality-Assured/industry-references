---
doc_kind: reference
canonical_id: cms-threat-modeling-handbook
topics: [threat-modeling, secure-design, stride]
rag_keywords:
  [
    cms,
    threat-modeling,
    four-question-frame,
    shostack,
    stride,
    dfd,
    pasta,
    linddun,
  ]
captured_at_utc: 2026-08-20T18:05:00Z
upstream_url: https://security.cms.gov/learn/cms-threat-modeling-handbook
advisory_only: true
---

# CMS Threat Modeling Handbook (methodology capture)

## Purpose

Paraphrased reusable threat-modeling methodology from the CMS Information Security and Privacy Program handbook (last reviewed 2/21/2024). Captures industry-standard process language only — not CMS-internal policy or systems of record.

## Upstream

- <https://security.cms.gov/learn/cms-threat-modeling-handbook>
- Related local STRIDE table: [`stride-categories.md`](./stride-categories.md)
- Compact process IDs: [`catalogs/threat-modeling-process.json`](./catalogs/threat-modeling-process.json)

## Scope disclaimer

Upstream material is aimed at CMS internal teams and ADOs. This capture keeps reusable methodology. CMS-internal tooling (CFACTS, CMS Confluence templates, CMS Mural accounts, Zoom, ISSO 90-day CFACTS upload) is **not adopted here** — mentioned only as CMS-internal tooling.

## What threat modeling is

Threat modeling is a proactive analysis of how attackers might abuse a system so teams can address risks early. Ideally it starts in design within the SDLC; the model is a **living artifact** revisited with new features or releases. Outputs include a model diagram plus a **prioritized list of security improvements** to conception, requirements, design, or implementation.

## Benefits (high level)

- Find problems earlier in the SDLC
- Surface security requirements and a structured remediation plan
- Explore attacks the team might not have considered
- Inform later testing and contingency thinking without replacing those practices

## Adam Shostack Four-Question Frame

Keep these four questions top-of-mind throughout the work:

1. What are we working on?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good enough job?

## How to run a session

1. **Gather system information** — name, description, data sensitivity, scope and external interactions, primary workflows/use cases.
2. **Gather existing diagrams** — architecture, sequence, or other views that inform a Data Flow Diagram (DFD).
3. **Identify stakeholders / personas** (roles, not org charts):
   - **Developer** — deep design knowledge; already thinking about threats and mitigations.
   - **Business** — owns functional/non-functional outcomes; ensures mitigations do not gut requirements.
   - **Security** — applies security design/build/test practices; helps evaluate threats and controls.
   - **Infrastructure** — physical/virtual platform constraints and shared-responsibility boundaries.
   - **Coordinator** — process SME and discussion moderator; balances security vs delivery.
4. **Document current and upcoming work** — answers “What are we working on?”
5. **Enumerate threats with STRIDE** — apply STRIDE per **interaction** (data/control flows between components), then per **element** (databases, APIs, UIs, etc.). Classify leftover items as **unstructured** threats.
6. **Assess impact and likelihood** — confidentiality/integrity/availability and related consequences; attacker access, complexity, existing controls, motivation.
7. **Prioritize, assign owners, plan follow-up** — keep residual threats with owners and target dates; schedule revisit.
8. **Validate and refine** — re-review analysis and mitigations when the system changes.

## DFD building blocks

| Element | Meaning (paraphrased) |
| --- | --- |
| External entity | Outside system or actor that sends/receives data |
| Process | Transforms incoming data into output |
| Data store | Holds data for later use |
| Data flow | Path of information between entities, processes, and stores |
| Trust boundary | Place where data trust level changes (remote calls, DB reads, any user input) |
| Tuple | Slice of a flow by source, destination, and data type |

## Terms

| Term | Meaning (paraphrased) |
| --- | --- |
| Impact | Potential damage if the threat succeeds (direct or indirect) |
| Likelihood | Possibility the threat is carried out (difficulty, reward, conditions) |
| Controls | Safeguards to avoid, detect, counteract, or minimize threats |
| Preventions | Controls that can make an attack infeasible |
| Mitigations | Controls that reduce likelihood or impact without fully preventing the attack |
| Workflows / use cases | User-goal sequences describing how the system responds to requests |

## Other frameworks (pointers only)

- **PASTA** — Process for Attack Simulation and Threat Analysis; risk-centric, multi-step attack-simulation framing.
- **LINDDUN** — privacy-oriented threat modeling (linkability, identifiability, and related privacy properties).
- **Mozilla Rapid Risk Assessment (RRA)** — lightweight, agile prioritization of security risks.

## Supplemental (not threat-modeling methods)

- **CVSS** — vulnerability severity scoring to guide remediation urgency; not a threat-modeling method.
- **MITRE ATT&CK** — adversary TTPs useful **after** threats are identified; point at [`../mitre-attack/`](../mitre-attack/), do not recapture here. Not a compliance framework.

## Industry tools (names + URLs)

- OWASP Threat Dragon — <https://owasp.org/www-project-threat-dragon/>
- Microsoft Threat Modeling Tool — <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool>

## Advisory

Paraphrased from the CMS public handbook. Advisory only — not agent instructions, not this repo’s process, and not a substitute for authoritative upstream or a threat-model skill workflow.
