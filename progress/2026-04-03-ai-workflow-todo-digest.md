# Session log: 2026-04-03 -- ai-workflow-todo-digest

**Date:** 2026-04-03
**Issue:** Ai workflow help with todo lists
**Branch:** copilot/ai-workflow-help-todo-lists

## What was done

Created a new research backlog item from the GitHub issue requesting research on AI-assisted productivity digest workflows.

**New backlog item:** `Research/backlog/2026-04-03-ai-workflow-todo-digest.md`

The item covers:
- The core pattern described in the YouTube video (https://youtu.be/hFRQb2e5cJs): Zapier + Notion + Claude/ChatGPT + Slack for daily and weekly digests
- Tooling comparison: Zapier, Make, n8n, custom scripts
- Messaging platform options for iOS: Slack, Microsoft Teams, Telegram, Apple Shortcuts/iMessage
- Memory system alternatives and complements: MemGPT, Mem.ai, Rewind.ai, OpenAI Memory
- Public research on proactive push vs pull-on-demand information delivery for knowledge workers
- Related davidamitchell GitHub repositories on memory and personal assistants
- 20 seeded sources, all with URLs

## Decisions

- Priority set to `medium`: interesting and practically useful but not blocking anything
- Output typed as `[knowledge, backlog-item]`: the research may surface a new sub-item for a specific integration to build
- Tags cover: ai, productivity, automation, zapier, notion, slack, task-management, personal-assistant, memory-systems, messaging, ios, workflow
- Scope deliberately excludes enterprise workflow automation and deep LLM quality evaluation to keep the item focused

## Checks

- `make check` -- passed (no Python source files changed)
- `make test` -- passed (no Python source files changed)
- No `docs/` changes committed

## Learnings

- The YouTube video describes a pattern based on human response behaviour ("we respond to what shows up in front of us") rather than retrieval behaviour -- this framing is worth preserving in the research context section
- The memory system angle (MemGPT, Rewind, etc.) is a genuine open question: it is not clear whether continuous memory makes scheduled digests redundant or complementary
- iOS delivery is a meaningful constraint for this owner; Telegram has the best bot API for lightweight delivery, but Slack is already in use
