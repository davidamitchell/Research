---
title: "How do academic and scientific publishing systems handle post-publication corrections, amendments, retractions, and commentary, and what is the minimal viable analogue for a versioned git-based research corpus?"
added: 2026-04-27T06:20:00+00:00
status: backlog
priority: high
blocks: []
tags: [academic-publishing, post-publication, corrections, retractions, amendments, rebuttal, immutability, versioning, knowledge-management, research-methodology, doi, corrigendum, erratum]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# How do academic and scientific publishing systems handle post-publication corrections, amendments, retractions, and commentary, and what is the minimal viable analogue for a versioned git-based research corpus?

## Research Question

How do established academic and scientific publishing systems (journal publishers, preprint servers, living review platforms) handle post-publication corrections, amendments, retractions, and formal commentary — and what is the minimal viable analogue for a versioned, git-based private research corpus where completed items should be treated as immutable records with narrow, explicitly defined exceptions?

## Scope

**In scope:**
- The four main post-publication update mechanisms in academic publishing: corrigenda/errata (corrections), retractions (invalidations), comments and replies (formal challenges and responses), and living reviews (continuously updated systematic reviews)
- The structural conventions used: how corrections are physically attached to the original record, what metadata fields change, what signals readers (and indexing systems) receive
- Preprint server versioning (arXiv, bioRxiv): how version history is preserved and surfaced, what constitutes a "new version" vs a "new paper"
- The distinction between acceptable silent corrections (typos, broken URLs) and corrections that require a formal record (factual claim changes, methodology changes, finding reversals)
- Cochrane Reviews as the gold standard for living systematic reviews: update protocol, versioning, what triggers an update vs a new review
- The practical minimum: what the smallest viable amendment mechanism looks like for a git-backed, Markdown-based corpus — specifically, what must be structured data (frontmatter fields) vs what can remain prose

**Out of scope:**
- Legal aspects of retractions (libel, misconduct investigations)
- Full systematic review methodology (PRISMA, GRADE) — only the update/amendment protocol is in scope
- Publisher-specific proprietary systems (CrossRef mechanics, DOI redirect infrastructure)
- Any mechanism requiring a database or external service — the target implementation is pure git + Markdown

**Constraints:**
- Primary sources preferred: publisher guidelines, COPE (Committee on Publication Ethics) guidelines, actual retraction notices, arXiv versioning documentation
- The output must include a specific recommendation for the amendment frontmatter schema and amendment item template for this repo (a direct input to W-0038 in BACKLOG.md)

## Context

This item directly informs the implementation of the research immutability protocol (repo improvement W-0038). The design principle is that completed research items should not be silently edited — the record of what was believed at a point in time is itself valuable, and silent edits destroy provenance. Academic publishing has solved this problem at scale. Before designing a bespoke mechanism, it is worth understanding what the established patterns are, why they are structured as they are, and what the minimal viable version looks like for a much smaller, private, git-backed corpus. The output of this item feeds directly into W-0038 scoping.

## Approach

1. **Corrigendum/erratum mechanics**: Survey 3–5 major journal publishers (Nature, Science, PLOS ONE, BMJ, IEEE) for their published correction policies. What triggers a corrigendum vs an erratum? What is physically published? How is it linked to the original? What metadata changes?
2. **Retraction mechanics**: Survey the Retraction Watch database and COPE retraction guidelines. What constitutes a retraction vs a correction? What is the minimum retraction notice? Is the original removed or marked? What fields change?
3. **Comment and reply mechanics**: Survey how journals handle formal post-publication commentary (letters to the editor, technical comments, invited replies). What is the structural relationship between comment and original? How are they indexed?
4. **Living reviews**: Survey Cochrane Reviews update protocol and at least one other living review format (e.g., Living Evidence Network). What triggers an update? What is preserved from prior versions? What is the versioning convention?
5. **Preprint versioning**: Survey arXiv and bioRxiv versioning. What is preserved between versions? What triggers a new version? How are citations to earlier versions handled?
6. **Minimal viable analogue**: Based on the above, define the minimal set of mechanisms needed for a git-backed Markdown corpus. Specifically: what frontmatter fields are needed, what file naming convention for amendment items, what the amendment item template must contain, and what the three acceptable silent-edit exceptions are (broken URLs, tag updates, citation URL fixes).
7. **Synthesis**: Produce a schema recommendation and amendment item template as the primary output — a direct input to W-0038.

## Sources

- [ ] [COPE (Committee on Publication Ethics) — Retraction Guidelines](https://publicationethics.org/retraction-guidelines) — primary source for retraction standards and triggers
- [ ] [COPE — Correction Guidelines](https://publicationethics.org/cope-guidelines-retracting-articles) — primary source for correction standards
- [ ] [Retraction Watch](https://retractionwatch.com/) — empirical data on retraction patterns and notices
- [ ] [arXiv — Submission and revision help](https://info.arxiv.org/help/submit/index.html) — versioning mechanics for preprint server
- [ ] [bioRxiv — About versioning](https://www.biorxiv.org/content/about-biorxiv) — versioning mechanics for life sciences preprint server
- [ ] [Cochrane — Updating Cochrane Reviews policy](https://www.cochranelibrary.com/about/about-cochrane-reviews) — gold standard for living systematic review update protocol
- [ ] [Nature — Corrections and retractions policy](https://www.nature.com/nature-portfolio/editorial-policies/corrections-and-retractions) — major journal primary policy
- [ ] [PLOS ONE — Corrections policy](https://journals.plos.org/plosone/s/corrections-and-retractions) — open-access journal primary policy
- [ ] [BMJ — Corrections policy](https://www.bmj.com/about-bmj/resources-authors/forms-policies-and-checklists/corrections) — medical journal primary policy

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge, backlog-item
- Description: Amendment schema recommendation and item template (feeds W-0038)
- Links:
