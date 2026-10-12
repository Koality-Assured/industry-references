---
doc_kind: reference
canonical_id: windows-security-identity-protocol-hardening
purpose: [reference, defensive-security, identity]
topics: [ldap, ldap-signing, channel-binding, smb, kerberos, ntlm]
version: "Microsoft Windows Server 2025 protocol-hardening captures; compatibility guidance captured 2026-09-04"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing
  - https://learn.microsoft.com/en-us/windows-server/identity/manage-ldap-signing-group-policy
  - https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security-hardening
  - https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing
  - https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-signing-overview
  - https://csrc.nist.gov/pubs/sp/800/63/4/final
  - https://attack.mitre.org/techniques/T1558/
  - https://attack.mitre.org/techniques/T1003/
advisory_only: true
---

# Identity and protocol hardening

## LDAP signing and channel binding

Microsoft distinguishes LDAP signing, which protects the integrity and authenticity of LDAP messages, from LDAP channel binding, which binds an application security context to the underlying TLS session. Together they address tampering, replay, and session-hijacking risks.

The Microsoft Server 2025 guidance says new AD deployments require LDAP signing by default, while upgrades preserve existing policies to avoid disruption. It also describes channel binding as “When supported” by default for new Server 2025 deployments. The companion Group Policy page recommends identifying unsigned-bind clients and moving from compatibility settings toward enforcement only after client validation. Directory Service events such as 2887, 2889, 3039, and 3040 are cited as compatibility and monitoring signals.

Do not copy these defaults across releases or assume that an upgrade has the same state as a new deployment. Inventory clients, libraries, certificates, proxies, and applications first; stage changes; monitor failures; and retain an explicit exception and retirement plan for legacy clients.

## SMB signing and SYSVOL

Microsoft describes SMB signing as message integrity and peer-authentication protection that helps resist tampering and relay/spoofing attacks. The SMB security-hardening page reports that Windows 11 24H2 and Windows Server 2025 require signing by default for all inbound and outbound SMB connections, while the separate control-behavior page's version matrix describes Windows Server 2025 as requiring outbound signing. The SMB overview also notes that domain controllers require signing for connections commonly used for SYSVOL and NETLOGON.

This is an official-source discrepancy, not a reason to guess. Verify the exact Windows build, client/server direction, policy state, and effective configuration in the target environment before documenting or changing the requirement.

These are release- and direction-specific behaviors. Check the exact client/server versions and third-party file-server capabilities before changing requirements. Microsoft warns against disabling signing merely as a workaround for an incompatible third-party server.

## Kerberos and credential protection context

MITRE ATT&CK T1558 covers theft or forgery of Kerberos tickets, including Golden Ticket, Silver Ticket, Kerberoasting, and AS-REP Roasting. T1003 covers OS credential dumping, including LSASS memory, NTDS, DCSync, and cached domain credentials. Use these entries to structure detections and privilege reviews; they are not implementation instructions.

NIST SP 800-63-4 is a digital-identity guideline for identity proofing, authentication, and federation. It supersedes SP 800-63-3 and is broader than on-premises AD protocols, so use it as identity-assurance context rather than a direct GPO mapping.

## Boundary

Protocol hardening can break legacy clients and change interoperability. This capture intentionally avoids declaring a single LDAP, SMB, Kerberos, NTLM, cipher, or channel-binding configuration safe for every Windows estate.
