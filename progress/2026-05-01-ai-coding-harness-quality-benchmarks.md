# 2026-05-01 -- Research Loop (ai-coding-harness-quality-benchmarks)

**Completed:**

Research item:
- `Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md` -- completed; the item concludes that Software Engineering Benchmark (SWE-bench) Verified is the strongest public anchor for comparing coding harnesses because it measures end-to-end issue resolution rather than isolated code snippets. It also finds that public leaderboard leaders are mostly benchmark-native or open harnesses, while major branded assistants such as GitHub Copilot and Cursor currently publish controlled-study or internal-eval evidence instead of first-party shared leaderboard scores.

Sources consulted:
- https://www.swebench.com/verified.html (benchmark definition and evaluation regime for end-to-end software engineering tasks)
- https://www.swebench.com/ (public leaderboard data used for named score comparisons)
- https://cursor.com/blog/cursorbench (internal-eval methodology and benchmark-credibility critique from a major branded assistant vendor)

## Mini-Retro

1. **Did the process work?** Yes, after the first review loop exposed exactly where evaluative language had slipped past the fact-versus-inference boundary.
2. **What slowed down or went wrong?** The main slowdown was repeated review feedback on wording precision in Findings, especially where comparative judgments were implicitly stronger than the underlying sources.
3. **What single change would prevent this next time?** Add an explicit pre-review pass that rewrites every benchmark-ranking or evidence-quality comparison into `[inference]` unless a cited source makes the same comparison directly.
4. **Is this a pattern?** Yes, it matches the known recurring pattern of surface evaluation and of research reviews failing when comparative synthesis is stated as fact instead of clearly marked inference.

## Applied improvements

- Tightened the item's Executive Summary, Key Findings, and mirrored `§6 Synthesis` so comparative benchmark judgments are labeled as inferences and confidence levels match the evidence actually cited.
- Updated `research-prompt.md` so benchmark-ranking and evidence-quality comparisons now default to `[inference]` unless a cited source explicitly makes the same comparison.
