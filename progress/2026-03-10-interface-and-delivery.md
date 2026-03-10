# 2026-03-10 — Research Loop (interface-and-delivery)

**Completed:**

Research item:
- `Research/completed/2026-02-27-interface-and-delivery.md` — completed; the GitHub wiki (already live via `publish-wiki.yml`) is the human browsing interface, and an MCP server with stdio transport is the agent query interface (designed in prior research, not yet implemented). Email digest and Slack push notification are architecturally viable but blocked pending credential approval (`RESEND_API_KEY`/`EMAIL_RECIPIENT` for email; `SLACK_WEBHOOK_URL` for Slack).

Sources consulted:
- https://modelcontextprotocol.io/docs/concepts/tools (MCP tool protocol specification — tool naming, input schema, result format)
- https://github.com/davidamitchell/Latest-developments- (email digest pattern — credentials required: Resend/Gmail + recipient)
- Research/completed/2026-03-02-chat-conversational-interface.md (MCP server three-tool contract and stdio transport decision)
