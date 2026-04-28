---
review_count: 2
title: "Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping"
added: 2026-03-22T07:06:52+00:00
status: completed
priority: high  # low | medium | high
blocks: []
tags: [capability-modelling, enterprise-architecture, togaf, sabsa, bian, tmf, csdm, business-capability-model, technical-capability-model, dependency-map, maturity-assessment, it-architecture, it-strategy]
started: 2026-03-22T07:06:52+00:00
completed: 2026-03-22T07:06:52+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Technology Capability Models: Survey, Comparison, and Recommendation for Multi-Level IT Capability Mapping

## Research Question

What established and emerging IT capability models define a complete, multi-level set of technical capabilities - such as authentication, networking, Application Programming Interface (API) gateways, and data storage - and which model or combination of models best supports: (a) designing new and existing solutions without tying to specific implementation details, and (b) assessing capability maturity against a standardised framework to identify where investment is needed?

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
- Traceability mechanisms: how each model traces from business capability -> IT service capability -> technical capability component
- CSDM as a data model for capability representation: how its Business Application, Technical Service, Application Service, and Configuration Item (CI) layers map to capability model levels
- Maturity frameworks that attach to capability models: Gartner IT Score, CMMI for Services, IT Capability Maturity Framework (IT-CMF) from Innovation Value Institute (IVI)
- Prior completed research directly connected: `2026-03-08-servicenow-csdm-data-modelling`, `2026-03-08-servicenow-platform-strategy`

**Out of scope:**
- Specific tooling for capability modelling (Ardoq, LeanIX, Alfabet, ServiceNow, etc.) - framework evaluation only; ignore marketing claims
- Business capability models that do not have a technical/IT capability component (e.g., pure Business Motivation Model (BMM))
- IT Financial Management (ITFM) and Technology Business Management (TBM) cost allocation (covered in prior research)
- Process frameworks without a capability taxonomy dimension (e.g., ITIL v4 practices are processes, not capability models per se - note the distinction)
- Security-only models that don't address the full technical capability stack
- Vendor-specific product roadmaps or feature lists

**Constraints:** Publicly accessible sources. Prefer practitioner accounts, academic reviews, and framework primary sources over vendor marketing. Where a framework has a formal specification document, use that as the primary source for definitions. Where only vendor materials exist, flag as marketing and treat as low-confidence.

## Context

The goal is to build a capability map that can be used for two distinct activities:

1. **Solution design** - when designing a new or existing system, reason about what capabilities it requires (e.g., "this service needs API gateway capability, identity and access management capability, and event streaming capability") without being locked into specific technology choices (e.g., "this service uses Kong, Okta, and Kafka"). The capability map should be the stable layer; the implementation layer should be variable and traceable to it.

2. **Maturity assessment** - evaluate the current state of each technical capability against a standardised framework. This produces a capability heat map: which capabilities are mature and reliable, which are fragile or absent, and where investment is most urgently needed. Without a standardised capability model, maturity assessments are ad hoc and non-comparable across teams, programmes, or time periods.

