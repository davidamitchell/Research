# 2026-03-11 — Reviewing state and dispatch trigger

**Completed:**

Implementation of the `reviewing` lifecycle state and migration of the research review workflow
from a `push` trigger to `workflow_dispatch`-only.

## What was built

- `src/research/item.py`: added `reviewing` → `in-progress` mapping in `state_dir_name()`
- `src/research/cli.py`: added `cmd_draft` (status update only, no file move), added
  `_get_frontmatter_field` helper, added soft guard to `cmd_complete` (warns if status ≠ reviewing),
  registered `draft` sub-command in `register_subparser` and `dispatch`
- `.github/workflows/research-review.yml`: removed `push` trigger on `Research/completed/**`;
  workflow is now `workflow_dispatch`-only; `item_path` description updated to accept
  `Research/in-progress/` paths; simplified "Determine items to review" step
- `research-prompt.md`: replaced single step 8 with three steps (draft → review → complete);
  renumbered session log and commit steps to 11 and 12
- `docs-adr/0007-reviewing-state-and-dispatch-trigger.md`: ADR documenting decisions
- `docs-adr/README.md`: added ADR-0007 to index
- `Research/in-progress/README.md`: documents `reviewing` status and in-place file behaviour
- `Research/README.md`: updated to four-state lifecycle with `research draft` in workflow
- `CHANGELOG.md`: added entry under [Unreleased]

## Tests added / updated

- `tests/test_research_item.py`: added `test_state_dir_name_reviewing_maps_to_in_progress`
- `tests/test_research_cli.py`: added `_get_frontmatter_field` tests, `cmd_draft` tests
  (status update, no file move, file remains in in-progress, exits on missing), `cmd_complete`
  warning tests (warns if not reviewing, still completes despite warning)
- `tests/test_research_review.py`: updated push trigger tests to assert push is absent;
  added `test_workflow_accepts_in_progress_item_paths`
- `tests/test_research_loop.py`: added "research draft" to required sections list

## Decisions made

- `reviewing` maps to `in-progress/` (no backward file moves, clean git history) — see ADR-0007
- `workflow_dispatch` replaces push trigger (explicit over implicit) — see ADR-0007
- Soft guard on `cmd_complete` (warn only, do not block) — see ADR-0007

## Mini-retro

**What worked:** The change was well-scoped. All existing tests passed after updates, the new
command follows the same pattern as `cmd_start` / `cmd_complete`, and the soft guard is the right
call for a human-in-the-loop workflow.

**Architectural observation:** The test for the push trigger being absent is now the inverse of
what it was. This is a clean state inversion, but it's worth noting that removing a trigger is
a breaking change for any automation that relied on the push trigger. In this case that's
intentional — the research loop now needs to call `gh workflow run` explicitly.

**Coupling note:** `research-prompt.md` directly names the CLI commands and step numbers. Each
time a new step is added, step numbers in the prompt must be updated manually. This is the same
DIP coupling identified earlier — a future improvement would be to reference a canonical step
list from a single location. Not addressed in this session (out of scope).
