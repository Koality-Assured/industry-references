---
doc_kind: reference
canonical_id: slack-security-baseline
purpose: [reference]
rank: high
advisory_only: true
topics: [slack, security, baseline, cis, oauth, compliance]
rag_keywords: [slack-security, cis-slack, audit-logs, sso, scim, encryption, ekm]
---

# Slack security baseline reference

## Overview

Advisory security controls, hardening baselines, and architectural benchmarks for Slack enterprise workspaces and integrations. Grounded in the CIS Slack Benchmark, NIST SP 800-63 Digital Identity Guidelines, and official Slack Security architecture.

## Identity and access management controls

- **SAML 2.0 Single Sign-On (SSO):** Enforce IdP federation with hardware-bound MFA (FIDO2). Disable password-based logins for standard members.
- **SCIM Lifecycle Management:** Automate user provisioning, profile synchronization, and immediate deactivation upon employee offboarding.
- **Session Duration:** Enforce maximum session lifetimes (e.g., 24 hours or 12 hours) and terminate inactive mobile/desktop sessions.
- **Enterprise Mobility Management (EMM):** Require approved mobile device management (MDM) profiles with app configuration policies blocking clipboard export of sensitive data on unmanaged mobile devices.

## Application and integration governance

- **App Approval Mode:** Mandate workspace administrator approval prior to enabling any third-party app or custom integration.
- **Granular Bot Scopes:** Disallow monolithic legacy scopes (`bot`, `client`). Require modern granular OAuth scopes (`chat:write`, `commands`, `incoming-webhook`, `channels:read`).
- **Domain Restricted Sharing:** Restrict external Slack Connect channels and direct messages to vetted, allowlisted partner domains. Block arbitrary public file sharing.
- **Token Secret Storage:** Restrict storage of Slack tokens (`xoxb-`, `xoxp-`, `xapp-`, webhooks) strictly to secure secret vaults and ephemeral runtime environment variables.

## Data protection and cryptography

- **Enterprise Key Management (Slack EKM):** In Enterprise Grid environments, integrate customer-managed AWS KMS keys for granular encryption of messages and files with instant revoke capabilities.
- **Data Loss Prevention (DLP):** Connect DLP inspection tools via Slack Discovery APIs to scan for credentials, PII, and sensitive source code in real time.
- **Audit Logs Ingestion:** Stream all administrative and access events via the Slack Audit Logs API v2 (`/api/v2/audit/logs`) directly into SIEM pipelines for threat detection.

## Sources

- [CIS Slack Benchmark](https://www.cisecurity.org/benchmark/slack)
- [Slack Enterprise Security Whitepaper](https://slack.com/security)
- [NIST SP 800-63-4 Digital Identity Guidelines](https://csrc.nist.gov/pubs/sp/800/63/4/final)
