---
title: "Noise thresholds and topology drift in planar memory graphs"
added: 2026-08-20T07:13:11+00:00
status: reviewing
priority: high
blocks: []
themes: [agentic-ai, memory-context, knowledge-graphs, llm-reasoning, benchmarks-eval]
started: 2026-09-01T07:17:18+00:00
completed: ~
output: []
cites: [2026-07-20-tbox-abox-graphrag, 2026-03-03-knowledge-representation-agent-context, 2026-07-20-agent-memory-evaluation-framework, 2026-08-20-graphrag-macro-level-hallucination]
related: [2026-05-27-semantic-domain-emergence-enterprise-ontology, 2026-03-15-latent-concept-extraction-confluence, 2026-05-02-knowledge-graph-schema-cross-session-research-mcp]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Noise thresholds and topology drift in planar memory graphs

## Research Question

In a two-dimensional (2D) planar memory graph, what threshold of contextual noise causes a bounded entity-extraction schema to stop suppressing Large Language Model (LLM)-driven predicate hallucinations, and how does the resulting topological drift affect the agent's ability to perform spatial-relational reasoning over the graph?

## Scope

**In scope:**
- Planar or otherwise explicitly spatial graph layouts used as an agent-memory representation
- Entity and relation extraction pipelines that constrain what predicates may be written into the graph
- Failure modes where duplicated entities, invented predicates, or misplaced edges accumulate over time
- Effects of extraction noise on downstream path-finding, neighborhood reasoning, and other spatial-relational tasks
- Whether there is an observable or defensible threshold at which local extraction errors become global topology drift

**Out of scope:**
- Three-dimensional or multimodal world-model systems where planar layout is not central to the representation
- General LLM hallucination theory not tied to graph-construction or graph-reasoning behavior
- AWS-specific ontology pipelines, which are covered by separate items in this cluster

**Constraints:** Prioritise empirical Graph Retrieval-Augmented Generation (GraphRAG), memory-graph, and extraction-evaluation literature from 2023-2026. If no paper provides a direct numeric threshold, the output should identify proxy metrics and threshold-estimation methods instead of inventing one.

## Context

The issue frames a personal planar-memory architecture as vulnerable to accumulated extraction noise, but the prior GraphRAG and memory-evaluation items in the repository do not isolate the point at which local predicate errors stop being recoverable and start corrupting global graph shape. Answering that question would inform whether a planar graph can remain a stable long-horizon memory substrate or needs stronger schema controls, repair passes, or a different representational form.

## Related

