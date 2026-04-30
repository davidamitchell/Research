---
title: "Grill-Me technique: iterative structured interviewing for human-AI alignment in code generation"
added: 2026-04-30T20:31:45+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, evaluation, agentic-ai]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-ubiquitous-language-ai-code-consistency, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-strategic-tactical-division-ai-teams, 2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Grill-Me technique: iterative structured interviewing for human-AI alignment in code generation

## Research Question

How effectively does the "Grill Me" technique — relentless iterative structured interviewing of the human developer by the AI assistant to build a shared design concept before generating any code — reduce misalignment between human intent and AI-generated output, and what are the measurable outcome differences compared to jumping directly into plan or code generation?

## Scope

**In scope:**
- Definition and mechanics of the "Grill Me" interaction pattern: the AI asks clarifying questions before producing any design or code; the human answers; the AI iterates until it can restate the requirements without ambiguity
- Measurement of alignment quality: how precisely the resulting code matches the original human intent; defect rates; the number of post-generation correction rounds required
- Measurable outcome differences between "grill-first" sessions and "prompt-to-code" sessions: correctness of first output, revision cycles, time-to-working-feature
- Iteration dynamics: how many questions/rounds are typically required to reach a stable shared design concept; which question types surface the most critical hidden assumptions or unspecified dependencies
- Connection to adjacent software engineering practices: specification quality, requirements gathering, user story refinement — and whether "Grill Me" is a natural language analogue for these activities in AI-augmented workflows
- Empirical evidence from practitioner reports, academic studies, or controlled experiments where available

**Out of scope:**
- Full analysis of Test-Driven Development (TDD) integration with AI — covered in `2026-04-30-tdd-feedback-loops-ai-augmented-dev`
- Deep module and architectural design decisions — covered in `2026-04-30-deep-modules-ai-augmented-codebases`
- Ubiquitous Language (UL) and domain glossary effects — covered in `2026-04-30-ubiquitous-language-ai-code-consistency`

**Constraints:**
- Evidence must be traceable to named practitioners, studies, or published frameworks; anecdote without source is flagged as `[assumption]`
- Sources from 2022 onwards preferred; older foundational software engineering (SE) sources accepted for the requirements-gathering analogy

## Context

Large Language Models (LLMs) used for code generation suffer from a well-known failure mode: the model produces plausible-looking code that satisfies the literal prompt but misses implicit intent, unstated constraints, or architectural assumptions the developer never thought to specify. This misalignment is the principal source of post-generation rework and of the "outrunning its headlights" phenomenon — where the AI generates large volumes of code that superficially compile but embed wrong design decisions that are expensive to unwind.

The "Grill Me" technique, associated with the Matt Pocock AI coding skills framework, proposes that the AI should interview the developer first — asking targeted questions until it can confidently restate the full design intent — before writing a single line. This mirrors established requirements engineering and domain-driven design (DDD) facilitation practice (Event Storming, Three Amigos, specification workshops) but applied to a single-developer, AI-as-interviewer context.

This item is part of a suite of items examining how traditional Software Engineering (SE) fundamentals improve AI-augmented development outcomes. The synthesis item `2026-04-30-se-fundamentals-ai-code-synthesis` depends on this item's findings.

## Approach

1. **Define the technique** — Identify the canonical description of "Grill Me" from Matt Pocock's published skills and blog posts. Extract the mechanism: question types, depth of interrogation, stopping criterion. Compare to adjacent practices: Three Amigos refinement, Event Storming, specification by example.

2. **Survey empirical evidence** — Search for controlled experiments, practitioner case studies, or A/B comparisons that measure outcome quality when AI sessions start with structured interrogation versus immediate code generation. Include academic literature on AI prompt engineering that addresses specification completeness.

3. **Measure iteration dynamics** — Review any published data on how many clarifying rounds are needed before AI output stabilises. Identify which question types (data model, error handling, edge cases, performance constraints, security assumptions) surface the highest-impact hidden assumptions.

4. **Compare outcome metrics** — Defect rates, revision cycles, time-to-working-feature, developer satisfaction. If no controlled studies exist, document practitioner consensus and label as `[inference]` or `[assumption]`.

5. **Assess transferability** — Does "Grill Me" work equally well across AI models (GPT-4, Claude, Gemini)? Across domains (frontend TypeScript, backend Python, data pipelines)? Identify constraints on generalisability.

6. **Synthesise** — Produce a structured assessment: does the evidence support "Grill Me" as a high-Return on Investment (ROI) practice? What are its limits? What follow-up experiments would strengthen the evidence base?

## Sources

- [ ] [Matt Pocock — Total TypeScript AI Fundamentals (GitHub Copilot Skills)](https://www.totaltypescript.com/ai-coding-assistants) — canonical description of the "Grill Me" and related skills; primary source for technique mechanics
- [ ] [Bavarian et al. (2022) — Efficient Training of Language Models to Fill in the Middle](https://arxiv.org/abs/2207.14255) — OpenAI research on fill-in-the-middle prompting; context for understanding how LLMs handle underspecified prompts
- [ ] [Xu et al. (2022) — An Empirical Evaluation of GitHub Copilot's Code Suggestions](https://doi.org/10.1145/3524842.3528470) — controlled empirical study of AI-generated code quality in practice; establishes baseline for measuring misalignment
- [ ] [Vaithilingam et al. (2022) — Expectation vs. Experience: Evaluating the Usability of Code Generation Tools](https://doi.org/10.1145/3491101.3519665) — user study on misalignment between developer intent and AI code output; directly relevant to "Grill Me" motivation
- [ ] [Ziegler et al. (2022) — Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537) — GitHub Copilot empirical productivity study; baseline for comparing grill-first vs. prompt-to-code workflows
- [ ] [Chen et al. (2021) — Evaluating Large Language Models Trained on Code (HumanEval)](https://arxiv.org/abs/2107.03374) — foundational LLM code evaluation benchmark; measurement methodology

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

*(This section seeds the Findings below.)*

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

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

### Open Questions

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
