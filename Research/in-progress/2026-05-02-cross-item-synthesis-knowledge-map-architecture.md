---
title: "What technical architecture best supports cross-item synthesis, knowledge mapping, and active insight generation for a file-based research corpus of ~200 items managed by Artificial Intelligence (AI) agents?"
added: 2026-05-02T06:11:10+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [knowledge-graph, agentic-ai, workflow, llm, memory-system, research-tooling]
started: 2026-05-02T09:31:35+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-03-03-cross-item-synthesis-meta-insights
  - 2026-03-12-exploration-synthesis-gap
  - 2026-03-18-api-context-hubs-rag-mcp
  - 2026-04-29-knowledge-scaffolding-context-engineering
related:
  - 2026-04-28-uelgf-tooling-reference-architecture
  - 2026-05-01-sustainable-ai-software-development-synthesis
  - 2026-05-01-extension-systems-ai-coding-agents
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What technical architecture best supports cross-item synthesis, knowledge mapping, and active insight generation for a file-based research corpus of ~200 items managed by Artificial Intelligence (AI) agents?

## Research Question

What technical architecture best supports three distinct but related capabilities in a file-based research corpus (~200 items, growing weekly): (1) a meta-distillation layer that proactively aggregates findings across items to surface higher-order themes and emergent insights not visible in any single item; (2) a knowledge map that renders relationships between items, concepts, and tags as a connected, navigable structure that regenerates automatically; and (3) a search and synthesis interface that answers ad-hoc queries with provenance links and publishes new distilled insights without requiring manual intervention - and what are the concrete tool choices, index formats, active/reactive trigger designs, and Large Language Model (LLM)-vs-heuristic trade-offs for each?

## Scope

**In scope:**
- Technical approaches for cross-document synthesis: MapReduce-style LLM summarisation, Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (STORM)-style iterative refinement, Retrieval-Augmented Generation (RAG)-based synthesis, and heuristic tag/frontmatter aggregation
- Knowledge map formats: Mermaid diagrams, static graph HyperText Markup Language (HTML) pages, Obsidian-style link graphs, JavaScript Object Notation for Linked Data (JSON-LD) graphs, and their suitability for GitHub Pages static site rendering
- Active vs reactive synthesis: event-triggered (on new item completion) vs scheduled (weekly) vs on-demand (`workflow_dispatch`) synthesis; trade-offs in freshness, compute cost, and coverage
- Trigger design for GitHub Actions workflows: which workflow events support automated synthesis commits to main
- Index format options: flat JavaScript Object Notation (JSON), graph JSON (nodes + edges), vector embeddings, YAML Ain't Markup Language (YAML)-based adjacency lists; suitability for a file-based repo without a database
- Prior art in AI-assisted knowledge management tools: Letta, Roam Research, Obsidian Publish, Open Knowledge Maps, and how they handle active synthesis or graph navigation

**Out of scope:**
- Full-text semantic search index (covered by W-0025 deferred item)
- Single-item research process (covered by the research loop and research skill)
- Authoring workflow (covered by W-0052)
- Any approach requiring a persistent database server (must work in GitHub Actions with only file I/O and Application Programming Interface (API) calls)

**Constraints:**
- Expand all acronyms on first use
- Must work within GitHub Actions runner constraints (ephemeral environment, no persistent database, compute budget per run)
- Solution must be triggerable from the GitHub website without a local Integrated Development Environment (IDE)
- Implementation language is Python 3.11+

## Context

W-0034 already defines the target outcome as a meta-distillation layer, a knowledge map, and a search and synthesis interface, so this item's decision value is architectural rather than conceptual. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

Prior completed items already establish three relevant precedents: synthesis needs explicit provenance and contradiction handling, context systems work best when they separate always-loaded working context from larger searchable memory, and layered architectures are safer than monolithic "one index does everything" designs. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md]

The outstanding decision is therefore which file-based artifacts, rendering format, and workflow triggers create the cheapest reliable path from a growing corpus to automatically refreshed structure and selectively generated insight. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

## Approach

1. **Survey cross-document synthesis methods**: Review MapReduce-style LLM summarisation, STORM-style synthesis, and simpler heuristic approaches (tag co-occurrence, frontmatter aggregation); assess each for fidelity, hallucination risk, compute cost, and suitability for a file-based corpus.
2. **Knowledge map format survey**: Survey Mermaid graph diagrams, D3.js force graphs, JSON-LD graph formats, and Obsidian Publish link graphs; assess each for static site rendering, auto-generation from Python, and navigability with ~200 items.
3. **Active synthesis trigger design**: Review GitHub Actions workflow trigger options (`push`, `schedule`, `workflow_dispatch`) and compare them with current repo workflows; assess freshness/cost trade-offs.
4. **Index format evaluation**: Compare flat JSON, graph JSON (nodes + edges), YAML adjacency lists, and vector embeddings for suitability in a file-based repo; assess query performance for synthesis retrieval.
5. **Prior art review**: Study how Letta, Obsidian Publish, Open Knowledge Maps, and adjacent completed repo items handle active synthesis, memory layering, or graph navigation.
6. **Design recommendation**: Synthesise findings into a concrete architecture recommendation covering all three capabilities (meta-distillation, knowledge map, search/synthesis) with tool choices, index format, trigger design, and implementation order.

