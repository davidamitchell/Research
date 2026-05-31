---
title: "Goal specification: minimum schema and completeness validation"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [formal-methods, software-engineering, governance-policy]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-gore-strategic-intent-to-delivery-decomposition, 2026-05-31-goal-fragmentation-vs-legitimate-sub-goal-signals, 2026-05-31-formal-methods-interdependent-inputs-feasibility, 2026-05-31-goal-scope-change-constraint-propagation]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal specification: minimum schema and completeness validation

## Research Question

What properties must a Goal specification carry for an automated system to determine whether it is complete enough to act on — specifically, what is the minimum schema, and what happens when fields are absent or contradictory?

## Scope

**In scope:**
- Identifying the minimum set of fields (schema elements) a Goal specification must contain for an automated system to assess its actionability.
- Analysing behaviour when schema fields are absent, null, or contradictory: what error modes arise, and what validation rules govern them.
- Survey of existing Goal schema proposals from requirements engineering, enterprise architecture, and AI planning literature.

**Out of scope:**
- Full end-to-end requirements engineering workflows.
- Subjective quality assessment of Goal content beyond structural completeness.
- Implementation of a validation tool or prototype.

**Constraints:** (time, source types, access)
- Focus on publicly documented schemas and standards (Goal-Oriented Requirements Engineering (GORE), The Open Group Architecture Framework (TOGAF), IEEE 29148, AI planning ontologies).
- Findings must be grounded in empirical or formal sources, not vendor marketing claims.

## Context

Automated systems that act on Goal specifications — planning engines, agentic AI (Artificial Intelligence) systems, delivery orchestrators — fail in hard-to-diagnose ways when the Goal schema is under-specified. Knowing the minimum required fields and the valid handling rules for missing or conflicting data is the prerequisite for building reliable completeness checks. This is a foundational Gap 1 question from issue #618.

## Approach

1. Survey published Goal schemas in GORE, TOGAF motivation model, IEEE 29148, and AI planning (STRIPS, PDDL) to extract field inventories.
2. Identify which fields appear across all schemas (candidate minimum) vs. those that are schema-specific.
3. Analyse how each schema handles absent fields: hard error, default, degraded mode, or undefined.
4. Analyse handling rules for contradictory fields: detection mechanism, resolution strategy, and escalation path.
5. Synthesise a candidate minimum schema with explicit completeness rules and flag gaps where no consensus exists.

## Sources

- [ ] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703) — GORE theoretical foundations and Goal schema from Axel van Lamsweerde
- [ ] [The Open Group TOGAF Standard — Motivation Architecture](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap08.html) — TOGAF motivation metamodel defining Driver, Goal, Outcome, Requirement
- [ ] [IEEE 29148-2018 Systems and Software Engineering — Requirements Engineering](https://standards.ieee.org/ieee/29148/6696/) — IEEE standard requirements for well-formed requirement and goal statements
- [ ] [Russell & Norvig Artificial Intelligence: A Modern Approach — Goal Representation](https://aima.cs.berkeley.edu/) — AI planning goal specification (STRIPS/PDDL formalism)

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
