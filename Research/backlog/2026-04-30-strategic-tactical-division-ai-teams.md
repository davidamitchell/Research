---
title: "Strategic versus tactical roles in AI-augmented software teams: division of labour, daily design investment, and the cost of bad code at scale"
added: 2026-04-30T20:31:45+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, agentic-ai, llm, organisational-design]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-grill-me-ai-alignment-shared-design, 2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-ubiquitous-language-ai-code-consistency, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Strategic versus tactical roles in AI-augmented software teams: division of labour, daily design investment, and the cost of bad code at scale

## Research Question

In an AI-augmented software team, what is the optimal division of labour between the human developer (strategic design, interface definition, architectural oversight) and the AI assistant (tactical implementation) — and does Kent Beck's advice to invest daily in system design provide compounding returns in AI-heavy workflows, particularly given that AI's ability to generate large volumes of code rapidly may be making bad code more expensive, not cheaper, in 2026+?

## Scope

**In scope:**
- Human strategic roles in AI-augmented teams: system design, architectural decision-making, interface definition, test specification, review and validation; the case that these are the non-delegatable human responsibilities
- AI tactical roles: implementing within well-defined interfaces, filling in bodies of specified functions, generating boilerplate, refactoring within a defined scope
- Kent Beck's daily design investment advice: the compound-interest argument for investing a fixed proportion of each session in system design quality (naming, interface clarity, test coverage); evidence for or against compounding returns
- The "code is cheap" assumption: whether low marginal cost of AI-generated code changes the economics of technical debt; the argument that bad code is more expensive in 2026 precisely because AI can generate it faster than it can be reviewed
- Opportunity cost of the human's attention: where human developer time has the highest leverage in an AI-augmented workflow; architectural design vs. prompt engineering vs. review vs. testing
- Evidence from practitioner accounts, team retrospectives, or academic studies on optimal human-AI collaboration patterns in software development
- Kent Beck's published views on AI-augmented development (2024–2026 posts and talks)

**Out of scope:**
- Full treatment of AI agent orchestration at the multi-agent systems level — out of scope unless directly relevant to single-developer AI-augmented workflows
- Non-software industry parallels (medicine, law, finance) — referenced only if directly instructive for software team design
- Empirical measurement of code complexity metrics — covered in `2026-04-30-ai-code-entropy-quality-metrics`

**Constraints:**
- Sources from 2022 onwards preferred; foundational SE texts and Kent Beck's published work accepted regardless of date
- Practitioner evidence accepted with appropriate confidence labelling

## Context

The emergence of AI coding assistants has triggered a debate about what the human developer's role should be when the AI can generate most of the code. Two extremes exist: the "vibe-coder" who types natural language descriptions and accepts AI output with minimal review; and the "architect-driver" who invests heavily in design, specifies interfaces precisely, and uses the AI purely as an implementation engine. The evidence increasingly suggests that the architect-driver pattern produces better long-term outcomes — but the question of how much design investment is optimal, and whether this investment has compound returns, remains unresolved.

Kent Beck's argument — that daily investment in system design (naming, coupling reduction, test coverage improvement) compounds over time — predates AI coding assistants but becomes more significant in the AI context: if the AI will generate code against whatever design state exists today, then a cleaner design today means better AI output tomorrow. The question is whether this compound effect is empirically measurable and, if so, how large it is.

The "code is cheap" assumption has historically been used to justify deferred design investment. If AI makes code generation essentially free, the question is whether it also makes bad code cheaper (because it can be regenerated) or more expensive (because the volume of bad code that can be generated in a session is now enormous, increasing the review and correction burden).

This item is part of a suite examining how traditional Software Engineering (SE) fundamentals improve AI-augmented development outcomes. The synthesis item `2026-04-30-se-fundamentals-ai-code-synthesis` depends on this item's findings.

## Approach

1. **Define the strategic/tactical division** — Survey published frameworks for human-AI division of labour in software development. Extract the consensus view from practitioner literature on what humans must own versus what can be safely delegated to AI.

2. **Review Kent Beck's design investment argument** — Locate Beck's published views on daily design investment and its application to AI-augmented workflows. Assess the compound-interest argument: does evidence from software maintenance research support it?

3. **Examine the "code is cheap" assumption** — Review the argument that AI generation has inverted the economics of technical debt: if generating code is free but reviewing and correcting bad code is expensive, the marginal cost of bad code has increased. Find published analysis or evidence.

4. **Survey human-AI collaboration models** — Search for empirical studies or structured practitioner accounts of how human time is best invested in AI-augmented development. Include Microsoft Research studies on Copilot workflows, practitioner retrospectives, and AI team structure discussions.

5. **Assess the opportunity cost of human attention** — Where does human developer time have the highest leverage? Design? Specification? Review? Testing? Synthesise from evidence, not assertion.

6. **Synthesise** — Produce a structured assessment: what does the evidence say about the optimal strategic/tactical division? Is daily design investment warranted? Has "code is cheap" become "bad code is expensive"?

## Sources

- [ ] [Beck (2023) — Tidy First? A Personal Exercise in Empirical Software Design](https://www.oreilly.com/library/view/tidy-first/9781098151232/) — Beck's most recent published work on incremental design investment; closest to the daily-design-investment argument; primary source
- [ ] [Beck (2024) — Kent Beck on AI and Software Design (Substack: Tidy First)](https://tidyfirst.substack.com/) — Beck's ongoing published commentary on AI coding assistants and design investment; primary source for contemporary views
- [ ] [Ousterhout (2018) — A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) — strategic complexity management; the case for investing in design quality; theoretical foundation for compound returns argument
- [ ] [Ziegler et al. (2022) — Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537) — GitHub Copilot productivity study; evidence on where AI adds most value and where human judgment remains essential
- [ ] [Peng et al. (2023) — The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590) — controlled experiment on Copilot productivity; measures overall developer velocity; context for evaluating strategic investment trade-offs
- [ ] [Cumming (2024) — The Cost of Software in the Age of AI](https://martinfowler.com/articles/ai-cost-of-software.html) — practitioner analysis on whether AI makes bad code cheaper or more expensive; directly addresses the "code is cheap" reversal
- [ ] [Fowler (2019) — Refactoring: Improving the Design of Existing Code (2nd ed.)](https://martinfowler.com/books/refactoring.html) — incremental design improvement; theoretical basis for Beck's daily investment argument
- [ ] [Hunt & Thomas (2019) — The Pragmatic Programmer (20th Anniversary Edition)](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — entropy, investment in design quality, and technical debt; foundational framing for the compound-returns argument

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
