---
title: "Structural audit and correction of all completed research items"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: high
blocks: []
tags: [research-infrastructure, evaluation, workflow]
started: ~
completed: ~
output: [tool, knowledge]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Structural audit and correction of all completed research items

## Research Question

What is the current structural quality of completed items in `Research/completed/`, and what targeted corrections are needed so that every item has valid frontmatter, complete required sections, canonical citation format, and no hollow filler prose?

## Scope

**In scope:**
- All ~287 items in `Research/completed/`
- Checks: required frontmatter fields present and non-null, `status: completed`, `output:` non-empty, `## Findings` non-empty, `## Sources` with ≥1 URL, no hollow filler phrases, citations in canonical suffix format
- A `scripts/item_audit.py` script automating the checks
- Corrections applied in-place with `versions:` entries for each corrected item

**Out of scope:**
- Items in `Research/backlog/` or `Research/in-progress/`
- Substantive changes to findings content (structural corrections only)
- Replacing the research-reviewer skill evaluation (W-0066)

**Constraints:** `versions:` entry must be added before committing corrections; `sha` field is populated after the commit. Citation format depends on `docs/citation-standards.md` existing (W-0067).

## Context

The corpus has grown to ~287 completed items, many produced before current quality standards were established. Structural inconsistencies degrade the published site and undermine the quality signal from `research-review.yml`. A systematic automated audit is the only practical way to find failures at this scale. Tracked in BACKLOG.md as W-0063.

## Approach

1. Implement `scripts/item_audit.py`: checks all required frontmatter fields, non-empty sections, citation format, and hollow-prose vocabulary list.
2. Run audit and generate `state/item_audit.json` and `state/item_audit.md` summary.
3. Triage findings: classify failures by type and frequency; prioritise structural fixes over prose rewrites.
4. Apply corrections in batches by failure type; add `versions:` entry to each corrected item.
5. Re-run audit until all items pass; commit clean state.
6. Write tests covering: audit identifies known failures in fixture items; corrected items pass re-audit; `versions:` entry format is valid.

## Sources

- [Research/_template.md](https://github.com/davidamitchell/Research/blob/main/Research/_template.md) — canonical field and section definitions
- [.github/skills/remove-ai-slop/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/remove-ai-slop/SKILL.md) — hollow-prose vocabulary reference
- [docs/citation-standards.md](https://github.com/davidamitchell/Research/blob/main/docs/citation-standards.md) — citation format reference (W-0067, to be created)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item.)*

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

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

- Type:
- Description:
- Links:
