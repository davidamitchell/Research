# Session: Workflow Regression Issue — Skills Sync and Research Loop

**Date:** 2026-03-14  
**Slug:** workflow-regression-issue

---

## What was done

Investigated recent workflow failures in the research loop and skills sync pipeline. Traced the regressions to specific commits, gathered log evidence from failing Actions runs, and opened a comprehensive tracking issue.

**Issue opened:** [#135 — Investigate workflow regressions: skills sync/submodule inconsistency and research loop dirty-working-tree crash](https://github.com/davidamitchell/Research/issues/135)

---

## Root cause findings

### 1. Skills sync/submodule inconsistency

Commit **`b65f00f`** (2026-03-08, "feat: add Better Business Cases (BBC) Five Case Model research item and bbc-author skill") made two changes together that broke internal consistency:

- **`sync-skills.yml`** — rewrote from proper `git submodule update --remote` pointer update to a clone-and-copy approach (`git clone davidamitchell/Skills` → `cp SKILL.md`)
- **`.gitmodules`** — removed the `.github/skills` submodule entry entirely

But the following were **not updated** in the same commit (and still haven't been):
- `research-review.yml` still runs `git submodule update --init .github/skills` (no-op because there's no submodule registered)
- `docs/adr/0002-agent-skills-submodule.md` still documents the submodule approach as `Status: accepted`
- `.github/copilot-instructions.md` still calls `.github/skills/` a "read-only submodule"

### 2. Research loop dirty-working-tree crash

Research Loop runs **#21** (2026-03-11) and **#25** (2026-03-13) both failed with the same pattern:
1. Copilot CLI session hit transient API errors (503 / HTTP/2 GOAWAY), exiting without committing files
2. Next iteration attempted `git pull --rebase origin main`
3. Rebased failed: `error: cannot pull with rebase: You have unstaged changes.`
4. Loop aborted

The loop has no guard to stash or clean the working tree before pulling. Last known good run was **#20** (2026-03-10).

---

## Investigation path for the fix (user chose Option B: Fix + write ADR)

The user chose to:
- Restore `.github/skills` to a proper git submodule
- Write a new ADR explaining the revert from copy-based sync back to submodule pointer updates

This work is captured in issue #135 with a detailed acceptance criteria checklist.

---

## Files changed

- `progress/2026-03-14-workflow-regression-issue.md` — this file

---

## Mini-retro

The regression was introduced by an agent making a logically consistent local change (add bbc-author skill via copy-based approach) without considering the wider contract: three other files (`research-review.yml`, ADR-0002, `copilot-instructions.md`) all assumed submodule semantics. This is a pattern of "partial update" — changing the mechanism without updating all the documents that describe the mechanism.

**Root-cause fix needed:** any future change to how skills are synced must update the four contract documents atomically: `sync-skills.yml`, `.gitmodules`, `research-review.yml`, and `copilot-instructions.md`. The ADR should also be updated/superseded.
