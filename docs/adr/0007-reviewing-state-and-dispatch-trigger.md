# ADR-0007: Reviewing state and workflow_dispatch trigger for research review

Date: 2026-03-11
Status: Accepted

## Context

The research item lifecycle was `backlog → in-progress → completed`. The review workflow
(`research-review.yml`) fired on a `push` trigger when files landed in `Research/completed/`.
This created two problems:

1. **No rework loop.** Review ran after the item was already marked done. If review failed,
   the item had to be moved back manually — a backward file move that polluted git history.
2. **Implicit activation.** The `push` trigger coupled review to the file-move commit. Any push
   to `Research/completed/` triggered review, including corrections, reformats, and metadata
   changes that had nothing to do with a new item completion.

Two constraints shaped the solution:

- Items must not move out of `in-progress/` until review passes. A mid-lifecycle directory move
  creates noise in git history and makes the state machine harder to reason about.
- The research loop calls `gh workflow run` explicitly after drafting — an explicit trigger is
  always available and does not require path-based automation.

## Decision

### 1. Add `reviewing` as a fourth lifecycle state

```
backlog → in-progress → reviewing → completed
               ↑_____________|
        (review fail: status reset to in-progress)
```

`reviewing` maps to `"in-progress"` in `state_dir_name()`. The file does not move when an item
enters `reviewing`. The single file move (`in-progress/ → completed/`) happens only after review
passes (or is explicitly overridden).

`cmd_draft` sets `status: reviewing` in-place. No file move.

### 2. Replace the push trigger with workflow_dispatch only

`research-review.yml` now has a single trigger: `workflow_dispatch` with an `item_path` input.

The research loop (or a human) calls:

```bash
gh workflow run research-review.yml -f item_path=Research/in-progress/<filename>
```

This is explicit over implicit — review only fires when requested, not on every push to a path.

### 3. Soft guard on `cmd_complete`

`cmd_complete` reads the current `status` before completing. If the status is not `reviewing`,
it prints a warning to stderr and logs a warning — but proceeds anyway. This is a soft guard,
not a hard block.

Rationale: a hard block would prevent the owner from completing an item if a reviewer false
positive were stuck. The warning is sufficient to surface the deviation without blocking the loop.

## Consequences

### Positive

- Clean git history: the only file move is the final `in-progress/ → completed/` transition.
- Explicit review activation: no surprise reviews triggered by metadata commits.
- Rework loop: a failed review resets `status` to `in-progress` and the agent loops back.
- `item_path` now accepts `Research/in-progress/` paths, removing the artificial restriction
  to `Research/completed/`.

### Negative / Trade-offs

- Review is no longer automatic on push — the loop must call `gh workflow run` explicitly.
  This is intentional (explicit over implicit) but adds one step to the research loop.
- The soft guard on `cmd_complete` means it is possible to complete an item that was never
  reviewed. The warning is the only signal. Future work could add a stricter flag.

### Neutral

- `workflow_dispatch` with `item_path` already existed and is tested. No new infrastructure.
- `contents: read` permission on the review job is unchanged.
- No new directories introduced.
