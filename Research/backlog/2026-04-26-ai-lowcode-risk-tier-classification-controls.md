---
title: "How should Artificial Intelligence (AI) and low-code use cases be classified into risk tiers, and how should governance controls vary across those tiers?"
added: 2026-04-26
status: backlog
priority: high
blocks: [2026-04-26-ai-lowcode-decision-rights-accountability-liability, 2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-26-ai-governance-cost-performance-delivery-impact]
tags: [ai-governance, low-code, risk-classification, risk-tiers, enterprise-governance, controls, regulated-enterprise]
started: ~
completed: ~
output: [knowledge]
---

# How should Artificial Intelligence (AI) and low-code use cases be classified into risk tiers, and how should governance controls vary across those tiers?

## Research Question

What structured risk classification framework is appropriate for AI and low-code use cases in enterprise environments — specifically, how should categories such as informational, decision-support, and autonomous action systems be defined and bounded, and how should required governance controls, oversight intensity, and approval thresholds be mapped to each risk tier?

## Scope

**In scope:**
- Defining risk tier categories suited to enterprise AI and low-code use cases (e.g. informational, decision-support, autonomous action, and any intermediate tiers)
- Criteria for classifying a use case into a risk tier (reversibility of action, regulatory exposure, data sensitivity, scope of automated decision, human override availability)
- Mapping from risk tier to required governance controls (approval thresholds, oversight intensity, monitoring requirements, human review frequency)
- Existing risk classification frameworks from regulatory bodies (EU AI Act risk classification, NIST AI Risk Management Framework (RMF) 1.0, ISO/IEC 42001) and how they can be adapted for enterprise-internal classification
- How risk tier assignment should evolve when a use case changes scope or capability over time

**Out of scope:**
- Technical implementation of risk tier controls (covered by Q3/Q16)
- Per-regulation compliance mapping (covered by Q15)
- Vendor-specific limitations on implementing tier-appropriate controls (covered by Q11)
- Organisational factors affecting compliance with tier assignment (covered by Q14)

**Constraints:**
- Must produce a classification scheme that is operable by business analysts, not just risk specialists
- Must be compatible with at least one major external regulatory framework (EU AI Act or NIST AI RMF 1.0)
- Sources must be assessable for applicability to a regulated enterprise (financial services context preferred)

## Context

Governance controls that are uniform across all AI and low-code use cases are simultaneously over-controlling for low-risk informational tools and under-controlling for autonomous action systems. Without a structured risk classification framework, organisations either apply maximum controls everywhere (creating developer friction and shadow Information Technology (IT)) or apply minimal controls everywhere (creating unacceptable operational and regulatory risk). A tiered classification scheme is the foundational instrument from which all other governance design choices — accountability structures, enforcement points, observability requirements, lifecycle controls — derive their proportionality.

This item is prerequisite to Q1 (decision rights vary by risk tier), Q9 (human-in-the-loop thresholds are tier-specific), and Q8 (cost/benefit analysis requires knowing what controls are tier-appropriate).

Cross-references:
- Q1: `2026-04-26-ai-lowcode-decision-rights-accountability-liability`
- Q9: `2026-04-26-human-in-the-loop-ai-automated-workflows`
- Q8: `2026-04-26-ai-governance-cost-performance-delivery-impact`
- Q16: `2026-04-26-ai-agent-control-plane-architecture-enterprise`
- Q15: `2026-04-26-ai-lowcode-regulatory-compliance-alignment`

## Approach

1. **Survey existing classification frameworks:** Review the EU AI Act (prohibited, high-risk, limited risk, minimal risk), NIST AI RMF 1.0 (risk characterisation dimensions), ISO/IEC 42001, and any enterprise-specific tier models published by major financial services regulators (APRA, UK FCA/PRA, Basel Committee). Assess applicability to internal enterprise use cases (not just externally-facing AI systems).
2. **Define tier boundaries:** Based on the survey, propose a working set of risk tiers with explicit boundary criteria (what makes a use case fall into each tier, including edge cases at tier boundaries).
3. **Map controls to tiers:** For each tier, specify what governance controls are required — approval authority, documentation standard, monitoring frequency, human review requirements, incident escalation, decommissioning criteria.
4. **Evaluate operability:** Assess whether the proposed classification can be applied by a business analyst with minimal specialist knowledge — i.e., is it a usable decision framework, not just a theoretical taxonomy?
5. **Cross-reference with regulatory obligations:** Identify which tier boundaries align with regulatory trigger points (e.g., the EU AI Act's high-risk classification thresholds, APRA CPS 230 operational risk materiality).
6. **Synthesis:** Produce a practical risk tier classification decision tree and control matrix suitable for use as an enterprise governance artefact.

## Sources

- [ ] [EU AI Act — risk classification framework](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689) — primary regulatory classification model; assess for adaptability to internal enterprise use cases
- [ ] [NIST AI RMF 1.0 — Artificial Intelligence Risk Management Framework](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — US framework for AI risk characterisation; review the GOVERN, MAP, MEASURE, MANAGE functions for tier-relevant controls
- [ ] [ISO/IEC 42001 — AI Management System](https://www.iso.org/standard/81230.html) — management system standard; assess for risk classification guidance within an enterprise management system context
- [ ] [NIST AI RMF Playbook](https://airc.nist.gov/Docs/1) — operational guidance for applying NIST AI RMF; assess for classification operability
- [ ] [UK FCA/PRA Discussion Paper DP5/22 — Artificial Intelligence and Machine Learning](https://www.fca.org.uk/publication/discussion/dp22-4.pdf) — financial services regulator view on AI risk; assess for tier-boundary guidance relevant to regulated enterprises
- [ ] [APRA CPG 234 — Information Security](https://www.apra.gov.au/sites/default/files/cpg_234_information_security_june_2019_0.pdf) — assess for risk-tiered control proportionality model applicable to AI

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
