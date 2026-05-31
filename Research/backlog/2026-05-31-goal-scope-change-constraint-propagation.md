---
title: "Model-based requirements engineering: goal scope change propagation to constraints"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [software-engineering, formal-methods]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-goal-specification-completeness-schema, 2026-05-31-gore-strategic-intent-to-delivery-decomposition, 2026-05-31-formal-methods-interdependent-inputs-feasibility, 2026-05-31-goal-constraint-feedback-convergence-vs-cycling]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Model-based requirements engineering: goal scope change propagation to constraints

## Research Question

Is there evidence from model-based requirements engineering on how scope changes to a Goal propagate to the constraint surface — specifically, does constraint re-enumeration happen automatically, or does it require a human trigger?

## Scope

**In scope:**
- Model-based requirements engineering (MBRE) approaches that link goals to constraints in a shared model: what traceability and change-propagation mechanisms exist.
- Whether constraint re-enumeration triggered by a goal scope change is automated (tool-driven), semi-automated (human-confirmed), or entirely manual.
- Empirical evidence on propagation reliability and failure modes when re-enumeration is not performed.

**Out of scope:**
- General change management process beyond the goal-to-constraint propagation mechanism.
- Requirements management tool comparison beyond propagation capability.
- Implementation of a propagation prototype.

**Constraints:** (time, source types, access)
- Primary sources: MBRE literature (SysML, KAOS, i-star with constraint extensions), requirements tool vendor documentation.
- Empirical evidence preferred over theoretical claims about propagation completeness.

## Context

Scope changes to Goals are a primary source of undetected constraint violations in delivery systems. If constraint re-enumeration is not automatic, there is a window during which the system's constraint surface is stale relative to the current goal definition. Knowing whether this propagation can be automated — and how reliably — determines the design requirement for any automated goal-constraint validation system. This is Gap 3 Q9 from issue #618.

## Approach

1. Survey MBRE frameworks and tools for goal-to-constraint traceability mechanisms: SysML (Systems Modeling Language) requirement links, KAOS obstacle analysis, i-star with constraint annotations.
2. Document the propagation trigger mechanism in each: event-driven, on-request, or manual.
3. Identify empirical studies of propagation completeness and failure: missed constraints, false positives, and latency.
4. Assess whether any tool provides guaranteed re-enumeration or only best-effort traceability.
5. Survey practitioner literature for reported cases where scope change without constraint re-enumeration caused downstream failure.

## Sources

- [ ] [Friedenthal et al. (2015) A Practical Guide to SysML: The Systems Modeling Language](https://www.elsevier.com/books/a-practical-guide-to-sysml/friedenthal/978-0-12-800202-1) — SysML requirement and constraint relationship traceability
- [ ] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703) — KAOS obstacle analysis and constraint-goal linkage
- [ ] [Nuseibeh & Easterbrook (2000) Requirements Engineering: A Roadmap](https://dl.acm.org/doi/10.1145/336512.336523) — requirements change propagation in model-based approaches
- [ ] [Egyed & Grünbacher (2002) Automating Requirements Traceability: Beyond the Records-and-Replay Paradigm](https://ieeexplore.ieee.org/document/1048545) — empirical study of automated traceability in requirements models

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
