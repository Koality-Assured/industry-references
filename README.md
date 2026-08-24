# Koality-Assured Industry References

Normalized, machine-readable catalogs, mappings, and practitioner guides for industry cybersecurity and engineering frameworks.

## Mission Statement

Provide centralized, verified, machine-readable reference schemas and guides for industry engineering and cybersecurity frameworks.

## Architecture Overview

This repository maintains normalized catalogs and mappings across leading international frameworks.

### Catalogs & Frameworks Included

- **OWASP**: Agentic Top 10 (2026), ASVS 5.0, LLM Top 10 mappings
- **MITRE ATT&CK**: Enterprise Matrix v19.1 tactics, techniques, and sub-techniques
- **MITRE ATLAS**: Adversarial Threat Landscape for AI Systems (2026.07)
- **NIST CSF**: Cybersecurity Framework 2.0 Core functions, categories, and subcategories
- **NIST AI RMF**: Artificial Intelligence Risk Management Framework 1.0 Core & GenAI Profile
- **CWE**: Common Weakness Enumeration v4.20 and CWE Top 25 (2025/2026)
- **Conventional Commits**: Standard specification v1.0.0 for structured git messages

## Validation & Testing

```bash
python tools/validator.py --all
python -m unittest discover -s tests -v
```

## Security Notice

All framework catalogs are verified against upstream specifications and maintained for agent and automation integration.

## License

MIT License Copyright (c) 2026 Koality-Assured.
