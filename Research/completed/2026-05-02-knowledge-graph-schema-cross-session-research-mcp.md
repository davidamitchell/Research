---
review_count: 2
title: "What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?"
added: 2026-05-02T06:11:10+00:00
status: completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-graph, memory-system, agentic-ai, llm, agent-tooling, workflow]
ai_themes: [agentic-ai, memory-context, knowledge-graphs, tools-infrastructure]
started: 2026-05-03T05:37:47+00:00
completed: 2026-05-03T07:10:13+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-03-02-agent-memory-management-context-injection
  - 2026-03-03-knowledge-linking-connected-corpus
  - 2026-03-03-knowledge-representation-agent-context
  - 2026-04-29-knowledge-scaffolding-context-engineering
related:
  - 2026-03-17-ai-memory-systems-rag-neuroscience
  - 2026-03-03-cross-item-synthesis-meta-insights
  - 2026-05-02-knowledge-gap-tracking-promotion-patterns-pkm
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) agent using the Model Context Protocol (MCP) memory server?

## Research Question

What entity-relation schema and write-query prompt patterns best support cross-session research provenance and concept reuse for an Artificial Intelligence (AI) research agent using the `@modelcontextprotocol/server-memory` Model Context Protocol (MCP) memory server, specifically: what entity types and relation types should represent research concepts, item provenance, and cross-item connections; what `create_entities`, `create_relations`, and `add_observations` call patterns enable reliable retrieval in later sessions; and what failure modes of Large Language Model (LLM)-managed knowledge graphs should the schema design protect against?

## Scope

**In scope:**
- The `@modelcontextprotocol/server-memory` MCP server: its data model, entities with observations and typed relations, plus its available tools
- Entity type design for a research corpus: what entity types best represent concepts, claims, research items, and methods
- Relation type design: what relation types best capture semantic connections between research concepts and items
- Write patterns: prompt instructions for an LLM agent to write 3-5 key concepts per item into the graph after completing section 6 synthesis, including provenance observations
- Query patterns: prompt instructions for querying the graph at section 0 initialise to surface prior findings related to a new research question
- Failure modes in LLM-managed knowledge graphs: entity proliferation, schema drift, orphaned entities, provenance loss, and query recall failures
- Prior art from Letta or MemGPT persistent memory patterns, cognitive architecture memory systems, and knowledge graph construction in Retrieval-Augmented Generation (RAG) systems

**Out of scope:**
- Full graph database implementations such as Neo4j or ArangoDB, because the design must work within the in-memory MCP server
- Semantic search over graph embeddings or vector retrieval
- Multi-agent shared memory
- Knowledge graph visualisation

**Constraints:**
- Expand all acronyms on first use
- Work with the `@modelcontextprotocol/server-memory` server as-is, with no schema changes to the server
- Keep the recommended write and query instructions within about 200 words each

## Context

W-0041 in `BACKLOG.md` proposes using the Model Context Protocol (MCP) memory server to build a cross-session knowledge graph, a graph whose nodes are entities and whose edges are typed relations, as research items are completed, but it leaves the schema and prompt contract unspecified. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