## Sources

- [x] [Shao et al. (2024) Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207)
- [x] [LlamaIndex Document Summary Index](https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/)
- [x] [GitHub Docs: Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [x] [GitHub workflow: Build and Deploy Research Site](https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml)
- [x] [GitHub workflow: Research Loop](https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml)
- [x] [Letta Docs: Archival memory](https://docs.letta.com/guides/ade/archival-memory)
- [x] [Obsidian Publish](https://obsidian.md/publish)
- [x] [Mermaid Flowcharts - Basic Syntax](https://mermaid.js.org/syntax/flowchart.html)
- [x] [D3 Force Simulation](https://d3js.org/d3-force/simulation)
- [x] [JSON-LD](https://json-ld.org/)
- [x] [Open Knowledge Maps](https://openknowledgemaps.org/)
- [x] [Mitchell (2026) Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
- [x] [Mitchell (2026) Exploration-synthesis gap: why people in explore mode fail to synthesise others' work, and whether agent synthesis can close the gap](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-exploration-synthesis-gap.md)
- [x] [Mitchell (2026) Application Programming Interface context hubs, Retrieval-Augmented Generation, and the Model Context Protocol](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md)
- [x] [Mitchell (2026) Is knowledge scaffolding an established concept within context engineering for Large Language Models and AI agents?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)
- [x] [Mitchell (2026) What principles and governance practices enable sustainable, high-quality software development with Artificial Intelligence coding agents?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Restated question: determine which file-based architecture best supports automatic cross-item synthesis, knowledge-map regeneration, and query-time synthesis for a corpus of roughly 200 research items without introducing a persistent database.
- Scope confirmed: synthesis methods, graph formats, trigger design, index formats, and prior art in scope; full semantic-search infrastructure and persistent-database designs out of scope.
- Constraints confirmed: must run inside GitHub Actions, remain file-based, stay accessible from the GitHub website, and fit the repository's existing Python and workflow patterns.
- [fact] Output format: full investigation through sections 0-7, followed by mirrored Findings with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps/Uncertainties, Open Questions, and Output. [source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
- [inference] The most relevant prior completed items are the existing synthesis-methodology item, the exploration-synthesis-gap item, the context-and-memory item, and the context-hubs/RAG/Model Context Protocol comparison item, because they already cover provenance discipline, why synthesis should be selective, memory-tiering patterns, and layered architecture trade-offs. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-exploration-synthesis-gap.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md]

### §1 Question Decomposition

**A. Cross-document synthesis method**
- A1. What value does STORM add beyond simple map-reduce summarisation?
- A2. What value does a document-summary index add beyond full-corpus prompting?
- A3. Which parts of synthesis should remain heuristic, and which require LLM reasoning?

**B. Knowledge-map format**
- B1. Which rendering formats stay usable at roughly 200 items on a static site?
- B2. Which formats are good for human navigation versus machine interoperability?
- B3. Which format should be primary, and which should be derivative exports?

**C. Trigger design**
- C1. Which triggers should refresh deterministic artifacts?
- C2. Which triggers should run expensive synthesis jobs?
- C3. Which trigger best serves ad hoc user questions from the GitHub website?

**D. Index format**
- D1. What is the minimum viable runtime artifact for nodes, edges, and summaries?
- D2. When is flat JSON enough, and when is graph JSON required?
- D3. Should vector embeddings be part of the baseline architecture now?

**E. Prior-art and memory pattern**
- E1. How do prior tools separate always-loaded context from large searchable memory?
- E2. What graph-navigation patterns are proven useful in public knowledge systems?
- E3. How should this repository publish new synthesized insights inside its current file layout?

**F. Recommendation**
- F1. What should be built first?
- F2. What should be deferred?
- F3. What concrete artifacts, scripts, and workflows make the design operational?

### §2 Investigation

#### 2.1 Prior work cross-reference

- [fact] The earlier cross-item synthesis item concluded that synthesis is not a list of summaries but an inter-item reasoning layer that must surface confirming evidence, tensions, integrated conclusions, confidence levels, and open questions. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]
- [fact] The exploration-synthesis-gap item concluded that synthesis has both organisational and technical value, but should be delegated to agents only when the artifacts are explicit enough for another agent to inspect and trace. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-exploration-synthesis-gap.md]
- [fact] The knowledge-scaffolding item found that strong context systems separate prompt-resident working context from larger searchable archival stores, rather than front-loading everything into one active window. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md]
- [fact] The Application Programming Interface context hubs vs Retrieval-Augmented Generation vs Model Context Protocol item found that prompt-time documentation, retrieval-time selection, and runtime invocation are separable layers rather than competing single-stack answers. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md]
- [inference] These prior items jointly favor a layered architecture here as well: deterministic structural artifacts for selection and navigation, then selective LLM synthesis over a bounded subset rather than whole-corpus prompting on every trigger. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-exploration-synthesis-gap.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md]

#### 2.2 Cross-document synthesis methods

- [fact] STORM explicitly improves long-form synthesis by discovering diverse perspectives, simulating grounded multi-perspective questioning, and curating collected information into an outline before writing. In evaluation against an outline-driven retrieval baseline, STORM's outputs were judged more organized and broader in coverage. [source: https://arxiv.org/abs/2402.14207]
- [fact] LlamaIndex's Document Summary Index extracts one summary per document, stores that summary plus the document's nodes, then retrieves relevant whole documents by matching queries against summaries before expanding into the document's underlying chunks. [source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- [inference] STORM is best understood as a high-cost, high-structure synthesis method for ambiguous or broad topics, while a document-summary index is a lower-cost retrieval and expansion mechanism for selecting which documents deserve full synthesis attention. [source: https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- [inference] For this repository, STORM-like multi-perspective synthesis is too expensive and too broad to run on every item completion, but it is well suited to weekly or contradiction-driven synthesis passes where higher-order theme discovery matters more than immediacy. [source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]
- [inference] Heuristic methods remain the right first-stage filter: tag overlap, `cites`, `related`, shared concepts in summaries, and recently changed clusters can narrow the candidate set before any LLM call, which directly reduces hallucination risk and compute cost. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

#### 2.3 Knowledge-map formats

- [fact] Mermaid flowcharts represent nodes and edges well, support subgraphs, and are easy to author or generate as text, but they remain diagram syntax rather than a large-scale interactive graph engine. [source: https://mermaid.js.org/syntax/flowchart.html]
- [fact] Obsidian Publish markets Graph view as a way to visually explore the connections between pages on a published site, which confirms that public readers do value link-graph navigation in a note corpus. [source: https://obsidian.md/publish]
- [fact] D3 force simulation can compute static force-directed layouts, and its documentation explicitly notes that static force layouts can be computed by manually ticking the simulation and then rendering the result. [source: https://d3js.org/d3-force/simulation]
- [fact] JSON-LD is a lightweight Linked Data format intended to make JSON interoperable at web scale, and it is positioned as good for programming environments, Representational State Transfer (REST) web services, and unstructured databases. [source: https://json-ld.org/]
- [fact] Open Knowledge Maps presents clustered visual maps as a discovery aid that helps users identify themes and focus on the most relevant literature within a large knowledge space. [source: https://openknowledgemaps.org/]
- [inference] Mermaid is the lowest-effort option for small thematic or per-tag subgraphs, but a full-corpus map of roughly 200 items needs a true graph runtime such as D3 if the result is meant to stay navigable rather than decorative. [source: https://mermaid.js.org/syntax/flowchart.html; https://d3js.org/d3-force/simulation; https://obsidian.md/publish]
- [inference] JSON-LD is valuable as an export layer because it preserves machine-readable semantics and external interoperability, but it is not itself a good primary runtime artifact for graph rendering or heuristic cluster queries inside a static GitHub Pages pipeline. [source: https://json-ld.org/; https://d3js.org/d3-force/simulation]
- [inference] The best combination is therefore graph JSON as the primary runtime artifact, D3 as the interactive renderer, Mermaid as a derivative snapshot format for small subgraphs, and JSON-LD as a secondary export for future interoperability. [source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://json-ld.org/; https://obsidian.md/publish]

#### 2.4 Trigger design

- [fact] GitHub Actions supports event-driven, scheduled, and manually dispatched workflows, and the current repository already uses `push`, `schedule`, and `workflow_dispatch` patterns in production workflows. [source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]
- [fact] The current Build and Deploy Research Site workflow runs on `push` to `main` for research and script changes, then rebuilds metadata and the static site and commits the generated output back to `main`. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml]
- [fact] The current Research Loop workflow uses both `workflow_dispatch` inputs and a weekday `schedule`, which demonstrates that the repository already treats expensive, autonomous work as a scheduled or manually triggered job rather than as a per-push action. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]
- [inference] Deterministic artifacts such as graph JSON, summary JSON, and derived static pages should refresh on `push`, because those builds are cheap, reproducible, and make the corpus immediately navigable after each completed item. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows]
- [inference] Expensive cross-item LLM distillation should default to `schedule`, because a weekly or batched run can amortize multi-item reasoning cost and operate over changed clusters rather than reprocessing the whole corpus after every item. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://arxiv.org/abs/2402.14207]
- [inference] Ad hoc search and synthesis should use `workflow_dispatch`, because that matches the repository's no-local-IDE constraint and gives the owner a GitHub website button for targeted questions without waiting for the next scheduled digest. [source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

#### 2.5 Index-format evaluation

- [fact] A document-summary index stores one summary per document plus pointers back to the document's underlying chunks, which makes it inherently document-centric rather than vector-store-centric. [source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- [fact] Letta's archival-memory model keeps large searchable memory outside the active context window and accesses it through explicit search tools, which is conceptually compatible with file-based summary and graph artifacts that stay on disk until selected. [source: https://docs.letta.com/guides/ade/archival-memory]
- [inference] Flat JSON is adequate for per-item metadata, but not for first-class relationship queries such as "show all cited neighbors plus shared-tag edges for a changed cluster," because those queries naturally depend on explicit edge records. [source: https://json-ld.org/; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- [inference] YAML adjacency lists are readable but awkward as the primary runtime format for static-site rendering, change detection, and downstream query tools, because they add little over JSON while being less natural for browser-side graph consumers. [source: https://json-ld.org/; https://d3js.org/d3-force/simulation]
- [inference] Vector embeddings should remain deferred in this baseline architecture, because W-0025 already covers semantic search separately and the current need is not nearest-neighbor retrieval in general, but explicit, provenance-safe synthesis over a moderately sized corpus. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]
- [inference] The minimum viable index stack is therefore three file artifacts: item summaries JSON, graph JSON with typed edges, and a cluster-manifest JSON that records which items changed and which clusters need distillation. [source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://d3js.org/d3-force/simulation; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]

#### 2.6 Prior art and memory-layer patterns

- [fact] Letta describes archival memory as a searchable external knowledge repository that stays outside the immediate context window, scales without increasing token usage, and is retrieved by explicit memory-search tools. [source: https://docs.letta.com/guides/ade/archival-memory]
- [fact] The knowledge-scaffolding item concluded that mainstream engineering practice prefers concrete mechanisms such as progressive disclosure, retrieval, memory, and context layering over a single broad "knowledge scaffolding" label. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md]
- [inference] That pattern maps cleanly to this repository: recent digests, per-item summaries, and cluster briefs should act as prompt-resident working context, while the full Markdown corpus and graph files act as archival memory searched only when needed. [source: https://docs.letta.com/guides/ade/archival-memory; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md]
- [inference] The Application Programming Interface context-hub versus Retrieval-Augmented Generation versus Model Context Protocol comparison also supports keeping layers distinct here: summary files are the curated prompt-time layer, graph and cluster manifests are retrieval-time selectors, and synthesis workflows are the runtime action layer. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md]

#### 2.7 Repository-fit recommendation evidence

- [fact] W-0034's suggested implementation order already points toward a knowledge map first, active meta-distillation second, and reactive search/synthesis third. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [fact] The repository already stores synthesis outputs as ordinary completed research items with `item_type: synthesis` rather than in a separate top-level synthesis directory. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]
- [inference] The new architecture should therefore publish weekly digests and thematic syntheses as normal completed synthesis items, not invent a parallel content store, because the existing item schema already supports provenance, citations, confidence, and versioning. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]
- [inference] The strongest concrete architecture is a hybrid stack: Python index builders on `push`, D3 knowledge-map rendering over graph JSON, scheduled Copilot-driven distillation over changed clusters, and `workflow_dispatch` query synthesis over the same artifacts. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://d3js.org/d3-force/simulation; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

### §3 Reasoning

- [inference] The architecture problem separates naturally into four layers: structural extraction, graph rendering, synthesis selection, and synthesis generation. Trying to collapse those layers into one index format or one workflow would either overfit the graph to synthesis needs or overfit the synthesis path to rendering needs. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md; https://d3js.org/d3-force/simulation; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- [inference] The most important trade-off is not LLM versus heuristic in the abstract, but where to place each. Heuristics are strongest where the repository already provides explicit signals such as tags, `cites`, `related`, dates, and changed files, while LLM reasoning is strongest only after that structure has already bounded the candidate set. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] The graph-format decision also splits into runtime and export concerns. Graph JSON is the simplest browser-native structure for D3 and Python transforms, while JSON-LD is stronger for semantic portability and future integration, so choosing one as runtime primary and the other as derivative export avoids a false either/or. [source: https://d3js.org/d3-force/simulation; https://json-ld.org/]
- [inference] Trigger choice should follow marginal cost. `push` is appropriate for cheap deterministic refresh, `schedule` is appropriate for expensive whole-cluster reasoning, and `workflow_dispatch` is appropriate for owner-driven ad hoc questions because it exposes a manual GitHub button without forcing the expensive path to run automatically. [source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]
- [inference] The resulting recommendation is deliberately incremental: it satisfies W-0034's active requirement quickly by making structure refresh immediate and synthesis periodic, while leaving full semantic search and embedding infrastructure deferred until deterministic artifacts prove insufficient. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]

### §4 Consistency Check

- [fact] No inspected source contradicted the core distinction between cheap structural refresh and expensive interpretive synthesis; the tension was about degree, not direction. STORM argues for richer synthesis structure, while LlamaIndex and Letta argue for layered selection and memory, and these positions are complementary rather than conflicting. [source: https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://docs.letta.com/guides/ade/archival-memory]
- [fact] The graph-format sources also align rather than conflict: Mermaid is text-first and lightweight, D3 is layout- and interaction-oriented, Obsidian Publish proves user value for link-graph browsing, and JSON-LD is interoperability-focused. [source: https://mermaid.js.org/syntax/flowchart.html; https://d3js.org/d3-force/simulation; https://obsidian.md/publish; https://json-ld.org/]
- [inference] The only material uncertainty is not whether a graph JSON plus scheduled synthesis architecture can work, but how much automatic cluster formation quality degrades as the corpus grows beyond the current scale. That uncertainty justifies deferring embeddings rather than disproving the recommended baseline. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

### §5 Depth and Breadth Expansion

- [inference] From a technical lens, the architecture behaves like a build pipeline more than a search product: extract deterministic state on each corpus change, then consume that state in separate rendering and synthesis workflows. That matches the repository's existing site-build and research-loop patterns and reduces the blast radius of each job. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]
- [inference] From a governance lens, selective synthesis is safer than continuous whole-corpus synthesis because it narrows provenance review to changed clusters and prevents silently rephrasing stable conclusions every time an unrelated item lands. This is consistent with the repo's broader emphasis on explicit versioning and reviewable diffs. [source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]
- [inference] From a human-usage lens, a map and a digest solve different jobs. The D3 graph lowers navigation friction and helps the owner find clusters, while scheduled digests and `workflow_dispatch` syntheses answer "what changed?" and "what does the corpus imply about this question?" respectively. [source: https://obsidian.md/publish; https://openknowledgemaps.org/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- [inference] From a maintenance lens, choosing graph JSON plus JSON-LD export keeps future options open. A later semantic-search layer can consume the same summaries and graph edges without replacing the map or rewriting stored synthesis outputs. [source: https://json-ld.org/; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

### §6 Synthesis

**Executive Summary**

The best-fit architecture is a hybrid, file-based stack that refreshes deterministic graph and summary artifacts on every corpus change, then applies Large Language Model (LLM) synthesis only to shortlisted clusters or queries rather than to the whole corpus each time. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://arxiv.org/abs/2402.14207]

For the knowledge map, a precomputed nodes-and-edges JSON file rendered as a static D3 force graph is the most scalable default for a roughly 200-item GitHub Pages corpus, while Mermaid should be reserved for small thematic subgraphs and JSON-LD should be emitted as an interoperability export rather than as the primary runtime index. [inference; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://json-ld.org/; https://obsidian.md/publish; https://openknowledgemaps.org/]

For active insight generation, the lowest-risk trigger pattern is push-driven index refresh plus scheduled weekly distillation and on-demand `workflow_dispatch` query synthesis, because `push` keeps artifacts fresh, `schedule` amortizes expensive multi-item reasoning, and manual dispatch preserves a website-only control surface for ad hoc questions. [inference; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

The retrieval layer should follow a Letta-style memory split: distilled per-item summaries, cluster manifests, and recent digests stay in prompt-resident working context, while the full Markdown corpus and graph artifacts remain searchable archival state on disk, which keeps provenance explicit without requiring a persistent database. [inference; source: https://docs.letta.com/guides/ade/archival-memory; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md]

**Key Findings**

1. **This repository should use heuristic relationship extraction and cluster formation as the backbone of the system, and reserve LLM synthesis for bounded candidate sets, because the corpus already exposes explicit signals such as tags, `cites`, `related`, and changed files that are cheap to compute and safer than whole-corpus prompting.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
2. **A document-summary index pattern is the best first retrieval layer for active synthesis in this repo, because it stores one summary per item, retrieves whole documents by summary relevance, and fits the file-based constraints better than introducing vector infrastructure before W-0025 is revived.** ([inference]; medium confidence; source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md)
3. **A D3 force-directed graph over graph JSON is the most scalable default knowledge-map renderer for a roughly 200-item public corpus, while Mermaid is better treated as a low-cost derivative for small subgraphs rather than as the primary full-corpus map.** ([inference]; high confidence; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://obsidian.md/publish)
4. **Graph JSON should be the primary runtime artifact and JSON-LD should be a secondary export, because graph JSON is the simplest structure for Python transforms and browser rendering, while JSON-LD adds semantic interoperability without being the easiest working format for static graph navigation.** ([inference]; medium confidence; source: https://json-ld.org/; https://d3js.org/d3-force/simulation)
5. **The best-aligned initial trigger design is `push` for deterministic artifact refresh, `schedule` for weekly or batched distillation, and `workflow_dispatch` for ad hoc synthesis, because the repository already uses those patterns successfully and each trigger aligns with a distinct cost and freshness profile.** ([inference]; medium confidence; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml)
6. **STORM-like multi-perspective synthesis should be a selective second-stage method for broad, ambiguous, or contradiction-heavy clusters rather than the default path, because it improves organization and breadth but carries materially higher reasoning and orchestration cost than deterministic selection plus ordinary synthesis prompts.** ([inference]; medium confidence; source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
7. **The repository should publish new synthesized insights as ordinary completed synthesis items plus targeted `learnings.md` updates, not as a new content store, because the current item schema already supports citations, confidence, provenance, and version history for exactly this kind of output.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
8. **A Letta-style memory split is the right mental model for the synthesis interface, with summaries and recent digests acting as working memory and the full corpus acting as searchable archival memory, because that preserves provenance and keeps prompt size bounded without requiring a standing service.** ([inference]; medium confidence; source: https://docs.letta.com/guides/ade/archival-memory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)

**Evidence Map**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Heuristic signals should shortlist items before any synthesis call. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | Cost control |
| [inference] A document-summary index pattern is the best first retrieval layer. | https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md | medium | File-based fit |
| [inference] D3 over graph JSON is the default full-corpus map. | https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://obsidian.md/publish | high | Mermaid for subgraphs |
| [inference] Graph JSON should be primary and JSON-LD derivative. | https://json-ld.org/; https://d3js.org/d3-force/simulation | medium | Export split |
| [inference] `push`, `schedule`, and `workflow_dispatch` are the best-aligned initial split of workflow roles in this repo. | https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml | medium | Existing precedent |
| [inference] STORM-like synthesis should be selective, not default. | https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | Use for ambiguity |
| [inference] New digests should stay inside the existing synthesis-item schema. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | No parallel store |
| [inference] Working-memory summaries plus archival full items match the repo's needs. | https://docs.letta.com/guides/ade/archival-memory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md | medium | Memory split |

**Assumptions**

- [assumption] The corpus will remain modest enough through the next implementation phase that graph JSON generation, per-item summary refresh, and static D3 layout computation all fit comfortably inside a normal GitHub Actions run. Justification: the existing site-build workflow already regenerates derived artifacts on `push`, and D3 explicitly supports offline computation of static layouts. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://d3js.org/d3-force/simulation]
- [assumption] Existing `cites` and `related` metadata can be populated consistently enough to become useful edge types in the first graph build without adding a new annotation workflow first. Justification: recent completed items already use these fields materially, so the graph can start from them and improve over time. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]

**Analysis**

The decisive design move is to separate structure generation from interpretation rather than trying to make one artifact serve both perfectly. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

That separation produces a coherent stack: Python scripts extract summaries and edges into JSON, D3 renders graph navigation from that JSON, and a later synthesis workflow consumes those same artifacts to decide what deserves LLM reasoning. [inference; source: https://d3js.org/d3-force/simulation; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

The most important trade-off is freshness versus cost, not simple automation versus manual work. [inference; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

Refreshing deterministic artifacts on every `push` gives immediate navigability at low risk, while delaying expensive distillation to a weekly schedule keeps the active requirement without paying STORM-like costs after every single completion. [inference; source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://arxiv.org/abs/2402.14207]

The graph-format choice follows the same logic: graph JSON is operationally simplest, D3 is interaction-rich enough for the full map, Mermaid remains useful for small embedded cluster views, and JSON-LD preserves future interoperability without complicating the primary pipeline. [inference; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://json-ld.org/]

This also keeps the system legible to reviewers, because every synthesized conclusion can point back to stable source items, summary artifacts, and explicit cluster manifests instead of disappearing into an opaque vector store or a one-shot whole-corpus prompt. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://docs.letta.com/guides/ade/archival-memory]

**Risks, gaps, uncertainties**

- The recommendation is strongest on architecture shape and weakest on exact cluster-quality thresholds, because the sources support layered selection and synthesis more clearly than they specify the precise heuristic cutoffs that will work best for this corpus. [inference; source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- The evidence for Open Knowledge Maps and Obsidian Publish supports the value of graph navigation, but it does not by itself prove which specific interaction design will be optimal for this repository's tag density and link structure. [inference; source: https://openknowledgemaps.org/; https://obsidian.md/publish]
- STORM provides strong evidence that multi-perspective pre-writing improves broad synthesis, but it is an article-generation system rather than a repository-governance workflow, so the recommendation to use it selectively remains an architectural inference rather than a direct product-level prescription. [inference; source: https://arxiv.org/abs/2402.14207]
- Embeddings may still become necessary later if heuristic cluster formation degrades as the corpus grows, but current evidence does not justify making them part of the baseline architecture before W-0025 is revived. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]

**Open Questions**

- At what corpus size or cluster-count does heuristic cluster formation stop being good enough and require persisted embeddings or another semantic-retrieval layer? [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- Which edge types should be weighted most heavily in the first graph: `cites`, `related`, shared tags, or shared extracted concepts from summaries? [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]
- Should active weekly digests update `learnings.md` automatically, open a draft synthesis item automatically, or do both depending on whether the new insight is thematic or transient? [inference; source: https://github.com/davidamitchell/Research/blob/main/learnings.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]

### §7 Recursive Review

- Label audit: completed.
- Acronym expansion audit: completed for AI, LLM, RAG, API, MCP, IDE, HTML, JSON, JSON-LD, YAML, REST, and STORM.
- [inference] The remaining uncertainty is confined to implementation thresholds and user-interface detail, not to the core recommendation that deterministic artifacts should be generated continuously while interpretive synthesis should be selective and scheduled. [source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

---

## Findings

### Executive Summary

The best-fit architecture is a hybrid, file-based stack that refreshes deterministic graph and summary artifacts on every corpus change, then applies Large Language Model (LLM) synthesis only to shortlisted clusters or queries rather than to the whole corpus each time. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://arxiv.org/abs/2402.14207]

For the knowledge map, a precomputed nodes-and-edges JSON file rendered as a static D3 force graph is the most scalable default for a roughly 200-item GitHub Pages corpus, while Mermaid should be reserved for small thematic subgraphs and JSON-LD should be emitted as an interoperability export rather than as the primary runtime index. [inference; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://json-ld.org/; https://obsidian.md/publish; https://openknowledgemaps.org/]

For active insight generation, the lowest-risk trigger pattern is push-driven index refresh plus scheduled weekly distillation and on-demand `workflow_dispatch` query synthesis, because `push` keeps artifacts fresh, `schedule` amortizes expensive multi-item reasoning, and manual dispatch preserves a website-only control surface for ad hoc questions. [inference; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

The retrieval layer should follow a Letta-style memory split: distilled per-item summaries, cluster manifests, and recent digests stay in prompt-resident working context, while the full Markdown corpus and graph artifacts remain searchable archival state on disk, which keeps provenance explicit without requiring a persistent database. [inference; source: https://docs.letta.com/guides/ade/archival-memory; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md]

### Key Findings

1. **This repository should use heuristic relationship extraction and cluster formation as the backbone of the system, and reserve LLM synthesis for bounded candidate sets, because the corpus already exposes explicit signals such as tags, `cites`, `related`, and changed files that are cheap to compute and safer than whole-corpus prompting.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
2. **A document-summary index pattern is the best first retrieval layer for active synthesis in this repo, because it stores one summary per item, retrieves whole documents by summary relevance, and fits the file-based constraints better than introducing vector infrastructure before W-0025 is revived.** ([inference]; medium confidence; source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md)
3. **A D3 force-directed graph over graph JSON is the most scalable default knowledge-map renderer for a roughly 200-item public corpus, while Mermaid is better treated as a low-cost derivative for small subgraphs rather than as the primary full-corpus map.** ([inference]; high confidence; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://obsidian.md/publish)
4. **Graph JSON should be the primary runtime artifact and JSON-LD should be a secondary export, because graph JSON is the simplest structure for Python transforms and browser rendering, while JSON-LD adds semantic interoperability without being the easiest working format for static graph navigation.** ([inference]; medium confidence; source: https://json-ld.org/; https://d3js.org/d3-force/simulation)
5. **The best-aligned initial trigger design is `push` for deterministic artifact refresh, `schedule` for weekly or batched distillation, and `workflow_dispatch` for ad hoc synthesis, because the repository already uses those patterns successfully and each trigger aligns with a distinct cost and freshness profile.** ([inference]; medium confidence; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml)
6. **STORM-like multi-perspective synthesis should be a selective second-stage method for broad, ambiguous, or contradiction-heavy clusters rather than the default path, because it improves organization and breadth but carries materially higher reasoning and orchestration cost than deterministic selection plus ordinary synthesis prompts.** ([inference]; medium confidence; source: https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
7. **The repository should publish new synthesized insights as ordinary completed synthesis items plus targeted `learnings.md` updates, not as a new content store, because the current item schema already supports citations, confidence, provenance, and version history for exactly this kind of output.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
8. **A Letta-style memory split is the right mental model for the synthesis interface, with summaries and recent digests acting as working memory and the full corpus acting as searchable archival memory, because that preserves provenance and keeps prompt size bounded without requiring a standing service.** ([inference]; medium confidence; source: https://docs.letta.com/guides/ade/archival-memory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Heuristic signals should shortlist items before any synthesis call. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | Cost control |
| [inference] A document-summary index pattern is the best first retrieval layer. | https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md | medium | File-based fit |
| [inference] D3 over graph JSON is the default full-corpus map. | https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://obsidian.md/publish | high | Mermaid for subgraphs |
| [inference] Graph JSON should be primary and JSON-LD derivative. | https://json-ld.org/; https://d3js.org/d3-force/simulation | medium | Export split |
| [inference] `push`, `schedule`, and `workflow_dispatch` are the best-aligned initial split of workflow roles in this repo. | https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml | medium | Existing precedent |
| [inference] STORM-like synthesis should be selective, not default. | https://arxiv.org/abs/2402.14207; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | Use for ambiguity |
| [inference] New digests should stay inside the existing synthesis-item schema. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md | medium | No parallel store |
| [inference] Working-memory summaries plus archival full items match the repo's needs. | https://docs.letta.com/guides/ade/archival-memory; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md | medium | Memory split |

### Assumptions

- [assumption] The corpus will remain modest enough through the next implementation phase that graph JSON generation, per-item summary refresh, and static D3 layout computation all fit comfortably inside a normal GitHub Actions run. Justification: the existing site-build workflow already regenerates derived artifacts on `push`, and D3 explicitly supports offline computation of static layouts. [source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://d3js.org/d3-force/simulation]
- [assumption] Existing `cites` and `related` metadata can be populated consistently enough to become useful edge types in the first graph build without adding a new annotation workflow first. Justification: recent completed items already use these fields materially, so the graph can start from them and improve over time. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]

### Analysis

The decisive design move is to separate structure generation from interpretation rather than trying to make one artifact serve both perfectly. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-18-api-context-hubs-rag-mcp.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]

That separation produces a coherent stack: Python scripts extract summaries and edges into JSON, D3 renders graph navigation from that JSON, and a later synthesis workflow consumes those same artifacts to decide what deserves LLM reasoning. [inference; source: https://d3js.org/d3-force/simulation; https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

The most important trade-off is freshness versus cost, not simple automation versus manual work. [inference; source: https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

Refreshing deterministic artifacts on every `push` gives immediate navigability at low risk, while delaying expensive distillation to a weekly schedule keeps the active requirement without paying STORM-like costs after every single completion. [inference; source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/build_site.yml; https://arxiv.org/abs/2402.14207]

The graph-format choice follows the same logic: graph JSON is operationally simplest, D3 is interaction-rich enough for the full map, Mermaid remains useful for small embedded cluster views, and JSON-LD preserves future interoperability without complicating the primary pipeline. [inference; source: https://d3js.org/d3-force/simulation; https://mermaid.js.org/syntax/flowchart.html; https://json-ld.org/]

This also keeps the system legible to reviewers, because every synthesized conclusion can point back to stable source items, summary artifacts, and explicit cluster manifests instead of disappearing into an opaque vector store or a one-shot whole-corpus prompt. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://docs.letta.com/guides/ade/archival-memory]

### Risks, Gaps, and Uncertainties

- The recommendation is strongest on architecture shape and weakest on exact cluster-quality thresholds, because the sources support layered selection and synthesis more clearly than they specify the precise heuristic cutoffs that will work best for this corpus. [inference; source: https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- The evidence for Open Knowledge Maps and Obsidian Publish supports the value of graph navigation, but it does not by itself prove which specific interaction design will be optimal for this repository's tag density and link structure. [inference; source: https://openknowledgemaps.org/; https://obsidian.md/publish]
- STORM provides strong evidence that multi-perspective pre-writing improves broad synthesis, but it is an article-generation system rather than a repository-governance workflow, so the recommendation to use it selectively remains an architectural inference rather than a direct product-level prescription. [inference; source: https://arxiv.org/abs/2402.14207]
- Embeddings may still become necessary later if heuristic cluster formation degrades as the corpus grows, but current evidence does not justify making them part of the baseline architecture before W-0025 is revived. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]

### Open Questions

- At what corpus size or cluster-count does heuristic cluster formation stop being good enough and require persisted embeddings or another semantic-retrieval layer? [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/]
- Which edge types should be weighted most heavily in the first graph: `cites`, `related`, shared tags, or shared extracted concepts from summaries? [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]
- Should active weekly digests update `learnings.md` automatically, open a draft synthesis item automatically, or do both depending on whether the new insight is thematic or transient? [inference; source: https://github.com/davidamitchell/Research/blob/main/learnings.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]

---

## Output

- Type: knowledge
- Description: Recommends a hybrid file-based architecture with graph JSON plus D3 for navigation, summary and cluster artifacts for retrieval, scheduled LLM distillation over changed clusters, and `workflow_dispatch` query synthesis, while keeping JSON-LD as an export layer rather than the primary runtime index. [inference; source: https://d3js.org/d3-force/simulation; https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/; https://json-ld.org/; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]
- Links:
  - https://arxiv.org/abs/2402.14207
  - https://developers.llamaindex.ai/python/examples/index_structs/doc_summary/docsummary/
  - https://d3js.org/d3-force/simulation
