# 2026-06-13 — Research: local tooling fragmentation threshold measurement

**Completed:**
- `Research/completed/2026-06-13-local-tooling-fragmentation-threshold-measurement.md` — researched and completed from backlog item. Question: at what scale or operating conditions do aggregate costs of fragmented local tooling exceed productivity gains from customization, and which metrics let organisations detect that crossover early?

**Key findings:**
- Crossover is driven by three structural multipliers: tool footprint per team (absorptive capacity), shared dependency density (coordination overhead), and staff turnover (knowledge-concentration risk exposure)
- Five leading indicators detectable with existing data: support ticket volume growth per tool, new-hire time-to-productivity, shadow-spend growth rate, incident attribution to non-standard tooling, and downstream queue growth rate vs. upstream delivery rate
- No universal numeric threshold exists; the crossover is context-dependent on the three multipliers
- Faros AI 2026 data (22,000 developers: individual +33.7%, PR review +441%, incidents/PR +242.7%) is consistent with TOC queue-flooding at shared constraint, though AI code-quality degradation is a competing explanation
- Shadow IT systematic review (Klotz et al. 2019, 82 papers) and governance-transition literature (Kopper et al. 2020) confirm the same crossover pattern across three prior technology waves

**Sources used:**
- Klotz et al. (2019) systematic review of shadow IT (82 papers): https://aisel.aisnet.org/ijispm/vol7/iss1/3/
- Kopper et al. (2020) shadow IT to business-managed IT governance: https://link.springer.com/article/10.1007/s10257-020-00472-6
- Faros AI 2026 Acceleration Whiplash: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025
- DORA 2025: https://dora.dev/research/2025/dora-report/
- Sinsky (2021) Annals of Family Medicine (abstract only; behind institutional access)

**Review passes:** 2 (auto-passed at review_count=2; second pass failed on §5 per-sentence labels, Assumptions bold pattern, Risks duplicate)

**Learnings.md update:** Added new evidence bullet to Thread 18 (Constraint management); extended Open Thread with bus factor question.

---

## Mini-Retro

1. **Did the process work?** Mostly. The research skill §§0–7 produced solid output, and the evidence base was well-sourced across independent primary and secondary sources. The two review passes caught real issues.

2. **What slowed down or went wrong?**
   - The §5 Depth and Breadth Expansion section is a systematic source of per-sentence label violations. Every paragraph in §5 ends with 2–3 sentences that follow a labeled opening but carry no labels themselves. This is the same pattern that failed in multiple prior items.
   - The Findings Assumptions section bolded full assertion sentences, triggering the inline-header list violation. Bold should apply only to key terms, not entire claim sentences.
   - A duplicate paragraph appeared in Findings Risks (introduced when adding the competing explanation for Faros data to the §6 RSO Risks section — it copied forward a sentence already present).

3. **What single change would prevent this next time?** Before triggering any review, run: `grep -n "^\*\*" <item>` over Findings Assumptions to detect full-sentence bold; scan every §5 paragraph and confirm each sentence after the first labeled one carries its own `[inference; source: URL]` label; and diff the Risks sections between §6 RSO and Findings to catch duplicates.

4. **Is this a pattern?** Yes. The §5 per-sentence label gap is a known recurring pattern (documented in the Known Recurring Patterns table in `.github/copilot-instructions.md` under "Unlabeled closing/summary sentences"). The inline-header bold in Assumptions is a variant of the same "full-sentence bold" pattern. Both should have been caught in Step 6 self-review before triggering the first review workflow.

5. **Does any documentation need updating?** The Known Recurring Patterns table already covers both patterns, but the self-review checklist in Step 6 does not include an explicit "scan §5 paragraph-by-paragraph for multi-sentence paragraphs where only the first sentence is labeled." That specific §5 check should be added.

6. **Do the default instructions need updating?** Add to the Known Recurring Patterns table: "§5 multi-sentence paragraphs with only the opening sentence labeled — every sentence following a labeled opening sentence in §5 must carry its own `[inference; source: URL]` label." The current entry covers closing sentences and §3 causal chains; §5 paragraphs should be called out explicitly.
