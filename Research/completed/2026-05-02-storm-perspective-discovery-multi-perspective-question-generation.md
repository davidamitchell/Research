---
review_count: 2
title: "How does STORM's perspective discovery step work, and what is the minimum-viable prompt design for replicating multi-perspective sub-question generation in a single-agent automated research workflow?"
added: 2026-05-02T06:11:10+00:00
status: completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, agent-tooling, evaluation]
started: 2026-05-03T07:52:09+00:00
completed: 2026-05-03T08:13:24+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-10-adversarial-agents-shared-goals-multi-perspective]
related: [2026-03-12-exploration-synthesis-gap]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How does STORM's perspective discovery step work, and what is the minimum-viable prompt design for replicating multi-perspective sub-question generation in a single-agent automated research workflow?

## Research Question

How does the STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective question generation) system's perspective discovery step generate diverse expert viewpoints before decomposing a research question into sub-questions, specifically what algorithm, prompt structure, and diversity criteria it uses, and what is the minimum-viable prompt template that replicates the coverage breadth improvement reported in the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024) paper (+10% against baseline Retrieval-Augmented Generation (RAG)) within a single-agent automated research workflow that cannot conduct real conversations with simulated experts?

## Scope

**In scope:**
- STORM's perspective discovery algorithm: how viewpoints are seeded, what diversity criteria are used (disciplinary, stakeholder, cultural, temporal), and how sub-questions are derived per perspective
- The reported +10% coverage breadth improvement: what metric was used, what baseline was compared, and whether the improvement is attributable to perspective discovery specifically or to other STORM components
- Alternative multi-perspective generation methods: role prompting, persona generation, ensemble prompting, chain-of-thought (CoT) diversity, and structured brainstorming frameworks (Six Thinking Hats, etc.)
- Minimum-viable prompt template: a concrete §0.5 prompt block that a single Large Language Model (LLM) agent can execute without multi-agent infrastructure
- Implementation fit for the existing research skill: how §0.5 Perspective Discovery inserts between §0 Initialise and §1 Question Decomposition without changing downstream steps

**Out of scope:**
- Full multi-agent STORM implementation (requires simulated expert conversations, not feasible in a single-agent workflow)
- STORM components unrelated to perspective discovery (outline generation, article writing)
- Evaluation of perspective discovery on this specific research corpus (empirical study not required, design recommendation is sufficient)

**Constraints:**
- Expand all acronyms on first use
- The output must be implementable as a text prompt block, no new MCP (Model Context Protocol) servers or external Application Programming Interfaces (APIs) required
- The design must fit within the existing §0–§7 numbering of the research skill

## Context

W-0038 in `BACKLOG.md` proposes adding a §0.5 Perspective Discovery step to the research skill before question decomposition. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

The STORM paper and released code both show that perspective discovery is a distinct pre-questioning step, but they do not show that persona prompting alone accounts for the full reported coverage gain. [fact; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py]

This item therefore focuses on the design gap between STORM's multi-perspective pre-writing stage and this repository's single-agent research workflow. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://aclanthology.org/2024.naacl-long.347/]

## Approach

1. **STORM paper analysis**: Read the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL 2024) STORM paper (arXiv:2402.14207) and extract the exact algorithm for perspective discovery, how expert viewpoints are generated, what diversity criteria are applied, and how sub-questions are derived per perspective.
2. **Coverage breadth metric review**: Identify the metric used to measure the +10% improvement, what baseline is compared against, and whether perspective discovery is isolated as the causal factor or whether other components contribute.
3. **Alternative method survey**: Survey alternative multi-perspective prompt techniques: role prompting, persona generation, Six Thinking Hats, ensemble prompting, and structured stakeholder mapping; assess each for cognitive diversity produced and prompt simplicity.
4. **Single-agent adaptation**: Design a minimum-viable §0.5 prompt block that replicates the perspective diversity mechanism without multi-agent infrastructure; the block must generate 3–5 expert viewpoints and at least one sub-question per viewpoint before §1 decomposition begins.
5. **Integration assessment**: Assess how §0.5 fits into the existing §0–§7 skill structure without requiring downstream changes; confirm the step is additive and not breaking.

## Sources

