# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Fixed
- `Research/completed/2026-03-08-ios-shortcuts-github-api-memory-capture.md`: expanded PAT, MIME, LTE acronyms; fixed secondary rate limit citation URL; corrected "most common failure mode" to "a likely failure mode"; added `[inference]` labels to unattributed claims (issues #66)
- `Research/completed/2026-03-08-inbox-folder-capture-triage-pattern.md`: expanded PKM, HCI, ULID acronyms; corrected `[fact]`→`[inference]` on YAML front-matter claim; removed unverifiable AAAI ICWSM citation; added `Opinion:` and `[inference]` labels; rewrote AI-slop patterns in Findings Analysis (issue #65)
- `Research/completed/2026-03-08-claude-ios-mcp-remote-integration.md`: expanded MCP, SSE, RFC, ASGI, WSGI, PAT acronyms; added Cloudflare Workers pricing citation; added Connectors Directory URL; added `Opinion:` and `[inference]` labels to subjective claims (issue #64)
- `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`: expanded ITSM, GRC, IRM, CI, CMDB, TBM, ITOM, DORA, RBNZ acronyms; replaced unverifiable "web search synthesis" citations with specific URLs; labelled uncited partner sources as `[inference]`; added `[fact]`/`[inference]` labels to §5 analytical claims; rewrote repetitive Findings Analysis paragraph openings; compressed near-verbatim repeated insight (issue #63)

### Added
- Research backlog items for mobile memory capture and retrieval (8 items covering iOS Shortcuts, Telegram, Slack, Claude iOS MCP, self-hosted MCP, LanceDB index rebuild, ChatGPT Actions, inbox pattern)
- `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`: completed research on emergent AI prompt patterns for SDLC phases; key findings: 55.8% Build-phase speed gain (Peng et al. 2023), SCoT +13.79% Pass@1 over CoT (Li et al. 2023), DORA 2024 AI adoption correlation (+3.4% code quality, -7.2% delivery stability); phase taxonomy, evidence map, and tooling alignment framework including MCP prompts primitive
- `.github/copilot-instructions.md` (full content, replaces `AGENTS.md` stub)
- `CHANGELOG.md` (this file)
- `docs/adr/0006-standardise-agent-instructions.md`
- `## Continuous Improvement & Learning` unified self-improvement framework in `.github/copilot-instructions.md`
- `## Chain-of-Thought Reasoning` section in `.github/copilot-instructions.md`

### Changed
- `.github/copilot-instructions.md`: replaced `## Mini-Retro — After Each Piece of Work` and `## When to Update These Instructions` with the unified Continuous Improvement & Learning framework

### Removed
- `AGENTS.md` (content moved to `.github/copilot-instructions.md`)
- `.claude/` directory and `.claude/skills` submodule

### Changed
- `.gitmodules`: removed `.claude/skills` entry
- `.github/workflows/sync-skills.yml`: removed `.claude/skills` sync step
- `README.md`: updated to reflect current structure
- `BACKLOG.md`: added W-0033 for standardisation work
- `docs/adr/README.md`: added ADR-0006, added "When to write an ADR" section
