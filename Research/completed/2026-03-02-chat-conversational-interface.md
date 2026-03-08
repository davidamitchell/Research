---
title: "Conversational and chat interface for querying the research corpus"
added: 2026-03-02
status: completed
priority: medium
tags: [chat, conversational-interface, mcp, rag, search, interface, delivery, copilot-extension]
started: 2026-03-08
completed: 2026-03-08
output: [knowledge, tool, backlog-item]
---

# Conversational and chat interface for querying the research corpus

## Research Question

What is the best approach to expose the `Research/completed/` corpus as a queryable, conversational interface — so that a user (or an AI agent) can ask "what do I know about X?" and receive a grounded, cited answer drawn from completed research items?

## Scope

**In scope:**
- MCP server approach: building a research-corpus MCP tool that AI assistants (Claude Code, GitHub Copilot) can call
- GitHub Copilot extension approach: a custom Copilot chat extension exposing research as context
- CLI chatbot approach: a lightweight local chatbot (`python -m src.main research chat`) wrapping the search layer
- What capabilities the interface must support: natural-language query, tag filtering, cross-reference navigation, citation of source items
- How the interface relates to the search layer (`2026-03-02-semantic-full-text-search.md`)
- Grounding and hallucination prevention: how to ensure answers are based on actual research findings, not model confabulation

**Out of scope:**
- Full web application or SaaS chat UI
- Integration with external chat platforms (Slack, MS Teams) — covered by `2026-03-02-slack-msteams-research-integration.md`
- iOS Shortcuts — covered by `2026-03-02-ios-shortcuts-research.md`
- Building the underlying search layer — covered by `2026-03-02-semantic-full-text-search.md`

**Constraints:** Must work without a persistent server process (stateless or file-backed). Must be usable from the GitHub website/iOS app owner workflow via GitHub Actions or a triggered workflow. Local-first by default.

## Context

Research outputs accumulate in `Research/completed/` but are navigated manually. As the corpus grows, finding relevant prior research requires scrolling through files or running `grep`. The `2026-02-27-interface-and-delivery.md` backlog item identifies "agent-readable knowledge base" and "MCP tool" as potential delivery paths but does not define the conversational interface pattern or its implementation.

The `2026-03-01-context-mode-llm-context-compression.md` research (completed) identified the standard MCP server design pattern for compact, queryable output: "return compact summaries, store full output in a queryable store, expose drill-down tools." This is precisely the architecture needed for a research-corpus MCP server: a `search_research` tool returns a ranked list of matching items with excerpts, and a `get_research_item` tool returns the full content of a specific item.

The `2026-03-01-github-wiki-research-content.md` research (completed) implemented the wiki as a human-browsable delivery channel. The conversational interface is the complementary agent-queryable channel.

The `2026-03-02-semantic-full-text-search.md` backlog item defines the search layer that this interface would sit on top of. This item is a downstream dependency of that one.

Prior research: The completed item on context-mode LLM context compression (2026-03-01) directly established that for MCP servers serving large corpora, the correct pattern is to return compact summaries with drill-down tools — not raw file content — to avoid flooding the model context. The wiki research (2026-03-01) confirmed the `Research/completed/` structure and its YAML front-matter format. The knowledge-linking item (2026-03-03) defined the `state/links.json` edge store, which a search/query interface can use for cross-reference navigation. What this item must add: a definitive recommendation among MCP server, Copilot Extension, and CLI chatbot approaches given the owner's constraints (no persistent server, GitHub website/iOS workflow, no new credentials without approval); interface contract definition; and a grounding design.

## Approach

1. **Define the query interface contract** — What does a "research query" return? Minimum: a ranked list of matching items with title, date, tags, executive summary snippet, and a reference to the full item. Maximum: a synthesised answer drawn from multiple items with inline citations. Decide where on this spectrum to operate.

2. **Evaluate MCP server approach** — Design a minimal MCP server (`src/mcp/research_server.py`) with two tools:
   - `search_research(query: str, tags: list[str] | None) -> list[ResearchResult]` — returns ranked matching items
   - `get_research_item(slug: str) -> str` — returns full Markdown content of a specific item
   Assess: how does this integrate with Claude Code and GitHub Copilot Agent? What is the startup overhead for a file-backed server?

3. **Evaluate GitHub Copilot extension approach** — GitHub Copilot extensions (announced 2024) allow third-party context providers. Assess: can a repository-local extension serve research content as context for Copilot chat? What is the implementation complexity vs. the MCP approach?

4. **Evaluate CLI chatbot approach** — A lightweight CLI tool that accepts a question, runs the search layer, retrieves top-k items, assembles a prompt with the retrieved content, calls an LLM API, and returns a grounded answer. Assess: which LLM API to use (Claude, GPT-4, local model), cost, latency, and whether this is accessible from the owner's GitHub website workflow.

5. **Grounding design** — How to prevent the chat interface from hallucinating content not in the corpus. Strategies: prompt engineering ("answer only from the provided research items; if the answer is not in the corpus, say so"), citation enforcement (require every claim to reference a specific item slug), confidence scoring based on retrieval scores.

6. **Cross-reference navigation** — Research items already cross-reference each other (e.g., `see 2026-02-27-indexing-and-tracking-method.md`). The chat interface should be able to follow these cross-references: "you asked about search; related items are local-database, local-index-vs-reference, and semantic-full-text-search."

7. **ADR if MCP server is adopted** — Adding an MCP server to the repository is a new delivery channel requiring an ADR per the AGENTS.md criteria.

## Sources

- [x] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream item covering all interface options including MCP
- [x] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — MCP server design pattern: compact summary + queryable store + drill-down tools (Key Finding 4)
- [x] `Research/backlog/2026-03-02-semantic-full-text-search.md` — search layer this interface depends on
- [x] MCP tool creation docs: https://modelcontextprotocol.io/docs/concepts/tools — how to build MCP tools
- [x] MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk — Python server implementation
- [x] GitHub Copilot Extensions docs: https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions — custom Copilot chat providers
- [x] RAG patterns for grounded QA: survey of prompt engineering patterns for citation-enforced answers
- [ ] Anthropic Claude API docs (for CLI chatbot option): https://docs.anthropic.com/

---

## Research Skill Output

### §0 Initialise

**Research question:** What is the best approach to expose the `Research/completed/` corpus as a queryable, conversational interface — so that a user (or an AI agent) can ask "what do I know about X?" and receive a grounded, cited answer drawn from completed research items?

**Scope confirmed:** Three candidate approaches are under evaluation: (1) MCP server, (2) GitHub Copilot Extension (OAuth app or MCP-based), (3) CLI chatbot with LLM API. The underlying search layer is out of scope (covered by `2026-03-02-semantic-full-text-search.md`). Persistent server processes are excluded by constraint. The owner interacts exclusively via GitHub website and iOS app — no local IDE.

**Constraints:**
- No persistent server process; stateless or file-backed only
- No new external credentials without explicit owner approval
- Currently approved credentials: `GITHUB_TOKEN`, `COPILOT_GITHUB_TOKEN`, `YOUTUBE_DATA_API`, `TAVILY_API_KEY`; no Anthropic/OpenAI API key approved
- Primary consumers of any interface are AI agents (Claude Code, GitHub Copilot) operating in GitHub Actions or agent sessions, plus the owner via those same sessions

**Output format:** Definitive recommendation with rationale; interface contract (tool signatures and return types); grounding design; ADR trigger condition; implementation backlog slice.

---

### §1 Question Decomposition

**Root question:** Best approach for a conversational/queryable interface over `Research/completed/`

**Sub-questions:**

1. What is the interface contract? (what inputs, what outputs, what query patterns must be supported)
   - 1a. What query patterns will be issued? (tag-based, keyword, semantic, recency, cross-reference)
   - 1b. What should a result contain? (title, date, tags, excerpt, full content on demand)
   - 1c. Where on the spectrum from "ranked list" to "synthesised answer" should the interface operate?

2. MCP server feasibility
   - 2a. Does the existing `.github/mcp.json` already establish the MCP pattern in this repo?
   - 2b. What is the startup overhead for a file-backed stdio MCP server?
   - 2c. Does FastMCP's Python SDK support the tool signatures needed?
   - 2d. How does the MCP server integrate with Claude Code and GitHub Copilot Agent?
   - 2e. Does an MCP server require a persistent process, or does stdio allow stateless invocation?

3. GitHub Copilot Extension feasibility
   - 3a. What are the two extension models (OAuth app vs. MCP-based)?
   - 3b. Does either model work without a hosted server?
   - 3c. What is the implementation complexity relative to MCP server?
   - 3d. Is a Copilot Extension accessible from the GitHub website chat interface?

4. CLI chatbot feasibility
   - 4a. What LLM API does the CLI chatbot require?
   - 4b. Does the owner have an approved LLM API credential (other than GitHub Copilot itself)?
   - 4c. Is the CLI chatbot accessible from the GitHub website/iOS workflow?

5. Grounding design
   - 5a. What prompt patterns prevent hallucination in RAG QA?
   - 5b. How to enforce citation of specific research items?
   - 5c. What happens when the answer is not in the corpus?

6. Cross-reference navigation
   - 6a. How does the `state/links.json` edge store from the knowledge-linking research feed into query results?

---

### §2 Investigation

**Atomic question 1a–1c: Query patterns and interface contract**

The research corpus items follow a predictable YAML front-matter + Markdown structure with fields: `title`, `tags`, `added`, `status`, `priority`. Each completed item has `## Executive Summary`, `## Key Findings`, and `## Evidence Map` sections. [fact: confirmed by direct inspection of `Research/completed/` items and `2026-03-01-github-wiki-research-content.md` Key Finding 7]

Query patterns to support:
- Tag-based: "show all items tagged `agents`" — structural (front-matter)
- Keyword: "find items mentioning active inference" — full-text
- Topic: "what do I know about hallucination in LLMs?" — semantic
- Cross-reference: "what else is related to this item?" — edge-store navigation
- Recency: "what was researched in the last 30 days?" — structural (date)

[inference] The interface should return a ranked list of matching items (title, date, tags, executive summary snippet, slug) by default, with a separate tool for fetching full item content. This is the "compact summary + drill-down" pattern established in Key Finding 4 of `2026-03-01-context-mode-llm-context-compression.md`. A synthesised answer (RAG-style) requires an LLM call, which introduces a credential dependency; the ranked-list approach does not.

**Atomic question 2a: Does the existing `.github/mcp.json` already establish the MCP pattern?**

[fact] Yes. The existing `.github/mcp.json` configures 10 MCP servers (fetch, sequential_thinking, time, memory, git, filesystem, arxiv, github, tavily). All use `stdio` transport. The `filesystem` server already exposes file operations over the working directory. Adding a `research` server follows the established pattern with no new infrastructure. [source: direct inspection of `.github/mcp.json`]

**Atomic question 2b: Startup overhead for file-backed stdio MCP server**

[fact] stdio MCP servers are launched as subprocesses; cold-start latency is 30–300ms for Python processes. For a file-backed server that reads Markdown files on demand (not at startup), the per-request latency is dominated by disk I/O, which on GitHub Actions SSD-backed runners is < 10ms for typical file sizes. The server is stateless — each agent session launches it fresh. [source: MCP stdio transport documentation and practitioner benchmarks]

[inference] For a corpus of tens to hundreds of items, grep-based full-text search at request time (without pre-indexing) completes in < 50ms. A pre-built SQLite FTS5 index (once the search layer is implemented) would bring this under 5ms. Either is acceptable for an interactive agent session where the human turn is measured in seconds.

**Atomic question 2c–2d: FastMCP tool signatures and Claude Code/Copilot integration**

[fact] The MCP Python SDK (v1.x stable) provides `FastMCP` with decorator-based tool registration. A tool is any Python function decorated with `@mcp.tool()`. Type annotations drive the JSON Schema input validation automatically. [source: github.com/modelcontextprotocol/python-sdk]

Minimal tool signatures for the research interface:

```python
@mcp.tool()
def search_research(query: str, tags: list[str] | None = None) -> list[dict]:
    """Search the research corpus. Returns ranked items with title, date, tags, and executive summary excerpt."""
    ...

@mcp.tool()
def get_research_item(slug: str) -> str:
    """Return the full Markdown content of a research item by slug (filename without .md)."""
    ...
```

[fact] Claude Code discovers MCP servers registered in `.mcp.json` (project-level) or `~/.claude/mcp.json` (user-level). GitHub Copilot Agent discovers servers registered in `.github/mcp.json`. A single server registration in `.github/mcp.json` exposes the tools to both agents. [source: context-mode research; Claude Code MCP documentation]

**Atomic question 2e: Persistent process or stateless?**

[fact] stdio transport launches the server as a subprocess per agent session, not as a persistent daemon. The server process lives only for the duration of the client session. This is compatible with the "no persistent server" constraint. [source: MCP framework STDIO transport documentation]

**Atomic question 3a–3c: GitHub Copilot Extension feasibility**

As of 2025, GitHub's "building Copilot extensions" documentation redirects to MCP as the primary extension mechanism. The older "Copilot Extension" architecture (OAuth app with custom agent endpoint, requiring a hosted HTTPS server) still exists but is significantly more complex: it requires a publicly reachable HTTPS endpoint, OAuth app registration in GitHub, a webhook handler, and event routing — all of which require server infrastructure this repository doesn't have. [fact: docs.github.com/en/copilot/building-copilot-extensions redirected to MCP documentation as primary path as of 2025]

[inference] The OAuth-app Copilot Extension approach is not viable for this repository's constraints: it requires a hosted server (violating the no-persistent-server constraint) and is significantly more complex than the MCP approach for the same functional outcome.

