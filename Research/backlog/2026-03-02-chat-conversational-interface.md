---
title: "Conversational and chat interface for querying the research corpus"
added: 2026-03-02
status: backlog
priority: medium
tags: [chat, conversational-interface, mcp, rag, search, interface, delivery, copilot-extension]
started: ~
completed: ~
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

- [ ] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream item covering all interface options including MCP
- [ ] `Research/completed/2026-03-01-context-mode-llm-context-compression.md` — MCP server design pattern: compact summary + queryable store + drill-down tools (Key Finding 4)
- [ ] `Research/backlog/2026-03-02-semantic-full-text-search.md` — search layer this interface depends on
- [ ] MCP tool creation docs: https://modelcontextprotocol.io/docs/concepts/tools — how to build MCP tools
- [ ] MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk — Python server implementation
- [ ] GitHub Copilot Extensions docs: https://docs.github.com/en/copilot/building-copilot-extensions — custom Copilot chat providers
- [ ] RAG patterns for grounded QA: survey of prompt engineering patterns for citation-enforced answers
- [ ] Anthropic Claude API docs (for CLI chatbot option): https://docs.anthropic.com/

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

- Type: knowledge, tool, backlog-item
- Description: Recommended approach (MCP server vs. Copilot extension vs. CLI chatbot); interface contract definition; ADR if MCP server adopted; implementation backlog slice
- Links:
  - `Research/backlog/2026-02-27-interface-and-delivery.md` (upstream item)
  - `Research/completed/2026-03-01-context-mode-llm-context-compression.md` (MCP design pattern)
  - `Research/backlog/2026-03-02-semantic-full-text-search.md` (search layer dependency)
  - `Research/backlog/2026-03-02-slack-msteams-research-integration.md` (complementary delivery channel)
  - `Research/backlog/2026-03-02-ios-shortcuts-research.md` (complementary mobile channel)
