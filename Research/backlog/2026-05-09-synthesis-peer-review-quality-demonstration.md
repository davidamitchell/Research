---
title: "End-to-end synthesis demonstrating peer-review quality: sourced claims, labelled speculation, surfaced contradictions"
added: 2026-05-09T22:32:29+00:00
status: backlog
priority: medium
blocks: []
tags: [synthesis, research-infrastructure, evaluation, agentic-ai]
started: ~
completed: ~
output: [knowledge]
cites: []
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# End-to-end synthesis demonstrating peer-review quality: sourced claims, labelled speculation, surfaced contradictions

## Research Question

Can the synthesis workflow (`synthesis-loop.yml`) produce a completed `Knowledge/` item that meets a peer-review quality standard — all key findings linked to source items, no unlabelled speculation, contradictions between source items explicitly named, and the synthesis question answered directly in the Executive Summary?

## Scope

**In scope:**
- Selecting one topic cluster of ≥5 completed items with overlapping tags
- Triggering `synthesis-loop.yml` for the selected cluster
- Reviewing the output against four explicit quality criteria: (1) every key finding cites ≥1 source item via `cites:`, (2) no claim appears without a confidence label, (3) contradictions between source items are named in "Contradictions and Tensions", (4) synthesis question answered in Executive Summary
- Iterating on the prompt or workflow if the first output fails the review
- Committing the passing synthesis item and recording which criteria required iteration

**Out of scope:**
- Producing multiple synthesis items (one passing item is the goal)
- Automating the quality review (manual review against the four criteria)
- Changes to the authoring workflow (W-0052)

**Constraints:** Depends on W-0051 (synthesis workflow — done); cluster selection is easier with W-0061 (synthesis candidates page) but can proceed without it; depends on W-0062 (canonical tags) for reliable cluster identification.

## Context

W-0051 (synthesis workflow) and W-0052 (authoring workflow) exist but have never been validated against a quality bar. A workflow that exists is not the same as a workflow that produces useful outputs. This slice provides the end-to-end proof that the synthesis pipeline can produce a knowledge artifact that meets the peer-review standard defined by the `citation-discipline`, `speculation-control`, and `remove-ai-slop` skills. Without this demonstration, the synthesis workflow is untested infrastructure. Tracked in BACKLOG.md as W-0068.

## Approach

1. Identify a topic cluster of ≥5 completed items — use `state/tag_report.md` or the synthesis candidates page (W-0061) if available.
2. Trigger `synthesis-loop.yml` with the selected cluster's item slugs and a synthesis question.
3. Review the output against the four quality criteria; record pass/fail per criterion.
4. If any criterion fails: diagnose whether the failure is in the prompt, the workflow, or the agent behaviour; apply a targeted fix; re-trigger.
5. Iterate until all four criteria pass.
6. Commit the passing synthesis item; record the cluster slugs, synthesis question, and iteration count in the progress note.

## Sources

- [.github/workflows/synthesis-loop.yml](https://github.com/davidamitchell/Research/blob/main/.github/workflows/synthesis-loop.yml) — synthesis workflow (W-0051)
- [synthesis-prompt.md](https://github.com/davidamitchell/Research/blob/main/synthesis-prompt.md) — synthesis agent prompt (W-0051)
- [Knowledge/_template.md](https://github.com/davidamitchell/Research/blob/main/Knowledge/_template.md) — synthesis item template (W-0051)
- [.github/skills/citation-discipline/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/citation-discipline/SKILL.md) — quality criterion: sourced claims
- [.github/skills/speculation-control/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/speculation-control/SKILL.md) — quality criterion: labelled speculation
- [.github/skills/remove-ai-slop/SKILL.md](https://github.com/davidamitchell/Skills/blob/main/remove-ai-slop/SKILL.md) — quality criterion: no hollow prose

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
