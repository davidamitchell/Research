---
title: "RQ 3.1 — LLMs as Statistical Optimisers: Token Distribution vs. Invariant Causal Models of Reality"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq3-2-stochastic-parrot-ood
tags: [llm, machine-learning, causal-inference, epistemology]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq2-1-erm-causal-blindness
related:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
  - 2026-05-18-rq3-2-stochastic-parrot-ood
  - 2026-05-18-rq3-3-cot-counterfactual-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 3.1 — LLMs as Statistical Optimisers: Token Distribution vs. Invariant Causal Models of Reality

## Research Question

To what extent do Large Language Models (LLMs) optimise strictly for linguistic form and statistical token distribution rather than constructing internal, invariant causal models of reality?

## Scope

**In scope:**
- Distributional semantics (Firth's Hypothesis: "You shall know a word by the company it keeps") as the theoretical basis of LLM training
- Spurious correlations in high-dimensional text spaces as a natural consequence of token-level optimisation
- The Linear Representation Hypothesis: what geometry of internal representations would be necessary for causal reasoning?
- Empirical evidence for and against LLMs constructing invariant causal representations
- Connection to Phase 2's ERM and causal hierarchy analysis

**Out of scope:**
- Fine-tuning, reinforcement learning from human feedback (RLHF), and alignment techniques
- Specific LLM architectures (Transformer internals are supporting context, not the primary focus)

**Constraints:** Builds directly on Phase 2 (especially RQ 2.4 — the Causal Hierarchy Theorem); must ground claims in formal properties rather than anecdote.

## Context

Phase 2 established the formal impossibility: a model trained on observational data cannot acquire interventional or counterfactual reasoning without additional causal structure. Phase 3 now applies this to Large Language Models (LLMs). LLMs are trained on massive corpora using next-token prediction — a Level 1 causal hierarchy task. This item asks whether the scale and architecture of LLMs could somehow transcend this formal barrier. It opens the LLM-specific analysis that runs through RQ 3.2 and 3.3 and directly motivates Phase 4's analysis of agentic wrapping.

## Approach

1. Characterise LLM training as an ERM problem over token distributions (formally: minimise cross-entropy on next-token prediction).
2. Apply Firth's Hypothesis: the distributional semantic signal available from text corpora is inherently Level 1 (association, not intervention).
3. Examine the Linear Representation Hypothesis: would linear probes for causal structure in LLM activations constitute evidence of causal modelling?
4. Survey empirical studies testing whether LLMs acquire causal representations (e.g., do they learn physical laws, or lexical proxies for them?).
5. Summarise: where does the evidence place LLMs on Pearl's causal hierarchy?

## Sources

- [ ] [Bender, E. M. et al. (2021) On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? — FAccT 2021](https://doi.org/10.1145/3442188.3445922) — primary source for the "Stochastic Parrot" hypothesis; form over meaning critique
- [ ] [Firth, J. R. (1957) A Synopsis of Linguistic Theory 1930–1955 — Studies in Linguistic Analysis](https://aclanthology.org/2020.coling-main.532) — original distributional semantics hypothesis underlying LLM training objectives
- [ ] [Nanda, N. et al. (2023) Progress Measures for Grokking via Mechanistic Interpretability — ICLR 2023](https://arxiv.org/abs/2301.05217) — mechanistic interpretability evidence on what LLMs learn internally
- [ ] [Kambhampati, S. et al. (2024) Can Large Language Models Reason and Plan? — Annals of the New York Academy of Sciences](https://doi.org/10.1111/nyas.15125) — empirical assessment of LLM causal and planning capabilities

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

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type: knowledge
- Description:
- Links:
