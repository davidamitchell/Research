---
title: "Universal Entity Lifecycle Governance Framework (UELGF) 8-layer organisational context model: evolution from static classification to a live, queryable knowledge graph for policy coherence and Confidentiality, Integrity, and Availability (CIA)-tiered enforcement"
added: 2026-05-15T19:59:47+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [uelgf, knowledge-graph, ontology, policy-coherence, cia-classification, regulated-banking]
started: 2026-05-16T00:00:18+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-04-27-uelgf-policy-architecture-8-layer-context
  - 2026-04-27-uelgf-entity-taxonomy-cia-classification
  - 2026-04-27-uelgf-synthesis-complete-framework
  - 2026-04-27-uelgf-runtime-feedback-loop
  - 2026-04-28-uelgf-tooling-reference-architecture
  - 2026-05-15-ontology-landscape-for-curated-enterprise-context
related:
  - 2026-05-12-web-ontologies-production-knowledge-graph-agentic
  - 2026-05-12-data-product-ontology
  - 2026-05-12-knowledge-graph-lifecycle-management-agentic
  - 2026-05-12-graph-db-saas-knowledge-ontology
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this item replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Universal Entity Lifecycle Governance Framework (UELGF) 8-layer organisational context model: evolution from static classification to a live, queryable knowledge graph for policy coherence and Confidentiality, Integrity, and Availability (CIA)-tiered enforcement

## Research Question

What is the most suitable knowledge representation architecture for evolving the Universal Entity Lifecycle Governance Framework (UELGF) 8-layer organisational context model from static classification into a live, queryable graph, including: a formal mapping from layers and entity types to ontology classes and named relationships; a justified choice between Resource Description Framework (RDF) / Web Ontology Language (OWL), Labelled Property Graph (LPG), or hybrid modelling for conflict detection, policy coherence checks, and Confidentiality, Integrity, and Availability (CIA)-tiered enforcement; semantically safe handling of relationship confidence or edge-weight signals; and an ingestion strategy for Kiwibank policy, system-state, and domain documentation rather than a curated open corpus?

## Scope

**In scope:**
- Ontological mapping from UELGF layers, entity taxonomy, and CIA tiers to classes, properties, constraints, and named relationships.
- Comparative evaluation of RDF/OWL, LPG, and hybrid designs against UELGF requirements for conflict detection, policy coherence checking, and CIA-tiered enforcement actions.
- Representation options for weighted or confidence-scored relationships without breaking semantic consistency guarantees.
- Parsing and ingestion architecture for heterogeneous Kiwibank internal artefacts, including policy text, system state, and architecture or domain documentation, with provenance and change tracking.
- Dependency mapping to prior UELGF completed items and explicit follow-up-question dependencies that should be sequenced in the research backlog.

**Out of scope:**
- Production implementation of a graph platform for Kiwibank.
- Vendor procurement decisions for specific graph databases.
- Legal advice on Kiwibank regulatory obligations beyond architecture-relevant requirements already captured in sources.

**Constraints:** (time, source types, access)
- Prioritise primary standards and peer-reviewed sources for graph and ontology design, plus prior repository research for UELGF assumptions.
- Treat Kiwibank-internal material as a constrained-access corpus; specify an ingestion challenge model that remains valid when documents are not publicly accessible.
- Distinguish hard semantic constraints from probabilistic confidence annotations so the resulting model preserves deterministic policy checks.

## Context

This item asks how to turn the existing UELGF specification into an operational, machine-checkable graph architecture rather than a static descriptive framework. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]

The prior UELGF items already define the layer stack, the entity taxonomy, the Confidentiality, Integrity, and Availability (CIA) scoring model, the runtime feedback loop, and the tooling surfaces, so this item's job is to choose the graph representation that can carry those semantics safely into enforcement and ingestion workflows. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html]

The adjacent ontology-landscape item now provides a broad survey baseline, so it is informative rather than a blocking prerequisite for this UELGF-specific decision. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

Prior completed research dependencies:
- [UELGF policy architecture and 8-layer context](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html)
- [UELGF entity taxonomy and CIA classification](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)
- [UELGF complete framework synthesis](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html)
- [UELGF runtime feedback loop](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html)
- [UELGF tooling reference architecture](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html)
- [Ontology landscape for curated lexical and structured enterprise context](https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html)

## Approach

1. Define the ontology surface: map each UELGF layer and entity type to candidate classes, properties, relationship predicates, and integrity constraints.
2. Evaluate model families, RDF/OWL, LPG, and hybrid, against required reasoning tasks: conflict detection, policy coherence checking, and CIA-tiered enforcement evaluation.
3. Specify how relationship confidence and edge weights are represented, separating epistemic certainty from normative policy truth conditions.
4. Design an ingestion and normalisation pipeline for Kiwibank internal policy, system state, and domain artefacts, including provenance, update cadence, and contradiction handling.
5. Produce a dependency map covering:
   5a. follow-up research questions implied by unresolved design choices in this item;
   5b. dependency ordering across existing research backlog items and newly generated follow-up questions, explicitly testing whether `2026-05-15-ontology-landscape-for-curated-enterprise-context` should run first as a discovery prerequisite.

