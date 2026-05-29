---
title: "Q3: Routing design that isolates exceptions from routine flow"
added: 2026-05-29
status: backlog
priority: high
tags: [routing, queue-design, exception-handling, triage]
blocks: [2026-05-29-split-authority-q1-flow-constraint, 2026-05-29-split-authority-q2-demand-segmentation]
started: ~
completed: ~
output: []
cites: []
related: []
supersedes: ~
superseded_by: []
item_type: primary
confidence: preliminary
---

# Q3: Routing design that isolates exceptions from routine flow

## Research Question

What intake, triage, queueing, escalation, and routing model allows routine work to move quickly while isolating high-risk or ambiguous work?

## Scope

**In scope:**
- Intake and routing designs that avoid one-queue-for-all bottlenecks.
- Escalation models for ambiguous/high-risk exceptions.

**Out of scope:**
- Control-policy selection independent of routing and segmentation evidence.

**Constraints:**
- Must incorporate Q1 constraint findings and Q2 demand classes.

## Context

Q3 combines routing/classification and exception-handling design to prevent exceptional work from blocking routine flow. It enables Q5, Q6, and P1.

## Approach

1. Compare serial, parallel, and hybrid lane-routing patterns.
2. Evaluate exception isolation mechanisms and escalation thresholds.
3. Define a routing model that protects baseline throughput under uncertainty.

## Sources

- [ ] Queueing scheduler and multi-queue dispatch literature
- [ ] Emergency intake/triage process design references
- [ ] Software delivery practices for change classification and escalation

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

- Claim -> source(s)

### Recommendations

### Limitations

### Follow-up Questions