The connection to CSDM is important: prior repository work on ServiceNow treats CSDM as a layered data model that separates Business Application, Application Service, Technical Service, and Configuration Item concerns for operational traceability rather than for capability definition. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`. The question in this item is whether an existing capability model can be mapped onto or integrated with that layer structure to produce a traceable capability map within or alongside ServiceNow.

Modern engineering practice (Wardley Mapping, Team Topologies, cloud Well-Architected Frameworks) has produced alternative approaches that are closer to how engineering teams actually think about capabilities - as composable, evolvable building blocks rather than formal architecture artefacts. These modern approaches may offer a more practical and maintainable capability taxonomy, but they may lack the formal rigour or industry standardisation needed for governance and maturity assessment.

**Prior research connections:**
- CSDM layer structure and data modelling: `2026-03-08-servicenow-csdm-data-modelling` - established the CSDM layers and their practical governance challenges; the present item must determine what capability taxonomy maps cleanly onto those layers.
- ServiceNow platform strategy: `2026-03-08-servicenow-platform-strategy` - established ServiceNow as the operational platform; the capability model must be compatible with CSDM.

## Approach

1. **Enumerate all candidate models** - produce a complete list of multi-level technical capability models from both traditional architecture frameworks and modern engineering practice. For each, note: source organisation, primary document, year, whether it is actively maintained, and whether it includes a formal capability taxonomy at multiple abstraction levels.

2. **Structural analysis** - for each model, analyse: (a) how many levels of capability decomposition it provides, (b) whether it distinguishes between business capability, logical IT capability, and physical/technical implementation, (c) whether it has a defined maturity assessment component, and (d) how it handles traceability from business function to technical component.

3. **Strengths and weaknesses per model** - produce a concise strengths/weaknesses assessment for each model relative to the stated goals: implementation-agnostic design and standardised maturity assessment.

4. **CSDM alignment analysis** - map each candidate model's levels to CSDM's Business Application / Application Service / Technical Service / CI layers. Which models align naturally? Which require bridging abstractions?

5. **Modern engineering approaches** - examine Wardley Mapping, Team Topologies platform design, DORA capabilities, and cloud Well-Architected Frameworks as engineering-native capability models. Assess their completeness as a technical capability taxonomy and their suitability for governance-grade maturity assessment.

6. **Recommendation** - synthesise findings into a recommendation: a single model, a combination, or a custom synthesis. The recommendation must address: (a) which model provides the best capability taxonomy, (b) which provides the best maturity assessment mechanism, (c) how they integrate with CSDM, and (d) what the migration path is from an unmapped state to a populated capability map.

7. **Synthesis** - produce Executive Summary, Key Findings, Evidence Map, and Recommendation.

## Sources

- [x] TOGAF Standard (10th Edition, 2022) - The Open Group - https://www.opengroup.org/togaf - specifically the Architecture Reference Models chapter; primary source for TOGAF Technical Reference Model (TRM) and Integrated Information Infrastructure Reference Model (III-RM)
- [x] SABSA Framework and Architecture - The SABSA Institute - https://sabsa.org - specifically the Business Attributes Profile and the SABSA Matrix; primary source for SABSA capability layers
- [x] BIAN Service Landscape (v12, 2023) - Banking Industry Architecture Network - https://bian.org - the service domain taxonomy as a banking-specific technical capability model
- [x] TM Forum Frameworx - TM Forum - https://www.tmforum.org - specifically the Business Process Framework (eTOM) and Application Framework (TAM) capability taxonomies
- [x] NIST SP 800-207 (2020) - "Zero Trust Architecture" - NIST - https://doi.org/10.6028/NIST.SP.800-207 - ZTA capability components as a modern security-layer capability model
- [x] NIST Cybersecurity Framework (CSF) 2.0 (2024) - NIST - https://doi.org/10.6028/NIST.CSWP.29 - capability function taxonomy (Govern, Identify, Protect, Detect, Respond, Recover)
- [x] DoDAF Architecture Framework (v2.02) - US Department of Defense - https://dodcio.defense.gov/library/dod-architecture-framework/ - specifically capability viewpoints (CV-1 through CV-7)
- [x] NAF v4 (2018) - NATO Architecture Framework - https://www.nato.int/cps/en/natohq/topics_157575.htm - capability taxonomy and Consultation, Command and Control (C3) Taxonomy
- [x] IT-CMF (IT Capability Maturity Framework) - Innovation Value Institute (IVI) - https://ivi.ie/it-cmf/ - the 36-capability taxonomy and maturity model
- [x] CMMI v2.0 (2018) - CMMI Institute - https://cmmiinstitute.com - capability area and practice area structure as a maturity-linked capability model
- [x] "Wardley Mapping" - Simon Wardley (2016-2024) - https://learnwardleymapping.com and https://medium.com/wardleymaps - capability evolution model from genesis to commodity
- [x] "Team Topologies" - Skelton, M. & Pais, M. (2019) - IT Revolution Press - specifically platform team capability design and the interaction modes
- [x] DORA (DevOps Research and Assessment) State of DevOps Reports (2019-2024) - Google/DORA - https://dora.dev - technical and process capability clusters and their performance linkages
- [x] AWS Well-Architected Framework (2024) - Amazon Web Services - https://aws.amazon.com/architecture/well-architected/ - six pillars as a cloud-native technical capability taxonomy
- [x] Azure Well-Architected Framework (2024) - Microsoft - https://learn.microsoft.com/en-us/azure/well-architected/ - five pillars and design area taxonomy
- [x] Google Cloud Architecture Framework (2024) - Google - https://cloud.google.com/architecture/framework - system design principles as capability taxonomy
- [x] Gartner IT Score - Gartner - https://www.gartner.com/en/information-technology/it-score - IT functional capability model and maturity scoring (note: marketing from Gartner; treat as low-confidence for structural detail but useful for industry adoption evidence)
- [x] Prior completed research: `2026-03-08-servicenow-csdm-data-modelling`
- [x] Prior completed research: `2026-03-08-servicenow-platform-strategy`

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- **[fact]** The research question asks which established and emerging Information Technology (IT) capability models can support both implementation-agnostic solution design and repeatable maturity assessment across a multi-level technical stack that includes identity, networking, integration, and data capabilities. Source: this item's Research Question and Scope.
- **[fact]** The investigation is constrained to public framework sources, practitioner-accessible summaries, and two prior completed repository items on ServiceNow's Common Service Data Model (CSDM) and platform strategy. Source: this item's Constraints and Prior research connections.
- **[fact]** Prior repository work already established that CSDM is a layered operational data model for traceability rather than a capability taxonomy, and that higher-order governance becomes reliable only after Foundation Data and technical-service layers are stable. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.
- **[fact]** The required output is a structured knowledge item that distinguishes full-stack capability taxonomies from reference models, security slices, maturity overlays, and operating-model lenses, then recommends the best-supported combination for use with CSDM. Source: this item's Approach.
- **[inference]** The most likely correct answer is a layered combination rather than a single framework, because the question combines two needs that frameworks often separate in practice: capability classification and maturity scoring. Sources: this item's Research Question; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.

### §1 Question Decomposition

- **A. Framework identification**
  - A1. Which surveyed models are true capability taxonomies rather than process frameworks, reference models, or assessment guides?
  - A2. Which models are cross-industry and which are domain-specific?
- **B. Structural fit**
  - B1. Which models decompose capabilities across business, logical, and physical or implementation layers?
  - B2. Which models can represent common enterprise technical capabilities such as identity, networking, integration, and data?
- **C. Assessment fit**
  - C1. Which models include built-in maturity scoring or improvement roadmaps?
  - C2. Which models require an external maturity overlay?
- **D. Traceability fit**
  - D1. Which models connect business capability to application/service and implementation layers?
  - D2. How can those layers map onto Business Application, Application Service, Technical Service, and Configuration Item (CI) structures in CSDM?
- **E. Overlay fit**
  - E1. Which models are best treated as domain overlays, security overlays, or operating-model lenses instead of the primary taxonomy?
  - E2. Which modern engineering approaches improve prioritisation or team design without defining the taxonomy itself?
- **F. Recommendation**
  - F1. What is the best single-framework answer if a single choice is mandatory?
  - F2. What is the best combined-stack answer if composition is allowed?
  - F3. What migration path is most evidence-supported for an organisation starting with CSDM but no mature capability map?

### §2 Investigation

#### 2.1 Prior work cross-reference

- **[fact]** `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md` found that CSDM separates Business Application, Application Service, Technical Service, and Configuration Item layers, and that those layers solve traceability and ownership problems but do not define an enterprise capability taxonomy.
- **[fact]** `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md` found that ServiceNow governance value depends on sequencing data foundations and technical-service maturity before strategic portfolio layers.
- **[inference]** The present item therefore needs a taxonomy that can be attached to CSDM, not a replacement for CSDM itself.

#### 2.2 Sources consulted and source quality

- **[fact]** Primary official or near-primary framework sources consulted for this item were: The Open Group on TOGAF (`https://www.opengroup.org/togaf`), Banking Industry Architecture Network (BIAN) Service Landscape (`https://bian.org/service-landscape/`), National Institute of Standards and Technology (NIST) Special Publication 800-207 (`https://csrc.nist.gov/pubs/sp/800/207/final`), NIST Cybersecurity Framework (CSF) 2.0 public resource material (`https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`), Innovation Value Institute (IVI) IT Capability Maturity Framework (IT-CMF) (`https://ivi.ie/it-capability-maturity-framework/`), Team Topologies (`https://teamtopologies.com/key-concepts`), DevOps Research and Assessment (DORA) (`https://dora.dev/`), AWS (Amazon Web Services) Well-Architected (`https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`), Azure Well-Architected (`https://learn.microsoft.com/en-us/azure/well-architected/`), Google Cloud Architecture Framework (`https://cloud.google.com/architecture/framework`), and the Department of Defense Architecture Framework (DoDAF) 2.02 public PDF (`https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`).
- **[fact]** Some official pages were partially inaccessible from this environment: SABSA Institute public pages returned 403 during direct fetch, and TM Forum official eTOM/TAM pages also returned 403 during direct fetch. Public summaries and official URL metadata were still available via search. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://www.tmforum.org/oda/open-digital-architecture/information-framework-sid/application-framework-tam/`.
- **[inference]** Claims built on inaccessible official pages are therefore lower-confidence than claims built on fully accessible official framework pages, and are treated as such below.

#### 2.3 General-purpose reference models and capability-planning frameworks

- **[fact]** The Open Group positions TOGAF as a standard enterprise architecture framework, and public TOGAF reference-model material describes the Technical Reference Model (TRM) as a generic platform-service taxonomy while the Integrated Information Infrastructure Reference Model (III-RM) extends application and data architecture concepts. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`.
- **[inference]** TOGAF is the closest surveyed cross-industry starting point for an implementation-agnostic technical capability backbone, but its public reference-model content is too coarse to function as a modern finished capability library on its own. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`; `https://ivi.ie/it-capability-maturity-framework/`.
- **[fact]** DoDAF 2.02 capability viewpoints cover capability vision, taxonomy, phasing, dependencies, and mappings to services or operational activities, but the framework separates those planning views from the more technical systems and services viewpoints. Sources: `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://dodcio.defense.gov/Library/DoD-Architecture-Framework/dodaf20_capability/`.
- **[fact]** NATO Architecture Framework (NAF) v4 and the NATO Consultation, Command and Control (C3) taxonomy support capability hierarchy and service decomposition for interoperability planning. Sources: `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://nisp.nw3.dk/node/T-a0d92ce5-6739-407c-82db-6ed315aa3651-X.html`; `https://www.ffi.no/en/publications-archive/service-decomposition-using-the-nato-c3-taxonomy-case-studies`.
- **[inference]** DoDAF and NAF are strong on top-down traceability, but they are specialised meta-models for defence and interoperability contexts rather than low-friction enterprise technology capability maps for a typical mixed IT estate. Sources: `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://nisp.nw3.dk/node/T-a0d92ce5-6739-407c-82db-6ed315aa3651-X.html`.

#### 2.4 Security-specific models and security overlays

