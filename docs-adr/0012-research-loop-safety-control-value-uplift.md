# ADR-0012: Research Loop Safety Control Value Uplift

Date: 2026-04-27
Status: accepted
Supersedes: safety control values in [ADR-0004](0004-autonomous-research-loop.md)

## Context

The research loop has been running successfully for several weeks. Two operational
pressures prompted a review of the numeric safety-control values established in ADR-0004:

1. **Throughput.** A 3-item scheduled cap processes 15 items per week. As the backlog grew,
   this was too slow to keep pace with new additions. 4 items/day (20/week) better matches
   the current ingest rate.

2. **Timeout.** The 90-minute ceiling was set conservatively when item processing times were
   unknown. Observed processing times are 20–45 minutes per item. A 4-item run with
   worst-case items (4 × 45 min) exceeds 90 minutes, causing the job to be killed mid-item.
   150 minutes provides headroom without being reckless.

3. **Dispatch options.** The 1–5 dropdown was insufficient for manual catch-up runs after
   holidays or rate-limit pauses. Extending to 1–7 matches the `HARD_MAX_ITERATIONS`
   ceiling (10) with a comfortable margin.

A secondary problem was discovered during this change: the Copilot agent running the
research loop treats inline comments and description strings as authoritative spec. When
code values diverge from those strings — even intentionally — the agent reverts the code
to match the documentation. All documentation must therefore be updated atomically with
the values, or the change will not persist.

## Decision

Update the three safety-control values and propagate them consistently to every location
that references them:

| Control | Old value | New value |
|---|---|---|
| `timeout-minutes` | 90 | 150 |
| Scheduled `MAX_ITEMS` | 3 | 4 |
| Dispatch `max_items` options | 1–5 | 1–7 |

Files updated atomically in a single commit:
- `.github/workflows/research-loop.yml` — code, inline comments, description string, and header comment block
- `docs-adr/0004-autonomous-research-loop.md` — control table, prose, and trade-offs section
- `.github/copilot-instructions.md` — schedule throughput and safety-controls summary
- `tests/test_research_loop.py` — timeout assertion and upper-bound check

The structural safety controls from ADR-0004 are unchanged: `HARD_MAX_ITERATIONS` (10),
`FAILURE_THRESHOLD` (2), `INTER_ITERATION_SLEEP` (30 s), and the concurrency group
remain as designed.

## Consequences

### Positive
- 4-item scheduled runs process 20 items/week, keeping pace with backlog growth.
- 150-minute timeout accommodates worst-case 4-item runs without false-positive kills.
- 1–7 dispatch options support manual catch-up without requiring workflow edits.
- Atomic documentation update prevents the Copilot agent from reverting the change.

### Negative / Trade-offs
- A 4-item scheduled run takes at least 2 minutes of inter-iteration sleep overhead (up from 1 minute).
- The higher timeout means a genuinely hung job takes longer to be killed. The
  `FAILURE_THRESHOLD` and `HARD_MAX_ITERATIONS` guards remain in place to catch this
  before the timeout fires.
- Dispatch options 6 and 7 approach `HARD_MAX_ITERATIONS` (10). If the hard ceiling is
  ever lowered, the options list must be re-checked.

### Neutral
- The test suite enforces the new values; any future agent revert will fail CI.
