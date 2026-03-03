---
title: "Knowledge Representation for Agent Context: LSE, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management"
added: 2026-03-03
status: backlog
priority: high
tags: [lse, lsa, knowledge-graphs, concept-maps, document-compression, context-management, rag, agents, knowledge-layering, intent-alignment, graphrag]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Knowledge Representation for Agent Context: LSE, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management

## Research Question

What techniques — latent semantic extraction, knowledge graphs, concept maps, hierarchical document compression, and layered abstraction — most effectively represent and compress large knowledge corpora (thousands of files) for retrieval-augmented agent systems operating under context-window constraints, and how should these techniques be combined so that agents can retrieve the right knowledge at the right level of abstraction for a given intent?

## Scope

**In scope:**
- Latent Semantic Analysis (LSA) / Latent Semantic Extraction (LSE): SVD-based dimensionality reduction of term-document matrices; construction of a compressed semantic space; document-to-document and query-to-document similarity in that space; relationship to modern dense embeddings
- Knowledge graphs as a knowledge management layer: entity and relation extraction from large corpora; graph construction strategies; community detection and hierarchical summarisation (GraphRAG pattern); graph traversal for intent-aligned context retrieval
- Concept maps: topological representations of a knowledge domain; differences from knowledge graphs (propositions vs. entities); use for navigability and agent-query alignment; automatic vs. manual construction
- Document compression strategies: extractive summarisation (sentence scoring, BM25-based salience), abstractive summarisation (LLM-based), hierarchical summarisation (multi-level abstract → section → paragraph); lossy vs. lossless trade-offs for agent consumption
- Knowledge layering and tiered abstraction: the principle that raw documents, extracted summaries, concept nodes, and graph communities are different abstraction levels; pull-based injection matching the required depth to the current task intent
- Context prioritisation under window constraints: intent-matching against knowledge layers; semantic proximity scoring; graph centrality-based ranking; recency weighting; combining multiple signals for priority ordering
- Relationship to this research corpus: can these techniques be applied to the `Research/completed/` item set at current and projected scale?

**Out of scope:**
- Full implementation of a search or RAG system (covered by `2026-03-02-semantic-full-text-search.md`)
- Low-level memory storage benchmarks and ephemeral/persistent memory classification (covered by `2026-03-02-agent-memory-management-context-injection.md`)
- Agent decision-making and DIKW integration (covered by `2026-03-02-integrative-framework-agent-decision-making.md`)
- Training-time knowledge encoding (fine-tuning, ROME/MEMIT weight editing)
- Real-time streaming knowledge updates

**Constraints:** Focus on techniques with published evidence of effectiveness at 100–10,000 document scale. Prefer implementations that remain local-first / open-source-compatible. Academic and practitioner sources both acceptable.

## Context

When an agent needs to reason over a large organisational knowledge base — regulations, policies, standards, prior decisions, domain knowledge — the naive approach of including all relevant files in the context window fails at scale. A 1,000-document corpus at typical document lengths exceeds any practical context window by an order of magnitude, and even if the window were large enough, the model has no principled way to prioritise competing signals buried in thousands of pages.

This is a distinct problem from context compression at the tool-output level (covered by `2026-03-01-context-mode-llm-context-compression.md`) and from memory injection at the session level (covered by `2026-03-02-agent-memory-management-context-injection.md`). Those items address what happens inside a running agent session. This item addresses the upstream problem: how to represent the knowledge base itself in a form that supports scalable, intent-aligned, precision retrieval before it ever enters the context window.

The techniques most directly relevant to this problem — LSA/LSE, knowledge graphs, concept maps, and hierarchical summarisation — share a common principle: they collapse high-dimensional, high-volume document corpora into navigable, low-dimensional structures that preserve semantic relationships. The agent's job then becomes not "read 1,000 files" but "traverse a graph / query an abstraction layer / select the right tier" — a tractable problem that fits within context windows.

This item grounds the knowledge-layer foundation that the integrative decision-making framework (`2026-03-02-integrative-framework-agent-decision-making.md`) requires. You cannot align agent intent with organisational knowledge if you have not first structured that knowledge in a navigable, compressible form.

## Approach

1. **LSA/LSE foundations and relevance to agent context** — Understand the core mechanism: term-document matrix → SVD → latent semantic space. What is preserved (semantic co-occurrence, topic coherence) and what is lost (exact term frequency, document structure)? How do LSA-derived representations compare to modern dense embeddings (sentence-transformers, Model2Vec) for agent context retrieval? What is the computational cost at 1,000–10,000 document scale? When does LSA outperform or complement embedding-based retrieval?

2. **Knowledge graphs: construction, structure, and retrieval** — Survey knowledge graph construction pipelines for agent context: entity and relation extraction (NLP-based, LLM-prompted); graph schemas; community detection algorithms (Leiden, Louvain); the GraphRAG pattern (Microsoft, 2024) — how it generates community summaries and uses them for global queries. Assess scalability and the cost of keeping the graph current as the knowledge base evolves. Compare local (subgraph retrieval) vs. global (community summary) query patterns.

3. **Concept maps: structure and navigability** — Define concept maps precisely (propositional networks where nodes are concepts and edges are labelled relationships, following Novak & Gowin). How do they differ from knowledge graphs? What are the construction approaches (manual expert elicitation, automated from text, LLM-assisted)? What does navigability mean for an agent — can an agent use a concept map as an index into deeper content? What tools and formats support machine-readable concept maps (CmapTools XML, RDF, JSON-LD)?

4. **Document compression and hierarchical summarisation** — Survey compression strategies that preserve agent-relevant information at multiple abstraction levels: (a) extractive: scoring sentences by information-theoretic salience, BM25 relevance to a query, or graph centrality in a local document graph; (b) abstractive: LLM-generated paragraph-level and document-level summaries; (c) hierarchical: multi-level abstractions (3-sentence executive summary → section-level summaries → full text). Assess quality degradation (information loss) and retrieval precision at each level.

5. **Knowledge layering: tiered abstraction as an architecture** — Define a layered knowledge architecture where each layer serves a different retrieval purpose: Layer 0 = raw documents; Layer 1 = extractive summaries (key sentences); Layer 2 = abstractive summaries (LLM-generated); Layer 3 = concept/graph nodes (entities, relationships, community summaries); Layer 4 = domain-level schema / ontology. Describe the pull-based injection model: agent determines required depth based on task intent, pulls from the appropriate layer. Assess how this maps to existing memory architectures (episodic, semantic, procedural) in agent systems.

6. **Context prioritisation under window constraints** — Given a query intent and a set of candidate knowledge items retrieved from multiple layers, what signals should rank them? Semantic proximity (embedding cosine similarity); graph centrality (PageRank, betweenness); recency (more recent items outrank older ones for dynamic knowledge); structural salience (executive summary > appendix); intent-type matching (regulatory query → regulation layer, procedural query → process layer). Survey research on combining these signals (RRF, learned rankers, LLM reranking).

7. **Synthesis and recommendations** — Produce a recommended architecture for a layered knowledge management system for agent context: which techniques to combine, at what scale thresholds each becomes necessary, what the construction and maintenance costs are, and how to phase the implementation (starting from current BM25 + embedding search, evolving toward knowledge graph + multi-tier abstraction).

## Sources

- [ ] Deerwester et al. (1990) "Indexing by latent semantic analysis" — original LSA paper: https://www.cs.bham.ac.uk/~pxt/IDA/lsa_ind.pdf
- [ ] Landauer, Foltz & Laham (1998) "Introduction to latent semantic analysis" — accessible conceptual overview: https://lsa.colorado.edu/papers/dp1.LSAintro.pdf
- [ ] Edge et al. (2024) "From Local to Global: A GraphRAG Approach to Query-Focused Summarization" — Microsoft GraphRAG: https://arxiv.org/abs/2404.16130
- [ ] GraphRAG GitHub + documentation: https://github.com/microsoft/graphrag
- [ ] Novak & Gowin (1984) *Learning How to Learn* — original concept map formulation (foundational reference for concept map structure)
- [ ] Novak (2010) "Learning, Creating, and Using Knowledge" — updated concept map theory: https://www.taylorfrancis.com/books/mono/10.4324/9780203862001
- [ ] CmapTools / IHMC concept mapping: https://cmap.ihmc.us — standard tool; assess machine-readability of format
- [ ] LlamaIndex knowledge graph integration: https://docs.llamaindex.ai/en/stable/examples/index_structs/knowledge_graph/ — practical agent implementation
- [ ] Neo4j + LLM integration patterns: https://neo4j.com/developer-blog/knowledge-graphs-llms-multi-hop-question-answering/
- [ ] Zep temporal knowledge graphs for agent memory: https://github.com/getzep/zep
- [ ] Cognee knowledge graph for AI memory: https://github.com/topoteretes/cognee
- [ ] RAPTOR (2024) "Recursive Abstractive Processing for Tree-Organized Retrieval" — hierarchical summarisation for RAG: https://arxiv.org/abs/2401.18059
- [ ] HippoRAG (2024) "Neurobiologically Inspired Long-Term Memory for Large Language Models": https://arxiv.org/abs/2405.14831
- [ ] Sarthi et al. (2024) RAPTOR: https://arxiv.org/abs/2401.18059 — tree-based recursive summarisation
- [ ] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — context compression at tool-output level; hybrid BM25+Model2Vec+sqlite-vec+RRF pattern (Key Finding 6)
- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — memory types and context injection; episodic/semantic/procedural memory architecture
- [ ] `Research/backlog/2026-03-02-semantic-full-text-search.md` — downstream consumer of search and retrieval findings
- [ ] `Research/backlog/2026-03-02-integrative-framework-agent-decision-making.md` — downstream consumer of knowledge representation findings; DIKW integration

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

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

- Type: knowledge, backlog-item
- Description: A structured comparison of LSE, knowledge graphs, concept maps, and hierarchical document compression as techniques for large-scale agent context management; a recommended layered knowledge architecture; and one or more follow-on backlog items for implementation (knowledge graph construction pipeline, concept map tooling, RAPTOR-style hierarchical summarisation for the research corpus)
- Links:
  - `Research/completed/2026-03-01-context-mode-llm-context-compression.md`
  - `Research/completed/2026-03-02-agent-memory-management-context-injection.md`
  - `Research/backlog/2026-03-02-semantic-full-text-search.md`
  - `Research/backlog/2026-03-02-integrative-framework-agent-decision-making.md`
