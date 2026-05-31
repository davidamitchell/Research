---
title: "Capability claim vs. production telemetry: arbitration mechanisms and overestimation"
added: 2026-05-31T09:42:57+00:00
status: backlog
priority: high
blocks: []
themes: [benchmarks-eval, governance-policy, software-engineering]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-31-sre-slo-threshold-justification, 2026-05-31-itil-capacity-baseline-assertion-vs-telemetry]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Capability claim vs. production telemetry: arbitration mechanisms and overestimation

## Research Question

When a team's capability claim conflicts with production telemetry, what arbitration mechanism produces a reliable baseline — and is there empirical evidence on which approach (telemetry override, structured challenge, third-party audit) reduces overestimation most?

## Scope

**In scope:**
- Documented arbitration mechanisms for resolving conflicts between stated capability claims and production telemetry data.
- Empirical evidence comparing the effectiveness of telemetry override, structured challenge, and third-party audit at reducing capability overestimation.
- Incentive and behavioural factors that contribute to capability overestimation.

**Out of scope:**
- Full change management or organisational psychology of capability disclosure.
- Specific vendor or tool comparison for telemetry platforms.
- Legal or contractual enforcement mechanisms for Service Level Agreements (SLAs).

**Constraints:** (time, source types, access)
- Prioritise empirical studies and documented case evidence over theoretical frameworks.
- Relevant domains: software delivery, SRE (Site Reliability Engineering), operations research, public procurement.

## Context

Capability claims that exceed production reality cause downstream planning failures: commitments are made against capacity that does not exist, and automated systems allocate work to teams that cannot absorb it. Knowing which arbitration method most reliably corrects overestimation — and under what conditions — is prerequisite to designing a defensible baseline-setting process. This is Gap 2 Q7 from issue #618.

## Approach

1. Define the three arbitration approaches: telemetry override, structured challenge (e.g. pre-mortem, red-team review), and third-party audit.
2. Survey empirical literature on capability overestimation: prevalence, magnitude, and root causes.
3. Review evidence comparing arbitration mechanisms: controlled studies, retrospective analyses, or documented programme reviews.
4. Assess conditions under which each mechanism performs better or worse (team size, domain, data availability, incentive structure).
5. Identify gaps: where no comparison evidence exists or where the evidence is conflicting.

## Sources

- [ ] [Flyvbjerg et al. (2003) Megaprojects and Risk: An Anatomy of Ambition](https://www.cambridge.org/core/books/megaprojects-and-risk/8F00E73ECA08DCF7888B2B5B0FCDE8D5) — empirical evidence on optimism bias and capability overestimation in large projects
- [ ] [Kahneman (2011) Thinking, Fast and Slow](https://us.macmillan.com/books/9780374533557/thinkingfastandslow) — reference class forecasting and structured challenge as debiasing mechanisms
- [ ] [Beyer et al. (2018) The Site Reliability Workbook: Practical Ways to Implement SRE](https://sre.google/workbook/table-of-contents/) — SRE error-budget enforcement as telemetry-override mechanism
- [ ] [Government Accountability Office (GAO) Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g) — third-party audit methodology for government programme capability claims

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
