# 2026-05-09 -- Research Loop (ai-capability-reference-architecture-second-cycle-update)

**Completed:**

Research item:
- `Research/completed/2026-05-08-ai-capability-reference-architecture-second-cycle-update.md` -- completed; the update keeps the five-layer enterprise AI architecture, but widens the prior provenance plane into a provenance-and-legibility plane and widens the governance plane into a governance, evaluation, and operational-assurance plane. The main new capabilities are declared AIBOM generation, runtime-evidence normalization, delegation receipts, operating-assurance controls from production incidents, and regulator-facing governance components for board literacy, supplier risk, logging, rollback, and evidence assembly.

Sources consulted:
- https://davidamitchell.github.io/Research/research/2026-05-06-ai-capability-reference-architecture-security-supply-chain-update.html (first-cycle architecture baseline)
- https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html (incident-driven control deltas)
- https://davidamitchell.github.io/Research/research/2026-05-07-ai-regulatory-guidance-update-gap-check.html (regulatory governance deltas)

## Mini-Retro

1. **Did the process work?** Yes; the item moved cleanly through draft, review, fix, and completion, and the review workflow surfaced the few weak spots that mattered.
2. **What slowed down or went wrong?** The main slowdown was that coined domain terms such as AIBOM and legibility needed authoritative external definition sources, not only internal synthesis citations, and that was caught late by review.
3. **What single change would prevent this next time?** Add an explicit pre-review rule that any central domain term defined by synthesis, such as AIBOM or legibility, must bind its first use to an authoritative external definition source. 
4. **Is this a pattern?** Not yet a confirmed recurring pattern, but it is similar to prior first-use and citation-discipline failures, so the prompt should catch it earlier.

## Applied improvements

- Updated `research-prompt.md` to require at least one authoritative external definition source on the first use of any central synthesized domain term, rather than relying only on completed repository items.