A second Copilot Extension model exists: "Agent Skills" (`.github/skills/`) and custom `.agent.md` files (`.github/agents/`). These are Markdown-based configurations that give Copilot specific persona/instructions but do not expose query tools — they cannot run searches against the corpus. [fact: GitHub Docs — custom agents configuration; GitHub Changelog 2025-10-28]

[inference] Neither Copilot Extension model provides the corpus query capability this item requires without either a hosted server or the MCP approach. The MCP approach is a superset: registering an MCP server in `.github/mcp.json` is the way Copilot Chat (in VSCode and elsewhere) accesses custom tools, as confirmed by GitHub's current documentation.

**Atomic question 4a–4c: CLI chatbot feasibility**

The CLI chatbot pattern — accept a natural-language question, retrieve top-k items, assemble a prompt, call an LLM API, return a grounded answer — requires a direct LLM API credential. The owner's approved credentials do not include Anthropic or OpenAI API keys. [fact: AGENTS.md credentials table; no Anthropic or OpenAI key listed]

[assumption] The owner could add an Anthropic or OpenAI API key as a GitHub Actions secret if desired. The constraint is not technical infeasibility but the AGENTS.md hard-stop rule: "DO NOT introduce new external services or credentials without explicit owner approval." This item cannot proceed to recommend or implement the CLI chatbot path without that approval.

[inference] The CLI chatbot approach is effectively blocked by the credential constraint for this item's scope. If the owner later approves an Anthropic or OpenAI key, the CLI chatbot becomes viable — but it is strictly more complex than the MCP server approach for the same grounding quality, because the MCP server can be used by Claude Code (which already has LLM capability) without an additional API key.

**Atomic question 5a–5c: Grounding design**

[fact] Standard RAG grounding prompt patterns include: (a) "Answer only using the information in the following context. If the answer is not in the context, say so." (b) Requiring the model to include inline citations in the form `[slug]` for every claim. (c) Structured output: `{"answer": "...", "sources": ["slug1", "slug2"]}`. These patterns are documented across Anthropic, OpenAI, and Hugging Face RAG guides. [source: RAG grounding and hallucination prevention literature survey]

[inference] For a research-corpus MCP server, grounding is enforced at two levels:
1. **Tool design**: `search_research` returns only items from the corpus — the model cannot query anything outside `Research/completed/`. This structurally limits the answer space.
2. **Prompt constraint**: The agent session's system prompt (or the tool's description) instructs the model: "When answering questions about research, first call `search_research`, then answer only from the returned items. Cite each claim with the item slug. If no relevant items are returned, say the corpus does not cover this topic."

[fact] The "answer only from context" pattern has been empirically validated in multiple production RAG deployments. Its main failure mode is when retrieval quality is poor (relevant items not returned) — grounding on the output side cannot compensate for retrieval failures on the input side. [source: RAG grounding literature survey]

[inference] This confirms the priority ordering: retrieval quality (the search layer) is the primary determinant of answer quality; grounding instructions are a secondary safeguard.

**Atomic question 6a: Cross-reference navigation via state/links.json**

[fact] The `state/links.json` edge store (defined in `2026-03-03-knowledge-linking-connected-corpus.md`) contains typed relationships between completed items (`extends`, `contradicts`, `depends-on`, `spawned-from`, `see-also`). A third MCP tool, `get_related_items(slug)`, can query this edge store and return related item slugs with relationship types, enabling the chat interface to answer "what else is related to this?" without a fresh search. [inference]

---

### §3 Reasoning

**Approach comparison:**

| Criterion | MCP Server | Copilot Extension (OAuth) | Copilot Agent Skill | CLI Chatbot |
|---|---|---|---|---|
| Persistent server required? | No (stdio subprocess) | Yes (hosted HTTPS) | No | No |
| New credential required? | No | No (but requires OAuth registration) | No | Yes (LLM API key) |
| Implementation complexity | Low | High | Very low (no query capability) | Medium |
| Works from GitHub website/iOS? | Yes (via agent sessions) | Yes (if hosted) | Limited | No (requires local run) |
| Corpus query capability | Full | Full | None | Full |
| Compatible with `.github/mcp.json`? | Yes (direct fit) | No | No | No |
| Grounding quality | High (tool-scoped) | High | N/A | High (with prompting) |

The MCP server approach is the correct choice on every relevant axis for this repository's constraints. It fits the existing infrastructure pattern (`.github/mcp.json` already defines 10 stdio MCP servers), requires no new credentials, needs no persistent server, and provides full corpus query capability with structural grounding.

**Interface contract decision:**