## Sources

Starting points and follow-on sources consulted during the investigation.
Every source includes a direct URL so the generated site can render verifiable citations.

- [x] [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/)
- [x] [W3C OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/)
- [x] [W3C OWL 2 Profiles](https://www.w3.org/TR/owl2-profiles/)
- [ ] [Angles et al. (2023) The Labeled Property Graph Model](https://doi.org/10.1145/3571255)
- [x] [Hogan et al. (2021) Knowledge Graphs](https://arxiv.org/abs/2003.02320)
- [x] [Neo4j Cypher Manual: Constraints](https://neo4j.com/docs/cypher-manual/current/constraints/)
- [x] [W3C RDF-star and SPARQL-star Community Group Report](https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html)
- [x] [W3C RDF and SPARQL Working Group](https://www.w3.org/groups/wg/rdf-star/)
- [x] [W3C SHACL Shapes Constraint Language](https://www.w3.org/TR/shacl/)
- [x] [W3C PROV Ontology (PROV-O)](https://www.w3.org/TR/prov-o/)
- [x] [W3C PROV Model Primer](https://www.w3.org/TR/prov-primer/)
- [x] [W3C Data Catalog Vocabulary (DCAT) Version 3](https://www.w3.org/TR/vocab-dcat-3/)
- [x] [W3C ODRL Information Model](https://www.w3.org/TR/odrl-model/)
- [x] [W3C ODRL Vocabulary and Expression](https://www.w3.org/TR/odrl-vocab/)
- [x] [W3C Data on the Web Best Practices](https://www.w3.org/TR/dwbp/)
- [x] [Sun et al. (2024) Docs2KG: Unified Knowledge Graph Construction from Heterogeneous Documents Assisted by Large Language Models](https://arxiv.org/html/2406.02962)
- [ ] [Kiwibank Responsible Business Policy](https://www.kiwibank.co.nz/about-us/who-we-are/our-purpose/responsible-business-policy/)
- [ ] [Kiwibank Sustainability Report 2025](https://www.kiwibank.co.nz/about-us/who-we-are/our-purpose/sustainability/sustainability-report-2025/)
- [x] [UELGF policy architecture and 8-layer context](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html)
- [x] [UELGF entity taxonomy and CIA classification](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)
- [x] [UELGF complete framework synthesis](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html)
- [x] [UELGF runtime feedback loop](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html)
- [x] [UELGF tooling reference architecture](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html)
- [x] [Ontology landscape for curated lexical and structured enterprise context](https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine the most suitable graph architecture for making UELGF live, queryable, provenance-aware, and safe for deterministic policy coherence and CIA-tiered enforcement.
- Scope: evaluate RDF/OWL, LPG, and hybrid architectures; map the UELGF layers and entity taxonomy into graph classes and relations; define confidence handling; define ingestion and change-tracking architecture for constrained-access internal artefacts.
- Constraints: prioritize standards and peer-reviewed sources; keep probabilistic confidence separate from normative truth conditions; assume Kiwibank source-of-truth material is mostly internal and not publicly inspectable.
- Output format: full research record with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior completed items consulted: UELGF policy architecture, entity taxonomy and CIA model, full framework synthesis, runtime feedback loop, tooling reference architecture, and the ontology-landscape survey baseline.

### §1 Question Decomposition

1. Representation choice
   1.1 What does RDF 1.1 contribute that UELGF needs?
   1.2 What does OWL 2 contribute that UELGF needs?
   1.3 What does SHACL contribute that OWL alone does not?
   1.4 What does LPG contribute that RDF/OWL does not?
   1.5 Which control surfaces require canonical semantics, and which require ergonomic traversal or analytics?
2. UELGF graph mapping
   2.1 How should the 8 organisational context layers be represented?
   2.2 How should UELGF entity types be represented?
   2.3 How should CIA axis values and derived overall tier be represented?
   2.4 Which named relationships are required for policy coherence and dependency checks?
3. Confidence and statement metadata
   3.1 Should confidence be represented as truth conditions or annotation metadata?
   3.2 When is RDF-star safe to use?
   3.3 What is the fallback if RDF-star support is not production-ready?
4. Internal-document ingestion
   4.1 How should source documents, extracted claims, and promoted graph assertions be separated?
   4.2 How should provenance, versions, and change tracking be modeled?
   4.3 What promotion path should apply to contradictory or high-impact extractions?
5. Dependency and sequencing
   5.1 Did the ontology-landscape item need to run first?
   5.2 Which follow-up questions remain after this architecture decision?

### §2 Investigation

#### 2.1 RDF, OWL, SHACL, and LPG as candidate families

- [fact] RDF 1.1 defines a graph-based data model built from subject-predicate-object triples and supports datasets with a default graph plus named graphs, which makes it suitable for separating canonical assertions from assertion context. [source: https://www.w3.org/TR/rdf11-concepts/]
- [fact] OWL 2 provides classes, properties, individuals, formally defined semantics, and profiles that trade expressive power for computational tractability. [source: https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/]
- [fact] SHACL validates RDF data graphs against explicit shapes graphs, including cardinality, datatype, logical, and SPARQL Protocol and RDF Query Language (SPARQL)-based constraints, which directly addresses closed-world conformance checks that OWL does not by itself provide. [source: https://www.w3.org/TR/shacl/]
- [fact] The knowledge-graph survey literature treats schema, identity, and context as first-class design questions and describes both deductive and inductive methods for knowledge graph creation, enrichment, and refinement. [source: https://arxiv.org/abs/2003.02320]
- [fact] Neo4j's current constraints documentation frames schema constraint support as a graph-shape maintenance mechanism, which supports the claim that LPG systems can enforce local graph structure even without RDF semantics. [source: https://neo4j.com/docs/cypher-manual/current/constraints/]
- [inference] RDF plus bounded OWL is stronger than LPG for authoritative meaning because it supplies globally referenceable identifiers, interoperable vocabularies, and explicit formal semantics, while SHACL adds the deterministic validation UELGF needs for policy coherence checks. [source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/]
- [inference] LPG remains useful for traversal-heavy user interfaces, graph analytics, and statement shapes with many edge properties, but it is weaker than RDF/OWL as the canonical source of truth for a governance model that depends on shared semantics across systems. [source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320]

#### 2.2 Mapping the existing UELGF structure into a graph

- [fact] The UELGF policy-architecture item specifies the 8-layer context model as an ordered constraint stack in which lower layers may specialize but not weaken higher layers. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]
- [fact] The UELGF taxonomy item specifies one canonical entity taxonomy, explicit CIA axis values, highest-triggered-axis overall tiering, and rule-based floors for high-consequence surfaces. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html]
- [fact] The UELGF runtime-feedback item treats runtime events as typed governance findings that can suspend, re-evaluate, retire, or reclassify entities. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]
- [fact] The UELGF tooling-reference item separates policy authoring and publication, decision evaluation, stateful context, telemetry collection, and enforcement adapters into distinct control-plane surfaces. [source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html]
- [inference] The 8 UELGF layers should be represented as typed instances or subclasses of a `uelgf:OrganisationalContextLayer` concept, linked by explicit precedence or `uelgf:constrains` and `uelgf:refines` relations, because the prior item already treats them as ordered governance layers rather than informal categories. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]
- [inference] UELGF entity families should be modeled as subclasses of `uelgf:Entity`, with named specializations for policy artefact, data product, software service, integration component, decision workflow, and Artificial Intelligence (AI) agent classes, because the taxonomy item already makes those distinctions operationally decisive. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html]
- [inference] CIA should be modeled as an explicit profile object with three axis values plus a derived overall tier, not as a single label, because enforcement intensity, runtime thresholds, and review routing depend on the separate axis values as well as the overall minimum. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html]

#### 2.3 Policy representation and confidence handling

- [fact] Open Digital Rights Language (ODRL) provides a policy expression model with policy, rule, permission, prohibition, duty, action, and constraint concepts, and is designed for interoperable machine-readable policy statements. [source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/odrl-vocab/]
- [fact] The RDF-star and SPARQL-star Community Group report provides a concise notation for statements about statements, but it is a community-group draft rather than a World Wide Web Consortium (W3C) Recommendation. [source: https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/]
- [fact] PROV Ontology (PROV-O) provides classes and properties for representing provenance, including entities, activities, agents, derivation, responsibility, and qualified relations. [source: https://www.w3.org/TR/prov-o/]
- [fact] The PROV Model Primer explicitly includes derivation and revision as core provenance concepts for tracking how one artefact comes from another over time. [source: https://www.w3.org/TR/prov-primer/]
- [inference] Normative UELGF policy truth conditions should be represented as asserted graph statements plus SHACL and policy constraints, while confidence should be represented as provenance-bearing annotation metadata attached to extracted or promoted claims, because mixing confidence weights into the truth value of policy edges would make deterministic enforcement ambiguous. [source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/odrl-model/]
- [inference] RDF-star is acceptable as a convenience layer for statement-level metadata when the implementation stack supports it, but named graphs plus PROV-O are the safer baseline because they are standardized and do not depend on a draft feature. [source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/prov-o/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/]

#### 2.4 Internal-document ingestion, provenance, and versioning

- [fact] Data Catalog Vocabulary (DCAT) Version 3 adds versioning support such as `dcat:version`, `dcat:previousVersion`, `dcat:hasCurrentVersion`, dataset series support, and checksum support for distributions. [source: https://www.w3.org/TR/vocab-dcat-3/]
- [fact] The Data on the Web Best Practices recommendation treats provenance, versioning, identifiers, metadata, and access policy as core publication concerns rather than optional embellishments. [source: https://www.w3.org/TR/dwbp/]
- [fact] Docs2KG targets heterogeneous unstructured documents, including web pages, Portable Document Format (PDF) files, email, and spreadsheets, and preserves document-structure references inside a graph representation. [source: https://arxiv.org/html/2406.02962]
- [fact] The ontology-landscape item concluded that ontology should be the canonical semantic layer while operational graph behavior, lineage, and retrieval needs are handled by complementary layers rather than a single universal representation. [source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] Internal ingestion should separate source documents, extracted candidate assertions, and promoted canonical assertions into distinct graph layers, because provenance, contradiction handling, and human review are materially simpler when raw extraction never overwrites canonical governance truth directly. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/vocab-dcat-3/; https://arxiv.org/html/2406.02962]
- [inference] Each source document should enter the graph as an immutable document entity with checksum, owner, access rights, version, and timestamp metadata, because that provides the minimal stable anchor for provenance, re-extraction, and audit. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/dwbp/; https://www.w3.org/TR/prov-o/]
- [inference] Contradictory or high-impact extracted assertions should require a human promotion step before they can become canonical UELGF facts, because the governance model is intended to drive enforcement rather than only retrieval and therefore cannot treat uncertain extraction as authoritative truth. [source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html]

#### 2.5 Dependency ordering and unresolved follow-up questions

- [fact] The ontology-landscape item now concludes that a layered hybrid architecture with ontology as canonical semantics and complementary validation, lineage, and operational layers is the strongest broad baseline for enterprise graph design. [source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] That item sharpened this investigation, but it did not need to run first to make the UELGF-specific decision, because the decisive evidence for this item also depends on the already completed UELGF policy, taxonomy, runtime, and tooling items plus the World Wide Web Consortium (W3C) standards corpus. [source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html]
- [inference] The highest-value follow-up questions are practical rather than conceptual: which OWL 2 profile is sufficient at expected scale, which RDF-star or named-graph implementation choices are supportable in the target platform, and how much automated extraction quality can be trusted before human review becomes a bottleneck. [source: https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/groups/wg/rdf-star/; https://arxiv.org/html/2406.02962]

#### Access notes and failed primary-source searches

- Access note: direct fetch of `https://www.kiwibank.co.nz/about-us/who-we-are/our-purpose/responsible-business-policy/` timed out in this runtime
- Access note: direct fetch of `https://www.kiwibank.co.nz/about-us/who-we-are/our-purpose/sustainability/sustainability-report-2025/` timed out in this runtime
- [assumption] Search query `"The Labeled Property Graph Model" Angles 2023 arXiv` did not locate a verified accessible primary text in this runtime, and the seeded DOI `https://doi.org/10.1145/3571255` returned an access failure, so LPG comparison claims in this item rely on the accessible knowledge-graph survey and vendor documentation instead of the inaccessible seeded paper. [source: https://arxiv.org/abs/2003.02320; https://neo4j.com/docs/cypher-manual/current/constraints/]

### §3 Reasoning

- [fact] RDF, OWL, SHACL, PROV-O, DCAT 3, and ODRL each cover a different required surface: graph identity and statements, ontology semantics, closed-world validation, provenance, versioning, and policy expression. [source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/odrl-model/]
- [fact] Prior UELGF items already commit the framework to deterministic layer precedence, explicit CIA scoring, typed runtime findings, and separated control-plane roles. [source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html]
- [inference] Because UELGF already depends on deterministic semantics and explicit validation, the canonical representation must be RDF/OWL plus SHACL rather than pure LPG. [source: https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]
- [inference] Because operational users will still need fast traversal, edge-rich exploration, and possibly graph analytics, the canonical RDF model should expose an LPG projection rather than forcing every runtime interface to query the canonical semantic store directly. [source: https://arxiv.org/abs/2003.02320; https://neo4j.com/docs/cypher-manual/current/constraints/; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [assumption] The target bank can support one canonical semantic store plus one derived operational graph without making synchronization risk worse than the benefits of semantic clarity and operational ergonomics. [source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/]

### §4 Consistency Check

- [inference] Tension: OWL uses open-world semantics while UELGF policy coherence requires fail-closed behavior. Resolution: use OWL for shared meaning and SHACL plus policy rules for closed-world admission and coherence checks. [source: https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/]
- [inference] Tension: LPG handles edge properties ergonomically while normative policy truth must stay deterministic. Resolution: keep confidence, provenance, and extraction metadata out of the truth conditions of canonical policy edges; project those annotations into the operational graph as needed. [source: https://www.w3.org/TR/prov-o/; https://neo4j.com/docs/cypher-manual/current/constraints/]
- [inference] Tension: RDF-star is convenient for statement metadata but is not yet a Recommendation. Resolution: support it only as an optional implementation detail behind a named-graph plus PROV baseline. [source: https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/; https://www.w3.org/TR/prov-o/]
- [inference] Tension: internal bank documents are largely inaccessible at research time. Resolution: define the ingestion architecture in terms of document classes, provenance requirements, and promotion controls rather than in terms of a public sample corpus. [source: https://www.w3.org/TR/dwbp/; https://arxiv.org/html/2406.02962]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the architecture boundary should fall between semantic authority and operational read models, because UELGF needs both interoperable semantics and graph-application ergonomics. [source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] Regulatory lens: provenance, version lineage, and policy publication metadata are not secondary concerns in a regulated bank, because auditability and change accountability affect whether enforcement decisions can be defended. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/dwbp/]
- [inference] Economic lens: hybrid modeling costs more to build than a single graph model, but it reduces later rework because the canonical semantics are stable while operational projections can change with user-interface and analytics needs. [source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]
- [inference] Historical lens: the repository's adjacent ontology and graph items repeatedly converge on layered architectures instead of one universal representation, which strengthens the case that UELGF should follow the same pattern rather than insisting on one graph formalism for every surface. [source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-05-12-web-ontologies-production-knowledge-graph-agentic.html; https://davidamitchell.github.io/Research/research/2026-05-12-data-product-ontology.html]
- [inference] Behavioural lens: separating extracted candidate assertions from promoted canonical assertions is necessary to prevent reviewers from trusting uncertain extraction too readily, because a live governance graph that silently promotes uncertain extraction into enforcement truth would encourage false confidence in the resulting controls. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://arxiv.org/html/2406.02962]

### §6 Synthesis

**Executive summary:**

A hybrid architecture with RDF 1.1 and a bounded Web Ontology Language (OWL) 2 profile as the canonical model, SHACL for closed-world validation, and a derived Labelled Property Graph (LPG) projection for traversal and analytics is the most suitable design for UELGF. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320]

This architecture fits the existing UELGF items because they already require deterministic layer precedence, explicit CIA scoring, typed runtime findings, and separated policy, decision, information, and enforcement roles that depend on stable shared semantics. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html]

Relationship confidence must remain annotation metadata attached to extracted or promoted statements rather than part of normative policy truth conditions, with named graphs plus PROV-O as the safe baseline and RDF-star as an optional convenience where supported. [inference; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/rdf11-concepts/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/]

Ingestion should treat internal documents as immutable versioned sources, preserve provenance from extraction onward, and require human promotion for contradictory or high-impact assertions before they can affect canonical governance state. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/; https://arxiv.org/html/2406.02962]

The ontology-landscape item strengthened this decision, but it did not need to run first; the decisive step here was grounding the existing UELGF specification in graph standards and assigning each formalism to the control surface it is strongest at. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/]

**Key findings:**

1. **A hybrid architecture with RDF 1.1 and a bounded OWL 2 profile as the canonical semantic model, SHACL as the validation layer, and an LPG projection as the operational read model is the best fit for UELGF because it combines formal shared meaning with deterministic conformance checking and graph-application ergonomics.** ([inference]; high confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320)
2. **Pure LPG is not a sufficient canonical representation for UELGF because the framework's existing policy, taxonomy, and runtime items already rely on explicit precedence, globally interpretable semantics, and cross-system policy coherence that are stronger in RDF/OWL than in application-scoped property-graph conventions.** ([inference]; medium confidence; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)
3. **The UELGF graph should model the eight organisational context layers, entity families, CIA axis values, and named governance relations as explicit classes and predicates rather than only labels or free-form properties, because enforcement, conflict detection, and review routing depend on those distinctions being machine-checkable instead of merely descriptive.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/)
4. **Relationship confidence and extraction uncertainty should be represented as provenance-bearing annotation metadata, not as weighted normative edges, because UELGF policy enforcement must stay deterministic while extraction reliability still needs to be preserved for ranking, triage, and human review.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/prov-primer/; https://www.w3.org/TR/shacl/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/)
5. **Named graphs plus PROV-O are the safest baseline for statement-level provenance and change tracking, while RDF-star should remain optional until platform support and standard maturity are acceptable for the target deployment, because the RDF-star work is still a draft-track effort rather than a finished Recommendation.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/prov-o/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/)
6. **The ingestion pipeline should preserve immutable document versions, checksums, access metadata, extraction lineage, and promotion history from the beginning, because provenance and versioning are not optional extras in a regulated governance graph that may later justify suspension, escalation, or audit conclusions.** ([inference]; high confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/)
7. **Internal policy, system-state, and domain-document ingestion should separate raw source objects, extracted candidate assertions, and promoted canonical assertions into distinct graph layers, because that separation contains contradiction risk and stops uncertain extraction from silently mutating the authoritative governance state.** ([inference]; medium confidence; source: https://arxiv.org/html/2406.02962; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html)
8. **The ontology-landscape item sharpened but did not block this decision, because this item's decisive work was mapping the existing UELGF policy and taxonomy structure onto standards-backed graph layers rather than only establishing that hybrid knowledge-graph architectures are generally common in enterprise settings.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid RDF/OWL plus SHACL plus LPG projection is the best overall UELGF design. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320 | high | Canonical semantics and operational ergonomics are split deliberately. |
| [inference] Pure LPG is too weak to be the canonical UELGF representation. | https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html | medium | Vendor constraint support does not replace interoperable formal semantics. |
| [inference] UELGF layers, entity families, CIA values, and named relations should be explicit classes and predicates. | https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/ | high | Machine-checkable distinctions matter for enforcement and coherence checks. |
| [inference] Confidence belongs in provenance metadata, not in normative truth conditions. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/prov-primer/; https://www.w3.org/TR/shacl/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/ | high | Deterministic enforcement must stay separate from extraction uncertainty. |
| [inference] Named graphs plus PROV-O are the safest baseline, with RDF-star optional. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/prov-o/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/ | medium | Draft-status metadata weakens confidence in RDF-star-first designs. |
| [inference] Versioning, checksum, provenance, and access metadata must be first-class ingestion artifacts. | https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/ | high | Regulated governance graphs need lineage and auditable change control. |
| [inference] Raw sources, extracted assertions, and canonical assertions should be distinct layers. | https://arxiv.org/html/2406.02962; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html | medium | Promotion control contains contradiction and automation-bias risk. |
| [inference] The ontology-landscape item was supportive, not blocking. | https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html | medium | This item still required UELGF-specific mapping and control-surface assignment. |

**Assumptions:**

- [assumption; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/] The target implementation can maintain one canonical semantic graph and at least one derived operational graph without losing lineage between them. Justification: the standards support versioning and provenance across resources, but they do not prove any specific estate already operates this pattern.
- [assumption; source: https://www.w3.org/TR/shacl/; https://arxiv.org/html/2406.02962] Human promotion of contradictory or high-impact assertions is operationally feasible even when extraction throughput rises. Justification: the sources support extraction plus validation patterns, but they do not prove the target bank's review capacity.

**Analysis:**

The strongest decision boundary is between canonical meaning and operational convenience, not between "semantic web" and "property graph" camps as if only one formalism may exist. [inference; source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

OWL 2 and RDF 1.1 win the canonical layer because UELGF is already framed as a shared governance specification with explicit classes, relationships, precedence, and policy consequences that need interoperable identifiers and reasoned semantics. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]

SHACL is the decisive complement because UELGF needs fail-closed admission and coherence checking, and that is a validation problem more than an ontology-entailment problem. [inference; source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/owl2-overview/]

LPG remains important, but its strongest place is the derived operational surface where edge-rich exploration, graph applications, and traversal-oriented queries matter more than canonical semantic authority. [inference; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320]

The main rival remedy would be to use pure RDF for every surface and avoid dual-model complexity, but that would push traversal and user-interface ergonomics into the canonical store and make edge-heavy operational work harder without improving governance truth conditions enough to justify the trade. [inference; source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://www.w3.org/groups/wg/rdf-star/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html] RDF-star maturity remains a moving target, so teams should not make it the only viable provenance pattern for statement-level metadata.
- [inference; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320] The item does not benchmark any specific platform, so the recommendation is architecture-level rather than procurement-level.
- [assumption; source: https://www.w3.org/TR/shacl/; https://arxiv.org/html/2406.02962] Human promotion of high-impact extracted claims may become a throughput bottleneck if document volume is high and extraction quality is mediocre.
- [inference; source: https://www.w3.org/TR/owl2-profiles/] The choice between OWL 2 RL and another bounded profile still needs scale and query testing against the target corpus and rule shapes.
- [assumption; source: https://www.w3.org/TR/dwbp/] Internal source-system metadata quality may be uneven, which would make provenance and ownership fields incomplete unless the ingestion pipeline enforces minimum metadata requirements at entry.

**Open questions:**

- [inference; source: https://www.w3.org/TR/owl2-profiles/] Which OWL 2 profile preserves the needed inferences for UELGF at the expected corpus size and refresh cadence?
- [inference; source: https://www.w3.org/groups/wg/rdf-star/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html] Which target platforms support RDF-star well enough to justify using it instead of named-graph provenance patterns?
- [inference; source: https://arxiv.org/html/2406.02962; https://www.w3.org/TR/shacl/] What extraction quality threshold justifies automatic promotion for low-risk assertions without creating unacceptable governance error?
- [inference; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/shacl/] How much of UELGF policy coherence checking can be expressed declaratively in ODRL and SHACL before application-level rules become unavoidable?
- [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/] What dataset-series and revision granularity is sufficient for audit without making the change history too expensive to store and review?

### §7 Recursive Review

- [fact] The first automated review pass flagged two defects in visible prose, unlabeled access-note text in section 2 and unlabeled review-metadata text in section 7, and both defects were corrected in this revision. [source: https://github.com/davidamitchell/Research/actions/runs/25947416586]
- [inference] After those corrections, the remaining visible research prose, Findings, and mirrored section-6 synthesis are aligned on labels, sources, and substantive conclusions. [source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-15-uelgf-live-queryable-knowledge-graph.md]

---

## Findings

### Executive Summary

A hybrid architecture with RDF 1.1 and a bounded Web Ontology Language (OWL) 2 profile as the canonical model, SHACL for closed-world validation, and a derived Labelled Property Graph (LPG) projection for traversal and analytics is the most suitable design for UELGF. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320]

That choice fits the existing UELGF specification because the prior items already require deterministic layer precedence, explicit CIA scoring, typed runtime findings, and separated policy, decision, information, and enforcement roles that depend on stable shared semantics. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-runtime-feedback-loop.html; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-tooling-reference-architecture.html]

Relationship confidence should remain annotation metadata attached to extracted or promoted statements rather than part of normative policy truth conditions, with named graphs plus PROV-O as the safe baseline and RDF-star as an optional convenience where supported. [inference; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/rdf11-concepts/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/]

Ingestion should treat internal documents as immutable versioned sources, preserve provenance from extraction onward, and require human promotion for contradictory or high-impact assertions before they can affect canonical governance state. [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/; https://arxiv.org/html/2406.02962]

The ontology-landscape item strengthened this recommendation, but it did not need to run first because the decisive step here was mapping the existing UELGF policy and taxonomy structure onto graph standards and assigning each formalism to the control surface it is strongest at. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/]

### Key Findings

1. **A hybrid architecture with RDF 1.1 and a bounded OWL 2 profile as the canonical semantic model, SHACL as the validation layer, and an LPG projection as the operational read model is the best fit for UELGF because it combines formal shared meaning with deterministic conformance checking and graph-application ergonomics.** ([inference]; high confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320)
2. **Pure LPG is not a sufficient canonical representation for UELGF because the framework's existing policy, taxonomy, and runtime items already rely on explicit precedence, globally interpretable semantics, and cross-system policy coherence that are stronger in RDF/OWL than in application-scoped property-graph conventions.** ([inference]; medium confidence; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)
3. **The UELGF graph should model the eight organisational context layers, entity families, CIA axis values, and named governance relations as explicit classes and predicates rather than only labels or free-form properties, because enforcement, conflict detection, and review routing depend on those distinctions being machine-checkable instead of merely descriptive.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/)
4. **Relationship confidence and extraction uncertainty should be represented as provenance-bearing annotation metadata, not as weighted normative edges, because UELGF policy enforcement must stay deterministic while extraction reliability still needs to be preserved for ranking, triage, and human review.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/prov-primer/; https://www.w3.org/TR/shacl/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/)
5. **Named graphs plus PROV-O are the safest baseline for statement-level provenance and change tracking, while RDF-star should remain optional until platform support and standard maturity are acceptable for the target deployment, because the RDF-star work is still a draft-track effort rather than a finished Recommendation.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/prov-o/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/)
6. **The ingestion pipeline should preserve immutable document versions, checksums, access metadata, extraction lineage, and promotion history from the beginning, because provenance and versioning are not optional extras in a regulated governance graph that may later justify suspension, escalation, or audit conclusions.** ([inference]; high confidence; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/)
7. **Internal policy, system-state, and domain-document ingestion should separate raw source objects, extracted candidate assertions, and promoted canonical assertions into distinct graph layers, because that separation contains contradiction risk and stops uncertain extraction from silently mutating the authoritative governance state.** ([inference]; medium confidence; source: https://arxiv.org/html/2406.02962; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html)
8. **The ontology-landscape item sharpened but did not block this decision, because this item's decisive work was mapping the existing UELGF policy and taxonomy structure onto standards-backed graph layers rather than only establishing that hybrid knowledge-graph architectures are generally common in enterprise settings.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid RDF/OWL plus SHACL plus LPG projection is the best overall UELGF design. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/owl2-profiles/; https://www.w3.org/TR/shacl/; https://arxiv.org/abs/2003.02320 | high | Canonical semantics and operational ergonomics are split deliberately. |
| [inference] Pure LPG is too weak to be the canonical UELGF representation. | https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html | medium | Vendor constraint support does not replace interoperable formal semantics. |
| [inference] UELGF layers, entity families, CIA values, and named relations should be explicit classes and predicates. | https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html; https://www.w3.org/TR/owl2-overview/; https://www.w3.org/TR/shacl/ | high | Machine-checkable distinctions matter for enforcement and coherence checks. |
| [inference] Confidence belongs in provenance metadata, not in normative truth conditions. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/prov-primer/; https://www.w3.org/TR/shacl/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/ | high | Deterministic enforcement must stay separate from extraction uncertainty. |
| [inference] Named graphs plus PROV-O are the safest baseline, with RDF-star optional. | https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/prov-o/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html; https://www.w3.org/groups/wg/rdf-star/ | medium | Draft-status metadata weakens confidence in RDF-star-first designs. |
| [inference] Versioning, checksum, provenance, and access metadata must be first-class ingestion artifacts. | https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/dwbp/ | high | Regulated governance graphs need lineage and auditable change control. |
| [inference] Raw sources, extracted assertions, and canonical assertions should be distinct layers. | https://arxiv.org/html/2406.02962; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-synthesis-complete-framework.html | medium | Promotion control contains contradiction and automation-bias risk. |
| [inference] The ontology-landscape item was supportive, not blocking. | https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-entity-taxonomy-cia-classification.html | medium | This item still required UELGF-specific mapping and control-surface assignment. |

### Assumptions

- [assumption; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/] **Assumption:** The target implementation can maintain one canonical semantic graph and at least one derived operational graph without losing lineage between them. **Justification:** the standards support versioning and provenance across resources, but they do not prove any specific estate already operates this pattern.
- [assumption; source: https://www.w3.org/TR/shacl/; https://arxiv.org/html/2406.02962] **Assumption:** Human promotion of contradictory or high-impact assertions is operationally feasible even when extraction throughput rises. **Justification:** the sources support extraction plus validation patterns, but they do not prove the target bank's review capacity.

### Analysis

The strongest decision boundary is between canonical meaning and operational convenience, not between "semantic web" and "property graph" camps as if only one formalism may exist. [inference; source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

OWL 2 and RDF 1.1 win the canonical layer because UELGF is already framed as a shared governance specification with explicit classes, relationships, precedence, and policy consequences that need interoperable identifiers and reasoned semantics. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/owl2-overview/; https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-policy-architecture-8-layer-context.html]

SHACL is the decisive complement because UELGF needs fail-closed admission and coherence checking, and that is a validation problem more than an ontology-entailment problem. [inference; source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/owl2-overview/]

LPG remains important, but its strongest place is the derived operational surface where edge-rich exploration, graph applications, and traversal-oriented queries matter more than canonical semantic authority. [inference; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320]

The main rival remedy would be to use pure RDF for every surface and avoid dual-model complexity, but that would push traversal and user-interface ergonomics into the canonical store and make edge-heavy operational work harder without improving governance truth conditions enough to justify the trade. [inference; source: https://arxiv.org/abs/2003.02320; https://davidamitchell.github.io/Research/research/2026-05-15-ontology-landscape-for-curated-enterprise-context.html]

### Risks, Gaps, and Uncertainties

- [inference; source: https://www.w3.org/groups/wg/rdf-star/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html] RDF-star maturity remains a moving target, so teams should not make it the only viable provenance pattern for statement-level metadata.
- [inference; source: https://neo4j.com/docs/cypher-manual/current/constraints/; https://arxiv.org/abs/2003.02320] The item does not benchmark any specific platform, so the recommendation is architecture-level rather than procurement-level.
- [assumption; source: https://www.w3.org/TR/shacl/; https://arxiv.org/html/2406.02962] Human promotion of high-impact extracted claims may become a throughput bottleneck if document volume is high and extraction quality is mediocre.
- [inference; source: https://www.w3.org/TR/owl2-profiles/] The choice between OWL 2 RL and another bounded profile still needs scale and query testing against the target corpus and rule shapes.
- [assumption; source: https://www.w3.org/TR/dwbp/] Internal source-system metadata quality may be uneven, which would make provenance and ownership fields incomplete unless the ingestion pipeline enforces minimum metadata requirements at entry.

### Open Questions

- [inference; source: https://www.w3.org/TR/owl2-profiles/] Which OWL 2 profile preserves the needed inferences for UELGF at the expected corpus size and refresh cadence?
- [inference; source: https://www.w3.org/groups/wg/rdf-star/; https://w3c-cg.github.io/rdf-star/cg-spec/2021-12-17.html] Which target platforms support RDF-star well enough to justify using it instead of named-graph provenance patterns?
- [inference; source: https://arxiv.org/html/2406.02962; https://www.w3.org/TR/shacl/] What extraction quality threshold justifies automatic promotion for low-risk assertions without creating unacceptable governance error?
- [inference; source: https://www.w3.org/TR/odrl-model/; https://www.w3.org/TR/shacl/] How much of UELGF policy coherence checking can be expressed declaratively in ODRL and SHACL before application-level rules become unavoidable?
- [inference; source: https://www.w3.org/TR/vocab-dcat-3/; https://www.w3.org/TR/prov-o/] What dataset-series and revision granularity is sufficient for audit without making the change history too expensive to store and review?

---

## Output

- Type: knowledge
- Description: Recommended UELGF graph architecture and ingestion model: canonical RDF/OWL plus SHACL, optional LPG projection, provenance-safe confidence handling, and versioned internal-document promotion workflow. [inference; source: https://www.w3.org/TR/rdf11-concepts/; https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/vocab-dcat-3/]
- Links:
  - https://www.w3.org/TR/rdf11-concepts/
  - https://www.w3.org/TR/shacl/
  - https://www.w3.org/TR/prov-o/
