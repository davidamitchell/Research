---
title: "RQ 6.1 — The Halting Problem and Rice's Theorem: The Absolute Boundary of Static Analysis for Coded Systems"
added: 2026-05-18T19:40:00+00:00
status: backlog
priority: high
blocks:
  - 2026-05-18-rq6-2-state-explosion-chaos-theory
tags: [formal-methods, epistemology, philosophy-of-science]
started: ~
completed: ~
output: [knowledge]
cites:
  - 2026-05-18-rq1-1-popper-falsifiability
related:
  - 2026-05-18-rq1-1-popper-falsifiability
  - 2026-05-18-rq6-2-state-explosion-chaos-theory
  - 2026-05-18-rq6-3-complexity-horizon-classical-systems
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# RQ 6.1 — The Halting Problem and Rice's Theorem: The Absolute Boundary of Static Analysis for Coded Systems

## Research Question

How do the Halting Problem (Turing) and Rice's Theorem formalise the absolute boundary of static analysis, proving that it is mathematically impossible to write a general algorithm to verify whether an arbitrary coded system possesses specific non-trivial semantic properties?

## Scope

**In scope:**
- Turing's Halting Problem proof and its implications for static verification of program behaviour
- Rice's Theorem: all non-trivial semantic properties of programs are undecidable
- Gödel's Incompleteness Theorems as a broader epistemological parallel
- Practical implications: what can static analysis tools (linters, type checkers, model checkers) actually prove, and what they cannot
- Connection to Phase 1's epistemological framework: undecidability as the formal counterpart of unfalsifiability in physical models

**Out of scope:**
- Implementation details of specific static analysis tools
- Decidable subsets of the halting problem (bounded model checking, restricted program classes)

**Constraints:** This item runs in parallel with Phases 2–4; it branches off Phase 1 (epistemological foundations) and feeds into the Phase 5 comparison. It must connect its formal results to the spirit of Phase 1 — both are about the limits of what we can know about a system from the outside.

## Context

Phase 6 is a parallel track that examines the fundamental limits of the alternative to agentic systems: deterministic coded software. Before comparing the two (Phase 5), we need to understand what formal guarantees coded systems can and cannot provide. This item establishes the hardest formal result: Rice's Theorem proves that there is no general algorithm for verifying any non-trivial semantic property of an arbitrary program. This is the coded-system counterpart to the Causal Hierarchy Theorem (RQ 2.4) — both establish hard epistemological boundaries.

## Approach

1. Present Turing's Halting Problem formally: no Turing machine can decide, for all input-program pairs, whether the program halts.
2. Derive Rice's Theorem from the Halting Problem: any non-trivial semantic property of a program is undecidable.
3. Apply Gödel's First Incompleteness Theorem as a parallel: there are true statements about a formal system that cannot be proved within it.
4. Map the boundary: what properties CAN be statically verified (syntactic properties, restricted safety properties via model checking), and what cannot?
5. Connect to Phase 1: draw the parallel between Rice's Theorem (limits of analysing coded systems) and Popper's demarcation (limits of evaluating physical models).

## Sources

- [ ] [Turing, A. M. (1936) On Computable Numbers, with an Application to the Entscheidungsproblem — Proceedings of the London Mathematical Society](https://doi.org/10.1112/plms/s2-42.1.230) — original proof of the Halting Problem and computability limits
- [ ] [Rice, H. G. (1953) Classes of Recursively Enumerable Sets and Their Decision Problems — Transactions of the American Mathematical Society Vol 74](https://doi.org/10.2307/1990888) — original proof of Rice's Theorem; all non-trivial semantic properties are undecidable
- [ ] [Gödel, K. (1931) Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme — Monatshefte für Mathematik und Physik Vol 38](https://doi.org/10.1007/BF01700692) — Gödel's First Incompleteness Theorem; epistemological parallel to Rice's Theorem
- [ ] [Sipser, M. (2012) Introduction to the Theory of Computation — Cengage Learning](https://www.cengage.com/c/introduction-to-the-theory-of-computation-3e-sipser/9781133187790/) — accessible textbook treatment of the Halting Problem and Rice's Theorem with proofs

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
