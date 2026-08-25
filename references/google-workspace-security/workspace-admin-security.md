---
doc_kind: reference
canonical_id: google-workspace-admin-security
topics: [google, workspace, admin, sso, mfa, dlp, zdr, governance]
---

# Google Workspace administration security reference

## Overview

Comprehensive administrative security best practices and compliance perimeters for Google Workspace enterprise tenants.

## Identity and access management

- **Single Sign-On (SSO):** Federate Google Workspace with enterprise IdP (Okta, Entra ID, Ping) via SAML 2.0. Enforce domain-wide SSO while maintaining a designated emergency break-glass administrator.
- **Phishing-Resistant 2FA:** Mandate FIDO2 / WebAuthn hardware security keys or device-bound passkeys. Disable SMS and voice-based 2FA across all administrative accounts.
- **SCIM Automated Deprovisioning:** Integrate automated user provisioning and deprovisioning via SCIM to eliminate orphaned active accounts after employee departures.
- **Context-Aware Access (CAA):** Define Zero Trust access rules based on user identity, device compliance state, IP location, and OS version.

## Zero data retention and AI governance

- **Enterprise Data Protection Terms:** Verify enterprise terms for Gemini for Google Workspace ensuring prompt content, documents, and emails are not used to train foundation models.
- **Zero Data Retention (ZDR):** Enforce zero prompt caching and retention policies where enterprise add-ons are enabled.
- **Data Locality:** Configure Google Workspace Data Regions to enforce geographic data residency for primary data at rest (e.g., United States or European Union).

## Data Loss Prevention (DLP) and sharing perimeters

- **DLP Rule Engines:** Implement automated DLP rules scanning Gmail and Drive for API keys, private keys, PII (SSN, credit cards), and proprietary classification markers.
- **Third-Party App Allowlisting:** Set Marketplace app installation policy to "Admin Allowlist Only". Block arbitrary OAuth token grants requesting broad scopes (`mail.google.com`, `drive`).
- **Audit Logging Export:** Stream administrative audit logs, Drive activity logs, and login audit logs to central Google Cloud BigQuery or external SIEM in real-time.

## Sources

- [Google Workspace Admin Help — Security Checklist for Medium and Large Businesses](https://support.google.com/a/answer/7587183)
- [CIS Google Workspace Benchmark v1.3.0](https://www.cisecurity.org/benchmark/google_workspace)
