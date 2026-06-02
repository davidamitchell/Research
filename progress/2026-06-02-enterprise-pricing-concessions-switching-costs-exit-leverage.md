# 2026-06-02 -- Research complete: enterprise-pricing-concessions-switching-costs-exit-leverage

**Item:** `Research/completed/2026-05-30-enterprise-pricing-concessions-switching-costs-exit-leverage.md`

**Completed:**
- `Research/completed/2026-05-30-enterprise-pricing-concessions-switching-costs-exit-leverage.md` — researched and completed; answers how enterprise vendors use upfront pricing concessions to build switching costs and what architectural/contractual/regulatory strategies preserve exit leverage across the contract lifecycle.
- `learnings.md` — added Thread 24 linking this item to three prior completed items (transaction costs, IT run-cost forecasting, vendor platform governance).

**Evidence gathered:**
- Klemperer (1987) two-period pricing model; Farrell and Klemperer (2007) survey — theoretical foundation
- CMA Final Decision (July 2025) — empirical: sub-1% annual UK cloud switching, £500M overcharge estimate, SMS designation recommendation
- EU Data Act (2023/2854) Articles 25 and 29 — regulatory: switching-facilitation obligations, egress fee elimination by Jan 2027
- ERP TCO industry data (ERPResearch, ArionERP) — 20-30% licensing / 70-80% lifecycle cost split; 25-50% switching cost estimate
- CNCF Cloud Native Definition v1.1 — architectural: containers, declarative APIs as lock-in reduction

**Review runs:**
- Run 1 (26817310300): FAIL — fixed bold Key Findings, em-dashes, fact/inference label, ROI expansion
- Run 2 (26817853451): FAIL — fixed CMA primary source citation, removed CEPR from maintenance fee sentence, Analysis paragraph openers, added network effects rival explanation, cross-references to two related items
- Run 3 (26818485068): FAIL (pass 2/2, no issue raised, cap reached) — fixed per-sentence citations in Analysis, removed "is clear" overconfident qualifier, rewrote Rule-of-Three formulaic structure
- Run 4 (26819025408): PASS (auto-pass at cap 2/2)

**Seeded URL error found and corrected:** The seeded NBER URL (https://www.nber.org/papers/w12911) resolved to Banerjee et al. on public goods, not Farrell/Klemperer. Correct URL: https://cepr.org/publications/dp5798.

## Mini-Retro

1. **Did the process work?** The research and writing process worked well — §0–§7 were completed in a single pass with good coverage. Four review runs were required, one more than the cap, which is a quality gap. Each review cycle caught real violations that the self-review step missed.

2. **What slowed down or went wrong?**
   - The "per-sentence citation" rule for multi-sentence paragraphs was applied inconsistently; self-review only checked that trailing labels existed, not that every sentence carried one.
   - The "Rule-of-Three" AI slop pattern in Analysis was introduced when fixing the paragraph opener monotony issue — replacing one violation with another.
   - Farrell and Klemperer's paper title ("...Competition with Switching Costs and Network Effects") was not read carefully enough at the start; network effects were treated as outside scope without explanation.

3. **What single change would prevent this next time?** Before committing, run an explicit sentence-by-sentence scan of every paragraph in Analysis and apply "does this sentence make a claim? If yes, does it have its own inline label and source?" rather than checking only the paragraph's trailing label.

4. **Is this a pattern?** Yes — multi-sentence paragraph with single trailing citation is listed in the Known Recurring Patterns table (the "Executive Summary multi-sentence paragraph with a single trailing citation block" entry). This recurred in the body Analysis paragraphs, not only the Executive Summary. The pattern is broader than documented.

5. **Does any documentation need updating?** The Known Recurring Patterns table should be extended to note that the multi-sentence / single-trailing-citation failure applies to every multi-sentence paragraph in Findings (Analysis, Risks, etc.), not only the Executive Summary.

6. **Do the default instructions need updating?** The existing pattern entry in copilot-instructions.md covers Executive Summary; it should explicitly say "every multi-sentence paragraph in Findings" to prevent the Analysis recurrence.
