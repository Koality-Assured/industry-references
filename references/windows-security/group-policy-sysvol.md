---
doc_kind: reference
canonical_id: windows-security-group-policy-sysvol
purpose: [reference, defensive-security, configuration-management]
topics: [group-policy, gpo, sysvol, dfsr, active-directory]
version: "Microsoft Learn Group Policy processing capture; page last updated 2025-06-16"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-processing
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-management-console
  - https://attack.mitre.org/techniques/T1484/001/
advisory_only: true
---

# Group Policy and SYSVOL

## Source-derived model

- A Group Policy Object (GPO) has components in both Active Directory and the domain controllers' SYSVOL folder. The two stores replicate through separate mechanisms: AD replication for directory data and DFS Replication (DFSR) for SYSVOL.
- Default processing begins with the local GPO, then site-linked, domain-linked, and OU-linked GPOs. Inheritance, link order, enforcement, security filtering, and WMI filtering can change which settings apply and which value wins.
- Computer policy is normally applied at startup and user policy at logon. Background refresh is periodic and randomized; a policy change may not be visible until the changed GPO has replicated to the domain controller serving the client.
- Loopback processing changes how user settings are selected based on the computer. Microsoft describes merge and replace modes and gives special-use computers as examples; it is not a generally safe default for every OU.

## Defensive checks

- Review who can modify GPOs, their links, filters, and the underlying SYSVOL content. Keep delegated write access narrowly scoped and subject to change control.
- Validate AD and SYSVOL replication independently after a change. A healthy directory replica does not by itself prove that the matching SYSVOL content is available everywhere.
- Use a representative test scope, then verify resultant policy on the intended computer and user populations. Record exceptions for legacy applications and special-purpose computers.
- Treat GPO backups and recovery procedures as privileged assets; protect them from unauthorized modification and test restoration in an isolated environment.

## ATT&CK context

MITRE ATT&CK T1484.001, Group Policy Modification, describes malicious GPO changes as a Windows privilege-escalation and defense-impairment path. The defensive implication is to monitor GPO permission and content changes and correlate them with unusual administrative activity. The ATT&CK entry is a threat reference, not an instruction to reproduce abuse.

## Boundary

Processing order, refresh intervals, and replication behavior are source-documented defaults or descriptions, not a promise about every topology or policy extension. Do not infer a safe GPO design without testing the actual forest, sites, OUs, clients, and applications.
