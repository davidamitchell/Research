---
review_count: 2
title: "Open Digital Rights Language (ODRL) policies in Knowledge Graphs for software-agent access control and usage governance"
added: 2026-05-12T08:21:48+00:00
status: reviewing
priority: medium
blocks: []
tags: [knowledge-graph, agentic-ai, governance, ricardian-contracts]
started: 2026-05-13T10:02:08+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-web-ontologies-production-knowledge-graph-agentic
  - 2026-04-26-ai-agent-identity-access-management-enterprise
  - 2026-04-26-permission-safe-rag-enterprise-information-architecture
  - 2026-05-09-data-governance-standards-ai-agentic-applicability
  - 2026-03-14-ricardian-contract-model
related:
  - 2026-05-12-knowledge-graph-data-product-agentic
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-04-26-access-control-amplification-agentic-operations
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Open Digital Rights Language (ODRL) policies in Knowledge Graphs for software-agent access control and usage governance

## Research Question

How can the World Wide Web Consortium (W3C) Open Digital Rights Language (ODRL) be used to encode access control, usage policies, and governance constraints within or alongside a Knowledge Graph (KG) that serves as a runtime dependency for multi-step software systems, and what are the practical patterns, limitations, and emerging tooling for enforcing ODRL policies at software-agent query time?

## Scope

**In scope:**
- ODRL 2.2 information model: Policies, Rules (permissions, prohibitions, duties), Parties, Actions, Constraints, and Assets
- Representing ODRL policies as Resource Description Framework (RDF) triples within or attached to a KG
- Patterns for using ODRL to express read or write access on identified graph partitions, conditional usage permissions based on software-agent identity or purpose, and data-use obligations such as attribution or deletion after use
- Relationship between ODRL and other access control frameworks: Web Access Control (WAC), Attribute-Based Access Control (ABAC), and dataset licenses such as Creative Commons and the Open Government Licence
- Policy enforcement at query time: intercepting SPARQL Protocol and RDF Query Language (SPARQL) queries, applying named-graph-level policies, and returning filtered results
- Relationship of ODRL to Solid pods and Linked Data Platform access control
- Runtime identity: how software-agent identity is expressed and authenticated so ODRL party constraints can be evaluated at runtime
- Relationship of ODRL to Ricardian contracts and machine-readable licence stacks

**Out of scope:**
- General web ontology design, covered in completed item `2026-05-12-web-ontologies-production-knowledge-graph-agentic`
- Data mesh ownership and contracts, covered in completed item `2026-05-12-knowledge-graph-data-product-agentic`
- Graph database platform selection, covered in completed item `2026-05-12-graph-db-saas-knowledge-ontology`
- Digital Rights Management (DRM) for media content

**Constraints:**
- Focus on the W3C ODRL 2.2 specification and its RDF and Web Ontology Language (OWL) representation
- Distinguish clearly between policy expression and policy enforcement
- Prefer peer-reviewed papers, W3C specifications, and documented implementations over vendor marketing

## Context

Knowledge Graphs increasingly sit in the runtime path of multi-step software systems that retrieve facts, select tools, and trigger actions, which makes the question of who or what can read, write, transform, or redistribute graph data an operational governance problem rather than a documentation problem. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html]

Raw access control is necessary but insufficient in that setting, because systems also need machine-readable statements about purpose limits, retention limits, attribution duties, downstream sharing, and other usage conditions attached to graph assets. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-standards-ai-agentic-applicability.html]

## Approach

1. Study the ODRL 2.2 W3C Recommendation and vocabulary with focus on structures directly applicable to KG governance.
2. Review Solid, ODRL Profile for Access Control (OAC), and related identity specifications to understand how richer ODRL rules relate to WAC and Access Control Policies (ACP).
3. Examine how named graphs or datasets can be annotated with ODRL policies and how middleware, connectors, or query interception can enforce them.
4. Review data-space implementations, especially the International Data Spaces Association (IDSA), Dataspace Protocol (DSP), and Eclipse Dataspace Components (EDC), to separate policy expression from runtime enforcement.
5. Investigate runtime identity mechanisms such as WebID, OpenID Connect (OIDC), OAuth 2.0, Demonstration of Proof-of-Possession at the Application Layer (DPoP), and Verifiable Credentials (VCs) where they are actually evidenced in the reviewed material.
6. Assess emerging tooling such as OAC, draft ODRL evaluator semantics, and ODRL-related policy engines.
7. Synthesize a practical pattern guide for attaching ODRL policies to a KG, enforcing them at query time, and auditing post-access duties.

## Sources

