# Session: superpowers-research

**Date**: 2026-03-12
**Branch**: copilot/research-superpowers-integration

## What was done

Conducted and completed research on what `davidamitchell/superpowers` can offer as inspiration for improving agent workflows across the owner's repos.

**Research item created**: `Research/completed/2026-03-12-superpowers-integration-analysis.md`

**Updated (PR comment)**: Reframed the research question from "can we integrate/use superpowers directly?" to "what can superpowers inspire?" — reflecting that the plugin delivery mechanism is incompatible with the owner's workflow, but the workflow disciplines and skill content are genuinely valuable ideas to borrow.

## Key findings

1. `davidamitchell/superpowers` is an uncustomised fork of `obra/superpowers` — it exists as a reference and tracking point.
2. Using it as a plugin is not the right path (incompatible with GitHub Copilot Agent). Using it as **inspiration** is.
3. All three active target repos (`Latest-developments-`, `Agent-Evaluation`, `Research`) already use `davidamitchell/Skills` submodule.
4. `Memory-System` does not exist on GitHub (404).
5. **Recommended path**: Adapt three superpowers concepts into `davidamitchell/Skills` via PRs: `test-driven-development`, `systematic-debugging`, `subagent-driven-development`. Benefits all three active repos with zero per-repo changes.
6. The superpowers philosophy itself — encode missing disciplines as non-negotiable skills — is worth borrowing.

## Files changed

- `Research/completed/2026-03-12-superpowers-integration-analysis.md` — new, completed research item (reframed per PR comment)
- `progress/2026-03-12-superpowers-research.md` — this session log

## Mini-Retro

1. **Did the process work?** Yes. All target repos were inspected directly via GitHub MCP tools; the superpowers fork's commit history confirmed zero owner customisations in one API call.
2. **What slowed down or went wrong?** `Memory-System` was listed in the problem statement but does not exist on GitHub — could not be assessed. Initial framing as "direct integration" required a correction pass after PR feedback to reframe as "inspiration."
3. **What single change would prevent this next time?** Read the problem statement more carefully for framing cues — "use for inspiration" vs "use directly" is a meaningful distinction that changes the entire research angle.
4. **Is this a pattern?** Yes — framing the research question correctly before writing is always cheaper than rewriting after.
