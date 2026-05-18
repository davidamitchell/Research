---
title: "Are Agentic Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Coded Systems?"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-agentic-production-tradeoffs
tags: [agentic-ai, llm, formal-methods, epistemology, evaluation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
related:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
  - 2026-05-18-agentic-production-tradeoffs
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Are Agentic Systems Inherently Less Explainable Than Equivalently Scoped Deterministic Coded Systems?

## Research Question

Are agentic systems (LLM-based, stochastic) inherently less explainable than equivalently scoped deterministic coded systems, or does the Complexity Horizon of classical architectures converge the two systems to equivalent levels of epistemic opacity at real-world production scale?

## Scope

**In scope:**
- Defining "explainability" formally in terms applicable to both system types: ability to trace a decision path, predict behaviour from specification, and reconstruct failure causes post-hoc
- Structured comparison across three explainability dimensions: local (single decision), global (overall policy), and contrastive (why X rather than Y)
- Whether the Complexity Horizon of classical microservice architectures (RQ 6.3) produces the same practical level of opacity as LLM non-determinism
- Formal characterisation of what "inherently" means: is reduced explainability a necessary structural property of agentic systems, or a contingent one (dependent on scale, tooling, design patterns)?
- Evidence from post-hoc explainability methods applied to both system types

**Out of scope:**
- Technical implementations of specific interpretability tools (SHAP, LIME, attention visualisation)
- Proposals for improving explainability in either system class

**Constraints:** This is a synthesis item; it depends on all of Phases 5 and 6 being complete. The question must be answered with formal rigour: "inherently" must be tested as a structural claim, not a qualitative impression.

## Context

Phase 5 compared how agentic and coded systems fail. Phase 6 established that classical systems are not trivially explainable — the Complexity Horizon creates real epistemic barriers. This item asks the pointed comparative question that emerges from those findings: is the explainability deficit of agentic systems *inherent* (structural), or is it merely a current-state-of-tooling deficit that is qualitatively no different from the opacity of a deeply nested microservice mesh? The answer determines how seriously to take explainability as a differentiating concern when choosing between system architectures.

## Approach

1. Construct a formal definition of explainability that is applicable to both agentic and coded systems: decompose into local, global, and contrastive explainability as per interpretability literature.
2. Score agentic systems on each dimension using evidence from Phases 3, 4, and 5.
3. Score classical microservice architectures on each dimension using evidence from Phase 6.
4. Test the "inherency" claim: is the explainability gap between the two classes a function of scale, or does it persist at all scopes?
5. Adjudicate: produce a structured comparative verdict with explicit confidence ratings for each claim.

## Sources

- [ ] [Doshi-Velez, F. & Kim, B. (2017) Towards a Rigorous Science of Interpretable Machine Learning — arXiv:1702.08608](https://arxiv.org/abs/1702.08608) — formal framework for defining and measuring interpretability applicable to both system classes
- [ ] [Lipton, Z. C. (2018) The Mythos of Model Interpretability — ACM Queue Vol 16 No 3](https://doi.org/10.1145/3236386.3241340) — critical analysis of what "interpretability" actually means across different system types
- [ ] [Wachter, S. et al. (2017) Counterfactual Explanations Without Opening the Black Box — Harvard Journal of Law & Technology Vol 31](https://doi.org/10.2139/ssrn.3063289) — contrastive and counterfactual explanation as a formal explainability method
- [ ] [Dekker, S. (2011) Drift into Failure — Ashgate Publishing](https://www.routledge.com/Drift-into-Failure/Dekker/p/book/9781409422211) — epistemic opacity in classical systems from a systems theory perspective

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
