---
title: "Goal fragmentation: signals distinguishing salami-slicing from legitimate sub-goals"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: medium
blocks: []
themes: [software-engineering, governance-policy]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-goal-specification-completeness-schema, 2026-05-31-gore-strategic-intent-to-delivery-decomposition, 2026-05-31-goal-scope-change-constraint-propagation]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal fragmentation: signals distinguishing salami-slicing from legitimate sub-goals

## Research Question

When a Goal is a fragment of a larger intent — salami-sliced deliberately or accidentally — what signals distinguish it from a legitimately scoped sub-goal?

## Scope

**In scope:**
- Defining and distinguishing two patterns: (a) salami-slicing (artificial fragmentation to evade scope or approval thresholds) and (b) legitimate goal decomposition (principled sub-goal scoping).
- Observable signals, heuristics, or structural properties that differentiate the two patterns in written goal specifications.
- Evidence from requirements engineering, product management, and programme governance literature on detection approaches.

**Out of scope:**
- Deliberate misuse or fraud detection beyond honest scope management error.
- Automated tool implementation for detection.
- Goal quality assessment beyond the fragment-vs-sub-goal distinction.

**Constraints:** (time, source types, access)
- Prioritise empirical evidence and documented heuristics over purely theoretical classification.
- Relevant domains include software delivery, programme management, enterprise architecture, and public sector procurement.

## Context

Deliberate or accidental goal fragmentation is a recurring dysfunction in delivery governance: goals are split to remain below approval thresholds, avoid constraint checks, or defer hard trade-offs. Automated systems that process goal specifications need to detect this pattern to avoid acting on structurally valid but semantically incomplete inputs. This is Gap 1 Q4 from issue #618.

## Approach

1. Define the conceptual distinction between salami-slicing and legitimate sub-goal scoping; identify the structural and semantic properties that separate them.
2. Survey requirements engineering, programme governance, and product management literature for documented signals and heuristics.
3. Catalogue signal categories: structural (e.g. missing parent reference, no value delivery at the fragment level), semantic (e.g. outcome only realisable in combination), and contextual (e.g. approval threshold proximity).
4. Assess signal reliability: are there false positives and false negatives documented in the literature?
5. Identify whether any formal method or standard encodes these signals as validation rules.

## Sources

- [ ] [Van Lamsweerde (2009) Requirements Engineering: From System Goals to UML Models to Software Specifications](https://www.wiley.com/en-gb/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703) — GORE decomposition completeness and obstacle analysis
- [ ] [Reinertsen (2009) The Principles of Product Development Flow](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) — batch-size and scope fragmentation effects on delivery flow
- [ ] [AXELOS Managing Successful Programmes (MSP)](https://www.axelos.com/certifications/propath/managing-successful-programmes-msp) — programme benefit decomposition and dependency governance rules
- [ ] [Firesmith (2005) Specifying Reusable Security Requirements](https://www.sei.cmu.edu/library/abstracts/journals/j-defense-software-engineering-2005.cfm) — goal granularity and the scope-coherence problem in requirements

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
