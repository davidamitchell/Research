# 2026-05-19 -- Research Loop (rq5-1-stochastic-vs-deterministic-failures)

**Completed:**

Research item:
- `Research/completed/2026-05-18-rq5-1-stochastic-vs-deterministic-failures.md` -- completed; the item concludes that deterministic and stochastic systems share the same abstract fault-error-failure chain but differ in where failure becomes visible. Deterministic workflows more often expose invalid-input failures as explicit or replayable boundary failures, while stochastic Large Language Model agents are more prone to silent semantic drift, path variance across identical reruns, and multi-step propagation once corrupted context is accepted.

Sources consulted:
- https://arxiv.org/abs/2302.12173 (indirect prompt injection as data-instruction boundary failure)
- https://arxiv.org/abs/2408.04667 (repeated-run nondeterminism under supposedly deterministic settings)
- https://cloudintelligenceworkshop.org/papers/aiops26-Ranganathan.pdf (production incident telemetry for Large Language Model serving)

## Mini-Retro

1. **Did the process work?** Yes. The research-and-review loop surfaced where I had overstated inferential claims and forced the item back onto narrower, better-supported wording.
2. **What slowed down or went wrong?** The review workflow auto-pass path still required manual log inspection because the run conclusion alone did not reflect the remaining violations, and one seeded telemetry source could not be located directly.
3. **What single change would prevent this next time?** Nothing immediate; the current prompt already warned about auto-pass logs and inferential overreach, and those checks did catch the real problems.
4. **Is this a pattern?** Yes. It matches existing repository patterns around overstated synthesis claims and around needing to inspect review logs rather than trusting the workflow conclusion alone.
