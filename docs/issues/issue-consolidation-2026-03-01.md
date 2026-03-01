# Issue Consolidation Analysis — 2026-03-01

*Produced following a review of all open GitHub issues in this repo. Captures deduplication decisions and grouping recommendations for implementation.*

---

## Summary of open issues

| # | Title | Target files |
|---|---|---|
| #8 | Research skill: 7 improvement gaps | `davidamitchell/Skills` → research/SKILL.md |
| #9 | Strategy-author skill: 7 improvement gaps | `davidamitchell/Skills` → strategy-author/SKILL.md |
| #10 | MCP servers unavailable in agent runner (runtime) | AGENTS.md (documentation option) |
| #11 | MCP config bugs: filesystem path, secret labels, no session check | `.mcp.json`, `.github/mcp.json`, `AGENTS.md` |
| #12 | Agent skills: submodule init undocumented, invocation model missing | `README.md`, `AGENTS.md` |
| #13 | AGENTS.md: Mini-Retro loop, empty-backlog protocol, update trigger, directory layout | `AGENTS.md` |

---

## Deduplication decision

### Close #10 — incorporated into #11

**Reason:** #10 observes that five MCP servers are unavailable in the agent runner and proposes three remediation options. #11 provides the specific config fixes that implement those options:

| #10 option | #11 fix |
|---|---|
| Option A: install pip packages in runner | Not covered — infrastructure concern, out of scope |
| Option B: add `BRAVE_API_KEY` as repo secret | Covered: #11 fixes the secret label from "Codespaces secret" to "repository secret" |
| Option C: document Codespaces-only servers in AGENTS.md | Covered: #11 adds a session-start MCP availability check and corrects AGENTS.md |

#11 already references #10: *"See also issue #10 for the broader runtime availability picture."* The runtime context from #10 is thus preserved.

**Action:** Close #10 with comment: *"Incorporated into #11, which covers all actionable config and documentation fixes. The remaining infrastructure item (pip package installation in runner) is noted in #11."*

---

## Grouping: work together in one PR

### Group A: AGENTS.md + config improvements — #11, #12, #13

All three issues require changes to `AGENTS.md`. Done separately they will produce three PRs modifying the same file, risking conflicts and inconsistency.

| Issue | AGENTS.md sections touched | Other files |
|---|---|---|
| #11 | MCP server table (fix secret labels), new session-start section | `.mcp.json`, `.github/mcp.json` |
| #12 | Skills table (invocation notes), new skills invocation section | `README.md` |
| #13 | Mini-Retro section, new empty-backlog section, new AGENTS.md update trigger section, Repository Layout | none |

**Recommended:** implement as one PR. Suggested commit order: #13 (structural additions) → #12 (skills section) → #11 (MCP section + config files). This avoids merge conflicts and produces a coherent, self-consistent AGENTS.md.

### Group B: Skills repo improvements — #8, #9

Both issues target the `davidamitchell/Skills` repository, not this repo. Both require changes to individual `SKILL.md` files within that repo.

| Issue | Target file in Skills repo |
|---|---|
| #8 | `research/SKILL.md` |
| #9 | `strategy-author/SKILL.md` |

No content overlap — they modify different files. Implementing as one PR to the Skills repo is clean and avoids two separate sync-skills workflow runs.

**Recommended:** implement as one PR to `davidamitchell/Skills`. Once merged, the weekly `sync-skills.yml` workflow will advance both submodule pointers, or a manual trigger can be run immediately.

---

## Implementation order recommendation

1. **Close #10** (no code change; just issue management)
2. **Implement Group A (#11 + #12 + #13)** — one PR to this repo; highest impact on agent reliability
3. **Implement Group B (#8 + #9)** — one PR to `davidamitchell/Skills`; triggers submodule sync

---

*Cross-references: #10 → #11, #11 → #12 → #13 (all AGENTS.md), #8 → #9 (both Skills repo)*
