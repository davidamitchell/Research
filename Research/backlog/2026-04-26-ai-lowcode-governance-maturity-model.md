---
title: "What maturity model best describes the evolution of governance capabilities for Artificial Intelligence (AI) and low-code in enterprises?"
added: 2026-04-26T10:11:11+00:00
status: backlog
priority: medium
blocks: []
tags: [maturity-model, ai-governance, low-code, enterprise-governance, capability-model, benchmarks, progression, assessment, regulated-enterprise]
started: ~
completed: ~
output: [knowledge]
---

# What maturity model best describes the evolution of governance capabilities for Artificial Intelligence (AI) and low-code in enterprises?

## Research Question

What maturity model best describes the evolution of governance capabilities for AI and low-code in enterprises — specifically, what are the clearly defined maturity stages, capability benchmarks, and progression pathways that allow an organisation to assess its current governance capability state and plan incremental improvements across all governance dimensions?

## Scope

**In scope:**
- Maturity model design: definition of maturity stages (e.g. initial, developing, defined, managed, optimising) with clear stage boundary criteria across all governance dimensions identified in Q1–Q12 and Q15
- Stage definitions: what capabilities, practices, evidence artefacts, and outcomes characterise each maturity level for each governance dimension
- Progression pathways: what sequence of improvements is recommended for progressing from one maturity level to the next, and what investment/effort is required at each step
- Benchmarking: how organisations can assess their current maturity level using observable evidence (not just self-assessment), and what common assessment mechanisms exist
- Existing maturity models: assessment of whether existing maturity frameworks (Capability Maturity Model Integration (CMMI), NIST AI RMF Maturity Model, AI governance maturity models from industry bodies) are applicable or require adaptation
- Relationship between governance maturity and risk profile: what the evidence says about the relationship between governance maturity level and operational risk, incident rate, and regulatory compliance
- The role of culture and behaviour (Q14) in maturity progression — whether maturity models that focus only on structural capabilities without addressing behavioural conditions overstate an organisation's actual governance capability

**Out of scope:**
- Detailed design of individual governance dimensions (covered by Q1–Q12)
- Economic modelling of the cost of maturity improvement (covered by Q8)
- Specific AI or technology maturity models unrelated to governance (focus is on governance capability maturity)

**Constraints:**
- This item depends on the findings of Q1–Q12 and Q14–Q15 to define what governance capabilities exist and therefore what maturity stages can be meaningfully defined. It should not be started until those items are substantially complete.
- Must assess existing maturity frameworks for adequacy before constructing a new one — a new maturity model is only warranted if existing frameworks are materially insufficient
- Must address the gap between capability possession (having a tool or policy) and capability exercise (consistently using it effectively) — a maturity model based only on capability possession will overstate maturity

## Context

Without a maturity model, governance improvement programmes lack an objective baseline, a target state, and a measurable progression path. Organisations cannot determine where they are, where they are going, or whether they are making progress. The maturity model is the instrument that makes governance improvement plannable and measurable — and provides the common language for board, risk committee, and technology leadership to discuss governance investment priorities.

This item is the synthesis capstone for the governance dimension research programme (Q1–Q12, Q14–Q15). It takes the complete picture of what enterprise AI and low-code governance requires across all dimensions, and translates it into a staged capability model that allows organisations to locate themselves and plan improvement. It also integrates the behavioural analysis from Q14 — a maturity model that ignores the gap between formal capability and actual practice will produce overconfident assessments.

This item should not be started until Q1–Q12 and Q14–Q15 are substantially complete.

Cross-references:
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q2: `2026-04-26-ai-agent-identity-access-management-enterprise`
- Q3: `2026-04-26-ai-lowcode-governance-enforcement-architecture`
- Q4: `2026-04-26-ai-lowcode-observability-telemetry-governance`
- Q5: `2026-04-26-ai-lowcode-risk-tier-classification-controls`
- Q6: `2026-04-26-data-governance-ai-lowcode-enterprise-enforcement`
- Q7: `2026-04-26-ai-lowcode-lifecycle-management`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`
- Q9: `2026-04-26-human-in-the-loop-ai-automated-workflows`
- Q10: `2026-04-26-ai-lowcode-sdlc-platform-engineering-integration`
- Q11: `2026-04-26-vendor-platform-governance-constraints-compensating-controls`
- Q12: `2026-04-26-ai-lowcode-failure-modes-governance-mitigation`
- Q14: `2026-04-26-ai-governance-culture-incentives-behaviour`
- Q15: `2026-04-26-ai-lowcode-regulatory-compliance-alignment`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`

## Approach

1. **Existing maturity model survey:** Review existing AI and IT governance maturity models: CMMI for governance, NIST AI RMF maturity, the AI governance maturity model published by industry bodies (BSI, DSIT, Microsoft, Gartner), and sector-specific models (financial services AI governance maturity). Assess each for: dimensional completeness against the Q1–Q12 governance dimensions, stage definition clarity, assessment mechanism quality, and evidence of use in practice.
2. **Dimensional gap analysis:** Identify which governance dimensions (Q1–Q12, Q14–Q15) are absent or inadequately covered by existing maturity models — particularly machine identity management (Q2), vendor constraint management (Q11), and behavioural governance (Q14).
3. **Maturity model design:** Based on the survey and gap analysis, either select and extend an existing model or define a new one. Define maturity stages (3–5 stages) with explicit, observable stage boundary criteria for each governance dimension.
4. **Capability progression pathways:** For each governance dimension, define the progression pathway from initial to optimising maturity — what capabilities must be developed, in what sequence, and what evidence artefacts demonstrate progression.
5. **Behavioural maturity integration:** Integrate the findings from Q14 (culture and behaviour) into the maturity model — define a behavioural maturity dimension that captures the gap between formal governance capability and actual practice.
6. **Assessment mechanism:** Design a self-assessment instrument that allows organisations to rate their current maturity level against observable evidence criteria — moving beyond questionnaire-based self-assessment toward evidence-based assessment.
7. **Synthesis:** Produce a governance maturity model — stage definitions, capability matrix, progression pathways, and self-assessment instrument — suitable for adoption as an enterprise governance artefact.

## Sources

- [ ] [CMMI Institute — CMMI for governance and management](https://cmmiinstitute.com/) — foundational maturity framework; assess for applicability to AI governance capability staging
- [ ] [NIST AI RMF 1.0 — maturity and measurement guidance](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — US AI risk management maturity guidance; assess for stage definition applicability
- [ ] [UK DSIT — Responsible AI Adoption Guidance](https://www.gov.uk/government/collections/responsible-ai) — UK government AI adoption maturity guidance; assess for governance maturity model content
- [ ] [Microsoft — AI Maturity Model](https://www.microsoft.com/en-us/ai/our-approach/ai-maturity-model) — vendor AI maturity model; assess critically for governance completeness and vendor bias
- [ ] [Gartner — AI Governance Maturity Model](https://www.gartner.com/en/documents) — analyst firm AI governance maturity assessment (access may be required)
- [ ] [BSI PAS 1820 — AI assurance standard (draft)](https://www.bsigroup.com/en-GB/insights-and-media/insights/brochures/ai-assurance-standards/) — UK AI assurance standard; assess for maturity staging and assessment mechanism design
- [ ] [MIT Sloan Management Review — AI governance maturity research](https://sloanreview.mit.edu/) — academic and practitioner AI governance research; assess for evidence on maturity model validity in practice

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

*(This section seeds the Findings below.)*

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

- Type: knowledge
- Description:
- Links:
