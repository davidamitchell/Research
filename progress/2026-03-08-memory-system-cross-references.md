# Session: Add Memory-System backlog cross-references

**Date:** 2026-03-08  
**Branch:** copilot/update-research-backlog-cross-reference-again

## What was done

Added `## Related` sections and `## Sources` entries to 8 research backlog items, cross-referencing their corresponding Memory-System discovery backlog items (W-0003 through W-0015).

**Note:** `davidamitchell/Memory-System` was not publicly accessible at the time of this session (404 on all access methods). W-XXXX numbers and titles are based on the mapping provided in the task specification. These should be verified when the Memory-System repo becomes accessible.

## Files changed

| Research item | Memory-System item |
|---|---|
| `2026-03-08-ios-shortcuts-github-api-memory-capture.md` | W-0008 — iOS Shortcuts + GitHub API: zero-infrastructure mobile capture |
| `2026-03-08-telegram-bot-memory-capture-retrieval.md` | W-0011 — Telegram bot as mobile memory capture and retrieval channel |
| `2026-03-08-slack-bot-memory-capture-retrieval.md` | W-0003 — Slack as a mobile memory capture and retrieval channel |
| `2026-03-08-claude-ios-mcp-remote-integration.md` | W-0004 — Claude for iOS: MCP remote integration for memory capture and retrieval |
| `2026-03-08-self-hosted-mcp-server-options.md` | W-0014 — Self-hosted MCP server options: enabling mobile AI app integration |
| `2026-03-08-lancedb-index-rebuild-from-git.md` | W-0015 — LanceDB index rebuild speed from git: enabling stateless deployment |
| `2026-03-08-chatgpt-actions-memory-integration.md` | W-0005 — ChatGPT Actions and custom GPTs: external memory integration options |
| `2026-03-08-inbox-folder-capture-triage-pattern.md` | W-0012 — Inbox folder pattern: frictionless capture without forced structure |

## Pattern applied

Each file received:
1. A new `## Related` section inserted between `## Context` and `## Approach`:
   ```
   ## Related

   **Memory-System backlog:** [W-XXXX — Title](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — one sentence describing the relationship.
   ```
2. A new entry at the end of `## Sources`:
   ```
   - [ ] `davidamitchell/Memory-System` BACKLOG.md W-XXXX — the corresponding discovery item that this research informs
   ```
