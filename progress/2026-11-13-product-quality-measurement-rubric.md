# 2026-11-13 -- Research: product-quality-measurement-rubric

**Completed:**
- `Research/completed/2026-11-12-product-quality-measurement-rubric.md` -- adapted ISO/IEC 25010:2023 into a five-level, evidence-tiered rubric for internal platforms; 12 Key Findings, confidence medium.
- `learnings.md` -- added Thread 31 (standards supply measures, not thresholds).

**Findings summary:** ISO/IEC 25010:2023 has nine characteristics (adds Safety, renames Usability and Portability), while ISO/IEC 25023:2016 measures the eight 2011-era ones and assigns no value ranges to levels. The recommended rubric scores the eight under 2023 names, treats Safety as conditional, and sets levels by evidence tier with locally agreed thresholds.

**Review:** pass 1 failed (mislabelled `[fact]` clauses merging derived consequences, unsupported DORA attribution); fixed. Pass 2 hit the review cap and auto-passed; residual access-note labels, HTTP/W3C expansions fixed afterwards.

**Sources:** arc42 ISO 25010 update, ISO 25000 portal, ISO/IEC 25023:2016 preview, DORA, NIST SP 800-53/800-218, CIS Controls, WCAG 2.2, CMMI, Google SRE error budget policy.

## Mini-Retro

1. **Did the process work?** Yes; research, draft and two review passes completed in one session.
2. **What slowed down or went wrong?** iso.org returned 403 and 25023 formulas are paywalled; review flagged `[fact]` clauses that merged derived consequences and an unsupported DORA attribution.
3. **What single change would prevent this next time?** Split every "X, so Y" Key Finding into a `[fact]` sentence and a separate `[inference]` sentence at drafting time.
4. **Is this a pattern?** Yes; already recorded in Known Recurring Failure Patterns (collapsed fact and inference clauses).
5. **Does any documentation need updating?** learnings.md updated; no other docs.
6. **Do the default instructions need updating?** No; also check that "Access note" bullets and HTTP/W3C-style acronyms get labels and expansions before the first review.