- [x] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://aclanthology.org/2024.naacl-long.347/) - primary paper describing STORM's perspective discovery algorithm, ablations, and human evaluation
- [x] [Stanford OVAL STORM README](https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/README.md) - project documentation summarising the two-stage workflow and the role of perspective-guided question asking
- [x] [Stanford OVAL STORM persona_generator.py](https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py) - released implementation of related-topic discovery and persona generation
- [x] [Stanford OVAL STORM knowledge_curation.py](https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py) - released implementation of persona-conditioned question asking and conversation simulation
- [x] [Wang et al. (2023) Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) - diversity-through-sampling baseline for comparison with perspective seeding
- [x] [Edward de Bono Ltd Six Thinking Hats Summary](https://www.debono.com/six-thinking-hats-summary) - structured thinking-mode framework for comparison with role-based perspective generation
- [x] [Anthropic Prompt Engineering System Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts) - prompt-writing guidance on explicit instruction following and scope control
- [x] [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - workflow guidance on using simple composable patterns and multiple perspectives when needed
- [x] [Adversarial agents with shared goals: multi-perspective coverage across competencies and time horizons](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md) - prior corpus item on why non-overlapping perspectives improve coverage
- [x] [Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-exploration-synthesis-gap.md) - prior corpus item on synthesis constraints in agent-mediated work

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- Question: How STORM's perspective discovery actually works, what the reported coverage-gain evidence does and does not isolate, and what minimum-viable single-agent prompt block best preserves the perspective-seeding mechanism.
- Scope: STORM's perspective-discovery mechanism, breadth metric, ablation evidence, comparison with simpler diversity techniques, and an additive §0.5 prompt block for this repository's research workflow.
- Constraints: No multi-agent infrastructure, no new external services, additive fit with existing §0–§7 research workflow numbering, and explicit separation between evidence-backed claims and design inferences.
- Output format: Structured synthesis with a concrete §0.5 prompt block and a direct answer about attribution limits.
- Prior work cross-reference:
  - [fact] The completed item on adversarial agents argues that deliberately non-overlapping perspectives improve coverage by surfacing blind spots across competencies and time horizons. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md
  - [inference] That prior item strengthens the case for a multi-perspective seeding step here, but it does not specify STORM's algorithm or establish the prompt shape needed for a single-agent workflow. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md; https://aclanthology.org/2024.naacl-long.347/

### §1 Question Decomposition

**A. STORM mechanism**
- A1. What concrete steps does STORM use to discover perspectives before question decomposition?
- A2. What prompt structure turns those perspectives into sub-questions?
- A3. What diversity criteria are explicit in the paper or code, and what criteria are only implicit?

**B. Evaluation and attribution**
- B1. What exactly is the reported +10% breadth improvement measuring?
- B2. Is the breadth improvement isolated to perspective discovery, or does it reflect the full STORM pipeline?
- B3. What do the ablation tables say about perspective discovery versus simulated conversation?

**C. Alternative techniques**
- C1. What does self-consistency add, and what does it not add, relative to perspective discovery?
- C2. What does Six Thinking Hats add, and what does it not add, relative to role-conditioned prompting?
- C3. What prompt-design guidance supports a minimum-viable single-agent version?

**D. Design recommendation**
- D1. Which STORM properties must be preserved in a single-agent adaptation?
- D2. What is the minimum prompt block that preserves those properties without pretending to reproduce full STORM behavior?
- D3. How should that prompt block plug into §0–§7 without breaking downstream steps?

### §2 Investigation

#### A1-A3. STORM's perspective discovery mechanism

- [fact] The STORM paper describes the pre-writing stage as a sequence of discovering perspectives, simulating conversations where writers carrying those perspectives ask questions to a topic expert grounded on trusted Internet sources, and then curating the collected information into an outline. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] Figure 2 and Section 3 of the paper state that STORM identifies perspectives by surveying related Wikipedia articles, then uses those perspectives to guide question asking before outline generation. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] The released `persona_generator.py` implementation operationalises this by first prompting for related Wikipedia pages, then scraping each related page's title and table of contents, and finally prompting the model to select a group of Wikipedia editors, each representing a different perspective, role, or affiliation related to the topic. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py

- [fact] The released implementation prepends a default persona, `Basic fact writer`, before the generated personas, so STORM always includes one broad factual lens alongside topic-specific roles. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py

