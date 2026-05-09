---
title: "GH Pages: synthesis candidates page listing tag-cluster groups"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: medium
blocks: []
tags: [static-site, synthesis, research-infrastructure, workflow]
started: ~
completed: ~
output: [tool]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# GH Pages: synthesis candidates page listing tag-cluster groups

## Research Question

What changes to `scripts/build_site.py` are needed to generate a synthesis candidates page that lists groups of completed items sharing three or more canonical tags, ranked by cluster size and average confidence, so that a reader can identify clusters ready for synthesis without reading every item?

## Scope

**In scope:**
- `docs/synthesis-candidates.html` page generation in `scripts/build_site.py`
- Cluster computation: groups of completed items sharing ≥3 canonical tags
- Ranking: by cluster size, then by average item confidence
- Cluster card layout: shared tags, item count, linked item titles, synthesise call-to-action
- Nav link added to all site pages
- Tests for cluster computation, threshold enforcement, ranking, nav presence

**Out of scope:**
- Changes to the synthesis workflow itself (W-0051)
- Triggering synthesis automatically from the candidates page
- Items in `Research/backlog/` or `Knowledge/` (completed items only)

**Constraints:** Tags must be canonical (depends on W-0043 and W-0053 being done); minimum cluster size threshold is 3 shared tags, not 3 items

## Context

The synthesis workflow (W-0051) exists but has no discovery mechanism. Without a synthesis candidates page, identifying which items cluster well requires manual inspection of all ~287 completed items. The page automates this discovery. It also makes the "next step" in the research pipeline visible to readers of the published site. Tracked in BACKLOG.md as W-0061.

## Approach

1. Define `compute_tag_clusters(items)`: for each unique tag triple, find all items sharing those tags; filter to clusters with ≥3 shared tags.
2. Rank clusters: primary key = cluster size, secondary key = mean confidence score.
3. Design cluster card HTML (shared tag pills, item list with links, call-to-action).
4. Add `generate_synthesis_candidates()` to `build_site.py` and wire it into the build pipeline.
5. Add "Synthesis Candidates" link to the shared nav template.
6. Write tests covering: correct grouping, threshold enforcement, deterministic ranking, nav presence in all page templates.

## Sources

- [scripts/build_site.py](https://github.com/davidamitchell/Research/blob/main/scripts/build_site.py) — current site generator to extend
- [docs/tag-vocabulary.md](https://github.com/davidamitchell/Research/blob/main/docs/tag-vocabulary.md) — canonical tag definitions (W-0043)
- [state/tag_report.md](https://github.com/davidamitchell/Research/blob/main/state/tag_report.md) — co-occurrence data (W-0053)

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
