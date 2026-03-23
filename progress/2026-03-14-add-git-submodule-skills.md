# 2026-03-14 — Convert .github/skills/ to a git submodule

## Objective

The problem statement requires `.github/skills/` to be a git submodule from
`davidamitchell/Skills`, matching the pattern used in
[`davidamitchell/Latest-developments-`](https://github.com/davidamitchell/Latest-developments-/tree/main/.github).

## What changed

### `.gitmodules` (created)

New file declaring the submodule:

```
[submodule ".github/skills"]
    path = .github/skills
    url = https://github.com/davidamitchell/Skills.git
```

### `.github/skills/` (converted from tracked directory to gitlink)

- All 15 SKILL.md files previously committed directly to this repo were removed
  from git tracking (`git rm --cached`).
- The directory was replaced by a gitlink (mode 160000) pointing to
  `davidamitchell/Skills@b5edbc1073a82b949414f175e8734b2cbadb8d8e` (latest
  `main` HEAD at time of conversion).

### `.github/workflows/sync-skills.yml` (updated)

- **Before:** clone-and-copy — cloned `davidamitchell/Skills` into `/tmp/upstream-skills`
  and copied SKILL.md files individually; locally-added skills (e.g. `bbc-author`)
  were preserved.
- **After:** submodule update — uses `git submodule update --remote .github/skills`
  to advance the pointer to the latest upstream commit. This matches the
  `sync-skills.yml` in `davidamitchell/Latest-developments-` exactly.

## Known gap: `bbc-author` skill

The `bbc-author` skill (`bbc-author/SKILL.md`, 272 lines) was added to
`.github/skills/` directly in a previous session. It does **not** exist in
`davidamitchell/Skills`. Converting to a submodule means this skill will only
be available to agents once it is added to the upstream Skills repo.

**Action required:** Open a PR to `davidamitchell/Skills` to add `bbc-author`.
A copy of the skill content is available in this repo's git history
(last commit that contained it). Use `create-skills-pr.yml` as a reference
for the PR creation pattern, or run the workflow manually.

Until the PR is merged and the submodule pointer is advanced, agents will fall
back to the `research-prompt.md` fallback path for BBC author tasks.

## Documentation status

- `copilot-instructions.md` — already documents `.github/skills/` as a read-only
  submodule with the correct constraint ("Never edit `.github/skills/` — it is a
  read-only submodule. All skill changes go to `davidamitchell/Skills`"). No change
  needed.
- `docs-adr/0002-agent-skills-submodule.md` — already documents the submodule
  decision as "accepted". No change needed.

## Tests

- `tests/test_research_review.py::test_workflow_initializes_skills_submodule` — passes
  (continues to verify `research-review.yml` calls `git submodule update --init .github/skills`).
- All 35 `test_research_review.py` tests pass.