- **[fact]** Public SABSA descriptions consistently present a six-layer architecture from contextual business requirements through conceptual, logical, physical, component, and operational layers, with security services and controls derived from a Business Attributes Profile. Sources: `https://en.wikipedia.org/wiki/Sherwood_Applied_Business_Security_Architecture`; `https://davidlynas.com/sabsa/`; `https://sabsa.org/sabsa-executive-summary/`.
- **[fact]** NIST CSF 2.0 defines six concurrent functions - Govern, Identify, Protect, Detect, Respond, and Recover - and uses profiles and tiers to tailor and characterise cybersecurity outcomes rather than prescribing a full technical implementation model. Sources: `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.rip/projects/cybersecurity-framework/nist-cybersecurity-framework-resource-and-overview`.
- **[fact]** NIST Special Publication 800-207 defines Zero Trust Architecture (ZTA) as an abstract architecture with no implicit trust based on network location and describes logical elements such as policy engines and enforcement points. Source: `https://csrc.nist.gov/pubs/sp/800/207/final`.
- **[inference]** SABSA, NIST CSF 2.0, and ZTA are all valuable overlays for security capability families, but none is intended to serve as the enterprise-wide technical capability backbone for the entire stack. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`.

#### 2.5 Domain-specific capability taxonomies

- **[fact]** BIAN's public service-landscape releases describe a banking model built around business capabilities, service domains, business scenarios, and standardised interfaces, with release 12 explicitly noting completed service domains and business capability content. Source: `https://bian.org/service-landscape/`.
- **[inference]** BIAN is a strong domain-specific capability taxonomy for banking because it decomposes business and service capabilities into reusable bounded domains, but it is not intended as a cross-industry technology capability model. Sources: `https://bian.org/service-landscape/`; `https://envizion.eu/blog/expressing-the-bian-reference-model-for-the-banking-industry-in-the-archimate-modeling-language.html`.
- **[fact]** Public TM Forum material and allied industry explainers distinguish eTOM as the Business Process Framework and Telecom Application Map (TAM) as the application-framework layer that maps telecom applications to business processes. Sources: `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://www.ntt-review.jp/archive/ntttechnical.php?contents=ntr202307gls_s.html`; `https://www.telecom-expertise.com/areas-of-expertise/`.
- **[inference]** TM Forum TAM is useful as a telecom-specific application capability taxonomy, but its industry specificity and partial source inaccessibility make it unsuitable as the general enterprise-wide core taxonomy for this repository's use case. Sources: `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://www.ntt-review.jp/archive/ntttechnical.php?contents=ntr202307gls_s.html`; `https://www.telecom-expertise.com/areas-of-expertise/`.

#### 2.6 Maturity frameworks and operating or review overlays

- **[fact]** IVI describes IT-CMF as a framework for deriving business value from IT, organised into four macro-capabilities and 37 Critical Capabilities, each with maturity profiles, assessment methods, and improvement roadmaps. Source: `https://ivi.ie/it-capability-maturity-framework/`.
- **[fact]** Public CMMI v2.0 materials describe practice areas and maturity or capability levels as a structured process-improvement model rather than a detailed enterprise technical capability inventory. Sources: `https://cmmiinstitute.com/learning/appraisals/levels`; `https://cmmiinstitute.com/cmmi/intro`.
- **[fact]** Gartner's public IT Score material presents the product as a capability-based maturity assessment with prioritised gap analysis, but the detailed question sets and scoring mechanics are gated, so it is useful mainly as adoption context rather than as a transparent framework source. Sources: `https://www.gartner.com/en/information-technology/research/gartner-it-score`; `https://www.gartner.com/en/research/methodologies/gartner-score-diagnostic-family`; `https://static.gartner.com/assets/pdf/score/RO_635300_EUP_Gartner_Score_FAQ_R2.pdf`.
- **[fact]** DORA describes itself as a research program studying the capabilities that drive software delivery and operations performance. Source: `https://dora.dev/`.
- **[fact]** Team Topologies defines four team types and three interaction modes as an approach to designing organisations for fast flow of value, and explicitly frames itself as a thinking model rather than an organisation-chart template. Sources: `https://teamtopologies.com/key-concepts`; `https://www.atlassian.com/devops/frameworks/team-topologies`.
- **[fact]** AWS, Azure, and Google all frame their well-architected guidance as principle or pillar-based assessment frameworks with review questions and design guidance rather than exhaustive capability libraries. Sources: `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.
- **[fact]** Wardley Mapping is publicly described as a strategic tool for positioning components in a value chain against their stage of evolution, from genesis to commodity, rather than as a capability taxonomy. Sources: `https://learnwardleymapping.com/`; `https://www.wardleymaps.com/guides/wardley-mapping-101`.
- **[inference]** IT-CMF is the strongest surveyed maturity overlay for enterprise Information Technology capability heat-maps, while CMMI, Gartner IT Score, DORA, Team Topologies, Wardley Mapping, and the cloud well-architected frameworks are better treated as targeted process, performance, operating, strategy, or design overlays rather than as the taxonomy itself. Sources: `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`; `https://www.gartner.com/en/information-technology/research/gartner-it-score`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.

#### 2.7 CSDM alignment and recommendation logic

- **[fact]** Prior repository work established that CSDM already provides persistence and traceability layers for Business Application, Application Service, Technical Service, and Configuration Item entities. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.
- **[inference]** The cleanest mapping is: business or domain capability to Business Capability and Business Application; logical application-facing capability to Business Application plus Application Service; shared technical or platform capability to Technical Service; concrete implementation to Configuration Item. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`.
- **[inference]** If a single model must be chosen, TOGAF is the closest generic starting point because it is the strongest cross-industry reference-model family in the set, but it remains insufficient alone because it lacks a strong built-in maturity method and requires local extension for modern platform capabilities. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`; `https://ivi.ie/it-capability-maturity-framework/`.
- **[inference]** The best-supported combined answer is TOGAF-style reference-model structure as the capability backbone, CSDM as the operational traceability layer, IT-CMF as the maturity overlay, and domain or quality overlays - BIAN, TM Forum TAM, SABSA, NIST CSF 2.0, ZTA, DORA, Team Topologies, and cloud well-architected frameworks - applied only where relevant. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://bian.org/service-landscape/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`; `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.

