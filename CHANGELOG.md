# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Research backlog items for mobile memory capture and retrieval (8 items covering iOS Shortcuts, Telegram, Slack, Claude iOS MCP, self-hosted MCP, LanceDB index rebuild, ChatGPT Actions, inbox pattern)
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
