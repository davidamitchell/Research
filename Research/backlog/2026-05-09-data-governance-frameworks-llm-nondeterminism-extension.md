---
title: "Extending Traditional Data Governance Frameworks to Address LLM Non-Determinism and Alignment Uncertainty"
added: 2026-05-09T22:44:23+00:00
status: backlog
priority: medium
blocks:
  - 2026-05-09-data-governance-standards-ai-agentic-applicability
tags: [governance, agentic-ai, llm, ai-governance, regulatory, organisational-learning]
started: ~
completed: ~
output: []
cites: []
related:
  - 2026-05-09-data-governance-standards-ai-agentic-applicability
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-05-09-policy-as-code-guardrails-regulatory-ai-governance
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Extending Traditional Data Governance Frameworks to Address LLM Non-Determinism and Alignment Uncertainty

## Research Question

How can traditional data governance frameworks be extended or mapped to address the inherent non-determinism and alignment uncertainty of modern LLMs (Large Language Models) and agentic systems?

## Scope

**In scope:**
- Analysis of DAMA-DMBOK (Data Management Body of Knowledge), ISO/IEC 38505, and COBIT (Control Objectives for Information and Related Technologies) governance domains and their extension points
- Proposed extensions or adaptations in academic literature and industry frameworks
- New governance domains or capabilities required specifically for LLM/agentic systems (e.g., prompt governance, model lineage, inference audit trails)
- Alignment uncertainty as a distinct governance problem separate from data quality

**Out of scope:**
- Proposing entirely novel frameworks — focus is extension/mapping of existing standards
- Governance of training data and model development (MLOps); focus is on deployed/inference-time governance

**Constraints:** Extensions must map clearly to existing framework structures to be adoptable without wholesale replacement

## Context

Traditional data governance frameworks were designed for relational data, structured pipelines, and deterministic processing. They include data quality, stewardship, lineage, and access control as core domains. LLMs introduce new failure modes — hallucination, context sensitivity, alignment drift, and emergent behaviour — that have no direct equivalents in these frameworks. Organisations attempting to govern LLM-based systems within existing DAMA or ISO/IEC 38505 structures find structural gaps: the frameworks do not account for probabilistic outputs, prompt-level controls, or model version governance. This research seeks to identify those gaps precisely and evaluate proposed extensions from the literature and practice.

## Approach

1. Map the governance domains of DAMA-DMBOK and ISO/IEC 38505 to the capabilities required for LLM/agentic system governance
2. Identify the gaps: domains for which no existing framework concept exists, and domains that require significant reinterpretation
3. Review proposed extensions in academic literature (AI governance frameworks, responsible AI frameworks) and industry guidance (Google PAIR, Microsoft Responsible AI, IBM AI Fairness 360)
4. Synthesise a mapping document: existing domain → required extension → proposed control

## Sources

- [ ] [DAMA International DMBOK2 — Data Management Body of Knowledge, Chapter 15: Data Governance](https://www.dama.org/cpages/body-of-knowledge) — primary framework for data governance domains
- [ ] [ISO/IEC 38505-1:2017 Governance of data](https://www.iso.org/standard/56639.html) — international standard for data governance accountability
- [ ] [ISACA COBIT 2019 Framework](https://www.isaca.org/resources/cobit) — IT governance framework with governance objectives that can be extended to AI
- [ ] [Google PAIR Explorables — AI governance principles](https://pair.withgoogle.com/) — Google's responsible AI framework
- [ ] [Microsoft Responsible AI Standard v2 (Microsoft)](https://blogs.microsoft.com/on-the-issues/2022/06/21/microsofts-responsible-ai-standard-v2-general-requirements/) — Microsoft's internal framework; contains extensions to traditional governance for AI
- [ ] [Arrieta et al. (2020) Explainable AI: Concepts, taxonomies, opportunities and challenges toward responsible AI (Information Fusion)](https://www.sciencedirect.com/science/article/pii/S1566253519308103) — explainability as an extension point for governance frameworks

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

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type:
- Description:
- Links:
