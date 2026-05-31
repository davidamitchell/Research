---
title: "Goal-constraint feedback: convergence conditions vs. specification cycling"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [formal-methods, software-engineering, organisational-design]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-formal-methods-interdependent-inputs-feasibility, 2026-05-31-goal-scope-change-constraint-propagation, 2026-05-31-goal-specification-completeness-schema]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Goal-constraint feedback: convergence conditions vs. specification cycling

## Research Question

In control systems with feedback between goal definition and constraint measurement, what conditions cause the system to converge on a stable specification versus cycle without resolution — and what is the equivalent risk in a software delivery context?

## Scope

**In scope:**
- Control theory conditions for convergence vs. cycling (oscillation) in feedback systems with goal-constraint coupling.
- Mapping these conditions to software delivery contexts: what in a delivery system plays the role of gain, damping, and feedback delay.
- Empirical or case-study evidence of specification cycling in software delivery (requirements churn, scope oscillation) and its drivers.

**Out of scope:**
- Full control systems engineering beyond the convergence/cycling analysis relevant to specification stability.
- Prescriptive delivery process redesign.
- Hardware or embedded systems control beyond the analogy to software delivery.

**Constraints:** (time, source types, access)
- Control theory sources must be primary (textbooks, peer-reviewed); delivery analogies must be grounded in documented empirical patterns, not intuition.
- Distinguish between bounded cycling (recoverable) and unbounded divergence (unresolvable).

## Context

Automated systems that iterate between goal definition and constraint evaluation risk entering a cycle where each constraint measurement triggers a goal revision that generates new constraints, without ever stabilising. Understanding the mathematical conditions for convergence vs. cycling — and their software delivery equivalents — is necessary to design a system that terminates rather than oscillates. This is Gap 3 Q10 from issue #618.

## Approach

1. Document the formal conditions for convergence vs. cycling in feedback control systems: Lyapunov stability, gain margin, and feedback delay effects.
2. Map control-system concepts to software delivery variables: goal revision as set-point change, constraint surface as plant model, review cycle as feedback delay.
3. Survey software delivery literature for documented cycling patterns: requirements churn, scope oscillation, approval loop instability.
4. Identify empirical evidence on which delivery-system conditions correlate with cycling vs. convergence.
5. Assess whether formal convergence conditions can be operationalised as practical design rules for an automated goal-constraint validation system.

## Sources

- [ ] [Åström & Wittenmark (2013) Adaptive Control](https://store.doverpublications.com/0486462781.html) — stability and convergence conditions in adaptive control systems
- [ ] [Senge (1990) The Fifth Discipline: The Art and Practice of the Learning Organization](https://www.penguinrandomhouse.com/books/158736/the-fifth-discipline-by-peter-m-senge/) — reinforcing and balancing feedback loops as convergence/cycling analogues in organisational systems
- [ ] [DeMarco & Lister (2003) Waltzing with Bears: Managing Risk on Software Projects](https://www.pearson.com/en-us/subject-catalog/p/waltzing-with-bears-managing-risk-on-software-projects/P200000009405) — scope oscillation and requirements instability patterns in software delivery
- [ ] [Reinertsen (2009) The Principles of Product Development Flow](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009) — feedback and variability effects on delivery system stability

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
