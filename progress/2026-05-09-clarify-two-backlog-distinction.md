# 2026-05-09 -- Clarify two-backlog distinction in copilot-instructions.md

**Completed:**
- Fixed ambiguous constraint in `.github/copilot-instructions.md`:
  - Before: `"New backlog items must be created in Research/backlog/"` (no qualification → caused previous session to place W-items there)
  - After: `"New *research* backlog items must be created in Research/backlog/…"` with an explicit note that repo improvement tasks belong in `BACKLOG.md`
- Added a `### Which backlog?` decision table before the "Adding a New Research Item" section, with a clear routing rule and an explanation of why placing repo improvements in `Research/backlog/` breaks the research loop

**Files changed:**
- `.github/copilot-instructions.md` — two targeted edits; no behaviour change, documentation only

## Mini-Retro

1. **Did the process work?** Yes — the README was already clear, the instructions had one ambiguous constraint and one missing decision gate.
2. **What slowed down or went wrong?** Nothing in this session. The root cause was already identified by the previous session's retro.
3. **What single change would prevent this next time?** Done: the constraint now says "research backlog items" and the decision table makes the fork explicit before any agent reaches the "Adding a New Research Item" section.
4. **Is this a pattern?** Yes — already recorded in the Known Recurring Patterns table as "making todos in the wrong backlog". The constraint fix and decision table directly address it at the instruction level.
5. **Does documentation need updating?** The README is clear; `.github/copilot-instructions.md` was the gap, now fixed.
6. **Do default instructions need updating?** These edits ARE the instruction update. No further change needed.
