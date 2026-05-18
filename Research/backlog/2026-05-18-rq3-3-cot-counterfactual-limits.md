---
title: "RQ 3.3 — In-Context Learning and Chain-of-Thought Prompting: Genuine Causal Reasoning or Extended Statistical Interpolation?"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
tags: [llm, machine-learning, evaluation, causal-inference]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
  - 2026-05-18-rq3-2-stochastic-parrot-ood
related:
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
  - 2026-05-18-rq3-2-stochastic-parrot-ood
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 3.3 — In-Context Learning and Chain-of-Thought Prompting: Genuine Causal Reasoning or Extended Statistical Interpolation?

## Research Question

What are the empirical boundaries of in-context learning and Chain-of-Thought (CoT) prompting when attempting to force a purely predictive, statistical architecture to resolve counterfactual problems?

## Scope

**In scope:**
- In-context learning (ICL) as a mechanism: what computational process underlies it?
- Chain-of-Thought (CoT) prompting: does generating intermediate reasoning steps produce structural causal reasoning or sequential conditional probability estimation?
- Autoregressive error accumulation in multi-step CoT sequences
- Spurious reasoning trajectories: cases where CoT produces a correct final answer via an incorrect causal path
- Formal test: can CoT prompting cause an LLM to answer Level 2 or Level 3 questions on Pearl's causal hierarchy?

**Out of scope:**
- Fine-tuning approaches that explicitly incorporate causal data structures
- Practical prompting heuristics for improving LLM accuracy

**Constraints:** Must interpret results in terms of Pearl's causal hierarchy (from RQ 2.4) and the Stochastic Parrot findings (RQ 3.2).

## Context

RQ 3.2 showed that LLMs fail systematically on OOD logical prompts. CoT prompting is widely cited as the technique that enables LLMs to "reason." This item investigates whether CoT actually introduces causal reasoning or whether it is an optimisation trick that increases compute per token by generating plausible conditional next-step predictions — which still lie on Level 1 of Pearl's hierarchy. This is the bridge into Phase 4: if CoT does not introduce genuine causal reach, then agentic loops that compose CoT steps cannot do so either.

## Approach

1. Formally characterise in-context learning as a computational process: does ICL perform Bayesian inference, gradient descent, or something else?
2. Characterise CoT as a sequence of conditional probability estimations: P(step_n+1 | all prior steps, problem).
3. Test whether CoT enables genuine Level 2 reasoning: find documented cases where CoT answers an interventional prompt correctly and cases where it produces a plausible but causally incorrect reasoning chain.
4. Analyse autoregressive error accumulation: how does error probability compound over N CoT steps?
5. Classify CoT: does it cross any boundary on Pearl's causal hierarchy, or does it remain Level 1 with extended compute?

## Sources

- [ ] [Wei, J. et al. (2022) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — NeurIPS 2022](https://arxiv.org/abs/2201.11903) — primary empirical evidence for CoT improving reasoning performance
- [ ] [Pearl, J. & Mackenzie, D. (2018) The Book of Why — Basic Books](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/) — causal hierarchy framework for classifying CoT outputs
- [ ] [Akyürek, E. et al. (2022) What learning algorithm is in-context learning? Investigations with linear models — arXiv:2211.15661](https://arxiv.org/abs/2211.15661) — formal analysis of what computational process ICL implements
- [ ] [Zeiler, M. & Fergus, R. (2014) Visualizing and Understanding Convolutional Networks — ECCV 2014](https://doi.org/10.1007/978-3-319-10590-1_53) — supporting evidence on the gap between model capability and mechanistic understanding

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
