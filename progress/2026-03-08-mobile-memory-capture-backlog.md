# 2026-03-08 — Mobile capture and memory system integration backlog items

## Session goal

Add 8 research backlog items to `Research/backlog/` covering mobile capture and memory system integration options for the `davidamitchell/Memory-System` repo.

## Work done

Created 8 new research backlog items in `Research/backlog/`:

1. **`2026-03-08-ios-shortcuts-github-api-memory-capture.md`** (high priority) — iOS Shortcuts + GitHub Contents API as zero-infrastructure mobile capture path. No hosted component required.

2. **`2026-03-08-telegram-bot-memory-capture-retrieval.md`** (medium priority) — Telegram bot as combined capture + semantic retrieval surface. Requires minimal hosted component (free-tier PaaS).

3. **`2026-03-08-slack-bot-memory-capture-retrieval.md`** (medium priority) — Slack as a memory capture and retrieval channel. Distinct from existing `2026-03-02-slack-msteams-research-integration.md` (which covers research delivery, not memory capture).

4. **`2026-03-08-claude-ios-mcp-remote-integration.md`** (high priority) — Whether Claude iOS app supports remote MCP (HTTP/SSE transport) to connect to a self-hosted `mcp_server.py`. Best long-term path if supported.

5. **`2026-03-08-self-hosted-mcp-server-options.md`** (high priority) — Minimum viable self-hosted deployment of `mcp_server.py` or a write-only HTTP wrapper. Prerequisite for Claude iOS and ChatGPT Actions items.

6. **`2026-03-08-lancedb-index-rebuild-from-git.md`** (high priority) — Benchmark LanceDB index rebuild speed from `.md` files at various corpus sizes. Determines which stateless deployment models are viable.

7. **`2026-03-08-chatgpt-actions-memory-integration.md`** (low priority) — ChatGPT custom GPT Actions for memory capture and retrieval. Strategic interest for memory portability across AI tools.

8. **`2026-03-08-inbox-folder-capture-triage-pattern.md`** (high priority) — Inbox folder pattern: capture to `inbox/` with no required metadata, periodic agent triage classifies items. Reduces capture friction by eliminating folder-selection decision.

## Checks performed

- Verified no duplication with existing backlog or completed items:
  - `2026-03-02-ios-shortcuts-research.md` (completed) covers the *research system* Shortcut; new item covers *Memory-System* capture via GitHub Contents API.
  - `2026-03-02-slack-msteams-research-integration.md` (completed) covers *research delivery*; new item covers *memory capture and retrieval*.
- All 8 files follow `Research/_template.md` format exactly.
- All 8 files cross-reference `2026-03-02-agent-memory-management-context-injection.md` in Sources.
- `CHANGELOG.md` updated under `[Unreleased]`.
