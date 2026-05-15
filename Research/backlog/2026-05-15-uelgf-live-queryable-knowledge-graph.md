---
title: "Universal Entity Lifecycle Governance Framework (UELGF) 8-layer organisational context model: evolution from static classification to a live, queryable knowledge graph for policy coherence and Confidentiality, Integrity, and Availability (CIA)-tiered enforcement"
added: 2026-05-15T19:59:47+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [uelgf, knowledge-graph, ontology, policy-coherence, cia-classification, regulated-banking]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-27-uelgf-policy-architecture-8-layer-context, 2026-04-27-uelgf-entity-taxonomy-cia-classification, 2026-04-27-uelgf-synthesis-complete-framework]
related: [2026-04-27-uelgf-runtime-feedback-loop, 2026-04-28-uelgf-tooling-reference-architecture, 2026-04-27-pdp-universal-policy-synchronisation-integrity, 2026-05-15-ontology-landscape-for-curated-enterprise-context]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
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
- Parsing and ingestion architecture for heterogeneous Kiwibank internal artefacts (policy text, system state, architecture/domain documentation), including provenance and change tracking.
- Dependency mapping to prior UELGF completed items and explicit follow-up-question dependencies that should be sequenced in the research backlog.

**Out of scope:**
- Production implementation of a graph platform for Kiwibank.
- Vendor procurement decisions for specific graph databases.
- Legal advice on Kiwibank regulatory obligations beyond architecture-relevant requirements already captured in sources.

**Constraints:** (time, source types, access)
- Prioritise primary standards and peer-reviewed sources for graph/ontology design, plus prior repository research for UELGF assumptions.
- Treat Kiwibank-internal material as a constrained-access corpus; specify an ingestion challenge model that remains valid when documents are not publicly accessible.
- Distinguish hard semantic constraints from probabilistic confidence annotations so the resulting model preserves deterministic policy checks.

## Context

This question informs how UELGF can transition from a static framework specification into an operational governance substrate that supports machine-checkable policy coherence and CIA-tiered enforcement decisions in a real banking environment where source-of-truth inputs are primarily internal artefacts.

Prior completed research dependencies:
- [UELGF policy architecture and 8-layer context](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-policy-architecture-8-layer-context.md)
- [UELGF entity taxonomy and CIA classification](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-entity-taxonomy-cia-classification.md)
- [UELGF complete framework synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-synthesis-complete-framework.md)

Potential research-backlog dependency:
- [Ontology landscape for curated lexical and structured enterprise context](https://github.com/davidamitchell/Research/blob/main/Research/backlog/2026-05-15-ontology-landscape-for-curated-enterprise-context.md) — candidate prerequisite for shared ontology and graph-model baseline decisions; if this item remains unmerged or is renamed, keep the dependency intent and update to the canonical successor slug.

## Approach

1. Define the ontology surface: map each UELGF layer and entity type to candidate classes, properties, relationship predicates, and integrity constraints.
2. Evaluate model families (RDF/OWL, LPG, hybrid) against required reasoning tasks: conflict detection, policy coherence checking, and CIA-tiered enforcement evaluation.
3. Specify how relationship confidence and edge weights are represented, separating epistemic certainty from normative policy truth conditions.
4. Design an ingestion and normalisation pipeline for Kiwibank internal policy, system state, and domain artefacts, including provenance, update cadence, and contradiction handling.
5. Produce a dependency map covering:
   5a. follow-up research questions implied by unresolved design choices in this item;
   5b. dependency ordering across existing research backlog items and newly generated follow-up questions, explicitly testing whether `2026-05-15-ontology-landscape-for-curated-enterprise-context` should run first as a discovery prerequisite.

## Sources

Starting points — papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below — they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` — for papers with named authors
- `[Organisation Title](https://url)` — for documentation, standards, or pages without a named author

- [ ] [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) — canonical semantic-data model foundations.
- [ ] [W3C OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/) — ontology expressivity and reasoning primitives.
- [ ] [Angles et al. (2023) The Labeled Property Graph Model](https://doi.org/10.1145/3571255) — formalisation of LPG semantics.
- [ ] [Hogan et al. (2021) Knowledge Graphs](https://arxiv.org/abs/2003.02320) — survey of modelling and operational trade-offs.
- [ ] [Neo4j Cypher Manual: Constraints](https://neo4j.com/docs/cypher-manual/current/constraints/) — practical consistency mechanisms in LPG systems.
- [ ] [RDF-star and SPARQL-star Community Group Report](https://w3c.github.io/rdf-star/cg-spec/) — approaches for statement-level metadata such as confidence/provenance.
- [ ] [Kiwibank Responsible Banking](https://www.kiwibank.co.nz/about-us/who-we-are/responsible-banking/) — organisational governance context anchor.
- [ ] [Kiwibank Annual Report](https://www.kiwibank.co.nz/about-us/investor-centre/annual-reports/) — publicly available context for organisational structure and risk framing.

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

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
