# 2026-03-11 — Review: research skill status update assessment

**Task:** Assess whether `davidamitchell/Skills` needs updates following the addition of the `reviewing` status and `research draft` command to the Research repo lifecycle.

---

## Skills repo assessment

### `research/SKILL.md`

Read in full. The skill is purely **methodological** — it describes how to conduct research (recursive decomposition, evidence gathering, synthesis, consistency checks, depth expansion). It does **not** reference:

- Lifecycle states (`backlog`, `in-progress`, `reviewing`, `completed`)
- CLI commands (`research start`, `research draft`, `research complete`)
- Directory layout (`Research/backlog/`, `Research/in-progress/`, `Research/completed/`)
- Workflow triggers or commit message conventions

The lifecycle states and CLI commands are Research-repo-specific orchestration concerns. The `SKILL.md` is intentionally decoupled from the repo's workflow machinery — it governs *how* research is done, not *how the repo manages research items*.

**Verdict: no changes warranted to `research/SKILL.md`.**

### Other skills

Reviewed all 12 skills in the submodule:

| Skill | Governs agent process? | References research lifecycle? |
|---|---|---|
| `backlog-manager` | yes — backlog item management | no |
| `bbc-author` | no | no |
| `citation-discipline` | yes — citation standards | no |
| `code-review` | no | no |
| `feedback` | no | no |
| `plain-language` | no | no |
| `remove-ai-slop` | yes — prose quality | no |
| `research` | yes — research methodology | **no** (see above) |
| `speculation-control` | yes — epistemic discipline | no |
| `strategic-persuasion` | no | no |
| `strategy-author` | no | no |
| `swe` | no | no |
| `technical-writer` | no | no |

None of the skills reference lifecycle states or CLI commands. The research lifecycle is a Research-repo concern, not a Skills concern.

**Verdict: no changes warranted to any skill in `davidamitchell/Skills`.**

---

## Research repo changes made (this session)

The `reviewing` status and `research draft` command were not yet implemented in the Research repo. The following changes were made as part of this work:

### `src/research/item.py`
- Added `reviewing` to the `status` type comment: `# backlog | in-progress | reviewing | completed`
- Added `"reviewing": "in-progress"` to `state_dir_name()` mapping — items in `reviewing` status stay in `in-progress/`; no file move

### `src/research/cli.py`
- Added `cmd_draft(filename)`: updates `status: reviewing` in frontmatter, keeps file in `in-progress/`, does not move the file
- Added `_get_frontmatter_field(text, key)`: helper to read a frontmatter field value
- Added soft guard to `cmd_complete`: warns (does not block) if `status` is not `reviewing` at completion time
- Registered `draft` as a sub-command in `register_subparser` and `dispatch`

### `research-prompt.md`
- Replaced step 8 ("Complete the item") with a two-step sequence:
  - Step 8: `research draft` + commit + `gh workflow run research-review.yml`
  - Step 9: wait for review result; if FAIL, address violations and loop; if PASS, proceed
  - Step 10: `research complete` (renumbered from old step 8)
  - Steps 9–11 renumbered accordingly

### `.github/copilot-instructions.md`
- Updated Project Overview: "four states" with note that `reviewing` stays in `in-progress/`
- Updated "When NOT to write an ADR": lifecycle now listed as `backlog → in-progress → reviewing → completed`
- Updated "Completing Research" workflow: added `research draft` step and review loop before `research complete`

### `tests/test_research_cli.py`
- Added tests for `cmd_draft`: status update, file not moved, exit on missing
- Added tests for `cmd_complete` soft guard: warns when status ≠ `reviewing`, no warning when status = `reviewing`
- Added tests for `_get_frontmatter_field`: reads value, returns empty for missing key
- Imported `cmd_draft` and `_get_frontmatter_field` in test imports