### §3 Reasoning

- **[fact]** The surveyed models fell into four functional categories: cross-industry reference models, domain-specific capability taxonomies, security or quality overlays, and maturity overlays. Sources: Section 2 of this item; `https://www.opengroup.org/togaf`; `https://bian.org/service-landscape/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://ivi.ie/it-capability-maturity-framework/`.
- **[inference]** The research question spans both classification and assessment, and the evidence shows that public frameworks usually specialise in one of those functions rather than both. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`.
- **[inference]** That split makes a layered recommendation stronger than a single-framework recommendation, because forcing a single model would either weaken taxonomy specificity or weaken maturity assessment discipline. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`.
- **[inference]** CSDM reinforces that conclusion: this repository's prior work already treated operational data structure and capability abstraction as different concerns, so a taxonomy-plus-overlay pattern is more internally consistent than replacing everything with one framework. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.

### §4 Consistency Check

- **[fact]** No contradiction was found on the central point that AWS, Azure, Google, DORA, Team Topologies, and Wardley Mapping are overlays or lenses rather than complete enterprise capability taxonomies. Sources: `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`; `https://learnwardleymapping.com/`.
- **[fact]** There is tension between TOGAF's generality and DoDAF or NAF's richer traceability, but the tension is resolved by context: TOGAF is broader and more reusable across industries, while DoDAF and NAF are more specialised and heavier-weight. Sources: `https://www.opengroup.org/togaf`; `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`.
- **[fact]** IT-CMF capability counts vary in older public references, but the accessible IVI page currently states 37 Critical Capabilities; that official current value is used here. Source: `https://ivi.ie/it-capability-maturity-framework/`.
- **[fact]** TM Forum TAM and SABSA classifications carry lower confidence than other major findings because official public pages were partially inaccessible during direct fetch, so those conclusions rely on mixed official metadata and public supporting summaries. Sources: `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://sabsa.org/sabsa-executive-summary/`.

### §5 Depth and Breadth Expansion

