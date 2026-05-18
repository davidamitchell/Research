---
title: "RQ 2.3 — Structural Stability vs. Predictive Fragility: Dynamical Systems Theory and the Cost of Noise"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
tags: [machine-learning, formal-methods, causal-inference, epistemology]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
related:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 2.3 — Structural Stability vs. Predictive Fragility: Dynamical Systems Theory and the Cost of Noise

## Research Question

Using the tools of dynamical systems theory, how does the fragility of a purely predictive model subjected to input noise or system drift differ from the structural stability of a model anchored in invariant physical mechanisms?

## Scope

**In scope:**
- Structural stability (Andronov-Pontryagin criterion) as a formal property of dynamical system models
- Sensitivity analysis of predictive models under input perturbation
- Distribution shift propagation: how small input changes cascade through causally ungrounded models
- Contrast between models with structurally stable attractor basins vs. causally ungrounded interpolators

**Out of scope:**
- Numerical stability of specific optimisation algorithms
- Hardware-level perturbation or adversarial machine learning attacks (covered in Phase 4)

**Constraints:** Must build on RQ 2.1's ERM analysis; use dynamical systems formalism from Thom and Strogatz.

## Context

RQ 2.1 established that ERM is causally blind. RQ 2.2 showed that multiple mechanisms are consistent with any finite dataset. This item asks: what are the practical consequences for a purely predictive model when the world drifts? Dynamical systems theory provides a formal answer via the Andronov-Pontryagin structural stability criterion. A model grounded in invariant causal mechanisms exhibits qualitatively stable behaviour under small perturbations; a model that merely interpolates observational data does not. This fragility is a mathematical consequence, not an implementation detail.

## Approach

1. Define structural stability (Andronov-Pontryagin) in the context of dynamical system models.
2. Formalise sensitivity to initial conditions: how a small change in input propagates through the output space of a causally ungrounded model.
3. Apply the framework to a concrete example: compare a physics-informed model (structurally stable) against a neural network interpolator (structurally fragile) under input drift.
4. Examine distribution shift propagation formally: when do small distribution changes cause qualitative behavioural changes in a predictive model?
5. Summarise: what formal property distinguishes a stable mechanistic model from a fragile interpolative one?

## Sources

- [ ] [Thom, R. (1975) Structural Stability and Morphogenesis — W. A. Benjamin](https://archive.org/details/structuralstabil00thom) — formal framework for structural stability in dynamical systems
- [ ] [Strogatz, S. H. (2014) Nonlinear Dynamics and Chaos — Westview Press](https://doi.org/10.1201/9780429492563) — accessible treatment of nonlinear dynamics, chaos, and structural stability
- [ ] [Andronov, A. A. & Pontryagin, L. S. (1937) Systèmes Grossiers — Doklady Akademii Nauk SSSR Vol 14](https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=dan&paperid=21) — original formulation of structural stability (Andronov-Pontryagin)
- [ ] [Sugiyama, M. et al. (2012) Machine Learning in Non-Stationary Environments — MIT Press](https://doi.org/10.7551/mitpress/9780262017091.001.0001) — formal treatment of distribution shift and covariate shift in machine learning

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
