---
title: "GH Pages: render item metadata fields as structured, human-readable content"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: medium
blocks: []
tags: [static-site, research-infrastructure, workflow]
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

# GH Pages: render item metadata fields as structured, human-readable content

## Research Question

What changes to `scripts/build_site.py` are needed so that each completed research item's individual page renders `confidence`, `item_type`, `cites`, `related`, and `superseded_by` as structured, human-readable content rather than omitting them or showing raw YAML frontmatter?

## Scope

**In scope:**
- Individual item page rendering in `scripts/build_site.py`
- Metadata fields: `confidence`, `item_type`, `cites`, `related`, `superseded_by`
- Slug-to-URL resolution for `cites` and `related` lists
- Visual deprecation indicator for `superseded_by`
- Omitting null/empty fields from rendered output
- Tests for the metadata panel

**Out of scope:**
- Adding new frontmatter fields to the item schema
- Changes to the tag pages or the all-items index
- The synthesis candidates page (tracked in W-0061)

**Constraints:** Must not break existing item page rendering; must use the existing site design language (badges, colour conventions)

## Context

Current individual item pages show only the Markdown body. Readers cannot see relationship metadata (`cites`, `related`, `superseded_by`) or quality signals (`confidence`, `item_type`) without accessing the raw file on GitHub. Making these fields visible enables readers to assess item quality, trace citation chains, and navigate the corpus from the published site. This is tracked in BACKLOG.md as W-0060.

## Approach

1. Audit which fields are currently rendered on individual item pages and which are silently dropped.
2. Design the metadata panel layout (sidebar or header section) consistent with the existing site design.
3. Implement `render_item_metadata_panel()` in `build_site.py` covering all five fields.
4. Resolve slug lists (`cites`, `related`) to hyperlinks; handle missing targets gracefully.
5. Add a deprecation indicator when `superseded_by` is non-null.
6. Write tests covering: correct labels, slug resolution, null-field omission, deprecation indicator.

## Sources

- [GitHub Pages static site generator — scripts/build_site.py](https://github.com/davidamitchell/Research/blob/main/scripts/build_site.py) — current implementation to extend
- [Research item template — Research/_template.md](https://github.com/davidamitchell/Research/blob/main/Research/_template.md) — canonical field definitions

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
