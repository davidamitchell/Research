---
title: "Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping"
added: 2026-03-21
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [capability-modelling, enterprise-architecture, togaf, sabsa, bian, tmf, csdm, business-capability-model, technical-capability-model, dependency-map, maturity-assessment, it-architecture, it-strategy]
started: ~
completed: ~
output: [knowledge]
---

# Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping

## Research Question

What established and emerging IT capability models define a complete, multi-level set of technical capabilities — such as authentication, networking, Application Programming Interface (API) gateways, and data storage — and which model or combination of models best supports: (a) designing new and existing solutions without tying to specific implementation details, and (b) assessing capability maturity against a standardised framework to identify where investment is needed?

Supporting questions:
- What multi-level capability taxonomy models currently exist across both traditional architecture frameworks and modern engineering-focused approaches?
- What are the strengths and weaknesses of each model for the purposes of abstract capability design and maturity assessment?
- How do these models handle the traceability link from business functions down through IT services to technical capabilities?
- How does ServiceNow's Common Service Data Model (CSDM) relate to or complement these capability models?
- Which single model or which combination would best serve as a foundation for a capability map that is implementation-agnostic and assessable for maturity?

## Scope

**In scope:**
- Established architecture framework capability models: TOGAF (The Open Group Architecture Framework) Application Reference Model (ARM) and Technology Reference Model (TRM); SABSA (Sherwood Applied Business Security Architecture); DoDAF (Department of Defense Architecture Framework) / NAF (NATO Architecture Framework); MODAF (Ministry of Defence Architecture Framework); BIAN (Banking Industry Architecture Network) Service Landscape; TM Forum (formerly TeleManagement Forum) Business Process Framework (eTOM) and Application Framework (TAM); NIST (National Institute of Standards and Technology) Cybersecurity Framework (CSF) and SP 800-series capability domains
- Modern / engineering-focused capability models: DORA (DevOps Research and Assessment) capabilities; Team Topologies interaction modes and platform capabilities; Cloud provider capability reference architectures (AWS (Amazon Web Services) Well-Architected Framework, Azure Well-Architected Framework, Google Cloud Architecture Framework); Wardley Mapping as a capability positioning tool; Infrastructure-as-Code (IaC) capability taxonomies; Site Reliability Engineering (SRE) capability domains; Zero Trust Architecture (ZTA) capability layers per NIST SP 800-207
- Capability model structural features: level of abstraction (business / logical / physical), multi-level decomposition, maturity model integration (CMM (Capability Maturity Model), CMMI (Capability Maturity Model Integration), Scaled Agile Framework (SAFe) Technical Portfolio), and support for implementation-independent expression
- Traceability mechanisms: how each model traces from business capability → IT service capability → technical capability component
- CSDM as a data model for capability representation: how its Business Application, Technical Service, Application Service, and Configuration Item (CI) layers map to capability model levels
- Maturity frameworks that attach to capability models: Gartner IT Score, CMMI for Services, IT Capability Maturity Framework (IT-CMF) from Innovation Value Institute (IVI)
- Prior completed research directly connected: `2026-03-08-servicenow-csdm-data-modelling`, `2026-03-08-servicenow-platform-strategy`

**Out of scope:**
- Specific tooling for capability modelling (Ardoq, LeanIX, Alfabet, ServiceNow, etc.) — framework evaluation only; ignore marketing claims
- Business capability models that do not have a technical/IT capability component (e.g., pure Business Motivation Model (BMM))
- IT Financial Management (ITFM) and Technology Business Management (TBM) cost allocation (covered in prior research)
- Process frameworks without a capability taxonomy dimension (e.g., ITIL v4 practices are processes, not capability models per se — note the distinction)
- Security-only models that don't address the full technical capability stack
- Vendor-specific product roadmaps or feature lists

**Constraints:** Publicly accessible sources. Prefer practitioner accounts, academic reviews, and framework primary sources over vendor marketing. Where a framework has a formal specification document, use that as the primary source for definitions. Where only vendor materials exist, flag as marketing and treat as low-confidence.

## Context

The goal is to build a capability map that can be used for two distinct activities:

1. **Solution design** — when designing a new or existing system, reason about what capabilities it requires (e.g., "this service needs API gateway capability, identity and access management capability, and event streaming capability") without being locked into specific technology choices (e.g., "this service uses Kong, Okta, and Kafka"). The capability map should be the stable layer; the implementation layer should be variable and traceable to it.

2. **Maturity assessment** — evaluate the current state of each technical capability against a standardised framework. This produces a capability heat map: which capabilities are mature and reliable, which are fragile or absent, and where investment is most urgently needed. Without a standardised capability model, maturity assessments are ad hoc and non-comparable across teams, programmes, or time periods.

The connection to CSDM is important: ServiceNow's CSDM already defines a layered data model (Business Application → Application Service → Technical Service → Infrastructure CI) that is used for Configuration Management Database (CMDB) governance, IT Service Management (ITSM), Application Portfolio Management (APM), and Integrated Risk Management (IRM) linkage. However, CSDM is a data model, not a capability taxonomy. The question is whether an existing capability model can be mapped onto or integrated with CSDM's layer structure to produce a traceable capability map within or alongside ServiceNow.

Modern engineering practice (Wardley Mapping, Team Topologies, cloud Well-Architected Frameworks) has produced alternative approaches that are closer to how engineering teams actually think about capabilities — as composable, evolvable building blocks rather than formal architecture artefacts. These modern approaches may offer a more practical and maintainable capability taxonomy, but they may lack the formal rigour or industry standardisation needed for governance and maturity assessment.

