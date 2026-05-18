---
title: "RQ 2.2 — The Duhem-Quine Thesis and Underdetermination: Quantifying When a Model Has Matched the True Mechanism"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
tags: [epistemology, philosophy-of-science, machine-learning, causal-inference, formal-methods]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq2-1-erm-causal-blindness
related:
  - 2026-05-18-rq2-1-erm-causal-blindness
  - 2026-05-18-rq2-3-predictive-model-fragility
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 2.2 — The Duhem-Quine Thesis and Underdetermination: Quantifying When a Model Has Matched the True Mechanism

## Research Question

How can the phenomenon of multiple distinct functions perfectly interpolating identical data points be formalised through the lens of the Duhem-Quine thesis (underdetermination of theory by data), and what are the quantitative metrics for evaluating when a model has matched the *true* mechanism rather than an observationally equivalent proxy?

## Scope

**In scope:**
- Duhem-Quine underdetermination thesis as a formal characterisation of the model selection problem
- Observational equivalence in dynamical systems: multiple models producing identical outputs from identical inputs
- Structural identifiability as a formal criterion for distinguishing true mechanisms from proxies
- Quantitative metrics (identifiability conditions, causal sufficiency) for mechanism matching

**Out of scope:**
- General philosophy of science debates about scientific realism
- Practical model selection heuristics without formal grounding

**Constraints:** Builds directly on RQ 2.1's ERM analysis; must provide quantitative criteria rather than purely philosophical framing.

## Context

RQ 2.1 showed that ERM can find causally wrong models that are observationally accurate in-distribution. This item formalises the deeper reason: the training data underdetermines the true model. The Duhem-Quine thesis provides the epistemological framework; structural identifiability provides the mathematical tool. Together, they answer: under what conditions can we even claim that a model has recovered the true mechanism? This is the theoretical foundation for understanding why LLMs (Phase 3) cannot be assumed to have learned causal structure.

## Approach

1. State the Duhem-Quine thesis formally: for any finite dataset, infinitely many theories are consistent with the data.
2. Formalise observational equivalence in dynamical systems using the Bongard-Lipson framework.
3. Survey structural identifiability theory: under what conditions does a dynamical system's parameters uniquely determine its observable outputs (and vice versa)?
4. Develop quantitative criteria for mechanism identification beyond observational accuracy.
5. Apply the framework: can deep learning models satisfy structural identifiability conditions?

## Sources

- [ ] [Quine, W. V. O. (1951) Two Dogmas of Empiricism — Philosophical Review Vol 60 No 1](https://doi.org/10.2307/2181906) — primary source for the Duhem-Quine underdetermination thesis
- [ ] [Bongard, J. & Lipson, H. (2007) Automated reverse engineering of nonlinear dynamical systems — PNAS Vol 104 No 24](https://doi.org/10.1073/pnas.0609476104) — automated discovery of mechanisms; demonstrates observational equivalence in practice
- [ ] [Raue, A. et al. (2009) Structural and practical identifiability analysis of partially observed dynamical models — Bioinformatics Vol 25 No 15](https://doi.org/10.1093/bioinformatics/btp358) — formal structural identifiability analysis
- [ ] [Peters, J. et al. (2017) Elements of Causal Inference — MIT Press](https://doi.org/10.7551/mitpress/9999.001.0001) — causal sufficiency conditions and identifiability in causal models

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
