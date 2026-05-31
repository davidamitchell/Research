# 2026-05-31 -- capability-claim-telemetry-conflict-arbitration

**Completed:**
- `Research/completed/2026-05-31-capability-claim-telemetry-conflict-arbitration.md` — researched and completed; answers which arbitration mechanism (telemetry override, structured challenge, third-party audit) most reliably corrects capability overestimation when team claims conflict with production telemetry; key finding: the choice must match root cause — optimism bias vs strategic misrepresentation require different remedies; no head-to-head comparison study exists in software delivery.

**Sources investigated:**
- Flyvbjerg, Holm and Buhl (2002) — 258-project dataset; 86% overrun rate; core quantitative evidence
- Flyvbjerg (2003) Megaprojects and Risk — optimism bias vs strategic misrepresentation distinction
- Kahneman and Lovallo (1993) — inside vs outside view; reference class forecasting (RCF)
- Kahneman and Tversky (1979) — original optimism bias and planning fallacy identification
- Mitchell, Russo and Pennington (1989) — pre-mortem controlled experiment
- Google SRE Workbook: Error Budget Policy — telemetry override mechanism with CTO escalation path
- Google SRE Workbook: Implementing SLOs — SLO/SLI definitions
- GAO Cost Estimating and Assessment Guide (GAO-20-195G) — Independent Cost Estimate (ICE) methodology
- DORA 2023 State of DevOps Report — self-report accuracy limitations

**Key findings:**
1. Capability overestimation is systematic (86% of large infrastructure projects overrun; average 20-44% above estimates)
2. Two root causes require different remedies: optimism bias (debiasing) vs strategic misrepresentation (accountability structures)
3. Telemetry override is most structurally direct because it removes team self-assessment from the loop
4. No head-to-head comparison study exists across all three mechanisms in software delivery settings
5. All three mechanisms fail without accountability structures

**Review outcome:** 2 passes, both FAIL; completed per `review_count >= 2` rule. Persistent violations included comparative superlatives in Executive Summary lacking inline labels, a single-source high-confidence claim (KF6), and a comparative ranking labeled [fact] in §2.B.

**learnings.md updated:** Thread 12 updated with measurement-independence corollary.

---

## Mini-Retro

1. **Did the process work?** The research skill process worked well for structuring the investigation and producing a complete item. The evidence base was clear and well-sourced across four distinct research domains.

2. **What slowed down or went wrong?** Three review passes were needed. The recurring issues were: (a) comparative evaluative claims mislabeled as [fact] instead of [inference], (b) the Executive Summary not carrying individual sentence labels despite the trailing citation pattern, and (c) the em-dash scan in §7 incorrectly reported "no em-dashes found" when multiple were present.

3. **What single change would prevent this next time?** Before any review run, scan every sentence in the Executive Summary individually for an inline `[inference; source:]` or `[assumption; source:]` label — the trailing-citation pattern on the final sentence does NOT cover preceding sentences. This is the most common Executive Summary violation.

4. **Is this a pattern?** Yes — the "unlabeled closing/summary sentences" pattern is already documented in the Known Recurring Patterns table in `.github/copilot-instructions.md`. The §7 em-dash false-negative is also a new variant of the "em_dash_scan" issue. The §2.B `[fact]` on a comparative-ranking claim ("most fully documented") is the "unlabeled evaluative judgments" pattern also in the table.

5. **Does any documentation need updating?** The §7 em-dash scan failure pattern should be noted: the §7 self-audit cannot reliably detect its own scanning errors; future items should use an external `grep` check for em-dashes before committing, not rely on the §7 report alone.

6. **Do the default instructions need updating?** No new patterns beyond those already documented. The existing guidance on Executive Summary labeling and comparative-superlative inference labels in the Known Recurring Patterns table covers the violations observed.
