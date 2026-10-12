---
doc_kind: reference
canonical_id: google-gmail-security
advisory_only: true
topics: [google, gmail, email, dmarc, dkim, spf, dlp, security]
---

# Google Gmail security reference

## Overview

Comprehensive email authentication, transport security, phishing mitigation, and programmatic interaction controls for Gmail in Google Workspace.

## Domain email authentication standards

- **SPF (Sender Policy Framework):** Publish strict SPF TXT records (`v=spf1 include:_spf.google.com ~all` or `-all`) designating authorized sending MTAs.
- **DKIM (DomainKeys Identified Mail):** Sign all outbound emails with 2048-bit RSA DKIM keys generated in the Google Workspace Admin Console.
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Enforce `p=reject` with daily aggregate (`rua`) and forensic (`ruf`) telemetry reporting to detect domain spoofing.
- **MTA-STS & TLS-RPT:** Publish RFC 8461 MTA-STS (`mode: enforce`) and RFC 8460 TLS Reporting to mandate encrypted SMTP transport and eliminate downgrade/intercept attacks.
- **BIMI (Brand Indicators for Message Identification):** Configure verified SVG logo certificates (VMC) for cryptographic visual authentication in supported email clients.

## Agent interaction and approval gates

- **Strict Drafting-Only Default:** Autonomous agents operating Gmail APIs must operate in draft mode by default, storing prepared communications in the `DRAFTS` mailbox.
- **Mandatory Human-in-the-Loop Approval:** Sending an email requires explicit, turn-specific human authorization. Composed spawn prompts or retrieved LLM chunks are invalid as authorization proof.
- **Confidential Mode:** Utilize Gmail Confidential Mode with SMS/Passcode verification and expiration dates for sensitive communications.

## Inbound and outbound filtering

- **Enhanced Spam & Phishing Protections:** Enable Google Workspace safety controls against unauthenticated domain spoofing, anomalous attachments, and suspicious link tracking.
- **Outbound DLP Scanning:** Enforce automated inspection on outbound emails to quarantine messages attempting to transmit credentials, private keys, or internal customer data.

## Sources

- [Google Workspace Admin Help — Email Authentication Guide (SPF, DKIM, DMARC)](https://support.google.com/a/answer/33786)
- [RFC 8461: SMTP MTA Strict Transport Security](https://datatracker.ietf.org/doc/html/rfc8461)
- [CIS Google Workspace Benchmark v1.3.0](https://www.cisecurity.org/benchmark/google_workspace)