- [fact] STORM's question-generation prompt conditions the writer on a specific perspective and asks for one question at a time, while the conversation simulator feeds back recent dialogue history so later questions can depend on retrieved information. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [fact] The topic-expert side of the conversation splits each question into search queries, retrieves sources, and synthesises an answer from gathered snippets before the writer asks the next question. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [fact] Neither the paper nor the released prompts specify a formal diversity taxonomy such as disciplinary, cultural, temporal, or geographic quotas; the explicit prompt language asks for different `perspective, role, or affiliation` and uses related-topic outlines as inspiration. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py

- [inference] STORM's diversity mechanism is therefore best understood as retrieval-primed persona generation rather than a fixed algorithmic coverage rubric. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py

#### B1-B3. Breadth metric and attribution limits

- [fact] STORM uses outline coverage as a proxy for pre-writing quality and evaluates it with heading soft recall and heading entity recall, comparing generated multi-level section headings to the human-written article headings. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] The paper defines heading soft recall with embedding similarity over headings and heading entity recall as the percentage of named entities from human-written article headings covered by the generated outline. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] The often-quoted `+10% broad in coverage` claim comes from experienced Wikipedia editors' human evaluation of full STORM articles against an outline-driven retrieval-augmented generation baseline, not from an isolated experiment on perspective discovery alone. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] Table 3 reports that removing perspective conditioning lowers outline quality for both model settings, but only modestly in heading soft recall: for the Generative Pre-trained Transformer (GPT)-3.5 setting, STORM falls from 86.26 to 84.49 and heading entity recall falls from 40.52 to 40.12; for GPT-4, heading soft recall falls from 92.73 to 92.39 and heading entity recall falls from 45.91 to 42.70. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] Table 5 reports that removing perspective conditioning reduces the average number of unique references collected from 99.83 to 54.36, while removing conversation reduces it further to 39.56. Source: https://aclanthology.org/2024.naacl-long.347/

- [fact] The `w/o Conversation` ablation performs materially worse than full STORM in both heading metrics, which the authors interpret as evidence that reading relevant information during multi-turn interaction is crucial to generating effective questions. Source: https://aclanthology.org/2024.naacl-long.347/

- [inference] The paper therefore supports a narrower claim than W-0038's wording implies: perspective discovery contributes to coverage, especially reference diversity and entity-level coverage, but the reported +10% human breadth gain belongs to the combined STORM pipeline rather than to the persona step alone. Source: https://aclanthology.org/2024.naacl-long.347/

#### C1-C3. Alternative multi-perspective techniques

- [fact] Self-consistency samples a diverse set of reasoning paths and then selects the most consistent answer by marginalising over those sampled paths. Source: https://arxiv.org/abs/2203.11171

- [inference] Self-consistency improves answer robustness after multiple attempts, but it is not a close match for STORM's perspective discovery because it aggregates alternative chains into one answer instead of preserving distinct topical lenses that can each seed different sub-questions. Source: https://arxiv.org/abs/2203.11171; https://aclanthology.org/2024.naacl-long.347/

- [fact] Six Thinking Hats defines six thinking modes, but the official method states that in group discussions everyone should use the same hat at the same time and warns against treating hats as personality types. Source: https://www.debono.com/six-thinking-hats-summary

- [inference] Six Thinking Hats is therefore a better checklist for question classes than a direct substitute for STORM's simultaneous role-conditioned perspective generation. Source: https://www.debono.com/six-thinking-hats-summary; https://aclanthology.org/2024.naacl-long.347/

- [fact] Anthropic's agent guidance recommends using the simplest composable workflow that fits the task and identifies parallelization as useful when multiple perspectives or attempts are needed for higher confidence results. Source: https://www.anthropic.com/engineering/building-effective-agents

- [fact] Anthropic's prompt guidance says current models follow instructions literally and perform better when scope and formatting expectations are explicit rather than implied. Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts

- [inference] For a single-agent research workflow, an explicit fixed set of perspective slots is more likely to preserve STORM's persona-conditioning effect than an open-ended instruction such as `be diverse`. Source: https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://aclanthology.org/2024.naacl-long.347/

#### D1-D3. Minimum-viable single-agent adaptation

- [fact] The closest prior completed item in this repository argues that non-overlapping perspectives improve coverage because each perspective notices different failure modes, trade-offs, and time horizons. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md

