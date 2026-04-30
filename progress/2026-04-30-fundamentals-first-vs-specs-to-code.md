# 2026-04-30 -- Research Loop (fundamentals-first-vs-specs-to-code)

**Completed:**

Research item:
- `Research/completed/2026-04-30-fundamentals-first-vs-specs-to-code.md` -- completed; the item concludes that prompt-only AI coding wins mainly on immediate prototype speed, while fundamentals-first controls pay back once code must survive review, debugging, and repeated change. The strongest supported controls are executable verification, explicit contracts or type signals, and architecture or context constraints, while the Matt Pocock stack is best supported at the component level rather than by a direct bundle-level ROI study.

Sources consulted:
- https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ (randomized controlled trial on local code quality with GitHub Copilot)
- https://www.gitclear.com/ai_assistant_code_quality_2025_research (repository-scale maintainability and duplication trends)
- https://doi.org/10.1145/3491101.3519665 (user-study evidence on review burden and debugging difficulty)

## Mini-Retro

1. **Did the process work?** Yes. The research-loop workflow, review pass, and auto-pass fallback all worked as designed.
2. **What slowed down or went wrong?** The main slowdown was review-driven wording correction: several claims were initially phrased more strongly than the evidence justified, especially around ranked ROI and cross-stack transferability.
3. **What single change would prevent this next time?** Nothing new beyond following the existing rule to prefer "plausible" or "supported" over ranked superlatives unless the source directly compares alternatives.
4. **Is this a pattern?** Yes. It matches the existing review pattern where citation discipline fails when a synthesis claim outruns the direct evidence, especially for bundle-level or comparative claims.