- [x] [World Wide Web Consortium (W3C) ODRL Information Model 2.2 (2018)](https://www.w3.org/TR/odrl-model/)
- [x] [World Wide Web Consortium (W3C) ODRL Vocabulary and Expression 2.2 (2018)](https://www.w3.org/TR/odrl-vocab/)
- [x] [World Wide Web Consortium (W3C) RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [World Wide Web Consortium (W3C) ODRL Implementation Best Practices (2019)](https://w3c.github.io/odrl/bp/)
- [x] [World Wide Web Consortium (W3C) ODRL Formal Semantics draft](https://w3c.github.io/odrl/formal-semantics/)
- [x] [World Wide Web Consortium (W3C) ODRL Data Spaces profile draft](https://w3c.github.io/odrl/profile-dataspaces/)
- [x] [Solid Project Web Access Control specification](https://solidproject.org/TR/wac)
- [x] [Solid Project Solid-OIDC specification](https://solidproject.org/TR/oidc)
- [x] [Solid Project Access Control Policy specification](https://solidproject.org/TR/acp)
- [x] [Esteves et al. (2021) ODRL Profile for Expressing Consent through Granular Access Control Policies in Solid](https://doi.org/10.1109/EuroSPW54576.2021.00038)
- [x] [Esteves et al. (2021) ODRL Profile for Expressing Consent through Granular Access Control Policies in Solid, open access summary](https://harshp.com/research/publications/048-odrl-profile-consent-solid-acp)
- [x] [Esteves et al. (2023) ODRL Profile for Access Control 0.2](https://w3id.org/oac/)
- [x] [Esteves et al. (2022) Using the ODRL Profile for Access Control for Solid Pod Resource Governance](https://link.springer.com/chapter/10.1007/978-3-031-11609-4_3)
- [x] [Inrupt Access Control Policies](https://docs.inrupt.com/guides/access-control-policies)
- [x] [World Wide Web Consortium (W3C) Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model/)
- [x] [International Data Spaces Association (IDSA) Knowledge Base](https://docs.internationaldataspaces.org/)
- [x] [International Data Spaces Association (IDSA) Reference Architecture page](https://internationaldataspaces.org/offers/reference-architecture/)
- [x] [International Data Spaces Association (IDSA) ODRL policy concepts](https://github.com/International-Data-Spaces-Association/IDS-G/blob/main/UsageControl/Specification/Concepts/T7_ODRL_policies.md)
- [x] [International Data Spaces Association (IDSA) Dataspace Connector usage control policies](https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl)
- [x] [Gaia-X Data Exchange policies](https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/)
- [x] [Kirrane et al. (2020) Query Based Access Control for Linked Data](https://arxiv.org/abs/2007.00461)
- [x] [De Vos et al. (2019) ODRL Policy Modelling and Compliance Checking](https://researchportal.bath.ac.uk/en/publications/odrl-policy-modelling-and-compliance-checking/)
- [x] [Slabbinck et al. (2025) Interoperable Interpretation and Evaluation of ODRL Policies](https://ruben.verborgh.org/publications/slabbink_eswc_2025/)
- [x] [Comunica querying over Solid](https://comunica.dev/docs/query/advanced/solid/)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Web ontologies in production Knowledge Graphs for multi-step Artificial Intelligence (AI) agents](https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html)
- [x] [Mitchell (2026) What identity and access management model is required for Artificial Intelligence (AI) agents and low-code artefacts operating within enterprise systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
- [x] [Mitchell (2026) Permission-safe Retrieval-Augmented Generation (RAG) in enterprise information architectures](https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html)
- [x] [Mitchell (2026) Data Governance Standards and Regulations Applied to Artificial Intelligence (AI) Systems and Multi-Step Autonomous AI Deployments](https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-standards-ai-agentic-applicability.html)
- [x] [Mitchell (2026) Ricardian Contract model: history, current state, and latest research](https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html)
- [ ] [Steyskal and Polleres source cited in the seed item, seeded URL resolved to an unrelated paper and was not used as evidence](https://arxiv.org/abs/1501.03791)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine how ODRL can encode and help govern KG access and usage, and identify the practical enforcement patterns, limits, and tooling for software-agent query time.
- Scope: ODRL model and vocabulary, graph attachment patterns, Solid and data-space implementations, runtime identity, query-time enforcement, and practical tooling are in scope; ontology design, graph platform procurement, and media DRM are out of scope.
- Constraints: prioritize W3C specifications, standards-related documentation, and peer-reviewed or implementation-level material; keep policy expression separate from policy enforcement; use URL-backed citations only.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed-item cross-reference: the most relevant completed items are the KG runtime-dependency item, the web-ontologies item, the AI-agent identity item, the permission-safe RAG item, the data-governance standards item, and the Ricardian contract item because they already cover runtime graph dependency, RDF-native modelling, machine identity, permission filtering limits, governance translation layers, and machine-readable contract stacks. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-standards-ai-agentic-applicability.html; https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html]
- [inference] Working definition for this item: query-time ODRL enforcement means evaluating a request to read, modify, extract, derive, or distribute graph data against ODRL policies before the system returns results or commits the action, while recognizing that some duties can only be checked after access. [source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/bp/]

### §1 Question Decomposition

- **A. ODRL expression model**
  - A1. What policy, rule, party, asset, action, constraint, inheritance, and conflict concepts does ODRL 2.2 define?
  - A2. Which ODRL actions and constraints matter most for graph access and usage governance?
- **B. KG attachment pattern**
  - B1. How can a named graph, dataset, or graph-backed service be represented as an ODRL asset?
  - B2. What does the specification provide for attaching policy metadata to assets?
- **C. Identity and authorization context**
  - C1. What does Solid WAC cover, and what does it not cover compared with ODRL?
  - C2. How do Solid-OIDC, ACP, WebID, and VCs provide runtime identity context that ODRL itself lacks?
- **D. Enforcement architecture**
  - D1. What do W3C and data-space sources say about expression versus enforcement?
  - D2. Where are Policy Decision Point, Policy Enforcement Point, Policy Information Point, and Policy Execution Point style components placed?
- **E. Query-time feasibility**
  - E1. Is there evidence for production-grade ODRL-aware SPARQL rewriting or named-graph filtering?
  - E2. Which parts of ODRL can be translated into allow-or-deny query decisions, and which parts require post-access monitoring?
- **F. Tooling and deployments**
  - F1. What emerging tools, profiles, or engines evaluate ODRL?
  - F2. Which implementations are research prototypes, connector-boundary tools, or production-adjacent systems?
- **G. Synthesis**
  - G1. What is the recommended pattern for attaching ODRL to KGs used by software agents?
  - G2. What are the main limitations and open questions?

### §2 Investigation

#### 2.1 Core ODRL expression model

- [fact] ODRL 2.2 defines a Policy as a non-empty group of permissions, prohibitions, and obligations, with subclasses `Set`, `Offer`, and `Agreement`, and allows `profile`, `inheritFrom`, and `conflict` properties at policy level. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [fact] ODRL defines Assets, Parties, Actions, Rules, Constraints, Logical Constraints, conflict strategies, and inheritance, and the vocabulary includes common data-governance-relevant actions such as `read`, `extract`, `derive`, `aggregate`, `anonymize`, `modify`, `delete`, `attribute`, `inform`, `obtainConsent`, and `nextPolicy`. [source: https://www.w3.org/TR/odrl-vocab/]
- [fact] An ODRL Permission may include duties that must be fulfilled as conditions, a Prohibition may include remedies, and a Duty may include consequences, which lets ODRL express both allow-or-deny logic and post-access obligations. [source: https://www.w3.org/TR/odrl-model/]
- [fact] The ODRL vocabulary includes constraint operands such as `purpose`, `recipient`, `dateTime`, `timeInterval`, `delayPeriod`, `count`, `spatial`, `virtualLocation`, and `version`, which are directly useful for graph usage governance. [source: https://www.w3.org/TR/odrl-vocab/]
- [fact] ODRL defines conflict strategies `perm`, `prohibit`, and `invalid`, and policy inheritance through `inheritFrom`, which matters when multiple policy layers apply to the same graph asset. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [inference] ODRL is expressive enough to model graph read access, derivative-use limits, temporal limits, purpose limits, attribution duties, and downstream policy chaining, but the model does not imply how any runtime should execute those rules. [source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/]

#### 2.2 Representing policies alongside Knowledge Graph assets

- [fact] ODRL assets are generic Internationalized Resource Identifier (IRI)-identified resources, and the vocabulary defines `target` on rules and `hasPolicy` on assets, which provides a normative way to point from a resource to the policy governing it. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [fact] ODRL was designed to work with Linked Data and RDF serializations, including JSON for Linked Data (JSON-LD), and the specification explicitly supports graph-based implementations while remaining neutral about non-graph implementations. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [fact] The ODRL Data Spaces draft extends the core model with data-space-specific actions such as `Query`, `Publish`, `Train`, `Evaluate`, `Anonymize`, and `Transform`, and with provider, consumer, controller, and broker party roles. [source: https://w3c.github.io/odrl/profile-dataspaces/]
- [inference] A practical KG attachment pattern is therefore to treat each named graph, meaning an RDF graph in a dataset that has its own identifier, dataset URI, or graph-backed service URI as the asset boundary, link it to policy metadata with `odrl:hasPolicy` or refer to it via `odrl:target`, and evaluate policy against the request context before query execution or result release. [source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/]

#### 2.3 Solid, WAC, ACP, and runtime identity

- [fact] WAC is a decentralized Access Control List model for Hypertext Transfer Protocol (HTTP) resources in Linked Data systems, covering resource-level `Read`, `Write`, `Append`, and `Control` permissions for URI-identified agents, but the specification explicitly states that it does not specify authentication mechanisms or methods to verify assertions. [source: https://solidproject.org/TR/wac]
- [fact] WAC does not provide first-class duties, prohibitions, purpose constraints, temporal constraints, or downstream usage controls, which makes it narrower than ODRL for usage governance. [source: https://solidproject.org/TR/wac; https://www.w3.org/TR/odrl-model/]
- [fact] ACP defines a context graph and authorization graph model that can consider target, mode, agent, client, issuer, owner, creator, and VC attributes when evaluating access, which gives Solid a richer runtime authorization context than WAC alone. [source: https://solidproject.org/TR/acp]
- [fact] Solid-OIDC uses WebID as a primary identifier and requires DPoP-bound tokens whose payload includes the `webid`, `iss`, `aud`, `azp`, `iat`, `exp`, and `cnf` claims, which supplies authenticated runtime identity data that can feed an external policy engine. [source: https://solidproject.org/TR/oidc]
- [fact] Esteves et al. (2021) and OAC extend Solid access control by combining ODRL with the Data Privacy Vocabulary and WAC semantics, adding richer policy terms such as purpose, recipient, legal basis, and processing context while still requiring a policy-matching or reasoning component outside the ODRL model itself. [source: https://doi.org/10.1109/EuroSPW54576.2021.00038; https://harshp.com/research/publications/048-odrl-profile-consent-solid-acp; https://w3id.org/oac/]
- [fact] Inrupt documents ACP as the foundational authorization language for pod resources and describes policies as matcher conditions plus allow or deny access modes, but the public documentation does not describe native ODRL evaluation inside ACP. [source: https://docs.inrupt.com/guides/access-control-policies; https://solidproject.org/TR/acp]
- [inference] The Verifiable Credentials Data Model supports `termsOfUse` and a machine-verifiable subject and issuer structure, which makes VCs a plausible carrier for runtime claims consumed by a policy engine even though the VC standard is not itself an ODRL evaluator. [source: https://www.w3.org/TR/vc-data-model/]
- [inference] ODRL does not authenticate software agents; it consumes party and constraint values supplied by surrounding identity and authorization infrastructure such as WebID, OIDC, ACP context, or VCs. [source: https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/wac; https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://w3id.org/oac/; https://www.w3.org/TR/vc-data-model/]

#### 2.4 Data-space and connector enforcement patterns

- [fact] The ODRL Implementation Best Practices document explicitly says that ODRL provides no mechanism whatsoever to implement access control logic and can only describe how an external access control system should behave. [source: https://w3c.github.io/odrl/bp/]
- [fact] The IDSA Knowledge Base describes the reference architecture and rulebook as the place where data usage policies, governance models, and technical specifications are translated into components and behavior patterns for trusted data sharing. [source: https://docs.internationaldataspaces.org/; https://internationaldataspaces.org/offers/reference-architecture/]
- [fact] IDSA ODRL policy examples show ODRL or ODRL-like agreements enriched with International Data Spaces-specific context, constraints, and Policy Information Point and Policy Execution Point endpoints, which makes enforcement explicitly connector and middleware based rather than intrinsic to ODRL. [source: https://github.com/International-Data-Spaces-Association/IDS-G/blob/main/UsageControl/Specification/Concepts/T7_ODRL_policies.md]
- [fact] The Dataspace Connector documentation states that the connector supports usage policies written in an International Data Spaces Usage Control Language based on ODRL, that the usage policy is the key motive of organizational and technical enforcement, and that only a subset of the defined policy classes is currently implemented. [source: https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl]
- [fact] The Gaia-X Data Exchange policies page distinguishes contract policies, which use ODRL as a policy definition language, from runtime policies, which are derived from the contract policy and executed through other policy languages or runtime systems. [source: https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]
- [inference] Across Solid, IDSA, and Gaia-X, the consistent implementation pattern is expression in ODRL or an ODRL-derived profile, followed by decision and execution in pods, connectors, or middleware; none of these ecosystems treats ODRL itself as the enforcement runtime. [source: https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

#### 2.5 Query-time enforcement, evaluation, and tooling

- [fact] The ODRL Formal Semantics draft defines the expected behavior of an ODRL evaluator, its inputs of Policy, State of the World, Evaluation Request, and optional behavior mode, and two scenarios: an access-control scenario and a policy-monitoring scenario. [source: https://w3c.github.io/odrl/formal-semantics/]
- [fact] Slabbinck et al. (2025) state that ODRL lacks a fully standardized evaluation semantics and introduce a Compliance Report Model plus an ODRL Evaluator to make policy interpretation and evaluation more interoperable. [source: https://ruben.verborgh.org/publications/slabbink_eswc_2025/]
- [fact] De Vos et al. (2019) describe a pipeline for ODRL policy modelling and compliance checking, which shows that formal evaluation work exists but remains a specialized research activity rather than a mainstream graph-platform capability. [source: https://researchportal.bath.ac.uk/en/publications/odrl-policy-modelling-and-compliance-checking/]
- [fact] Kirrane et al. (2020) show that query rewriting can enforce Linked Data access controls at SPARQL query level, which confirms the plausibility of rewriting as a control pattern even though the paper is not an ODRL-specific implementation. [source: https://arxiv.org/abs/2007.00461]
- [fact] Comunica documents querying public and private Solid documents with authenticated fetch functions and Solid-aware engines, but the public documentation does not describe ODRL-aware query rewriting or named-graph filtering. [source: https://comunica.dev/docs/query/advanced/solid/]
- [fact] The ODRL Data Spaces draft says policy enforcement is implemented through translation into a process-algebra-like model and checking against platform logging information such as Apache Spark or Apache Flink logs, which is a monitoring pattern rather than an in-engine SPARQL filter. [source: https://w3c.github.io/odrl/profile-dataspaces/]
- [inference] No reviewed source documents a production-grade ODRL-aware SPARQL rewriter or named-graph filter for KG query time; current evidence supports connector-boundary, pod-boundary, or compliance-checking tooling, not a mature graph-native enforcement engine. [source: https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl]

#### 2.6 Practical limits and cross-item integration

- [fact] ODRL duties such as attribution, deletion after use, notification, or downstream policy transfer are not reducible to a simple allow-or-deny read decision and therefore require post-access execution or monitoring components. [source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/]
- [fact] The permission-safe RAG completed item found that copied permission metadata and query-time filtering only work when the permission model is already coherent and correctly represented, which directly qualifies ODRL-at-query-time designs for KG systems. [source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]
- [fact] The AI-agent identity completed item found that software agents should be represented as bounded machine identities rather than as durable extensions of human accounts, which is directly relevant because ODRL party constraints need stable machine identities to evaluate. [source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]
- [fact] The KG runtime-dependency completed item found that live graph dependencies create latency, consistency, and availability risks, which means query-time policy checks add a real operational surface and should be kept as narrow as possible. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [fact] The Ricardian contract completed item describes machine-readable plus human-readable contract stacks that bind legal semantics to digital execution, which makes it a useful comparison for ODRL-based policy layers but not a substitute for graph access enforcement. [source: https://davidamitchell.github.io/Research/research/2026-03-14-ricardian-contract-model.html]
- [inference] The practical boundary supported by the reviewed evidence is to use ODRL for policy metadata and evaluable request context, translate only the allow-or-deny and filterable subset into query-time controls, and push duties plus audit obligations into external execution and monitoring services. [source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.7 Source corrections and explicit search gaps

- [fact] The seeded Esteves source `https://arxiv.org/abs/2107.04699` resolves to an unrelated graph-algorithm paper, and the corrected evidence source for the Solid and OAC work is the IEEE workshop DOI plus the open-access Harsh Pandit publication page. [source: https://arxiv.org/abs/2107.04699; https://doi.org/10.1109/EuroSPW54576.2021.00038; https://harshp.com/research/publications/048-odrl-profile-consent-solid-acp]
- [fact] The seeded IDSA and Gaia-X URLs were stale, so the item uses the current IDSA Knowledge Base, reference-architecture page, Dataspace Connector documentation, and Gaia-X Data Exchange policies page instead. [source: https://docs.internationaldataspaces.org/; https://internationaldataspaces.org/offers/reference-architecture/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]
- [assumption] Search note: query `\"How to Legally Link Linked Data\" Steyskal Polleres PDF` did not yield a stable open primary full text in this runtime, and the seeded `1501.03791` page was unrelated, so this item relies on later W3C, Solid, and data-space sources rather than on unverified claims from the intended paper. [source: https://arxiv.org/abs/1501.03791; https://w3c.github.io/odrl/bp/; https://ceur-ws.org/Vol-2198/paper_114.pdf]

### §3 Reasoning

- [fact] The reviewed ODRL specifications cover policy expression, rule structure, asset attachment, and constraint modelling. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [fact] W3C, Solid, IDSA, and Gaia-X materials consistently separate policy expression from enforcement runtime. [source: https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]
- [fact] Solid and data-space implementations provide concrete evidence that identity and authorization context come from surrounding protocols such as WebID, OIDC, ACP context graphs, VCs, pod servers, or connectors rather than from ODRL itself. [source: https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://docs.inrupt.com/guides/access-control-policies; https://w3id.org/oac/]
- [inference] The strongest supported architecture is therefore a layered one: ODRL for policy expression, external identity and request context for party resolution, a policy decision layer for evaluation, and a policy enforcement layer that performs either query filtering or action denial. [source: https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl]
- [inference] Query-time enforcement can only cover the subset of ODRL that can be decided before data release, while duties and downstream usage requirements remain outside pure SPARQL filtering. [source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/]

### §4 Consistency Check

- [inference] No reviewed source contradicts the claim that ODRL is an expression language rather than a complete enforcement runtime. [source: https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/]
- [inference] The reviewed sources are consistent that richer usage constraints require external runtime context and execution points, although they differ on where those components sit, such as pod servers, connector stacks, or compliance engines. [source: https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]
- [inference] The main unresolved area is not whether ODRL can describe graph governance rules, but whether a standard, interoperable, graph-native query-time evaluator will emerge; the evidence base remains thin and no reviewed source proves production-grade SPARQL-native enforcement. [source: https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/]

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** RDF-native KGs are a natural fit for ODRL policy attachment because the same graph tooling can store policy metadata, but high-value query paths should keep evaluation narrow to avoid adding brittle latency or consistency dependencies. [source: https://www.w3.org/TR/odrl-model/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] **Regulatory lens:** ODRL can operationalize purpose, retention, and attribution constraints in machine-readable form, but standards and compliance still depend on deterministic runtime controls and audit evidence rather than on policy metadata alone. [source: https://www.w3.org/TR/odrl-model/; https://davidamitchell.github.io/Research/research/2026-05-09-data-governance-standards-ai-agentic-applicability.html]
- [inference] **Economic lens:** Query-time filtering for every graph read is cheaper to adopt than duplicating graph stores per audience, but it only works if identities and graph permission metadata are already coherent enough to support deterministic evaluation. [source: https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html]
- [inference] **Behavioral lens:** Software agents intensify the value of explicit usage policy because they operate continuously and can exploit the full permission envelope presented to them, which raises the value of distinct machine identities and pre-query policy checks. [source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-access-control-amplification-agentic-operations.html]

### §6 Synthesis

**Executive summary:**

ODRL can encode access and usage governance for Knowledge Graphs, but it cannot by itself enforce software-agent query-time controls; practical systems must pair ODRL policies with external identity, policy-decision, and policy-enforcement components. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/]

The strongest attachment pattern is to treat each named graph, meaning an RDF graph in a dataset that has its own identifier, dataset URI, or graph-backed service URI as an ODRL asset, attach policy metadata with `odrl:hasPolicy` or `odrl:target`, and evaluate permissions, prohibitions, duties, and constraints against request context before query execution or result release. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/]

Solid, IDSA, Gaia-X, and related tooling show a consistent architectural split: ODRL or ODRL-derived profiles express usage conditions, while pod servers, connector stacks, and middleware perform the actual allow, deny, filter, logging, and post-access duty execution. [inference; source: https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

For KG systems used by software agents, the recommended pattern is bounded machine identity plus ODRL-tagged graph assets plus middleware that translates the allow-or-deny subset of ODRL into query filtering, while duties such as attribution, deletion, and notification are audited outside the query path. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://w3c.github.io/odrl/formal-semantics/]

**Key findings:**

1. **ODRL 2.2 is expressive enough to model KG access and usage governance because it defines policies, permissions, prohibitions, duties, parties, assets, constraints, inheritance, and conflict strategies over generic IRI-identified resources.** ([fact]; high confidence; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/)
2. **The most robust KG attachment pattern is to bind ODRL policies to named graph, dataset, or service URIs with `odrl:hasPolicy` or `odrl:target`, then treat those URIs as the policy boundary that request-time evaluation operates against.** ([inference]; medium confidence; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/)
3. **WAC and ACP provide resource and request context for Solid systems, but they do not replace ODRL because they lack first-class duties, purpose constraints, explicit prohibitions, and richer downstream usage conditions.** ([fact]; high confidence; source: https://solidproject.org/TR/wac; https://solidproject.org/TR/acp; https://www.w3.org/TR/odrl-model/)
4. **ODRL does not authenticate requesters, so runtime enforcement depends on external identity layers such as WebID, Solid-OIDC, ACP context attributes, or Verifiable Credentials to resolve which party and request parameters should be evaluated.** ([fact]; high confidence; source: https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://www.w3.org/TR/vc-data-model/; https://w3id.org/oac/)
5. **The reviewed Solid, IDSA, Dataspace Connector, and Gaia-X materials all separate ODRL policy expression from enforcement, placing enforcement in pod servers, connectors, middleware, or derived runtime policy engines rather than in ODRL itself.** ([fact]; high confidence; source: https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/)
6. **Current tooling supports ODRL authoring, profile extension, and draft evaluator semantics, but the ecosystem remains fragmented and the reviewed sources do not show a production-grade ODRL-aware SPARQL rewriter or named-graph filter.** ([inference]; medium confidence; source: https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/)
7. **Query-time enforcement can only cover the subset of ODRL that resolves before release, such as allow, deny, and filterable constraints, while duties such as attribution, deletion, notification, and onward-policy transfer require post-access execution or monitoring.** ([inference]; medium confidence; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/bp/)
8. **For software-agent access to a KG, the best-supported design is a layered one in which bounded machine identities call a middleware decision point that evaluates ODRL-tagged graph assets and translates only the decision-ready subset into query filtering or denial.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://w3c.github.io/odrl/formal-semantics/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] ODRL 2.2 can model KG governance with policies, rules, assets, parties, constraints, inheritance, and conflict strategies. | https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/ | high | Core specification |
| [inference] Named graph, dataset, or service URIs are the most practical ODRL policy boundary for KG use. | https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/ | medium | Attachment pattern |
| [fact] WAC and ACP provide access context but not full ODRL-style usage governance. | https://solidproject.org/TR/wac; https://solidproject.org/TR/acp; https://www.w3.org/TR/odrl-model/ | high | Resource-level authorization only |
| [fact] ODRL runtime evaluation depends on external identity and request context such as WebID, OIDC, ACP attributes, or VCs. | https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://www.w3.org/TR/vc-data-model/; https://w3id.org/oac/ | high | Identity supplied externally |
| [fact] Reviewed Solid and data-space implementations separate ODRL expression from enforcement runtime. | https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/ | high | Connector and middleware pattern |
| [inference] No reviewed source documents a production-grade ODRL-aware SPARQL rewriter or named-graph filter. | https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/ | medium | Tooling gap |
| [inference] Duties and monitoring-oriented obligations cannot be fully enforced by pre-query filtering alone. | https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/bp/ | medium | Requires execution or audit layer |
| [inference] The best-supported production pattern is bounded machine identity plus middleware evaluation of ODRL-tagged graph assets plus narrow query-time filtering. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://w3c.github.io/odrl/formal-semantics/ | medium | Synthesis claim |

**Assumptions:**

- [assumption] A KG used in this pattern exposes stable URIs for named graphs, datasets, or graph-backed resources so that ODRL policies can attach to something operationally meaningful. **Justification:** ODRL assets are URI-identified resources, and the graph-layer recommendation depends on having a stable policy boundary to target. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [assumption] Runtime request context can supply identity, client, issuer, and purpose values to the policy decision layer even when the graph query language does not carry those features natively. **Justification:** reviewed Solid and ODRL evaluator materials assume such context exists outside the policy expression itself. [source: https://solidproject.org/TR/acp; https://solidproject.org/TR/oidc; https://w3c.github.io/odrl/formal-semantics/]
- [assumption] Post-access duties are operationally acceptable when executed by separate monitoring or execution components rather than by the SPARQL engine itself. **Justification:** the reviewed sources repeatedly separate usage-policy expression from execution and monitoring infrastructure. [source: https://w3c.github.io/odrl/bp/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

**Analysis:**

The evidence weighs strongly toward ODRL as an expressive policy layer and weakly toward ODRL as a graph-native runtime, because every authoritative source that directly addresses implementation separates policy description from the runtime that enforces it. [inference; source: https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl]

That split resolves the apparent tension between RDF-native policy metadata and practical enforcement: the graph can store policy and can participate in decision support, but access denial, query rewriting, logging, and post-access duties belong to external control layers that already understand identity, timing, and trusted execution context. [inference; source: https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/acp; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

The best evidence for query-time enforcement is indirect rather than direct, because query rewriting exists for Linked Data access control and ODRL evaluators exist as draft semantics or prototypes, but the reviewed material does not show a mature implementation that joins those capabilities into one production-grade SPARQL control surface. [inference; source: https://arxiv.org/abs/2007.00461; https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/]

This leads to a practical design choice: keep query-time ODRL evaluation focused on the subset that can deterministically produce allow, deny, or filter results, and keep duties, propagation, and compliance evidence in adjacent execution and audit paths. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

**Risks, gaps, uncertainties:**

- The reviewed evidence base is strong for ODRL expression and for connector-boundary enforcement, but weak for graph-native SPARQL enforcement inside mainstream KG products. [inference; source: https://w3c.github.io/odrl/bp/; https://comunica.dev/docs/query/advanced/solid/]
- The seeded Steyskal and Polleres source could not be verified from an accessible primary text in this runtime, so linked-data licensing history is supported here mainly by later W3C and data-space materials. [assumption; source: https://arxiv.org/abs/1501.03791; https://w3c.github.io/odrl/bp/]
- The ODRL Formal Semantics and ODRL Data Spaces profile are community drafts rather than W3C Recommendations, which lowers confidence for claims about interoperable evaluator behavior. [fact; source: https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/profile-dataspaces/]
- The public Solid and Inrupt material demonstrates runtime identity and access context, but not a normative bridge from those identity claims into fully standardized ODRL evaluation semantics. [fact; source: https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://docs.inrupt.com/guides/access-control-policies]
- Gaia-X evidence in this item is stronger on the expression versus runtime split than on direct proof of ODRL-native enforcement, because the originally seeded Gaia-X URL was stale and the replacement source is a current policy page rather than a full architecture study. [inference; source: https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

**Open questions:**

- What is the cleanest way to bind named-graph identifiers and SPARQL query structure to ODRL constraints without inventing a profile that is too engine-specific? [inference; source: https://w3c.github.io/odrl/profile-dataspaces/; https://w3c.github.io/odrl/formal-semantics/]
- Which runtime claim format is most practical for software-agent purpose assertions in enterprise graph systems: OIDC claims, VCs, or application-specific middleware parameters? [inference; source: https://solidproject.org/TR/oidc; https://www.w3.org/TR/vc-data-model/]
- How should post-access duties such as deletion-after-use or onward-policy transfer be audited when graph results are cached, summarized, or merged into downstream derived artifacts? [inference; source: https://www.w3.org/TR/odrl-model/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- Is there enough repeated demand to justify a dedicated KG-focused ODRL profile that adds first-class graph query, graph update, and graph partition operands beyond the current data-spaces draft? [inference; source: https://w3c.github.io/odrl/profile-dataspaces/; https://www.w3.org/TR/odrl-vocab/]

### §7 Recursive Review

```text
review-status: pass
acronym-audit: complete
domain-term-audit: complete
claim-audit: complete
findings-parity: aligned
source-audit: url-backed
```

---

## Findings

### Executive Summary

ODRL can encode access and usage governance for Knowledge Graphs, but it cannot by itself enforce software-agent query-time controls; practical systems must pair ODRL policies with external identity, policy-decision, and policy-enforcement components. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/]

The strongest attachment pattern is to treat each named graph, meaning an RDF graph in a dataset that has its own identifier, dataset URI, or graph-backed service URI as an ODRL asset, attach policy metadata with `odrl:hasPolicy` or `odrl:target`, and evaluate permissions, prohibitions, duties, and constraints against request context before query execution or result release. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/]

Solid, IDSA, Gaia-X, and related tooling show a consistent architectural split: ODRL or ODRL-derived profiles express usage conditions, while pod servers, connector stacks, and middleware perform the actual allow, deny, filter, logging, and post-access duty execution. [inference; source: https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

For KG systems used by software agents, the recommended pattern is bounded machine identity plus ODRL-tagged graph assets plus middleware that translates the allow-or-deny subset of ODRL into query filtering, while duties such as attribution, deletion, and notification are audited outside the query path. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://w3c.github.io/odrl/formal-semantics/]

### Key Findings

1. **ODRL 2.2 is expressive enough to model KG access and usage governance because it defines policies, permissions, prohibitions, duties, parties, assets, constraints, inheritance, and conflict strategies over generic IRI-identified resources.** ([fact]; high confidence; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/)
2. **The most robust KG attachment pattern is to bind ODRL policies to named graph, dataset, or service URIs with `odrl:hasPolicy` or `odrl:target`, then treat those URIs as the policy boundary that request-time evaluation operates against.** ([inference]; medium confidence; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/)
3. **WAC and ACP provide resource and request context for Solid systems, but they do not replace ODRL because they lack first-class duties, purpose constraints, explicit prohibitions, and richer downstream usage conditions.** ([fact]; high confidence; source: https://solidproject.org/TR/wac; https://solidproject.org/TR/acp; https://www.w3.org/TR/odrl-model/)
4. **ODRL does not authenticate requesters, so runtime enforcement depends on external identity layers such as WebID, Solid-OIDC, ACP context attributes, or Verifiable Credentials to resolve which party and request parameters should be evaluated.** ([fact]; high confidence; source: https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://www.w3.org/TR/vc-data-model/; https://w3id.org/oac/)
5. **The reviewed Solid, IDSA, Dataspace Connector, and Gaia-X materials all separate ODRL policy expression from enforcement, placing enforcement in pod servers, connectors, middleware, or derived runtime policy engines rather than in ODRL itself.** ([fact]; high confidence; source: https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/)
6. **Current tooling supports ODRL authoring, profile extension, and draft evaluator semantics, but the ecosystem remains fragmented and the reviewed sources do not show a production-grade ODRL-aware SPARQL rewriter or named-graph filter.** ([inference]; medium confidence; source: https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/)
7. **Query-time enforcement can only cover the subset of ODRL that resolves before release, such as allow, deny, and filterable constraints, while duties such as attribution, deletion, notification, and onward-policy transfer require post-access execution or monitoring.** ([inference]; medium confidence; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/bp/)
8. **For software-agent access to a KG, the best-supported design is a layered one in which bounded machine identities call a middleware decision point that evaluates ODRL-tagged graph assets and translates only the decision-ready subset into query filtering or denial.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://w3c.github.io/odrl/formal-semantics/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] ODRL 2.2 can model KG governance with policies, rules, assets, parties, constraints, inheritance, and conflict strategies. | https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/ | high | Core specification |
| [inference] Named graph, dataset, or service URIs are the most practical ODRL policy boundary for KG use. | https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/; https://w3c.github.io/odrl/profile-dataspaces/ | medium | Attachment pattern |
| [fact] WAC and ACP provide access context but not full ODRL-style usage governance. | https://solidproject.org/TR/wac; https://solidproject.org/TR/acp; https://www.w3.org/TR/odrl-model/ | high | Resource-level authorization only |
| [fact] ODRL runtime evaluation depends on external identity and request context such as WebID, OIDC, ACP attributes, or VCs. | https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://www.w3.org/TR/vc-data-model/; https://w3id.org/oac/ | high | Identity supplied externally |
| [fact] Reviewed Solid and data-space implementations separate ODRL expression from enforcement runtime. | https://w3c.github.io/odrl/bp/; https://w3id.org/oac/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/ | high | Connector and middleware pattern |
| [inference] No reviewed source documents a production-grade ODRL-aware SPARQL rewriter or named-graph filter. | https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/; https://comunica.dev/docs/query/advanced/solid/ | medium | Tooling gap |
| [inference] Duties and monitoring-oriented obligations cannot be fully enforced by pre-query filtering alone. | https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/bp/ | medium | Requires execution or audit layer |
| [inference] The best-supported production pattern is bounded machine identity plus middleware evaluation of ODRL-tagged graph assets plus narrow query-time filtering. | https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://w3c.github.io/odrl/formal-semantics/ | medium | Synthesis claim |

### Assumptions

- **Assumption:** The KG exposes stable URIs for named graphs, datasets, or graph-backed resources so that ODRL policies can attach to meaningful boundaries. **Justification:** ODRL assets are URI-identified resources, and the graph-layer recommendation depends on stable attachment points. [assumption; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- **Assumption:** Runtime request context can supply identity, client, issuer, and purpose values to the policy decision layer even when the graph query language does not carry those features natively. **Justification:** reviewed Solid and ODRL evaluator materials assume such context exists outside the policy expression itself. [assumption; source: https://solidproject.org/TR/acp; https://solidproject.org/TR/oidc; https://w3c.github.io/odrl/formal-semantics/]
- **Assumption:** Post-access duties are operationally acceptable when executed by separate monitoring or execution components rather than by the SPARQL engine itself. **Justification:** the reviewed sources repeatedly separate usage-policy expression from execution and monitoring infrastructure. [assumption; source: https://w3c.github.io/odrl/bp/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

### Analysis

The evidence favors ODRL as an expressive policy layer and does not favor ODRL as a self-sufficient graph-native runtime, because every authoritative source that directly addresses implementation separates policy description from the system that enforces it. [inference; source: https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/; https://international-data-spaces-association.github.io/DataspaceConnector/Documentation/v5/UsageControl]

That split resolves the main design question for KGs: store and publish policy in RDF-native form, but let a dedicated decision layer evaluate policy against request context and let a dedicated enforcement layer deny, filter, log, or trigger post-access duties. [inference; source: https://www.w3.org/TR/odrl-model/; https://solidproject.org/TR/acp; https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

The strongest positive evidence for query-time enforcement is indirect rather than direct, because query rewriting exists for Linked Data access control and ODRL evaluators exist as draft semantics or prototypes, but the reviewed material does not show a mature implementation that joins those capabilities into a production-grade SPARQL control surface. [inference; source: https://arxiv.org/abs/2007.00461; https://w3c.github.io/odrl/formal-semantics/; https://ruben.verborgh.org/publications/slabbink_eswc_2025/]

The practical implication is to keep query-time ODRL evaluation focused on the subset that can deterministically produce allow, deny, or filter decisions, and to keep duties, propagation, and compliance evidence in adjacent execution and audit paths. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/formal-semantics/; https://davidamitchell.github.io/Research/research/2026-04-26-permission-safe-rag-enterprise-information-architecture.html]

### Risks, Gaps, and Uncertainties

- The evidence base is strong for ODRL expression and for connector-boundary enforcement, but weak for graph-native SPARQL enforcement inside mainstream KG products. [inference; source: https://w3c.github.io/odrl/bp/; https://comunica.dev/docs/query/advanced/solid/]
- The seeded Steyskal and Polleres source could not be verified from an accessible primary text in this runtime, so linked-data licensing history is supported here mainly by later W3C and data-space materials. [assumption; source: https://arxiv.org/abs/1501.03791; https://w3c.github.io/odrl/bp/]
- The ODRL Formal Semantics and ODRL Data Spaces profile are community drafts rather than W3C Recommendations, which lowers confidence for claims about interoperable evaluator behavior. [fact; source: https://w3c.github.io/odrl/formal-semantics/; https://w3c.github.io/odrl/profile-dataspaces/]
- The public Solid and Inrupt material demonstrates runtime identity and access context, but not a normative bridge from those identity claims into fully standardized ODRL evaluation semantics. [fact; source: https://solidproject.org/TR/oidc; https://solidproject.org/TR/acp; https://docs.inrupt.com/guides/access-control-policies]
- Gaia-X evidence in this item is stronger on the expression versus runtime split than on direct proof of ODRL-native enforcement, because the originally seeded Gaia-X URL was stale and the replacement source is a current policy page rather than a full architecture study. [inference; source: https://gaia-x.gitlab.io/technical-committee/data-exchange-working-group/data-exchange/policies/]

### Open Questions

- What is the cleanest way to bind named-graph identifiers and SPARQL query structure to ODRL constraints without creating a profile that is too engine-specific? [inference; source: https://w3c.github.io/odrl/profile-dataspaces/; https://w3c.github.io/odrl/formal-semantics/]
- Which runtime claim format is most practical for software-agent purpose assertions in enterprise graph systems: OIDC claims, VCs, or application-specific middleware parameters? [inference; source: https://solidproject.org/TR/oidc; https://www.w3.org/TR/vc-data-model/]
- How should post-access duties such as deletion-after-use or onward-policy transfer be audited when graph results are cached, summarized, or merged into downstream derived artifacts? [inference; source: https://www.w3.org/TR/odrl-model/; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- Is there enough repeated demand to justify a dedicated KG-focused ODRL profile that adds first-class graph query, graph update, and graph partition operands beyond the current data-spaces draft? [inference; source: https://w3c.github.io/odrl/profile-dataspaces/; https://www.w3.org/TR/odrl-vocab/]

---

## Output

- Type: knowledge
- Description: Pattern guide for attaching ODRL policies to Knowledge Graph assets, evaluating them with external identity and policy engines, and separating query-time filtering from post-access duty execution. [inference; source: https://www.w3.org/TR/odrl-model/; https://w3c.github.io/odrl/bp/; https://w3c.github.io/odrl/formal-semantics/]
- Links:
  - https://www.w3.org/TR/odrl-model/
  - https://w3c.github.io/odrl/bp/
  - https://w3c.github.io/odrl/formal-semantics/
