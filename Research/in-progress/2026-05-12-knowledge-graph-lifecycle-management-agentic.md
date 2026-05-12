---
title: "Knowledge Graph lifecycle management for multi-step software agents: schema versioning, entity resolution, and knowledge freshness"
added: 2026-05-12T08:21:48+00:00
status: reviewing
priority: high
blocks: []
tags: [knowledge-graph, agentic-ai, workflow]
started: 2026-05-12T10:35:05+00:00
completed: ~
output: []
cites:
  - 2026-05-12-knowledge-graph-agentic-runtime-dependency
  - 2026-05-12-graph-db-saas-knowledge-ontology
  - 2026-05-02-knowledge-graph-schema-cross-session-research-mcp
  - 2026-04-22-knowledge-curation-governance-for-regulated-ai
related:
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-03-03-knowledge-linking-connected-corpus
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Knowledge Graph lifecycle management for multi-step software agents: schema versioning, entity resolution, and knowledge freshness

## Research Question

What are the best practices for maintaining and evolving a Knowledge Graph (KG), a structured graph of entities and relationships, that serves multi-step software agents, covering schema versioning, entity resolution, conflict detection, and knowledge freshness, while avoiding disruption to dependent agents?

## Scope

**In scope:**
- Schema and ontology versioning strategies for Knowledge Graphs used in production multi-step software agents, including additive changes, separately versioned named graphs, meaning Resource Description Framework (RDF) datasets with distinct graph identifiers, and migration tooling
- Entity resolution, meaning identifying records or nodes that refer to the same real-world entity, and deduplication for a Knowledge Graph populated from multiple sources
- Knowledge freshness: how to detect stale facts, prioritise updates, and propagate changes without full reingestion
- Conflict detection: identifying when two sources assert contradictory facts about the same entity and how to resolve them
- Provenance and lineage, meaning traceable records of which source contributed each fact and how that affects trust and update prioritisation
- Continuous ingestion pipeline design: trigger-based versus scheduled updates, and incremental versus full refresh

