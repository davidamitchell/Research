---
title: "Evaluating and improving autonomous research loop quality: prompt engineering and output assessment"
added: 2026-03-03
status: backlog
priority: high
tags: [research-loop, prompt-engineering, quality, autonomous-research, evaluation, research-prompt, github-actions]
started: ~
completed: ~
output: [knowledge, tool, backlog-item]
---

# Evaluating and improving autonomous research loop quality: prompt engineering and output assessment

## Research Question

How can the quality of research items produced by the `research-loop.yml` autonomous pipeline be systematically evaluated, and what changes to `research-prompt.md` and the loop's prompting strategy would produce higher-quality, deeper, more synthesis-rich research outputs?

## Scope

**In scope:**
- Defining quality dimensions specific to autonomous research output: depth, source diversity, citation accuracy, executive summary precision, findings specificity, open-questions usefulness
- Empirical assessment of existing completed items produced by the loop: what patterns of shallow or formulaic output appear, and what is their root cause in the prompt?
- Prompt engineering techniques applicable to research prompts: chain-of-thought, role assignment, structured output constraints, negative constraints ("do not just list headings"), step decomposition
- Evaluation methodology: what criteria distinguish a high-quality completed research item from a low-quality one, and how can these criteria be applied automatically (CI check) vs. manually (spot check)?
- `research-prompt.md` redesign options: what changes would address identified weaknesses without making the prompt so long that it degrades instruction-following?
- Loop-level improvements: how the outer `while` loop in `research-loop.yml` selects items, whether priority-ordering is respected, and whether a "research brief" passed to each session improves focus

**Out of scope:**
- The underlying model (Copilot, Claude, GPT-4) selection — constrained by `COPILOT_GITHUB_TOKEN` and the existing `research-loop.yml` setup
- Loop safety controls (timeout, failure threshold, max iterations) — covered by ADR-0004 and not in scope unless evaluation reveals safety-relevant defects
- Manual research quality (items written by an agent in a direct session, not the loop) — focus is on loop-produced items

**Constraints:** Any prompt changes must remain compatible with the existing `research-loop.yml` invocation pattern. `research-prompt.md` is the only lever; no changes to the workflow file are required unless a loop-level fix is identified as necessary.

## Context

The `research-loop.yml` workflow runs automatically on weekdays, processing up to 3 backlog items per day. It has been in operation since late February 2026 and has produced the majority of items in `Research/completed/`. The `research-prompt.md` file is the sole instruction document passed to the agent each session.

The current loop has produced variable-quality output. Some items (e.g., `2026-03-01-context-mode-llm-context-compression.md`, `2026-03-02-agent-memory-management-context-injection.md`) contain rich, specific findings with cited evidence. Others follow the template structure mechanically without providing substantive answers to the research question. The root cause is unclear: is it prompt ambiguity, item underspecification, or model limitation?

The `2026-03-02-research-quality-assurance-methodology.md` backlog item addresses the quality review methodology (what checks to apply after output is produced). This item is the complement: it addresses the upstream cause (what prompting strategy produces better output in the first place). Both items are required to close the quality loop.

There is no current mechanism to detect when the loop has produced a shallow item vs. a deep one. The CI pipeline (`ci.yml`) runs linting and tests but has no research-quality check. Adding a structured quality gate (even a simple one) would provide a signal for when to trigger manual review.

## Approach

1. **Quality dimension definition** — Define the measurable quality dimensions for a completed research item produced by the loop:
   - *Depth*: does the Executive Summary directly answer the Research Question with a specific claim (not just a restatement)?
   - *Source engagement*: are the listed sources actually referenced in the Findings, or are they listed but ignored?
   - *Findings specificity*: are Key Findings concrete, evidence-backed claims, or vague generalisations?
   - *Open Questions utility*: do Open Questions represent genuine unresolved tensions surfaced by the research, or are they boilerplate?
   - *Cross-item integration*: does the item reference related completed items where relevant?
   Assess: which dimensions are automatable (structure/pattern checks) vs. require agent reasoning.

2. **Corpus audit** — Apply the quality dimensions to all existing completed items (specifically those produced by the autonomous loop). Identify the 3–5 most common failure patterns. Classify each failure as prompt-caused (the prompt did not instruct the agent to do X) vs. model-caused (the prompt did instruct it but the model did not comply).

3. **Prompt engineering survey** — Review the literature and practitioner community for prompt engineering techniques that improve research and synthesis quality in long-form outputs:
   - Chain-of-thought: explicit reasoning steps before producing findings
   - Role assignment: "You are a research analyst with expertise in X"
   - Negative constraints: "Do not reproduce the template headings without substantive content"
   - Structured output: require specific fields (e.g., "state the exact answer to the research question in one sentence in the Executive Summary")
   - Decomposition prompts: break the research task into sub-questions with separate reasoning passes

4. **research-prompt.md redesign** — Draft a revised `research-prompt.md` that addresses the identified failure patterns using the techniques from step 3. Key principles: the prompt should be long enough to set quality expectations clearly, but not so long that it dilutes the specific instructions. Test the revised prompt against the quality dimensions defined in step 1.

5. **Loop item-selection review** — Examine whether the loop respects `priority: high` items over `priority: medium` items when selecting from the backlog. Confirm the selection logic in the prompt or workflow. If items are selected in file-system order rather than priority order, propose a fix.

6. **Lightweight quality gate design** — Design a minimal quality check that can run as a GitHub Actions step after a research item is committed by the loop. Candidate checks:
   - Executive Summary word count ≥ 50 and contains a verb
   - Key Findings list contains ≥ 2 non-placeholder entries
   - At least one source listed in the Sources section is referenced in the Findings section
   - `started` and `completed` dates are populated
   Assess: are these checks sufficient to detect the most common failure modes?

7. **Iterative test** — If possible, run the revised prompt on a low-priority backlog item via `workflow_dispatch` (1 item) and compare the output quality to a pre-revision item of similar complexity. Document the before/after comparison.

## Sources

- [ ] `research-prompt.md` — current prompt; the primary artefact to evaluate and revise
- [ ] `.github/workflows/research-loop.yml` — loop implementation; understand item selection and session invocation
- [ ] `Research/completed/` — existing loop-produced items; corpus for the quality audit
- [ ] `Research/completed/2026-03-01-github-specify-ralph-loop-lisa-planning.md` — completed research on the Ralph Wiggum Technique, loop phases (Specify → Plan → Build), and proof-driven development; covers loop *design* (this item covers loop output *quality* and prompt improvement)
- [ ] `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` — complement to this item: quality review methodology (downstream quality checks vs. this item's upstream prompt improvements)
- [ ] Anthropic Prompt Engineering Guide: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview — chain-of-thought, role prompting, negative constraints
- [ ] OpenAI Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering — structured output, decomposition patterns
- [ ] LMSYS / arXiv — survey papers on LLM instruction following and research task performance (2023–2025)
- [ ] Fabric (Daniel Miessler): https://github.com/danielmiessler/fabric — prompt patterns for research extraction and synthesis; patterns like `extract_wisdom`, `summarize`, `create_report`
- [ ] `docs/adr/0004-autonomous-research-loop.md` — ADR for the loop; safety controls and design rationale

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

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge, tool, backlog-item
- Description: Quality dimension framework for autonomous research output; corpus audit findings; revised `research-prompt.md`; lightweight quality gate design; loop item-selection fix if required
- Links:
  - `research-prompt.md` (primary artefact to revise)
  - `Research/backlog/2026-03-02-research-quality-assurance-methodology.md` (complement: downstream quality review)
  - `docs/adr/0004-autonomous-research-loop.md` (loop design rationale)
