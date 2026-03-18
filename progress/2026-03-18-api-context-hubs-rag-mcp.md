# Session: New Research Item — API Context Hubs, RAG, and MCP

**Date:** 2026-03-18
**Slug:** api-context-hubs-rag-mcp
**Issue:** API context hubs and RAG (Retrieval-Augmented Generation) and MCP (Model Context Protocol)

## What was done

Created a new backlog research item from the GitHub issue requesting research into how AI agents discover and use APIs, using `andrewyng/context-hub` as a seed.

**File created:** `Research/backlog/2026-03-18-api-context-hubs-rag-mcp.md`

## Decisions made

- **Priority: high** — the question of how agents discover and use tools/APIs is foundational to agent capability. MCP is actively evolving (2024–2026) and the field is still unsettled.
- **Tags:** `api-discovery`, `context-hub`, `rag`, `mcp`, `model-context-protocol`, `retrieval-augmented-generation`, `agents`, `tooling`, `ai-agents`, `api-integration`
- **Scope framing:** The three approaches (context hubs, Retrieval-Augmented Generation (RAG)-based discovery, Model Context Protocol (MCP)) are treated as the primary design archetypes. The research question explicitly asks whether the problem solved by `context-hub` is addressed differently elsewhere — this is the central comparative question.
- **Sources seeded:** Gorilla, ToolBench/ToolLLM, REST-GPT, HuggingGPT, API-Bank, the MCP specification, and OpenAPI Specification as the structured API description standard.

## Conventions followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`
- Research Skill Output and Findings sections left blank for the research agent to fill
- Acronyms expanded on first use throughout: Application Programming Interface (API), Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), Language Model (LLM), Remote Procedure Call (RPC), Large Language Model (LLM)
