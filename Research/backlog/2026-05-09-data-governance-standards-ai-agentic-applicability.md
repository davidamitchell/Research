---
title: "Data Governance Standards and Regulations Applied to AI and Agentic AI Deployments"
added: 2026-05-09T22:44:23+00:00
status: backlog
priority: high
blocks: []
tags: [governance, agentic-ai, llm, regulatory, compliance, ai-governance]
started: ~
completed: ~
output: []
cites: []
related:
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-05-09-compliance-risks-stochastic-llm-governance-decisions
  - 2026-05-09-data-governance-frameworks-llm-nondeterminism-extension
  - 2026-05-09-policy-as-code-guardrails-regulatory-ai-governance
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Data Governance Standards and Regulations Applied to AI and Agentic AI Deployments

## Research Question

How do established data governance standards (e.g., ISO/IEC 38505, DAMA-DMBOK (Data Management Body of Knowledge), NIST (National Institute of Standards and Technology)) and regulations (GDPR (General Data Protection Regulation) accountability, CCPA (California Consumer Privacy Act), HIPAA (Health Insurance Portability and Accountability Act)) apply specifically to AI systems and agentic AI deployments?

## Scope

**In scope:**
- Mapping of ISO/IEC 38505, DAMA-DMBOK, and NIST AI Risk Management Framework (RMF) requirements to AI and agentic systems
- Analysis of how GDPR accountability, CCPA, and HIPAA obligations extend to AI-generated decisions and autonomous agents
- Gaps or ambiguities in existing standards when applied to agentic AI (multi-step, multi-agent pipelines)
- Published guidance, regulatory interpretations, and enforcement precedents relating to AI systems

**Out of scope:**
- Detailed legal analysis or jurisdiction-specific case law beyond the named regulations
- Standards not yet ratified or published (draft versions noted but not primary focus)
- AI-specific regulations not yet in force (EU AI Act treatment is contextual only)

**Constraints:** Sources published from 2020 onward preferred; favour primary regulatory/standards documents over secondary commentary

## Context

Organisations deploying AI systems and agentic pipelines face a landscape where existing data governance standards were designed for human-driven processes and traditional software. The accountability, auditability, and data lineage requirements in GDPR, CCPA, and HIPAA create obligations that are architecturally challenging for LLM (Large Language Model)-based systems and multi-agent workflows. Understanding which clauses apply, how they translate into system requirements, and where the standards are silent is a prerequisite for compliant AI deployment at enterprise scale.

## Approach

1. Identify the accountability, transparency, and auditability clauses in each named regulation and standard
2. Assess each clause against the technical characteristics of LLM-based and agentic AI systems (non-determinism, opacity, emergent behaviour)
3. Search for published regulatory guidance, enforcement actions, or advisory opinions on AI applicability
4. Map gaps: requirements the standards state but AI systems cannot currently satisfy by default
5. Identify mitigations or compensating controls referenced in official sources

## Sources

- [ ] [ISO/IEC 38505-1:2017 Information technology — Governance of IT — Governance of data](https://www.iso.org/standard/56639.html) — primary governance-of-data standard, defines accountability and oversight principles
- [ ] [DAMA International DMBOK2 — Data Management Body of Knowledge](https://www.dama.org/cpages/body-of-knowledge) — canonical data management framework; check data governance domain
- [ ] [NIST AI Risk Management Framework 1.0](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) — NIST's AI-specific risk framework with govern, map, measure, manage structure
- [ ] [GDPR Full Text — EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) — Articles 5, 22, and 25 are most relevant (accountability, automated decision-making, data protection by design)
- [ ] [California Consumer Privacy Act (CCPA) — State of California DOJ](https://oag.ca.gov/privacy/ccpa) — consumer rights and business obligations
- [ ] [HHS HIPAA for Professionals](https://www.hhs.gov/hipaa/for-professionals/index.html) — Privacy and Security Rules applicable to AI processing PHI

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
