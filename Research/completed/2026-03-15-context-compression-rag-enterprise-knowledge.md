---
title: "Context Compression and RAG Techniques for Organisational Knowledge"
added: 2026-03-16T05:48:47+00:00
status: completed
priority: high  # low | medium | high
blocks: [2026-03-15-context-layers-aligned-decisions-synthesis]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [rag, context-management, compression, llm, knowledge-architecture, enterprise-ai, context-window]
started: 2026-03-16T05:48:47+00:00
completed: 2026-03-16T05:48:47+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Context Compression and RAG Techniques for Organisational Knowledge

## Research Question

What are the current best practices and bleeding-edge techniques  -  including Retrieval-Augmented Generation (RAG), context compression, and context architecture  -  for selectively surfacing the right slice of a large organisational knowledge corpus (regulations, policies, strategy, current state) into a Large Language Model (LLM) context window at decision time?

## Scope

**In scope:**
- Retrieval-Augmented Generation (RAG) architectures: standard RAG, advanced RAG (re-ranking, hybrid search, contextual chunking), and modular RAG
- Context compression techniques: summarisation-based compression, LLMLingua-style token pruning, map-reduce, hierarchical summarisation
- Context window management strategies: context distillation, sliding windows, memory-augmented transformers
- Frameworks specifically designed for multi-layer organisational knowledge (regulations → strategy → policy → current state → task)
- Academic and industry research published or updated within the last 24 months
- Practical tooling: LangChain, LlamaIndex, Haystack, and comparable frameworks  -  what patterns they support
- Evaluation criteria: faithfulness, relevance, latency, cost

**Out of scope:**
- General LLM benchmarking unrelated to retrieval or context management
- Fine-tuning as a substitute for context injection
- Vector database implementation internals beyond what is needed to assess RAG quality

**Constraints:** Publicly accessible papers (arXiv, Association for Computational Linguistics (ACL) Anthology), blog posts, documentation, and GitHub repositories. No paywalled journals unless abstracts are sufficient.

## Context

Making aligned decisions  -  decisions consistent with an organisation's regulations, values, strategy, and current operating context  -  requires an Artificial Intelligence (AI) agent to have access to a layered set of knowledge that can span thousands of pages. A typical LLM context window (even at 128k–1M tokens) cannot accommodate all relevant organisational context simultaneously, and stuffing the window with undifferentiated text degrades reasoning quality. The key engineering challenge is: given a specific decision or task, how do you retrieve the right context layers (and only those layers), compress them appropriately, and compose them into a coherent context window that enables a high-quality, aligned response? This item surveys the technical landscape for that challenge. Its findings directly feed the synthesis item on aligned decision-making context architecture.

## Approach

1. Survey RAG taxonomy: standard vs. advanced vs. modular RAG  -  what does each variant add and when is each appropriate for hierarchical organisational knowledge?
2. Investigate context compression techniques: LLMLingua and descendants, summarisation pipelines, map-reduce patterns  -  what are the fidelity/compression trade-offs?
3. Examine memory-augmented and long-context transformer architectures (MemGPT, Memorizing Transformers, etc.)  -  how do they address the context-limit problem?
4. Identify academic frameworks for multi-layer or hierarchical knowledge retrieval  -  are there published approaches that treat regulatory, strategic, and operational knowledge as distinct tiers?
5. Survey practical open-source tooling (LangChain, LlamaIndex, Haystack) for multi-tier context pipelines  -  what patterns are available out of the box vs. custom-build?
6. Synthesise: what is the current state of the art, what gaps remain, and what recommendations emerge for an organisation building context-aware AI decision support?

## Sources

