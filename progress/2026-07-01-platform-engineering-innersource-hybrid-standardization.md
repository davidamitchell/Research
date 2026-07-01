# 2026-07-01 -- Research Loop (platform-engineering-innersource-hybrid-standardization)

**Completed:**

Research item:
- `Research/completed/2026-06-13-platform-engineering-innersource-hybrid-standardization.md` -- completed; finds that platform engineering (golden paths, self-service with guardrails), InnerSource contribution patterns (Trusted Committer, Common Requirements, Portal), and Bartlett and Ghoshal's transnational operating-model archetype converge on the same structural prescription: a well-supported standard core plus sanctioned local extension points, paired with monitoring of the shared constraint's capacity, is the most reliable design for preserving local agility without fragmentation. DORA 2024 evidence shows platform engineering can decrease change stability when extension points create shared single-point dependencies, and a companion completed item on local-to-global throughput loss shows the same failure recurs whenever local acceleration is not matched by shared-constraint capacity increases.

This session picked up the item at Step 8 (one review pass already run). The first review pass had failed due to Copilot API quota exhaustion (no actual violations were produced), so a second review pass was triggered and produced real, actionable violations (pass 2 of 2, which auto-passes per the workflow's review cap regardless of outcome). Rather than relying on the auto-pass, the flagged violations were fixed before completing: an unexpanded "IDP" acronym at first prose use, an inaccurate §7 acronym-audit self-description, a `[fact]` label that should have been `[inference]` per the item's own §4 consistency-check note, two banned words ("genuinely", "inevitably"), two Key Findings and their Evidence Map rows downgraded from high to medium confidence (single-source claims), and two materially related completed items (local-tooling-fragmentation-threshold-measurement and local-global-optima-knowledge-work-throughput) cited in Open Questions and Analysis where the review found they were listed in `related:` but never engaged with in the body. Both items were promoted from `related:` to `cites:` in frontmatter to reflect the direct citation.

Sources consulted:
- https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem (Spotify golden path origin case, already in item)
- https://dora.dev/research/2024/dora-report/ (DORA 2024 platform-engineering stability finding, already in item)
- https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html (cross-referenced for Open Question 1)
- https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html (cross-referenced for Analysis rival-model discussion)

## Mini-Retro

1. **Did the process work?** Yes. Picking up mid-loop at Step 8 worked cleanly once the actual review log (not just the run conclusion) was inspected -- the workflow's `success` conclusion on the first review run was misleading because the Copilot review agent itself had hit a quota error and never produced real findings.
2. **What slowed down or went wrong?** The first review pass consumed a run without producing signal (quota exhaustion mid-review), and the run's GitHub Actions conclusion showed "success" even though the log showed the review agent failing. This matches the documented caveat in the prompt ("do not trust the workflow conclusion alone") but the failure mode here was one step earlier: a completely empty/non-informative review, not a stale PASS after a real FAIL.
3. **What single change would prevent this next time?** None needed in this item's process -- the existing "log is the source of truth" instruction already covers this. No change made.
4. **Is this a pattern?** Possibly emerging: transient Copilot API quota errors causing a review pass to be consumed without producing a report. If this recurs, it would be worth adding an explicit check in Step 8 for "Copilot review agent failed" in the log (distinct from an actual `OVERALL: FAIL` with `VIOLATION:` lines) so the loop treats a quota-exhaustion failure as non-informative rather than counting it against the review cap.

## Pending skill improvements

None identified -- the fixes applied were standard citation-discipline, speculation-control, and peer-reviewer style corrections already covered by existing skill files.
