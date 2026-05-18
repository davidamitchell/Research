---
title: "RQ 6.2 — State Space Explosion and Deterministic Chaos: Fragility Shared Between Concurrent Coded Systems and Machine Learning Models"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
tags: [formal-methods, machine-learning, distributed-systems, epistemology]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq6-1-halting-problem-static-analysis
related:
  - 2026-05-18-rq6-1-halting-problem-static-analysis
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
  - 2026-05-18-rq2-3-predictive-model-fragility
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 6.2 — State Space Explosion and Deterministic Chaos: Fragility Shared Between Concurrent Coded Systems and Machine Learning Models

## Research Question

How do State Space Explosion in concurrent systems and Chaos Theory (Sensitivity to Initial Conditions) in deterministic algorithms mirror the fragility of machine learning models when subjected to minor input perturbations?

## Scope

**In scope:**
- State space explosion in concurrent systems: the combinatorial growth of reachable states in multi-threaded programs
- Race conditions and concurrency anomalies as manifestations of state space explosion at runtime
- Deterministic chaos (Lorenz Attractor, Butterfly Effect): how deterministic systems exhibit sensitive dependence on initial conditions
- Formal comparison: does perturbation sensitivity in ML models (adversarial examples) share the mathematical structure of chaotic sensitivity in deterministic algorithms?
- Lamport's logical clocks as a partial ordering solution to concurrency non-determinism

**Out of scope:**
- Numerical chaos in floating-point arithmetic (a narrower technical topic)
- Chaos in biological or physical systems beyond what directly illuminates software system properties

**Constraints:** Builds on RQ 6.1's undecidability foundations; must connect to RQ 2.3's structural stability analysis as a bridge between the two tracks.

## Context

RQ 6.1 established that static analysis cannot determine non-trivial semantic properties of programs. This item examines how deterministic programs behave dynamically: even if we could fully specify a concurrent program, state space explosion makes it practically unverifiable, and chaotic sensitivity makes its outputs unpredictable under small input changes. The key insight is that this fragility is not unique to ML models — it is a property of complex deterministic systems. This creates an unexpected parallel with RQ 2.3 (ML model fragility) that will be crucial for the Phase 5 comparison.

## Approach

1. Define state space explosion formally: in a concurrent system with N threads, the reachable state space grows exponentially; quantify this growth.
2. Analyse race conditions as manifestations of state space explosion: non-deterministic interleavings that produce qualitatively different outputs.
3. Introduce deterministic chaos via the Lorenz (1963) attractor: a deterministic system that is practically unpredictable due to sensitive dependence.
4. Establish the mathematical parallel: sensitive dependence on initial conditions in chaotic systems vs. sensitivity to input perturbations in adversarially attacked ML models.
5. Apply Lamport's logical clocks as a partial ordering constraint; show what can and cannot be guaranteed even with clock-based ordering.

## Sources

- [ ] [Lorenz, E. N. (1963) Deterministic Nonperiodic Flow — Journal of the Atmospheric Sciences Vol 20](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2) — original discovery of deterministic chaos and sensitive dependence on initial conditions
- [ ] [Lamport, L. (1978) Time, Clocks, and the Ordering of Events in a Distributed System — Communications of the ACM Vol 21](https://doi.org/10.1145/359545.359563) — logical clocks as a formal tool for managing concurrency non-determinism
- [ ] [Clarke, E. M. et al. (2018) Model Checking — MIT Press](https://mitpress.mit.edu/9780262038553/model-checking/) — state space explosion problem in model checking; formal analysis of its intractability
- [ ] [Goodfellow, I. J. et al. (2014) Explaining and Harnessing Adversarial Examples — arXiv:1412.6572](https://arxiv.org/abs/1412.6572) — perturbation sensitivity in ML as a counterpart to chaotic sensitivity in deterministic systems

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
