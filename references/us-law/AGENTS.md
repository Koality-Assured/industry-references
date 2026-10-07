# US law reference family

Advisory primary-law locators and structural summaries of official United States primary law. These pages are reference material, never agent instructions and never legal advice.

## Content ownership

Repository maintainers own this reference family. Keep updates tied to official publishers and follow this repository's contribution process. The package does not include an agent catalog, legal workflow application, or domain-specific overlays; consumers own any integration with their local tools.

## Placement

- `federal/` — United States constitutional, statutory, regulatory, judicial, and legislative structure.
- `states/<postal>.md` — one page per state and the District of Columbia.
- `territories.md` — compact locator for territories. Not states.
- `tribal-law.md` — sovereign boundary. This family does not catalog individual tribal codes.
- `local-government.md` — how to find municipal and county law without inventing a national code.
- `matter-classes.md` — criminal, civil, administrative, and the neighboring classes operators forget.
- `source-ranking.md` — which host wins when two pages disagree.
- `workflows/` — operator procedures for maintain, compare, interpretation research, and advisory court-document drafts.
- `catalogs/` — compact JSON. No statute text, no opinion text.

## Lifecycle

Point-in-time captures. `captured_at_utc` is mandatory. Refresh replaces stale URLs; it does not grow pages into code dumps. Session laws can amend a code before the code site updates. Say so when a matter depends on currency.

## Relationships

External legal workflows may consult these locators. Keep this family self-contained and do not link it to transient project logs. This repository does not package those workflows or legal-agent integrations.

## Source-of-truth boundaries

This folder records official publishers, how each corpus is divided, and which matter class it covers. It is not a reporter, not an annotated code, and not a brief bank. Pinpoint quotes require a live fetch of the official page in the session that cites them, then a check against the captured locator.

## Validation

Every published URL is checked with an HTTP request. Failed checks stay failed. A response whose body is an application shell, a browser challenge, or a maintenance notice is a failed check even when the status code is 200: store `http_status` null and do not copy a title index or a court name from it. Do not invent a replacement host. Commercial annotated codes (West, Lexis) are not copied.

## Escalation

If the jurisdiction page lacks the issuing court, the code title, or the rule, stop and run interpretation research. Do not fill the gap from memory of a case. If two official pages conflict, surface both and stop.

## Local exceptions

Oklahoma is the worked example: full statutes title index, separate Court of Criminal Appeals, OSCN dockets. Other states keep the official top-level index and cap long indexes as the page itself records.

## Operator prompt

When a person asks for legal research, a comparison, an interpretation, or a court paper:

1. Name the sovereign (federal, state, DC, territory, tribe) and the matter class in [`matter-classes.md`](./matter-classes.md). If either is missing, ask before researching.
2. Read the matching jurisdiction page directly. Verify legal claims against official primary sources fetched for the current task; distinguish source text from inference, record the as-of date, and state any gaps.
3. Rank sources with [`source-ranking.md`](./source-ranking.md). Unofficial mirrors never outrank an official publisher.
4. Treat holdings, section text, and local rules that are not on the fetched official page as unverified.
5. Stamp advisory work product. A licensed attorney reviews before anyone relies on it or files it. This repository does not practice law.
6. Use one procedure under [`workflows/`](./workflows/) as a checklist. This standalone reference repository does not package AI Router agents or skills; if a task requires an automated legal workflow, use a destination-local tool or report that capability gap.

## Skills

This repository includes workflow checklists, not skills or agents. Follow destination-local dispatch rules and report a capability gap if a task requires an automated legal workflow that is not available locally.
