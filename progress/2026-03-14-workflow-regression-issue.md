# Session: Workflow Regression Fix — Skills Sync and Research Loop

**Date:** 2026-03-14  
**Slug:** workflow-regression-issue

---

## What was done

Investigated recent workflow failures in the research loop and skills sync pipeline. Traced the regressions to specific commits, gathered log evidence from failing Actions runs, opened tracking issue #135, then applied the full fix.

**Issue opened:** [#135 — Investigate workflow regressions: skills sync/submodule inconsistency and research loop dirty-working-tree crash](https://github.com/davidamitchell/Research/issues/135)

---

## Root cause findings

### 1. Skills sync/submodule inconsistency

Commit **`b65f00f`** (2026-03-08, "feat: add Better Business Cases (BBC) Five Case Model research item and bbc-author skill") made two changes together that broke internal consistency:

- **`sync-skills.yml`** — rewrote from proper `git submodule update --remote` pointer update to a clone-and-copy approach (`git clone davidamitchell/Skills` → `cp SKILL.md`)
- **`.gitmodules`** — removed the `.github/skills` submodule entry entirely

The following were **not updated** in the same commit:
- `research-review.yml` still ran `git submodule update --init .github/skills` (broken — no submodule registered)
- `docs/adr/0002-agent-skills-submodule.md` still documented the submodule approach as `Status: accepted`
- `.github/copilot-instructions.md` still called `.github/skills/` a "read-only submodule"

### 2. Research loop dirty-working-tree crash

Research Loop runs **#21** (2026-03-11) and **#25** (2026-03-13) both failed with the same pattern:
1. Copilot CLI session hit transient API errors (503 / HTTP/2 GOAWAY), exiting without committing files
2. Next iteration attempted `git pull --rebase origin main`
3. Rebase failed: `error: cannot pull with rebase: You have unstaged changes.`
4. Loop aborted

### 3. TAVILY_API_KEY not exposed to Copilot CLI process

`TAVILY_API_KEY` was listed as available in the credentials table but was never passed as an
environment variable to the Copilot CLI steps in `research-loop.yml` or `research-review.yml`.
The `tavily-mcp` MCP server reads the key from `${TAVILY_API_KEY}` in the process environment,
so Copilot sessions had no Tavily web search capability regardless of whether the secret was set.

---

## Fixes applied (formalise copy-based approach, option B)

### `research-loop.yml`
- Removed stale `submodules: false` from checkout step (skills are regular tracked files)
- Added `TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}` to the Copilot step env
- Added dirty-working-tree commit guard before `git pull --rebase`:
  if the previous session left uncommitted files, they are committed as residuals
  (never discarded with `reset --hard` — uncommitted files are completed research)

### `research-review.yml`
- Removed the "Initialize skills submodule" step (`git submodule update --init .github/skills`)
- Added `TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}` to the Copilot step env

### `copilot-instructions.md`
- Updated Quick Reference rule #3: removed "read-only submodule" language
- Updated Non-Negotiable Constraints item to reflect copy-based sync approach

### `docs/adr/0002-agent-skills-submodule.md`
- Changed status from `accepted` to `superseded by ADR-0008`

### `docs/adr/0008-skills-copy-based-sync.md` (new)
- Documents the current clone-and-copy sync approach as the accepted ADR
- Explains why the submodule approach was abandoned
- Preserves the decision rationale for future reference

### `docs/adr/README.md`
- Added ADR-0008 to index; updated ADR-0002 status to "Superseded by ADR-0008"

---

## Files changed

- `.github/workflows/research-loop.yml` — dirty-tree guard + TAVILY_API_KEY env
- `.github/workflows/research-review.yml` — remove submodule step + TAVILY_API_KEY env
- `.github/copilot-instructions.md` — fix submodule language
- `docs/adr/0002-agent-skills-submodule.md` — superseded status
- `docs/adr/0008-skills-copy-based-sync.md` — new ADR
- `docs/adr/README.md` — updated index
- `progress/2026-03-14-workflow-regression-issue.md` — this file

---

## Mini-retro

The regression was introduced by an agent making a logically consistent local change (add bbc-author skill via copy-based approach) without considering the wider contract: three other files (`research-review.yml`, ADR-0002, `copilot-instructions.md`) all assumed submodule semantics. This is a "partial update" pattern.

Additionally, TAVILY_API_KEY was in the credentials table but never wired into the workflow env — a gap between "documented as available" and "actually reachable by the Copilot process".

**Systemic fix:** any future change to how skills are synced, or how a new credential is added, must update all four contract documents atomically: the workflow, `.gitmodules`, `copilot-instructions.md`, and the ADR.