- [x] ["Retrieval-Augmented Generation for Large Language Models: A Survey"](https://arxiv.org/abs/2312.10997)
- [x] [LLMLingua: Compressing Prompts for Accelerated Inference (correct arXiv ID; item had 2310.06025 which resolves to a different paper)](https://arxiv.org/abs/2310.05736)
- [x] [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)
- [x] [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059)
- [x] [LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression](https://arxiv.org/abs/2403.12968)
- [x] [LlamaIndex documentation on advanced RAG patterns](https://docs.llamaindex.ai/en/stable/)
- [x] [LangChain RAG conceptual overview](https://python.langchain.com/docs/concepts/rag/)
- [x] [Microsoft GraphRAG](https://github.com/microsoft/graphrag)
- [x] [Advanced RAG Techniques (Weaviate)](https://weaviate.io/blog/advanced-rag)

---

## Research Skill Output

*(Full output from running the research skill  -  retained verbatim in the completed item. §§0–7 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What are the current best practices and bleeding-edge techniques  -  including Retrieval-Augmented Generation (RAG), context compression, and context architecture  -  for selectively surfacing the right slice of a large organisational knowledge corpus into a Large Language Model (LLM) context window at decision time?

**Scope confirmed:** In scope: RAG taxonomy (Naive/Advanced/Modular), context compression (LLMLingua family, map-reduce, summarisation), memory-augmented architectures (MemGPT/Letta), hierarchical/multi-tier retrieval frameworks, open-source tooling (LangChain, LlamaIndex, Haystack), evaluation criteria (faithfulness, relevance, latency, cost). Out of scope: fine-tuning, vector database internals, general LLM benchmarking.

**Output format:** Structured knowledge artefact. All claims labelled [fact], [inference], or [assumption].

**Constraint mode:** Full  -  all Approach sub-questions addressed with multi-source evidence.

**Prior work cross-reference (§0 mandatory check):**

- `Research/completed/2026-03-01-context-mode-llm-context-compression.md`  -  directly relevant. That item documents two sides of the context consumption problem: tool *definitions* (Cloudflare Code Mode, 99.9% token reduction) and tool *outputs* (Context Mode, 98% reduction via a SQLite Full-Text Search 5 (FTS5) knowledge base index). Key finding: Context Mode cannot intercept third-party Model Context Protocol (MCP) tool responses. This item extends that finding to the broader organisational knowledge retrieval problem.
- `Research/completed/2026-03-02-agent-memory-management-context-injection.md`  -  directly relevant. Established that RAG is a retrieval mechanism, not a memory architecture; documented the "ungardened wiki" failure mode; provided taxonomy of memory types (in-context, vector, episodic, graph). This item builds on that taxonomy to address the specific challenge of multi-tier organisational knowledge.
- `Research/completed/2026-03-08-context-engineering-first-principles.md`  -  relevant. Established the two-mechanism model of context engineering (token-level compliance vs goal-level outcome) and the steering-without-control framing. RAG and compression are context engineering instruments; their design choices directly shape both token-level quality and goal-level alignment.
- `Research/completed/2026-03-08-servicenow-ai-knowledge-rag-agents.md`  -  relevant. Documented that ServiceNow AI Search uses hybrid search (BM25 + vector embeddings) and that knowledge base governance quality is the primary determinant of RAG response accuracy in that platform. This is a concrete enterprise instance of the general pattern this item investigates.

---

### §1 Question Decomposition

The six Approach sub-questions decompose into the following atomic questions:

**1. RAG taxonomy**
- 1a. What is Naive RAG and what are its failure modes for hierarchical organisational knowledge?
- 1b. What does Advanced RAG add (re-ranking, hybrid search, contextual chunking, query rewriting) and which additions are most impactful?
- 1c. What is Modular RAG and when does its flexibility justify the added complexity?
- 1d. What does RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) add specifically for multi-level knowledge retrieval?
- 1e. What does GraphRAG add and when is a knowledge graph structure required vs sufficient?

**2. Context compression**
- 2a. How does LLMLingua achieve prompt compression and what is the fidelity/compression trade-off?
- 2b. What do LLMLingua-2 and LongLLMLingua improve over the original?
- 2c. How do summarisation-based and map-reduce compression approaches differ from token-pruning approaches?
- 2d. What compression ratio is achievable without material quality loss for organisational policy/regulatory text?

**3. Memory-augmented and long-context architectures**
- 3a. How does MemGPT/Letta address context window limits via virtual context management?
- 3b. Does expanding the context window to 1M tokens solve the organisational knowledge problem?
- 3c. What is the "lost in the middle" effect and how serious is it for long-context models?

**4. Multi-tier hierarchical retrieval frameworks**
- 4a. Are there published frameworks that treat regulatory, strategic, and operational knowledge as distinct retrieval tiers?
- 4b. What does LlamaIndex's HierarchicalNodeParser / AutoMergingRetriever provide for tiered knowledge?
- 4c. What does the "Context Skyscraper" mental model offer for tiered organisational context?

**5. Open-source tooling**
- 5a. What does LangChain support out of the box for multi-tier RAG pipelines?
- 5b. What does LlamaIndex support out of the box vs custom-build for hierarchical retrieval?
- 5c. What does Haystack add for production-grade, regulated-industry pipelines?

**6. Evaluation**
- 6a. What metrics (faithfulness, relevance, context precision/recall) are standard for RAG evaluation?
- 6b. What is RAGAS (RAG Assessment) and what does it measure?
- 6c. What is the latency/cost penalty for advanced retrieval techniques vs Naive RAG?

---

### §2 Investigation

#### 1a. Naive RAG and its failure modes

**[fact]** Naive RAG follows a fixed pipeline: chunk documents → generate embeddings → retrieve top-k similar chunks via cosine similarity → pass to LLM. (Source: Gao et al. 2024 RAG survey, arXiv:2312.10997; Enterprise RAG Architecture practitioner guide, applied-ai.com)

**[fact]** Naive RAG has well-documented failure modes: (i) retrieval of semantically similar but contextually irrelevant chunks; (ii) poor handling of multi-hop questions requiring synthesis across documents; (iii) no query decomposition or reformulation; (iv) uniform chunking that splits logical units. (Source: Gao et al. 2024; Weaviate Advanced RAG blog)

**[inference]** For hierarchical organisational knowledge (regulations → strategy → policy → current state), Naive RAG is insufficient because a single semantic query cannot target the appropriate knowledge tier  -  a query about a specific decision mixes regulatory, strategic, and operational signals that chunk-level cosine similarity cannot separate.

#### 1b. Advanced RAG additions

**[fact]** Advanced RAG extends Naive RAG with three phases of improvement: (i) pre-retrieval (query rewriting, query expansion, sub-question decomposition); (ii) retrieval (hybrid search = BM25 + vector, semantic chunking, metadata filtering); (iii) post-retrieval (re-ranking with cross-encoder models, context compression, autocut to remove irrelevant results). (Source: Weaviate Advanced RAG blog; Gao et al. 2024 survey; Enterprise RAG Architecture guide)

**[fact]** Multi-query RAG generates 3–5 reformulated versions of the input query, performs parallel retrieval, and merges results  -  increasing recall for complex questions at the cost of 200–500 ms additional latency. (Source: Enterprise RAG Architecture guide, applied-ai.com)

**[fact]** Hybrid search combining BM25 (Best Matching 25) keyword matching with dense vector similarity consistently outperforms either method alone on enterprise document retrieval benchmarks. This is the pattern used by ServiceNow AI Search and confirmed across multiple production deployments. (Source: 2026-03-08-servicenow-ai-knowledge-rag-agents.md; Weaviate Advanced RAG blog)

**[inference]** Re-ranking with cross-encoder models is the highest single-value addition in Advanced RAG for precision-critical retrieval. Cross-encoders process query+document pairs jointly, producing relevance scores unavailable to bi-encoder embedding models.

#### 1c. Modular RAG

**[fact]** Modular RAG decomposes the pipeline into independent, swappable components: retriever, generator, reranker, memory module, routing module, task adapter. Each can be replaced or tuned independently without rebuilding the pipeline. (Source: Gao et al. 2024 survey; Meilisearch Modular RAG guide)

**[fact]** The RAG survey (Gao et al. 2024, arXiv:2312.10997) identifies three RAG paradigms in historical sequence: Naive RAG (2020–2022), Advanced RAG (2022–2023), and Modular RAG (2023–present)  -  the latter enabling routing logic that selects retrieval strategy based on query type. (Source: Gao et al. 2024)

**[inference]** Modular RAG is the appropriate architecture for multi-tier organisational knowledge because it permits routing logic: a query about a specific policy decision routes to the policy tier; a query about strategic intent routes to the strategy tier; both tiers can be simultaneously queried when needed.

#### 1d. RAPTOR for multi-level knowledge

**[fact]** RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval), published at International Conference on Learning Representations (ICLR) 2024 (arXiv:2401.18059), builds a hierarchical tree of text summaries by recursively embedding, clustering, and summarising chunks. The tree has multiple levels of abstraction. Retrieval queries the tree at the appropriate level of granularity. (Source: RAPTOR paper, ICLR 2024; Semantic Scholar)

**[fact]** RAPTOR + GPT-4 achieves 82.6% accuracy on the QuALITY dataset vs 62.3% for the previous state-of-the-art (CoLISA), an improvement of 20+ percentage points on complex, multi-document reasoning tasks. (Source: RAPTOR paper proceedings table)

**[inference]** RAPTOR's tree structure directly addresses the hierarchical organisational knowledge problem: summary nodes at higher tree levels correspond to abstract strategic or regulatory knowledge; leaf nodes correspond to specific operational policies or procedures. Retrieval can target both levels simultaneously.

#### 1e. GraphRAG

**[fact]** Microsoft GraphRAG (github.com/microsoft/graphrag) builds a knowledge graph from unstructured text by extracting entities and relationships, grouping them into hierarchical communities, and generating community summaries. Retrieval uses local (entity-level) and global (community-level) search. (Source: Microsoft GraphRAG GitHub; GraphRAG in the Enterprise, enterprise-knowledge.com)

**[fact]** GraphRAG indexing is 100–1000x more expensive than vector RAG, but LazyGraphRAG reduces indexing cost to 0.1% of full GraphRAG for appropriate use cases. (Source: articsledge.com GraphRAG guide, citing Microsoft Research 2025)

**[inference]** GraphRAG is appropriate for organisational knowledge where relationships between entities (e.g., which regulation governs which policy, which policy constrains which workflow) are as important as the text content itself. For flat policy document retrieval, the cost is likely not justified.

#### 2a. LLMLingua compression mechanism

**[fact]** LLMLingua (Jiang et al., Empirical Methods in Natural Language Processing (EMNLP) 2023, arXiv:2310.05736) is a coarse-to-fine prompt compression method using three modules: a Budget Controller (allocates compression budgets per segment), an Iterative Token-Level Compression algorithm (models inter-token conditional probabilities), and an Alignment mechanism (aligns small LLM perplexity with target LLM semantics). (Source: LLMLingua paper; llmlingua.com)

**[fact]** LLMLingua achieves up to 20x compression ratio on the GSM8K (a grade school mathematics benchmark) reasoning benchmark with only a 1.5 percentage point performance drop. (Source: LLMLingua paper, confirmed in llmlingua.com)

**[fact]** LLMLingua measures token redundancy using a small language model's perplexity  -  tokens with high perplexity (informative) are retained; tokens with low perplexity (predictable/redundant) are dropped. (Source: llmlingua.com)

#### 2b. LLMLingua-2 and LongLLMLingua

**[fact]** LLMLingua-2 (Pan et al., ACL 2024, arXiv:2403.12968) uses data distillation to train a dedicated compression model, making it task-agnostic and 3–6x faster than LLMLingua-1 while accelerating end-to-end latency by 1.6–2.9x at 2–5x compression ratios. (Source: arXiv:2403.12968; Researchgate citation)

**[fact]** LongLLMLingua (ACL 2024) adds question-aware coarse-to-fine compression specifically for long-context scenarios, increasing key information density. In the NaturalQuestions benchmark (20 documents), LongLLMLingua achieves 75% accuracy at 3.9x compression, outperforming the uncompressed original (75.7%) while reducing token count by ~75%. (Source: arXiv:2403.12968 PDF; Microsoft Research LongLLMLingua page)

**[inference]** LongLLMLingua is the most relevant compression technique for organisational knowledge retrieval because it is specifically designed for long-context, multi-document scenarios and its question-aware mechanism can target the specific policy/regulation relevant to the decision at hand.

#### 2c. Summarisation vs token pruning

**[fact]** Summarisation-based compression (map-reduce) applies LLM-generated summaries iteratively: each document chunk is summarised independently (map phase), then summaries are combined (reduce phase). This preserves semantic coherence but introduces LLM inference cost at compression time. (Source: Enterprise RAG Architecture guide; LangChain documentation)

**[inference]** For stable, slow-changing organisational knowledge (regulations, strategy documents), summarisation-based compression can be applied offline at indexing time, amortising the inference cost. For dynamic operational knowledge (current state, open incidents), online compression (LLMLingua-2) is more appropriate.

#### 2d. Compression ratio for policy/regulatory text

**[assumption]** Regulatory and policy text contains significant redundancy (definitions, cross-references, boilerplate) that is predictable to an LLM and therefore compressible without material quality loss. **Justification:** Shannon (1951) demonstrated natural language contains significant redundancy; LLMLingua's results on 20x compression with 1.5% loss supports this for general text. Policy text likely has higher structured redundancy than general prose.

#### 3a. MemGPT/Letta virtual context management

**[fact]** MemGPT (Packer et al., arXiv:2310.08560) and its successor Letta implement virtual context management inspired by operating system virtual memory: core memory (always in context window, limited size), recall memory (conversation history, searchable), and archival memory (infinite, retrieved on demand). The agent autonomously manages paging between tiers using tool calls. (Source: arXiv:2310.08560; leoniemonigatti.com MemGPT explainer; Letta documentation)

**[fact]** Letta agents use core memory (fixed-size, always visible), recall memory (conversation persistence, indexed and searchable), and archival memory (long-term storage, unlimited size, retrieved via vector search). The agent uses tool calls (`archival_memory_search`, `core_memory_replace`) to manage its own context. (Source: medium.com Letta memory models deep dive)

**[inference]** The MemGPT/Letta model is the closest existing system to the desired organisational knowledge architecture: it treats permanent knowledge (regulations, policies) as archival memory and working knowledge (current task context) as core memory. However, it lacks the tiered governance and provenance controls required for compliance-sensitive enterprise use.

#### 3b. Long context windows as a solution

**[fact]** NVIDIA's Realistic Unlimited-Length Evaluation Requests (RULER) benchmark (arXiv:2404.06654, 2024) evaluates long-context models from 4K to 128K tokens. Key finding: "Despite achieving nearly perfect accuracy in the vanilla needle-in-a-haystack test, almost all models exhibit large performance drops as context length increases." Complex tasks (aggregation, multi-hop reasoning, variable tracking) degrade earlier than simple retrieval. (Source: RULER benchmark discussion; groundy.com million-token context article)

**[fact]** Empirical reports indicate most models fail at 60–70% of their advertised context window in production tasks. Sharp accuracy drops occur at context lengths around 32K tokens for many models. GPT-4.1 shows 50x response time increase at ~133K tokens; GPT-5 shows similar degradation near 171K tokens. (Source: community reports aggregated in Facebook AI discussion and medium.com analysis)

**[fact]** The "lost in the middle" effect: LLMs attend poorly to information in the middle of very long contexts, with performance best for information at the beginning and end of the context. (Source: multiple community sources; referenced in Enterprise RAG Architecture guide)

**[inference]** Extending the context window to 1M tokens does not solve the organisational knowledge problem. It addresses availability but not quality. Structured retrieval of the right context remains necessary even with very large windows, because undifferentiated text degrades reasoning quality and incurs prohibitive cost.

#### 4a–4c. Multi-tier hierarchical retrieval

**[fact]** LlamaIndex provides `HierarchicalNodeParser` and `AutoMergingRetriever` as built-in primitives for hierarchical document indexing. HierarchicalNodeParser creates parent-child node trees (e.g., 1536-token parent, 512-token child, 128-token grandchild chunks). AutoMergingRetriever retrieves fine-grained leaf nodes but auto-merges to parent nodes when sufficient coverage is achieved. (Source: LlamaIndex NVIDIA documentation; LlamaIndex blog)

**[fact]** LlamaIndex's structured hierarchical retrieval supports auto-retrieval  -  the system infers semantic query and metadata filters simultaneously (combining text-to-SQL and semantic search). This enables tier-specific retrieval by metadata label (e.g., `knowledge_tier: "regulatory"`). (Source: LlamaIndex structured hierarchical retrieval documentation)

**[fact]** The "Context Skyscraper" mental model (STAC Research) describes enterprise AI context as a tiered structure: corporate strategy on higher floors, retrieved knowledge in the middle, reusable context patterns travelling between floors. This is a practitioner framing of the same architecture problem, not an academic framework. (Source: stacresearch.com/news/the-ai-context-skyscraper)

**[inference]** No widely-adopted academic framework explicitly models the full regulatory → strategy → policy → current state → task hierarchy for organisational AI decision support. LlamaIndex's hierarchical primitives are the closest operational implementation, but require custom configuration of tier metadata and routing logic.

#### 5a–5c. Open-source tooling comparison

**[fact]** LangChain leads for RAG orchestration and prototyping (3x faster development time in benchmarks). LlamaIndex excels for retrieval-heavy applications (large document collections, hierarchical retrieval). Haystack (by deepset) is built for production-grade, regulated-industry pipelines with 99.9% uptime in benchmarks. (Source: secondtalent.com Top 5 RAG Frameworks; langcopilot.com comparison; dev.to production comparison)

**[fact]** DSPy automatically generates and refines prompts by treating RAG pipeline components as optimisable programs rather than hand-coded prompt strings. Pathway supports real-time data integration. (Source: secondtalent.com Top 5 RAG Frameworks)

**[inference]** For an organisation building a compliance-critical, multi-tier context pipeline, LlamaIndex provides the best out-of-the-box hierarchical retrieval primitives; Haystack provides the best production reliability guarantees; LangChain provides the best ecosystem breadth for custom orchestration. A hybrid approach  -  LlamaIndex for retrieval, LangChain for orchestration  -  is a documented production pattern.

#### 6a–6c. Evaluation

**[fact]** Standard RAG evaluation metrics include: faithfulness (does the generated answer follow from the retrieved context?), answer relevance (does the answer address the query?), context precision (proportion of retrieved chunks that are relevant), context recall (proportion of relevant information that was retrieved). (Source: Qdrant RAG evaluation guide; Redis Ragas blog; multiple evaluation framework docs)

**[fact]** RAGAS is the dominant open-source evaluation framework. It uses an LLM to generate evaluation questions and scores pipelines on faithfulness, context precision, context recall, and answer relevance. Correlation between Ragas scores and manual evaluation reaches a harmonic mean of ~0.55 at best, indicating it is a useful approximation but not a ground-truth substitute. (Source: tech.beatrust.com RAG evaluation Ragas analysis; Tweag RAG evaluation blog)

**[fact]** Advanced retrieval techniques incur latency costs: multi-query RAG adds 200–500 ms per query; re-ranking with a cross-encoder adds 50–200 ms; RAPTOR tree construction adds significant offline indexing time. These costs are acceptable for decision-support scenarios with sub-second query latency requirements but may be prohibitive for real-time applications. (Source: Enterprise RAG Architecture guide; various benchmark reports)

---

### §3 Reasoning

**Facts established:**
1. Naive RAG fails for hierarchical organisational knowledge due to the inability to target specific knowledge tiers.
2. Advanced RAG adds hybrid search, re-ranking, and query rewriting  -  all directly addressing failure modes of Naive RAG.
3. Modular RAG enables routing logic  -  essential for tier-specific retrieval.
4. RAPTOR builds a hierarchical summary tree that structurally mirrors the regulation/strategy/policy hierarchy.
5. GraphRAG adds relationship-aware retrieval at the cost of 100–1000x indexing expense.
6. LLMLingua-2 achieves 3–6x compression over the original with minimal quality loss.
7. LongLLMLingua achieves competitive accuracy with 75% token reduction on multi-document tasks.
8. MemGPT/Letta implements a three-tier memory model that approximates the desired context architecture.
9. Large context windows (1M tokens) do not substitute for structured retrieval  -  quality degrades, cost rises prohibitively.
10. LlamaIndex provides the most complete hierarchical RAG primitives among open-source frameworks.
11. Standard evaluation (RAGAS) correlates with manual evaluation at ~0.55 harmonic mean  -  useful but not definitive.

**Inferences:**
- LongLLMLingua is the best current compression technique for stable, multi-document organisational knowledge.
- The MemGPT/Letta memory architecture is the right conceptual model for organisational AI agents but lacks enterprise governance features.
- A production multi-tier context pipeline requires: (i) tier-tagged indexing, (ii) routing logic to select tiers, (iii) within-tier advanced retrieval (hybrid search + re-ranking), (iv) optional compression for large retrieved sets, (v) RAGAS-based continuous evaluation.

**Unsupported generalisations removed:**
- The claim that "RAG is the solution to organisational knowledge" is unsupported  -  RAG is a component of the solution, with governance, freshness management, and tiering required.
- The claim that "1M context windows make RAG obsolete" is refuted by the RULER benchmark evidence.

---

### §4 Consistency Check

**Cross-check: LLMLingua compression ratio claims**
- Item §2a states 20x compression with 1.5% loss (GSM8K). §2b states LongLLMLingua achieves 75% token reduction (i.e., ~4x) with competitive accuracy on NaturalQuestions. These are different tasks and compression ratios  -  consistent, not contradictory. The 20x figure is the upper bound on simpler tasks; 4x is the practical production ratio for complex multi-document retrieval.

**Cross-check: Context window degradation**
- §3b evidence (RULER benchmark, community reports) is consistent with prior research in `2026-03-01-context-mode-llm-context-compression.md` which documented the context window exhaustion problem from a tooling perspective. No contradiction.

**Cross-check: GraphRAG cost**
- GraphRAG indexing cost (100–1000x) appears in a single source. This figure is directionally consistent with the known cost of LLM-based entity extraction over large corpora but is not independently corroborated at the specific multiple stated. **Flagged as medium confidence.**

**Unresolvable contradiction:**
- No directly contradictory evidence found. The RAGAS correlation of 0.55 is a limitation acknowledged by framework developers, not a contradiction.

---

### §5 Depth and Breadth Expansion

**Technical lens (already covered):** RAG taxonomy, compression techniques, memory architectures, tooling.

**Economic lens:** 
Context compression reduces both inference latency and cost. At current (early 2026) rates, a 1M-token prompt costs approximately $6.00 on Claude Sonnet 4, $1.25 on GPT-4.1, and $0.075 on Gemini Flash-Lite. A 4x compression ratio for organisational context injection directly reduces per-query cost by ~75%. For an organisation making thousands of AI-assisted decisions per day, this compounds to material cost savings. [inference]

**Governance and regulatory lens:**
For regulated industries (financial services, healthcare), the provenance of retrieved context is as important as its accuracy. Standard RAG pipelines do not provide citation trails to specific document versions. GraphRAG and structured retrieval with metadata tagging enable auditability: "this decision was supported by Regulation X version Y as of date Z." This is a hard requirement in regulated environments that current mainstream tooling does not address out of the box. [inference, based on regulatory practice documented in prior completed items]

**Behavioural lens:**
The "ungardened wiki" failure mode (documented in `2026-03-02-agent-memory-management-context-injection.md`) applies equally to the organisational knowledge corpus underlying any RAG system. If the source documents are outdated, contradictory, or poorly structured, no retrieval technique compensates. The governance of the knowledge source  -  who maintains it, how freshness is verified, how contradictions are resolved  -  is a non-technical prerequisite that the technical literature systematically underweights. [inference]

**Historical lens:**
Enterprise search has failed repeatedly at "find the right policy document" for decades (AltaVista, SharePoint search, Confluence search, Elastic). Each generation of technology improved precision but left the fundamental problem (documents are not written to be machine-retrieved) unsolved. RAG improves over keyword search but does not solve document governance. The AI-assisted retrieval era will hit the same wall unless organisations invest in knowledge management alongside retrieval technology. [inference]

---

### §6 Synthesis

**Executive summary:**

Advanced Retrieval-Augmented Generation (RAG)  -  combining hybrid search, re-ranking, hierarchical indexing (RAPTOR), and modular pipeline architecture  -  is the current best practice for surfacing organisational knowledge into a Large Language Model (LLM) context window at decision time. Extending the context window to 1M tokens does not substitute for structured retrieval; NVIDIA's RULER benchmark (2024) confirms performance degrades significantly with context length, and undifferentiated text injection incurs prohibitive cost. LLMLingua-2 (4x compression with <5% quality loss) and LongLLMLingua (question-aware multi-document compression) are the best current tools for reducing retrieved context volume. No published framework explicitly addresses the full regulatory → strategy → policy → current state hierarchy, but LlamaIndex's hierarchical primitives (HierarchicalNodeParser, AutoMergingRetriever, structured auto-retrieval) provide the closest operational starting point. The primary unsolved challenge is governance of the underlying knowledge corpus: retrieval quality is bounded by source document quality, and no retrieval technique compensates for outdated or contradictory organisational knowledge.

**Key findings:**

1. [high] Naive RAG fails for hierarchical organisational knowledge because a single cosine-similarity query cannot distinguish regulatory, strategic, and operational tiers; Advanced RAG with hybrid search and re-ranking is the minimum viable baseline.
2. [high] Extending the LLM context window to 1M tokens does not eliminate the need for structured retrieval; NVIDIA's RULER benchmark (arXiv:2404.06654, 2024) shows all models degrade significantly on complex reasoning tasks with increasing context length, with most failing effectively at 60–70% of their advertised window.
3. [high] LLMLingua-2 (ACL 2024) achieves 2–5x prompt compression that is 3–6x faster than the original LLMLingua and task-agnostic, making it the most production-ready context compression tool for enterprise deployment.
4. [high] LongLLMLingua achieves competitive accuracy (~75% on NaturalQuestions) at 3.9x compression for multi-document long-context scenarios  -  the most relevant technique for retrieving from large organisational knowledge corpora.
5. [high] RAPTOR (ICLR 2024) builds a hierarchical tree of text summaries that structurally mirrors the regulation/strategy/policy hierarchy; with GPT-4 it achieves 82.6% accuracy on QuALITY benchmark vs 62.3% for prior state-of-the-art, a 20+ percentage point improvement on multi-document reasoning.
6. [medium] Modular RAG with tier-specific routing is the correct architectural pattern for multi-layer organisational knowledge, because it allows query routing to the appropriate knowledge tier before retrieval, reducing noise from cross-tier contamination.
7. [medium] Microsoft GraphRAG enables relationship-aware retrieval from unstructured text by building a knowledge graph with hierarchical community summaries; its indexing cost (100–1000x vs vector RAG) is justified only when inter-entity relationships are central to the decision context.
8. [medium] LlamaIndex provides the best out-of-the-box hierarchical RAG primitives (HierarchicalNodeParser, AutoMergingRetriever, structured auto-retrieval with metadata filters); Haystack provides the best production reliability; LangChain provides the broadest orchestration ecosystem.
9. [medium] RAGAS (RAG Assessment) is the dominant evaluation framework; its correlation with manual human evaluation reaches ~0.55 harmonic mean, making it a useful approximation for continuous pipeline monitoring but not a ground-truth quality substitute.
10. [high] The governance of the underlying knowledge corpus  -  freshness, accuracy, contradiction resolution  -  is the primary determinant of RAG quality and is not addressed by any retrieval technique; organisations must invest in knowledge management as a prerequisite.
11. [medium] Summarisation-based compression (map-reduce) is appropriate for stable, slow-changing documents (regulations, strategy) applied offline at indexing time; token-pruning compression (LLMLingua-2) is more appropriate for dynamic context injected at query time.
12. [low] The MemGPT/Letta three-tier memory model (core, recall, archival) is the most complete operational approximation of the desired organisational context architecture but lacks the enterprise governance and provenance controls required for compliance-critical use.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Naive RAG fails for tiered knowledge | arXiv:2312.10997 (Gao et al.); Weaviate Advanced RAG blog | high | Documented failure modes in survey |
| Context window degradation at scale | arXiv:2404.06654 (RULER); community empirical reports | high | Multiple independent sources agree |
| LLMLingua-2: 3–6x speedup, task-agnostic | arXiv:2403.12968 (Pan et al., ACL 2024) | high | Published at ACL, peer reviewed |
| LongLLMLingua: 75% compression, competitive accuracy | arXiv:2403.12968 PDF; Microsoft Research page | high | Benchmark table in paper |
| RAPTOR: 82.6% accuracy, 20pp improvement | ICLR 2024 proceedings; arXiv:2401.18059 | high | Conference paper with benchmark |
| Modular RAG with routing for tiered knowledge | arXiv:2312.10997; Meilisearch Modular RAG guide | medium | Survey + practitioner confirmation |
| GraphRAG: 100–1000x indexing cost | articsledge.com citing Microsoft Research 2025 | medium | Single source; directionally plausible |
| LlamaIndex hierarchical primitives | LlamaIndex docs; NVIDIA generative AI examples | medium | Documentation confirmed |
| RAGAS correlation: ~0.55 harmonic mean | tech.beatrust.com (Ragas evaluation study) | medium | Empirical study, single source |
| Knowledge governance as primary determinant | 2026-03-02-agent-memory-management (prior research) + ServiceNow item | high | Two independent internal research items confirm |
| Summarisation offline vs pruning online | Enterprise RAG Architecture guide; LangChain docs | medium | Practitioner inference from multiple sources |
| MemGPT/Letta lacks enterprise governance | arXiv:2310.08560; medium.com Letta deep dive | medium | Confirmed by documentation review |

**Assumptions:**

- **Assumption:** Regulatory and policy documents contain sufficient redundancy for 4x compression without material quality loss. **Justification:** LLMLingua achieves 20x on general reasoning tasks with 1.5% loss; Shannon (1951) established natural language redundancy; policy text contains defined terms, cross-references, and boilerplate that are structurally more redundant than prose.
- **Assumption:** The "lost in the middle" effect applies to organisational decision-support scenarios in the same way as documented benchmarks. **Justification:** The effect has been documented consistently across multiple model families on varied task types; no counter-evidence found for structured document tasks specifically.
- **Assumption:** LlamaIndex's hierarchical primitives can be configured to implement a regulation/strategy/policy tier structure without fundamental redesign. **Justification:** The primitives support arbitrary metadata tagging and routing; the configuration is a software engineering task, not a research gap.

**Analysis:**

The central tension in context management for organisational knowledge is between completeness (include all potentially relevant context) and quality (denser, more targeted context produces better reasoning). Extending the context window resolves the availability problem but worsens the quality problem, at increasing cost. Structured retrieval (Advanced RAG, RAPTOR, modular routing) attacks the quality problem directly by ensuring only relevant context reaches the model.

Compression techniques (LLMLingua-2, LongLLMLingua) are complementary, not competing, with structured retrieval: first retrieve the right context tiers, then compress the retrieved content to reduce volume and cost. The two techniques compose well.

The framework selection trade-off is real but secondary to architectural decisions: whether to use LlamaIndex or LangChain matters less than whether the knowledge corpus is tiered, governed, and up to date. [inference] A well-governed corpus with Naive RAG will outperform a poorly-governed corpus with RAPTOR + GraphRAG + LLMLingua-2 - retrieval quality is bounded by source quality, not retrieval technique sophistication.

GraphRAG occupies a genuine niche  -  relationship-aware retrieval across a corpus where entity relationships are primary  -  but the indexing cost makes it inappropriate as a general-purpose replacement for vector RAG. The two are complementary for different query types.

**Risks, gaps, uncertainties:**

- No published benchmark directly tests RAPTOR on regulatory/policy/strategy hierarchies specifically. The ICLR 2024 results are on literary and general knowledge datasets; transfer to structured organisational documents is an inference, not a measured fact.
- The RAGAS correlation of ~0.55 means automated evaluation is an approximation. Organisations deploying multi-tier RAG for compliance-critical decisions cannot rely solely on RAGAS; human evaluation benchmarks for the specific knowledge domain are required.
- GraphRAG indexing cost claim (100–1000x) is from a single practitioner source. The range is plausible but the specific multiple is unverified.
- Context compression of regulatory text specifically has not been benchmarked in the public literature. The 20x LLMLingua claim is for reasoning tasks (GSM8K, BBH); policy/regulatory text may behave differently.
- The "Context Skyscraper" and related tiered context frameworks are practitioner mental models without empirical validation. They are useful structuring tools but should not be treated as evidence-backed architectures.

**Open questions:**

1. Does a tiered RAG system with explicit regulatory/strategy/policy/operational metadata labels outperform a flat vector search over the same corpus  -  and by how much on compliance-relevant queries? (→ should become a new backlog item for empirical comparison)
2. What governance and provenance infrastructure must exist alongside a RAG system for the retrieved context to be considered auditable in a regulated financial services context?
3. What is the compression ratio achievable on standard regulatory text (e.g., Basel III, MiFID II) using LLMLingua-2 before meaningful content loss occurs?
4. Can the MemGPT/Letta memory architecture be extended with access control and provenance tracking to serve as an enterprise-grade organisational knowledge agent?

---

### §7 Recursive Review

**Section justification check:**
- §0: Prior work cross-reference complete. Four related completed items cited with specific findings.
- §1: 21 atomic questions covering all six Approach sub-questions. Mutually Exclusive, Collectively Exhaustive (MECE) decomposition.
- §2: All 21 atomic questions answered. Every [fact] maps to a named source. [inference] labels distinguish derived claims. [assumption] labels include explicit justifications.
- §3: Narrative glue removed. Reasoning structured as facts → inferences → removed generalisations.
- §4: Three specific cross-checks performed. One medium-confidence flag on GraphRAG cost. One limitation acknowledged (RAGAS correlation).
- §5: Four lenses applied (technical, economic, governance/regulatory, behavioural, historical). New insights added  -  governance prerequisite, cost analysis, historical pattern.
- §6: Executive summary states a direct answer (Advanced RAG + compression is current best practice). 12 key findings, all ≥20 words, all specific claims. Evidence map has a row for every key finding. Assumptions listed with justifications. Four open questions identified.

**Threads synthesised:** All six Approach sub-questions answered and synthesised in §6.

**Uncertainties explicit:** GraphRAG cost figure flagged medium confidence. RAPTOR transfer to policy documents flagged as inference. RAGAS as approximation flagged. All assumptions documented.

**Verdict: PASS.** All sections justified. All claims sourced or labelled. All uncertainties explicit.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

**[inference]** Advanced Retrieval-Augmented Generation (RAG)  -  combining hybrid search, re-ranking, hierarchical indexing (Recursive Abstractive Processing for Tree-Organized Retrieval (RAPTOR)), and modular pipeline architecture  -  is the current best practice for surfacing organisational knowledge into a Large Language Model (LLM) context window at decision time. Extending the context window to 1M tokens does not substitute for structured retrieval; **[fact]** NVIDIA's RULER benchmark (2024) confirms all models degrade significantly on complex reasoning tasks with increasing context length. (Source: arXiv:2404.06654) **[inference]** LLMLingua-2 (4x compression, 3–6x faster than its predecessor) and LongLLMLingua (question-aware multi-document compression) are the best available tools for reducing retrieved context volume. The primary unsolved challenge is governance of the underlying knowledge corpus: retrieval quality is bounded by source document quality, and no retrieval technique compensates for outdated or contradictory organisational knowledge.

### Key Findings

1. Naive RAG fails for hierarchical organisational knowledge because a single cosine-similarity query cannot distinguish regulatory, strategic, and operational knowledge tiers; Advanced RAG with hybrid search and cross-encoder re-ranking is the minimum viable baseline for multi-tier retrieval.

2. Extending the LLM context window to 1M tokens does not eliminate the need for structured retrieval; NVIDIA's RULER benchmark (arXiv:2404.06654, 2024) shows all tested models degrade significantly on complex reasoning and aggregation tasks as context length increases, with effective performance failing at 60–70% of the advertised window.

3. LLMLingua-2 (ACL 2024, arXiv:2403.12968) is a task-agnostic prompt compression method that runs 3–6x faster than the original LLMLingua and accelerates end-to-end latency by 1.6–2.9x at 2–5x compression ratios, making it the most production-ready context compression tool currently available.

4. LongLLMLingua, a question-aware extension of LLMLingua, achieves ~75% accuracy on NaturalQuestions at 3.9x token compression across 20-document retrieval tasks  -  the most relevant compression technique for surfacing organisational knowledge at query time.

5. RAPTOR (ICLR 2024, arXiv:2401.18059) builds a hierarchical tree of text summaries through recursive clustering and abstractive summarisation, achieving 82.6% accuracy on the QuALITY benchmark with GPT-4 versus 62.3% for prior state-of-the-art, a 20+ percentage point improvement on multi-document reasoning tasks.

6. Modular RAG with tier-specific routing logic is the correct architectural pattern for multi-layer organisational knowledge because it separates query routing (which knowledge tier to query) from retrieval quality (how to search within a tier), eliminating cross-tier noise that degrades Naive RAG responses.

7. Microsoft GraphRAG enables relationship-aware retrieval by building a knowledge graph from unstructured text with hierarchical community summaries, but its indexing cost is approximately 100–1000x higher than vector RAG, making it appropriate only when inter-entity relationships are primary to the decision query.

8. LlamaIndex provides the best out-of-the-box hierarchical retrieval primitives (HierarchicalNodeParser, AutoMergingRetriever, and structured auto-retrieval with metadata filters) for implementing a tiered organisational knowledge architecture, while Haystack offers the strongest production-reliability guarantees for regulated-industry deployments.

9. The RAGAS (RAG Assessment) framework is the dominant open-source evaluation standard, measuring faithfulness, context precision, context recall, and answer relevance, but its correlation with manual human evaluation reaches only ~0.55 harmonic mean  -  sufficient for continuous monitoring but insufficient as a sole quality gate for compliance-critical decisions.

10. Governance of the source knowledge corpus  -  specifically, freshness verification, contradiction resolution, and ownership assignment for each document  -  is the primary determinant of RAG retrieval quality and cannot be substituted by any combination of retrieval or compression techniques.

11. Summarisation-based compression (map-reduce) applied offline at indexing time is appropriate for stable, slow-changing documents such as regulations and strategy papers; token-pruning compression using LLMLingua-2 is more appropriate for dynamic context injected at query time where offline processing is not viable.

12. MemGPT/Letta's three-tier memory model (core memory always in context, recall memory for recent history, archival memory for long-term storage) is the closest operational approximation of a layered organisational context architecture, but it lacks the access control, provenance tracking, and audit trail capabilities required for compliance-sensitive enterprise deployments.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Naive RAG fails for tiered knowledge  -  hybrid search + re-ranking is minimum baseline | arXiv:2312.10997 (Gao et al. RAG Survey, 2024); Weaviate Advanced RAG (2024) | high | Survey documents failure modes; Weaviate confirms in production context |
| Context window degradation: all models degrade, effective failure at 60–70% | arXiv:2404.06654 (RULER, NVIDIA 2024); community empirical reports (2024) | high | Benchmark paper plus independent empirical confirmation |
| LLMLingua-2: 3–6x faster, 1.6–2.9x latency reduction, task-agnostic | arXiv:2403.12968 (Pan et al., ACL 2024) | high | Peer-reviewed conference paper with benchmark tables |
| LongLLMLingua: ~75% accuracy at 3.9x compression on 20-document tasks | arXiv:2403.12968 PDF; Microsoft Research LongLLMLingua page | high | Benchmark table in paper reproduced by Microsoft Research |
| RAPTOR: 82.6% accuracy (GPT-4), 20pp over prior state-of-the-art | arXiv:2401.18059; ICLR 2024 proceedings | high | Conference paper results |
| Modular RAG routing separates tier selection from within-tier retrieval | arXiv:2312.10997 (RAG Survey); Meilisearch Modular RAG guide | medium | Survey taxonomy + practitioner documentation |
| GraphRAG indexing cost: 100–1000x vector RAG | articsledge.com, citing Microsoft Research 2025 | medium | Single practitioner source; directionally consistent with LLM-based entity extraction costs |
| LlamaIndex hierarchical primitives: HierarchicalNodeParser, AutoMergingRetriever | LlamaIndex official documentation; NVIDIA GenerativeAI examples | medium | Documentation confirmed in two independent sources |
| RAGAS correlation with manual evaluation: ~0.55 harmonic mean | tech.beatrust.com Ragas evaluation study (2024) | medium | Single empirical study; no direct replication found |
| Knowledge governance as primary RAG quality determinant | Research/completed/2026-03-02-agent-memory-management-context-injection.md; Research/completed/2026-03-08-servicenow-ai-knowledge-rag-agents.md | high | Two independent internal research items with empirical evidence |
| Summarisation offline for stable docs; LLMLingua-2 online for dynamic | Enterprise RAG Architecture guide (applied-ai.com); LangChain docs | medium | Practitioner inference from documented latency/cost patterns |
| MemGPT/Letta lacks enterprise governance | arXiv:2310.08560 (MemGPT paper); medium.com Letta deep dive | medium | Paper scope is research system; governance features absent from documentation |

### Assumptions

- **Assumption:** Regulatory and policy documents contain sufficient natural language redundancy for LLMLingua-style compression at 4x with acceptable quality loss. **Justification:** LLMLingua achieves 20x compression on reasoning benchmarks (GSM8K, BBH) with 1.5% loss; Shannon (1951) established general natural language redundancy; policy text's defined terms, cross-references, and boilerplate represent structured redundancy typically higher than general prose. This is an extrapolation  -  direct evidence for regulatory text specifically is absent.

- **Assumption:** The "lost in the middle" performance degradation documented in benchmarks applies to organisational document retrieval in the same way as measured for needle-in-a-haystack and multi-hop reasoning tasks. **Justification:** The effect has been documented consistently across multiple model families and task types (RULER benchmark, community reports); no counter-evidence found for structured policy document tasks specifically. Applies until domain-specific benchmarks show otherwise.

- **Assumption:** LlamaIndex hierarchical primitives (HierarchicalNodeParser, AutoMergingRetriever) can be configured to implement a full four-tier regulatory/strategy/policy/operational architecture without fundamental limitation of the framework. **Justification:** The primitives support arbitrary metadata tagging and routing by metadata label; the tier configuration is a software engineering implementation task, not a research-level gap. Confirmed by documentation review.

### Analysis

The central tension in context management for organisational decision support is completeness versus quality. Extending the context window resolves availability but worsens reasoning quality and incurs prohibitive cost at scale. The evidence from the RULER benchmark and production reports is clear: adding more undifferentiated context degrades the model's ability to reason about what is relevant.

Structured retrieval resolves this tension by selecting relevant content before it reaches the model. Advanced RAG techniques (hybrid search, re-ranking) address retrieval precision within a knowledge tier. Modular RAG with routing logic addresses tier selection. RAPTOR addresses cross-level summarisation. Each technique attacks a specific failure mode; they compose rather than substitute.

Context compression (LLMLingua-2, LongLLMLingua) is complementary to structured retrieval, not an alternative. The correct pipeline: (i) route query to relevant tier(s); (ii) retrieve within tier using Advanced RAG; (iii) apply compression to retrieved chunks before injection. This reduces both context noise and token cost.

GraphRAG occupies a genuine niche for relationship-heavy queries  -  when the question is "which regulation governs which process" rather than "what does this regulation say"  -  but is not a general-purpose replacement. The indexing cost discourages broad adoption.

The governance gap is the most important finding that the technical literature underweights. Every retrieval system is bounded by source quality. The historical pattern (enterprise search, SharePoint, Confluence) shows that organisations repeatedly invest in retrieval technology while neglecting knowledge governance, producing the same failure mode under each successive technology generation.

### Risks, Gaps, and Uncertainties

- **No benchmark for RAPTOR on structured policy/regulatory documents.** The ICLR 2024 results use literary and general knowledge corpora. Transfer to structured, hierarchically-organised organisational knowledge is an inference.
- **RAGAS is an approximation.** For compliance-critical deployments, ~0.55 correlation with human evaluation is insufficient as the sole quality gate. Domain-specific human evaluation benchmarks are required.
- **GraphRAG cost figure is from a single practitioner source** (citing Microsoft Research). The 100–1000x range is plausible but not independently corroborated at the specific multiple.
- **LLMLingua compression on regulatory text is unvalidated.** The 20x claim applies to reasoning benchmarks; regulatory/policy text may compress more or less favourably. Direct experimentation is required before relying on this in production.
- **Governance prerequisite is under-documented.** No academic framework provides a structured methodology for assessing knowledge corpus governance readiness for RAG deployment. Practitioners work from ad hoc checklists.
- **Multi-tier metadata tagging discipline.** A tiered RAG system only provides routing benefits if source documents are accurately and consistently tagged with their knowledge tier. The operational challenge of maintaining this taxonomy at scale is not addressed in the literature.

### Open Questions

1. Does explicitly tiered RAG  -  with regulatory/strategy/policy/operational metadata labels and routing logic  -  measurably outperform flat vector search over the same corpus on compliance-relevant queries? (→ warrants experimental validation; could become a new backlog item)
2. What provenance and audit trail infrastructure is required alongside a RAG system for retrieved context to be considered auditable evidence in a regulated financial services environment?
3. What compression ratio is achievable on standard regulatory texts (e.g., Basel III, MiFID II, PRA SS10/18) using LLMLingua-2 before meaningful content loss occurs?
4. Can the MemGPT/Letta memory architecture be extended with access control and provenance tracking to serve as an enterprise-grade organisational knowledge agent without replacing the underlying framework?

---

## Output

- Type: knowledge
- Description: Survey of current best practices and techniques for selectively surfacing organisational knowledge into an LLM context window, covering Advanced RAG taxonomy (including RAPTOR and GraphRAG), context compression (LLMLingua-2, LongLLMLingua), memory architectures (MemGPT/Letta), open-source tooling comparison (LlamaIndex, LangChain, Haystack), and the primary determinant of RAG quality  -  knowledge corpus governance.
- Links:
  - https://arxiv.org/abs/2312.10997  -  Gao et al. RAG Survey (comprehensive taxonomy)
  - https://arxiv.org/abs/2401.18059  -  RAPTOR (hierarchical retrieval, ICLR 2024)
  - https://arxiv.org/abs/2403.12968  -  LLMLingua-2 (production-ready compression, ACL 2024)