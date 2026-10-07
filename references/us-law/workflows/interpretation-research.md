---
doc_kind: process
canonical_id: us-law-workflow-interpretation
purpose: [process]
topics: [us-law, research]
rag_keywords: [us-law-interpretation-research, holding, persuasive-authority]
rank: high
---

# Research interpretations of US law

This checklist is advisory guidance for human or destination-local research workflows. Return the memo in-session by default; write a file only when requested and under the destination repository's output rules.

## When to use

The person asks what a constitution, statute, regulation, or opinion means, or how a court has applied it.

## When not to use

Locator maintenance (`maintain.md`). A yes-or-no check against an existing page (`compare.md`). A complaint or motion skeleton (`court-document-draft.md`).

## Criticality

High. A holding is the court's decision on the facts before it. Commentary, dissents, headnotes, and AG opinions are not holdings. Label each one.

## Source of truth

Use [`../source-ranking.md`](../source-ranking.md) and the jurisdiction page to locate sources. Fetch and cite official primary sources for the current task, separate verified holdings from inference or publisher summaries, and state the as-of date and any unresolved gaps.

## Isolation

Read the corpus first. Fetch official texts needed for the memo. Write a dossier only when the person asks for a durable research artifact.

## How to use

1. State the sovereign, the matter class, the legal question, and the as-of date.
2. Read in this order, and only sources fetched this session or already captured as official: constitutional text, statute, session law if the code may lag, regulation, binding court of that sovereign, then persuasive material labeled persuasive.
3. For a case, record the court, date, docket or official citation if the fetched page prints one, the URL, and separate the holding from any dissent or publisher summary.
4. Legislative history comes from an official congressional or legislative source. If Congress.gov returns 403, use a GovInfo or legislature page that resolves, or mark legislative history unverified.
5. Stop when the official text does not answer the question. Say what was not found.
6. Stamp the memo advisory. Attorney review. Not legal advice. Not a filing.

## Dry run

Pick one federal rule family from the inferior-courts page and list which official URL would be fetched. Do not write a memo.

## Security

No sealed records, no PACER credential use, no bulk download of opinions into git. Store the locator and the memo, not the opinion archive.

## Completion gates

Return the memo in-session unless the user asks for a file; if writing one, use the destination repository's documented output convention. Promote a stable publisher correction into `references/us-law/` through the repository's normal contribution review, not by pasting a research memo into a jurisdiction page.
