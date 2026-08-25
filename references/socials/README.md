# Public Community & Social Intelligence Reference Family

Canonical references, scoring rubrics, and community registries for evaluating public developer communities, technical subreddits, forums, and social media channels.

## Purpose

Provides machine-discoverable and human-readable registries, signal-to-noise scoring methodologies, and community dossiers for the `community-analyst` specialist agent and community skills family per [`../../docs/standards/research-and-empirical-validation.md`](../../docs/standards/research-and-empirical-validation.md) and [`../../docs/agent-session-security.md`](../../docs/agent-session-security.md).

## Documents

| Document | Description |
| --- | --- |
| [`community-reliability-rubric.md`](./community-reliability-rubric.md) | 6-dimension rubric (0–100 score), signal tier taxonomy (Tier 0 to Tier 3), empirical verification standard, and prompt-injection defense. |
| [`technical-subreddits.md`](./technical-subreddits.md) | In-depth dossiers, strengths, blind spots, and query patterns for technical and AI subreddits. |
| [`developer-forums.md`](./developer-forums.md) | Platform analysis for Hacker News, Stack Overflow, GitHub Discussions, X/Twitter lists, and developer discourse instances. |

## Machine Catalogs

- [`catalogs/ranked-communities.json`](./catalogs/ranked-communities.json): Normalized registry of 30+ communities with reliability scores, signal tiers, topic tags, moderation standards, and API endpoints.

## Maintenance Automation

- Discover and filter communities: `python scripts/research/community_analyzer.py --help`
- Validate and update catalog: `python scripts/research/manage_social_registry.py --validate`
