# 2026-03-27 — Research Loop (cost-reduction-is-not-strategy)

**Completed:**

Research item:
- `Research/completed/2026-03-26-cost-reduction-is-not-strategy.md` — completed; argues that cost reduction fails as a strategy because it strips unmeasured value while booking only visible savings — the "doorman fallacy" (Sutherland). Nike's Consumer Direct Acceleration (2020–2024) is the empirical anchor: pulling back from wholesale to capture margin destroyed brand omnipresence and required full reversal under CEO Elliott Hill. AI is now being pitched to CFOs through the same cost-reduction frame, risking the same category of value destruction at scale; Amazon's recommendation engine (35% of sales) demonstrates the alternative opportunity frame.

Sources consulted:
- https://shows.acast.com/business-leader-podcast/episodes/rory-sutherland-the-advertising-gurus-tips (Business Leader podcast — Sutherland/Harpin, Jan 2026; primary source for doorman fallacy and cost-vs-strategy argument)
- https://www.retaildive.com/news/nike-pivots-dtc-wholesale-strategy-flat-sales-earnings/711102/ (RetailDive — Nike DTC reversal analysis)
- https://www.ifm.eng.cam.ac.uk/research/dstools/porters-generic-competitive-strategies/ (Cambridge IFM — Porter's generic strategies; theoretical framework)

## Mini-Retro

1. **Did the process work?** Yes — the research loop produced a complete, substantive item with a clearly falsifiable core claim, strong empirical support (Nike), and a credible mechanistic explanation (measurement asymmetry). The review cycle caught genuine citation and labelling issues that improved the item.

2. **What slowed down or went wrong?** Review pass 1 returned 13 violations. The majority were source-URL gaps and em-dashes in the Findings section, most of which should have been caught in the Step 8 self-review. The stash/pull/rebase dance added minor friction. A second review was required; the item auto-passed on review_count reaching 2.

3. **What single change would prevent this next time?** Run a dedicated em-dash grep over `## Findings` before committing the draft — `grep -n " — " Research/in-progress/<file>.md | awk 'NR > [findings_start_line]'` — and confirm every `[fact — Source]` citation block in §2 includes a URL before marking the item ready.

4. **Is this a pattern?** Yes — citation URL gaps and em-dashes in Findings are the two most common review failure modes, both noted in the Known Recurring Patterns table in the instructions. The em-dash issue persisted into Assumptions and Open Questions sub-sections even after fixing the Executive Summary and Key Findings prose, suggesting the zero-tolerance scope needs to be applied to the entire `## Findings` section uniformly, not just the named sub-sections.