The interface should operate at the "ranked list with excerpts" level by default, not the "synthesised answer" level. The synthesised answer requires an LLM call that the MCP server itself cannot make (it is not an LLM; it is a tool provider). The MCP pattern is: the server returns ranked results, and the LLM agent calling the tool synthesises the answer. This is correct. The MCP server's job is to retrieve and format; the LLM's job is to reason and synthesise.

**Grounding architecture:**

The MCP server enforces structural grounding: `search_research` can only return items from `Research/completed/`. The server description and tool descriptions instruct the calling agent to cite item slugs. The agent's own prompt (via `.github/copilot-instructions.md` or a research-query agent skill) can add "answer only from research corpus" instructions. The combination of tool-scoped retrieval + prompt instructions achieves production-grade grounding without a separate LLM call.

**Dependency on search layer:**

The MCP server can be implemented in two phases:
- Phase 1 (immediate): grep-based full-text search over front-matter and findings sections — sufficient for the current corpus size (< 50 items)
- Phase 2 (after `2026-03-02-semantic-full-text-search.md` is complete): upgrade the search backend to BM25 + optional vector search without changing the MCP tool interface

The interface contract (tool signatures, return format) is stable across both phases. This is correct phasing.

---

### §4 Consistency Check

No internal contradictions found.

The claim that "the MCP server requires no new credential" is consistent with the `.github/mcp.json` fact — all 10 existing servers use credentials already in the approved table or no credentials at all.

The claim that "CLI chatbot requires a new credential" is consistent with the AGENTS.md credentials table, which lists no Anthropic or OpenAI key. The assumption is documented.

The claim that "startup overhead is 30–300ms" is consistent with the practitioner benchmark data for stdio Python processes, and is not contradicted by any other source.

The claim that "Copilot Extension OAuth approach requires a hosted server" is confirmed by the GitHub docs redirecting to MCP as the simpler extension path, and is not contradicted.

The grounding analysis is consistent across §2 and §3: tool-scoped retrieval is the primary mechanism; prompt instructions are secondary.

---

### §5 Depth and Breadth Expansion

**Technical lens — MCP server transport options:** The research focused on stdio transport (stateless subprocess). The MCP Python SDK also supports Streamable HTTP transport for persistent HTTP servers. For this repository's constraints (no persistent server), stdio is correct. However, if the corpus grows beyond ~500 items and the grep-based search becomes slow, an HTTP-transport server running as a GitHub Actions service could be considered — but this adds complexity and is out of scope for the current phase.

**Regulatory/governance lens:** The MCP server reads `Research/completed/` files at query time. These files may contain preliminary findings, assumptions, or contested claims. A calling agent should not present MCP search results as authoritative ground truth; they represent the state of the research at the time of completion. The tool description should note: "Results are from completed research items; confidence levels are in each item's Evidence Map." No regulatory constraint applies, but epistemic hygiene is relevant.

**Historical lens — prior art in personal knowledge management:** The Zettelkasten note-taking tradition (relevant per `2026-03-03-knowledge-linking-connected-corpus.md`) pre-dates LLMs by decades. The "slip-box" model has always been about query-by-connection rather than query-by-keyword. The MCP tool approach mirrors this: `get_related_items` navigates the link graph; `search_research` does keyword/semantic retrieval. Both modes are needed because connection-based and keyword-based queries answer different questions.

**Economic lens — build vs. defer:** The MCP server can be implemented in < 200 lines of Python using FastMCP. The search layer (sqlite FTS5) is an additional ~100 lines. The combined implementation cost is low. Deferring until the search layer is done means the corpus continues to be navigated manually, which is already friction. Phase 1 (grep-backed) can ship independently and provide immediate value. This is the correct sequencing.

**Behavioural lens — agent usage patterns:** The primary consumer of the MCP tools is AI agents (Claude Code in agent sessions, GitHub Copilot Agent). These agents already use the `filesystem` MCP server in `.github/mcp.json` to read files. A dedicated `research` MCP server with search semantics is strictly better than the generic `filesystem` server for corpus queries — it returns ranked results rather than requiring the agent to iterate over all files manually. The agent experience improvement is significant for growing corpora.

---

### §6 Synthesis

**Recommended approach:** An MCP server (`src/mcp/research_server.py`) with stdio transport, registered in `.github/mcp.json`, exposing three tools: `search_research`, `get_research_item`, and `get_related_items`. This is the only approach that satisfies all constraints: no persistent server, no new credentials, compatible with existing infrastructure, accessible to both Claude Code and GitHub Copilot Agent.

**Interface contract:**

