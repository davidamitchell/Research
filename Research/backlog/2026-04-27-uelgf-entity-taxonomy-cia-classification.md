---
title: "Universal Entity Lifecycle Governance Framework (UELGF): canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system for determining governance intensity"
added: 2026-04-27T01:28:25+00:00
status: backlog
priority: high
blocks: [2026-04-27-uelgf-synthesis-complete-framework]
tags: [uelgf, entity-taxonomy, cia-classification, governance-profile, agentic-ai, autonomous-agents, citizen-development, saas, data-products, regulated-banking, risk-tiering]
started: ~
completed: ~
output: [knowledge]
---

# Universal Entity Lifecycle Governance Framework (UELGF): canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system for determining governance intensity

## Research Question

What canonical entity taxonomy and Confidentiality, Integrity, and Availability (CIA) classification system should the UELGF use to determine governance intensity, ensuring that every entity type — from a fully autonomous AI agent to a procurement decision — receives a governance profile that is proportionate to its actual risk and that the classification process cannot be gamed by builder self-assessment at high CIA tiers?

## Scope

**In scope:**
- Canonical entity taxonomy covering all entity types: AI agents (subdivided by autonomy level), software services, Software as a Service (SaaS) products, data products, frontend applications, integration components, and policy and content artefacts
- For each entity type: distinguishing properties, observable characteristics at rail entry, mandatory classification inputs the builder must provide, mandatory invariants assigned at scaffold generation, and lifecycle stage variations
- CIA rating system: Confidentiality axis (data classification, subject count), Integrity axis (action reversibility, blast radius at machine speed), Availability axis (dependency criticality, failure consequence)
- CIA rating tiers (minimum: Low, Medium, High, Critical) with explicit thresholds per axis and tier
- CIA rating assignment process: who assigns, on what evidence, appeal and override process, and automatic rating floors by entity type (a fully autonomous agent with write access to financial systems cannot be self-assessed as Low)
- The governance profile matrix: mapping of entity type × CIA tier to applicable policy layers, mandatory hard gates, manual checkpoint requirements, observability requirements, and maximum re-evaluation intervals
- Criteria for automatic rating escalation when observed behaviour exceeds declared classification

**Out of scope:**
- Rail specifications for each entity type and CIA tier combination (covered by `2026-04-27-uelgf-governed-golden-rails`)
- Policy architecture design (covered by `2026-04-27-uelgf-policy-architecture-8-layer-context`)
- Foundational framework principles (covered by `2026-04-27-uelgf-foundational-definitions-principles`)
- Decommission and runtime feedback loop specifications

**Constraints:**
- The taxonomy must be exhaustive for the purposes of the framework — if an entity type is not in the taxonomy, it cannot enter a rail, which creates a gap
- CIA classification thresholds must be grounded in observable, measurable criteria, not qualitative self-assessment at Medium tier and above
- The autonomy-level sub-taxonomy for AI agents must be precise enough to place a given agent in exactly one sub-category without ambiguity — the distinctions between declarative/scoped, action agents with tool calls, event-triggered autonomous agents, and fully autonomous agents must be operationalisable

## Context

The entity taxonomy and CIA classification system is the decision mechanism that determines which rail an entity travels and what governance intensity applies. Without a precise taxonomy, entities of genuinely different risk profiles receive identical governance — both under- and over-governance result. Without automatic rating floors and an override process, high-risk entities (fully autonomous AI agents with write access to financial systems) can be systematically under-classified by builders motivated to minimise governance friction. This item produces the classification layer that all rail specifications and policy architecture components must reference.

Prior completed research directly informs this item:
- [AI agent control plane architecture for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — agent autonomy levels and control requirements
- [AI agent identity and access management for enterprise](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) — credential scoping and access control implications of agent type
- [Business-led low-code agent governance](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html) — citizen development entity types and governance constraints
- [AI and low-code risk tier classification and controls](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html) — risk tiering approaches for low-code and AI entities

## Approach

1. **Entity type taxonomy construction:** Survey existing classification systems for software entities — CMDB (Configuration Management Database) entity types in ServiceNow and BMC, cloud asset taxonomies (AWS resource types, Azure resource types), enterprise architecture asset taxonomies (TOGAF application components, ArchiMate application layer) — to identify canonical distinctions that are already operationalised. Determine where the UELGF taxonomy aligns with and departs from existing practice, and justify departures.
2. **AI agent autonomy sub-taxonomy:** Draw on the completed AI agent control plane research and agent taxonomy literature (e.g., ReAct, AutoGPT, and related agentic frameworks) to produce precise, operationalisable definitions for each autonomy level. Each definition must include a falsification criterion: a characteristic that, if present, moves the agent to a higher autonomy level.
3. **CIA framework selection and adaptation:** Survey CIA classification frameworks used in regulated financial services — APRA (Australian Prudential Regulation Authority) CPG 234, ISO/IEC 27005, NIST SP 800-30, PCI DSS data classification — to identify whether an existing framework provides the three-axis CIA model with blast-radius and reversibility criteria for the Integrity axis. Assess fitness and adapt or justify a novel specification.
4. **Rating floor and override mechanisms:** Investigate how high-assurance domains (nuclear safety, aviation, pharmaceutical manufacturing) implement mandatory minimum classification levels that cannot be overridden by individual assessors. Translate applicable mechanisms to the software entity governance context.
5. **Governance profile matrix construction:** Using the entity type taxonomy and CIA tiers as dimensions, construct the governance profile matrix. For each cell, specify: applicable policy layers from the 8-layer model, mandatory hard gates, manual checkpoint requirements, observability requirements, and maximum re-evaluation interval. Ground each matrix entry in a stated rationale.
6. **Invariants at scaffold generation:** For each entity type, identify which classification inputs become immutable invariants at the point of scaffold generation — values that, if the builder subsequently needs to change them, trigger full re-evaluation rather than a simple update. Justify each invariant selection.

## Sources

- [ ] [APRA CPG 234 — Information Security (guidance)](https://www.apra.gov.au/sites/default/files/cpg_234_information_security.pdf) — data classification and risk tiering in regulated financial services
- [ ] [NIST SP 800-30 Rev 1 — Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — CIA classification methodology
- [ ] [ISO/IEC 27005:2022 — Information Security Risk Management](https://www.iso.org/standard/80585.html) — risk assessment and classification framework
- [ ] [PCI DSS v4.0 Data Classification](https://www.pcisecuritystandards.org/document_library/) — cardholder data classification as a regulated-industry CIA model analogue
- [ ] [NIST AI RMF 1.0 — AI Risk Management Framework](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) — AI-specific risk dimensions including autonomy and reversibility
- [ ] [AI agent control plane architecture — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html) — agent autonomy levels and control implications
- [ ] [AI agent identity and access management — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html) — credential scoping by entity type
- [ ] [AI and low-code risk tier classification — completed item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-risk-tier-classification-controls.html) — existing risk tiering approaches
- [ ] [Business-led low-code agent governance — completed item](https://davidamitchell.github.io/Research/research/2026-04-24-business-led-low-code-agent-governance.html) — citizen development entity types
- [ ] [ServiceNow CMDB entity types documentation](https://docs.servicenow.com/bundle/washingtondc-it-asset-management/page/product/configuration-management/reference/cmdb-ci-class-hierarchy.html) — existing operational entity taxonomy as comparison point
- [ ] [AWS resource type taxonomy](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) — cloud asset classification as comparison point

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
