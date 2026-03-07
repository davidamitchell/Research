# Changelog

All notable changes to this project will be documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- `.github/copilot-instructions.md` (full content, replaces `AGENTS.md` stub)
- `CHANGELOG.md` (this file)
- `docs/adr/0006-standardise-agent-instructions.md`

### Removed
- `AGENTS.md` (content moved to `.github/copilot-instructions.md`)
- `.claude/` directory and `.claude/skills` submodule

### Changed
- `.gitmodules`: removed `.claude/skills` entry
- `.github/workflows/sync-skills.yml`: removed `.claude/skills` sync step
- `README.md`: updated to reflect current structure
- `BACKLOG.md`: added W-0033 for standardisation work
- `docs/adr/README.md`: added ADR-0006, added "When to write an ADR" section