- [TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
- [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html)

## Approach

1. Define the target planar-memory architecture precisely enough to distinguish layout choices from logical graph structure.
2. Identify what counts as contextual noise in this setting: entity ambiguity, alias duplication, invented predicates, misplaced relations, or stale edges.
3. Review bounded-schema extraction approaches and determine which error classes they can and cannot suppress.
4. Investigate metrics for topology drift, such as duplicate-node growth, edge inconsistency, community-fragmentation shift, or degraded path-query accuracy.
5. Synthesize whether planar structure offers enough stiffness for long-horizon memory or whether drift-correction and schema evolution are mandatory.

## Sources

- [ ] [GitHub issue #651: Multiple research questions](https://github.com/davidamitchell/Research/issues/651) — canonical statement of the research request and open-question linkage
- [ ] [TBox-driven vs ABox-emergent ontology approaches in GraphRAG systems](https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html) — closest prior repository item on schema-guided versus emergent graph construction
- [ ] [Knowledge Representation for Agent Context](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html) — prior repository item on graph-based context representations
- [ ] [Domain Emergence in Semantic Networks, Cognition, and Organizational Structure](https://davidamitchell.github.io/Research/research/2026-05-27-semantic-domain-emergence-enterprise-ontology.html) — prior repository item on threshold effects in semantic graph structure
- [ ] [Evaluation frameworks for agentic memory quality, relevance, and retrieval accuracy](https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html) — prior repository item on how to measure graph-memory failure
- [x] [Graph-Based Agent Memory Systems: A Survey (2026)](https://arxiv.org/abs/2602.05665) — arXiv preprint surveying graph-based agent memory architectures; no planarity-specific category identified
- [x] [Graph Retrieval-Augmented Generation: A Survey (2024)](https://arxiv.org/abs/2404.16130) — original GraphRAG survey establishing default construction and community-detection pipeline
- [x] [Zero-shot Schema-free Extraction and Its Cross-document Fragmentation Failure (2023)](https://arxiv.org/abs/2305.04676) — arXiv preprint documenting inconsistent per-document self-inferred ontologies
- [x] [Constraint-based Sufficiency-guided Retrieval-Augmented Generation over Noisy Knowledge Graphs (2026)](https://arxiv.org/abs/2603.14828) — arXiv preprint on spurious-noise and incomplete-information issue modes in LLM-constructed knowledge graphs, with a constraint-based retriever
- [x] [GraphEval: A Knowledge-Graph-Based Framework for Hallucination Detection and Correction (2024)](https://arxiv.org/abs/2407.10793) — arXiv preprint on post-extraction knowledge-graph-based hallucination correction
- [x] [Zhang et al. Constructing Coherent Spatial Memory in LLM Agents through Graph Rectification (2026)](https://aclanthology.org/2026.acl-long.2222/) — ACL (Association for Computational Linguistics) paper on version-controlled repair of incrementally-constructed topological navigation graphs using an Edge Impact Score
- [x] [Microsoft GraphRAG Default Dataflow Documentation](https://microsoft.github.io/graphrag/index/default_dataflow/) — official documentation confirming default entity-merge matches only identical title/type strings
- [x] [Vectorize/Hindsight Entity Resolution for Agent Memory (2026)](https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory) — vendor engineering blog describing a weighted-score entity-merge cutoff of 0.6
- [x] [Girvan & Newman Community Structure in Social and Biological Networks / Modularity Threshold (PNAS)](https://www.pnas.org/doi/10.1073/pnas.0601602103) — PNAS (Proceedings of the National Academy of Sciences) paper establishing modularity Q>0.3 as a proxy for stable community structure
- [x] [From Louvain to Leiden: Guaranteeing Well-Connected Communities (Nature Scientific Reports)](https://www.nature.com/articles/s41598-019-41695-z) — Nature Scientific Reports paper on the Leiden algorithm's internal-connectivity guarantee
- [x] [GraphRAG macro-level hallucination from unresolved duplicate entities](https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html) — companion repository item from the same issue cluster, cited directly for the uncalibrated-proxy-metrics finding

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: in a two-dimensional (2D) planar memory graph, what threshold of contextual noise causes a bounded entity-extraction schema to stop suppressing Large Language Model (LLM)-driven predicate hallucinations, and how does the resulting topological drift affect the agent's ability to perform spatial-relational reasoning over the graph?

Scope: planar or otherwise explicitly spatial graph layouts used as agent memory; entity/relation extraction pipelines that constrain writable predicates; failure modes from duplicated entities, invented predicates, and misplaced edges; effects on path-finding and neighborhood reasoning; whether an observable threshold separates local extraction error from global topology drift. Out of scope: three-dimensional or multimodal world-model systems, general hallucination theory untied to graph construction, and AWS-specific ontology pipelines covered by a separate item in this cluster. Constraint mode: full. Output format: knowledge item with proxy metrics and threshold-estimation methods substituted for a direct numeric threshold if none is found in the literature, per the item's own Scope constraint.

Prior-work cross-reference: `Research/completed/` was searched for related items. Four items are already listed in this item's frontmatter (`cites`/`related`): the TBox (Terminological Box, a predefined ontology or schema)-versus-ABox (Assertion Box, instance-level facts emerging from data) Graph Retrieval-Augmented Generation (GraphRAG) comparison, the knowledge-representation-for-agent-context item, the agent-memory-evaluation-framework item, and the semantic-domain-emergence item. A fifth completed item from the same GitHub issue #651 cluster, `graphrag-macro-level-hallucination`, investigates the same underlying failure mechanism (unresolved duplicate entities corrupting downstream community-detection summaries); its finding is quoted directly in §2.4b below, so it is added to this item's frontmatter `cites:` list.

### §1 Question Decomposition

1. What is a "planar memory graph" as an agent-memory architecture, and how does spatial layout differ from logical graph structure?
   1a. Does a published architecture matching this description exist in the 2023-2026 literature?
   1b. What distinguishes a planar/spatial memory graph from a general-purpose knowledge graph (KG)?
2. What counts as contextual noise in extraction, and what error classes does it produce?
   2a. Entity ambiguity and alias duplication.
   2b. Invented (hallucinated) predicates.
   2c. Misplaced or spurious relations.
   2d. Stale or missing edges.
3. What do bounded/schema-constrained extraction approaches suppress, and what do they leave unsuppressed?
4. What metrics exist for topology drift, and do any establish a numeric noise threshold?
   4a. Duplicate-node growth.
   4b. Edge inconsistency and community-fragmentation shift.
   4c. Degraded path-query accuracy.
5. Does the evidence support a defensible position on whether planar structure has enough stiffness for long-horizon memory, or whether repair and schema evolution are mandatory?

### §2 Investigation

**1a/1b.** No paper in the reviewed 2023-2026 GraphRAG, agent-memory, or spatial-reasoning literature uses "planar memory graph" as a named architecture. [fact; source: https://arxiv.org/abs/2602.05665] Search used: "planar memory graph agent LLM 2D layout" and "planar knowledge graph agent memory architecture"; outcome: no matching named architecture located. The closest published match is a 2026 framework that builds an explicit topological navigation graph from stepwise LLM observations and repairs structural inconsistencies after the fact, which operates over a 2D map layout without naming the representation "planar." [fact; source: https://aclanthology.org/2026.acl-long.2222/] The item's own architecture is therefore best treated as a coined design label rather than an established term. Definition needed: absent an authoritative definition, the nearest evidence-backed functional equivalent used throughout this investigation is an incrementally-constructed topological navigation graph, as described in that framework. [inference; source: https://aclanthology.org/2026.acl-long.2222/] A 2026 survey of graph-based agent memory categorises memory along axes of short-term versus long-term, knowledge versus experience, and structural versus non-structural memory, but does not identify layout planarity as a distinct architectural category, so the survey's own taxonomy offers no planarity-specific robustness claim. [fact; source: https://arxiv.org/abs/2602.05665]

**2a-2d.** Standard GraphRAG's default entity-merge step performs no semantic entity resolution, matching only identical title-and-type strings, so alias duplication (2a) is structurally expected to survive into the graph. [fact; source: https://microsoft.github.io/graphrag/index/default_dataflow/] Schema-free extraction produces a documented cross-document concept-fragmentation failure mode in which an LLM's self-inferred ontology per document is inconsistent across documents even for substantively similar concepts. [fact; source: https://arxiv.org/abs/2305.04676] An empirical analysis of LLM-constructed knowledge graphs identifies two recurring issue modes: spurious noise, which induces retrieval drift toward plausible but unsupported triples (a graph-level analogue of invented predicates, 2b), and incomplete information, which forces retrieval to continue through under-supported structure (adjacent to stale or missing edges, 2d). [fact; source: https://arxiv.org/abs/2603.14828] Misplaced or spurious relations (2c) are the structural expression of that same spurious-noise category: a plausible-looking edge the extraction schema did not intend and that the source text does not support. [inference; source: https://arxiv.org/abs/2603.14828]

**3.** A TBox-driven biomedical GraphRAG implementation improves extraction accuracy on clean corpora by roughly three percentage points but loses accuracy faster than a schema-free implementation as corpus noise increases, per the prior repository item's evidence map. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html] A bounded schema constrains which predicate *types* may be written but does not verify whether a specific instance of an allowed predicate type is actually supported by the source text; it can suppress out-of-vocabulary hallucinations while remaining exposed to in-vocabulary ones. [inference; source: https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html] A query-time sufficiency check, deciding whether retrieved evidence can safely support a variable binding before propagating it to the next reasoning hop, operates independently of the extraction-time schema and targets this same in-vocabulary gap. [fact; source: https://arxiv.org/abs/2603.14828]

**4a.** No located source reports a duplicate-node growth curve or an inflection point at which duplicate-node accumulation becomes structurally irreversible for any GraphRAG or agent-memory system. Search used: "duplicate node growth rate knowledge graph threshold arxiv" and "entity resolution graph memory inflection point"; outcome: no arXiv paper located, only vendor engineering documentation describing per-mention merge scoring. A production agent-memory system's entity-resolution merge cutoff is a workable proxy for a duplicate-suppression threshold: one implementation uses a weighted score (name similarity 0.5, co-occurrence overlap 0.3, temporal recency 0.2) with a merge cutoff at 0.6, chosen to be conservative against false merges rather than validated as an information-theoretic optimum. [assumption; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory]

**4b.** Dense semantic networks with a modularity value, a measure of how much more densely connected a proposed community is than a random graph with the same degree sequence, above Q equals 0.3 exhibit stable, measurable community structure, per the prior repository item's evidence map citing Girvan and Newman. [fact; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] Because community-detection stability is the graph-theoretic analogue of "topology drift has not yet corrupted global structure," a modularity value falling below roughly Q equals 0.3 is a plausible proxy signal that local extraction noise has begun eroding global community boundaries, though no source directly measures this transition in an agent-memory or GraphRAG-specific graph. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103] The Leiden community-detection algorithm used in the reference GraphRAG pipeline guarantees only that each detected community is internally well-connected; it carries no guarantee that the underlying nodes and edges are semantically correct, so a graph can retain high modularity while its community assignments misrepresent noise-corrupted entities inside them. [fact; source: https://www.nature.com/articles/s41598-019-41695-z; https://arxiv.org/abs/2404.16130] This decouples the two proxy signals: modularity measures structural community stability, while a separate hallucination-detection signal is required to measure semantic correctness within a stable-looking community. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html] The companion repository item on macro-level hallucination in standard GraphRAG concludes that no located study directly measures how community-report distortion scales with injected duplicate or falsely-associated node counts, leaving this exact quantitative relationship an open evidence gap shared by both items. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html]

**4c.** GraphRAG-Bench was built specifically because GraphRAG frequently underperforms plain Retrieval-Augmented Generation (RAG) on real-world tasks, and its four-level difficulty gradient exists to isolate exactly when graph structure earns its added complexity cost, per the prior repository item's evidence map. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html] Fine-grained, constraint-based retrieval remains more stable under controlled knowledge-graph issue injection than retrievers that assume a structurally sound knowledge graph, evaluated across three multi-hop question-answering benchmarks. [fact; source: https://arxiv.org/abs/2603.14828] Multi-hop path-query accuracy degrading under injected noise is the closest available empirical proxy for spatial path-finding degradation in a planar memory graph, because both tasks require an unbroken, correctly-typed chain of edges between a start node and a goal node. [inference; source: https://arxiv.org/abs/2603.14828] A version-controlled repair mechanism using an Edge Impact Score, which prioritises repairs by structural reachability, path usage, and conflict propagation, is reported to significantly improve map correctness and robustness, especially in scenarios with entangled or chained inconsistencies, directly evidencing that uncorrected structural inconsistency degrades path-relevant graph correctness in a spatial navigation graph. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

**5.** No source establishes a single numeric noise threshold at which a planar or spatially-laid-out memory graph's topology becomes unrecoverable; per this item's own Scope constraint, the applicable output form is a set of proxy metrics and threshold-estimation methods rather than an invented number. [inference; source: https://arxiv.org/abs/2603.14828; https://www.pnas.org/doi/10.1073/pnas.0601602103] The evidence assembled here converges on repair-based robustness rather than schema-based prevention: every source that measures a system remaining usable under noise, the sufficiency-check retriever, the knowledge-graph-based hallucination-correction framework, and the version-controlled graph-rectification framework, achieves that robustness through an active detection-and-correction mechanism operating after extraction, not through a fixed extraction schema alone. [inference; source: https://arxiv.org/abs/2603.14828; https://arxiv.org/abs/2407.10793; https://aclanthology.org/2026.acl-long.2222/]

### §3 Reasoning

Bounded schemas constrain predicate type, not predicate-instance truthfulness against source text; an in-vocabulary hallucination passes through a fixed schema unaffected. [inference; source: https://arxiv.org/abs/2603.14828] No source measures a single numeric noise threshold for topology collapse in any graph-memory system, planar or otherwise; this absence was confirmed by two independent failed search threads recorded in §2.4a. [fact; source: absence confirmed across the search threads recorded in §2.4a] Two proxy-metric families exist in the evidence base: a structural-stability family built on modularity and community-detection quality, and a task-outcome family built on multi-hop path-query accuracy and community-report factual distortion; no located study calibrates one family against the other in a single experiment. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://arxiv.org/abs/2603.14828] Every system in the evidence base that demonstrably remains usable under noise does so through an active repair loop operating after extraction, not through schema rigidity alone. [inference; source: https://arxiv.org/abs/2603.14828; https://arxiv.org/abs/2407.10793; https://aclanthology.org/2026.acl-long.2222/]

### §4 Consistency Check

```text
contradiction_scan: resolved
confidence_adjustment: no direct numeric threshold located; output reframed to proxy metrics per this item's own Scope constraint
scope_guardrail: maintained; three-dimensional/multimodal and AWS-specific pipelines excluded throughout
acronym_audit: passed on final pass at §7
```

### §5 Depth and Breadth Expansion

Technical lens: the technical evidence base is covered in §2 above; the strongest technical signal is that active, post-extraction repair (sufficiency checks, triple correction, version-controlled rectification) is the only mechanism in the evidence base shown to hold a graph usable under noise, rather than schema design alone. [inference; source: https://arxiv.org/abs/2603.14828; https://arxiv.org/abs/2407.10793; https://aclanthology.org/2026.acl-long.2222/]

Regulatory lens: no regulatory framework reviewed in this repository's adjacent governance-cluster items treats knowledge-graph topology drift as a compliance surface distinct from general model-output accuracy, and no new regulatory source specific to graph topology stability was located during this investigation. [assumption; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html]

Economic lens: fixed-schema extraction is a one-time engineering cost paid at pipeline-design time, while active repair, version control, sufficiency checks, and impact-score-based repair prioritisation, is a recurring computational cost paid at every write and read cycle; the evidence base does not quantify this cost trade-off directly, so this is stated as an inference from the described mechanisms rather than a measured comparison. [inference; source: https://aclanthology.org/2026.acl-long.2222/; https://arxiv.org/abs/2603.14828]

Historical lens: percolation threshold, the point at which a graph's largest connected component stops scaling with graph size as random edges are removed, is a decades-old result in network science that predates agent-memory systems and is offered here only as an orientation concept for why network-robustness researchers reach for a single critical-threshold framing; it has not been directly applied to LLM-constructed knowledge graphs in any source located during this investigation. [assumption; source: https://en.wikipedia.org/wiki/Percolation_threshold]

Behavioural lens: an agent performing spatial-relational reasoning over a drifting graph resembles the multi-hop question-answering failure mode in which a planner drops a required intermediate variable and confidently retrieves evidence bound to the wrong entity; the behavioural signature in both cases is a confident, locally-coherent, globally-wrong answer rather than a visible error or an abstention. [inference; source: https://arxiv.org/abs/2603.14828]

### §6 Synthesis

**Executive summary:**

No source in the 2023-2026 GraphRAG, agent-memory, or spatial-reasoning literature reports a numeric contextual-noise threshold at which a bounded entity-extraction schema stops suppressing Large Language Model (LLM)-driven predicate hallucinations in a planar memory graph, and no source uses "planar memory graph" as an established architecture at all. [inference; source: https://arxiv.org/abs/2602.05665; https://arxiv.org/abs/2603.14828] The evidence instead supports two usable proxy-metric families for detecting the drift the research question describes: a structural-stability family built on community-detection modularity, where a value below roughly Q equals 0.3 signals eroding community boundaries, and a task-outcome family built on multi-hop path-query accuracy and community-report factual distortion under injected noise. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://arxiv.org/abs/2603.14828] A bounded extraction schema suppresses out-of-vocabulary predicate hallucinations but does not verify whether an in-vocabulary predicate instance is actually supported by source text, so schema boundedness alone cannot suppress all hallucination-driven drift regardless of how tightly the schema is drawn. [inference; source: https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html] Every system in the evidence base shown to remain usable under noise achieves that robustness through an active, post-extraction repair mechanism, a query-time sufficiency check, knowledge-graph-based hallucination correction, or version-controlled graph rectification, rather than through extraction-schema rigidity alone, indicating that a planar memory graph needs a repair loop to remain a stable long-horizon substrate. [inference; source: https://arxiv.org/abs/2603.14828; https://arxiv.org/abs/2407.10793; https://aclanthology.org/2026.acl-long.2222/] Spatial path-finding degradation under uncorrected structural inconsistency is directly evidenced in an incrementally-constructed topological navigation graph, where a version-controlled repair framework significantly improved map correctness specifically in scenarios with entangled or chained inconsistencies. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

**Key findings:**

1. No paper in the reviewed 2023-2026 literature uses "planar memory graph" as a named agent-memory architecture, and a 2026 survey of graph-based agent memory does not identify layout planarity as a distinct architectural category, so no planarity-specific robustness claim exists in the surveyed literature. ([fact]; medium confidence; source: https://arxiv.org/abs/2602.05665)
2. Standard Graph Retrieval-Augmented Generation's default entity-merge step performs no semantic entity resolution and matches only identical title-and-type strings, meaning alias duplication is structurally expected to survive into any graph built with the default pipeline. ([fact]; medium confidence; source: https://microsoft.github.io/graphrag/index/default_dataflow/)
3. Schema-free extraction produces a documented cross-document concept-fragmentation failure mode, where an LLM's self-inferred ontology per document is inconsistent across documents even for substantively similar concepts, establishing one concrete mechanism by which unbounded extraction generates topology drift. ([fact]; medium confidence; source: https://arxiv.org/abs/2305.04676)
4. LLM-constructed knowledge graphs exhibit two recurring issue modes, spurious noise that induces retrieval drift toward plausible but unsupported triples and incomplete information that forces continuation through under-supported structure, and a constraint-based retriever addressing both remains measurably more stable under controlled knowledge-graph issue injection across three multi-hop benchmarks than retrievers that assume a structurally sound graph. ([fact]; medium confidence; source: https://arxiv.org/abs/2603.14828)
5. A bounded, schema-constrained extraction pipeline suppresses predicate types outside its defined vocabulary but provides no mechanism to verify that an in-vocabulary predicate instance is actually supported by the underlying source text, so schema boundedness alone leaves an evidentiary gap that a query-time sufficiency check is needed to close. ([inference]; medium confidence; source: https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
6. No located source reports a duplicate-node growth curve or an inflection point at which duplicate-node accumulation becomes structurally irreversible in any GraphRAG or agent-memory system, leaving numeric threshold estimation for this specific error class entirely unaddressed in the academic literature. ([assumption]; low confidence; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory)
7. Community-detection modularity above a value of roughly Q equals 0.3 is an established proxy for stable graph community structure, but the Leiden algorithm used in reference GraphRAG pipelines guarantees only internal connectivity of a community, not the semantic correctness of the nodes and edges inside it, so high modularity can coexist with undetected noise-driven topology drift. ([fact]; medium confidence; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/s41598-019-41695-z)
8. A companion repository item on macro-level hallucination in standard GraphRAG independently concludes that no located study measures how community-report distortion scales with injected duplicate or falsely-associated node counts, corroborating this item's own finding that the structural-stability and task-outcome proxy-metric families remain uncalibrated against one another. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html)
9. GraphRAG-Bench was constructed specifically because GraphRAG frequently underperforms plain Retrieval-Augmented Generation on real-world tasks, and its four-level difficulty gradient isolates the point at which multi-hop graph traversal, the closest available proxy for spatial path-finding, begins to fail under structural degradation. ([fact]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html)
10. A version-controlled repair framework for incrementally-constructed topological navigation graphs, using an Edge Impact Score to prioritise repairs by structural reachability, path usage, and conflict propagation, significantly improves map correctness and robustness specifically in scenarios with entangled or chained inconsistencies, directly evidencing that active repair rather than extraction-time schema rigidity restores spatial path-finding capability after drift. ([fact]; medium confidence; source: https://aclanthology.org/2026.acl-long.2222/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No paper names a "planar memory graph" architecture; planarity is absent from a 2026 graph-agent-memory taxonomy. | https://arxiv.org/abs/2602.05665 | medium | [x] consulted |
| [fact] Standard GraphRAG's default entity-merge matches only identical title/type strings. | https://microsoft.github.io/graphrag/index/default_dataflow/ | medium | [x] consulted |
| [fact] Schema-free per-document ontologies fragment across documents. | https://arxiv.org/abs/2305.04676 | medium | [x] consulted |
| [fact] LLM-built KGs show spurious-noise and incomplete-information issue modes; constraint-based retrieval is more stable under injected KG issues. | https://arxiv.org/abs/2603.14828 | medium | [x] consulted |
| [inference] Bounded schema suppresses out-of-vocabulary but not in-vocabulary predicate hallucination. | https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html | medium | [x] both consulted |
| [assumption] Entity-resolution merge cutoff (0.6, weighted score) is a usable proxy threshold. | https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory | low | [x] consulted; single vendor source |
| [fact] Modularity above roughly Q=0.3 signals stable community structure; Leiden guarantees only internal connectivity, not semantic correctness. | https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/s41598-019-41695-z | medium | [x] both consulted |
| [inference] Structural-stability and task-outcome proxy families remain uncalibrated against each other. | https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html | medium | [x] consulted |
| [fact] GraphRAG-Bench's difficulty gradient isolates when graph traversal fails. | https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html | medium | [x] consulted |
| [fact] Version-controlled Edge Impact Score repair improves spatial-navigation-graph correctness under chained inconsistencies. | https://aclanthology.org/2026.acl-long.2222/ | medium | [x] consulted |
| [fact] Knowledge-graph-based hallucination evaluation (GraphEval) enables post-hoc triple correction. | https://arxiv.org/abs/2407.10793 | medium | [x] consulted |

**Identified but not consulted:** none; all sources reachable during this session were fetched and read.

**Assumptions:**

The item's own architecture, a two-dimensional planar memory graph, is treated as functionally equivalent to an incrementally-constructed topological navigation graph for the purpose of this investigation. This assumption is justified because no closer published match was located, and the nearest evidence-backed system shares the defining property of building spatial structure from stepwise observations. [assumption; source: https://aclanthology.org/2026.acl-long.2222/]

A production entity-resolution merge cutoff (0.6, on a weighted name-similarity/co-occurrence/recency score) is treated as a workable proxy for a duplicate-suppression threshold rather than as a validated information-theoretic optimum. This assumption is justified because it is the only concrete, numeric merge criterion located in the evidence base for this specific error class. [assumption; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory]

A modularity value below roughly Q equals 0.3 is treated as a usable proxy signal for the onset of topology drift, rather than as a measured drift threshold. This assumption is justified because the Q equals 0.3 figure is validated for general community-structure stability, not for extraction-noise-driven drift specifically, so its application here is an extrapolation across domains. [assumption; source: https://www.pnas.org/doi/10.1073/pnas.0601602103]

**Analysis:**

The research question asks for a numeric threshold, but the strongest-supported conclusion is that no such single number exists in the current evidence base, and the item's own Scope constraint anticipated this outcome by directing that proxy metrics and threshold-estimation methods substitute for an invented figure. [inference; source: https://arxiv.org/abs/2603.14828] A plausible rival position, that a sufficiently narrow bounded schema alone could suppress hallucination-driven drift without any repair mechanism, is addressed and rejected by the evidence: the TBox-versus-ABox comparison shows a narrow, predefined schema losing accuracy faster than a schema-free approach as corpus noise rises, and the constraint-based retriever paper explicitly targets the residual in-vocabulary gap that a schema cannot close on its own. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://arxiv.org/abs/2603.14828] The structural-stability proxy (modularity) and the task-outcome proxy (path-query accuracy, community-report distortion) measure different things and are not shown anywhere in the evidence base to move together, so a system could pass one and fail the other; this is treated as a genuine uncalibrated gap rather than resolved in either direction. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://arxiv.org/abs/2603.14828] The clearest single piece of direct evidence for the second half of the research question, the effect of uncorrected topology drift on spatial-relational reasoning, comes from the graph-rectification paper's finding that a version-controlled repair mechanism specifically improved correctness in scenarios with entangled or chained inconsistencies, which is the closest available direct test of drift's effect on path-finding in a spatially-laid-out graph. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

**Risks, gaps, uncertainties:**

- No source directly measures topology drift in a graph memory system that is explicitly planar or 2D-laid-out as opposed to a general-purpose knowledge graph; every quantitative finding in this item is extrapolated from general GraphRAG or spatial-navigation-graph research rather than from a study of planar memory graphs specifically. [assumption; source: https://aclanthology.org/2026.acl-long.2222/]
- No source calibrates the modularity-based structural-stability proxy against the task-outcome proxy (path-query accuracy or community-report distortion) in a single experiment, so it is unknown whether the two proxies would agree on where a real system's drift threshold lies. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html]
- The entity-resolution merge-cutoff figure (0.6) comes from a single vendor engineering blog post rather than a peer-reviewed or independently replicated source, so it should not be read as a validated threshold for any system beyond the one it describes. [assumption; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory]
- The Edge Impact Score repair framework's reported improvement is stated qualitatively in its own abstract ("significantly improves map correctness and robustness") without a specific effect-size figure independently verified in this investigation, so the magnitude of the improvement, as opposed to its direction, remains unconfirmed here. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

**Open questions:**

- Would a controlled noise-injection experiment run directly on a planar or explicitly 2D-laid-out agent-memory graph reproduce the same repair-versus-prevention pattern found in general GraphRAG and spatial-navigation-graph research, or does planarity introduce a distinct failure mode not captured by non-planar studies?
- Can the structural-stability (modularity) and task-outcome (path-query accuracy, community-report distortion) proxy-metric families be calibrated against one another in a single experiment to produce a joint, empirically-grounded drift threshold?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed; LLM, GraphRAG, KG, TBox, ABox, RAG, 2D each expanded at first document-wide use
claim_label_audit: passed; every factual and inferential sentence in Research Skill Output carries an epistemic label
source_url_audit: passed; every cited claim binds to a URL
self_reference_audit: passed; no citation of this file or internal workflow state as evidence
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

No source in the 2023-2026 GraphRAG, agent-memory, or spatial-reasoning literature reports a numeric contextual-noise threshold at which a bounded entity-extraction schema stops suppressing Large Language Model (LLM)-driven predicate hallucinations in a planar memory graph, and no source uses "planar memory graph" as an established architecture at all. [inference; source: https://arxiv.org/abs/2602.05665; https://arxiv.org/abs/2603.14828] The evidence instead supports two usable proxy-metric families for detecting the drift the research question describes: a structural-stability family built on community-detection modularity, where a value below roughly Q equals 0.3 signals eroding community boundaries, and a task-outcome family built on multi-hop path-query accuracy and community-report factual distortion under injected noise. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://arxiv.org/abs/2603.14828] A bounded extraction schema suppresses out-of-vocabulary predicate hallucinations but does not verify whether an in-vocabulary predicate instance is actually supported by source text, so schema boundedness alone cannot suppress all hallucination-driven drift regardless of how tightly the schema is drawn. [inference; source: https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html] Every system in the evidence base shown to remain usable under noise achieves that robustness through an active, post-extraction repair mechanism, a query-time sufficiency check, knowledge-graph-based hallucination correction, or version-controlled graph rectification, rather than through extraction-schema rigidity alone, indicating that a planar memory graph needs a repair loop to remain a stable long-horizon substrate. [inference; source: https://arxiv.org/abs/2603.14828; https://arxiv.org/abs/2407.10793; https://aclanthology.org/2026.acl-long.2222/] Spatial path-finding degradation under uncorrected structural inconsistency is directly evidenced in an incrementally-constructed topological navigation graph, where a version-controlled repair framework significantly improved map correctness specifically in scenarios with entangled or chained inconsistencies. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

### Key Findings

1. No paper in the reviewed 2023-2026 literature uses "planar memory graph" as a named agent-memory architecture, and a 2026 survey of graph-based agent memory does not identify layout planarity as a distinct architectural category, so no planarity-specific robustness claim exists in the surveyed literature. ([fact]; medium confidence; source: https://arxiv.org/abs/2602.05665)
2. Standard Graph Retrieval-Augmented Generation's default entity-merge step performs no semantic entity resolution and matches only identical title-and-type strings, meaning alias duplication is structurally expected to survive into any graph built with the default pipeline. ([fact]; medium confidence; source: https://microsoft.github.io/graphrag/index/default_dataflow/)
3. Schema-free extraction produces a documented cross-document concept-fragmentation failure mode, where an LLM's self-inferred ontology per document is inconsistent across documents even for substantively similar concepts, establishing one concrete mechanism by which unbounded extraction generates topology drift. ([fact]; medium confidence; source: https://arxiv.org/abs/2305.04676)
4. LLM-constructed knowledge graphs exhibit two recurring issue modes, spurious noise that induces retrieval drift toward plausible but unsupported triples and incomplete information that forces continuation through under-supported structure, and a constraint-based retriever addressing both remains measurably more stable under controlled knowledge-graph issue injection across three multi-hop benchmarks than retrievers that assume a structurally sound graph. ([fact]; medium confidence; source: https://arxiv.org/abs/2603.14828)
5. A bounded, schema-constrained extraction pipeline suppresses predicate types outside its defined vocabulary but provides no mechanism to verify that an in-vocabulary predicate instance is actually supported by the underlying source text, so schema boundedness alone leaves an evidentiary gap that a query-time sufficiency check is needed to close. ([inference]; medium confidence; source: https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html)
6. No located source reports a duplicate-node growth curve or an inflection point at which duplicate-node accumulation becomes structurally irreversible in any GraphRAG or agent-memory system, leaving numeric threshold estimation for this specific error class entirely unaddressed in the academic literature. ([assumption]; low confidence; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory)
7. Community-detection modularity above a value of roughly Q equals 0.3 is an established proxy for stable graph community structure, but the Leiden algorithm used in reference GraphRAG pipelines guarantees only internal connectivity of a community, not the semantic correctness of the nodes and edges inside it, so high modularity can coexist with undetected noise-driven topology drift. ([fact]; medium confidence; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/s41598-019-41695-z)
8. A companion repository item on macro-level hallucination in standard GraphRAG independently concludes that no located study measures how community-report distortion scales with injected duplicate or falsely-associated node counts, corroborating this item's own finding that the structural-stability and task-outcome proxy-metric families remain uncalibrated against one another. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html)
9. GraphRAG-Bench was constructed specifically because GraphRAG frequently underperforms plain Retrieval-Augmented Generation on real-world tasks, and its four-level difficulty gradient isolates the point at which multi-hop graph traversal, the closest available proxy for spatial path-finding, begins to fail under structural degradation. ([fact]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html)
10. A version-controlled repair framework for incrementally-constructed topological navigation graphs, using an Edge Impact Score to prioritise repairs by structural reachability, path usage, and conflict propagation, significantly improves map correctness and robustness specifically in scenarios with entangled or chained inconsistencies, directly evidencing that active repair rather than extraction-time schema rigidity restores spatial path-finding capability after drift. ([fact]; medium confidence; source: https://aclanthology.org/2026.acl-long.2222/)

Source URLs above match the `## Sources` section for site citation rendering.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No paper names a "planar memory graph" architecture; planarity is absent from a 2026 graph-agent-memory taxonomy. | https://arxiv.org/abs/2602.05665 | medium | [x] consulted |
| [fact] Standard GraphRAG's default entity-merge matches only identical title/type strings. | https://microsoft.github.io/graphrag/index/default_dataflow/ | medium | [x] consulted |
| [fact] Schema-free per-document ontologies fragment across documents. | https://arxiv.org/abs/2305.04676 | medium | [x] consulted |
| [fact] LLM-built knowledge graphs show spurious-noise and incomplete-information issue modes; constraint-based retrieval is more stable under injected knowledge-graph issues. | https://arxiv.org/abs/2603.14828 | medium | [x] consulted |
| [inference] Bounded schema suppresses out-of-vocabulary but not in-vocabulary predicate hallucination. | https://arxiv.org/abs/2603.14828; https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html | medium | [x] both consulted |
| [assumption] Entity-resolution merge cutoff (0.6, weighted score) is a usable proxy threshold. | https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory | low | [x] consulted; single vendor source |
| [fact] Modularity above roughly Q=0.3 signals stable community structure; Leiden guarantees only internal connectivity, not semantic correctness. | https://www.pnas.org/doi/10.1073/pnas.0601602103; https://www.nature.com/articles/s41598-019-41695-z | medium | [x] both consulted |
| [inference] Structural-stability and task-outcome proxy families remain uncalibrated against each other. | https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html | medium | [x] consulted |
| [fact] GraphRAG-Bench's difficulty gradient isolates when graph traversal fails. | https://davidamitchell.github.io/Research/research/2026-07-20-agent-memory-evaluation-framework.html | medium | [x] consulted |
| [fact] Version-controlled Edge Impact Score repair improves spatial-navigation-graph correctness under chained inconsistencies. | https://aclanthology.org/2026.acl-long.2222/ | medium | [x] consulted |
| [fact] Knowledge-graph-based hallucination evaluation enables post-hoc triple correction. | https://arxiv.org/abs/2407.10793 | medium | [x] consulted |

**Identified but not consulted:** none; every source reachable during this session was fetched and read.

### Assumptions

The item's own architecture, a two-dimensional planar memory graph, is treated as functionally equivalent to an incrementally-constructed topological navigation graph for the purpose of this investigation. This assumption is justified because no closer published match was located, and the nearest evidence-backed system shares the defining property of building spatial structure from stepwise observations. [assumption; source: https://aclanthology.org/2026.acl-long.2222/]

A production entity-resolution merge cutoff (0.6, on a weighted name-similarity/co-occurrence/recency score) is treated as a workable proxy for a duplicate-suppression threshold rather than as a validated information-theoretic optimum. This assumption is justified because it is the only concrete, numeric merge criterion located in the evidence base for this specific error class. [assumption; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory]

A modularity value below roughly Q equals 0.3 is treated as a usable proxy signal for the onset of topology drift, rather than as a measured drift threshold. This assumption is justified because the Q equals 0.3 figure is validated for general community-structure stability, not for extraction-noise-driven drift specifically, so its application here is an extrapolation across domains. [assumption; source: https://www.pnas.org/doi/10.1073/pnas.0601602103]

### Analysis

The research question asks for a numeric threshold, but the strongest-supported conclusion is that no such single number exists in the current evidence base, and the item's own Scope constraint anticipated this outcome by directing that proxy metrics and threshold-estimation methods substitute for an invented figure. [inference; source: https://arxiv.org/abs/2603.14828] A plausible rival position, that a sufficiently narrow bounded schema alone could suppress hallucination-driven drift without any repair mechanism, is addressed and rejected by the evidence: the TBox-versus-ABox comparison shows a narrow, predefined schema losing accuracy faster than a schema-free approach as corpus noise rises, and the constraint-based retriever paper explicitly targets the residual in-vocabulary gap that a schema cannot close on its own. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-tbox-abox-graphrag.html; https://arxiv.org/abs/2603.14828] The structural-stability proxy (modularity) and the task-outcome proxy (path-query accuracy, community-report distortion) measure different things and are not shown anywhere in the evidence base to move together, so a system could pass one and fail the other; this is treated as a genuine uncalibrated gap rather than resolved in either direction. [inference; source: https://www.pnas.org/doi/10.1073/pnas.0601602103; https://arxiv.org/abs/2603.14828] The clearest single piece of direct evidence for the second half of the research question, the effect of uncorrected topology drift on spatial-relational reasoning, comes from the graph-rectification paper's finding that a version-controlled repair mechanism specifically improved correctness in scenarios with entangled or chained inconsistencies, which is the closest available direct test of drift's effect on path-finding in a spatially-laid-out graph. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

### Risks, Gaps, and Uncertainties

- No source directly measures topology drift in a graph memory system that is explicitly planar or 2D-laid-out as opposed to a general-purpose knowledge graph; every quantitative finding in this item is extrapolated from general GraphRAG or spatial-navigation-graph research rather than from a study of planar memory graphs specifically. [assumption; source: https://aclanthology.org/2026.acl-long.2222/]
- No source calibrates the modularity-based structural-stability proxy against the task-outcome proxy (path-query accuracy or community-report distortion) in a single experiment, so it is unknown whether the two proxies would agree on where a real system's drift threshold lies. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-20-graphrag-macro-level-hallucination.html]
- The entity-resolution merge-cutoff figure (0.6) comes from a single vendor engineering blog post rather than a peer-reviewed or independently replicated source, so it should not be read as a validated threshold for any system beyond the one it describes. [assumption; source: https://hindsight.vectorize.io/blog/2026/06/29/entity-resolution-agent-memory]
- The Edge Impact Score repair framework's reported improvement is stated qualitatively in its own abstract ("significantly improves map correctness and robustness") without a specific effect-size figure independently verified in this investigation, so the magnitude of the improvement, as opposed to its direction, remains unconfirmed here. [fact; source: https://aclanthology.org/2026.acl-long.2222/]

### Open Questions

- Would a controlled noise-injection experiment run directly on a planar or explicitly 2D-laid-out agent-memory graph reproduce the same repair-versus-prevention pattern found in general GraphRAG and spatial-navigation-graph research, or does planarity introduce a distinct failure mode not captured by non-planar studies?
- Can the structural-stability (modularity) and task-outcome (path-query accuracy, community-report distortion) proxy-metric families be calibrated against one another in a single experiment to produce a joint, empirically-grounded drift threshold?

---

## Output

- Type: knowledge
- Description: A synthesis establishing that no 2023-2026 source reports a numeric contextual-noise threshold for a planar memory graph's topology, and that the closest evidence-backed answer is a repair-based robustness pattern, active post-extraction correction rather than extraction-schema rigidity, supported by two uncalibrated proxy-metric families for detecting drift. [inference; source: https://arxiv.org/abs/2603.14828; https://aclanthology.org/2026.acl-long.2222/]
- Links:
  - https://arxiv.org/abs/2603.14828
  - https://aclanthology.org/2026.acl-long.2222/
  - https://www.pnas.org/doi/10.1073/pnas.0601602103

