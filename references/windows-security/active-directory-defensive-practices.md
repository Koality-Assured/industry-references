---
doc_kind: reference
canonical_id: windows-security-active-directory-defensive-practices
purpose: [reference, defensive-security, identity]
topics: [active-directory, ad-ds, domain-controllers, privileged-access, recovery]
version: "Microsoft Learn captures; source pages apply Windows Server 2016-2025"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/reducing-the-active-directory-attack-surface
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/securing-domain-controllers-against-attack
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/planning-for-compromise
advisory_only: true
---

# Defensive Active Directory practices

## Scope

Microsoft describes Active Directory Domain Services (AD DS) as a high-value control plane. This capture summarizes defensive themes from Microsoft's AD security guidance; it is not a deployment standard or a forest-recovery runbook.

## Source-derived themes

- Reduce exposure around privileged accounts, domain controllers, and other identity or configuration-management infrastructure. Microsoft calls out permanent privilege, privileged-account use on untrusted systems, excessive privileged-group membership, and weak domain-controller management as recurring risks.
- Separate administration of domain controllers from general systems management and keep software installed on domain controllers to the minimum required for their role.
- Restrict browser and general internet access to domain controllers according to the organization's operating model. Microsoft distinguishes hybrid/cloud-protected deployments from environments that must remain on-premises only.
- Monitor sensitive AD objects and Windows events for signs of compromise. Microsoft points to legacy audit categories, audit subcategories, and Advanced Audit Policy as possible mechanisms, with the appropriate choice depending on the environment.
- Plan for compromise and recovery before an incident. Microsoft's “secure cell” and pristine-forest discussion is a planning concept for isolating critical assets and legacy dependencies, not a claim that every organization should rebuild its forest.

## Defensive use

Use this capture to frame an AD review around privileged access, administrative-host separation, domain-controller exposure, monitoring, lifecycle ownership, and recovery readiness. Pair it with the relevant Windows version's security baseline and local business, regulatory, and compatibility requirements.

## Boundary

The source pages provide broad recommendations and link to more detailed guidance. They do not establish a universal set of GPO links, firewall rules, account tiers, or recovery timings. Test and document any local implementation.
