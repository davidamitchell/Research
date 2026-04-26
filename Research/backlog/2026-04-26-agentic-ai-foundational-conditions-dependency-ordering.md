---
title: "Dependency ordering of foundational conditions for safe agentic Artificial Intelligence (AI) deployment: the prerequisite graph and the regulatory consequence of deploying at any layer before the layer below it is satisfied"
added: 2026-04-26
status: backlog
priority: high
blocks: []
tags: [agentic-ai, dependency-ordering, foundational-conditions, access-control, rag, policy-coherence, deployment-pipeline, synthesis, regulated-banking, operational-risk, regulatory-compliance]
started: ~
completed: ~
output: [knowledge]
---

# Dependency ordering of foundational conditions for safe agentic Artificial Intelligence (AI) deployment: the prerequisite graph and the regulatory consequence of deploying at any layer before the layer below it is satisfied

## Research Question

The foundational conditions for safe agentic AI deployment in a regulated financial institution are not independent — they form a dependency graph in which policy coherence is a prerequisite for information architecture, which is a prerequisite for access control, which is a prerequisite for safe agent credential scoping, which is a prerequisite for safe Retrieval-Augmented Generation (RAG) deployment over organisational knowledge, which is a prerequisite for safe deployment of the deployment pipeline gate itself. What is the correct characterisation of this dependency ordering? What is the consequence of deploying at any layer before the layer below it is satisfied — is the consequence merely increased risk, or does it constitute a control failure under any applicable regulatory framework? And does any existing framework — zero trust, operational resilience, AI governance — explicitly encode this dependency ordering, or must it be constructed as a novel contribution?

## Scope

**In scope:**
- Characterising the dependency ordering of the following five foundational conditions: (1) policy coherence, (2) information architecture and access control, (3) agent credential scoping and least privilege, (4) permission-safe RAG deployment, (5) deployment pipeline governance gate
- Whether each dependency relationship is logically necessary (lower layer must be satisfied for upper layer to be technically achievable) or merely strongly recommended (lower layer increases risk if unsatisfied but upper layer remains technically deployable)
- The regulatory consequence of deploying at each layer before the layer below it is satisfied: is the consequence characterised by applicable frameworks (APRA CPS 230, DORA, NIST SP 800-207, ISO 31000) as increased risk, governance gap, or current control failure?
- Whether any existing framework explicitly encodes the dependency ordering, or whether the ordering must be constructed as a novel synthesis from first principles and the companion research items
- Cross-reference and synthesis of findings from the five companion research items: permission-safe RAG and information architecture; access control amplification under agentic operations; implicit rate-limiting controls removed by agentic AI; policy coherence as machine-checkable prerequisite; deployment pipeline as governed control gate
- The relationship between the dependency ordering and the systems capability debt causal chain established in prior completed research

**Out of scope:**
- Detailed investigation of any individual layer (each is covered by a companion research item)
- AI model selection, deployment architecture, or technical implementation of individual controls
- Research methodology or data collection for the companion items — this is a synthesis item
- Jurisdiction-specific legal analysis beyond what is needed to characterise the regulatory consequence finding

**Constraints:**
- This item should not be started until the five companion items (permission-safe RAG, access control amplification, implicit rate-limiting controls, policy coherence, deployment pipeline) are completed, as it synthesises their findings
- The dependency graph characterisation must distinguish logical necessity from empirical regularity — a relationship that has always been observed to hold is not the same as a relationship that is logically required
- The regulatory consequence characterisation must be grounded in the findings of the completed regulatory preconditions item and the companion items, not asserted independently

## Context

This is the synthesis item for the full set of research questions raised in the original issue. The following companion items must be completed before this synthesis is attempted:

- Permission-safe RAG in enterprise information architectures (backlog: `2026-04-26-permission-safe-rag-enterprise-information-architecture`)
- Access control amplification under agentic operations (backlog: `2026-04-26-access-control-amplification-agentic-operations`)
- Implicit rate-limiting controls removed by agentic AI (backlog: `2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal`)
- Policy coherence as machine-checkable prerequisite (backlog: `2026-04-26-policy-coherence-machine-checkable-prerequisite`)
- Deployment pipeline as the only enforceable control gate (backlog: `2026-04-26-deployment-pipeline-citizen-development-governed-gate`)

The following completed items provide the foundational context:
- [Systems capability debt and agentic AI operational risk: the causal chain and the AI-for-risk-reduction sequencing argument](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html)
- [Systems capability debt as the root cause of citizen development: empirical evidence and effective governance architectures](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html)
- [Regulatory and standards preconditions for deployment of agentic AI systems](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html)
- [Global artificial intelligence agent regulation in financial services](https://davidamitchell.github.io/Research/research/2026-04-24-ai-agent-regulation-global-financial-services.html)
- [Business-led low-code agent governance: conditions for durable value versus fragmentation in regulated environments](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html)

## Approach

1. **Dependency graph construction:** Draw on the findings of all five companion items to construct the dependency graph of foundational conditions. For each dependency relationship, assess whether it is logically necessary or empirically observed. Produce a directed acyclic graph (DAG) of the relationships with a written justification for each edge.
2. **Layer-violation consequence analysis:** For each layer in the dependency ordering, assess what the regulatory consequence is of deploying at that layer before the layer below it is satisfied — drawing on the regulatory preconditions completed item and the companion items for the specific control-failure evidence.
3. **Framework encoding survey:** Survey the zero trust literature (NIST SP 800-207), operational resilience frameworks (APRA CPS 230, DORA, Basel), and AI governance frameworks (NIST AI RMF 1.0, ISO 42001) for any explicit encoding of a deployment-prerequisites dependency ordering or any guidance that resembles the dependency graph constructed here.
4. **Novelty assessment:** Assess whether the dependency graph is a novel contribution — i.e., whether no existing framework encodes the full ordering — or whether it can be derived from one or more existing frameworks without additional synthesis.
5. **Decision framework:** Produce a decision framework characterising what each layer requires, what the minimum bar for "satisfying" each layer is, and what the test a board risk committee or risk function should apply to determine whether it is safe to proceed to the next layer.
6. **Synthesis:** Integrate all findings into an executive summary, key findings, and a visual representation of the dependency graph suitable for use in a board risk committee presentation.

## Sources

- [ ] [Systems capability debt agentic AI risk synthesis — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.html) — foundational context
- [ ] [Systems capability debt citizen development empirical evidence — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-systems-capability-debt-citizen-development-empirical-evidence.html) — empirical base
- [ ] [Regulatory preconditions for agentic AI deployment — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-agentic-ai-regulatory-preconditions-control-failure-assessment.html) — regulatory consequence base
- [ ] [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — assess for any explicit prerequisite ordering or maturity model
- [ ] [NIST AI RMF 1.0 and Playbook](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — assess for any explicit staging or maturity ordering of governance conditions
- [ ] [ISO/IEC 42001 — AI Management System](https://www.iso.org/standard/81230.html) — assess for management-system maturity staging
- [ ] [APRA CPS 230 — Operational Risk Management](https://handbook.apra.gov.au/standard/cps-230) — assess for any explicit sequencing of operational-resilience controls
- [ ] [DORA — Regulation (EU) 2022/2554](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2554) — assess for ICT risk management staging or prerequisite ordering
- [ ] [CMMI (Capability Maturity Model Integration) and comparable maturity frameworks](https://cmmiinstitute.com/) — assess for whether process maturity models provide analogous dependency ordering concepts applicable to AI governance

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
