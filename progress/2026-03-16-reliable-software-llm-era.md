# 2026-03-16 — Research Loop (reliable-software-llm-era)

**Completed:**

Research item:
- `Research/completed/2026-03-14-reliable-software-llm-era.md` — completed; The Quint formal specification ecosystem proposes a four-step LLM workflow (spec change → interactive spec validation → code generation → model-based testing) that assigns translation tasks to LLMs and reasoning to deterministic tools, applied to a production BFT consensus engine change at a self-reported ~1-week vs. months-estimate speedup. The companion "cognitive debt" concept names the trust/understanding deficit created when LLM code generation bypasses understand-while-coding. Spectacle (a Haskell-embedded equivalent) demonstrates via near-zero adoption why accessibility is as important as formal correctness.

Sources consulted:
- https://quint-lang.org/posts/llm_era (primary article: Reliable Software in the LLM Era, Nov 2025)
- https://quint-lang.org/posts/cognitive_debt (cognitive debt companion post, March 2026)
- https://github.com/informalsystems/quint-llm-kit (quint-llm-kit repository)
- https://hackage.haskell.org/package/spectacle (Spectacle Haskell package)
- https://news.ycombinator.com/item?id=47347901 (HN thread, 108 upvotes, 35 comments)

## Mini-Retro

1. **Did the process work?** Yes. All five sources were accessible and yielded substantive content. The four-step structured approach (fetch sources → compose §§0–7 → audit acronyms → draft → review) produced a review-pass on the first submission.

2. **What slowed down or went wrong?** TLA+ was used without expansion in the Scope section before being expanded in §2 — caught during the pre-draft acronym audit. CI, GHC, ROI, CRUD, and UI also required post-composition fixes. These are the recurring acronym-expansion failures.

3. **What single change would prevent this next time?** Write acronym expansions at first-draft time in the Scope/Context sections rather than patching after composition. The Scope section introduces many abbreviations before §2 Investigation — seed expansions there proactively.

4. **Is this a pattern?** Yes — this matches the known recurring pattern. Acronym failures in Scope/Context before §2 are consistent with every prior session note. The fix is well-understood; the discipline of applying it at first-draft time has not yet been internalised.
