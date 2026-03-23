# ADR-0004: Autonomous Research Loop Design and Safety Controls

Date: 2026-03-02
Status: accepted

## Context

The repository needs an automated mechanism to drain the `Research/backlog/` queue without
requiring the owner to manually process each item. The owner interacts exclusively via the
GitHub website and iOS app — no local shell, no Codespaces.

The chosen approach — a GitHub Actions workflow that invokes the GitHub Copilot CLI in a
loop — is a direct application of the **Ralph Wiggum Technique**: each agent session
processes exactly one item (fresh context window), with an outer shell loop that restarts
Copilot for the next item.

Because the loop runs autonomously and commits directly to `main`, runaway behaviour
(e.g. a hung Copilot session, an infinite loop bug, or API rate-limit exhaustion) could
cause serious harm: wasted GitHub Actions minutes, corrupted repository state, or
uncontrolled API spend.

This ADR documents the design decisions and the safety controls that mitigate those risks.

## Decision

### Secret name

The workflow authenticates with a GitHub Personal Access Token stored as the repository
secret `COPILOT_GITHUB_TOKEN`. This name is specific and self-documenting. The previous
name `GH_TOKEN` was generic and could be confused with the auto-provided `GITHUB_TOKEN`.

### Runaway loop controls

Five independent safety controls are layered to stop runaway behaviour:

| Control | Mechanism | Value |
|---|---|---|
| Job timeout | `timeout-minutes` on the GitHub Actions job | 90 minutes |
| Per-run item cap | `MAX_ITEMS` from workflow input or schedule default | 1 (dispatch) / 3 (schedule) |
| Hard iteration ceiling | `HARD_MAX_ITERATIONS` constant in the shell script | 10 |
| Consecutive failure abort | `FAILURE_THRESHOLD` + `CONSECUTIVE_FAILURES` counter | 2 consecutive failures |
| Inter-iteration sleep | `INTER_ITERATION_SLEEP` between loop iterations | 30 seconds |

**Job timeout** is the hardest ceiling. GitHub Actions will kill the entire job after
90 minutes regardless of what the shell script is doing. Even if every other control fails,
the job cannot run indefinitely.

**Per-run item cap** limits expected throughput. The `max_items` input is a constrained
dropdown (choices 1–5), removing the possibility of accidentally entering 0 or an
arbitrarily large number.

**Hard iteration ceiling** is a defence-in-depth guard independent of `max_items`. Even
if `max_items` were somehow set to a large value, the shell loop exits at 10 iterations.

**Consecutive failure abort** prevents a broken Copilot invocation from silently looping.
If Copilot fails twice in a row without making progress, the job exits with an error,
triggering a GitHub Actions notification.

**Inter-iteration sleep** serves two purposes:
1. Provides GitHub API rate-limit recovery time between Copilot invocations.
2. Makes runaway loops detectable: if the job is clearly taking much longer than
   `max_items × expected_item_time`, something is wrong.

### Concurrency

`cancel-in-progress: false` on the `research-loop` concurrency group ensures that a
scheduled run triggered while a previous run is still processing an item does not kill
the in-progress work. A new run queues and starts only after the current run finishes.

### Shell error handling

The loop step uses `set -euo pipefail` so any unexpected command failure immediately
aborts the script, preventing silent partial failures from corrupting state.

### Prompt as the only tuning lever

All agent behaviour is controlled by `research-prompt.md`. The workflow YAML is not
touched to change research priorities, findings structure, or writing style. This
separation keeps the feedback loop short: the owner edits one file, the next run picks
it up automatically.

## Rejected Alternatives

### Unlimited `max_items` (original design)

The first version accepted `max_items` as a free-text string, with `0` meaning
"process the entire backlog". This was removed because:
- A scheduled run with `max_items=0` could exhaust the backlog in one run, consuming
  significant Copilot minutes and leaving no items for future sessions.
- No hard timeout was set, meaning a hung session could run indefinitely.

### Claude Code CLI

An early version of this workflow used the `claude` CLI (Anthropic Claude Code). This was
replaced with the GitHub Copilot CLI because:
- The owner does not have an Anthropic API key.
- The Copilot CLI requires only the `COPILOT_GITHUB_TOKEN` (GitHub PAT), which the owner
  already needs for direct `main` pushes.
- Using Copilot aligns with the owner's existing GitHub subscription.

### Pull-request-per-item model

An alternative would create a GitHub Issue per backlog item, assign it to `@copilot`, and
wait for the resulting PR. This was not chosen because:
- It requires manual PR review and merge, adding friction the owner wanted to avoid.
- It produces PRs, which the owner explicitly does not need for this repo.
- The Ralph pattern (direct `main` commits from a loop) fits the use case better.

## Consequences

### Positive
- The loop runs unattended and drains the backlog while the owner sleeps.
- Multiple independent safety controls prevent runaway behaviour.
- The constrained dropdown prevents accidental large-batch runs.
- The concurrency group prevents overlapping runs from conflicting.
- ADR-0004 + tests prove the controls are in place and will catch regressions.

### Negative / Trade-offs
- The 30-second inter-iteration sleep adds latency when processing multiple items.
  A 3-item scheduled run takes at least 1 minute of sleep overhead. This is acceptable.
- The hard ceiling of 10 iterations prevents processing large backlogs in a single run.
  The scheduled trigger running weekdays at 07:00 UTC (3 items/day) compensates.
- The workflow does not retry after a Copilot failure; it only tracks consecutive failures.
  A single isolated failure increments the counter but does not immediately abort.

### Neutral
- `research-prompt.md` must be kept accurate. If it goes stale, the agent may behave
  incorrectly. This is explicitly noted in `AGENTS.md`.
- The `timeout-minutes: 90` is generous relative to expected item processing time (≤30
  minutes per item). It is deliberately conservative to avoid false-positive timeouts on
  unusually complex research items.
