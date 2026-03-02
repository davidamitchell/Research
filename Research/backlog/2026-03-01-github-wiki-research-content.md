---
title: "GitHub wiki for research content: approach and tooling"
added: 2026-03-01
status: backlog
priority: medium
tags: [wiki, github, delivery, interface, output]
started: ~
completed: ~
output: [tool, knowledge, backlog-item]
---

# GitHub wiki for research content: approach and tooling

## Research Question

What is the best approach for publishing completed research items from `Research/completed/` into the GitHub wiki, and what tooling is needed to keep it current and readable?

## Scope

**In scope:**
- How the GitHub wiki is structured and how pages are created/updated
- Automated pipeline options: GitHub Actions workflow to publish research on merge/push
- Format translation: Markdown front-matter stripping, index page generation, per-item wiki pages
- Navigation: tag-based index, date-sorted index, topic grouping

**Out of scope:**
- Full static site (Jekyll, MkDocs, etc.) — the question is specific to GitHub wiki
- Email digest or MCP server delivery (covered by `2026-02-27-interface-and-delivery.md`)

**Constraints:** The owner uses GitHub website and iOS app only; any publish step must be fully automated via GitHub Actions with no local tooling required.

## Context

Research outputs accumulate in `Research/completed/` as Markdown files with YAML front-matter. They are well-structured for agents and git history, but not easily browsable by a human reader on mobile or web. The GitHub wiki is natively accessible from the repository's **Wiki** tab on both the GitHub website and iOS app, requires no separate hosting, and renders Markdown directly. Converting research content to wiki pages would improve day-to-day readability at zero infrastructure cost.

The existing `2026-02-27-interface-and-delivery.md` backlog item covers the broader interface question; this item is specifically scoped to the GitHub wiki delivery path, which the owner has explicitly prioritised.

## Approach

1. Survey GitHub wiki constraints: page naming rules, directory support, sidebar/footer customisation, API access, and Actions permissions needed to push to the wiki repo.
2. Design the publish pipeline: which files are published (completed only vs in-progress too), how front-matter is stripped, how the index page is generated, and when the workflow runs (push to main, nightly schedule, or manual dispatch).
3. Prototype: implement a minimal GitHub Actions workflow that publishes one completed research item to the wiki and generates an index page.
4. Evaluate ongoing maintenance: how to handle renames, deletions, and updates; whether a full-rebuild or incremental approach is simpler given the volume.
5. Produce a `BACKLOG.md` item for the implementation slice if the prototype validates the approach.

## Sources

- [ ] GitHub Docs — Wikis: https://docs.github.com/en/communities/documenting-your-project-with-wikis
- [ ] GitHub Actions — checkout wiki repo pattern (common community pattern using `actions/checkout` with wiki URL)
- [ ] `davidamitchell/Research` wiki tab — current state (empty or populated?)
- [ ] Existing similar repos that auto-publish to GitHub wiki via Actions

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

- Type: tool, knowledge, backlog-item
- Description: GitHub Actions workflow for wiki publishing; index page template; implementation backlog slice
- Links:
