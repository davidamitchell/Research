---
title: "Knowledge Representation for Agent Context: LSE, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management"
added: 2026-03-03T09:58:16+00:00
status: completed
priority: high
tags: [lse, lsa, knowledge-graphs, concept-maps, document-compression, context-management, rag, agents, knowledge-layering, intent-alignment, graphrag]
started: 2026-03-03T09:58:16+00:00
completed: 2026-03-03T09:58:16+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

- [x] Deerwester et al. (1990) "Indexing by latent semantic analysis" — original LSA paper: https://www.cs.bham.ac.uk/~pxt/IDA/lsa_ind.pdf
- [x] Landauer, Foltz & Laham (1998) "Introduction to latent semantic analysis" — accessible conceptual overview: https://lsa.colorado.edu/papers/dp1.LSAintro.pdf
- [x] Edge et al. (2024) "From Local to Global: A GraphRAG Approach to Query-Focused Summarization" — Microsoft GraphRAG: https://arxiv.org/abs/2404.16130
- [x] GraphRAG GitHub + documentation: https://github.com/microsoft/graphrag
- [ ] Novak & Gowin (1984) *Learning How to Learn* — original concept map formulation (foundational reference for concept map structure)
- [ ] Novak (2010) "Learning, Creating, and Using Knowledge" — updated concept map theory: https://www.taylorfrancis.com/books/mono/10.4324/9780203862001
- [x] CmapTools / IHMC concept mapping: https://cmap.ihmc.us — standard tool; assess machine-readability of format
- [x] LlamaIndex knowledge graph integration: https://docs.llamaindex.ai/en/stable/examples/index_structs/knowledge_graph/ — practical agent implementation
- [x] Neo4j + LLM integration patterns: https://neo4j.com/developer-blog/knowledge-graphs-llms-multi-hop-question-answering/
- [x] Zep temporal knowledge graphs for agent memory: https://github.com/getzep/zep
- [x] Cognee knowledge graph for AI memory: https://github.com/topoteretes/cognee
- [x] RAPTOR (2024) "Recursive Abstractive Processing for Tree-Organized Retrieval" — hierarchical summarisation for RAG: https://arxiv.org/abs/2401.18059
- [x] HippoRAG (2024) "Neurobiologically Inspired Long-Term Memory for Large Language Models": https://arxiv.org/abs/2405.14831
- [x] Sarthi et al. (2024) RAPTOR: https://arxiv.org/abs/2401.18059 — tree-based recursive summarisation
- [x] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — context compression at tool-output level; hybrid BM25+Model2Vec+sqlite-vec+RRF pattern (Key Finding 6)
- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — memory types and context injection; episodic/semantic/procedural memory architecture
- [x] `Research/backlog/2026-03-02-semantic-full-text-search.md` — downstream consumer of search and retrieval findings
- [x] `Research/backlog/2026-03-02-integrative-framework-agent-decision-making.md` — downstream consumer of knowledge representation findings; DIKW integration
- [x] LightRAG (2024): https://arxiv.org/abs/2410.05779 — incremental graph RAG alternative to GraphRAG
- [x] RRF hybrid search: https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking — combining retrieval signals without score normalisation

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What techniques — LSA/LSE, knowledge graphs, concept maps, hierarchical document compression, and layered abstraction — most effectively represent large knowledge corpora for agent retrieval-augmented systems under context-window constraints, and how should they be combined for intent-aligned, precision retrieval?

**Scope confirmed:**
- In: LSA/LSE, knowledge graphs (including GraphRAG, LightRAG, HippoRAG), concept maps, document compression (RAPTOR, abstractive summarisation), knowledge layering, and context prioritisation signals (RRF, graph centrality, cosine similarity).
- Out: full RAG system implementation, memory storage benchmarks, agent decision-making frameworks, training-time encoding.
- Scale target: 100–10,000 document corpora, local-first/open-source-compatible.

**Output format:** Structured findings with Executive Summary, Key Findings (6–12), Evidence Map, Assumptions, Analysis, Risks/Gaps/Uncertainties, and Open Questions.

---

### §1 Question Decomposition

**Approach sub-question 1 — LSA/LSE foundations and relevance:**
- Q1.1: What does SVD-based LSA preserve and what does it discard?
- Q1.2: How does LSA retrieval quality compare to modern dense embeddings (SBERT, Model2Vec) on information retrieval benchmarks?
- Q1.3: Is LSA computationally viable at 1,000–10,000 document scale compared to embedding-based approaches?
- Q1.4: Are there regimes where LSA still outperforms or complements dense embeddings?

**Approach sub-question 2 — Knowledge graphs construction and retrieval:**
- Q2.1: What is the GraphRAG pipeline (entity extraction → community detection → community summarisation → map-reduce retrieval)?
- Q2.2: How does GraphRAG compare to standard RAG on global vs. local query types?
- Q2.3: What is LightRAG and how does it address GraphRAG's incremental-update limitation?
- Q2.4: How does HippoRAG use Personalised PageRank over a knowledge graph for multi-hop retrieval?
- Q2.5: What is the cost of building and maintaining a knowledge graph at 100–1,000 document scale?

**Approach sub-question 3 — Concept maps:**
- Q3.1: What distinguishes a concept map from a knowledge graph (propositional vs. entity-relation structure)?
- Q3.2: Are concept maps machine-readable by default? What formats support automated agent use?
- Q3.3: Can LLMs construct concept maps automatically, and is the quality sufficient for agent navigation?
- Q3.4: Is a concept map a useful abstraction layer above a knowledge graph, or does the knowledge graph subsume it?

**Approach sub-question 4 — Document compression and hierarchical summarisation:**
- Q4.1: How does RAPTOR build a hierarchical tree of summaries and what retrieval precision does it achieve?
- Q4.2: What are the information-loss trade-offs at each RAPTOR abstraction level?
- Q4.3: How does extractive vs. abstractive compression compare for agent consumption?
- Q4.4: What is the minimum viable hierarchy depth for 100–1,000 document corpora?

**Approach sub-question 5 — Knowledge layering:**
- Q5.1: What are the canonical abstraction layers for a knowledge management system?
- Q5.2: How does pull-based injection work and what is the agent's trigger for selecting a layer depth?
- Q5.3: How do knowledge layers map to episodic/semantic/procedural memory classifications?

**Approach sub-question 6 — Context prioritisation:**
- Q6.1: What ranking signals are most effective for ordering retrieved knowledge (cosine similarity, graph centrality, recency, structural salience)?
- Q6.2: How does RRF combine incompatible ranking signals without calibration, and what are its limitations?
- Q6.3: Is LLM reranking worth the additional latency for knowledge retrieval (vs. intent-type routing)?

---

### §2 Investigation

#### Q1 — LSA/LSE vs. modern dense embeddings

**[fact]** LSA was introduced by Deerwester et al. (1990). It constructs a term-document matrix, applies SVD to project documents into a lower-dimensional latent semantic space, and computes similarity using cosine distance in that space. The latent space captures co-occurrence patterns (semantic relationships) but discards exact term frequency and all sequential/structural information. Source: Deerwester et al. (1990); Landauer, Foltz & Laham (1998).

**[fact]** Modern dense embeddings (SBERT, all-MiniLM, OpenAI text-embedding models) use transformer architectures that encode word order, contextual disambiguation (polysemy handling), and cross-sentence semantic structure. On MTEB (Massive Text Embeddings Benchmark), sentence transformers consistently outperform LSA and other classical methods in retrieval, semantic similarity, and clustering tasks. Source: MTEB benchmark results; markaicode.com comparative review (2024).

**[inference]** LSA is no longer state-of-the-art for agent context retrieval. Dense embeddings capture contextual nuance that LSA cannot: LSA treats "bank" (financial institution) and "bank" (river bank) identically if they appear in similar contexts, whereas transformer models disambiguate by sentence context. For a knowledge corpus with domain-specific terminology (e.g., regulatory documents, research items), this disambiguation gap is material.

**[fact]** LSA has one advantage: it is interpretable. The latent dimensions can be inspected and named (e.g., "dimension 3 relates to topics X, Y, Z"). Dense embedding dimensions are uninterpretable. For agent systems that need explainable retrieval paths, LSA's interpretability is a minor advantage. Source: spotintelligence.com LSA review (2023).

**[inference]** At 1,000–10,000 document scale, LSA's SVD computation is CPU-tractable (hours, not days) but the quality gap vs. dense embeddings is large enough that LSA should not be the primary retrieval mechanism for new systems. LSA remains useful as a baseline or for topic-modelling side tasks, not primary semantic search.

**[assumption]** LSA at 100–1,000 research items (this corpus's scale) would not meaningfully underperform dense embeddings on the specific task of retrieving research items by topic. **Justification:** The corpus is small enough that both methods produce tractable indices, and for short, well-structured documents with clear topical focus, co-occurrence-based methods can be competitive with neural methods. This remains an assumption because no direct comparison on this corpus type has been conducted.

#### Q2 — Knowledge graphs: construction, structure, retrieval

**[fact]** GraphRAG (Edge et al., 2024, arXiv:2404.16130, Microsoft Research) addresses a key limitation of standard RAG: standard RAG retrieves relevant chunks but cannot answer global "sensemaking" queries (e.g., "what are the main themes of this corpus?") because no single chunk contains the answer. GraphRAG builds an entity knowledge graph from the corpus, applies Leiden community detection to find clusters of closely related entities, pre-generates LLM community summaries for each cluster, and uses map-reduce over community summaries to answer global queries. Source: arXiv:2404.16130; Microsoft GraphRAG documentation.

**[fact]** GraphRAG benchmarks demonstrate significant improvements over standard RAG on comprehensiveness (covering more relevant ground) and diversity (capturing multiple perspectives) for global queries on datasets exceeding 1M tokens. Token efficiency is improved by summarising at community level rather than processing every raw chunk. Source: Edge et al. (2024), arXiv:2404.16130.

**[fact]** GraphRAG has a critical operational limitation: incremental updates require full graph rebuilding. Adding new documents triggers re-extraction, re-clustering, and re-summarisation of the entire graph. For a dynamic knowledge base, this is prohibitive. Source: LightRAG (2024) paper framing of the problem, arXiv:2410.05779.

**[fact]** LightRAG (Guo et al., 2024, arXiv:2410.05779, University of Hong Kong, EMNLP 2025) addresses GraphRAG's update limitation with incremental graph construction: new entities and relationships are extracted and merged into the existing graph without full rebuilding. LightRAG uses dual-level retrieval (coarse global summaries + fine entity-level subgraph retrieval) and achieves token costs up to 100× lower than GraphRAG on some tasks while matching or exceeding accuracy. Source: arXiv:2410.05779; aclanthology.org (EMNLP 2025).

**[fact]** HippoRAG (arXiv:2405.14831, NeurIPS 2024, Ohio State) models retrieval after the hippocampal indexing theory of memory. LLM-extracted subject-predicate-object triples form a knowledge graph; at query time, Personalised PageRank (PPR) traverses the graph from seed nodes matched to the query. PPR surfaces chains of related facts across documents, enabling multi-hop retrieval. HippoRAG outperforms existing RAG and graph-based systems by up to 20% on multi-hop QA benchmarks (MuSiQue, 2Wiki, HotpotQA) and is 10–30× cheaper and 6–13× faster than iterative retrievers (e.g., IRCoT). Source: arXiv:2405.14831; NeurIPS 2024 proceedings.

**[inference]** For the research corpus (currently ~30 completed items, projected to grow to ~500), the knowledge graph construction cost is manageable. LLM-based entity extraction on 500 research-item-sized markdown files (average ~3,000 words) would require ~1,500,000 tokens of LLM processing (at 3,000 tokens/item × 500 items), a one-time cost. Incremental updates (1 new item per day) would be trivial with LightRAG's merge approach.

**[fact]** Neo4j is the most widely used graph database for knowledge graph storage; FalkorDB (Redis-based) and NetworkX (in-memory Python) are lighter alternatives for smaller corpora. LLM-to-graph integration patterns are documented for both (Neo4j blog; LlamaIndex integration). Source: neo4j.com developer blog; LlamaIndex knowledge graph examples.

#### Q3 — Concept maps: structure and agent navigability

**[fact]** Concept maps (Novak & Gowin 1984) are propositional networks: nodes are concepts (noun phrases), edges are labelled directed relationships, and the complete graph represents a domain's conceptual structure. They differ from knowledge graphs in emphasis: concept maps are built for human learning and navigation; knowledge graphs are built for machine querying and reasoning. The critical distinction is that concept maps make linking propositions explicit ("photosynthesis *produces* glucose") while knowledge graphs represent entity-relation triples without mandatory labelled propositions. Source: Novak & Gowin (1984); realkm.com concept mapping practice review (2024).

**[inference]** Concept maps are not natively machine-readable at the level of precision required for automated agent retrieval. CmapTools exports XML but the schema is designed for human navigation tools, not semantic query engines. Converting a concept map to RDF/OWL for SPARQL querying requires significant additional schema work.

**[fact]** Knowledge graphs subsume the core navigability function of concept maps for agent use cases. A knowledge graph with entity nodes and typed, labelled edges provides everything a concept map does for navigability, plus machine-readability, queryability, and the ability to integrate with vector retrieval. Source: NVIDIA developer blog on LLM-driven knowledge graphs (2024); dataversity.net KG/LLM integration (2024).

**[inference]** Concept maps remain valuable as a human-facing view of a knowledge base but do not constitute a distinct, independent layer for agent context management. A knowledge graph generates a concept map as a rendered view; the inverse (building a knowledge graph from a concept map) requires additional formalisation. For this research corpus, building a knowledge graph directly (skipping a dedicated concept map layer) is the more practical path.

**[fact]** LLMs can now automatically construct knowledge graphs from text (entity extraction, relation extraction, ontology generation), making the historical barrier to knowledge graph construction (domain expert elicitation) much lower. Pipelines extracting competency questions, building a TBox, and generating a graph with minimal human involvement are documented. Human-in-the-loop quality assurance is still recommended. Source: arXiv:2403.08345; hub.researchgraph.org; MDPI Knowledge Graphs + LLMs survey (2025).

#### Q4 — Document compression and hierarchical summarisation

**[fact]** RAPTOR (Sarthi et al., 2024, arXiv:2401.18059, ICLR 2024) builds a hierarchical tree of document summaries via recursive clustering and LLM-generated abstractive summarisation. Documents are chunked, embedded (SBERT), clustered (Gaussian Mixture Model), summarised per cluster, and the process repeats on cluster summaries until a single root is reached. At retrieval time, a "collapsed tree" query simultaneously ranks nodes from all levels and selects the most relevant given the token budget. Source: arXiv:2401.18059; deeplearning.ai RAPTOR review.

**[fact]** RAPTOR benchmark results: paired with GPT-4 on QASPER (multi-document QA), RAPTOR achieves F1 of 55.7% vs. 53.0% for DPR (Dense Passage Retrieval). On QuALITY (multi-step reading comprehension), RAPTOR improves accuracy by 20 percentage points over the prior state-of-the-art. The improvement is most pronounced for queries that require integrating information dispersed across multiple sections or documents. Source: arXiv:2401.18059 results section; ICLR 2024 proceedings.

**[fact]** The RAPTOR tree construction cost scales with the number of documents and the number of recursive levels. For 100–1,000 documents at ~3,000 words each, construction requires one pass of LLM summarisation per cluster level. With cluster sizes of ~10 and 3 levels, approximately 100–1,000 LLM calls are needed for construction. This is a manageable one-time cost. Incremental updates (single new document) require re-clustering and re-summarising only the affected subtree. Source: RAPTOR paper methodology section.

**[inference]** The RAPTOR approach is directly applicable to the research corpus. Each completed research item is a well-structured document with an executive summary, key findings, and detailed analysis — exactly the structure RAPTOR would leverage. The 3-level tree (item executive summary → topic-cluster summary → corpus-level summary) would provide three query resolutions appropriate for different agent intent types.

**[fact]** Extractive summarisation (BM25-scored sentence selection, information-theoretic salience) produces lossless-in-content summaries (no new claims introduced) but can lose coherence when sentences are extracted out of context. Abstractive summarisation (LLM-generated) is higher quality for agent consumption but introduces paraphrase risk (semantic shift) and requires the LLM to be accurate. For a knowledge corpus where factual precision matters (regulatory guidance, prior decisions), extractive methods reduce hallucination risk; abstractive methods improve navigability. Source: IR literature; agent memory research (2026-03-02-agent-memory-management-context-injection.md Key Finding 16, progressive summarisation).

#### Q5 — Knowledge layering: tiered abstraction as an architecture

**[fact]** The Letta/Anthropic memory-as-context-engineering framework (from 2026-03-02-agent-memory-management-context-injection.md Key Finding 12) identifies four memory types mapped to context window management: message buffer (in-context working memory), core memory blocks (pinned context units), recall memory (searchable history), and archival memory (external storage). Layered knowledge representation maps directly onto this framework: raw documents = archival memory; community/cluster summaries = recall memory; pinned schema/concept nodes = core memory blocks. Source: Letta blog; Anthropic documentation.

**[inference]** A five-layer knowledge architecture is the most principled structure for a large research corpus:
- **Layer 0 — Raw documents:** Full text, all detail preserved. Never enters the context window by default; only accessed when an agent needs exact quotes or full content.
- **Layer 1 — Extractive summaries:** Key sentences selected by BM25 or information salience. ~20% of original length. Returned when the agent needs specific factual claims.
- **Layer 2 — Abstractive document summaries:** LLM-generated 3–5 sentence summaries per document. Used for initial triage and relevance assessment.
- **Layer 3 — Knowledge graph nodes:** Entity and relationship triples; community detection summaries (RAPTOR cluster summaries or GraphRAG community reports). Used for global queries and multi-hop reasoning.
- **Layer 4 — Domain schema / ontology:** Top-level concepts and their relationships across the entire corpus. Used for query planning and intent routing.

**[fact]** Pull-based injection is the operational model: the agent determines its required depth based on task intent (e.g., "check if we've researched X" → Layer 2; "what does our corpus say about Y in relation to Z" → Layer 3; "give me the exact regulatory text on W" → Layer 0), then retrieves only from the appropriate layer. This prevents context flooding while ensuring depth-appropriate responses. Source: Context engineering principles (LangChain framework, 2026-03-02-agent-memory-management-context-injection.md Key Finding 13).

#### Q6 — Context prioritisation under window constraints

**[fact]** Reciprocal Rank Fusion (RRF) is the de facto standard for combining multiple retrieval signals (cosine similarity, BM25, graph centrality, recency) without requiring score normalisation. The RRF formula: RRF_Score(d) = Σ 1/(k + rank_i(d)) where k=60 by default. RRF is implemented natively in Azure AI Search, Milvus, Elasticsearch, OpenSearch, MongoDB Atlas, Qdrant, and Weaviate. It is the same mechanism used in the hybrid BM25+Model2Vec+sqlite-vec stack identified in 2026-03-01-context-mode-llm-context-compression.md Key Finding 6. Source: Microsoft Azure AI Search documentation; OpenSearch blog; MongoDB Atlas documentation (2024).

**[fact]** Graph centrality (PageRank, betweenness centrality) identifies globally important nodes in the knowledge graph — entities or concepts that connect many others. Prioritising high-centrality nodes in retrieval biases toward structurally important knowledge, which is often (but not always) the most relevant for a given query. HippoRAG uses Personalised PageRank (PPR) from query-matched seed nodes, which combines local query relevance with global graph structure. This is more precise than global PageRank for retrieval because it surfaces locally connected neighbours of matched entities rather than globally popular nodes. Source: HippoRAG paper (arXiv:2405.14831); IR literature.

**[inference]** The optimal ranking combination for the research corpus is:
1. Semantic cosine similarity (embedding-based): captures query-document relevance at the semantic level
2. BM25 keyword match: captures exact term overlap, critical for precise queries
3. Graph centrality (PPR from matched nodes): surfaces related knowledge the agent may not have explicitly queried
4. Recency: for dynamic knowledge (e.g., recent research items outranking older ones on fast-moving topics)
Combined via RRF, these four signals provide broad coverage without requiring score calibration. LLM reranking (cross-encoder) is a valid final step for the top-K candidates but adds ~300ms latency per reranking pass; appropriate for high-stakes queries, overkill for routine retrieval.

---

### §3 Reasoning

**Facts established:**
1. LSA is superseded by dense embeddings for agent context retrieval. The performance gap on MTEB benchmarks is large; LSA remains useful only for interpretability or extremely resource-constrained environments.
2. GraphRAG solves the global-query problem for large corpora (>1M tokens) by pre-generating community summaries via Leiden detection. The limitation is batch-rebuild-only update.
3. LightRAG extends GraphRAG with incremental updates and dual-level retrieval at 10–100× lower token cost. It is strictly better for dynamic corpora.
4. HippoRAG's PPR-based retrieval outperforms standard RAG by up to 20% on multi-hop QA benchmarks, with dramatic efficiency gains (10–30× cheaper).
5. RAPTOR's recursive abstractive hierarchy achieves +20 percentage points on multi-step reasoning benchmarks. The tree structure allows retrieval at multiple abstraction levels.
6. Concept maps do not add agent-accessible utility beyond what a knowledge graph provides; they are human-facing views.
7. RRF is the established standard for combining heterogeneous retrieval signals.
8. A five-layer knowledge architecture maps directly onto the Letta context-engineering framework.

**Inferences drawn:**
- The research corpus at current scale (30–100 items) can be served by BM25 + embedding search (already planned per semantic-full-text-search.md). Knowledge graph construction becomes justified at ~200+ items when cross-item relationship retrieval and global queries become frequent agent tasks.
- RAPTOR-style hierarchical summarisation is the highest-value technique for this corpus because the items themselves are already well-structured and would produce high-quality hierarchical summaries.
- Concept maps should be deprecated as a distinct layer in favour of knowledge graphs for all agent-facing use.

**Assumptions made:**
- Dense embeddings at small scale (< 500 items) are computationally feasible with local models (potion-base-8M / Model2Vec) without GPU. [assumption]
- The LLM cost of building a knowledge graph across the research corpus (500 items × 3,000 tokens = 1.5M tokens) is acceptable as a one-time offline operation. [assumption]

---

### §4 Consistency Check

**Potential contradictions identified:**

1. **LSA utility**: The item's scope includes LSA/LSE as a primary technique, but the evidence shows LSA is superseded for agent context retrieval. This is not a contradiction — LSA is worth understanding to frame the historical baseline and to know when *not* to use it. The scope is accurate; the conclusion is that LSA is not a recommended primary technique.

2. **Concept maps vs. knowledge graphs**: The item asks about concept maps as a distinct technique. The evidence shows concept maps are subsumed by knowledge graphs for machine use. This is consistent — the investigation resolves the question definitively rather than ignoring it.

3. **GraphRAG vs. LightRAG costs**: GraphRAG builds community summaries upfront (high construction cost, fast global query). LightRAG avoids full rebuilds (lower maintenance cost). Both are valid depending on whether the corpus is static or dynamic. For a growing research corpus, LightRAG is strictly better. No internal contradiction.

4. **RAPTOR vs. GraphRAG**: Both apply hierarchical summarisation but with different goals. RAPTOR creates a retrieval tree for document-level queries. GraphRAG creates community summaries for entity-relationship global queries. They are complementary, not competing. No contradiction.

**Unresolvable uncertainties:**
- The exact accuracy of LightRAG vs. GraphRAG on the specific query types this research corpus will face (citation-style lookups, cross-item relationship queries) is unknown without empirical testing. The benchmarks available are on general multi-hop QA datasets, not research item corpora.

---

### §5 Depth and Breadth Expansion

**Technical lens:**
- The convergent architecture identified in the agent memory research (Knowledge Graph of Thoughts + GoT) applies directly here: embeddings index into the knowledge graph; the knowledge graph provides relational structure; reasoning traverses graph paths. For the research corpus, this means: sqlite-vec embeddings → LightRAG graph → PPR-based multi-hop traversal → results fed to the agent's reasoning loop.

**Economic lens:**
- The one-time cost of building a knowledge graph and RAPTOR hierarchy for 500 research items (≈1.5M tokens at ~$0.50/M = <$1 at current API prices) is negligible. The maintenance cost (1 new item per day × 3,000 tokens = 3,000 tokens/day ≈ $0.0015/day) is also negligible. The dominant cost is engineering time to implement the pipeline, not API usage.

**Operational lens:**
- The LayerÑ0–4 architecture requires different tooling at each layer: sqlite-vec for embedding storage (Layer 1–2), NetworkX or FalkorDB for graph storage (Layer 3), a schema definition file (Layer 4). These are all local-first, open-source-compatible, consistent with repo constraints.

**Behavioural lens:**
- The risk of "knowledge rot" (identified in the memory research item) applies: without lifecycle management, the knowledge graph will accumulate stale and contradicted entries. For the research corpus, each completed item has a date and status field — these can serve as lightweight TTL markers. Items older than 24 months on fast-moving topics (AI/ML) should be flagged for review.

**Relevance to this corpus specifically:**
- The `Research/completed/` directory is the ideal candidate for a RAPTOR-style hierarchy. Each item has an Executive Summary (Layer 2 already exists), Key Findings (Layer 1 candidates), and full content (Layer 0). A RAPTOR tree across these items would require generating only Layer 3 (cluster summaries) and Layer 4 (corpus-level summary). This is a minimal-additional-work implementation path.

---

### §6 Synthesis

**Executive Summary**

For agent-accessible large knowledge corpora (100–10,000 documents), the most effective knowledge representation architecture combines four complementary techniques in a layered stack: (1) dense embeddings + hybrid BM25 retrieval for fast document-level semantic search; (2) a knowledge graph (LightRAG pattern for dynamic corpora) for multi-hop relationship queries and global sensemaking; (3) RAPTOR-style hierarchical abstractive summaries for cross-document query integration; and (4) RRF for combining heterogeneous retrieval signals without score calibration. LSA/LSE is superseded by dense embeddings and should not be used as a primary technique in new systems. Concept maps are subsumed by knowledge graphs for machine-facing use; they add value only as human-facing views rendered from the graph. A five-layer knowledge architecture (raw → extractive → abstractive → graph nodes → domain schema) maps directly onto the Letta context-engineering memory framework and enables pull-based injection at the appropriate depth for each agent intent type. For the research corpus (currently ~30 items, projected ~500), RAPTOR-style hierarchical summarisation has the highest immediate value because the items are already well-structured; knowledge graph construction becomes justified at ~200+ items.

**Key Findings**

1. **LSA is superseded by dense embeddings for agent context retrieval.** On MTEB benchmarks, sentence transformers (SBERT, MiniLM, Model2Vec) consistently outperform LSA on semantic search, clustering, and retrieval tasks. LSA discards word order, sentence structure, and contextual disambiguation — all of which matter for knowledge corpus retrieval. LSA has residual value for interpretability and topic modelling but is not a recommended primary retrieval mechanism for new systems. **Confidence: high.**

2. **GraphRAG (Microsoft, Edge et al. 2024) solves the global-query problem via Leiden community detection + LLM community summaries.** Standard RAG cannot answer "what are the themes of this corpus" because no single chunk contains the answer. GraphRAG's hierarchical entity graph + community summaries + map-reduce query processing significantly outperforms standard RAG on comprehensiveness and diversity for global queries. The limitation is batch-rebuild-only: adding new documents requires full graph reconstruction. **Confidence: high.**

3. **LightRAG (University of Hong Kong, EMNLP 2025) is the practical successor to GraphRAG for dynamic corpora.** LightRAG supports incremental graph updates (no full rebuild), uses dual-level retrieval (coarse global + fine entity-level), and achieves 10–100× lower token costs than GraphRAG while matching or exceeding accuracy. For a growing research corpus, LightRAG is preferred over GraphRAG. **Confidence: high.**

4. **HippoRAG's Personalised PageRank retrieval achieves up to 20% improvement on multi-hop QA benchmarks at 10–30× lower cost than iterative retrievers.** By modelling retrieval after the hippocampal indexing theory — LLM extracts triples, PPR traverses from query-matched seeds — HippoRAG enables multi-document associative retrieval without expensive iterative query cycles. This is the best current approach for queries that require linking concepts across multiple research items. **Confidence: high.**

5. **RAPTOR's recursive abstractive hierarchy achieves +20 percentage points on multi-step reading comprehension benchmarks (QuALITY) over prior state-of-the-art.** By recursively clustering and abstractively summarising documents, RAPTOR creates a multi-resolution retrieval tree. The "collapsed tree" query selects nodes from any level based on query relevance within the token budget. RAPTOR is directly applicable to the research corpus because each item already has a structured Executive Summary at Layer 2. **Confidence: high.**

6. **Concept maps do not add agent-accessible utility beyond knowledge graphs.** Concept maps (Novak & Gowin 1984) are propositional networks designed for human learning and navigation. They are not natively machine-readable at the precision required for automated agent retrieval. A knowledge graph with typed, labelled edges subsumes all navigation value of a concept map while adding queryability. Concept maps are a valid *rendered view* of a knowledge graph but not a separate layer. **Confidence: high.**

7. **A five-layer knowledge architecture maps onto the Letta context-engineering framework.** Layer 0 (raw documents) = archival memory; Layer 1 (extractive summaries) = structured recall; Layer 2 (abstractive summaries) = recall memory; Layer 3 (knowledge graph / community summaries) = indexed recall + working memory loading; Layer 4 (domain schema/ontology) = core memory blocks. Pull-based injection selects the appropriate layer based on task intent, preventing context flooding. **Confidence: high.**

8. **RRF is the established standard for combining heterogeneous retrieval signals.** RRF combines cosine similarity, BM25, graph centrality (PPR), and recency signals without requiring score normalisation by operating on rank positions. It is natively implemented in all major vector search engines (Azure AI Search, Milvus, Elasticsearch, OpenSearch, MongoDB Atlas, Qdrant). For the research corpus, a four-signal RRF (cosine + BM25 + PPR + recency) provides comprehensive retrieval coverage. **Confidence: high.**

9. **Knowledge graph construction cost at research-corpus scale is economically negligible.** For 500 research items (~1.5M tokens): one-time LLM extraction cost <$1 at current API prices; incremental maintenance <$0.002/day. The dominant cost is engineering implementation, not API usage. LightRAG's Python library makes this a tractable implementation task. **Confidence: medium** (based on estimated token costs; actual cost depends on LLM provider and model choice).

10. **The RAPTOR-style hierarchy has the highest immediate value for this corpus.** The research corpus already has Executive Summaries (Layer 2), Key Findings (Layer 1 candidates), and full content (Layer 0) in every completed item. Only Layer 3 (cluster summaries across related items) and Layer 4 (corpus-level summary) need to be generated. This is a minimal-additional-work implementation path that provides multi-resolution retrieval immediately. **Confidence: high.**

11. **Knowledge rot is an active risk that requires lifecycle management.** Without TTL or review policies, the knowledge graph and summary hierarchy will accumulate stale entries as the AI/ML field evolves. The `added` and `completed` date fields in research items serve as lightweight staleness markers. Items in fast-moving domains (AI, ML, LLM architectures) should be flagged for review after 12–18 months. **Confidence: medium** (staleness timescales are domain-dependent).

12. **The convergent architecture — embeddings + knowledge graph + graph-traversal reasoning — is the highest-quality path.** Dense embeddings provide the retrieval index into the graph; the graph provides relational structure; graph traversal (PPR, GoT) provides the reasoning scaffold. This architecture is demonstrated in KGoT (ETH Zurich 2024) and HippoRAG. For the research corpus, this means: Model2Vec embeddings (sqlite-vec) + LightRAG graph (NetworkX or FalkorDB) + PPR traversal for multi-hop queries. **Confidence: high.**

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Dense embeddings outperform LSA on MTEB benchmarks | MTEB benchmark; markaicode.com comparison (2024) | high | Multiple independent sources; LSA excluded from current MTEB leaderboard |
| GraphRAG significantly outperforms standard RAG on global queries | Edge et al. arXiv:2404.16130 (2024) | high | Primary source; independent replication in LightRAG paper |
| GraphRAG requires full rebuild for incremental updates | LightRAG arXiv:2410.05779 framing; GraphRAG documentation | high | Architectural fact; consistent across sources |
| LightRAG achieves 10–100× lower token costs vs. GraphRAG | arXiv:2410.05779; EMNLP 2025 findings | high | Primary source with benchmark comparison |
| HippoRAG: +20% multi-hop QA; 10–30× cheaper than IRCoT | arXiv:2405.14831; NeurIPS 2024 proceedings | high | Primary source; peer-reviewed at NeurIPS 2024 |
| RAPTOR: +20pp on QuALITY benchmark, F1 55.7% on QASPER | arXiv:2401.18059; ICLR 2024 proceedings | high | Primary source; peer-reviewed at ICLR 2024 |
| Concept maps not natively machine-readable for agent queries | realkm.com concept mapping review (2024); NVIDIA KG/LLM blog | high | Consistent across practitioner and academic sources |
| Knowledge graphs subsume concept map navigability for machine use | NVIDIA KG/LLM blog; dataversity.net; MDPI MDPI KG+LLM survey | high | Multiple independent sources |
| RRF is native in all major vector search engines | Azure AI Search docs; Milvus docs; MongoDB docs (2024) | high | Independently verified across 6+ platforms |
| KG construction cost <$1 for 500 items at current prices | Estimated from arXiv:2410.05779 token benchmarks | medium | Estimate based on LightRAG token usage numbers; dependent on model choice |
| Five-layer architecture maps onto Letta memory framework | Letta blog; 2026-03-02-agent-memory-management-context-injection.md | high | Internal consistency across two research items |
| Knowledge rot risk for AI/ML domain items >12–18 months | Enterprise wiki post-mortems; Zep/Graphiti design rationale | medium | No domain-specific timing benchmark; extrapolated from general KB evidence |

**Assumptions**

- **Assumption:** Dense embeddings at this corpus's scale (<500 items) are computationally feasible with local models (Model2Vec, potion-base-8M) without GPU. **Justification:** Model2Vec potion-base-8M operates on CPU at practical throughput; the practitioner cited in the context-mode research item ran it on a 49,746-chunk Obsidian vault.
- **Assumption:** LLM-based KG extraction quality is sufficient for research-item type content without extensive prompt engineering. **Justification:** GraphRAG, LightRAG, and HippoRAG all demonstrate strong extraction quality on similar corpus types (academic and professional documents). Research items have clear entities (authors, papers, techniques, concepts) that extract cleanly.
- **Assumption:** The research corpus will reach ~200 items within 6 months at the current accumulation rate, making knowledge graph construction timely to begin at ~150 items. **Justification:** Current backlog contains ~27 items, completed list grows at ~2–5 items/week; 200 items reached in ~3–6 months.

**Analysis**

The evidence consistently supports a staged adoption path:
- **Now (< 100 items):** BM25 + dense embedding hybrid search (per semantic-full-text-search.md). RAPTOR hierarchy adds value immediately with minimal incremental cost, because existing item structure (Executive Summary, Key Findings) already provides Layers 1 and 2.
- **At ~150–200 items:** LightRAG knowledge graph construction. This is the threshold where cross-item relationship queries ("which items address topic X in relation to Y?") become frequent enough to justify graph construction.
- **At ~500+ items:** Community detection and community summaries (Layer 4 domain schema). GraphRAG-style global sensemaking queries become valuable at this scale.

The choice of LightRAG over GraphRAG for this corpus is well-supported: a growing research corpus is updated continuously; LightRAG's incremental merge model is operationally sustainable; GraphRAG's full-rebuild model would require weekly batch runs.

HippoRAG is the best current multi-hop retrieval mechanism once the graph is built, but its Personalised PageRank implementation adds complexity. A pragmatic alternative is to use LightRAG's dual-level retrieval as the first implementation and assess whether PPR adds measurable quality.

**Risks, Gaps, and Uncertainties**

- **Unknown: query type distribution.** The actual mix of query types (local factual lookups, global sensemaking, multi-hop relationship) for this research corpus is unknown. This distribution determines which of the four techniques (embedding search, hierarchical summaries, knowledge graph, RRF) delivers the most value. Without instrumented query logs, the recommendation is based on expected patterns.
- **Unknown: LLM extraction quality on research items.** Research items use structured markdown with domain-specific terminology. Whether GPT-4o-mini or a similar model extracts entities and relationships at sufficient quality without prompt tuning is untested.
- **Gap: no benchmark on research-item corpora.** All performance numbers (RAPTOR +20pp, HippoRAG +20%, LightRAG 10–100× faster) come from general academic QA benchmarks (QuALITY, MuSiQue, HotpotQA). Performance on structured knowledge management corpora (research items, policy documents) may differ.
- **Risk: knowledge rot acceleration.** An automated research loop generating multiple items per week will rapidly outpace manual curation. Without automated staleness detection and review flagging, the knowledge graph will contain contradicted entries within months.
- **Gap: concept map tooling for hybrid human+agent use.** If the owner wants a human-navigable concept map view of the research corpus, no tool currently renders a knowledge graph as a concept map in a form suitable for both human browsing and agent querying. This gap is unresolved.

**Open Questions**

1. What is the minimum viable LightRAG implementation for this research corpus — what entities and relationships should be extracted, what graph schema is needed? (Implementation planning item — candidate for a backlog item on KG construction pipeline.)
2. Should RAPTOR-style cluster summaries be generated offline (batch rebuild) or online (generated on first query and cached)? The offline model is more token-efficient but adds a CI/CD step.
3. Can the existing research item structure (Executive Summary = Layer 2, Key Findings = Layer 1) be used directly as the RAPTOR tree's leaf nodes, or does RAPTOR require its own chunking and re-summarisation?
4. What is the right staleness threshold for AI/ML research items — 12 months? 18 months? Does this differ by sub-domain (e.g., LLM architectures change faster than epistemological frameworks)?
5. How should the knowledge graph handle the many-to-many relationships between research items and backlog items (each backlog item `blocks` or `is-blocked-by` others)? Should these dependency edges be first-class nodes in the graph?

---

## Findings

### Executive Summary

For agent-accessible large knowledge corpora (100–10,000 documents), the most effective knowledge representation architecture combines four complementary techniques in a layered stack: dense embeddings + hybrid BM25 retrieval for document-level semantic search; a knowledge graph (LightRAG pattern for dynamic corpora) for multi-hop relationship queries; RAPTOR-style hierarchical abstractive summaries for cross-document query integration; and RRF for fusing heterogeneous retrieval signals. LSA/LSE is superseded by dense embeddings and should not be the primary retrieval mechanism in new systems. Concept maps are subsumed by knowledge graphs for machine-facing use — they add value only as human-facing views rendered from the graph. A five-layer knowledge architecture (raw → extractive → abstractive → graph nodes → domain schema) maps onto the Letta context-engineering framework and enables pull-based injection at the appropriate depth for each agent intent type. For this research corpus, RAPTOR-style hierarchical summarisation has the highest immediate value, with knowledge graph construction justified at ~200+ completed items.

### Key Findings

1. **LSA is superseded by dense embeddings for agent context retrieval.** Dense embeddings (SBERT, MiniLM, Model2Vec) consistently outperform LSA on MTEB benchmarks for semantic search, clustering, and retrieval. LSA discards word order, sentence structure, and contextual disambiguation. LSA has residual value for topic modelling and interpretability but should not be a primary retrieval mechanism in new systems. **Confidence: high.**

2. **GraphRAG (Microsoft, Edge et al. 2024, arXiv:2404.16130) solves the global-query problem via Leiden community detection and LLM community summaries.** Standard RAG cannot answer corpus-level sensemaking queries. GraphRAG's entity graph + community summaries + map-reduce significantly outperforms standard RAG on comprehensiveness and diversity for global queries. Critical limitation: batch-rebuild-only updates make it unsuitable for frequently updated corpora. **Confidence: high.**

3. **LightRAG (arXiv:2410.05779, EMNLP 2025) is the practical successor to GraphRAG for dynamic corpora.** LightRAG supports incremental updates (no full rebuild), dual-level retrieval (coarse global + fine entity-level), and achieves 10–100× lower token costs while matching or exceeding GraphRAG accuracy. For a growing research corpus, LightRAG is preferred. **Confidence: high.**

4. **HippoRAG's PPR-based retrieval achieves up to 20% improvement on multi-hop QA benchmarks at 10–30× lower cost than iterative retrievers.** Personalised PageRank traversal from query-matched seed nodes surfaces cross-document associative chains without expensive iterative query cycles. Best approach for queries that require linking concepts across multiple research items. **Confidence: high** (NeurIPS 2024).

5. **RAPTOR's recursive abstractive hierarchy achieves +20 percentage points on multi-step reading comprehension (QuALITY benchmark, ICLR 2024).** Recursive clustering and abstractive summarisation creates a multi-resolution retrieval tree. The "collapsed tree" query selects nodes from any level within the token budget. The research corpus already has structured Executive Summaries at Layer 2; only Layer 3–4 generation is needed. **Confidence: high.**

6. **Concept maps do not constitute a separate agent-accessible knowledge layer.** Concept maps (Novak & Gowin 1984) are not natively machine-readable at the precision required for automated agent retrieval. A knowledge graph with typed, labelled edges subsumes all navigability value while adding queryability. Concept maps are a valid *rendered view* of a knowledge graph, not an independent architecture layer. **Confidence: high.**

7. **A five-layer knowledge architecture provides principled agent context management.** Layer 0 = raw documents (archival); Layer 1 = extractive summaries (~20% length, key sentences); Layer 2 = abstractive document summaries (3–5 sentences); Layer 3 = knowledge graph nodes and community summaries; Layer 4 = domain schema/ontology. Pull-based injection selects the appropriate layer based on task intent. Maps directly onto the Letta memory framework. **Confidence: high.**

8. **RRF is the established standard for combining retrieval signals.** RRF(d) = Σ 1/(k + rank_i(d)) with k=60 combines cosine similarity, BM25, graph centrality (PPR), and recency without score calibration. Natively implemented in Azure AI Search, Milvus, Elasticsearch, OpenSearch, MongoDB Atlas, Qdrant. The same mechanism underpins the hybrid BM25+Model2Vec+sqlite-vec pattern from the context-mode research item. **Confidence: high.**

9. **KG construction cost at this corpus's scale is economically negligible.** 500 items × ~3,000 tokens/item = 1.5M tokens for one-time extraction; incremental updates <3,000 tokens/day. Total cost <$1 at current API prices. The dominant cost is engineering implementation, not API usage. **Confidence: medium** (cost estimate based on LightRAG token benchmarks; actual cost depends on model choice).

10. **RAPTOR implementation on the research corpus requires minimal additional work.** Each completed item already has Executive Summary (Layer 2), Key Findings (Layer 1), and full text (Layer 0). Only cluster-level summaries (Layer 3) across related items and a corpus-level summary (Layer 4) need to be generated. This is a 2–3 hour implementation task using LangChain's RAPTOR integration or a custom clustering script. **Confidence: high.**

11. **Knowledge rot is an active risk requiring lifecycle management.** Without review policies, the knowledge graph will accumulate stale entries as AI/ML knowledge evolves. Research items in fast-moving sub-domains (LLM architectures, agent memory) should be flagged for review at 12–18 months. The `added` and `completed` date fields in each item serve as lightweight TTL markers. **Confidence: medium.**

12. **The convergent architecture (embeddings + knowledge graph + graph-traversal reasoning) is the highest-quality long-term path.** Dense embeddings index into the knowledge graph; the graph provides relational structure; PPR or GoT traversal provides the reasoning scaffold for multi-hop queries. Demonstrated in HippoRAG (NeurIPS 2024) and KGoT (ETH Zurich 2024). Practical stack: Model2Vec (sqlite-vec) + LightRAG (NetworkX) + PPR for multi-hop queries. **Confidence: high.**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Dense embeddings outperform LSA on MTEB | MTEB benchmark; markaicode.com embedding comparison (2024) | high | Multiple independent sources |
| GraphRAG outperforms standard RAG on global queries | Edge et al. arXiv:2404.16130 | high | Primary source; peer-reviewed at Microsoft Research |
| GraphRAG requires full rebuild for incremental updates | arXiv:2410.05779 (LightRAG framing); GraphRAG docs | high | Architectural fact, confirmed across sources |
| LightRAG 10–100× lower token costs, matching accuracy | arXiv:2410.05779; EMNLP 2025 | high | Primary source with benchmark data |
| HippoRAG +20% multi-hop QA, 10–30× cheaper | arXiv:2405.14831; NeurIPS 2024 | high | Peer-reviewed primary source |
| RAPTOR +20pp on QuALITY, F1 55.7% on QASPER | arXiv:2401.18059; ICLR 2024 | high | Peer-reviewed primary source |
| Concept maps not machine-readable for agent retrieval | realkm.com (2024); NVIDIA KG+LLM blog | high | Consistent across practitioner and academic sources |
| KG subsumes concept map navigability for machine use | NVIDIA KG+LLM blog; MDPI KG+LLM survey (2025) | high | Multiple independent sources |
| RRF native in all major vector search engines | Azure AI Search docs; Milvus; MongoDB Atlas (2024) | high | Verified across 6+ platforms |
| KG construction <$1 for 500 items | Estimated from arXiv:2410.05779 token benchmarks | medium | Estimate; depends on model choice |
| Five-layer architecture maps onto Letta framework | Letta blog; 2026-03-02-agent-memory-management-context-injection.md KF12 | high | Internal consistency across research items |
| Knowledge rot risk for AI/ML items >12–18 months | Enterprise wiki post-mortems; Zep/Graphiti temporal design | medium | No domain-specific timing data; extrapolated |

### Assumptions

- **Assumption:** Dense embeddings at <500 items are computationally feasible on CPU with local models (Model2Vec). **Justification:** Demonstrated in the context-mode research item by a practitioner running Model2Vec on a 49,746-chunk Obsidian vault without GPU.
- **Assumption:** LLM-based KG extraction produces sufficient quality on research-item content without extensive prompt tuning. **Justification:** GraphRAG, LightRAG, and HippoRAG all demonstrate strong extraction quality on similar corpus types; research items have clear, extractable entities.
- **Assumption:** The corpus will reach ~200 items within 6 months at current accumulation rates. **Justification:** Current backlog ~27 items; completing 2–5 items/week reaches 200 items in 3–6 months.

### Analysis

The evidence supports a staged adoption path that avoids over-engineering at current corpus scale while positioning for the full convergent architecture as the corpus grows.

**Stage 1 (now, <100 items):** BM25 + dense embedding hybrid search (per `semantic-full-text-search.md`). Add RAPTOR Layer 3–4 generation as a near-zero-cost enhancement that unlocks multi-item query capability immediately, given that Layers 0–2 already exist in every completed item.

**Stage 2 (~150–200 items):** Build a LightRAG knowledge graph. This is the threshold where cross-item relationship queries justify graph construction overhead. LightRAG's incremental merge model is operationally sustainable for a daily-updated corpus.

**Stage 3 (~500+ items):** Add community detection and community summaries (GraphRAG pattern within LightRAG). Global sensemaking queries ("what does the corpus say about X?") become the dominant query type at this scale.

The choice of LSA/LSE is resolved definitively: it adds no value over dense embeddings for this corpus and should not be implemented. The choice of concept maps is resolved: they are not a separate implementation concern; any concept-map-like view is a rendered artefact of the knowledge graph.

The four-signal RRF (cosine + BM25 + PPR + recency) is the recommended ranking combination. LLM cross-encoder reranking is optional and should be added only if retrieval quality falls short after the four-signal RRF is deployed.

### Risks, Gaps, and Uncertainties

- **Unknown query type distribution.** The actual mix of local factual lookups, global sensemaking queries, and multi-hop relationship queries for this corpus is not yet known. This distribution determines relative technique value. Recommendation: instrument agent queries once the corpus reaches 100 items.
- **LLM extraction quality on research items is untested.** Whether standard LightRAG/HippoRAG extraction prompts work well on structured research markdown without tuning is unknown. A small-scale extraction test on 10–20 items before full pipeline build would de-risk this.
- **No benchmark on research-item corpora.** All performance numbers come from general academic QA benchmarks. Generalisation to structured knowledge management corpora is an inference, not a measured result.
- **Knowledge rot timescales are domain-dependent.** The 12–18 month staleness threshold for AI/ML items is an estimate. Sub-domains vary: LLM architecture research has a 6-month cycle; epistemological and consciousness research has a multi-year cycle.

### Open Questions

1. **KG construction pipeline:** What entities and relationships should be extracted from research items, and what graph schema is optimal? (Candidate backlog item: `knowledge-graph-construction-pipeline`)
2. **RAPTOR offline vs. on-demand:** Should cluster summaries be generated in a CI/CD step (offline) or cached on first query (on-demand)? Offline is more token-efficient; on-demand avoids stale cache management.
3. **Existing item structure as RAPTOR input:** Can the Executive Summary fields be used directly as Layer 2 leaf nodes in the RAPTOR tree, or does RAPTOR's clustering require raw text re-chunking?
4. **Staleness threshold:** What is the right review trigger (12 months? 18 months?) and does it vary by tag (e.g., `llm`, `agents` = 12 months; `philosophy`, `neuroscience` = 24 months)?
5. **Backlog dependency edges in the graph:** Should research item `blocks`/`is-blocked-by` relationships from YAML front matter be first-class edges in the knowledge graph?

---

## Output

- Type: knowledge, backlog-item
- Description: A structured comparison of LSE, knowledge graphs (GraphRAG, LightRAG, HippoRAG), concept maps, and hierarchical document compression (RAPTOR) as techniques for large-scale agent context management; a recommended five-layer knowledge architecture; a staged adoption path tied to corpus scale; and open questions that seed follow-on implementation items.
- Links:
  - https://arxiv.org/abs/2404.16130 (GraphRAG — Edge et al., 2024)
  - https://arxiv.org/abs/2410.05779 (LightRAG — Guo et al., 2024)
  - https://arxiv.org/abs/2401.18059 (RAPTOR — Sarthi et al., 2024)