**Prior research connections:**
- CSDM layer structure and data modelling: `2026-03-08-servicenow-csdm-data-modelling` — established the CSDM layers and their practical governance challenges; the present item must determine what capability taxonomy maps cleanly onto those layers.
- ServiceNow platform strategy: `2026-03-08-servicenow-platform-strategy` — established ServiceNow as the operational platform; the capability model must be compatible with CSDM.

## Approach

1. **Enumerate all candidate models** — produce a complete list of multi-level technical capability models from both traditional architecture frameworks and modern engineering practice. For each, note: source organisation, primary document, year, whether it is actively maintained, and whether it includes a formal capability taxonomy at multiple abstraction levels.

2. **Structural analysis** — for each model, analyse: (a) how many levels of capability decomposition it provides, (b) whether it distinguishes between business capability, logical IT capability, and physical/technical implementation, (c) whether it has a defined maturity assessment component, and (d) how it handles traceability from business function to technical component.

3. **Strengths and weaknesses per model** — produce a concise strengths/weaknesses assessment for each model relative to the stated goals: implementation-agnostic design and standardised maturity assessment.

4. **CSDM alignment analysis** — map each candidate model's levels to CSDM's Business Application / Application Service / Technical Service / CI layers. Which models align naturally? Which require bridging abstractions?

5. **Modern engineering approaches** — examine Wardley Mapping, Team Topologies platform design, DORA capabilities, and cloud Well-Architected Frameworks as engineering-native capability models. Assess their completeness as a technical capability taxonomy and their suitability for governance-grade maturity assessment.

6. **Recommendation** — synthesise findings into a recommendation: a single model, a combination, or a custom synthesis. The recommendation must address: (a) which model provides the best capability taxonomy, (b) which provides the best maturity assessment mechanism, (c) how they integrate with CSDM, and (d) what the migration path is from an unmapped state to a populated capability map.

7. **Synthesis** — produce Executive Summary, Key Findings, Evidence Map, and Recommendation.

## Sources

- [ ] TOGAF Standard (10th Edition, 2022) — The Open Group — https://www.opengroup.org/togaf — specifically the Architecture Reference Models chapter; primary source for TOGAF Technical Reference Model (TRM) and Integrated Information Infrastructure Reference Model (III-RM)
- [ ] SABSA Framework and Architecture — The SABSA Institute — https://sabsa.org — specifically the Business Attributes Profile and the SABSA Matrix; primary source for SABSA capability layers
- [ ] BIAN Service Landscape (v12, 2023) — Banking Industry Architecture Network — https://bian.org — the service domain taxonomy as a banking-specific technical capability model
- [ ] TM Forum Frameworx — TM Forum — https://www.tmforum.org — specifically the Business Process Framework (eTOM) and Application Framework (TAM) capability taxonomies
- [ ] NIST SP 800-207 (2020) — "Zero Trust Architecture" — NIST — https://doi.org/10.6028/NIST.SP.800-207 — ZTA capability components as a modern security-layer capability model
- [ ] NIST Cybersecurity Framework (CSF) 2.0 (2024) — NIST — https://doi.org/10.6028/NIST.CSWP.29 — capability function taxonomy (Govern, Identify, Protect, Detect, Respond, Recover)
- [ ] DoDAF Architecture Framework (v2.02) — US Department of Defense — https://dodcio.defense.gov/library/dod-architecture-framework/ — specifically capability viewpoints (CV-1 through CV-7)
- [ ] NAF v4 (2018) — NATO Architecture Framework — https://www.nato.int/cps/en/natohq/topics_157575.htm — capability taxonomy and C3 Taxonomy
- [ ] IT-CMF (IT Capability Maturity Framework) — Innovation Value Institute (IVI) — https://ivi.ie/it-cmf/ — the 36-capability taxonomy and maturity model
- [ ] CMMI v2.0 (2018) — CMMI Institute — https://cmmiinstitute.com — capability area and practice area structure as a maturity-linked capability model
- [ ] "Wardley Mapping" — Simon Wardley (2016–2024) — https://learnwardleymapping.com and https://medium.com/wardleymaps — capability evolution model from genesis to commodity
- [ ] "Team Topologies" — Skelton, M. & Pais, M. (2019) — IT Revolution Press — specifically platform team capability design and the interaction modes
- [ ] DORA (DevOps Research and Assessment) State of DevOps Reports (2019–2024) — Google/DORA — https://dora.dev — technical and process capability clusters and their performance linkages
- [ ] AWS Well-Architected Framework (2024) — Amazon Web Services — https://aws.amazon.com/architecture/well-architected/ — six pillars as a cloud-native technical capability taxonomy
- [ ] Azure Well-Architected Framework (2024) — Microsoft — https://learn.microsoft.com/en-us/azure/well-architected/ — five pillars and design area taxonomy
- [ ] Google Cloud Architecture Framework (2024) — Google — https://cloud.google.com/architecture/framework — system design principles as capability taxonomy
- [ ] Gartner IT Score — Gartner — https://www.gartner.com/en/information-technology/it-score — IT functional capability model and maturity scoring (note: marketing from Gartner; treat as low-confidence for structural detail but useful for industry adoption evidence)
- [ ] Prior completed research: `2026-03-08-servicenow-csdm-data-modelling`
- [ ] Prior completed research: `2026-03-08-servicenow-platform-strategy`

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

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

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
