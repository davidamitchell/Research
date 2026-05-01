# 2026-05-01 -- Research Loop (compound-error-accumulation-ai-codebases)

**Completed:**

Research item:
- `Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md` -- completed; the item concludes that compounding risk in AI-heavy codebases is mainly a verification-capacity problem, not a blanket indictment of AI-generated code. Bounded tasks with strong executable checks can work well, but long-context, high-coupling changes need layered controls, stronger independent tests, and expert human review because local fixes otherwise accumulate as repository-scale warning load, duplication, and review debt.

Sources consulted:
- https://arxiv.org/abs/2310.06770 (SWE-bench benchmark design and long-context repository difficulty)
- https://arxiv.org/html/2604.01527v1 (ProdCodeBench evidence on production-derived tasks and validation-tool use)
- https://arxiv.org/html/2511.04427v2 (longitudinal evidence linking AI-assisted coding to warning and complexity growth)

## Mini-Retro

1. **Did the process work?** Yes, the research-loop flow worked, and the review workflow surfaced several real calibration issues that were worth fixing.
2. **What slowed down or went wrong?** Review failures clustered around citation discipline for session-local access notes and around over-strong synthesis wording that should have been inferential or lower confidence.
3. **What single change would prevent this next time?** Add an explicit prompt rule that session-local access failures must not appear in Findings as sourced facts; they should be omitted or rewritten as evidence-scope gaps.
4. **Is this a pattern?** Yes, it matches the repository's recurring citation-discipline and synthesis-calibration friction, even though this specific DOI-backed access-note variant was not spelled out clearly enough.

## Applied improvements

- Updated `research-prompt.md` to forbid carrying session-local access failures into Findings as sourced factual claims when the only citation is a DOI or landing page.
