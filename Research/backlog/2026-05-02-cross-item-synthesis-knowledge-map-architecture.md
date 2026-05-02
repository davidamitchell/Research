---
title: "What technical architecture best supports cross-item synthesis, knowledge mapping, and active insight generation for a file-based research corpus of ~200 items managed by Artificial Intelligence (AI) agents?"
added: 2026-05-02T06:11:10+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-graph, agentic-ai, workflow, llm, memory-system, research-tooling]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: []
related: [2026-03-03-cross-item-synthesis-meta-insights, 2026-03-12-exploration-synthesis-gap, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What technical architecture best supports cross-item synthesis, knowledge mapping, and active insight generation for a file-based research corpus of ~200 items managed by Artificial Intelligence (AI) agents?

## Research Question

What technical architecture best supports three distinct but related capabilities in a file-based research corpus (~200 items, growing weekly): (1) a meta-distillation layer that proactively aggregates findings across items to surface higher-order themes and emergent insights not visible in any single item; (2) a knowledge map that renders relationships between items, concepts, and tags as a connected, navigable structure that regenerates automatically; and (3) a search and synthesis interface that answers ad-hoc queries with provenance links and publishes new distilled insights without requiring manual intervention — and what are the concrete tool choices, index formats, active/reactive trigger designs, and Large Language Model (LLM)-vs-heuristic trade-offs for each?

## Scope

**In scope:**
- Technical approaches for cross-document synthesis: MapReduce-style LLM summarisation, STORM-style iterative refinement, retrieval-augmented generation (RAG)-based synthesis, and heuristic tag/frontmatter aggregation
- Knowledge map formats: Mermaid diagrams, static graph HTML pages, Obsidian-style link graphs, JSON-LD graphs, and their suitability for GitHub Pages static site rendering
- Active vs reactive synthesis: event-triggered (on new item completion) vs scheduled (weekly) vs on-demand (workflow_dispatch) synthesis; trade-offs in freshness, compute cost, and coverage
- Trigger design for GitHub Actions workflows: which workflow events support automated synthesis commits to main
- Index format options: flat JSON, graph JSON (nodes + edges), vector embeddings, YAML-based adjacency lists; suitability for a file-based repo without a database
- Prior art in AI-assisted knowledge management tools: Letta, Roam Research, Obsidian Publish, Knowledge Explorer, and how they handle active synthesis

**Out of scope:**
- Full-text semantic search index (covered by W-0025 deferred item)
- Single-item research process (covered by the research loop and research skill)
- Authoring workflow (covered by W-0052)
- Any approach requiring a persistent database server (must work in GitHub Actions with only file I/O and API calls)

**Constraints:**
- Expand all acronyms on first use
- Must work within GitHub Actions runner constraints (ephemeral environment, no persistent DB, compute budget per run)
- Solution must be triggerable from the GitHub website without a local IDE
- Implementation language is Python 3.11+

## Context

W-0034 in `BACKLOG.md` defines three distinct but related needs: meta-distillation, knowledge mapping, and search/synthesis. Before implementing any of these, the design decisions (tool choices, index format, LLM-vs-heuristic trade-offs, active/reactive trigger design) must be resolved. The completed corpus has grown to ~200 items with cross-cutting themes invisible in individual items. The synthesis capability gap is the most significant outstanding structural gap in the research system — the corpus accumulates information but does not currently synthesise knowledge. This research item answers the architecture question so W-0034 implementation can proceed on a sound design.

## Approach

1. **Survey cross-document synthesis methods**: Review MapReduce-style LLM summarisation (Langchain, LlamaIndex), STORM-style synthesis (NAACL 2024), and simpler heuristic approaches (tag co-occurrence, frontmatter aggregation); assess each for fidelity, hallucination risk, compute cost, and suitability for a file-based corpus.
2. **Knowledge map format survey**: Survey Mermaid graph diagrams, D3.js force graphs, JSON-LD graph formats, and Obsidian Publish link graphs; assess each for static site rendering, auto-generation from Python, and navigability with ~200 items.
3. **Active synthesis trigger design**: Review GitHub Actions workflow trigger options (push, schedule, workflow_dispatch, workflow_run); identify which trigger patterns support automated synthesis commits without requiring manual intervention; assess freshness/cost trade-offs.
4. **Index format evaluation**: Compare flat JSON, graph JSON (nodes + edges), YAML adjacency lists, and vector embeddings for suitability in a file-based repo; assess query performance for synthesis retrieval.
5. **Prior art review**: Study how Letta, Roam Research, Obsidian Publish, and the Knowledge Explorer pattern handle active synthesis; identify design patterns applicable to this repo's constraints.
6. **Design recommendation**: Synthesise findings into a concrete architecture recommendation covering all three capabilities (meta-distillation, knowledge map, search/synthesis) with tool choices, index format, trigger design, and implementation order.

## Sources

- [ ] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (STORM)](https://arxiv.org/abs/2402.14207) — STORM synthesis methodology including multi-perspective coverage and iterative refinement
- [ ] [LlamaIndex documentation — Document Summaries Index](https://docs.llamaindex.ai/en/stable/examples/index_structs/doc_summary/) — MapReduce-style multi-document synthesis approach
- [ ] [Langchain documentation — Summarize Chain](https://python.langchain.com/docs/tutorials/summarize/) — map-reduce summarisation pipeline for large document corpora
- [ ] [Obsidian Publish — graph view](https://obsidian.md/publish) — link-graph knowledge map approach for file-based note systems
- [ ] [GitHub Actions — Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows) — trigger options for automated synthesis workflows
- [ ] [Letta (MemGPT) architecture documentation](https://docs.letta.com/introduction) — active memory and synthesis patterns in persistent agent systems

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
