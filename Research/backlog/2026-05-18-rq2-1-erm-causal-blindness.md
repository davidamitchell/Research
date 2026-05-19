---
title: "RQ 2.1 — Empirical Risk Minimisation's Causal Blindness and the Limits of In-Distribution Guarantees"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-3-predictive-model-fragility
tags: [machine-learning, causal-inference, epistemology, formal-methods]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
related:
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
  - 2026-05-18-rq2-2-duhem-quine-underdetermination
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 2.1 — Empirical Risk Minimisation's Causal Blindness and the Limits of In-Distribution Guarantees

## Research Question

How does the framework of Empirical Risk Minimisation (ERM) mathematically guarantee predictive accuracy within a known data distribution while remaining completely blind to the causal mechanisms necessary for out-of-distribution (OOD) generalisation?

## Scope

**In scope:**
- Mathematical guarantees of ERM within the training distribution (PAC-learning bounds)
- Formal characterisation of ERM's OOD failure modes
- Spurious correlations as the mechanism by which ERM produces causally blind solutions
- Invariant Risk Minimisation (IRM) as a causal alternative to ERM
- Inductive biases of gradient descent that favour spurious correlations

**Out of scope:**
- Implementation details of specific optimisers
- Empirical benchmarks of IRM vs ERM on specific datasets

**Constraints:** Must connect to Phase 1 epistemological foundations; mathematical treatment is required alongside conceptual explanation.

## Context

Phase 1 established the epistemological distinction between mechanistic explanation and interpolation. Phase 2 now operationalises this distinction in the language of machine learning theory. ERM is the dominant training paradigm across modern machine learning — including deep learning and large language models (LLMs). Understanding why ERM is causally blind is the mathematical core of the entire research programme. This item enables RQ 2.2 and RQ 2.3 to build precise formal comparisons.

## Approach

1. State the ERM objective formally and its PAC-learning guarantees within a fixed distribution.
2. Construct a formal counter-example: show a dataset where ERM finds a causally wrong but in-distribution-accurate solution.
3. Examine spurious correlation as the mechanism: the training environment selects features that correlate with labels without capturing the causal arrow.
4. Survey Arjovsky et al. (2019) Invariant Risk Minimisation (IRM) as the formal correction.
5. Characterise the inductive bias of gradient descent — why it prefers the simplest (often causally incorrect) solution under ERM.

## Sources

- [ ] [Arjovsky, M. et al. (2019) Invariant Risk Minimization — arXiv:1907.02893](https://arxiv.org/abs/1907.02893) — formal causal alternative to ERM; defines the OOD failure mode of ERM
- [ ] [Schölkopf, B. et al. (2021) Toward Causal Representation Learning — Proceedings of the IEEE Vol 109](https://doi.org/10.1109/JPROC.2021.3058954) — framework for causal representation as an alternative to ERM
- [ ] [Shalev-Shwartz, S. & Ben-David, S. (2014) Understanding Machine Learning — Cambridge University Press](https://doi.org/10.1017/CBO9781107298019) — formal treatment of PAC-learning and ERM guarantees
- [ ] [Geirhos, R. et al. (2020) Shortcut Learning in Deep Neural Networks — Nature Machine Intelligence Vol 2](https://doi.org/10.1038/s42256-020-00257-z) — empirical evidence of spurious correlations under ERM

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
