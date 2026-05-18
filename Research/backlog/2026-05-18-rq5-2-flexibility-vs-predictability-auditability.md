---
title: "RQ 5.2 — Flexibility vs. Predictability: How the Agentic Tradeoff Affects Auditability and Formal Verification in Production Pipelines"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-agentic-production-tradeoffs
tags: [agentic-ai, llm, formal-methods, workflow]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
related:
  - 2026-05-18-rq5-1-stochastic-vs-deterministic-failures
  - 2026-05-18-agentic-explainability-vs-traditional
  - 2026-05-18-agentic-production-tradeoffs
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 5.2 — Flexibility vs. Predictability: How the Agentic Tradeoff Affects Auditability and Formal Verification in Production Pipelines

## Research Question

In a production pipeline with uncontrolled inputs, how does the trade-off between the flexibility of an agentic system and the predictability of a deterministic execution model affect the auditability and formal verification of the system's runtime state?

## Scope

**In scope:**
- Lineage tracking: can the decision path of an agentic system be reconstructed post-hoc with sufficient fidelity for audit?
- State space explosion in agentic systems: does the exponential branching of LLM token choices make formal verification intractable?
- Non-Deterministic Finite Automata (NDFA) vs. Probabilistic Graphical Models (PGMs) as formal models of agentic vs. coded system runtime state
- Formal verification approaches (model checking) applied to agentic pipelines: what is tractable?
- Regulatory and compliance implications of unverifiable runtime state

**Out of scope:**
- Specific compliance frameworks (General Data Protection Regulation, AI Act)
- Post-hoc explainability techniques for LLMs in isolation

**Constraints:** Builds on RQ 5.1's failure mode comparison; must connect to formal verification theory from Phase 6 (Clarke et al.).

## Context

RQ 5.1 showed that agentic and coded systems fail in structurally different ways. This item asks a production-critical follow-up: can we even audit or formally verify an agentic system's runtime state? Deterministic systems have well-understood model checking approaches (Clarke et al.), even if they face state space explosion. Stochastic agentic systems combine this state space explosion with non-deterministic probabilistic branching, making formal verification qualitatively harder. The conclusion of this item feeds directly into the final synthesis on production tradeoffs.

## Approach

1. Formalise lineage tracking requirements for production audit: what must be recorded to reconstruct a decision path?
2. Model the state space of an agentic pipeline as an NDFA and as a PGM; compare tractability of formal verification for each.
3. Apply Clarke et al.'s model checking framework: what properties of agentic pipelines can and cannot be verified statically or dynamically?
4. Identify the flexibility-predictability Pareto frontier: as agentic flexibility increases, at what rate does verifiability decrease?
5. Summarise implications for regulated production environments (finance, healthcare, critical infrastructure).

## Sources

- [ ] [Clarke, E. M. et al. (2018) Model Checking — MIT Press](https://mitpress.mit.edu/9780262038553/model-checking/) — formal model checking methods for verification of concurrent and distributed systems
- [ ] [Baier, C. & Katoen, J.-P. (2008) Principles of Model Checking — MIT Press](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/) — comprehensive treatment of model checking theory including probabilistic model checking
- [ ] [Holzmann, G. J. (2003) The SPIN Model Checker — Addison-Wesley](https://spinroot.com/spin/Doc/Book_extras/) — practical model checking tool; illustrates what is tractable in real systems
- [ ] [European Parliament (2024) EU AI Act — Official Journal of the European Union](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — regulatory context: auditability and transparency requirements for high-risk AI systems

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
