---
title: "Evaluate research-reviewer skill and workflow against completed items; fix false passes and failures"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: high
blocks: []
tags: [research-infrastructure, evaluation, workflow]
started: ~
completed: ~
output: [knowledge, skill]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Evaluate research-reviewer skill and workflow against completed items; fix false passes and failures

## Research Question

Does the `research-reviewer` skill combined with `research-review.yml` produce a reliable pass/fail signal when applied to completed research items, and what changes are needed to eliminate false passes and false failures?

## Scope

**In scope:**
- Sampling 10 completed items: 5 known-good (high confidence, full citations, no hollow prose) and 5 known-weak (missing fields, uncited claims, hollow phrases)
- Running each item through `research-review.yml` and capturing `OVERALL/VIOLATION` log lines (not just workflow success/failure)
- Classifying results: true pass, true fail, false pass, false fail
- Correcting the `research-reviewer` skill's check rules to eliminate false results
- Opening a PR in `davidamitchell/Skills` with the corrected skill
- Updating `research-review.yml` if workflow-level changes are needed
- Advancing the submodule pointer after the Skills PR merges

**Out of scope:**
- Correcting the items themselves (W-0063)
- Changing the review workflow trigger or dispatch mechanism
- Evaluating the `research-question` skill (W-0065)

**Constraints:** Must capture `OVERALL/VIOLATION` log lines, not just workflow exit code — workflow success alone can hide item-level review failures (established failure pattern). Known-weak items must be identifiable from the audit results of W-0063 if that slice is done first.

## Context

The research-review workflow currently auto-passes some items without running meaningful checks — workflow success hides item-level review failures. This is a known recurring failure pattern. Without a calibrated skill, the `research-loop.yml` completion step cannot be trusted to gate quality. A systematic evaluation against known-good and known-weak items is the only way to calibrate the pass/fail signal. Tracked in BACKLOG.md as W-0066.

## Approach

1. Identify 5 known-good and 5 known-weak items from the corpus (use audit results from W-0063 if available; otherwise select by inspection).
2. Run each item through `research-review.yml` via `workflow_dispatch`; capture log output for `OVERALL` and `VIOLATION` lines.
3. Classify each result: true pass, true fail, false pass, false fail.
4. For each false result, identify the specific check that produced the wrong verdict.
5. Draft corrections to `research-reviewer/SKILL.md` — tighten checks producing false passes, clarify checks producing false failures.
6. Open a PR in `davidamitchell/Skills` with the corrected skill; update `research-review.yml` if needed.
7. Re-run evaluation on the same 10 items; confirm zero false passes and zero false failures before closing.

## Sources

- [.github/skills/research-reviewer/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/research-reviewer/SKILL.md) — skill under evaluation
- [.github/workflows/research-review.yml](https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-review.yml) — workflow under evaluation
- [BACKLOG.md — Known Recurring Failure Patterns](https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md) — "workflow success alone can hide item-level review failures" pattern
- [Research/completed/](https://github.com/davidamitchell/Research/tree/main/Research/completed) — source items for sampling

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
