---
title: "Evaluate research-question skill against past backlog items and fix structural weaknesses"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: medium
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

# Evaluate research-question skill against past backlog items and fix structural weaknesses

## Research Question

Does the `research-question` skill in `davidamitchell/Skills` reliably produce questions that are specific, bounded, and answerable within a single research session, and if not, what structural changes to the skill are needed?

## Scope

**In scope:**
- Sampling 10 past backlog items from `Research/backlog/` and `Research/completed/` (questions with known outcomes)
- Applying the skill's five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) to each sampled question
- Producing a structured evaluation report in `state/eval_reports/research-question-skill-eval.md`
- Identifying structural weaknesses in the skill (underspecified tests, vague rewrite criteria, unenforced scope constraints)
- Opening a PR in `davidamitchell/Skills` correcting the `research-question/SKILL.md`
- Advancing the submodule pointer in this repo after the Skills PR merges

**Out of scope:**
- Evaluating the research skill itself (different scope)
- Rewriting existing backlog items that fail the evaluation
- Changing how research questions are picked or prioritised

**Constraints:** Uses `scripts/eval_harness.py` (W-0059) for sampling; the submodule (`davidamitchell/Skills`) requires a separate PR and merge before the pointer can be advanced.

## Context

The `research-question` skill gates every new backlog item's quality but has never been formally evaluated against real outputs. Without this evaluation, the skill may be producing questions that pass its own tests but remain too broad or unanswerable in a single session. The eval harness (W-0059) now provides the mechanism to run a structured evaluation. Tracked in BACKLOG.md as W-0065.

## Approach

1. Use `scripts/eval_harness.py --n 10 --seed 42` to sample backlog and completed items.
2. For each item, apply the five-test check manually: Specific, Answerable, Scoped, Motivated, Decomposable.
3. Record per-item pass/fail verdicts and failure reasons in `state/eval_reports/research-question-skill-eval.md`.
4. Identify failure patterns: which tests fail most often, and why.
5. Draft corrections to `research-question/SKILL.md` — updated test criteria, clearer rewrite guidance, explicit scope-constraint enforcement.
6. Open a PR in `davidamitchell/Skills` with the corrected skill.
7. After the PR merges, advance the submodule pointer in this repo and update `copilot-instructions.md` if invocation instructions change.

## Sources

- [.github/skills/research-question/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/research-question/SKILL.md) — skill under evaluation
- [scripts/eval_harness.py](https://github.com/davidamitchell/Research/blob/main/scripts/eval_harness.py) — evaluation harness (W-0059)
- [Research/backlog/](https://github.com/davidamitchell/Research/tree/main/Research/backlog) — source of past backlog items
- [Research/completed/](https://github.com/davidamitchell/Research/tree/main/Research/completed) — completed items with known outcomes

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
