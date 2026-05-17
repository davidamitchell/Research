---
title: "Datasets for measuring conversion from manual workaround demand to central Information Technology backlog items"
added: 2026-05-17T20:40:49+00:00
status: backlog
priority: high
blocks: []
tags: [organisation, workflow, analytics]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-17-post-gap-closure-persistence-low-code-bots-agents, 2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Datasets for measuring conversion from manual workaround demand to central Information Technology backlog items

## Research Question

What public or internal datasets can validly measure the rate at which manual workaround demand is converted into formal central Information Technology (IT) backlog items?

## Scope

**In scope:**
- Public benchmark datasets and industry surveys that expose demand, ticket, backlog, and completion fields
- Internal operational datasets from ticketing, workflow, and portfolio systems that can be joined for conversion-rate measurement
- Measurement designs that support repeatable month-over-month conversion tracking

**Out of scope:**
- Prescriptive tooling selection or implementation of any specific IT service management platform
- Causal claims about why conversion does or does not happen without supporting evidence

**Constraints:** Prefer sources with documented schemas or metric definitions, and prioritise data structures that can be reproduced in enterprise environments.

## Context

Leadership cannot prioritise remediation of workaround-heavy operating areas without a measurable conversion funnel from manual demand to centrally governed backlog intake.

## Approach

1. Catalogue candidate public and internal datasets with fields that capture workaround demand and backlog conversion events.
2. Define join keys and denominator choices needed to compute conversion rates without double counting.
3. Assess data-quality, governance, and survivorship-bias risks that affect comparability across organisations.

## Sources

- [ ] [Google Cloud DevOps Research and Assessment metrics overview](https://cloud.google.com/architecture/devops/devops-measurement-metrics) - baseline metric taxonomy that can inform funnel and conversion denominator design
- [ ] [Atlassian Jira Cloud REST API issue search](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/) - canonical issue and workflow fields for backlog and ticket-state extraction
- [ ] [GitHub REST API issues documentation](https://docs.github.com/en/rest/issues/issues) - standard event and state fields for issue lifecycle and queue-flow analysis
- [ ] [Microsoft Power Platform Center of Excellence Starter Kit](https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit) - enterprise low-code telemetry and governance datasets relevant to workaround demand signals

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
| | | high / medium / low | |

### Assumptions

-

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
