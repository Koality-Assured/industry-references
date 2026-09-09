---
doc_kind: reference
canonical_id: windows-security-audit-policy-event-logging
purpose: [reference, defensive-security, detection]
topics: [audit-policy, event-logging, windows-event-forwarding, log-management, incident-response]
version: "Microsoft audit/WEF captures; NIST SP 800-92 final 2006-09-13; NIST SP 800-53 release notice captured 2026-09-04"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations
  - https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection
  - https://csrc.nist.gov/pubs/sp/800/92/final
  - https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
advisory_only: true
---

# Audit policy and event logging

## Microsoft audit policy

Microsoft's audit-policy page presents baseline and stronger recommendations for Windows clients and servers. It labels settings as generally enabled, generally not enabled, conditional on a scenario or installed role, or domain-controller-specific. Microsoft says the tables are a starting baseline: administrators should choose, test, and modify policy based on threats, risk tolerance, and operational requirements.

The page distinguishes normal-security recommendations from stronger recommendations intended for more demanding threat conditions. This distinction is important when evaluating volume, privacy, performance, and analyst capacity; enabling more categories is not automatically a complete detection strategy.

## Windows Event Forwarding

Microsoft describes Windows Event Forwarding (WEF) as a mechanism that forwards selected operational or administrative events from devices to a Windows Event Collector. Its example model has baseline and suspect subscriptions. WEF is passive with respect to the source event log: it does not itself resize logs, enable disabled channels, change channel permissions, or configure audit policy. Event generation therefore must be established separately, including through suitable policy.

## NIST log-management context

NIST SP 800-92 is high-level guidance for establishing log-management infrastructure and robust organization-wide processes; it is not a step-by-step implementation guide. NIST SP 800-53 includes Audit and Accountability controls and related families, but its controls are flexible and risk-managed rather than a Windows event-ID checklist.

## Defensive use

Define the questions the logs must answer, enable only the channels and subcategories that support those questions, size and retain logs for the expected event rate, forward them to protected centralized storage, restrict access, monitor collection health, and test alerting and recovery. Account for domain controllers, member servers, workstations, application-specific channels, time synchronization, privacy, and retention obligations.

## Boundary

The source guidance does not establish one universal audit policy, event-log size, retention period, subscription, or alert threshold. Any event-ID or setting selection must be validated against the target Windows release, role, workload, and detection objectives.
