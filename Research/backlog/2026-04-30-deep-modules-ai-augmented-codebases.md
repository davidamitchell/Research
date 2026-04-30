---
title: "Deep modules in AI-augmented development: interface design, gray-box delegation, and architectural rescue of AI-generated codebases"
added: 2026-04-30T20:31:45+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, evaluation, agentic-ai]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-grill-me-ai-alignment-shared-design, 2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-ubiquitous-language-ai-code-consistency, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-strategic-tactical-division-ai-teams, 2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Deep modules in AI-augmented development: interface design, gray-box delegation, and architectural rescue of AI-generated codebases

## Research Question

How much more effective is AI at understanding, navigating, and correctly modifying a codebase composed of deep modules with simple interfaces versus one filled with many shallow modules — and can iterative architectural improvement ("Improve Codebase Architecture" skill) rescue an AI-generated "ball of mud" codebase, and if so what is the typical effort-versus-benefit ratio?

## Scope

**In scope:**
- Deep modules definition from Ousterhout's *A Philosophy of Software Design*: modules with powerful functionality behind a small, simple interface; contrasted with shallow modules that expose as much complexity as they hide
- AI code navigation and comprehension: empirical or practitioner evidence that deep modules reduce the cognitive load and context-window pressure on AI assistants when modifying or extending existing code
- Gray-box delegation: the design practice where a human developer designs and specifies the interface (contract, tests, types) while delegating the implementation entirely to an AI assistant; evidence that this produces better outcomes than asking the AI to design and implement simultaneously
- Iterative architectural improvement: the "Improve Codebase Architecture" skill or equivalent refactoring-first approaches for AI-generated codebases; effort and benefit evidence from case studies or practitioner reports
- Connection to information hiding and module decomposition: Parnas's information-hiding principle as the theoretical parent; relevance to AI-assisted development
- The cost of rescue: how much effort is required to recover a "ball of mud" codebase (dense coupling, shallow modules, poor naming) after it has been AI-generated without architectural guidance

**Out of scope:**
- Code entropy metrics and measurement methodology — covered in `2026-04-30-ai-code-entropy-quality-metrics`
- Test-Driven Development (TDD) as an interface-design tool — covered in `2026-04-30-tdd-feedback-loops-ai-augmented-dev`
- Ubiquitous Language (UL) and domain naming — covered in `2026-04-30-ubiquitous-language-ai-code-consistency`
- Microservices architecture at system-of-systems level — out of scope unless directly relevant to module decomposition at the code level

**Constraints:**
- Sources from 2020 onwards preferred for AI-specific evidence; foundational SE texts accepted regardless of date
- Practitioner case studies accepted if sufficiently detailed; anecdote without traceable source labelled `[assumption]`

## Context

John Ousterhout's central argument in *A Philosophy of Software Design* — that deep modules are the most effective structural unit for managing complexity — has a natural extension to AI-augmented development: an AI assistant with a fixed context window can more reliably understand, test, and modify a module if its interface is small and its behaviour is fully specified behind that interface. Shallow modules, by contrast, leak implementation detail into every callsite, forcing the AI to load far more context to make any change safely.

The gray-box delegation pattern is a direct application: the human defines the contract (interface types, documented preconditions, test cases) and the AI implements the body. This separates the strategic concern (what must the module do?) from the tactical concern (how should it do it?). Evidence that this pattern works well would strongly support the case for deep-module architecture as an AI-readiness practice.

The rescue scenario is equally important: given that many teams have already accumulated large AI-generated codebases without architectural guidance, the question of whether iterative refactoring toward deep modules is feasible — and at what cost — is practically significant.

This item is part of a suite examining how traditional Software Engineering (SE) fundamentals improve AI-augmented development outcomes. The synthesis item `2026-04-30-se-fundamentals-ai-code-synthesis` depends on this item's findings.

## Approach

1. **Define deep vs. shallow modules in the AI context** — Summarise Ousterhout's framework. Map it to the AI-assisted development context: what does a "deep module" look like in a TypeScript/Python codebase, and how does it reduce AI context-window pressure?

2. **Survey AI comprehension and modification evidence** — Search for studies or practitioner reports measuring AI performance on codebases with well-defined interfaces versus densely coupled code. Identify any controlled experiments comparing Copilot/Claude on deep vs. shallow architectures.

3. **Examine gray-box delegation** — Search for practitioner descriptions of interface-first / test-first AI delegation. Review whether the "Total TypeScript" skills framework or similar describes this pattern explicitly. Assess outcome quality: correctness, revision rate, alignment with intent.

4. **Review "ball of mud" rescue approaches** — Survey the available guidance on incremental refactoring of AI-generated codebases toward deep-module structure. Include the "Improve Codebase Architecture" skill if published. Estimate the typical effort-versus-benefit ratio from case studies.

5. **Analyse information-hiding depth** — Review Parnas's original information-hiding work and Ousterhout's extension. Assess whether AI assistants naturally respect information-hiding boundaries or tend to break them when generating new features.

6. **Synthesise** — Produce a structured assessment: does the evidence support deep modules as an AI-readiness investment? What is the minimal viable architecture for safe AI delegation? What does the rescue effort look like at different levels of existing entropy?

## Sources

- [ ] [Ousterhout (2018) — A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) — deep modules vs. shallow modules; information hiding; complexity management; primary theoretical framework
- [ ] [Parnas (1972) — On the Criteria To Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623) — foundational information-hiding principle; parent of Ousterhout's deep modules concept
- [ ] [Fowler (2018) — Refactoring: Improving the Design of Existing Code (2nd ed.)](https://martinfowler.com/books/refactoring.html) — canonical reference for incremental refactoring; rescue of ball-of-mud codebases
- [ ] [Matt Pocock — Total TypeScript AI Fundamentals: Improve Codebase Architecture](https://www.totaltypescript.com/ai-coding-assistants) — practitioner skill for iterative architectural improvement of AI-generated codebases; primary source for rescue approach
- [ ] [Ziegler et al. (2022) — Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537) — GitHub Copilot productivity study; context for measuring AI performance on structured vs. unstructured codebases
- [ ] [Dakhel et al. (2023) — GitHub Copilot AI Pair Programmer: Asset or Liability?](https://arxiv.org/abs/2206.15331) — controlled study of Copilot code quality; measurement basis for deep-module comparison
- [ ] [Gamma et al. (1994) — Design Patterns: Elements of Reusable Object-Oriented Software](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/) — structural patterns relevant to module decomposition; context for deep-module design
- [ ] [Tornhill (2023) — Software Design X-Rays (2nd ed.)](https://pragprog.com/titles/atevol/software-design-x-rays/) — hotspot analysis; identifying modules that accumulate disproportionate complexity and change churn — directly relevant to rescue prioritisation

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
