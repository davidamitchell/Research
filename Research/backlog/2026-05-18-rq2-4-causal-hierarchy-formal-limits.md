---
title: "RQ 2.4 — Pearl's Causal Hierarchy: Information-Theoretic Limits on Observational Data for Intervention and Counterfactual Reasoning"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
tags: [causal-inference, machine-learning, formal-methods, epistemology]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-3-predictive-model-fragility
related:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-3-predictive-model-fragility
  - 2026-05-18-rq3-1-llm-statistical-vs-causal
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 2.4 — Pearl's Causal Hierarchy: Information-Theoretic Limits on Observational Data for Intervention and Counterfactual Reasoning

## Research Question

What are the formal information-theoretic boundaries that prevent a model trained exclusively on observational data (Level 1 on Pearl's Ladder of Causation) from ever executing or predicting the outcomes of structural interventions (Level 2) or counterfactuals (Level 3)?

## Scope

**In scope:**
- Pearl's Ladder of Causation: Association (Level 1), Intervention (Level 2), Counterfactuals (Level 3)
- The Causal Hierarchy Theorem and its formal proof
- Information-theoretic lower bounds on what observational data can determine
- Observational vs. interventional distributions and the do-calculus
- Confounding bias as a mechanism preventing Level 1 → Level 2 inference

**Out of scope:**
- Practical causal discovery algorithms (e.g., PC, FCI)
- Specific applications of causal inference to medical trials or policy evaluation

**Constraints:** This is the synthesis item for Phase 2; it must integrate findings from RQ 2.1, 2.2, and 2.3 into a unified formal statement about the limits of observational learning.

## Context

The three preceding items in Phase 2 have established, from different angles, that purely observational/predictive models are epistemically limited. RQ 2.4 synthesises these findings into a single formal theorem: Pearl's Causal Hierarchy Theorem. This theorem proves that no algorithm operating only on observational data (Level 1) can answer questions about interventions (Level 2) or counterfactuals (Level 3) without additional causal assumptions. This is the formal bedrock for Phase 3's analysis of LLMs and Phase 4's analysis of agentic systems — both are trained exclusively on observational data.

## Approach

1. Formally define all three levels of Pearl's Ladder of Causation: P(Y | X), P(Y | do(X)), P(Y_x | X', Y').
2. State and prove the Causal Hierarchy Theorem (Bareinboim et al. 2020): observational distribution cannot uniquely determine interventional or counterfactual distributions.
3. Characterise confounding bias: when does observational correlation systematically mislead interventional prediction?
4. Formalise the do-calculus as the complete set of rules for converting interventional queries into observational ones (when possible).
5. Apply the theorem to deep learning: show that ERM models are Level 1 and cannot reach Levels 2 or 3 without structural assumptions.

## Sources

- [ ] [Bareinboim, E. et al. (2020) On Pearl's Hierarchy of Causation: Formal Foundations and Implications for AI — ACM FACCT 2022](https://doi.org/10.1145/3531146.3533229) — formal proof and implications of the Causal Hierarchy Theorem
- [ ] [Peters, J. et al. (2017) Elements of Causal Inference — MIT Press](https://doi.org/10.7551/mitpress/9999.001.0001) — comprehensive treatment of causal inference foundations
- [ ] [Pearl, J. (2000) Causality: Models, Reasoning, and Inference — Cambridge University Press](https://doi.org/10.1017/CBO9780511803161) — original formulation of the do-calculus and causal hierarchy
- [ ] [Pearl, J. & Mackenzie, D. (2018) The Book of Why — Basic Books](https://www.basicbooks.com/titles/judea-pearl/the-book-of-why/9780465097609/) — accessible exposition of the causal hierarchy with worked examples

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
