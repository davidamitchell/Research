---
title: "What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an AI agent using the Model Context Protocol (MCP) memory server?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-graph, memory-system, agentic-ai, llm, workflow, research-tooling]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-03-03-cross-item-synthesis-meta-insights, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What entity-relation schema and write/query patterns best support cross-session research provenance and concept reuse for an AI agent using the Model Context Protocol (MCP) memory server?

## Research Question

What entity-relation schema and write/query prompt patterns best support cross-session research provenance and concept reuse for an AI research agent using the `@modelcontextprotocol/server-memory` Model Context Protocol (MCP) memory server — specifically: what entity types and relation types should represent research concepts, item provenance, and cross-item connections; what `create_entities`, `create_relations`, and `add_observations` call patterns enable reliable retrieval in later sessions; and what are the failure modes of LLM-managed knowledge graphs that the schema design must protect against?

## Scope

**In scope:**
- The `@modelcontextprotocol/server-memory` MCP server: its data model (entities with observations, typed relations), available tools (`create_entities`, `create_relations`, `add_observations`, `search_nodes`, `open_nodes`), and documented best practices
- Entity type design for a research corpus: what entity types best represent concepts, claims, research items, tags, and cross-item relationships
- Relation type design: what relation types (e.g., `supports`, `contradicts`, `extends`, `mentions`, `derived-from`) best capture the semantic connections between research concepts and items
- Write patterns: prompt instructions for an LLM agent to write 3–5 key concepts per item into the graph after completing §6 Synthesis, including provenance (item slug) as an observation
- Query patterns: prompt instructions for querying the graph at §0 Initialise to surface prior findings related to the new research question
- Failure modes in LLM-managed knowledge graphs: entity proliferation (too many near-duplicate entities), schema drift (inconsistent entity types across sessions), and query recall failures
- Prior art: Letta/MemGPT persistent memory patterns, cognitive architecture memory systems (episodic, semantic, procedural), and knowledge graph construction in RAG systems

**Out of scope:**
- Full knowledge graph database implementations (Neo4j, ArangoDB) — must work within the in-memory MCP server
- Semantic search over graph embeddings (vector search)
- Multi-agent knowledge graph sharing (single-agent only)
- Knowledge graph visualisation

**Constraints:**
- Expand all acronyms on first use
- Must work with the `@modelcontextprotocol/server-memory` server as-is (no schema changes to the server)
- Write and query instructions must fit within a prompt block of ~200 words

## Context

W-0041 in `BACKLOG.md` proposes using the `@modelcontextprotocol/server-memory` MCP server (already configured in `.mcp.json`) to build a cross-session knowledge graph as research items are completed. The BACKLOG item specifies the outcome (entities, relations, provenance observations, session-start queries) but not the schema or patterns. Without evidence-based schema design, the knowledge graph will suffer from entity proliferation, schema drift, and poor recall — producing a graph that accumulates data but cannot answer useful queries. This research item grounds the schema and prompt design in evidence from existing knowledge graph and persistent memory systems.

## Approach

1. **MCP memory server data model review**: Read the `@modelcontextprotocol/server-memory` server documentation and source code; document the entity model (name, entity_type, observations list), relation model (from, to, relation_type), and available query tools.
2. **Letta/MemGPT memory architecture review**: Study how Letta (formerly MemGPT) structures its archival memory, in-context working memory, and entity store; extract entity and relation patterns applicable to research concept graphs.
3. **Research knowledge graph prior art**: Survey knowledge graph construction for scientific literature (SciKG, OpenKE), semantic scholar's knowledge graph, and RAG-with-KG systems; identify entity and relation taxonomies used for academic concept representation.
4. **Entity type design**: Propose entity types for the research corpus (Concept, Claim, ResearchItem, Tag, Method) with examples and justification; assess trade-offs between fine-grained and coarse-grained type systems.
5. **Relation type design**: Propose relation types (supports, contradicts, extends, derived-from, mentioned-in, co-occurs-with) with definitions and examples; identify minimum set required for useful cross-item queries.
6. **Failure mode analysis**: Document known failure modes of LLM-managed knowledge graphs (entity proliferation, schema drift, orphaned entities, query recall failures) and design schema constraints that mitigate each.
7. **Prompt template design**: Produce concrete write and query prompt blocks (§6 write, §0 query) fitting within 200 words each.

## Sources

- [ ] [Modelcontextprotocol server-memory documentation and source code](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) — entity-relation data model and available tools for the MCP memory server
- [ ] [Packer et al. (2023) MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — Letta/MemGPT archival memory and entity storage patterns for persistent agent memory
- [ ] [Pan et al. (2024) Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — survey of knowledge graph construction and retrieval patterns for LLM agents
- [ ] [Wang et al. (2023) Knowledge Graph Prompting for Multi-Document Question Answering](https://arxiv.org/abs/2308.11730) — knowledge graph construction from documents and query patterns for multi-document RAG
- [ ] [Ahrens (2017) How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking](https://www.soenkeahrens.de/en/takesmartnotes) — Zettelkasten permanent note structure as an analogue for entity-based knowledge graph design

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

### Key Findings

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
