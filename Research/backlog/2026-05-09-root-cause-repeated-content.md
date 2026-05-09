---
title: "Root cause investigation: repeated or near-identical content across generated pages and completed items"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: medium
blocks: []
tags: [research-infrastructure, static-site, evaluation, workflow]
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

# Root cause investigation: repeated or near-identical content across generated pages and completed items

## Research Question

What is the root cause of repeated or near-identical content appearing across generated site pages or completed research items, and what targeted changes to the site generator, item template, or research prompt are needed to prevent new items from reproducing the pattern?

## Scope

**In scope:**
- Pairwise similarity analysis of `## Findings` sections across `Research/completed/`
- Three candidate root causes: (a) `research-prompt.md` boilerplate copied verbatim by agents, (b) `Research/_template.md` placeholder text surviving into completed items, (c) `build_site.py` duplicating content blocks across pages
- A `scripts/similarity_report.py` script producing `state/similarity_report.md`
- Fixes applied to whichever root causes are confirmed
- An ADR if a structural change to the template or prompt is made

**Out of scope:**
- Substantive rewrites of completed item findings (structural corrections are W-0063)
- Tag-level deduplication (W-0043, W-0053, W-0062)
- Near-duplicate item merging

**Constraints:** Similarity threshold for flagging is 0.85 cosine similarity on TF-IDF of `## Findings` text; items with identical research questions are expected to have high similarity and should be noted but not treated as a defect.

## Context

Repeated content across completed items reduces the signal-to-noise ratio of the corpus and can inflate synthesis candidate clusters with false positives (items sharing text rather than concepts). Identifying and fixing the root cause is a prerequisite for trusting the synthesis candidates page (W-0061) and the structural audit (W-0063). Tracked in BACKLOG.md as W-0064.

## Approach

1. Implement `scripts/similarity_report.py`: TF-IDF on `## Findings` sections, pairwise cosine similarity, flag pairs above 0.85 threshold, output to `state/similarity_report.md`.
2. Inspect flagged pairs: categorise by root cause (prompt boilerplate, template placeholder, site generator duplication).
3. For confirmed root causes: fix the prompt, template, or site generator; document the fix.
4. Write an ADR if the template or prompt structure changes.
5. Re-run similarity report; confirm flagged count decreases.

## Sources

- [research-prompt.md](https://github.com/davidamitchell/Research/blob/main/research-prompt.md) — agent research prompt (candidate root cause a)
- [Research/_template.md](https://github.com/davidamitchell/Research/blob/main/Research/_template.md) — item template (candidate root cause b)
- [scripts/build_site.py](https://github.com/davidamitchell/Research/blob/main/scripts/build_site.py) — site generator (candidate root cause c)
- [Scikit-learn TF-IDF documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) — cosine similarity implementation reference

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
