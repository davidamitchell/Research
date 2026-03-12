# Session: superpowers-research

**Date**: 2026-03-12
**Branch**: copilot/research-superpowers-integration

## What was done

Conducted and completed research on whether and how `davidamitchell/superpowers` can be integrated into the owner's repos.

**Research item created**: `Research/completed/2026-03-12-superpowers-integration-analysis.md`

## Key findings

1. `davidamitchell/superpowers` is an uncustomised fork of `obra/superpowers` — a plugin for Claude Code, Cursor, Codex, and OpenCode.
2. The plugin system is **incompatible with GitHub Copilot Agent** (the owner's primary agent). Direct installation is not possible.
3. All three active target repos (`Latest-developments-`, `Agent-Evaluation`, `Research`) already use `davidamitchell/Skills` submodule.
4. `Memory-System` does not exist on GitHub (404).
5. **Recommended path**: Port three superpowers skills (`test-driven-development`, `systematic-debugging`, `subagent-driven-development`) into `davidamitchell/Skills` via PRs to that repo. Benefits all three active repos with zero per-repo changes.
6. If Claude Code is ever used directly: `/plugin install superpowers@claude-plugins-official` is a zero-config install.

## Files changed

- `Research/completed/2026-03-12-superpowers-integration-analysis.md` — new, completed research item
- `progress/2026-03-12-superpowers-research.md` — this session log

## Mini-Retro

1. **Did the process work?** Yes. All target repos were inspected directly via GitHub MCP tools; the superpowers fork's commit history confirmed zero owner customisations in one API call.
2. **What slowed down or went wrong?** `Memory-System` was listed in the problem statement but does not exist on GitHub — could not be assessed. No meaningful slowdown otherwise.
3. **What single change would prevent this next time?** Nothing to change; the research was completable from first principles with available tools. If Memory-System is created later, a follow-up research item can assess it.
4. **Is this a pattern?** No — one-off finding specific to this investigation.