The server itself is intentionally simple: entities have a unique name, a string `entityType`, and a list of atomic observations; relations are directed triples; `search_nodes` performs lexical substring matching over names, entity types, and observations; and `open_nodes` retrieves exact names plus adjacent relations. [fact; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

That simplicity makes schema discipline more important than in richer graph systems, because duplicate entity names, vague relation vocabularies, or missing provenance tokens quickly reduce retrieval quality and concept reuse. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://arxiv.org/html/2411.09601v1]

## Approach

1. **MCP memory server review:** inspect the server documentation and source to confirm the entity model, relation model, and query behavior.
2. **Persistent memory prior art:** review MemGPT and Letta material to identify how durable memory is partitioned into working, recall, and archival layers, and what that implies for a small research knowledge graph.
3. **Knowledge graph retrieval prior art:** review document-grounded knowledge graph work to identify node and relation patterns that support later retrieval rather than one-off graph construction.
4. **Schema design:** propose a minimum viable entity set, naming convention, observation pattern, and relation vocabulary that fit the server's actual query affordances.
5. **Failure-mode analysis:** identify duplicate-entity, schema-drift, provenance-loss, and recall problems, then map each to a concrete mitigation.
6. **Prompt design:** produce one write prompt and one query prompt that fit within the prompt budget and encode the schema rules explicitly.

## Sources

- [x] [Model Context Protocol server-memory README](https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md)
- [x] [Model Context Protocol server-memory source code](https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)
- [x] [Packer et al. (2024) MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)
- [x] [Letta (2025) Agent Memory: How to Build Agents that Learn and Remember](https://www.letta.com/blog/agent-memory)
- [x] [Luo et al. (2024) Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302)
- [x] [Wang et al. (2023) Knowledge Graph Prompting for Multi-Document Question Answering](https://arxiv.org/abs/2308.11730)
- [x] [Hitzler et al. (2024) Accelerating Knowledge Graph and Ontology Engineering with Large Language Models](https://arxiv.org/html/2411.09601v1)
- [x] [Cheng et al. (2025) EasyEA: Large Language Model is All You Need in Entity Alignment Between Knowledge Graphs](https://aclanthology.org/2025.findings-acl.1080/)
- [x] [Anonymous et al. (2024) Entity Alignment with Noisy Annotations from Large Language Models](https://openreview.net/forum?id=qfCQ54ZTX1)
- [x] [Ahrens (2017) How to Take Smart Notes](https://www.soenkeahrens.de/en/takesmartnotes)
- [x] [Mitchell (2026) Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html)
- [x] [Mitchell (2026) Agent Memory Management and Context Injection](https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
- [x] [Mitchell (2026) Knowledge Representation for Agent Context: LSE, Knowledge Graphs, Concept Maps, and Document Compression for Large-Scale Context Management](https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html)
- [x] [Mitchell (2026) Is knowledge scaffolding an established concept within context engineering for Large Language Models and AI agents, and how is it defined and implemented?](https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which entity-relation schema and write-query prompt pattern best support cross-session provenance and concept reuse in the Model Context Protocol (MCP) memory server.
- Scope: server contract, memory-system prior art, knowledge-graph retrieval patterns, schema design, failure modes, and compact prompts are in scope; graph databases, vector retrieval, and visualisation are out of scope.
- Constraints: use the existing server affordances only, keep recommendations promptable in about 200 words, and expand acronyms on first use.
- Output format: full section 0 to section 7 investigation plus Findings with Executive Summary, Key Findings, Evidence Map, Analysis, Risks, Gaps, Uncertainties, Open Questions, and Output.
- [inference] Prior completed-item cross-reference: the most relevant repository items are the knowledge-linking item for relationship vocabulary, the agent-memory item for long-term memory layering, the knowledge-representation item for graph retrieval structure, and the knowledge-scaffolding item for the stable vocabulary of context engineering. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html; https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html]
- [inference] Working definition: for this item, a useful research knowledge graph, meaning a structured knowledge model that stores entities and typed relations, is a small, curated network rather than a full ontology, and it should contain only research items, reusable concepts, reusable claims, and reusable methods that can be found again through lexical search and shallow graph expansion. [source: https://arxiv.org/abs/2306.08302; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

### §1 Question Decomposition

- A. Server contract
  - A1. What exact data structures and query behaviors does the MCP memory server support?
  - A2. Which server behaviors constrain naming, provenance, and retrieval design?
- B. Memory prior art
  - B1. What do MemGPT and Letta imply about what should remain in active context versus archival memory?
  - B2. How much structure is useful before a memory graph becomes maintenance-heavy?
- C. Knowledge graph retrieval
  - C1. What node and edge patterns help document-grounded retrieval?
  - C2. What relation vocabulary is useful enough to justify maintaining it manually?
- D. Schema design
  - D1. Which entity types are necessary for this repository?
  - D2. What naming convention minimizes duplication and supports exact `open_nodes` lookup?
  - D3. Should tags be first-class entities or observations?
- E. Failure modes
  - E1. How do duplicate entities arise?
  - E2. How does schema drift arise?
  - E3. How does provenance get lost?
  - E4. Why does recall fail even when the graph contains the right information?
- F. Prompt design
  - F1. What is the minimum write pattern that creates reusable nodes without graph spam?
  - F2. What is the minimum query pattern that surfaces prior relevant work at session start?

### §2 Investigation

#### 2.1 Server contract and retrieval affordances

- [fact] The Model Context Protocol server-memory README defines three primitive graph objects only: entities with a unique `name`, a string `entityType`, and a list of observations; directed relations with `from`, `to`, and `relationType`; and observation strings that should be atomic, meaning one fact per observation. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]
- [fact] The exposed write tools are `create_entities`, `create_relations`, and `add_observations`; `create_entities` ignores entities whose names already exist, `create_relations` skips duplicates, and `add_observations` fails if the target entity does not already exist. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [fact] The server persists data in JSON Lines (JSONL) form and reconstructs the graph from those lines at load time, which means there is no separate schema registry, no ontology layer, and no server-side validation beyond name uniqueness and exact relation duplication checks. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [fact] `search_nodes` performs case-insensitive substring search across entity names, entity types, and observation content, while `open_nodes` retrieves only the exact entity names supplied plus relations where at least one endpoint touches the requested node set. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] Because the server offers lexical search rather than semantic retrieval, stable naming conventions, alias observations, and short provenance tokens are not optional metadata, they are the primary retrieval surface. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]

#### 2.2 Persistent-memory prior art

- [fact] MemGPT frames long-term agent memory as virtual context management, where the system moves information between fast in-context memory and slower external memory tiers to work around limited context windows. [source: https://arxiv.org/abs/2310.08560; https://research.memgpt.ai/]
- [fact] Letta's agent-memory guidance states that agent memory is fundamentally context management, because what an agent remembers is determined by what reaches the context window at inference time, with message buffers, editable memory blocks, recall memory, and archival memory serving different roles. [source: https://www.letta.com/blog/agent-memory]
- [inference] For this repository, the MCP graph should therefore act as curated archival memory for reusable concepts, claims, and methods rather than as a dump of every sentence from every completed item, because the graph's job is to justify later context injection. [source: https://www.letta.com/blog/agent-memory; https://arxiv.org/abs/2310.08560; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]
- [fact] The repository's agent-memory research item concludes that ungardened memory stores accumulate outdated, duplicated, or contradictory entries unless their write path includes curation, provenance, or pruning. [source: https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]
- [inference] A useful schema for this server should therefore optimize for curation cost first and graph completeness second, because the server's affordances do not support automated deduplication, temporal reasoning, or confidence decay. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]

#### 2.3 Knowledge graph retrieval and note-linking prior art

- [fact] Wang et al. construct a knowledge graph over documents using nodes for passages or structures and edges for semantic or structural relations, then use graph traversal to gather supporting context for multi-document question answering. [source: https://arxiv.org/abs/2308.11730]
- [fact] Luo et al. describe Large Language Model and knowledge graph systems as complementary but emphasize that knowledge graph construction, completion, and evolution remain difficult because graphs are structured, dynamic artifacts rather than passive text stores. [source: https://arxiv.org/abs/2306.08302]
- [fact] Hitzler et al. argue that knowledge graph and ontology engineering tasks such as ontology modeling, extension, alignment, and entity disambiguation remain hard, and that modular approaches matter because large schemas overwhelm both humans and Large Language Models. [source: https://arxiv.org/html/2411.09601v1]
- [fact] The repository's knowledge-linking item concludes that direct links with a small typed vocabulary are more durable than broad undifferentiated metadata because structure emerges from explanatory links rather than from an ever-growing tag cloud. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [fact] Ahrens' Smart Notes guidance favors durable, explicitly linked notes over disconnected storage, which supports keeping graph nodes few, meaningful, and justified by reuse value rather than exhaustiveness. [source: https://www.soenkeahrens.de/en/takesmartnotes]
- [inference] These sources collectively support a small, modular, purpose-built graph over reusable concepts instead of a maximal extraction graph, because later retrieval depends more on legible conceptual structure than on raw graph size. [source: https://arxiv.org/html/2411.09601v1; https://arxiv.org/abs/2308.11730; https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

#### 2.4 Entity-type design

- [inference] The minimum viable entity set for this repository is four entity types: `research_item`, `concept`, `claim`, and `method`. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [inference] `research_item` is necessary because every reusable node needs an explicit provenance anchor, and the repository already treats item slugs as stable durable identifiers. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] `concept` is necessary because cross-session reuse usually begins with stable topic phrases such as `knowledge graph`, `context engineering`, or `active recall`, and these are the best lexical search surface for session-start retrieval. [source: https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]
- [inference] `claim` is necessary because provenance and epistemic links such as `supports` or `contradicts` usually apply to a proposition, not directly to a broad concept, and merging proposition-level relationships into concept nodes loses the distinction between topic and conclusion. [source: https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-cross-item-synthesis-meta-insights.html]
- [inference] `method` is necessary because techniques such as Graph Retrieval-Augmented Generation (GraphRAG), MemGPT, or Test-Driven Development (TDD) recur across items and benefit from being separately searchable without being confused for concepts or claims. [source: https://arxiv.org/abs/2310.08560; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-representation-agent-context.html]
- [inference] Tags should not be first-class entities in the initial schema, because the server cannot query by ontology or graph pattern, and the repository already stores tags in frontmatter; representing tags as observations such as `tag:knowledge-graph` preserves lexical recall without multiplying low-value nodes. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [inference] Exact-name lookup makes prefixed canonical identifiers preferable: `item:<slug>`, `concept:<canonical-term>`, `claim:<slug>:<short-key>`, and `method:<canonical-term>`. Prefixes reduce collisions and make `open_nodes` easier to target after a broad `search_nodes` pass. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

#### 2.5 Relation-type design

- [fact] The server README specifies that relations should be stored in active voice. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]
- [inference] The minimum relation vocabulary should be: `addresses` from `research_item` to `concept`; `states` from `research_item` to `claim`; `about` from `claim` to `concept`; `uses_method` from `research_item` or `claim` to `method`; `supports` from `claim` to `claim`; `contradicts` from `claim` to `claim`; and `extends` from `research_item` to `research_item` or from `claim` to `claim` where later work materially qualifies earlier work. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [inference] A fallback `related_to` relation is unnecessary in the initial schema, because it weakens recall precision by collapsing distinct semantics into one vague edge and makes later queries less interpretable. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://arxiv.org/html/2411.09601v1]
- [inference] `mentions` and `co_occurs_with` should also be excluded initially, because the repository goal is concept reuse and provenance, not dense co-reference mapping, and weak relations are the fastest path to graph spam. [source: https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

#### 2.6 Observation pattern and provenance design

- [fact] The server documentation recommends atomic observations, one fact per observation string. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]
- [inference] Observation strings should therefore carry short, lexical, search-friendly tokens rather than paragraph summaries, for example `title: ...`, `provenance:item=<slug>`, `section:key-finding-2`, `tag:knowledge-graph`, `alias:knowledge graphs`, `confidence:medium`, or `summary: lexical search needs stable names and provenance tokens`. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] Provenance should be stored on every `claim`, `concept`, and `method` touched by an item, not only on `research_item`, because `search_nodes` can hit observations directly and because later sessions may discover a node through a concept query before they know which item introduced it. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] Alias observations are especially important because lexical search cannot bridge naming variants on its own, so a concept such as `concept:knowledge-graph` should also carry `alias:knowledge graphs` and any stable repo-specific phrasing used in completed items. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]

#### 2.7 Failure modes and mitigations

- [fact] Entity alignment work on knowledge graphs shows that identifying equivalent entities is difficult even in dedicated alignment systems, and Large Language Model-generated annotations can be noisy enough to mislead downstream alignment unless refinement or selection policies are applied. [source: https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]
- [inference] In this server, duplicate-entity proliferation will most often come from agents creating near-synonyms such as `concept:knowledge graph`, `concept:knowledge-graph`, and `concept:knowledge-graphs` in separate sessions. The primary mitigation is a search-first rule plus canonical naming and alias observations instead of new entities. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]
- [fact] Hitzler et al. argue that knowledge graph and ontology engineering tasks such as extension, modification, and alignment remain hard and benefit from modular schemas rather than large undifferentiated structures. [source: https://arxiv.org/html/2411.09601v1]
- [inference] Schema drift in this repository will therefore arise less from raw model hallucination than from ungoverned expansion of entity and relation vocabularies across sessions. The mitigation is a fixed vocabulary written directly into the prompt and repeated in the item template or instructions. [source: https://arxiv.org/html/2411.09601v1; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [inference] Provenance loss occurs when a reusable concept or claim is stored without `provenance:item=<slug>` or without a relation back to `item:<slug>`, which makes later reuse possible but unverifiable. The mitigation is a hard rule that every created or updated node must either connect to a `research_item` node or carry a provenance observation from that item. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-cross-item-synthesis-meta-insights.html]
- [inference] Recall failures occur when search terms appear nowhere in names or observations, when nodes are too generic to rank meaningfully, or when weak relations swamp the graph. The mitigation is to keep nodes few, use exact lexical aliases, and require every non-item node to remain connected to at least one research item. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://www.soenkeahrens.de/en/takesmartnotes]
- [inference] Orphaned entities are a special case of provenance and recall failure: a node that is not connected to an item or claim may still be searchable, but it cannot explain why it exists or how it should be reused. The mitigation is to reject writes that leave a newly created node without at least one typed relation. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

#### 2.8 Recommended write and query patterns

- [inference] Recommended write sequence: search candidate concepts and methods first; reuse exact nodes when possible; create one `item:<slug>` node; create at most 3-5 concept nodes, 1-3 claim nodes, and 0-2 method nodes; then add typed relations and atomic provenance observations. This sequence matches the server's actual error behavior and minimizes silent duplication. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]
- [inference] Recommended query sequence: extract 2-4 noun phrases and synonyms from the new research question; run `search_nodes` on each phrase and relevant tag token; then `open_nodes` the most promising exact names and inspect adjacent `item`, `claim`, and `method` nodes with provenance observations. This compensates for the lack of graph traversal or embedding retrieval. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://arxiv.org/abs/2308.11730]
- [inference] The write prompt can stay under 200 words if it encodes only the fixed vocabulary, naming convention, search-first rule, and per-item node cap. The query prompt can also stay under 200 words if it focuses on phrase extraction, lexical widening by aliases, and provenance-first summarization. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://www.letta.com/blog/agent-memory]

### §3 Reasoning

- [inference] The strongest direct evidence in this item comes from the memory server's own README and source code, because schema recommendations that ignore its lexical search and exact-name retrieval behavior would be mismatched to the actual tool. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] External knowledge graph sources were used mainly to justify why a small modular schema is safer than a broad ontology and why duplicate-entity and alignment problems deserve first-class mitigation. [source: https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]
- [inference] Repository completed items were used to adapt those general lessons to this corpus, especially the preference for explanatory links, curated memory, and context engineering over indiscriminate storage. [source: https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://davidamitchell.github.io/Research/research/2026-04-29-knowledge-scaffolding-context-engineering.html]

### §4 Consistency Check

- [fact] The server contract and the recommended schema are consistent: every recommended entity or relation type can be represented with existing `name`, `entityType`, `observations`, and `relationType` fields. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] No material contradiction remains between the memory-system sources and the knowledge-linking sources, because both favor curation, modularity, and explicit relationship structure over maximal capture. [source: https://www.letta.com/blog/agent-memory; https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]
- [inference] The main trade-off is between proposition-level precision and graph size: adding `claim` nodes improves support and contradiction tracking, but it also increases write cost. The recommended cap on claim nodes keeps that trade-off acceptable. [source: https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-cross-item-synthesis-meta-insights.html]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the server's lexical search means that retrieval quality depends more on disciplined surface forms than on hidden semantics, so schema design here is partly an information-architecture problem rather than only a graph-modeling problem. [source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]
- [inference] Behavioural lens: agent compliance cost matters because, if the write pattern asks the agent to create too many node types or relations per completed item, graph maintenance will decay over time just as manual wiki curation decays. [source: https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html; https://www.soenkeahrens.de/en/takesmartnotes]
- [fact] Historical lens: knowledge graph engineering literature has repeatedly found that alignment, disambiguation, and ontology evolution stay expensive even with strong automation, which supports starting with a deliberately narrow schema rather than a future-proof but brittle one. [source: https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/]
- [inference] Economic lens: the recommended schema is cheaper than a richer ontology not only in implementation effort but in future review effort, because each additional node type or weak relation multiplies the number of low-value graph updates an agent must make correctly. [source: https://arxiv.org/html/2411.09601v1; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

### §6 Synthesis

**Executive summary:**

A four-entity schema built around `research_item`, `concept`, `claim`, and `method`, with tags stored as observations rather than as first-class nodes, is the best fit for the current Model Context Protocol server-memory because this knowledge graph, a network of named entities linked by typed relations, supports only lexical search, exact-name retrieval, atomic observations, and shallow relation expansion. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

The key design choice is to treat the graph as curated archival memory for reusable concepts and propositions, not as a full extraction of every research sentence, because the main failure modes are duplicate entities, schema drift, provenance loss, and lexical recall failure rather than lack of storage capacity. [inference; source: https://www.letta.com/blog/agent-memory; https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/]

Reliable reuse depends on three disciplines: canonical prefixed names, a fixed small relation vocabulary, and provenance-rich atomic observations that expose tags and aliases to lexical search. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

The write and query patterns can fit within the prompt budget if they encode only those disciplines and cap each completed item to a handful of reusable nodes rather than attempting comprehensive graph capture. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://www.letta.com/blog/agent-memory]

**Key findings:**

1. **The current Model Context Protocol server-memory contract strongly favors a small canonical schema because it offers only lexical substring search over names, entity types, and observations, plus exact-name opening of nodes and adjacent relations.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)
2. **The best default entity set for this repository is `research_item`, `concept`, `claim`, and `method`, because that set preserves provenance, reusable topics, proposition-level support or contradiction, and recurring techniques without forcing the graph to model every frontmatter field as a separate node type.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html)
3. **Tags should remain provenance-rich observations such as `tag:knowledge-graph` instead of becoming first-class nodes, because the server cannot query by ontology or graph pattern and low-value tag nodes would increase duplication faster than they improve retrieval.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html)
4. **A minimum useful relation vocabulary is `addresses`, `states`, `about`, `uses_method`, `supports`, `contradicts`, and `extends`, because these edges capture provenance and epistemic reuse while avoiding the graph spam created by weak relations such as `mentions` or `related_to`.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://www.soenkeahrens.de/en/takesmartnotes)
5. **The write path should always be search-first, then create a single item node, then create only 3-5 concept nodes plus a small number of claim and method nodes, because name reuse and node caps are the simplest effective defenses against duplicate entities, orphaned nodes, and schema drift.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1)
6. **Provenance and recall both improve when every reusable node carries atomic observation tokens such as `provenance:item=<slug>`, `section:key-finding-2`, `tag:<canonical-tag>`, and `alias:<variant>`, because those short strings become the server's practical retrieval index.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)
7. **MemGPT and Letta support treating this graph as curated archival memory for reusable concepts and claims rather than as exhaustive storage, because long-term agent memory is useful only when later sessions can pull the right structured context back into the active window at the right time.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
8. **The major failure modes for an LLM-managed graph in this repository are duplicate entity alignment, schema drift, provenance loss, and lexical recall gaps, and each one is better mitigated by fixed vocabulary and naming rules than by adding more schema complexity.** ([inference]; medium confidence; source: https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The server's lexical search and exact-name retrieval constrain the schema more than any external graph-theory preference. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Primary tool contract |
| [inference] Four entity types capture the reusable structure of this corpus without overfitting the graph to frontmatter details. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Schema judgment |
| [inference] Tag observations are a better first-stage choice than tag entities because search is lexical and graph queries are shallow. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Retrieval-cost trade-off |
| [inference] A seven-relation vocabulary is enough to capture provenance and epistemic reuse while avoiding weak-edge sprawl. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Vocabulary judgment |
| [inference] Search-first writes with node caps are the practical guardrail against duplicate entities and schema drift. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1 | medium | Failure-mode mitigation |
| [inference] Provenance and alias observations function as the server's real retrieval index. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Observation design |
| [inference] Memory-system prior art supports a curated archival-memory role instead of exhaustive storage. | https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html | medium | Cross-source convergence |
| [inference] Fixed vocabulary and naming discipline mitigate the major failure modes better than additional schema complexity. | https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Control-surface recommendation |

**Assumptions:**

- None beyond the stated scope and the documented server contract.

**Analysis:**

The decisive constraint in this item is not abstract knowledge-graph theory but the actual retrieval behavior of the Model Context Protocol server-memory, because lexical substring search means that stable names and observation tokens carry most of the retrieval burden. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]

That is why a richer ontology, first-class tag nodes, or broad weak relations were rejected as the default design: those alternatives increase maintenance cost without giving this server a better query surface, while the external knowledge-graph literature repeatedly shows that alignment and schema-management effort scale badly. [inference; source: https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]

The strongest rival design would be a concept-plus-tag graph with no separate claim nodes, because it is cheaper to write. That rival was rejected because support and contradiction are proposition-level relationships, and collapsing them into concept nodes would blur the difference between a topic and a conclusion. [inference; source: https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-cross-item-synthesis-meta-insights.html]

The other plausible rival would be comprehensive extraction of every key finding sentence. MemGPT, Letta, and the repository's prior memory work all point the other way: useful long-term memory is curated context that can be reactivated later, not maximal archival volume. [inference; source: https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]

**Risks, gaps, uncertainties:**

- The recommended schema is optimized for the current repository scale and the current server implementation, so it may need revision if the corpus grows enough that tags, source nodes, or temporal validity become retrieval-critical. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://arxiv.org/html/2411.09601v1]
- The evidence base supports the failure modes strongly, but the exact node cap of 3-5 concepts per item remains a practical design judgment rather than an experimentally benchmarked threshold. [inference; source: https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]
- The server has no native multi-hop traversal, temporal reasoning, or confidence-aware ranking, so some later retrieval failures may remain even with good schema hygiene. [fact; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

**Open questions:**

- At what corpus size does `tag:<canonical-tag>` stop being a sufficient observation-level recall surface and become worth modeling as a first-class node?
- Would a later version of the repository benefit from adding `source` nodes for external papers and URLs, or would that only recreate bibliographic metadata already stored elsewhere?
- How much retrieval quality would improve if the server gained hybrid lexical plus vector search while keeping the same graph schema?

**Write prompt template (under 200 words):**

```text
Before writing, run search_nodes for each candidate concept and method term and reuse existing nodes when they mean the same thing. Create exactly one research item node named item:<slug>. Create at most 3-5 concept nodes named concept:<canonical-term>, 1-3 claim nodes named claim:<slug>:<short-key>, and 0-2 method nodes named method:<canonical-term>. Do not create tag nodes. Store tags, aliases, provenance, and short summaries as atomic observations such as tag:knowledge-graph, alias:knowledge graphs, provenance:item=<slug>, section:key-finding-2, confidence:medium. Use only these relations: addresses, states, about, uses_method, supports, contradicts, extends. Every non-item node must connect to item:<slug> directly or through a claim node. If a node already exists, prefer add_observations over create_entities.
```

**Query prompt template (under 200 words):**

```text
At session start, extract 2-4 noun phrases from the new research question plus likely aliases and canonical tags. Run search_nodes on each phrase separately. Prefer results whose names begin with concept:, claim:, method:, or item:. Open the most relevant exact names with open_nodes, then inspect adjacent nodes and keep only results that expose provenance:item=<slug> from completed items. Summarize prior work as concepts, claims, methods, and source items. Treat near-synonyms as candidates for reuse, not as evidence that a new node is needed. If the first search is sparse, widen only with aliases and related methods; do not read the whole graph.
```

### §7 Recursive Review

- Confidence: medium
- Acronym audit: passed
- Domain-term clarity audit: passed
- Findings and section 6 parity: aligned
- Open contradictions: none material

---

## Findings

### Executive Summary

A four-entity schema built around `research_item`, `concept`, `claim`, and `method`, with tags stored as observations rather than as first-class nodes, is the best fit for the current Model Context Protocol (MCP) server-memory because this knowledge graph, meaning a structured knowledge model that stores entities and typed relations, supports only lexical search, exact-name retrieval, atomic observations, and shallow relation expansion. [inference; source: https://arxiv.org/abs/2306.08302; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

The key design choice is to treat the graph as curated archival memory for reusable concepts and propositions, not as a full extraction of every research sentence, because the main failure modes are duplicate entities, schema drift, provenance loss, and lexical recall failure rather than lack of storage capacity. [inference; source: https://www.letta.com/blog/agent-memory; https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/]

Reliable reuse depends on three disciplines: canonical prefixed names, a fixed small relation vocabulary, and provenance-rich atomic observations that expose tags and aliases to lexical search. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html]

The write and query patterns can fit within the prompt budget if they encode only those disciplines and cap each completed item to a handful of reusable nodes rather than attempting comprehensive graph capture. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://www.letta.com/blog/agent-memory]

### Key Findings

1. **The current Model Context Protocol server-memory contract strongly favors a small canonical schema because it offers only lexical substring search over names, entity types, and observations, plus exact-name opening of nodes and adjacent relations.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)
2. **The best default entity set for this repository is `research_item`, `concept`, `claim`, and `method`, because that set preserves provenance, reusable topics, proposition-level support or contradiction, and recurring techniques without forcing the graph to model every frontmatter field as a separate node type.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html)
3. **Tags should remain provenance-rich observations such as `tag:knowledge-graph` instead of becoming first-class nodes, because the server cannot query by ontology or graph pattern and low-value tag nodes would increase duplication faster than they improve retrieval.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html)
4. **A minimum useful relation vocabulary is `addresses`, `states`, `about`, `uses_method`, `supports`, `contradicts`, and `extends`, because these edges capture provenance and epistemic reuse while avoiding the graph spam created by weak relations such as `mentions` or `related_to`.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html; https://www.soenkeahrens.de/en/takesmartnotes)
5. **The write path should always be search-first, then create a single item node, then create only 3-5 concept nodes plus a small number of claim and method nodes, because name reuse and node caps are the simplest effective defenses against duplicate entities, orphaned nodes, and schema drift.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1)
6. **Provenance and recall both improve when every reusable node carries atomic observation tokens such as `provenance:item=<slug>`, `section:key-finding-2`, `tag:<canonical-tag>`, and `alias:<variant>`, because those short strings become the server's practical retrieval index.** ([inference]; medium confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)
7. **MemGPT and Letta support treating this graph as curated archival memory for reusable concepts and claims rather than as exhaustive storage, because long-term agent memory is useful only when later sessions can pull the right structured context back into the active window at the right time.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html)
8. **The major failure modes for an LLM-managed graph in this repository are duplicate entity alignment, schema drift, provenance loss, and lexical recall gaps, and each one is better mitigated by fixed vocabulary and naming rules than by adding more schema complexity.** ([inference]; medium confidence; source: https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The server's lexical search and exact-name retrieval constrain the schema more than any external graph-theory preference. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Primary tool contract |
| [inference] Four entity types capture the reusable structure of this corpus without overfitting the graph to frontmatter details. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Schema judgment |
| [inference] Tag observations are a better first-stage choice than tag entities because search is lexical and graph queries are shallow. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Retrieval-cost trade-off |
| [inference] A seven-relation vocabulary is enough to capture provenance and epistemic reuse while avoiding weak-edge sprawl. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-03-knowledge-linking-connected-corpus.html | medium | Vocabulary judgment |
| [inference] Search-first writes with node caps are the practical guardrail against duplicate entities and schema drift. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1 | medium | Failure-mode mitigation |
| [inference] Provenance and alias observations function as the server's real retrieval index. | https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Observation design |
| [inference] Memory-system prior art supports a curated archival-memory role instead of exhaustive storage. | https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html | medium | Cross-source convergence |
| [inference] Fixed vocabulary and naming discipline mitigate the major failure modes better than additional schema complexity. | https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1; https://arxiv.org/html/2411.09601v1; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts | medium | Control-surface recommendation |

### Assumptions

- None beyond the stated scope and the documented server contract.

### Analysis

The decisive constraint in this item is not abstract knowledge-graph theory but the actual retrieval behavior of the Model Context Protocol server-memory, because lexical substring search means that stable names and observation tokens carry most of the retrieval burden. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md]

That is why a richer ontology, first-class tag nodes, or broad weak relations were rejected as the default design: those alternatives increase maintenance cost without giving this server a better query surface, while the external knowledge-graph literature repeatedly shows that alignment and schema-management effort scale badly. [inference; source: https://arxiv.org/html/2411.09601v1; https://aclanthology.org/2025.findings-acl.1080/; https://openreview.net/forum?id=qfCQ54ZTX1]

The strongest rival design would be a concept-plus-tag graph with no separate claim nodes, because it is cheaper to write. That rival was rejected because support and contradiction are proposition-level relationships, and collapsing them into concept nodes would blur the difference between a topic and a conclusion. [inference; source: https://arxiv.org/abs/2308.11730; https://davidamitchell.github.io/Research/research/2026-03-03-cross-item-synthesis-meta-insights.html]

The other plausible rival would be comprehensive extraction of every key finding sentence. MemGPT, Letta, and the repository's prior memory work all point the other way: useful long-term memory is curated context that can be reactivated later, not maximal archival volume. [inference; source: https://arxiv.org/abs/2310.08560; https://www.letta.com/blog/agent-memory; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]

### Risks, Gaps, and Uncertainties

- The recommended schema is optimized for the current repository scale and the current server implementation, so it may need revision if the corpus grows enough that tags, source nodes, or temporal validity become retrieval-critical. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://arxiv.org/html/2411.09601v1]
- The evidence base supports the failure modes strongly, but the exact node cap of 3-5 concepts per item remains a practical design judgment rather than an experimentally benchmarked threshold. [inference; source: https://www.soenkeahrens.de/en/takesmartnotes; https://davidamitchell.github.io/Research/research/2026-03-02-agent-memory-management-context-injection.html]
- The server has no native multi-hop traversal, temporal reasoning, or confidence-aware ranking, so some later retrieval failures may remain even with good schema hygiene. [fact; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts]

### Open Questions

- At what corpus size does `tag:<canonical-tag>` stop being a sufficient observation-level recall surface and become worth modeling as a first-class node?
- Would a later version of the repository benefit from adding `source` nodes for external papers and URLs, or would that only recreate bibliographic metadata already stored elsewhere?
- How much retrieval quality would improve if the server gained hybrid lexical plus vector search while keeping the same graph schema?

---

## Output

- Type: knowledge
- Description: This item produces a repository-specific schema, naming convention, relation vocabulary, and compact write-query prompts for using the Model Context Protocol server-memory as curated cross-session research memory. [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md; https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts; https://www.letta.com/blog/agent-memory]
- Links:
  - https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/README.md
  - https://raw.githubusercontent.com/modelcontextprotocol/servers/4503e2d12b799448cd05f789dd40f9643a8d1a6c/src/memory/index.ts
  - https://www.letta.com/blog/agent-memory
