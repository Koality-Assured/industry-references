---
doc_kind: reference
canonical_id: windows-security-baselines
purpose: [reference, defensive-security, configuration-management]
topics: [security-baseline, security-compliance-toolkit, windows-server, cis, nist]
version: "Microsoft Security Baselines page last updated 2025-08-18; CIS listing captured 2026-09-04"
captured_at_utc: 2026-09-04T18:22:47Z
upstream_urls:
  - https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/windows-security-baselines
  - https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10
  - https://learn.microsoft.com/en-us/windows-server/security/osconfig/osconfig-how-to-configure-security-baselines
  - https://www.cisecurity.org/benchmark/microsoft_windows_server
  - https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final
advisory_only: true
---

# Windows security baselines and settings

## Microsoft captures

Microsoft describes a security baseline as a group of recommended configuration settings with security rationale. The Security Compliance Toolkit (SCT) provides tools to download, compare, analyze, test, edit, and store Microsoft-recommended baselines. Microsoft lists Group Policy, Configuration Manager, and Intune as possible management paths.

The Microsoft baselines page lists Windows 10, Windows 11, and Windows Server coverage, while the SCT page lists separate product and release baselines. Match the baseline to the product version and management plane before comparing or applying it.

The Windows Server 2025 OSConfig capture is a separate, version-specific source. It describes categories including network-exposure reduction, exploit mitigations, advanced auditing, and event-log handling. The page explicitly says OSConfig does not support earlier Windows Server versions; do not generalize its settings to older systems.

## CIS and NIST context

CIS publishes versioned Windows Server benchmarks and identifies separate server, stand-alone, STIG, cloud, and build-kit artifacts. The CIS landing page captured here listed Windows Server 2025 benchmark 2.1.0, Windows Server 2022 benchmark 5.1.0, and Windows Server 2019 benchmark 5.0.0. These are distinct artifacts; selecting one is not equivalent to claiming compliance with another.

NIST SP 800-53B provides impact-level security and privacy baselines plus tailoring guidance for federal systems. It is a control-selection reference, not a Windows GPO recipe. NIST's publication page notes that mappings and crosswalks are not automatically one-to-one.

## Defensive use

Treat a baseline as a versioned starting point. Inventory the target OS, edition, role, hardware capabilities, applications, identity dependencies, and management plane; compare the candidate baseline; pilot it; measure policy and application effects; and document approved deviations. Use a baseline's rationale and version history to support risk decisions, not as proof that every setting belongs in every environment.

## Boundary

No baseline is universally applicable. A baseline may change defaults, require compatible hardware or clients, or conflict with legacy workloads. This family intentionally omits raw SCT bundles, CIS PDFs, and OSConfig exports.