**Out of scope:**
- Choice of graph database platform, covered in [Mitchell (2026) Hosted Software-as-a-Service graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
- Runtime access patterns and failure modes, covered in [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- Web ontology language selection
- Access policies and digital-rights design

**Constraints:**
- Focus on operationally mature approaches, not academic-only proposals
- Prefer documented practices from production systems or well-maintained open-source projects

## Context

Multi-step software agents depend on external knowledge surfaces that can change while the agent is still operating, so Knowledge Graph maintenance quality affects both answer quality and downstream actions. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://arxiv.org/abs/2312.10997]

The maintenance problem is not only about storing facts, but also about preserving stable identifiers, traceable provenance, bounded freshness lag, and safe correction paths as the graph evolves over time. [inference; source: https://www.w3.org/TR/prov-o/; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]

## Approach

1. Survey academic and practitioner literature on Knowledge Graph lifecycle management, especially update strategies, versioning patterns, and schema migration tooling.
2. Investigate entity resolution approaches at scale, especially blocking or indexing before matching and conservative merge practices.
3. Review provenance models for Knowledge Graphs, including RDF 1.2 triple terms, named graphs, and PROV-O, and assess how they support trust propagation and update prioritisation.
4. Examine conflict detection and resolution patterns, including assertion-level contradiction, ontology-level inconsistency, and temporal staleness.
5. Review continuous Knowledge Graph update pipeline architectures, especially Wikidata and DBpedia-style snapshot plus incremental update patterns.
6. Synthesize the evidence into recommended lifecycle practices and decision criteria for teams maintaining a Knowledge Graph as a dependency for multi-step software agents.

## Sources

- [ ] [Pellissier Tanon et al. (2020) Wikidata: A Free Collaborative Knowledge Base](https://dl.acm.org/doi/10.1145/3366423.3380185)
- [ ] [Kejriwal et al. (2022) Knowledge Graphs: Fundamentals, Techniques, and Applications](https://mitpress.mit.edu/9780262045094/knowledge-graphs/)
- [x] [Hogan et al. (2021) Knowledge Graphs](https://arxiv.org/abs/2003.02320)
- [x] [World Wide Web Consortium (W3C) RDF 1.2 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf12-concepts/)
- [ ] [Christophides et al. (2020) An Overview of End-to-End Entity Resolution for Big Data](https://dl.acm.org/doi/10.1145/3418896)
- [x] [Papadakis et al. (2020) End-to-End Entity Resolution for Big Data: A Survey](https://arxiv.org/abs/1905.06397)
- [x] [DBpedia Databus dataset version model](https://github.com/dbpedia/databus/blob/master/docs/version.md)
- [x] [DBpedia Databus versioning guide](https://github.com/dbpedia/databus/blob/master/docs/versioning.md)
- [x] [World Wide Web Consortium (W3C) PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)
- [x] [World Wide Web Consortium (W3C) SHACL: Shapes Constraint Language](https://www.w3.org/TR/shacl/)
- [x] [Wikidata Help: Merge](https://www.wikidata.org/wiki/Help:Merge)
- [x] [Wikidata Help: Redirects](https://www.wikidata.org/wiki/Help:Redirects)
- [x] [Wikidata Help: Sources](https://www.wikidata.org/wiki/Help:Sources)
- [x] [Wikidata: Database download](https://www.wikidata.org/wiki/Wikidata:Database_download)
- [x] [MediaWiki EventStreams](https://www.mediawiki.org/wiki/EventStreams)
- [x] [MediaWiki Wikibase RDF Dump Format](https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format)
- [x] [Wikidata: Identifiers](https://www.wikidata.org/wiki/Wikidata:Identifiers)
- [x] [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
- [x] [Mitchell (2026) Hosted Software-as-a-Service graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html)
- [x] [Mitchell (2026) What entity-relation schema and write-query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html)
- [x] [Mitchell (2026) Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine the lifecycle practices that keep a Knowledge Graph reliable for multi-step software agents while schema, source data, and entity identity evolve.
- Scope: schema versioning, entity resolution, provenance, conflict detection, freshness, and continuous ingestion are in scope; graph-platform choice, runtime-serving patterns, ontology-language selection, and access-policy design are out of scope.
- Constraints: prefer accessible production documentation, open standards, and well-documented open systems over paywalled summaries; expand acronyms on first use; keep the output directly usable as an operating model.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- Prior completed items consulted: [Mitchell (2026) Knowledge Graph in the live execution path of multi-step Large Language Model (LLM) systems: architecture and failure modes](https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html), [Mitchell (2026) Hosted Software-as-a-Service graph database options for knowledge ontology](https://davidamitchell.github.io/Research/research/2026-05-12-graph-db-saas-knowledge-ontology.html), [Mitchell (2026) What entity-relation schema and write-query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?](https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html), and [Mitchell (2026) Knowledge curation governance as an enterprise AI capability in regulated financial institutions](https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html).
- [inference] Working definition: in this item, lifecycle management means the operational controls that preserve a Knowledge Graph's identity model, provenance, structural validity, and freshness as new data arrives and older assertions are corrected, superseded, or retired. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]

### §1 Question Decomposition

- A. Versioning and change management
  - A1. How should graph or schema changes be published so dependent consumers can keep working?
  - A2. What metadata is needed to reconstruct an older graph state or explain when a change happened?
- B. Provenance and conflict handling
  - B1. How should the graph record where each assertion came from?
  - B2. How should the system distinguish structural invalidity from disagreement between sources?
- C. Entity resolution
  - C1. What steps should happen before two records are merged into one canonical entity?
  - C2. What should happen to old identifiers after a merge?
- D. Freshness and ingestion
  - D1. What combination of full refresh and incremental update is operationally mature?
  - D2. How should downstream agents know how fresh a graph-derived artifact is?
- E. Synthesis
  - E1. What operating model combines versioning, provenance, validation, and freshness into one safe lifecycle?
  - E2. Which adjacent repository findings qualify or sharpen that model?

### §2 Investigation

#### 2.0 Identified but not consulted

- [ ] Pellissier Tanon et al. (2020) Wikidata: A Free Collaborative Knowledge Base, seeded ACM DOI page.
- [ ] Kejriwal et al. (2022) Knowledge Graphs: Fundamentals, Techniques, and Applications, seeded MIT Press page.
- [ ] Christophides et al. (2020) An Overview of End-to-End Entity Resolution for Big Data, seeded ACM DOI page.

#### 2.1 Prior repository context

- [fact] The runtime-dependency item concluded that a Knowledge Graph used during execution should be treated as a tiered live service with explicit freshness limits rather than as a single always-live source of truth. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [fact] The cross-session schema item concluded that a small curated graph with explicit provenance is more durable than a maximal extraction graph for later reuse. [source: https://davidamitchell.github.io/Research/research/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.html]
- [fact] The knowledge-curation-governance item synthesized a six-stage lifecycle of intake, validation, publication, use with citation, correction, and retirement or recertification for authoritative knowledge assets. [source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]
- [inference] This item extends those prior findings from runtime and governance into the Knowledge Graph maintenance plane, where the key question is how to evolve graph structure and content without breaking dependent consumers. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]

#### 2.2 Versioning and publication mechanics

- [fact] RDF 1.2 defines RDF datasets as a default graph plus zero or more named graphs, and it allows triple terms so statements can themselves be objects of other statements. [source: https://www.w3.org/TR/rdf12-concepts/]
- [fact] PROV-O provides classes and properties for representing provenance and interchange of provenance information across systems, including derivation relationships between entities. [source: https://www.w3.org/TR/prov-o/]
- [fact] DBpedia Databus distinguishes an abstract artifact from a specific version and from a distribution, requires version-level metadata, and models dataset-version derivation with `prov:wasDerivedFrom`. [source: https://github.com/dbpedia/databus/blob/master/docs/version.md]
- [fact] DBpedia Databus recommends sortable timestamp-like version identifiers such as `YYYY.MM.DD-hhmmss`, allows re-submission of a version while changing the issued timestamp, and treats `dct:modified` as a version-level timestamp. [source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md]
- [fact] Wikibase RDF dumps expose `schema:softwareVersion` and `schema:dateModified` on dump metadata, and each entity data node carries `schema:version` and `schema:dateModified` for the entity record. [source: https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format]
- [fact] Wikidata database downloads describe JSON and RDF dumps as stable interfaces, publish JSON dumps weekly, and distinguish full RDF dumps from truthy RDF dumps that omit qualifiers and references. [source: https://www.wikidata.org/wiki/Wikidata:Database_download]
- [inference] The strongest published pattern is therefore immutable or at least separately identifiable graph publication, with explicit version IDs, timestamps, and derivation links, rather than silent in-place rewrites that force consumers to guess what changed. [source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://www.wikidata.org/wiki/Wikidata:Database_download]
- [inference] For schema evolution, additive-first change and deprecation of old terms are safer than repurposing existing identifiers, because the consulted versioning surfaces all preserve historical identity and change metadata instead of redefining old identifiers in place. [source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://www.wikidata.org/wiki/Wikidata:Database_download]

#### 2.3 Provenance and conflict handling

- [fact] Wikidata's sourcing guidance says most statements should be verifiable and backed by references, commonly through `stated in (P248)` for publications or `reference URL (P854)` for online sources. [source: https://www.wikidata.org/wiki/Help:Sources]
- [fact] SHACL is a W3C Recommendation for validating RDF graphs against shapes and producing validation reports that identify whether data graphs conform to declared constraints. [source: https://www.w3.org/TR/shacl/]
- [fact] PROV-O is explicitly intended to represent and interchange provenance information generated in different systems and contexts, and its `prov:wasDerivedFrom` relation is reused directly in DBpedia Databus version metadata. [source: https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md]
- [inference] Conflict detection should therefore be split into two control types: structural validation, using SHACL or an equivalent constraints layer to catch impossible states, and evidential adjudication, using provenance metadata to compare contradictory source assertions without overwriting their traceability. [source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Help:Sources]
- [inference] Recording source-specific assertions in separate named graphs, versioned snapshots, or assertion-level provenance triples is safer than flattening every update into one mutable current-state graph, because separation preserves both contradiction visibility and rollback paths. [source: https://www.w3.org/TR/rdf12-concepts/; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md]

#### 2.4 Entity resolution and duplicate repair

- [fact] Papadakis et al. define entity resolution as identifying different descriptions that refer to the same real-world entity, and describe end-to-end workflows that combine indexing or blocking with later matching to cope with scale, diversity, and speed. [source: https://arxiv.org/abs/1905.06397]
- [fact] Wikidata's merge guidance says merges should happen only when editors are certain two items describe the same thing, and automatic merge tools are preferred over manual transfer because redirects must be preserved. [source: https://www.wikidata.org/wiki/Help:Merge]
- [fact] Wikidata's redirect guidance states that redirects exist to provide stable identifiers, should not be deleted or repurposed, and are the preferred outcome when duplicates are merged. [source: https://www.wikidata.org/wiki/Help:Redirects]
- [fact] Wikidata identifiers are globally unique Uniform Resource Identifiers (URIs), and old or retired identifier systems are kept rather than erased even when the source website goes offline. [source: https://www.wikidata.org/wiki/Wikidata:Identifiers]
- [inference] Operationally mature entity resolution is conservative before merge and trace-preserving after merge: first narrow candidate pairs through indexing or blocking and evidence review, then merge only when certainty is high, while retaining aliases, old identifiers, or redirects so downstream references still resolve. [source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Identifiers]
- [inference] The lifecycle implication for agent-facing Knowledge Graphs is that canonicalization should be reversible or at least auditable, because aggressive auto-merge can silently collapse distinct entities and break historical references that dependent systems still hold. [source: https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.5 Freshness and ingestion patterns

- [fact] Wikidata publishes full JSON dumps weekly and documents RDF dumps as stable interfaces for batch access. [source: https://www.wikidata.org/wiki/Wikidata:Database_download]
- [fact] EventStreams exposes continuous structured event streams over Hypertext Transfer Protocol (HTTP) using Server-Sent Events and includes MediaWiki RecentChanges as a supported stream family. [source: https://www.mediawiki.org/wiki/EventStreams]
- [fact] The runtime-dependency item found that graph-derived caches and summaries need explicit freshness limits because change propagation and rebuild lag are normal operational conditions. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] The mature update pattern is a baseline snapshot plus incremental event ingestion plus periodic resynchronization, because dumps give complete stable state while change streams shrink freshness lag between scheduled full refreshes. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams]
- [inference] Derived artifacts consumed by agents, such as cached subgraphs, truthy exports, or generated summaries, need their own freshness metadata and rebuild policy, because source-system update mechanisms do not automatically tell the agent whether a derivative has caught up. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

#### 2.6 Cross-source operating model

- [inference] Across RDF standards, Wikidata operations, DBpedia Databus versioning, and the repository's adjacent items, the common lifecycle pattern is: ingest from identified sources, attach provenance, validate structure, resolve duplicates conservatively, publish a versioned state, propagate deltas, and recertify or retire stale assertions. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]
- [inference] For multi-step software agents, the lifecycle boundary that matters most is not only when the graph changes, but when a dependent derivative becomes safe to consume, because agents often read snapshots, caches, or summaries instead of querying the authoritative graph directly. [source: https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html; https://www.wikidata.org/wiki/Wikidata:Database_download]

### §3 Reasoning

- [fact] The strongest direct evidence in the consulted set covers four mechanics clearly: versioned publication, provenance representation, validation against constraints, and conservative duplicate handling. [source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Help:Merge]
- [inference] No single consulted source provides a complete lifecycle blueprint for agent-facing Knowledge Graphs, so the final operating model is a synthesis of open standards, public platform documentation, and adjacent completed repository items. [source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [assumption] Teams maintaining a Knowledge Graph for multi-step software agents can choose immutable publication and deprecation conventions at the application or workflow layer even if the underlying database supports in-place mutation. [source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]

### §4 Consistency Check

- [fact] The consulted sources agree that preserving identifier continuity after merge is preferable to deleting or reusing identifiers, even though they implement that continuity through different mechanisms such as redirects, version nodes, or derivation links. [source: https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Help:Merge; https://github.com/dbpedia/databus/blob/master/docs/version.md]
- [inference] The evidence is also internally consistent that provenance must remain queryable alongside current data, because the sources repeatedly model references, derivations, or timestamps as first-class metadata rather than optional annotations. [source: https://www.wikidata.org/wiki/Help:Sources; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format]
- [inference] Remaining uncertainty is concentrated in operational thresholds, such as merge-confidence cutoffs or acceptable freshness lag, not in the direction of the recommended controls. [source: https://arxiv.org/abs/1905.06397; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: lifecycle safety depends on separating authoritative state from consumable derivatives, because full dumps, truthy exports, caches, and summaries expose different trade-offs between completeness and freshness. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]
- [inference] Governance lens: lifecycle management needs named ownership for source correction and publication approval, because version metadata and provenance alone do not decide which change is authoritative. [source: https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html; https://www.w3.org/TR/prov-o/]
- [inference] Economic lens: incremental propagation with periodic re-sync is cheaper and operationally calmer than repeated full reingestion, provided the pipeline preserves a recoverable full snapshot. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams]
- [inference] Historical lens: stable identifiers, redirects, and version IDs reduce downstream breakage because they let older references keep resolving while consumers migrate to newer graph states. [source: https://www.wikidata.org/wiki/Help:Redirects; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format]
- [inference] Behavioural lens: overconfident automated merges are a higher-risk human-and-system failure mode than temporary duplicate records, because false merges silently contaminate later retrieval and are harder to detect than obvious unresolved duplicates. [source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge]

### §6 Synthesis

**Executive summary:**

Knowledge Graph lifecycle management for multi-step software agents is safest when teams publish additive, separately identifiable graph states, preserve historical identifiers after merges, attach provenance at assertion or graph level, and combine validation with explicit freshness metadata rather than relying on silent in-place updates. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.wikidata.org/wiki/Help:Redirects; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Wikidata:Database_download]

The strongest operational pattern in the consulted evidence is a lifecycle that separates authoritative state from consumable derivatives, because versioned snapshots, derivation links, dumps, change streams, and redirects all exist to preserve continuity while data changes. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://www.mediawiki.org/wiki/EventStreams; https://www.wikidata.org/wiki/Help:Redirects]

Entity resolution should be conservative before merge and trace-preserving after merge, while conflict handling should distinguish structural invalidity from legitimate disagreement between sources. [inference; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Help:Sources]

For agent-dependent use cases, freshness is not only a source-ingestion issue but also a derivative-publication issue, so caches, truthy views, and graph summaries need explicit rebuild policy and freshness stamps before dependent agents consume them. [inference; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Key findings:**

1. **Publishing Knowledge Graph changes as additive, separately identifiable versions or named-graph snapshots is safer than mutating live schemas in place, because RDF datasets, DBpedia Databus versions, and Wikibase dump metadata all preserve explicit version identity and change timestamps for consumers.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf12-concepts/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format)
2. **Schema evolution should default to additive change and deprecation instead of repurposing old identifiers, because the consulted lifecycle surfaces preserve derivation, issue dates, software versions, and stable interfaces rather than redefining historical identifiers in place.** ([inference]; medium confidence; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format)
3. **Assertion-level or graph-level provenance should remain queryable throughout the lifecycle, because reference metadata and PROV-style derivation are the mechanisms that let teams explain, compare, and safely overwrite conflicting facts.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Help:Sources; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md)
4. **Conflict handling is a two-part discipline that combines structural validation with evidential adjudication, because SHACL can detect invalid graph states while provenance records identify which source asserted each competing fact.** ([inference]; medium confidence; source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Help:Sources)
5. **Entity resolution should narrow candidates before matching and should preserve redirects or old identifiers after merge, because production-scale workflows depend on indexing plus matching and Wikidata's duplicate-repair practice prioritises stable identifier continuity.** ([inference]; high confidence; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Identifiers)
6. **Operationally mature freshness management uses a full snapshot plus incremental change stream plus periodic resynchronization, because dumps provide complete stable state while EventStreams-style feeds reduce lag between scheduled full refreshes.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams)
7. **For multi-step software agents, every derived graph artifact needs its own freshness stamp and publication gate, because the agent often consumes cached subgraphs, truthy exports, or summaries whose catch-up lag differs from the authoritative graph itself.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
8. **The safest end-to-end lifecycle is ingest, attach provenance, validate, resolve duplicates conservatively, publish a versioned state, propagate deltas, and periodically recertify or retire stale assertions, because that sequence aligns the strongest controls from standards, open Knowledge Graph operations, and adjacent repository research.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Additive, separately identifiable versions or named-graph snapshots are safer than silent in-place mutation for Knowledge Graph publication. | https://www.w3.org/TR/rdf12-concepts/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format | medium | Version identity and timestamp visibility |
| [inference] Schema evolution should default to additive change and deprecation rather than repurposing old identifiers. | https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format | medium | Stable-interface logic rather than explicit vendor rule |
| [inference] Provenance should stay queryable because references and derivation metadata are first-class parts of the consulted lifecycle surfaces. | https://www.wikidata.org/wiki/Help:Sources; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md | medium | Directly documented provenance mechanisms plus lifecycle synthesis |
| [inference] Conflict handling should combine validation rules with provenance-aware adjudication. | https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Help:Sources | medium | Structural versus evidential split |
| [inference] Entity resolution should use candidate narrowing before merge and should preserve redirects or old identifiers after merge. | https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Identifiers | high | Strong agreement across survey and operational docs |
| [inference] Mature freshness management uses a full snapshot, incremental change stream, and periodic resynchronization. | https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams | medium | Mature open-system ingestion pattern |
| [inference] Derived graph artifacts need their own freshness stamp and publication gate for agent use. | https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Cross-item synthesis on derivative lag |
| [inference] The safest end-to-end lifecycle is ingest, provenance, validate, resolve, version, propagate, and recertify or retire. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html | medium | Operating-model synthesis |

**Assumptions:**

- [assumption] Teams can implement additive publication and deprecation conventions above the storage engine even when the graph database itself permits destructive mutation. [source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]
- [assumption] Most multi-step software-agent deployments will consume some graph-derived caches, filtered exports, or summaries instead of querying the authoritative graph directly on every step. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Analysis:**

The evidence is strongest on control surfaces that are visible in mature open systems: version metadata, reference metadata, redirect-preserving merge practice, and separate mechanisms for full snapshots and incremental deltas. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.wikidata.org/wiki/Help:Sources; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams]

That evidence supports a lifecycle built around continuity and traceability rather than around maximal automation, because the consulted sources repeatedly preserve historical identity and source history even when doing merges, reissues, or refreshed dumps. [inference; source: https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://github.com/dbpedia/databus/blob/master/docs/versioning.md]

The main trade-off is operational cost versus disruption: keeping old identifiers, version nodes, and provenance graphs increases metadata overhead, but it sharply reduces breakage, rollback difficulty, and ambiguity about what changed. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.w3.org/TR/prov-o/; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format]

An alternative design that overwrites entities and schemas in place could be simpler to implement initially, but the consulted standards and operational documentation give much stronger support to explicit version, reference, and redirect surfaces than to silent mutation. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.wikidata.org/wiki/Help:Redirects; https://www.w3.org/TR/prov-o/]

**Risks, gaps, uncertainties:**

- The consulted evidence is stronger on open RDF ecosystems and public operational documentation than on private enterprise Knowledge Graph teams, so some platform-specific implementation details may differ outside those exemplars. [inference; source: https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Wikidata:Database_download; https://github.com/dbpedia/databus/blob/master/docs/version.md]
- The consulted sources establish the need for conservative entity resolution, but they do not provide one universal quantitative merge threshold for all domains, so merge confidence remains a local governance decision. [inference; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge]
- The evidence base is weaker on how quickly graph summaries should be rebuilt after each source update, because the open documentation is clearer about update mechanisms than about optimal rebuild cadence under production load. [inference; source: https://www.mediawiki.org/wiki/EventStreams; https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

**Open questions:**

- What freshness service-level objective should separate authoritative graph state from consumable derivatives for a given agent workflow?
- When should a team promote a contradiction from a source-level disagreement into a schema or shapes-level validation rule?
- What review evidence is sufficient to auto-merge duplicate entities in a domain with weak or missing external identifiers?

### §7 Recursive Review

- Review result: pass
- Confidence: medium
- Acronym audit: passed
- Domain-term clarity audit: passed
- Findings and section 6 parity: aligned
- Open contradictions: none material

---

## Findings

### Executive Summary

Knowledge Graph lifecycle management for multi-step software agents is safest when teams publish additive, separately identifiable graph states, preserve historical identifiers after merges, attach provenance at assertion or graph level, and combine validation with explicit freshness metadata rather than relying on silent in-place updates. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.wikidata.org/wiki/Help:Redirects; https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Wikidata:Database_download]

The strongest operational pattern in the consulted evidence is a lifecycle that separates authoritative state from consumable derivatives, because versioned snapshots, derivation links, dumps, change streams, and redirects all exist to preserve continuity while data changes. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://www.mediawiki.org/wiki/EventStreams; https://www.wikidata.org/wiki/Help:Redirects]

Entity resolution should be conservative before merge and trace-preserving after merge, while conflict handling should distinguish structural invalidity from legitimate disagreement between sources. [inference; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.w3.org/TR/shacl/; https://www.wikidata.org/wiki/Help:Sources]

For agent-dependent use cases, freshness is not only a source-ingestion issue but also a derivative-publication issue, so caches, truthy views, and graph summaries need explicit rebuild policy and freshness stamps before dependent agents consume them. [inference; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Key Findings

1. **Publishing Knowledge Graph changes as additive, separately identifiable versions or named-graph snapshots is safer than mutating live schemas in place, because RDF datasets, DBpedia Databus versions, and Wikibase dump metadata all preserve explicit version identity and change timestamps for consumers.** ([inference]; medium confidence; source: https://www.w3.org/TR/rdf12-concepts/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format)
2. **Schema evolution should default to additive change and deprecation instead of repurposing old identifiers, because the consulted lifecycle surfaces preserve derivation, issue dates, software versions, and stable interfaces rather than redefining historical identifiers in place.** ([inference]; medium confidence; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format)
3. **Assertion-level or graph-level provenance should remain queryable throughout the lifecycle, because reference metadata and PROV-style derivation are the mechanisms that let teams explain, compare, and safely overwrite conflicting facts.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Help:Sources; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md)
4. **Conflict handling is a two-part discipline that combines structural validation with evidential adjudication, because SHACL can detect invalid graph states while provenance records identify which source asserted each competing fact.** ([inference]; medium confidence; source: https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Help:Sources)
5. **Entity resolution should narrow candidates before matching and should preserve redirects or old identifiers after merge, because production-scale workflows depend on indexing plus matching and Wikidata's duplicate-repair practice prioritises stable identifier continuity.** ([inference]; high confidence; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Identifiers)
6. **Operationally mature freshness management uses a full snapshot plus incremental change stream plus periodic resynchronization, because dumps provide complete stable state while EventStreams-style feeds reduce lag between scheduled full refreshes.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams)
7. **For multi-step software agents, every derived graph artifact needs its own freshness stamp and publication gate, because the agent often consumes cached subgraphs, truthy exports, or summaries whose catch-up lag differs from the authoritative graph itself.** ([inference]; medium confidence; source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html)
8. **The safest end-to-end lifecycle is ingest, attach provenance, validate, resolve duplicates conservatively, publish a versioned state, propagate deltas, and periodically recertify or retire stale assertions, because that sequence aligns the strongest controls from standards, open Knowledge Graph operations, and adjacent repository research.** ([inference]; medium confidence; source: https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Additive, separately identifiable versions or named-graph snapshots are safer than silent in-place mutation for Knowledge Graph publication. | https://www.w3.org/TR/rdf12-concepts/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format | medium | Version identity and timestamp visibility |
| [inference] Schema evolution should default to additive change and deprecation rather than repurposing old identifiers. | https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format | medium | Stable-interface logic rather than explicit vendor rule |
| [inference] Provenance should stay queryable because references and derivation metadata are first-class parts of the consulted lifecycle surfaces. | https://www.wikidata.org/wiki/Help:Sources; https://www.w3.org/TR/prov-o/; https://github.com/dbpedia/databus/blob/master/docs/version.md | medium | Directly documented provenance mechanisms plus lifecycle synthesis |
| [inference] Conflict handling should combine validation rules with provenance-aware adjudication. | https://www.w3.org/TR/shacl/; https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Help:Sources | medium | Structural versus evidential split |
| [inference] Entity resolution should use candidate narrowing before merge and should preserve redirects or old identifiers after merge. | https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Identifiers | high | Strong agreement across survey and operational docs |
| [inference] Mature freshness management uses a full snapshot, incremental change stream, and periodic resynchronization. | https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams | medium | Mature open-system ingestion pattern |
| [inference] Derived graph artifacts need their own freshness stamp and publication gate for agent use. | https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html | medium | Cross-item synthesis on derivative lag |
| [inference] The safest end-to-end lifecycle is ingest, provenance, validate, resolve, version, propagate, and recertify or retire. | https://www.w3.org/TR/prov-o/; https://www.w3.org/TR/shacl/; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html | medium | Operating-model synthesis |

### Assumptions

- [assumption] Teams can implement additive publication and deprecation conventions above the storage engine even when the graph database itself permits destructive mutation. [source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://github.com/dbpedia/databus/blob/master/docs/version.md; https://davidamitchell.github.io/Research/research/2026-04-22-knowledge-curation-governance-for-regulated-ai.html]
- [assumption] Most multi-step software-agent deployments will consume some graph-derived caches, filtered exports, or summaries instead of querying the authoritative graph directly on every step. [source: https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Analysis

The evidence is strongest on control surfaces that are visible in mature open systems: version metadata, reference metadata, redirect-preserving merge practice, and separate mechanisms for full snapshots and incremental deltas. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.wikidata.org/wiki/Help:Sources; https://www.wikidata.org/wiki/Help:Redirects; https://www.wikidata.org/wiki/Wikidata:Database_download; https://www.mediawiki.org/wiki/EventStreams]

That evidence supports a lifecycle built around continuity and traceability rather than around maximal automation, because the consulted sources repeatedly preserve historical identity and source history even when doing merges, reissues, or refreshed dumps. [inference; source: https://www.wikidata.org/wiki/Help:Merge; https://www.wikidata.org/wiki/Help:Redirects; https://github.com/dbpedia/databus/blob/master/docs/versioning.md]

The main trade-off is operational cost versus disruption: keeping old identifiers, version nodes, and provenance graphs increases metadata overhead, but it sharply reduces breakage, rollback difficulty, and ambiguity about what changed. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.w3.org/TR/prov-o/; https://www.mediawiki.org/wiki/Special:MyLanguage/Wikibase/Indexing/RDF_Dump_Format]

An alternative design that overwrites entities and schemas in place could be simpler to implement initially, but the consulted standards and operational documentation give much stronger support to explicit version, reference, and redirect surfaces than to silent mutation. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/versioning.md; https://www.wikidata.org/wiki/Help:Redirects; https://www.w3.org/TR/prov-o/]

### Risks, Gaps, and Uncertainties

- The consulted evidence is stronger on open RDF ecosystems and public operational documentation than on private enterprise Knowledge Graph teams, so some platform-specific implementation details may differ outside those exemplars. [inference; source: https://www.w3.org/TR/prov-o/; https://www.wikidata.org/wiki/Wikidata:Database_download; https://github.com/dbpedia/databus/blob/master/docs/version.md]
- The consulted sources establish the need for conservative entity resolution, but they do not provide one universal quantitative merge threshold for all domains, so merge confidence remains a local governance decision. [inference; source: https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Help:Merge]
- The evidence base is weaker on how quickly graph summaries should be rebuilt after each source update, because the open documentation is clearer about update mechanisms than about optimal rebuild cadence under production load. [inference; source: https://www.mediawiki.org/wiki/EventStreams; https://www.wikidata.org/wiki/Wikidata:Database_download; https://davidamitchell.github.io/Research/research/2026-05-12-knowledge-graph-agentic-runtime-dependency.html]

### Open Questions

- What freshness service-level objective should separate authoritative graph state from consumable derivatives for a given agent workflow?
- When should a team promote a contradiction from a source-level disagreement into a schema or shapes-level validation rule?
- What review evidence is sufficient to auto-merge duplicate entities in a domain with weak or missing external identifiers?

---

## Output

- Type: knowledge
- Description: Lifecycle management guidance for Knowledge Graphs that support multi-step software agents, covering versioned publication, provenance, conservative entity resolution, and hybrid snapshot-plus-delta freshness control. [inference; source: https://github.com/dbpedia/databus/blob/master/docs/version.md; https://www.w3.org/TR/prov-o/; https://arxiv.org/abs/1905.06397; https://www.wikidata.org/wiki/Wikidata:Database_download]
- Links:
  - https://github.com/dbpedia/databus/blob/master/docs/version.md
  - https://www.w3.org/TR/prov-o/
  - https://arxiv.org/abs/1905.06397