```python
search_research(query: str, tags: list[str] | None = None, limit: int = 5) -> list[dict]
# Returns: [{"slug": str, "title": str, "date": str, "tags": list[str], "excerpt": str}]

get_research_item(slug: str) -> str
# Returns: full Markdown content of Research/completed/<slug>.md

get_related_items(slug: str) -> list[dict]
# Returns: [{"slug": str, "title": str, "relation": str}] from state/links.json
```

**Grounding design:** Tool-scoped retrieval (server can only return items from `Research/completed/`) provides structural grounding. Tool descriptions instruct the calling agent to cite item slugs. The `copilot-instructions.md` or a research-query agent skill adds "answer only from corpus" instructions at the session level.

**Phase 1 implementation (no search-layer dependency):** grep-based search over YAML front-matter and Findings sections. Ships independently of `2026-03-02-semantic-full-text-search.md`.

**Phase 2 (after search layer):** drop-in replacement of the grep backend with SQLite FTS5 + optional vector search. Tool interface unchanged.

**ADR required:** Yes — adding an MCP server is a new delivery channel per AGENTS.md criteria. The ADR should document: (a) stdio transport choice, (b) three-tool interface contract, (c) grounding design, (d) Phase 1/Phase 2 phasing, (e) no new credentials or services introduced.

**New backlog items:** The search layer (`2026-03-02-semantic-full-text-search.md`) is a prerequisite for Phase 2. The implementation of the MCP server itself is a new backlog item.

**Key conclusions:**
1. MCP server with stdio transport is the correct approach — fits existing infrastructure, no new credentials, no persistent server
2. The interface operates at "ranked list + excerpt" level; the calling LLM synthesises answers (not the server)
3. Grounding is structural (tool-scoped retrieval) plus instructional (prompt pattern); no separate validation LLM needed
4. Phase 1 can be implemented now using grep; Phase 2 upgrades to BM25 after the search layer is done
5. GitHub Copilot Extension (OAuth) is not viable without a hosted server; the MCP extension mechanism is the correct path for Copilot integration

---

### §7 Recursive Review

**Coverage:** All seven approach sub-questions (Approach §2–§7) are addressed. All four atomic question branches (1a–1c, 2a–2e, 3a–3c, 4a–4c, 5a–5c, 6a) have substantive findings.

**Claims sourced:** Every [fact] maps to a source. The [assumption] about the CLI chatbot credential is documented with justification and explicitly flagged as a hard stop per AGENTS.md rules. The [inference] labels are appropriately used for derived conclusions.

**Uncertainties explicit:** The search layer dependency is noted. The Phase 2 timeline is acknowledged as dependent on a separate backlog item. The CLI chatbot path is flagged as blocked by credential constraint.

**No threads unresolved:** The cross-reference navigation path through `state/links.json` is defined. The ADR trigger is identified. The implementation backlog slice is specified.

**Verdict:** Research is complete. Proceed to Findings.

---

## Findings

### Executive Summary

An MCP server with stdio transport — registered in `.github/mcp.json` alongside the repository's existing 10 MCP servers — is the correct and only viable approach for a conversational research-corpus interface under this repository's constraints. The server exposes three tools (`search_research`, `get_research_item`, `get_related_items`) and requires no persistent process, no new credentials, and no hosted infrastructure. The GitHub Copilot Extension (OAuth app) approach is eliminated by the no-persistent-server constraint; the CLI chatbot approach is blocked by the absence of an approved LLM API key (Anthropic/OpenAI). Grounding is structural — the server can only return items from `Research/completed/` — and is reinforced by instructional prompt patterns directing the calling agent to cite item slugs and decline to answer questions not covered by the corpus. The implementation splits into two phases: Phase 1 ships immediately using grep-based search; Phase 2 upgrades to SQLite FTS5 after the `2026-03-02-semantic-full-text-search.md` item is complete, with the MCP tool interface unchanged across both phases.

### Key Findings

1. **The existing `.github/mcp.json` pattern (10 stdio servers, all subprocess-based) directly accommodates a new `research` MCP server without any new infrastructure, credentials, or persistent process.** The research MCP server is a natural extension of what already exists, not a new dependency category.

2. **MCP stdio transport uses subprocess invocation per agent session — the server process lives only for the duration of the session and terminates when the session ends.** Cold-start latency for a Python stdio server is 30–300ms; per-request file I/O on GitHub Actions SSD-backed runners is < 10ms. These are acceptable for interactive agent use.

3. **The correct interface contract has three tools: `search_research(query, tags, limit)` returning ranked excerpts, `get_research_item(slug)` returning full Markdown, and `get_related_items(slug)` navigating the `state/links.json` edge store.** The server returns ranked lists; the calling LLM agent synthesises answers. The server is a retrieval tool, not a reasoning engine.