- [inference] A minimum-viable STORM-inspired §0.5 step should preserve three properties from the released system: one default broad factual lens, explicit additional non-overlapping lenses, and one seed question per lens before downstream decomposition starts. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [assumption] The single-agent workflow can infer adequate perspectives from the topic statement and seeded sources without scraping related Wikipedia tables of contents on every run, because the design target here is minimum viable prompt cost rather than full STORM fidelity. Source: https://www.anthropic.com/engineering/building-effective-agents; https://aclanthology.org/2024.naacl-long.347/

- [inference] A fixed four-slot structure is safer than a freeform `3-5 perspectives` instruction because it guarantees baseline factual, mechanism, stakeholder-impact, and failure-mode coverage while keeping the added prompt short enough to remain operational inside the current workflow. Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md

- [inference] This §0.5 step is additive rather than breaking because §1 Question Decomposition can simply recurse over the seed questions it emits, leaving §§2-§7 unchanged. Source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://aclanthology.org/2024.naacl-long.347/

### §3 Reasoning

- [inference] STORM's perspective discovery is a lightweight persona-seeding heuristic that shapes the starting questions, not a formal diversity-optimisation algorithm with explicit coverage constraints. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py

- [inference] The single-agent analogue should therefore target the causal ingredient that survives without simulated dialogue, namely persona-conditioned first-question selection, rather than claiming to reproduce the full STORM pipeline. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [inference] The ablation evidence makes conversation the larger contributor to question quality, while perspective discovery mainly improves source diversity and entity-level outline coverage. Source: https://aclanthology.org/2024.naacl-long.347/

- [inference] The honest design target is thus a prompt block that broadens initial coverage and reduces generic decomposition, not a prompt block that promises the paper's +10% human-evaluation result without new local evaluation. Source: https://aclanthology.org/2024.naacl-long.347/

### §4 Consistency Check

- [fact] The paper, README, and released code all agree on the same ordering: discover perspectives, ask perspective-guided questions, simulate conversations, then build and refine the outline. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/README.md; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [fact] The headline `+10% broad in coverage` claim and the outline-creation ablations answer different questions, so using the former as proof of the isolated persona step would overstate the evidence. Source: https://aclanthology.org/2024.naacl-long.347/

- [inference] No unresolved contradiction remains if the recommendation is framed as a minimum-viable analogue of STORM's perspective seeding rather than a direct reproduction of the full system's measured outcome. Source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** STORM's strongest differentiator is not just multiple roles, but the combination of role-conditioned prompting with iterative retrieval and follow-up, which means a single-agent adaptation should be explicit about what it preserves and what it drops. Source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py

- [inference] **Behavioral lens:** Explicit perspective slots counter the generic-question failure mode that current models show when instructions are broad, because literal instruction following improves when role and output structure are specified up front. Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts

- [inference] **Method lens:** Six Thinking Hats is most useful here as a validation checklist for missing question classes, especially factual, critical, creative, and process lenses, rather than as the primary prompt scaffold. Source: https://www.debono.com/six-thinking-hats-summary

- [inference] **Repository lens:** The adversarial-agents completed item suggests including at least one critic or failure-mode lens in the minimum prompt because multi-perspective coverage is most valuable when viewpoints are deliberately non-overlapping rather than cosmetically varied. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md

### §6 Synthesis

**Executive summary:**

STORM's perspective discovery is a lightweight persona-generation step seeded from related Wikipedia article outlines, not a formal diversity algorithm, and the safest single-agent replication is a fixed perspective-seeding prompt rather than a claim that the full STORM coverage gain will transfer unchanged. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py]

The paper's +10% `broad in coverage` result belongs to end-to-end STORM versus an outline-driven retrieval-augmented generation baseline, while the ablation evidence supports the inference that perspective discovery alone has a smaller but still real effect, especially on source diversity and entity-level outline coverage. [inference; source: https://aclanthology.org/2024.naacl-long.347/]

