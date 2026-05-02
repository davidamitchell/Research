---
title: "How does STORM's perspective discovery step work, and what is the minimum-viable prompt design for replicating multi-perspective sub-question generation in a single-agent automated research workflow?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, research-tooling, evaluation, prompt-engineering]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-03-10-adversarial-agents-shared-goals-multi-perspective, 2026-03-12-exploration-synthesis-gap]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How does STORM's perspective discovery step work, and what is the minimum-viable prompt design for replicating multi-perspective sub-question generation in a single-agent automated research workflow?

## Research Question

How does the STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective question generation) system's perspective discovery step generate diverse expert viewpoints before decomposing a research question into sub-questions — specifically what algorithm, prompt structure, and diversity criteria it uses — and what is the minimum-viable prompt template that replicates the coverage breadth improvement reported in the NAACL 2024 paper (+10% against baseline Retrieval-Augmented Generation) within a single-agent automated research workflow that cannot conduct real conversations with simulated experts?

## Scope

**In scope:**
- STORM's perspective discovery algorithm: how viewpoints are seeded, what diversity criteria are used (disciplinary, stakeholder, cultural, temporal), and how sub-questions are derived per perspective
- The reported +10% coverage breadth improvement: what metric was used, what baseline was compared, and whether the improvement is attributable to perspective discovery specifically or to other STORM components
- Alternative multi-perspective generation methods: role prompting, persona generation, ensemble prompting, chain-of-thought (CoT) diversity, and structured brainstorming frameworks (Six Thinking Hats, etc.)
- Minimum-viable prompt template: a concrete §0.5 prompt block that a single LLM agent can execute without multi-agent infrastructure
- Implementation fit for the existing research skill: how §0.5 Perspective Discovery inserts between §0 Initialise and §1 Question Decomposition without changing downstream steps

**Out of scope:**
- Full multi-agent STORM implementation (requires simulated expert conversations — not feasible in a single-agent workflow)
- STORM components unrelated to perspective discovery (outline generation, article writing)
- Evaluation of perspective discovery on this specific research corpus (empirical study not required — design recommendation is sufficient)

**Constraints:**
- Expand all acronyms on first use
- The output must be implementable as a text prompt block — no new MCP (Model Context Protocol) servers or external APIs required
- The design must fit within the existing §0–§7 numbering of the research skill

## Context

W-0038 in `BACKLOG.md` proposes adding a §0.5 Perspective Discovery step to the research skill, citing the STORM paper's +10% coverage breadth improvement. Before updating `davidamitchell/Skills` research skill and `research-prompt.md`, the mechanism must be understood precisely: what STORM's perspective step actually does, whether the +10% improvement is attributable to perspective discovery specifically, and what a minimum-viable single-agent equivalent looks like. The BACKLOG item specifies the outcome but not the design — this research item fills the design gap.

## Approach

1. **STORM paper analysis**: Read the NAACL 2024 STORM paper (arXiv:2402.14207) and extract the exact algorithm for perspective discovery — how expert viewpoints are generated, what diversity criteria are applied, and how sub-questions are derived per perspective.
2. **Coverage breadth metric review**: Identify the metric used to measure the +10% improvement, what baseline is compared against, and whether perspective discovery is isolated as the causal factor or whether other components contribute.
3. **Alternative method survey**: Survey alternative multi-perspective prompt techniques: role prompting, persona generation, Six Thinking Hats, ensemble prompting, and structured stakeholder mapping; assess each for cognitive diversity produced and prompt simplicity.
4. **Single-agent adaptation**: Design a minimum-viable §0.5 prompt block that replicates the perspective diversity mechanism without multi-agent infrastructure; the block must generate 3–5 expert viewpoints and at least one sub-question per viewpoint before §1 decomposition begins.
5. **Integration assessment**: Assess how §0.5 fits into the existing §0–§7 skill structure without requiring downstream changes; confirm the step is additive and not breaking.

## Sources

- [ ] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (STORM)](https://arxiv.org/abs/2402.14207) — primary paper describing the perspective discovery algorithm and coverage breadth evaluation
- [ ] [Lo et al. (2023) The S3-Eval Benchmark for Scientific Article Summarization](https://arxiv.org/abs/2310.14020) — evaluation methodology for coverage breadth in multi-document synthesis
- [ ] [Wang et al. (2022) Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) — ensemble prompting approach for diversity in LLM reasoning
- [ ] [de Bono (1985) Six Thinking Hats](https://www.debono.com/Books/six-thinking-hats) — structured multi-perspective brainstorming framework applicable to prompt design
- [ ] [Anthropic documentation — Role prompting and persona generation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts) — role-based perspective generation techniques

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

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

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
