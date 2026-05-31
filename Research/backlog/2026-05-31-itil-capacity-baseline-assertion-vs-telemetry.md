---
title: "ITIL capacity management: baseline measurement and assertion vs. telemetry"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: medium
blocks: []
themes: [governance-policy, software-engineering, benchmarks-eval]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-sre-slo-threshold-justification, 2026-05-31-capability-claim-telemetry-conflict-arbitration]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# ITIL capacity management: baseline measurement and assertion vs. telemetry

## Research Question

What does IT Infrastructure Library (ITIL) capacity management specify as the measurement practice for establishing a platform capability baseline, and where does it rely on assertion rather than telemetry?

## Scope

**In scope:**
- ITIL capacity management: the specified measurement practices, data collection requirements, and baseline-setting procedures.
- Explicit identification of where ITIL requires empirical telemetry vs. where it accepts or defaults to asserted values.
- ITIL 4 updates to capacity management vs. ITIL v3/2011 baseline practices.

**Out of scope:**
- Full ITIL service management lifecycle beyond capacity and performance management.
- Specific vendor implementations or tooling for ITIL capacity management.
- Comparison with non-ITIL frameworks (that is handled in Q5 SRE and Q7 arbitration items).

**Constraints:** (time, source types, access)
- Primary sources: ITIL official publications (AXELOS); secondary sources: practitioner retrospectives and empirical studies.
- Distinguish between prescriptive ITIL text and interpretive practitioner guidance.

## Context

ITIL is the dominant IT service management framework and many organisations use it to establish platform capability baselines. Whether ITIL's capacity management practice mandates telemetry-based measurement or permits assertion-based baselines determines whether capability claims derived from ITIL processes can be trusted as evidence-backed. This is Gap 2 Q6 from issue #618.

## Approach

1. Extract the capacity management measurement requirements from ITIL 4 (Capacity and Performance Management practice) and ITIL v3/2011.
2. Identify explicit telemetry requirements: what must be measured, at what frequency, and with what retention.
3. Identify where ITIL text uses language indicating assertion is acceptable (e.g. "estimated", "agreed", "documented").
4. Assess whether the gap between telemetry requirements and assertion tolerance is acknowledged by ITIL or left implicit.
5. Review empirical studies or audits of ITIL capacity management implementations for evidence of assertion-vs-telemetry failure patterns.

## Sources

- [ ] [AXELOS ITIL 4 — Capacity and Performance Management Practice](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation) — primary source for ITIL 4 capacity management measurement requirements
- [ ] [AXELOS ITIL Service Design — Capacity Management (ITIL v3/2011)](https://www.axelos.com/resource-hub/book/itil-service-design) — ITIL v3/2011 baseline practices for comparison
- [ ] [Betz (2011) Managing IT as a Business](https://www.pearson.com/en-us/subject-catalog/p/managing-it-as-a-business/P200000009386) — practitioner analysis of ITIL capacity management gaps
- [ ] [ISO/IEC 20000-1:2018 — IT Service Management System Requirements](https://www.iso.org/standard/70636.html) — ISO standard codifying ITIL capacity management requirements for formal compliance comparison

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
