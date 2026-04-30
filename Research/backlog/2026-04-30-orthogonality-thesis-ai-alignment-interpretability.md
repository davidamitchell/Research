---
title: "The orthogonality thesis in Artificial Intelligence (AI) alignment: intelligence, goals, and the limits of interpretability"
added: 2026-04-30T06:52:37+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []
tags: [alignment, governance, explainability, ai-safety, llm, mechanistic-interpretability]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-04-30-explainable-ai-xai-regulation-governance, 2026-04-30-human-bias-ai-trust-rlhf-sycophancy, 2026-04-02-claude-mythos]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# The orthogonality thesis in Artificial Intelligence (AI) alignment: intelligence, goals, and the limits of interpretability

## Research Question

What is the orthogonality thesis in Artificial Intelligence (AI) alignment, what is the current evidence for and against it, and what are its practical implications for Explainable Artificial Intelligence (XAI) — specifically whether explaining *what* a model did is sufficient when the thesis implies we cannot infer *why* (in a goal-sense) from capability or output alone?

## Scope

**In scope:**
- The orthogonality thesis as articulated by Nick Bostrom (2012, 2014): any level of intelligence can in principle be combined with any terminal goal; intelligence and goals are orthogonal
- Instrumental convergence thesis (Omohundro, Bostrom): convergent instrumental goals that almost any sufficiently capable AI will develop regardless of terminal goal (self-preservation, goal-content integrity, resource acquisition)
- Current state of the debate: philosophical critiques (corrigibility, value loading as a constraint on orthogonality), empirical challenges (do LLMs exhibit goal-like behaviour? RLHF aligns behaviour not goals), and mechanistic interpretability as a potential empirical test
- Relationship to feature superposition (Anthropic): if internal representations are polysemantic and compressed, can we recover terminal goals from weights even in principle?
- Implications for regulated industries: what does the thesis imply for audit and accountability — specifically, can an audit conclude that a system "acted with intent" or only that it "produced output consistent with a pattern"?
- Connection to alignment research programmes: Anthropic Constitutional AI (CAI), OpenAI Superalignment, DeepMind MIRI-adjacent work

**Out of scope:**
- Full treatment of human cognitive bias toward AI explanations — see related item `2026-04-30-human-bias-ai-trust-rlhf-sycophancy`
- Consciousness and sentience debates
- Specific RLHF training mechanics — covered in the human bias item
- Speculative superintelligence scenarios beyond what is needed to understand the regulatory and audit framing

**Constraints:**
- Ground claims in published philosophy of mind, AI safety literature, and empirical mechanistic interpretability work
- Flag clearly which claims are philosophical argument vs. empirical finding

## Context

The orthogonality thesis, originally a philosophical argument in AI safety discourse, has direct practical relevance to explainable AI governance. If intelligence (capability) and goals (motivation) are genuinely orthogonal, then explaining the *output* of a model does not explain its *objective function*. Regulators who demand explainability for automated decisions are implicitly assuming that explaining the decision chain reveals something about the system's "intent" — an assumption the orthogonality thesis directly challenges. This tension is sharpest in agentic AI systems that pursue multi-step plans, where attribution of "why" a chain of actions was taken becomes increasingly important as stakes rise.

The thesis also intersects with mechanistic interpretability: if we can recover the true goal representation from model weights, orthogonality is not just a philosophical concern but an empirical obstacle. Anthropic's superposition hypothesis suggests this recovery is non-trivially hard even for simple toy models.

This item should be read alongside `2026-04-30-explainable-ai-xai-regulation-governance` (XAI landscape) and `2026-04-30-human-bias-ai-trust-rlhf-sycophancy` (human trust biases).

## Approach

1. **Original formulation** — Review Bostrom's formulation of the orthogonality thesis (Superintelligence, 2014; earlier paper 2012). Review Omohundro's convergent instrumental goals. Establish the philosophical baseline.

2. **Empirical status** — What does current LLM behaviour reveal about the thesis? Do LLMs exhibit stable goal-like representations? Survey mechanistic interpretability findings on goal representations in transformers (Nanda et al.; Lieberum et al. on goal misgeneralisation); review Hubinger et al. (2019) on deceptive alignment as the extreme case.

3. **Connection to superposition and polysemanticity** — If terminal goals are represented in superposition alongside other features (Elhage et al., 2022 toy model), what does this mean for our ability to extract or verify goals? Is goal-probing feasible?

4. **Critiques and counter-arguments** — Review philosophical critiques of orthogonality: value loading problem (Stuart Russell's cooperative inverse reinforcement learning framing); whether RLHF effectively constrains the thesis in practice; mesa-optimisation framing (inner vs. outer alignment). Assess whether the thesis remains as open as Bostrom stated.

5. **Regulatory and audit implications** — What should auditors and regulators conclude? Can "intent" be established for an automated decision? Review how existing legal frameworks (EU AI Act Article 9 risk management, UK FCA model risk guidance) handle the intent question. Produce a concise framing of what is and is not auditable given the thesis.

## Sources

- [ ] [Bostrom (2012) — The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents](https://nickbostrom.com/superintelligentwill.pdf) — original orthogonality thesis paper
- [ ] [Bostrom (2014) — Superintelligence: Paths, Dangers, Strategies](https://www.oxfordscholarship.com/view/10.1093/acprof:oso/9780199678112.001.0001/acprof-9780199678112) — full book-length treatment; Chapter 7 (The Orthogonality Thesis) and Chapter 8 (The Instrumental Convergence Thesis)
- [ ] [Omohundro (2008) — The Basic AI Drives](https://selfawaresystems.files.wordpress.com/2008/01/ai_drives_final.pdf) — instrumental convergence; convergent sub-goals for capable AI
- [ ] [Hubinger et al. (2019) — Risks from Learned Optimization in Advanced Machine Learning Systems](https://arxiv.org/abs/1906.01820) — deceptive alignment; mesa-optimisation; inner vs. outer alignment
- [ ] [Elhage et al. (2022) — Toy Models of Superposition (Anthropic)](https://transformer-circuits.pub/2022/toy_model/index.html) — superposition; goal representations in compressed feature spaces
- [ ] [Nanda et al. (2023) — Progress measures for grokking via mechanistic interpretability](https://arxiv.org/abs/2301.05217) — mechanistic interpretability; recovery of learned algorithms from weights
- [ ] [Lieberum et al. (2023) — Does Circuit Analysis Interpretability Scale? A Case Study on Sparse Autoencoders in Language Models](https://arxiv.org/abs/2307.09458) — empirical limits of circuit analysis as a goal-recovery technique
- [ ] [Russell (2019) — Human Compatible: Artificial Intelligence and the Problem of Control](https://www.penguinrandomhouse.com/books/566677/human-compatible-by-stuart-russell/) — cooperative inverse reinforcement learning as an alternative to orthogonality; value alignment framing
- [ ] [EU AI Act Article 9 — Risk Management System (2024)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) — regulatory framing of risk management obligations relevant to intent attribution
