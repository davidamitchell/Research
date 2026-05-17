---
title: "Matched denominator for comparing post-pipeline build-mode failures with production do-mode incidents"
added: 2026-05-17T20:40:49+00:00
status: backlog
priority: high
blocks: []
tags: [organisation, workflow, analytics]
started: ~
completed: ~
output: []
cites: []
related: [2026-05-17-manual-workaround-to-central-it-backlog-conversion-datasets, 2026-05-17-vendor-vs-internal-do-mode-automation-visibility-exit-outcomes]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Matched denominator for comparing post-pipeline build-mode failures with production do-mode incidents

## Research Question

What common denominator enables direct matched comparison between post-pipeline build-mode failure rates and production do-mode incident rates for equivalent workflow classes?

## Scope

**In scope:**
- Candidate denominator definitions for build and run reliability comparison (for example workflow execution unit, deployment unit, and business-process transaction unit)
- Matching strategies for equivalent workflow classes across delivery and production operations
- Bias and observability limitations in cross-phase failure and incident comparison

**Out of scope:**
- Platform-specific implementation details of any single continuous integration or service-management product
- Reliability economics models that do not provide measurable denominator mappings

**Constraints:** Prioritise denominator choices that can be computed from standard engineering and incident-management telemetry without proprietary data models.

## Context

Teams cannot make defensible control or investment decisions when build failures and production incidents are tracked on incompatible units.

## Approach

1. Identify denominator options used in software delivery performance and operational reliability literature.
2. Evaluate which denominator can be computed consistently for both post-pipeline failures and production incidents.
3. Define a matched comparison protocol and known distortion risks for workflow-class equivalence.

## Sources

- [ ] [Google Cloud DevOps Research and Assessment metrics overview](https://cloud.google.com/architecture/devops/devops-measurement-metrics) - deployment and change-failure metrics commonly used for build-mode reliability
- [ ] [Google Site Reliability Engineering handbook](https://sre.google/sre-book/table-of-contents/) - incident-rate and service-level measurement patterns for production do-mode reliability
- [ ] [Information Technology Infrastructure Library v4 incident management practice](https://www.axelos.com/certifications/itil-service-management-practices/itil-4-practice-manager/incident-management) - standard production-incident classification context
- [ ] [National Institute of Standards and Technology Special Publication 800-55 Rev.1](https://csrc.nist.gov/pubs/sp/800/55/r1/final) - performance-measurement design principles for defensible denominator selection

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
