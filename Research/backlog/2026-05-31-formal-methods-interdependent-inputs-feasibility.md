---
title: "Formal methods: specifying interdependent inputs for automated feasibility checking"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [formal-methods, enterprise-adoption, software-engineering]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-goal-specification-completeness-schema, 2026-05-31-goal-scope-change-constraint-propagation, 2026-05-31-goal-constraint-feedback-convergence-vs-cycling]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Formal methods: specifying interdependent inputs for automated feasibility checking

## Research Question

In formal specification methods (Z notation, Alloy, TLA+), how are systems with interdependent inputs specified so that an automated solver can determine feasibility without human arbitration at each step — and what are the known limits of that approach at the scale of an enterprise delivery system?

## Scope

**In scope:**
- How Z notation, Alloy, and TLA+ handle interdependent inputs: constraint expression, invariant specification, and automated solver invocation.
- The conditions under which automated feasibility checking is complete vs. undecidable for each method.
- Documented scale limits: state-space explosion, combinatorial blowup, and practical enterprise-scale thresholds.
- Empirical or case-study evidence of formal-methods adoption in enterprise delivery contexts.

**Out of scope:**
- Full formal methods tutorial or language comparison beyond the feasibility-checking question.
- Other formal specification languages (B method, VDM, Event-B) unless directly comparative.
- Implementation of a formal specification tool.

**Constraints:** (time, source types, access)
- Primary sources: formal methods literature, tool documentation (Alloy Analyzer, TLC model checker, Z/EVES).
- Scale limits must be grounded in empirical benchmarks or documented case failures, not theoretical worst cases only.

## Context

Automated delivery systems that validate goal-constraint combinations need a formal basis for deciding feasibility. Formal methods provide this for bounded problems, but enterprise delivery systems involve large numbers of interdependent variables. Knowing where these methods work and where they break down is necessary before choosing whether to rely on them or design around their limits. This is Gap 3 Q8 from issue #618.

## Approach

1. Document how each method (Z notation, Alloy, TLA+) expresses interdependent inputs and the solver semantics for feasibility checking.
2. Identify the decidability and completeness properties for each approach: what classes of problem are guaranteed solvable?
3. Survey empirical benchmarks and documented case studies for state-space and scale limits.
4. Identify documented enterprise adoption cases: what scale was attempted, and what limits were encountered?
5. Synthesise: for what class of enterprise delivery constraint problem is automated feasibility checking tractable?

## Sources

- [ ] [Woodcock & Davies (1996) Using Z: Specification, Refinement and Proof](https://www.cs.ox.ac.uk/publications/books/PJ/) — Z notation specification and constraint expression
- [ ] [Jackson (2012) Software Abstractions: Logic, Language, and Analysis](https://mitpress.mit.edu/9780262017039/software-abstractions/) — Alloy language, Alloy Analyzer, and bounded feasibility checking
- [ ] [Lamport (2002) Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers](https://lamport.azurewebsites.net/tla/book.html) — TLA+ specification and TLC model checker scale characteristics
- [ ] [Newcombe et al. (2015) How Amazon Web Services Uses Formal Methods](https://cacm.acm.org/magazines/2015/4/184701-how-amazon-web-services-uses-formal-methods/fulltext) — empirical Amazon Web Services (AWS) case study on formal methods at enterprise scale

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

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
