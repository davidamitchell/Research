# ADR-0006: Standardise Agent Instruction Files

Date: 2026-03-07
Status: Accepted

## Context

Agent instructions lived in `AGENTS.md` at the repo root and a stub `.github/copilot-instructions.md` that pointed to it. The organisation standard is `.github/copilot-instructions.md` as the sole source of truth for all agents. A `.claude/` directory existed for Claude-specific configuration, with a separate `skills` submodule entry in `.gitmodules`.

## Decision

Expand `.github/copilot-instructions.md` with the full content from `AGENTS.md`, removing the indirection. Delete `AGENTS.md` and `.claude/`. Update `.gitmodules` to remove the `.claude/skills` submodule entry. Update `sync-skills.yml` to sync only `.github/skills`. Add `BACKLOG.md`, `PROGRESS.md`, `CHANGELOG.md`, and `docs-adr/` mandates to the instructions.

## Consequences

### Positive
- Consistent with all other repos in the davidamitchell organisation
- All agents use the same well-known path (`.github/copilot-instructions.md`)
- No indirection or sync scripts needed between instruction files
- Simpler submodule configuration (single submodule instead of two)

### Negative / Trade-offs
- Claude Code no longer has a `.claude/` directory; it must use `.github/copilot-instructions.md` directly

### Neutral
- No change to skill content or the Skills submodule itself
