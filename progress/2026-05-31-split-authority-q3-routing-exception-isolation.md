# 2026-05-31 -- Research complete: split-authority-q3-routing-exception-isolation

**Item:** `Research/completed/2026-05-29-split-authority-q3-routing-exception-isolation.md`
**Status:** completed
**Review passes:** 4 (2 workflow passes, each required a fix cycle; review cap reset mid-session)

## Completed

- Researched intake, triage, queueing, escalation, and routing model for split-authority delivery systems.
- Built on Q2 three-class demand model (Class 1 fast path, Class 2 standard path, Class 3 exception path).
- Key findings: three-lane physical routing with Drum-Buffer-Rope hybrid scheduling; WIP limit on exception lane; three observable item-level escalation triggers (failed recovery test, blast radius breach, template deviation); named single decision authority for item-level escalation; named integrator authority for system-level circuit-breaker.
- Evidence drawn from: Little's Law, Reinertsen's classes of service, ITIL 4 change enablement, SRE Incident Command System, Theory of Constraints, DORA metrics, Adler & Borys enabling formalisation.
- Companion items cited: Q2 demand segmentation, P1 operating model synthesis, backpressure/ToC item, governance controls item.

## Mini-Retro

1. **Did the process work?** The research and evidence gathering worked well. The iterative review cycle did not — four passes were needed where the intent was two. The pattern of unlabeled paragraph-closing and paragraph-opening summary sentences recurred across three review cycles.

2. **What slowed down or went wrong?**
   - The known recurring pattern "unlabeled closing/summary sentences" applied to every review pass. The §5 Historical Lens closing sentence, §3 causal chain items 1-4, §5 Behavioural Lens closing sentence, and §6/Findings Analysis opening sentences were all unlabeled at the time of each respective review.
   - The ITIL AXELOS URL was flagged as a marketing page not supporting specific procedural claims. A secondary ITIL source (invensislearning.com) was required.
   - The "correct" evaluative adjective was used three times (§2 D3, §5 ICS sentence, KF 7) and had to be removed.
   - `[fact]` was applied to a DBR application claim that should have been `[inference]`.
   - Bold applied to full Key Finding sentences in `## Findings` (the known inline-header-list violation).
   - Review counter did not reset between fix cycles, so the workflow treated fix-and-retrigger passes as continuation of the original two-pass cap, eventually treating a third and fourth submission as cap-already-reached.

3. **What single change would prevent this next time?** Run an explicit scan before every commit: `grep -n '\.\s*$' <item>` across §3, §5, §6, and Findings to find period-terminated sentences without a trailing epistemic label. Every paragraph-closing sentence in non-metadata sections must carry its own label and source. Do not rely on the label of the preceding sentence extending forward.

4. **Is this a pattern?** Yes. This is the "unlabeled closing/summary sentences" pattern already in the Known Recurring Patterns table. The table notes it as the single most common failure in the pass 5–10 range. This session confirmed it also dominates early passes when the item is written as flowing prose and labels are added only to the primary claim sentence in each paragraph, not to each closing inference.

5. **Does any documentation need updating?** The Known Recurring Patterns table entry for "unlabeled closing/summary sentences" should be updated to emphasise §3 causal chain lists, not just §6 Synthesis and Executive Summary opening sentences. The check instruction in Step 6 should explicitly mention §3 numbered lists.

6. **Do the default instructions need updating?** The pre-commit checklist in Step 6 item 2 already covers this, but the scope is "§6 Synthesis and Findings Executive Summary opening sentences". Expanding the scope to include §3 numbered causal chain items would have caught items 1-4 in this session. Recommend adding: "Scan §3 numbered list items — each must carry its own [fact], [inference], or [assumption] label and URL-backed source."
