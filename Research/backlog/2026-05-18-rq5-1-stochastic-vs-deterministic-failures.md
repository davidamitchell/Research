---
title: "RQ 5.1 — Stochastic vs. Deterministic Failure Modes: How Agentic and Coded Systems Break Differently on Identical Unvalidated Inputs"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-agentic-explainability-vs-traditional
tags: [agentic-ai, llm, formal-methods, machine-learning, evaluation]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq4-3-ood-generalization-agentic
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
related:
  - 2026-05-18-rq4-3-ood-generalization-agentic
  - 2026-05-18-rq5-2-flexibility-vs-predictability-auditability
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
  - 2026-05-18-agentic-explainability-vs-traditional
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 5.1 — Stochastic vs. Deterministic Failure Modes: How Agentic and Coded Systems Break Differently on Identical Unvalidated Inputs

## Research Question

How do the failure modes of a stochastic agentic system (e.g., semantic drift, alignment degradation, non-deterministic branching) differ fundamentally from the failure modes of a non-stochastic, statically coded system when processing identical unvalidated inputs?

## Scope

**In scope:**
- Deterministic vs. stochastic runtime behaviour as a formal property distinguishing coded systems from LLM-based agents
- Silent failures vs. crash-fast topologies: how coded systems fail loudly while agentic systems degrade silently
- Semantic corruption: cases where a stochastic agent produces plausible-looking but semantically wrong output under adversarial or OOD input
- Formal comparison of failure mode taxonomy for both system classes
- Production telemetry evidence of agentic failure patterns

**Out of scope:**
- Remediation strategies for either system class
- Hardware or infrastructure failures

**Constraints:** Requires both Phase 4 (agentic failure analysis) and Phase 6 (coded system underpinnings) to be complete before this item can begin; it is the convergence point of the two tracks.

## Context

Phase 4 characterised agentic system failures from a machine learning perspective. Phase 6 (running in parallel) characterises the fundamental limits and failure modes of deterministic coded systems. This item brings the two analyses together for direct comparison. The core question is: when both classes of system encounter the same unvalidated input, what are the structural differences in how they fail? This comparison is the empirical foundation for the final two synthesis items on explainability and production tradeoffs.

## Approach

1. Compile a formal taxonomy of agentic system failure modes from Phases 3 and 4: semantic drift, hallucination, error cascade, silent degradation.
2. Compile a formal taxonomy of coded system failure modes from Phase 6: undecidability of properties, state space explosion, chaotic sensitivity, complexity horizon opacity.
3. Map both taxonomies onto a common comparison schema: detectability of failure, failure propagation speed, recoverability, formal verifiability.
4. Survey production telemetry studies (Subramaniam et al. 2024) for empirical evidence of agentic failure patterns vs. conventional software patterns.
5. Identify: are there failure modes unique to each class, and are there failure modes that are qualitatively worse in one class vs. the other?

## Sources

- [ ] [Dijkstra, E. W. (1989) On the Cruelty of Really Teaching Computer Science — Communications of the ACM Vol 32 No 12](https://doi.org/10.1145/74580.74582) — formal argument for the epistemological gap between human intuition and deterministic system behaviour
- [ ] [Subramaniam, S. et al. (2024) Telemetry and failure patterns in production LLM agents — search for most recent publication at arxiv.org/search](https://arxiv.org/search/?query=LLM+agent+failure+production&searchtype=all) — empirical production failure telemetry for LLM-based agentic systems
- [ ] [Avizienis, A. et al. (2004) Basic Concepts and Taxonomy of Dependable and Secure Computing — IEEE Transactions on Dependable and Secure Computing Vol 1](https://doi.org/10.1109/TDSC.2004.2) — formal taxonomy of system failures applicable to both coded and stochastic systems
- [ ] [Bernstein, P. A. (1987) Sequoia: A Fault-Tolerant Tightly Coupled Multiprocessor — IEEE Computer Vol 20](https://doi.org/10.1109/MC.1988.1663007) — crash-fast design philosophy as a formal alternative to silent failure

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