- **[inference] Technical lens:** A durable enterprise capability map should separate at least four layers: domain and business capability, application-facing logical capability, shared technical or platform capability, and concrete implementation. That layered pattern matches both TOGAF-style abstraction and prior CSDM research on Business Application, Application Service, Technical Service, and Configuration Item separation. Sources: `https://www.opengroup.org/togaf`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`.
- **[inference] Governance lens:** Maturity scoring only works when capability boundaries stay stable over time, which means a capability taxonomy without a governed operational anchor such as CSDM or a Configuration Management Database (CMDB) will decay into opinion. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://ivi.ie/it-capability-maturity-framework/`.
- **[inference] Economic lens:** A layered combination is cheaper to maintain than a bespoke one-off taxonomy because it reuses a generic reference-model core, sector-specific overlays only where needed, and a separate maturity mechanism instead of forcing one framework to do incompatible jobs. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://bian.org/service-landscape/`; `https://teamtopologies.com/key-concepts`.
- **[inference] Historical lens:** The frameworks show a clear division of labour over time: older enterprise architecture models standardised structural categories, while newer engineering frameworks concentrated on performance, team interaction, and review loops. No surveyed modern framework fully collapsed those functions back into one model. Sources: `https://www.opengroup.org/togaf`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.
- **[inference] Behavioural lens:** Teams are more likely to adopt Team Topologies, DORA, and cloud review language than TOGAF category language, so a practical rollout should translate the reference-model backbone into platform and delivery vocabulary that engineering teams already recognise. Sources: `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.

### §6 Synthesis

**Executive summary:**

- **[inference]** No surveyed public framework provides, by itself, both a cross-industry, multi-level, implementation-agnostic technical capability taxonomy and a strong built-in maturity model, so the best-supported answer is a layered combination rather than a single-framework choice. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`.
- **[fact]** TOGAF is the closest cross-industry starting point because its reference-model family covers platform and application or data structure, but it remains a coarse reference model rather than a modern finished capability library or maturity framework. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`.
- **[fact]** IT-CMF explicitly supplies 37 Critical Capabilities, maturity profiles, assessment methods, and improvement roadmaps, while prior repository work shows that CSDM supplies the operational traceability layers needed to connect capability abstractions to Business Applications, Application Services, Technical Services, and Configuration Items. Sources: `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.
- **[inference]** Sector frameworks such as BIAN and Telecom Application Map (TAM), plus overlays such as SABSA, NIST CSF 2.0, ZTA, DORA, Team Topologies, and cloud well-architected frameworks, are best used as domain or quality overlays rather than as the enterprise-wide backbone. Sources: `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.

**Key findings:**

1. **[inference][high]** No surveyed public framework is simultaneously a modern enterprise-wide technical capability taxonomy and a robust maturity model, so organisations that need both outcomes must combine at least one classification framework with at least one maturity overlay. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`.
2. **[inference][medium]** TOGAF's Technical Reference Model and Integrated Information Infrastructure Reference Model are the best general-purpose public backbone in the set because they provide reusable cross-industry structural categories without binding the capability map to specific vendors or implementations. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`.
3. **[inference][high]** IT-CMF is the strongest enterprise-level maturity companion in the survey because IVI explicitly positions it as a 37-capability framework with maturity profiles, assessments, and improvement roadmaps that complement other domain-specific frameworks rather than replace them. Source: `https://ivi.ie/it-capability-maturity-framework/`.
4. **[fact][medium]** DoDAF, NAF, BIAN, and TM Forum TAM all provide meaningful multi-level decomposition or traceability, but each does so inside a bounded defence, banking, or telecom context rather than as a neutral enterprise technology stack. Sources: `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`.
5. **[fact][high]** SABSA, NIST CSF 2.0, and ZTA are valuable security overlays because they describe security attributes, outcomes, or logical security components, but they do not attempt to describe the full technical capability stack for the rest of enterprise IT. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`.
6. **[fact][high]** Team Topologies, DORA, Wardley Mapping, and the well-architected frameworks contribute team-design, performance, strategy, or review discipline rather than a canonical enterprise capability taxonomy, so they should challenge and improve the map instead of defining it. Sources: `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.
7. **[inference][high]** CSDM should be used as the operational representation layer for the capability map, with shared technical capabilities anchored first to Technical Services and then traced down to Configuration Items, because prior repository work shows that CSDM is strong on traceability but not on capability definition. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.
8. **[inference][high]** The most defensible rollout path is to stabilise CSDM ownership and service layers first, define a small implementation-agnostic enterprise capability backbone next, map Technical Services and Application Services onto it, and only then apply IT-CMF and targeted overlays for maturity and design review. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://ivi.ie/it-capability-maturity-framework/`.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| **[inference]** No single public framework covers both taxonomy and maturity well. | `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels` | high | Cross-framework comparison rather than a single-source statement. |
| **[inference]** TOGAF is the best generic backbone in the set. | `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm` | medium | Reference-model details are partly older public material. |
| **[inference]** IT-CMF is the strongest maturity companion. | `https://ivi.ie/it-capability-maturity-framework/` | high | Official IVI statement is explicit. |
| **[fact]** DoDAF, NAF, BIAN, and TAM are domain-bounded decompositions. | `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/` | medium | Stronger for DoDAF and BIAN than for TM Forum due access limits. |
| **[fact]** SABSA, NIST CSF 2.0, and ZTA are overlays or slices, not full-stack maps. | `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final` | high | Security-specific scope is explicit in the sources. |
| **[fact]** Team Topologies, DORA, Wardley Mapping, and well-architected frameworks are improvement or design lenses. | `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework` | high | Multiple independent sources agree on role. |
| **[inference]** CSDM should hold the map, not define the taxonomy. | `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md` | high | Strong repository-specific evidence. |
| **[inference]** A phased rollout should be CSDM-first, taxonomy-second, maturity-third. | `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://ivi.ie/it-capability-maturity-framework/` | high | Synthesises repository sequencing with maturity overlay evidence. |

**Assumptions:**

- **[assumption]** TM Forum TAM remains application-centric in the current public standard even though the official TAM detail page was inaccessible in this environment. **Justification:** accessible public explainers and official TM Forum references consistently describe eTOM as process architecture and TAM as the application architecture companion. Sources: `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://www.ntt-review.jp/archive/ntttechnical.php?contents=ntr202307gls_s.html`; `https://www.telecom-expertise.com/areas-of-expertise/`.
- **[assumption]** SABSA's current public executive-summary content still reflects the six-layer, business-attribute-driven structure described in accessible secondary sources. **Justification:** direct fetch of the official page returned 403, but public SABSA descriptions were consistent and aligned with long-standing SABSA structure. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://en.wikipedia.org/wiki/Sherwood_Applied_Business_Security_Architecture`; `https://davidlynas.com/sabsa/`.
- **[assumption]** A local enterprise capability map will need extension for modern platform areas such as internal developer platforms, event streaming, and artificial intelligence operations because the generic public frameworks do not normalise those areas consistently. **Justification:** the most general frameworks are reference models or overlays rather than contemporary exhaustive technical libraries. Sources: `https://www.opengroup.org/togaf`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

**Analysis:**

- **[inference]** The evidence points to a layered architecture because the frameworks answer different questions: TOGAF and sector models classify capability structure, IT-CMF and CMMI score maturity, CSDM provides traceability, and DORA or Team Topologies shape how capabilities are operated. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`.
- **[inference]** The main trade-off is breadth versus specificity: general frameworks are reusable but coarse, while sector frameworks are precise but hard to generalise beyond their native industries. Sources: `https://www.opengroup.org/togaf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`.
- **[inference]** The recommendation therefore favours composition over purity: use one backbone for stable capability names, one operational model for traceability, and targeted overlays for risk, design quality, or engineering performance. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://dora.dev/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

**Risks, gaps, uncertainties:**

