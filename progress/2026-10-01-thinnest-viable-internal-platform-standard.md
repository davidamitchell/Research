# 2026-10-01 — Add backlog item (thinnest-viable-internal-platform-standard)

**Completed:**
- `Research/backlog/2026-10-01-thinnest-viable-internal-platform-standard.md` — added from issue #665; formulates a ready-to-investigate question about the thinnest viable internal platform and a practical product-management standard for platform teams.

The candidate passed the research-question skill's Specific, Answerable, Scoped, Motivated, and Decomposable tests. The expected output is knowledge. Research itself was not conducted.

**Validation:**
- 28 targeted research-item and theme tests passed.
- Full suite: 620 passed, 2 skipped, 1 failed because `TAVILY_API_KEY` is unavailable in this sandbox.
- `make check`: lint passed; format check found four pre-existing violations in unrelated completed research items.
- Manual checks confirmed item metadata, URL-linked sources, internal links, empty research placeholders, and the six-part Mini-Retro.

## Mini-Retro

1. **Did the process work?** Yes. Applying the research-question skill resulted in clear scope boundaries and a decomposed path from first-principles criteria to an assessable standard.
2. **What slowed down or went wrong?** The skills submodule was initially unpopulated. Repository-wide validation also found four formatting violations in unrelated completed items and a missing `TAVILY_API_KEY` for one integration test.
3. **What single change would prevent this next time?** Initialize the skills submodule before intake work; address the unrelated formatting baseline and configure the integration-test secret through their own maintenance tasks.
4. **Is this a pattern?** The submodule setup is already documented; the validation blockers predate and are outside this intake change.
5. **Does any documentation need updating?** No. This intake adds a backlog item, not research findings or a change to repository behavior.
6. **Do the default instructions need updating?** No new convention or constraint emerged.

## Related

- [First-principles taxonomy of modern technology platforms](https://davidamitchell.github.io/Research/research/2026-09-14-modern-technology-platform-taxonomy.html)
- [Platform engineering, InnerSource, and standard-core plus local-extension operating models](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [Local optimisation of team- and role-level tooling in knowledge work](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)

---

# 2026-10-02 — Research loop: complete the item

**Completed:**
- Ran the full `research` skill (§0–§7) against `Research/in-progress/2026-10-01-thinnest-viable-internal-platform-standard.md`, cross-referencing the three prior completed items above, then seeded `## Findings` from `§6 Synthesis`.
- Ran `research draft`, committed, pushed, and triggered `research-review.yml` (run `36945112446`). **Result: OVERALL FAIL** (4 violations: two mislabeled-superlative `[fact]` claims that should have been `[inference]`, 29 prohibited em-dashes, and an Executive Summary sentence that attributed a funding/staffing finding to both the Cloud Native Computing Foundation (CNCF) and Microsoft when only the CNCF source supported it). The review's own commit failed to push (race condition against my prior push), so this pass did not consume review budget per the repository's documented recurring-pattern fix.
- Fixed all four violations (removed every em-dash, relabeled the two superlatives as `[inference]`, narrowed the Executive Summary claim to CNCF-only, mirrored the fix into `§6 Synthesis` for parity) and resubmitted (run `36945626159`). **Result: OVERALL FAIL**, this time for real (review commit `91a9002` landed, consuming pass 1 of 2): two citation-discipline violations for naming "Flow Framework," "Theory of Constraints," and "Conway's Law" without binding them to authoritative definition sources.
- Added authoritative definition links (Flow Framework Community's Discover page, the Theory of Constraints Institute, and Conway's original 1968 essay) at first use and to `## Sources`, committed, pushed, and resubmitted (run `36946050725`, review commit `3fc09be`, pass 2 of 2). **Result: OVERALL FAIL** on a single trivial violation: "PDF" used unexpanded in an Access note.
- Fixed the PDF expansion, committed, pushed, and triggered review once more (run `36946391492`). Because `review_count` was already at the workflow's cap of 2, this run auto-passed per the workflow's documented cap-reached behaviour (no new commit, 16-second run, no FAIL warning).
- Ran `python -m src.main research complete 2026-10-01-thinnest-viable-internal-platform-standard.md`, moved the item to `Research/completed/`, and set `output: [knowledge]` in frontmatter (the move script left it as `[]`).
- Added a new evidence bullet to `learnings.md` Thread 18 (Constraint management as a general systems design principle), connecting the Thinnest Viable Platform (TVP) satisfiability standard's voluntary-adoption and net-feature-removal diagnostics to the thread's existing Theory of Constraints subordination-principle vocabulary.

**Validation:**
- `ruff format --check` passed on every commit touching the item.
- `grep -c "—"` confirmed zero em-dashes after the fix.
- Confirmed via `git log origin/main` after each push that the review's own commit landed (or, for the first FAIL, that it did not, per the race-condition pattern) before treating a review pass as consumed.

## Mini-Retro

1. **Did the process work?** Yes, but it took three real review cycles (plus one race-condition false-start) to reach a clean pass, each time catching a genuinely new and distinct class of violation rather than repeating prior ones — the self-review process before the first submission caught many issues but not all of them.
2. **What slowed down or went wrong?** Two judgment errors survived self-review: (a) treating em-dashes in the Sources list and Access notes as "acceptable, list style" when the rule is an absolute zero-exception prohibition, and (b) labeling the item's own evaluative judgments about its sources ("most rigorous evidence," "weakest evidence") as `[fact]` rather than recognising they are the item's own comparative inference, not a fact the source itself asserts. A third gap was citing named frameworks (Flow Framework, Theory of Constraints, Conway's Law) by name without binding the first use to an authoritative external definition source, even though the self-review checklist named this exact check for other domain terms.
3. **What single change would prevent this next time?** Before the first review submission, run a dedicated em-dash grep as an explicit, separate pre-submission gate (not folded into the general self-review pass), and treat any evaluative or comparative adjective applied to the item's own evidence ("most," "weakest," "strongest," "most reliable") as a trigger to double-check the label is `[inference]` rather than `[fact]`.
4. **Is this a pattern?** Yes — both the em-dash-in-lists exception and the self-evaluative-superlative mislabeling match existing entries in the Known Recurring Failure Patterns table in `.github/copilot-instructions.md` (closely related to, but not identical to, prior entries); no new pattern needs to be added, but it confirms those existing entries are still live risks worth re-reading before every submission, not just after a first failure.
5. **Does any documentation need updating?** No new convention emerged beyond what is already documented; the existing Known Recurring Failure Patterns table already covers the failure classes encountered.
6. **Do the default instructions need updating?** No — the instructions already specify the fixes needed; the gap was in applying them during self-review, not in the instructions themselves.
