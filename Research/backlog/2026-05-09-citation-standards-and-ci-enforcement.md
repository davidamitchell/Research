---
title: "docs/citation-standards.md and CI citation enforcement"
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

# docs/citation-standards.md and CI citation enforcement

## Research Question

What changes to `docs/`, `research-prompt.md`, `Research/_template.md`, and `ci.yml` are needed so that (a) a canonical citation format is defined with examples in `docs/citation-standards.md`, (b) the research prompt and item template reference it, and (c) CI fails any completed item PR that contains an uncited factual claim?

## Scope

**In scope:**
- Creating `docs/citation-standards.md` with: canonical citation format definition, five worked examples, list of prohibited formats
- Updating `Research/_template.md` to reference `docs/citation-standards.md` in the `## Sources` and `## Findings` section comments
- Updating `research-prompt.md` Step 6 companion checks to reference `docs/citation-standards.md` and make the uncited-claim check blocking (not advisory)
- Implementing `scripts/citation_check.py`: flags factual claims lacking trailing citations; flags sources in `## Sources` with no matching citation in `## Findings`
- Updating `ci.yml`: run `citation_check.py` on PRs touching `Research/completed/**`; fail the step on uncited claims
- Tests covering: correct identification of uncited claims, canonical format accepted, prohibited formats rejected

**Out of scope:**
- Retroactively correcting existing completed items (W-0063 covers that)
- Changing the citation format itself (the canonical suffix-style format is already defined in the template)
- MLA, APA, or other academic style variants

**Constraints:** `docs/citation-standards.md` must not be edited directly if `docs/` is auto-generated — this file is a documentation artifact, not a generated page, so it must be confirmed that it can be committed to `docs/` or placed elsewhere (e.g. `docs-adr/` or repo root).

## Context

Uncited factual claims are the most common quality failure in completed items. The `citation-discipline` skill and the research-prompt citation check are both advisory. Making citation enforcement automated and blocking in CI removes the human review burden and ensures the standard is enforced. This is the single change most likely to prevent recurring citation failures in new items. Tracked in BACKLOG.md as W-0067.

## Approach

1. Confirm whether `docs/citation-standards.md` can be committed directly to `docs/` or must go elsewhere (check `build_site.yml` behaviour).
2. Draft `docs/citation-standards.md` with canonical format definition, five worked examples (paper, org doc, web page, dataset, preprint), and prohibited-format list.
3. Update `Research/_template.md` `## Sources` and `## Findings` comments to link to `docs/citation-standards.md`.
4. Update `research-prompt.md` Step 6: reference `docs/citation-standards.md`; change uncited-claim check from advisory to blocking.
5. Implement `scripts/citation_check.py` with the two checks (uncited claims, orphaned sources).
6. Update `ci.yml` to run `citation_check.py` on `Research/completed/**` PRs.
7. Write tests; confirm CI pipeline passes on a clean item and fails on a known-uncited item.

## Sources

- [Research/_template.md](https://github.com/davidamitchell/Research/blob/main/Research/_template.md) — current citation format instructions in the template
- [research-prompt.md](https://github.com/davidamitchell/Research/blob/main/research-prompt.md) — current Step 6 citation checks
- [.github/skills/citation-discipline/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/citation-discipline/SKILL.md) — citation discipline skill (advisory reference)
- [.github/workflows/ci.yml](https://github.com/davidamitchell/Research/blob/main/.github/workflows/ci.yml) — CI workflow to extend

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