- **[fact]** Official SABSA and TM Forum detail pages were partially inaccessible from this environment, so the conclusions on those frameworks rest on mixed official metadata and public supporting summaries rather than on fully fetched primary text. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`.
- **[inference]** TOGAF's public material is sufficient to justify its role as the generic backbone, but a production rollout would still need licensed or internal detail to define the exact level-2 and level-3 capability families. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/togaf-standard-10th-edition-downloads`.
- **[inference]** The recommendation does not eliminate local design work, because modern platform capabilities are not normalised consistently across the surveyed public frameworks. Sources: `https://www.opengroup.org/togaf`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

**Open questions:**

- Which concrete level-2 and level-3 capability families should be standardised first for this repository's likely enterprise context: identity, networking, integration, observability, or data?
- What is the cleanest way to attach IT-CMF maturity scoring to individual Technical Services in CSDM without creating duplicate governance structures?
- How much local extension is needed to represent platform engineering, internal developer platform, and artificial intelligence operations capabilities cleanly on top of a TOGAF-style backbone?

### §7 Recursive Review

- **[fact]** I rechecked Sections 2 through 6 and confirmed that each claim-bearing bullet is either sourced to a URL or explicitly marked as a fact, inference, or assumption. Source: this item's Research Skill Output Sections 2 through 6.
- **[fact]** I compared the Findings section against Section 6 and confirmed that the Findings restate the Section 6 synthesis rather than introducing new substantive claims. Source: this item's Section 6 Synthesis and Findings section.
- **[inference]** The remaining uncertainty is concentrated in framework accessibility and local extension depth, not in the core conclusion that a layered taxonomy-plus-maturity-plus-traceability stack is the best-supported answer. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`.

---

## Findings

*(Populated from Section 6 Synthesis above.)*

### Executive Summary

**[inference]** No single surveyed public framework can serve as both the enterprise-wide technical capability taxonomy and the maturity model, so the strongest answer is a layered stack that combines a generic taxonomy backbone, a maturity overlay, and an operational traceability model. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`.

**[inference]** The most defensible composition is a TOGAF-style backbone plus IT-CMF plus CSDM, because TOGAF contributes reusable implementation-agnostic structure, IT-CMF contributes maturity mechanics, and prior repository work shows that CSDM contributes the operational traceability layers needed to anchor the model in ServiceNow. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.

**[inference]** Sector, security, and engineering frameworks such as BIAN, TM Forum TAM, SABSA, NIST CSF 2.0, ZTA, DORA, Team Topologies, Wardley Mapping, and the cloud well-architected frameworks should improve or specialise the map rather than replace the enterprise-wide backbone. Sources: `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.

### Key Findings

1. **[inference][high]** No surveyed public framework is simultaneously a modern enterprise-wide technical capability taxonomy and a robust maturity model, so organisations that need both outcomes must combine at least one classification framework with at least one maturity overlay. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`.
2. **[inference][medium]** TOGAF's Technical Reference Model and Integrated Information Infrastructure Reference Model are the best general-purpose public backbone in the set because they provide reusable cross-industry structural categories without binding the capability map to specific vendors or implementations. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm`.
3. **[inference][high]** IT-CMF is the strongest enterprise-level maturity companion in the survey because IVI explicitly positions it as a 37-capability framework with maturity profiles, assessments, and improvement roadmaps that complement other domain-specific frameworks rather than replace them. Source: `https://ivi.ie/it-capability-maturity-framework/`.
4. **[fact][medium]** DoDAF, NAF, BIAN, and TM Forum TAM all provide meaningful multi-level decomposition or traceability, but each does so inside a bounded defence, banking, or telecom context rather than as a neutral enterprise technology stack. Sources: `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`.
5. **[fact][high]** SABSA, NIST CSF 2.0, and ZTA are valuable security overlays because they describe security attributes, outcomes, or logical security components, but they do not attempt to describe the full technical capability stack for the rest of enterprise IT. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final`.
6. **[fact][high]** Team Topologies, DORA, Wardley Mapping, and the well-architected frameworks contribute team-design, performance, strategy, or review discipline rather than a canonical enterprise capability taxonomy, so they should challenge and improve the map instead of defining it. Sources: `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework`.
7. **[inference][high]** CSDM should be used as the operational representation layer for the capability map, with shared technical capabilities anchored first to Technical Services and then traced down to Configuration Items, because prior repository work shows that CSDM is strong on traceability but not on capability definition. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`.
8. **[inference][high]** The most defensible rollout path is to stabilise CSDM ownership and service layers first, define a small implementation-agnostic enterprise capability backbone next, map Technical Services and Application Services onto it, and only then apply IT-CMF and targeted overlays for maturity and design review. Sources: `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://ivi.ie/it-capability-maturity-framework/`.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| **[inference]** No single public framework covers both taxonomy and maturity well. | `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels` | high | Cross-framework comparison rather than a single-source statement. |
| **[inference]** TOGAF is the best generic backbone in the set. | `https://www.opengroup.org/togaf`; `https://www.opengroup.org/architecture/0210can/togaf8/doc-review/togaf8cr/c/p3/iii-rm/concepts.htm` | medium | Reference-model details are partly older public material. |
| **[inference]** IT-CMF is the strongest maturity companion. | `https://ivi.ie/it-capability-maturity-framework/` | high | Official IVI statement is explicit. |
| **[fact]** DoDAF, NAF, BIAN, and TAM are domain-bounded decompositions. | `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`; `https://fachglossar.platinus.at/assets/files/NAFv4_2020.09-ed0964cf26fb5f5d0c23a54bc073b5ea.pdf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/` | medium | Stronger for DoDAF and BIAN than for TM Forum due access limits. |
| **[fact]** SABSA, NIST CSF 2.0, and ZTA are overlays or slices, not full-stack maps. | `https://sabsa.org/sabsa-executive-summary/`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://csrc.nist.gov/pubs/sp/800/207/final` | high | Security-specific scope is explicit in the sources. |
| **[fact]** Team Topologies, DORA, Wardley Mapping, and well-architected frameworks are improvement or design lenses. | `https://teamtopologies.com/key-concepts`; `https://dora.dev/`; `https://learnwardleymapping.com/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`; `https://learn.microsoft.com/en-us/azure/well-architected/`; `https://cloud.google.com/architecture/framework` | high | Multiple independent sources agree on role. |
| **[inference]** CSDM should hold the map, not define the taxonomy. | `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md` | high | Strong repository-specific evidence. |
| **[inference]** A phased rollout should be CSDM-first, taxonomy-second, maturity-third. | `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-platform-strategy.md`; `https://ivi.ie/it-capability-maturity-framework/` | high | Synthesises repository sequencing with maturity overlay evidence. |

