---
title: "SRE: establishing SLOs as contractual capability boundaries"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [software-engineering, mlops-deployment, benchmarks-eval]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-itil-capacity-baseline-assertion-vs-telemetry, 2026-05-31-capability-claim-telemetry-conflict-arbitration]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# SRE: establishing SLOs as contractual capability boundaries

## Research Question

How do Site Reliability Engineering (SRE) practices establish what a system can safely do, expressed as a contractual boundary rather than an observed average — specifically, how are Service Level Objectives (SLOs) set, and what evidence justifies the chosen threshold?

## Scope

**In scope:**
- SRE methodology for setting SLOs: the process, the evidence types used, and the decision logic for threshold selection.
- The distinction between SLOs as contractual commitments vs. observed operational averages.
- What evidence (telemetry, user research, business negotiation) is considered authoritative for SLO threshold selection.
- Error budget derivation and its relationship to capability boundaries.

**Out of scope:**
- Service Level Agreement (SLA) legal enforceability analysis.
- Full SRE operational practices beyond SLO/error-budget setting.
- Specific vendor SRE tooling comparison.

**Constraints:** (time, source types, access)
- Primary sources: Google SRE books, industry SRE literature, and practitioner retrospectives.
- Focus on evidence-based threshold justification, not aspirational SLO setting.

## Context

Systems that act on behalf of teams must know the capability boundaries those teams can reliably commit to — not their best-case performance. SRE's SLO model is the most widely documented method for expressing this as a verifiable contractual boundary. Understanding how thresholds are justified is prerequisite to assessing whether a stated allowance is evidence-backed or asserted. This is Gap 2 Q5 from issue #618.

## Approach

1. Document the SRE SLO-setting process from primary sources (Google SRE book, SRE workbook): inputs, steps, and output artefacts.
2. Identify what evidence types are specified as required vs. optional for threshold selection.
3. Analyse the error-budget model: how it converts an SLO threshold into a quantified capability boundary.
4. Survey practitioner literature for cases where SLO thresholds were set without adequate evidence and the resulting failure modes.
5. Assess whether the SRE model provides explicit rules for distinguishing a contractual boundary from an observed average.

## Sources

- [ ] [Beyer et al. (2016) Site Reliability Engineering: How Google Runs Production Systems](https://sre.google/sre-book/table-of-contents/) — primary Google SRE reference: SLO definition, error budgets, and threshold selection
- [ ] [Beyer et al. (2018) The Site Reliability Workbook: Practical Ways to Implement SRE](https://sre.google/workbook/table-of-contents/) — practical SLO setting guidance and worked examples
- [ ] [Hidalgo (2020) Implementing Service Level Objectives](https://www.oreilly.com/library/view/implementing-service-level/9781492076803/) — practitioner guide to evidence-based SLO threshold selection
- [ ] [DORA State of DevOps Reports](https://dora.dev/research/) — empirical data on SLO adoption and associated reliability outcomes

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
