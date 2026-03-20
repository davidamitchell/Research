# 2026-03-20 — Research Loop (api-context-hubs-rag-mcp)

**Completed:**

Research item:
- `Research/completed/2026-03-18-api-context-hubs-rag-mcp.md` — completed; the item concludes that context hubs, Retrieval-Augmented Generation (RAG)-based API discovery, and the Model Context Protocol (MCP) are complementary layers rather than direct substitutes. `context-hub` handles curated prompt-time grounding, RAG systems handle large-catalogue selection and freshness, and MCP standardises connected-server invocation, with the OpenAPI Specification (OAS) acting as the common structural substrate across the stack.

Sources consulted:
- https://raw.githubusercontent.com/andrewyng/context-hub/main/README.md (`context-hub` problem statement and agent-facing design)
- https://modelcontextprotocol.io/specification/latest/server/tools (MCP tool discovery and invocation model)
- https://arxiv.org/abs/2307.16789 (ToolLLM / ToolBench paper on large-scale API retrieval and tool use)

## Mini-Retro

1. **Did the process work?** Yes. The draft-review-complete loop worked end to end, including automated review passes and frontmatter state transitions.
2. **What slowed down or went wrong?** The review workflow was stricter than the written prompt in two places: it required URL-grade citations inside retained Research Skill Output text and explicit claim labels plus inline sources inside `## Findings`.
3. **What single change would prevent this next time?** Add an explicit repository rule that retained `## Findings` prose must use `[fact]` / `[inference]` labels with inline source URLs, not just the Research Skill Output section.
4. **Is this a pattern?** Yes. It matches the existing pattern in the instructions that citation discipline and acronym expansion cause repeated review failures; this item showed that findings-section citation discipline should be treated as part of the same recurring pattern.
