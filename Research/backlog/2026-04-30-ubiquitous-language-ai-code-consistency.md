---
title: "Ubiquitous Language in AI-augmented development: domain glossaries, naming consistency, and long-term codebase coherence"
added: 2026-04-30T20:31:45+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, agentic-ai]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-grill-me-ai-alignment-shared-design, 2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-strategic-tactical-division-ai-teams, 2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Ubiquitous Language in AI-augmented development: domain glossaries, naming consistency, and long-term codebase coherence

## Research Question

How significantly does maintaining a living Ubiquitous Language (UL) — in the Domain-Driven Design (DDD) sense: a shared, precise domain vocabulary used consistently in both code and conversation — improve the precision and consistency of AI-generated code, reduce AI verbosity, and prevent naming drift across a growing codebase over time?

## Scope

**In scope:**
- Ubiquitous Language as defined in Evans's *Domain-Driven Design*: a shared vocabulary developed with domain experts and used consistently in code, tests, documentation, and conversation; its role in reducing ambiguity and translation overhead
- AI verbosity and precision: empirical or practitioner evidence that AI assistants produce more concise, on-target code when given an explicit domain glossary versus when they must infer terminology from context
- Naming consistency and drift: how quickly naming inconsistencies accumulate in AI-generated codebases; the cost of synonym proliferation (e.g., `user` vs. `customer` vs. `account_holder` for the same domain concept)
- Living glossary maintenance: how to construct, version, and provide a domain glossary to AI assistants as part of system prompt or context injection; evidence on the impact of glossary quality on output consistency
- The Matt Pocock "Ubiquitous Language" skill: description, mechanics, and practitioner evidence
- Cross-session consistency: whether AI assistants without persistent memory maintain naming conventions across sessions if given an explicit glossary versus if they must infer from file context alone

**Out of scope:**
- Full treatment of Domain-Driven Design (DDD) tactical patterns (aggregates, repositories, bounded contexts) — covered only insofar as they relate to naming conventions
- AI memory systems and long-term context persistence — a separate architectural concern
- Grill-Me alignment technique — covered in `2026-04-30-grill-me-ai-alignment-shared-design`

**Constraints:**
- Sources from 2022 onwards preferred for AI-specific evidence; Evans (2003) and other DDD foundational texts accepted as theoretical anchors
- Practitioner evidence from blog posts, talks, or skills frameworks accepted if attributed and traceable

## Context

Large Language Models (LLMs) are remarkably sensitive to vocabulary: the same code generation request phrased with domain-specific terminology versus generic terms produces meaningfully different outputs. But in a long-running project with many AI-assisted sessions, terminology can drift: the AI in one session calls the concept a `Policy`, in the next session a `Rule`, in the third a `Constraint`. Each variant is locally reasonable but collectively incoherent, and the cost — renaming, search-and-replace, reasoning about which `Policy` is which `Rule` — compounds over time.

Domain-Driven Design's Ubiquitous Language practice was invented precisely to prevent this class of problem in human teams. The question is whether it translates to the AI-augmented context and, if so, whether the benefit is large enough to justify the overhead of constructing and maintaining the glossary. If the answer is yes, a domain glossary becomes an AI-readiness artifact as important as a type system or a test suite.

This item is part of a suite examining how traditional Software Engineering (SE) fundamentals improve AI-augmented development outcomes. The synthesis item `2026-04-30-se-fundamentals-ai-code-synthesis` depends on this item's findings.

## Approach

1. **Define Ubiquitous Language in the AI context** — Summarise Evans's UL definition and its practical mechanics in DDD. Translate it to the AI-assisted workflow: what does a living glossary look like as a context-injection artifact?

2. **Survey AI vocabulary sensitivity** — Search for empirical studies or systematic practitioner observations on how terminology in prompts and context affects AI code generation output. Include research on prompt sensitivity and specification vocabulary.

3. **Examine the Matt Pocock Ubiquitous Language skill** — Locate the canonical description of the skill; extract its mechanics and the practitioner rationale. Assess the evidence for the claimed benefits.

4. **Measure naming drift** — Review available evidence on naming inconsistency in AI-generated codebases. Are there studies tracking synonym proliferation rates? If not, document the theoretical risk as `[inference]` with supporting logic.

5. **Assess cross-session consistency** — Is there evidence that providing an explicit glossary improves consistency across AI sessions (without persistent memory)? Review prompt engineering literature on context injection and system-prompt vocabulary.

6. **Synthesise** — Produce a structured assessment: does the evidence support living UL maintenance as a high-Return on Investment (ROI) practice in AI-augmented teams? What is the minimum viable glossary? How should it be maintained and versioned?

## Sources

- [ ] [Evans (2003) — Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.oreilly.com/library/view/domain-driven-design-tackling/0321125215/) — foundational definition of Ubiquitous Language; primary theoretical framework
- [ ] [Vernon (2013) — Implementing Domain-Driven Design](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/) — practical DDD implementation; living glossary mechanics; bounded context vocabulary management
- [ ] [Matt Pocock — Total TypeScript AI Fundamentals: Ubiquitous Language skill](https://www.totaltypescript.com/ai-coding-assistants) — canonical practitioner description of the UL skill for AI-assisted development; primary source for AI-specific application
- [ ] [Brown (2020) — The C4 Model for Visualising Software Architecture](https://c4model.com/) — structured vocabulary for architecture communication; adjacent to UL; context for naming artifacts
- [ ] [Zhao et al. (2021) — Calibrating the Use of LLMs: A Study of Prompting Strategies for Code Generation](https://arxiv.org/abs/2112.00114) — empirical study of prompt vocabulary effects on LLM code output quality; directly relevant to UL impact on AI output
- [ ] [White et al. (2023) — A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/abs/2302.11382) — prompt engineering patterns; includes vocabulary and persona patterns relevant to UL injection
- [ ] [Trebing et al. (2023) — Evaluating the Consistency of LLMs in Code Generation](https://arxiv.org/abs/2307.10680) — LLM naming and structural consistency across sessions; directly relevant to cross-session naming drift

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
