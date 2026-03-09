# 2026-03-09 — Research Loop (ai-coding-harnesses-agent-philosophy)

**Completed:**

Research item:
- `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` — completed; All major AI coding harnesses (Anthropic Claude Code, OpenAI Codex, GitHub Copilot, Cursor, AMP, Aider, Cline, Opencode, Continue.dev, Zed) have converged on tool-mediated execution, AGENTS.md for project-context injection, and git as the state store; they diverge on execution environment (local vs. cloud sandbox) and context window management strategy. Anthropic's published long-running harness architecture (initializer agent + feature-list JSON + per-session progress file) is the field's most detailed public treatment of multi-context-window task execution.

Sources consulted:
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (Anthropic harness architecture for long-running agents)
- https://www.anthropic.com/engineering/building-effective-agents (Anthropic five composable workflow patterns — December 2024)
- https://agents.md (AGENTS.md cross-vendor standard for project-context injection)
- https://openai.com/index/introducing-codex (OpenAI Codex cloud sandbox agent design)
- https://cursor.com/docs/agent/overview (Cursor agent mode — dynamic context discovery)
- https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot (GitHub Copilot dual-layer architecture)
- https://ampcode.com/manual (AMP/Sourcegraph sub-agent Owner's Manual)
- https://aider.chat/docs (Aider design philosophy and CONVENTIONS.md)
- https://deepwiki.com/cline/cline/1.1-architecture-overview (Cline five-layer VSCode architecture)
- https://deepwiki.com/sst/opencode (Opencode client/server architecture)
- https://tessl.io/blog/zed-debuts-agent-client-protocol (Zed Agent Client Protocol announcement)