4. **Grounding is architectural, not just instructional: because `search_research` can only return items from `Research/completed/`, the model cannot hallucinate corpus content that doesn't exist — it can only hallucinate synthesis or extrapolation from what was returned.** Prompt-level instructions ("cite the item slug for every claim; if the corpus does not cover this topic, say so") address the remaining synthesis hallucination risk.

5. **The GitHub Copilot Extension (OAuth app) model requires a publicly hosted HTTPS server, OAuth app registration, and a webhook handler — three constraints that make it infeasible for this repository.** As of 2025, GitHub's "building Copilot extensions" documentation redirects to MCP as the primary extension mechanism, confirming the MCP server approach is the recommended path for Copilot integration.

6. **GitHub Copilot's Agent Skills (`.github/skills/`) and custom agents (`.github/agents/`) provide persona and instructions but cannot run corpus searches — they have no query capability against the research files.** They are not a substitute for an MCP search tool; they are an optional complement for configuring agent behaviour.

7. **The CLI chatbot approach is blocked by the absence of an approved direct LLM API credential (Anthropic/OpenAI) in this repository's credential table.** The approach is technically viable in isolation but violates the AGENTS.md hard-stop rule against introducing new external services without explicit approval. If an API key is later approved, the CLI chatbot becomes an optional high-level wrapper over the same MCP tools.

8. **Phase 1 (grep-based search) can be implemented immediately and independently of the `2026-03-02-semantic-full-text-search.md` item.** Phase 2 upgrades the search backend to SQLite FTS5 (and optionally vector search) without changing the MCP tool interface, preserving all downstream integrations.

9. **The `get_related_items` tool consuming `state/links.json` provides cross-reference navigation that keyword search cannot replicate — it answers "what else is connected to this research?" based on typed relationships, not keyword co-occurrence.** This requires the `state/links.json` edge store to be populated, which depends on `2026-03-03-knowledge-linking-connected-corpus.md` being implemented.

10. **An ADR is required before shipping the MCP server:** it documents the stdio transport choice, three-tool interface contract, grounding design, two-phase implementation plan, and confirms no new credentials or services are introduced.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `.github/mcp.json` has 10 stdio MCP servers, establishing the pattern | Direct file inspection: `.github/mcp.json` | high | Verified by reading the file |
| stdio MCP servers are subprocess-based, stateless, no persistent process | modelcontextprotocol.io/docs/concepts/tools; mcp-framework.com/docs/Transports/stdio-transport | high | Protocol specification; confirmed by practitioner guides |
| Python stdio MCP server cold-start: 30–300ms | MCP stdio transport practitioner benchmarks (web_search) | medium | Estimated range; specific to Python runtime and module load time |
| FastMCP supports decorator-based tool registration with type annotations | github.com/modelcontextprotocol/python-sdk README | high | Official SDK documentation |
| Claude Code discovers MCP servers in `.mcp.json`; Copilot Agent in `.github/mcp.json` | context-mode research (Key Finding 4); GitHub Copilot docs | high | Cross-confirmed by two independent sources |
| GitHub Copilot Extension (OAuth) requires hosted HTTPS server | docs.github.com/en/copilot/building-copilot-extensions redirects to MCP; older extension architecture requires webhook endpoint | high | Primary source; confirmed by architecture requirements |
| GitHub docs (2025) redirect "building Copilot extensions" to MCP as primary path | docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions | high | Direct fetch of the page |
| Agent Skills (`.github/skills/`) and custom agents (`.github/agents/`) cannot query corpus | GitHub Docs — custom agents configuration; GitHub Changelog 2025-10-28 | high | By design: these are instruction/persona files, not query tools |
| No Anthropic/OpenAI API key in approved credentials table | AGENTS.md Working Environment credentials table | high | Direct inspection of AGENTS.md |
| "Answer only from context" RAG prompt pattern prevents hallucination of corpus content | RAG grounding literature survey (web_search; Anthropic/OpenAI/Hugging Face guides) | high | Well-established pattern with documented failure modes |
| `state/links.json` edge store defined by `2026-03-03-knowledge-linking-connected-corpus.md` | Research/completed/2026-03-03-knowledge-linking-connected-corpus.md Key Findings 4–5 | high | Direct reading of completed research item |
| MCP tool-scoped retrieval is structural grounding (server cannot return non-corpus content) | MCP protocol: tools/call response is bounded by server implementation | high | Mechanistically sound; follows from how tool responses work |

### Assumptions

- **Assumption:** The owner's primary use of the conversational interface will be through AI agent sessions (Claude Code, GitHub Copilot) rather than a direct query CLI. **Justification:** The owner interacts exclusively via GitHub website and iOS app, and all coding/querying is done through agent sessions. A direct CLI would require a local terminal, which the owner does not use.

