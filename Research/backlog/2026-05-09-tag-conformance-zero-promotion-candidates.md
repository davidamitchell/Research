---
title: "Tag conformance: canonicalise full corpus to zero promotion candidates"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: high
blocks: []
tags: [research-infrastructure, workflow, evaluation]
started: ~
completed: ~
output: [tool, knowledge]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: high
versions: []
---

# Tag conformance: canonicalise full corpus to zero promotion candidates

## Research Question

What steps are needed to bring all tags across `Research/completed/` and `Research/backlog/` into full conformance with `docs/tag-vocabulary.md`, such that running `scripts/tag_report.py` produces zero near-duplicate and zero singleton-promotion candidates?

## Scope

**In scope:**
- Running `scripts/canonicalise_tags.py` against the full corpus
- Identifying tags not yet in `docs/tag-vocabulary.md` and either adding them or rewriting them
- Re-running `scripts/tag_report.py` until the report is clean
- Triggering `tag-review.yml` to confirm clean state
- Committing the canonical state

**Out of scope:**
- Redesigning the tag vocabulary structure (W-0043 is done)
- Changes to `scripts/tag_report.py` or `scripts/canonicalise_tags.py` logic (those are W-0043/W-0053)
- Tags in `Research/in-progress/` or `Knowledge/`

**Constraints:** W-0043 (canonical vocabulary defined) and W-0053 (tag report script) must be done before this slice can start; both are done.

## Context

W-0043 defined the canonical tag vocabulary and W-0053 built the tag report script. The corpus has continued to accumulate new items since those slices were completed, and the canonicalisation script has not been run to completion since then. This slice closes the loop: running canonicalisation end-to-end until the report shows a green state. Tracked in BACKLOG.md as W-0062.

## Approach

1. Run `scripts/tag_report.py` to get the current state of near-duplicate and singleton candidates.
2. For each near-duplicate cluster: decide canonical form and add to `docs/tag-vocabulary.md` if not present; then run `scripts/canonicalise_tags.py`.
3. For each singleton: decide whether to promote to canonical or merge with an existing canonical form.
4. Re-run `scripts/tag_report.py` after each batch of changes; iterate until zero candidates remain.
5. Trigger `tag-review.yml`; confirm the workflow closes with no open issues.
6. Commit with message `tags: canonicalise full corpus — zero promotion candidates`.

## Sources

- [scripts/tag_report.py](https://github.com/davidamitchell/Research/blob/main/scripts/tag_report.py) — tag report script (W-0053)
- [scripts/canonicalise_tags.py](https://github.com/davidamitchell/Research/blob/main/scripts/canonicalise_tags.py) — canonicalisation script (W-0043)
- [docs/tag-vocabulary.md](https://github.com/davidamitchell/Research/blob/main/docs/tag-vocabulary.md) — canonical vocabulary (W-0043)
- [state/tag_report.md](https://github.com/davidamitchell/Research/blob/main/state/tag_report.md) — current tag report (W-0053)

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
