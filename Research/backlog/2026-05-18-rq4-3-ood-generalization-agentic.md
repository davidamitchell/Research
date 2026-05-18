---
title: "RQ 4.3 — Formal OOD Generalisation Bounds for Agentic Architectures Under Non-Deterministic Tool Outputs"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
tags: [agentic-ai, llm, machine-learning, formal-methods, evaluation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
  - 2026-05-18-rq4-2-adversarial-error-propagation
related:
  - 2026-05-18-rq4-1-agentic-loop-explanatory-reach
  - 2026-05-18-rq4-2-adversarial-error-propagation
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 4.3 — Formal OOD Generalisation Bounds for Agentic Architectures Under Non-Deterministic Tool Outputs

## Research Question

What are the formal bounds of out-of-distribution (OOD) generalisation for agentic architectures when managing non-deterministic tool outputs under unconstrained production conditions?

## Scope

**In scope:**
- Epistemic vs. aleatoric uncertainty in agentic system outputs: what can be reduced by more data vs. what is irreducibly random
- Bounded rationality as a formal framework for agentic decision-making under uncertainty
- Uncertainty quantification (UQ) in deep learning applied to agentic loop outputs
- Dropout as a Bayesian approximation (Gal & Ghahramani): does this provide valid uncertainty estimates for agentic decisions?
- Formal OOD generalisation bounds for LLM-based planners

**Out of scope:**
- Specific production observability tooling
- Human-in-the-loop mitigation strategies

**Constraints:** Synthesises Phase 4; must provide formal bounds (not just qualitative assessment) and connect to Phase 5 via the stochastic vs. deterministic comparison.

## Context

RQ 4.1 and RQ 4.2 established that agentic loops do not overcome the causal blindness of their core LLM and that adversarial inputs cascade through verification. RQ 4.3 asks: what are the formal limits? In production systems, tool outputs are non-deterministic (web search results, API responses, real-time data). The agentic system must manage uncertainty it cannot model causally. This item derives formal OOD generalisation bounds and characterises the types of uncertainty that are reducible vs. irreducible — the foundation for Phase 5's comparison with coded deterministic systems.

## Approach

1. Distinguish epistemic uncertainty (reducible: due to insufficient data) from aleatoric uncertainty (irreducible: inherent in the process) for agentic system outputs.
2. Apply bounded rationality (Simon): what does optimal decision-making under uncertainty look like when the agent cannot model the causal structure?
3. Survey uncertainty quantification methods applicable to LLM-based agents: Bayesian neural networks, MC Dropout (Gal & Ghahramani), conformal prediction.
4. Derive formal OOD generalisation bounds for agentic architectures: under what conditions can we guarantee the agent's outputs are within an acceptable error range?
5. Identify: which classes of tool non-determinism are manageable by the agentic loop, and which are not?

## Sources

- [ ] [Gal, Y. & Ghahramani, Z. (2016) Dropout as a Bayesian Approximation — ICML 2016](https://arxiv.org/abs/1506.02142) — primary source for uncertainty quantification in deep neural networks via MC Dropout
- [ ] [Simon, H. A. (1955) A Behavioral Model of Rational Choice — Quarterly Journal of Economics Vol 69](https://doi.org/10.2307/1884852) — bounded rationality as a formal framework for decision-making under computational and epistemic limits
- [ ] [Angelopoulos, A. N. & Bates, S. (2021) A Gentle Introduction to Conformal Prediction — arXiv:2107.07511](https://arxiv.org/abs/2107.07511) — distribution-free uncertainty quantification; applicable to agentic output calibration
- [ ] [Kendall, A. & Gal, Y. (2017) What Uncertainties Do We Need in Bayesian Deep Learning? — NeurIPS 2017](https://arxiv.org/abs/1703.04977) — formal distinction between epistemic and aleatoric uncertainty in deep learning

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