One strong minimum-viable §0.5 candidate for this repository is an additive four-perspective prompt that emits one seed question per non-overlapping lens and minimizes downstream workflow change, while leaving room for later testing of topic-sensitive slot changes or a light `related topics` retrieval step. [inference; source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://www.anthropic.com/engineering/building-effective-agents]

**Key findings:**

1. **STORM discovers perspectives by surveying related Wikipedia pages, extracting their titles and tables of contents, and then prompting the model to invent editor personas that each represent a different perspective, role, or affiliation before any question decomposition begins.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
2. **The released implementation always prepends a `Basic fact writer` persona, which means STORM explicitly combines one broad factual lens with a small set of topic-specific lenses instead of relying only on specialist roles.** ([fact]; medium confidence; source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
3. **STORM does not publish an explicit diversity rubric over disciplinary, cultural, temporal, or stakeholder categories, so its diversity mechanism is implicit and retrieval-primed rather than a formal coverage algorithm with declared quotas.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
4. **The paper's +10% `broad in coverage` result should not be attributed to perspective discovery alone, because that number compares full STORM against an outline-driven retrieval-augmented generation baseline and the ablations isolate a smaller persona-specific effect.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/)
5. **The ablation results show that removing perspective conditioning roughly halves the number of unique references collected and lowers entity-level outline recall, while removing simulated conversation hurts performance even more, so the evidence supports the inference that conversation contributes more than persona seeding to overall question quality.** ([inference]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/)
6. **Self-consistency and Six Thinking Hats are useful comparison points, but neither is a close substitute for STORM's perspective discovery because self-consistency collapses multiple attempts into one answer and Six Thinking Hats organises modes of thought rather than parallel role-conditioned lenses.** ([inference]; medium confidence; source: https://arxiv.org/abs/2203.11171; https://www.debono.com/six-thinking-hats-summary; https://aclanthology.org/2024.naacl-long.347/)
7. **A strong minimum-viable candidate for this repository is a four-slot prompt, `basic facts`, `mechanism or implementation`, `stakeholder or decision impact`, and `failure mode or critic`, with one seed question per perspective, because that preserves STORM's broad-facts-plus-specialist-lenses pattern while keeping the prompt simple and leaving room for later topic-sensitive refinements.** ([inference]; low confidence; source: https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md)
8. **The safest repository recommendation is to keep §0.5 additive by making it emit seed questions for §1 instead of redesigning later stages, because the backlog goal is broader question coverage and Anthropic guidance favors the smallest workflow change that preserves task structure.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://www.anthropic.com/engineering/building-effective-agents])

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] STORM surveys related Wikipedia pages, extracts tables of contents, and generates personas before asking questions. | https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Paper plus code |
| [fact] STORM prepends a `Basic fact writer` persona to topic-specific personas. | https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Code-backed |
| [fact] Diversity criteria are implicit `perspective, role, or affiliation`, not a fixed rubric. | https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Prompt-backed |
| [fact] The +10% breadth claim belongs to end-to-end STORM versus outline-driven retrieval-augmented generation, not to the persona step alone. | https://aclanthology.org/2024.naacl-long.347/ | medium | Human-eval claim |
| [inference] Ablations show perspective discovery matters, but conversation appears to matter more, especially for unique references and entity recall. | https://aclanthology.org/2024.naacl-long.347/ | medium | Table 3 plus Table 5 |
| [inference] Self-consistency and Six Thinking Hats are useful complements, but neither preserves STORM's role-conditioned question seeding on its own. | https://arxiv.org/abs/2203.11171; https://www.debono.com/six-thinking-hats-summary; https://aclanthology.org/2024.naacl-long.347/ | medium | Comparison judgment |
| [inference] A four-slot prompt is a strong minimum-viable candidate because it preserves STORM's broad-facts-plus-specialist-lenses pattern while allowing later topic-sensitive refinements. | https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md | low | Design synthesis |
| [inference] The safest integration recommendation is to keep §0.5 additive and scoped to seed-question emission rather than to redesign later stages. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://www.anthropic.com/engineering/building-effective-agents | medium | Integration recommendation |

**Assumptions:**

- [assumption] The minimum-viable version should optimise for preserving perspective seeding, not for reproducing STORM's full multi-turn conversation behavior, because the repository workflow does not run simulated expert dialogues. Justification: the workflow constraint removes the paper's strongest ablated component. Source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents
- [assumption] The topic statement and seeded sources usually contain enough signal for four useful lenses without first scraping related Wikipedia outlines, because the design goal is low-overhead prompt insertion rather than exact parity with STORM's internet-research phase. Justification: Anthropic guidance favors simpler composable workflows when they are adequate. Source: https://www.anthropic.com/engineering/building-effective-agents; https://aclanthology.org/2024.naacl-long.347/

**Analysis:**

STORM's released code and paper align on a narrow interpretation of `perspective discovery`: it is a prompt-driven persona seeding stage that happens before question asking, not a formal optimisation pass over declared diversity dimensions. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py]

That distinction matters because W-0038 cites the paper's +10% breadth gain as if it were the direct output of §0.5 alone, while the ablations show the single largest drop comes from removing simulated conversation rather than from removing perspective conditioning. [inference; source: https://aclanthology.org/2024.naacl-long.347/]

The safest design move is therefore to preserve the part that the repository can realistically inherit, persona-conditioned initial question selection, and to state plainly that the repository is not inheriting STORM's conversation-driven follow-up behavior. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents]

Self-consistency is valuable once competing answer paths already exist, but it does not tell the model which topical lenses to open in the first place. [inference; source: https://arxiv.org/abs/2203.11171; https://aclanthology.org/2024.naacl-long.347/]

Six Thinking Hats provides useful coverage reminders, especially factual, critical, creative, and process modes, but its official method is parallel thinking rather than role multiplexing, so it works better as a post-generation audit than as the primary scaffold. [inference; source: https://www.debono.com/six-thinking-hats-summary]

Anthropic's guidance points toward a short fixed-structure prompt with explicit output slots, which fits the repository's existing deterministic workflow better than a verbose freeform persona-generation instruction. [inference; source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://www.anthropic.com/engineering/building-effective-agents]

Recommended §0.5 prompt block: [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md]

```text
### §0.5 Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research perspectives for the question below.
You are still one researcher. Do not simulate a panel, dialogue, or debate. Your job is to seed better questions.

Use these four slots:
1. Basic facts lens, what a broad factual writer must cover first.
2. Mechanism or implementation lens, how the thing works, is built, or fails operationally.
3. Stakeholder or decision-impact lens, who is affected, who decides, and what trade-offs matter.
4. Failure-mode or critic lens, what could be missing, misleading, risky, or overstated.

For each perspective, output:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer that question>

Constraints:
- Prefer non-overlap over stylistic variety.
- If two perspectives collapse into the same question class, rewrite one.
- Keep every seed question specific enough that §1 can decompose it into atomic sub-questions.
- Do not answer the questions yet.
```

**Risks, gaps, uncertainties:**

- [fact] The paper does not publish a direct experiment showing that a single-agent prompt block can reproduce the reported +10% breadth gain, so any claim of numeric equivalence would be unsupported. Source: https://aclanthology.org/2024.naacl-long.347/
- [fact] STORM's released implementation depends on simulated multi-turn retrieval-grounded conversation, which this repository's minimum-viable prompt does not reproduce. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py
- [inference] The four-slot template may underfit topics whose most important diversity axis is historical or regulatory rather than stakeholder or failure mode, so the slot labels may need light topic-sensitive adjustment during implementation. Source: https://www.anthropic.com/engineering/building-effective-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md

**Open questions:**

- Can the repository evaluate §0.5 locally by measuring question diversity or downstream evidence-map coverage before and after insertion? [inference; source: https://aclanthology.org/2024.naacl-long.347/]
- Would a light `related topics` retrieval step before §0.5 materially outperform the fixed four-slot prompt enough to justify the added complexity? [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents]
- Should Six Thinking Hats be used as a post-§0.5 audit checklist to catch missing question classes without replacing role-conditioned lenses? [inference; source: https://www.debono.com/six-thinking-hats-summary]

### §7 Recursive Review

- Confidence assessment: `medium`.
- Citation audit: completed.
- Review status: two automated review passes completed.
- Remaining uncertainty: the recommended §0.5 prompt block is a design synthesis for this repository and has not yet been benchmarked locally against question-coverage outcomes.

---

## Findings

### Executive Summary

STORM's perspective discovery is a lightweight persona-generation step seeded from related Wikipedia article outlines, not a formal diversity algorithm, and the safest single-agent replication is a fixed perspective-seeding prompt rather than a claim that the full STORM coverage gain will transfer unchanged. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py]

The paper's +10% `broad in coverage` result belongs to end-to-end STORM versus an outline-driven retrieval-augmented generation baseline, while the ablation evidence supports the inference that perspective discovery alone has a smaller but still real effect, especially on source diversity and entity-level outline coverage. [inference; source: https://aclanthology.org/2024.naacl-long.347/]

One strong minimum-viable §0.5 candidate for this repository is an additive four-perspective prompt that emits one seed question per non-overlapping lens and minimizes downstream workflow change, while leaving room for later testing of topic-sensitive slot changes or a light `related topics` retrieval step. [inference; source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://www.anthropic.com/engineering/building-effective-agents]

### Key Findings

1. **STORM discovers perspectives by surveying related Wikipedia pages, extracting their titles and tables of contents, and then prompting the model to invent editor personas that each represent a different perspective, role, or affiliation before any question decomposition begins.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
2. **The released implementation always prepends a `Basic fact writer` persona, which means STORM explicitly combines one broad factual lens with a small set of topic-specific lenses instead of relying only on specialist roles.** ([fact]; medium confidence; source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
3. **STORM does not publish an explicit diversity rubric over disciplinary, cultural, temporal, or stakeholder categories, so its diversity mechanism is implicit and retrieval-primed rather than a formal coverage algorithm with declared quotas.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py)
4. **The paper's +10% `broad in coverage` result should not be attributed to perspective discovery alone, because that number compares full STORM against an outline-driven retrieval-augmented generation baseline and the ablations isolate a smaller persona-specific effect.** ([fact]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/)
5. **The ablation results show that removing perspective conditioning roughly halves the number of unique references collected and lowers entity-level outline recall, while removing simulated conversation hurts performance even more, so the evidence supports the inference that conversation contributes more than persona seeding to overall question quality.** ([inference]; medium confidence; source: https://aclanthology.org/2024.naacl-long.347/)
6. **Self-consistency and Six Thinking Hats are useful comparison points, but neither is a close substitute for STORM's perspective discovery because self-consistency collapses multiple attempts into one answer and Six Thinking Hats organises modes of thought rather than parallel role-conditioned lenses.** ([inference]; medium confidence; source: https://arxiv.org/abs/2203.11171; https://www.debono.com/six-thinking-hats-summary; https://aclanthology.org/2024.naacl-long.347/)
7. **A strong minimum-viable candidate for this repository is a four-slot prompt, `basic facts`, `mechanism or implementation`, `stakeholder or decision impact`, and `failure mode or critic`, with one seed question per perspective, because that preserves STORM's broad-facts-plus-specialist-lenses pattern while keeping the prompt simple and leaving room for later topic-sensitive refinements.** ([inference]; low confidence; source: https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md)
8. **The safest repository recommendation is to keep §0.5 additive by making it emit seed questions for §1 instead of redesigning later stages, because the backlog goal is broader question coverage and Anthropic guidance favors the smallest workflow change that preserves task structure.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://www.anthropic.com/engineering/building-effective-agents])

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] STORM surveys related Wikipedia pages, extracts tables of contents, and generates personas before asking questions. | https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Paper plus code |
| [fact] STORM prepends a `Basic fact writer` persona to topic-specific personas. | https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Code-backed |
| [fact] Diversity criteria are implicit `perspective, role, or affiliation`, not a fixed rubric. | https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py | medium | Prompt-backed |
| [fact] The +10% breadth claim belongs to end-to-end STORM versus outline-driven retrieval-augmented generation, not to the persona step alone. | https://aclanthology.org/2024.naacl-long.347/ | medium | Human-eval claim |
| [inference] Ablations show perspective discovery matters, but conversation appears to matter more, especially for unique references and entity recall. | https://aclanthology.org/2024.naacl-long.347/ | medium | Table 3 plus Table 5 |
| [inference] A four-slot prompt is a strong minimum-viable candidate because it preserves STORM's broad-facts-plus-specialist-lenses pattern while allowing later topic-sensitive refinements. | https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md | low | Design synthesis |
| [inference] The safest integration recommendation is to keep §0.5 additive and scoped to seed-question emission rather than to redesign later stages. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://www.anthropic.com/engineering/building-effective-agents | medium | Integration recommendation |

### Assumptions

- [assumption] The minimum-viable version should optimise for preserving perspective seeding, not for reproducing STORM's full multi-turn conversation behavior, because the repository workflow does not run simulated expert dialogues. Justification: the workflow constraint removes the paper's strongest ablated component. Source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents
- [assumption] The topic statement and seeded sources usually contain enough signal for four useful lenses without first scraping related Wikipedia outlines, because the design goal is low-overhead prompt insertion rather than exact parity with STORM's internet-research phase. Justification: Anthropic guidance favors simpler composable workflows when they are adequate. Source: https://www.anthropic.com/engineering/building-effective-agents; https://aclanthology.org/2024.naacl-long.347/

### Analysis

STORM's released code and paper align on a narrow interpretation of `perspective discovery`: it is a prompt-driven persona seeding stage that happens before question asking, not a formal optimisation pass over declared diversity dimensions. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py]

That distinction matters because W-0038 cites the paper's +10% breadth gain as if it were the direct output of §0.5 alone, while the ablations show the single largest drop comes from removing simulated conversation rather than from removing perspective conditioning. [inference; source: https://aclanthology.org/2024.naacl-long.347/]

The safest design move is therefore to preserve the part that the repository can realistically inherit, persona-conditioned initial question selection, and to state plainly that the repository is not inheriting STORM's conversation-driven follow-up behavior. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents]

Self-consistency is valuable once competing answer paths already exist, but it does not tell the model which topical lenses to open in the first place. [inference; source: https://arxiv.org/abs/2203.11171; https://aclanthology.org/2024.naacl-long.347/]

Six Thinking Hats provides useful coverage reminders, especially factual, critical, creative, and process modes, but its official method is parallel thinking rather than role multiplexing, so it works better as a post-generation audit than as the primary scaffold. [inference; source: https://www.debono.com/six-thinking-hats-summary]

Anthropic's guidance points toward a short fixed-structure prompt with explicit output slots, which fits the repository's existing deterministic workflow better than a verbose freeform persona-generation instruction. [inference; source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://www.anthropic.com/engineering/building-effective-agents]

Recommended §0.5 prompt block: [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents; https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md]

```text
### §0.5 Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research perspectives for the question below.
You are still one researcher. Do not simulate a panel, dialogue, or debate. Your job is to seed better questions.

Use these four slots:
1. Basic facts lens, what a broad factual writer must cover first.
2. Mechanism or implementation lens, how the thing works, is built, or fails operationally.
3. Stakeholder or decision-impact lens, who is affected, who decides, and what trade-offs matter.
4. Failure-mode or critic lens, what could be missing, misleading, risky, or overstated.

For each perspective, output:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer that question>

Constraints:
- Prefer non-overlap over stylistic variety.
- If two perspectives collapse into the same question class, rewrite one.
- Keep every seed question specific enough that §1 can decompose it into atomic sub-questions.
- Do not answer the questions yet.
```

### Risks, Gaps, and Uncertainties

- [fact] The paper does not publish a direct experiment showing that a single-agent prompt block can reproduce the reported +10% breadth gain, so any claim of numeric equivalence would be unsupported. Source: https://aclanthology.org/2024.naacl-long.347/
- [fact] STORM's released implementation depends on simulated multi-turn retrieval-grounded conversation, which this repository's minimum-viable prompt does not reproduce. Source: https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py
- [inference] The four-slot template may underfit topics whose most important diversity axis is historical or regulatory rather than stakeholder or failure mode, so the slot labels may need light topic-sensitive adjustment during implementation. Source: https://www.anthropic.com/engineering/building-effective-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-adversarial-agents-shared-goals-multi-perspective.md

### Open Questions

- Can the repository evaluate §0.5 locally by measuring question diversity or downstream evidence-map coverage before and after insertion? [inference; source: https://aclanthology.org/2024.naacl-long.347/]
- Would a light `related topics` retrieval step before §0.5 materially outperform the fixed four-slot prompt enough to justify the added complexity? [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents]
- Should Six Thinking Hats be used as a post-§0.5 audit checklist to catch missing question classes without replacing role-conditioned lenses? [inference; source: https://www.debono.com/six-thinking-hats-summary]

---

## Output

- Type: knowledge
- Description: This item produces a sourced design note and a minimum-viable §0.5 Perspective Discovery prompt block for the repository's research workflow. [inference; source: https://aclanthology.org/2024.naacl-long.347/; https://www.anthropic.com/engineering/building-effective-agents]
- Links:
  - https://aclanthology.org/2024.naacl-long.347/
  - https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/persona_generator.py
  - https://github.com/stanford-oval/storm/blob/fb951af7744dab086e34962e9bc6fe878e145f83/knowledge_storm/storm_wiki/modules/knowledge_curation.py
