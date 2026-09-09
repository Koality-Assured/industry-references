---
doc_kind: reference
canonical_id: windows-security-mitre-ad-techniques
purpose: [reference, defensive-security, threat-modeling]
topics: [mitre-attack, active-directory, group-policy, credential-access, detection]
version: "MITRE ATT&CK Enterprise technique pages captured 2026-09-04"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://attack.mitre.org/techniques/T1484/
  - https://attack.mitre.org/techniques/T1484/001/
  - https://attack.mitre.org/techniques/T1003/
  - https://attack.mitre.org/techniques/T1558/
advisory_only: true
---

# MITRE ATT&CK AD-relevant techniques

MITRE ATT&CK is a threat-behavior reference. The entries below are compact defensive context for reviewing AD control-plane changes, credentials, and Kerberos telemetry; they do not authorize or describe reproducing adversary behavior.

- **T1484 — Domain or Tenant Policy Modification:** changes to centrally managed domain or identity policy can evade defenses or elevate privilege. Its Windows sub-technique **T1484.001 — Group Policy Modification** covers malicious GPO changes.
- **T1003 — OS Credential Dumping:** includes Windows-relevant sub-techniques for LSASS Memory, Security Account Manager, NTDS, LSA Secrets, Cached Domain Credentials, and DCSync.
- **T1558 — Steal or Forge Kerberos Tickets:** includes Golden Ticket, Silver Ticket, Kerberoasting, AS-REP Roasting, and Ccache Files.

## Defensive application

Use these IDs to organize review coverage: GPO and delegation change monitoring for T1484.001; replication-rights and privileged-access review for T1003.003/T1003.006; and Kerberos issuance, encryption, account, and ticket telemetry review for T1558. Always verify technique names and version metadata against the live MITRE entry before citing them in a report.
