# Session: Update Default Instructions for New Skills

**Date:** 2026-03-27  
**Branch:** `copilot/update-default-instructions-for-skills`  
**Issue:** New skill and update — mandate tdd, swe, and code-review skills in the development loop

---

## What Was Done

1. **Advanced `.github/skills` submodule pointer** from `de3d2cf` to `111ec45` (latest HEAD of `davidamitchell/Skills`), which includes the new `tdd`, `swe`, and `code-review` skills.

2. **Updated `.github/copilot-instructions.md`** with targeted changes (two rounds):
   - Added Quick Reference item #10 mandating the `swe → tdd → code-review` development loop for all non-trivial work
   - Added `tdd`, `swe`, and `code-review` rows to the Agent Skills table, marked **mandatory**
   - Added a new **Development Loop** section under Working Methodology explaining when and how each skill is applied in sequence, including a Step 4 for documentation and ADR review
   - Added three development-loop checklist items to the Slice Completion Checklist
   - Extended the Mini-Retro to six questions, adding: documentation/ADR check and default instructions check

3. **Verified** `make check` (ruff) passes clean and 190/191 tests pass (1 pre-existing failure: `TAVILY_API_KEY` not set in sandbox — unrelated to these changes).

---

## Mini-Retro

1. **Did the process work?** Yes. Straightforward: update submodule, read all three new skills, update instructions in three places for coherence.

2. **What slowed down or went wrong?** Nothing significant. `ruff` and `pytest` had to be installed manually in the sandbox, but that is a sandbox bootstrap issue, not a process issue.

3. **What single change would prevent this next time?** Nothing to add — the sync-skills workflow already handles submodule advancement automatically on a weekly schedule. This was a manual advance ahead of the scheduled sync.

4. **Is this a pattern?** No new pattern identified. The "advance submodule then update instructions" flow is well-documented and worked smoothly.

5. **Does any documentation need updating?** No — this PR *is* the documentation update. No user-facing README changes required. No ADR needed: this is a process addition, not a significant architectural decision.

6. **Do the default instructions need updating?** Yes — the retro and development loop steps lacked documentation and ADR review prompts. Added in this session (PR review round 2).
