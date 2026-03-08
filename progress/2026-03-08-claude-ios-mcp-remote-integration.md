# 2026-03-08 — Research Loop (claude-ios-mcp-remote-integration)

**Completed:**

Research item:
- `Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md` — completed; confirmed Claude iOS supports remote MCP via the Connectors system using Streamable HTTP over HTTPS (not stdio); configuration is through the claude.ai web UI (not `.mcp.json`), syncing to iOS at login; custom connectors require a Claude Pro plan minimum, and auth is either no-auth or OAuth 2.1 (static bearer tokens are API-only).

Sources consulted:
- https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities (Connectors cross-device sync and iOS availability)
- https://modelcontextprotocol.io/docs/concepts/transports (MCP Streamable HTTP transport specification)
- https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq (Plan requirements, auth options, platform support)
- https://docs.anthropic.com/en/agents-and-tools/mcp-connector (MCP connector API, HTTPS requirement, static bearer token)
- https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization (OAuth 2.1 auth specification)
- https://support.anthropic.com/en/articles/11175166-what-is-claude-ai-s-connection-feature (Custom connector setup flow)
- https://developers.cloudflare.com/agents/guides/remote-mcp-server/ (Minimum deployment example with Cloudflare Workers)
- https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2043 (MCP RFC #2043 Memory Interchange Format — community proposal, no Anthropic commitment)