### Assumptions

- **[assumption]** TM Forum TAM remains application-centric in the current public standard even though the official TAM detail page was inaccessible in this environment. **Justification:** accessible public explainers and official TM Forum references consistently describe eTOM as process architecture and TAM as the application architecture companion. Sources: `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://www.ntt-review.jp/archive/ntttechnical.php?contents=ntr202307gls_s.html`; `https://www.telecom-expertise.com/areas-of-expertise/`.
- **[assumption]** SABSA's current public executive-summary content still reflects the six-layer, business-attribute-driven structure described in accessible secondary sources. **Justification:** direct fetch of the official page returned 403, but public SABSA descriptions were consistent and aligned with long-standing SABSA structure. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://en.wikipedia.org/wiki/Sherwood_Applied_Business_Security_Architecture`; `https://davidlynas.com/sabsa/`.
- **[assumption]** A local enterprise capability map will need extension for modern platform areas such as internal developer platforms, event streaming, and artificial intelligence operations because the generic public frameworks do not normalise those areas consistently. **Justification:** the most general frameworks are reference models or overlays rather than contemporary exhaustive technical libraries. Sources: `https://www.opengroup.org/togaf`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

### Analysis

- **[inference]** The evidence points to a layered architecture because the frameworks answer different questions: TOGAF and sector models classify capability structure, IT-CMF and CMMI score maturity, CSDM provides traceability, and DORA or Team Topologies shape how capabilities are operated. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://cmmiinstitute.com/learning/appraisals/levels`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://dora.dev/`; `https://teamtopologies.com/key-concepts`.
- **[inference]** The main trade-off is breadth versus specificity: general frameworks are reusable but coarse, while sector frameworks are precise but hard to generalise beyond their native industries. Sources: `https://www.opengroup.org/togaf`; `https://bian.org/service-landscape/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`; `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf`.
- **[inference]** The recommendation therefore favours composition over purity: use one backbone for stable capability names, one operational model for traceability, and targeted overlays for risk, design quality, or engineering performance. Sources: `https://www.opengroup.org/togaf`; `https://ivi.ie/it-capability-maturity-framework/`; `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`; `https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final`; `https://dora.dev/`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

### Risks, Gaps, and Uncertainties

- **[fact]** Official SABSA and TM Forum detail pages were partially inaccessible from this environment, so the conclusions on those frameworks rest on mixed official metadata and public supporting summaries rather than on fully fetched primary text. Sources: `https://sabsa.org/sabsa-executive-summary/`; `https://www.tmforum.org/open-digital-architecture/process-framework-etom/`.
- **[inference]** TOGAF's public material is sufficient to justify its role as the generic backbone, but a production rollout would still need licensed or internal detail to define the exact level-2 and level-3 capability families. Sources: `https://www.opengroup.org/togaf`; `https://www.opengroup.org/togaf-standard-10th-edition-downloads`.
- **[inference]** The recommendation does not eliminate local design work, because modern platform capabilities are not normalised consistently across the surveyed public frameworks. Sources: `https://www.opengroup.org/togaf`; `https://teamtopologies.com/key-concepts`; `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`.

### Open Questions

- Which concrete level-2 and level-3 capability families should be standardised first for this repository's likely enterprise context: identity, networking, integration, observability, or data?
- What is the cleanest way to attach IT-CMF maturity scoring to individual Technical Services in CSDM without creating duplicate governance structures?
- How much local extension is needed to represent platform engineering, internal developer platform, and artificial intelligence operations capabilities cleanly on top of a TOGAF-style backbone?

---

## Output

- Type: knowledge
- Description: Comparative evaluation of cross-industry and domain-specific capability models, with a recommendation to use a TOGAF-style backbone plus IT-CMF maturity overlay plus CSDM traceability for multi-level IT capability mapping.
- Links:
  - `https://www.opengroup.org/togaf`
  - `https://ivi.ie/it-capability-maturity-framework/`
  - `https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`