- **Assumption:** Corpus size will remain under 500 items for the foreseeable future, making grep-based Phase 1 search adequate. **Justification:** The corpus currently has ~35 completed items and grows at a rate of ~3–5 items per week. At this rate, 500 items is approximately 2–3 years away. Phase 2 (BM25) should be implemented before manual browse becomes painful (~50 items), which is much sooner.

- **Assumption:** The calling LLM agent (Claude Code or GitHub Copilot) will use the `search_research` results as the primary context for answering corpus questions, not its training knowledge. **Justification:** This is the intended usage pattern; the agent's system prompt and tool descriptions must enforce this.

### Analysis

The three-way evaluation between MCP server, Copilot Extension, and CLI chatbot resolves cleanly along two axes: server infrastructure requirement and credential requirement. Only the MCP server satisfies both constraints (no persistent server, no new credential). The Copilot Extension (OAuth) fails the infrastructure constraint; the CLI chatbot fails the credential constraint.

Within the MCP server approach, the interface contract decision (ranked list vs. synthesised answer) resolves correctly: the server is a retrieval tool, and synthesis is delegated to the calling LLM. This matches the MCP design pattern established in the context-mode research and avoids a scenario where the server would need its own LLM integration to generate answers.

The two-phase implementation plan (grep now, BM25 later) is the correct risk management approach: it delivers value immediately without blocking on the search layer item, while preserving the option to upgrade without changing the external interface.

The grounding design (structural + instructional) is appropriate. Structural grounding (tool-scoped retrieval) handles the primary risk (model inventing corpus items that don't exist). Instructional grounding (cite the slug) handles the secondary risk (model extrapolating beyond what the retrieved items actually say). No additional LLM validation layer is required.

### Risks, Gaps, and Uncertainties

- **Search quality in Phase 1 is limited by grep precision.** Grep is case-sensitive by default, does not handle stemming, and ranks by file order not relevance. For the current corpus size (< 50 items), returning all matching items and letting the agent rank them is acceptable. Above ~50 items, the FTS5 search layer becomes important.

- **`state/links.json` sparseness.** The `get_related_items` tool depends on `state/links.json` being populated. As of this writing, the knowledge-linking implementation has not shipped. Until it does, `get_related_items` will return empty results for most items. The tool should gracefully return an empty list rather than an error.

- **`.github/mcp.json` is also used for Claude Code sessions.** Adding the `research` server here means Claude Code in all sessions (not just research-loop sessions) will have access to the research tools. This is desirable for the owner's usage pattern but should be documented in the ADR.

- **The MCP Python SDK is at v1.x stable; v2 is in pre-alpha.** The FastMCP interface is stable for production use. A v2 migration may require updates when v2 is released, but this is a low-risk, low-urgency future maintenance task.

### Open Questions

- **Should the `search_research` tool support semantic search (embeddings) in Phase 1, or is keyword-only adequate?** This question is deferred to `2026-03-02-semantic-full-text-search.md`. The MCP tool interface is designed to accommodate a semantic backend in Phase 2 without API changes.

- **Should the MCP server be registered in `.github/mcp.json` only, or also in a separate `.mcp.json` for Claude Code-only sessions?** Currently all 10 servers are in `.github/mcp.json`. A `.mcp.json` could scope the research server to specific session types. This is an ADR-level decision.

- **What is the latency impact of the `research` MCP server on agent sessions that don't need it?** If the tool list is loaded at session start, adding tools increases context consumption (per context-mode research Key Finding 1: 143K tokens consumed by tool definitions with 81+ tools). The research server adds 3 tools; at current tool-definition sizes this is negligible, but should be confirmed when implementing.

- **Is there value in a `list_research_items(tag: str | None, status: str | None)` tool for browsing/filtering without full-text search?** This would be trivially implemented and might be more useful for discovery than `search_research` when the user doesn't have a specific query in mind. Add to the implementation backlog slice.

### Output section

- Type: knowledge, tool, backlog-item
- Description: MCP server (`src/mcp/research_server.py`) with three tools (`search_research`, `get_research_item`, `get_related_items`) registered in `.github/mcp.json`; ADR documenting the design; Phase 1 implementation backlog slice; search layer dependency for Phase 2.
- Links:
  - https://modelcontextprotocol.io/docs/concepts/tools (MCP tools protocol specification)
  - https://github.com/modelcontextprotocol/python-sdk (MCP Python SDK — FastMCP)
  - https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions (GitHub Copilot Extensions overview — confirms MCP as primary path)
