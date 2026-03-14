# ADR-0008: Agent Skills via Clone-and-Copy Sync

Date: 2026-03-14
Status: accepted
Supersedes: [ADR-0002](0002-agent-skills-submodule.md)

## Context

ADR-0002 adopted git submodules to embed `davidamitchell/Skills` at `.github/skills/`.
In practice the submodule approach created recurring operational friction:

- Cloning the repo without `--recurse-submodules` left `.github/skills/` empty, causing
  agent sessions to silently fail to find skill files.
- The `.gitmodules` entry for `.github/skills` was removed in commit `b65f00f`
  (2026-03-08) when a local skill (`bbc-author`) was added directly to `.github/skills/`,
  converting the path from a gitlink to a regular tracked directory. After that commit,
  `research-review.yml` still called `git submodule update --init .github/skills` (now a
  no-op), and `copilot-instructions.md` still described `.github/skills/` as a "read-only
  submodule" — an inconsistency that persisted until ADR-0008 resolved it.
- The copy-based `sync-skills.yml` already in use (`git clone davidamitchell/Skills` then
  `cp SKILL.md`) is simpler to understand, requires no submodule initialisation at checkout,
  and allows locally-added skills to coexist with upstream-synced ones.

## Decision

Formalise `.github/skills/` as a **regular tracked directory** populated by a
clone-and-copy workflow, superseding the git submodule approach.

- `sync-skills.yml` clones `davidamitchell/Skills` to `/tmp/upstream-skills` and copies
  each `SKILL.md` into `.github/skills/<skill-name>/SKILL.md`. It runs on a weekly
  schedule (Mondays 06:00 UTC) and supports `workflow_dispatch` for manual syncs.
- Locally-added skills (e.g. `bbc-author`) that do not exist in the upstream repo are
  preserved because the sync only overwrites files that exist upstream.
- `.gitmodules` contains no entry for `.github/skills`.
- Workflow checkouts do **not** need `submodules: true` — skill files are present as
  ordinary tracked files in the repository tree.

## Consequences

### Positive
- No submodule initialisation step required. Any `actions/checkout` brings skill files
  along with the rest of the repo, including in the research loop and review workflows.
- Local skills can be added directly to `.github/skills/` without needing a PR to
  `davidamitchell/Skills` first. They survive future syncs as long as they have no
  matching name in the upstream repo.
- Simpler mental model: `.github/skills/` is just a directory of Markdown files.

### Negative / Trade-offs
- Skill files are duplicated in this repo rather than referenced by pointer. A divergence
  between the file content and the upstream commit is possible if a sync is delayed.
- There is no pinned upstream SHA — each sync pulls whatever is at the upstream HEAD.
  If the upstream repo introduces a breaking change, the next Monday sync will propagate
  it immediately.

### Neutral
- Adding or updating a skill still requires a PR to `davidamitchell/Skills`; the change
  propagates to this repo on the next sync (or via `workflow_dispatch`).
- Direct edits to `.github/skills/` files in this repo will be overwritten on the next
  sync if a file with the same name exists upstream. This matches the previous "read-only
  submodule" intent — the correct place to make lasting skill changes remains
  `davidamitchell/Skills`.
