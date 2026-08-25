---
doc_kind: reference
canonical_id: valid-sources-security-and-compliance
purpose: [reference, governance, research]
topics: [valid-sources, security, nist, mitre, owasp, cis, cisa]
advisory_only: true
---

# Authoritative Sources: Security and Compliance

## Purpose

Defines primary, authoritative documentation endpoints, control catalogs, and frameworks for cybersecurity, AI security, vulnerability databases, and regulatory compliance.

## Primary Source Registry

### National Institute of Standards and Technology (NIST)
- **NIST Cybersecurity Framework (CSF 2.0)**: `https://www.nist.gov/cyberframework`
- **NIST AI Risk Management Framework (AI RMF 1.0)**: `https://www.nist.gov/itl/ai-risk-management-framework`
- **NIST Computer Security Resource Center (CSRC)**: `https://csrc.nist.gov/publications/sp800`
- **NIST National Vulnerability Database (NVD)**: `https://nvd.nist.gov/`
- **Trust Tier**: Tier 1 (Standards Body)

### MITRE Corporation
- **MITRE ATT&CK Enterprise Matrix**: `https://attack.mitre.org/`
- **MITRE ATLAS (Adversarial Threat Landscape for AI Systems)**: `https://atlas.mitre.org/`
- **MITRE Common Weakness Enumeration (CWE)**: `https://cwe.mitre.org/`
- **MITRE Common Vulnerabilities and Exposures (CVE)**: `https://cve.mitre.org/`
- **Trust Tier**: Tier 1 (Standards Body)

### Open Web Application Security Project (OWASP)
- **OWASP Foundation**: `https://owasp.org/`
- **OWASP Top 10 Web Application Security Risks**: `https://owasp.org/Top10/2025/`
- **OWASP GenAI / LLM Top 10**: `https://genai.owasp.org/`
- **OWASP Application Security Verification Standard (ASVS)**: `https://owasp.org/www-project-application-security-verification-standard/`
- **Trust Tier**: Tier 1 (Standards Body)

### Center for Internet Security (CIS)
- **CIS Critical Security Controls (v8.1)**: `https://www.cisecurity.org/controls/v8-1`
- **CIS Benchmarks**: `https://www.cisecurity.org/cis-benchmarks`
- **Trust Tier**: Tier 1 (Standards Body)

### Cybersecurity and Infrastructure Security Agency (CISA)
- **Known Exploited Vulnerabilities (KEV) Catalog**: `https://www.cisa.gov/known-exploited-vulnerabilities-catalog`
- **CISA Cross-Sector Cybersecurity Performance Goals (CPGs)**: `https://www.cisa.gov/cpgs`
- **Trust Tier**: Tier 1 (Government Advisory Authority)

## Operational Usage

When citing security controls, threat tactics, or vulnerability IDs:
1. Always ground control IDs and tactic names in the corresponding official framework catalog.
2. Cross-verify against in-repo captures under [`../nist-csf/`](../nist-csf/), [`../nist-ai-rmf/`](../nist-ai-rmf/), [`../mitre-attack/`](../mitre-attack/), [`../mitre-atlas/`](../mitre-atlas/), [`../owasp/`](../owasp/), or [`../cis-controls/`](../cis-controls/).
3. Prohibit inventing synthetic control numbers or referencing third-party summaries that distort canonical definitions.
