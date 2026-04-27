# 2026-04-27 -- Research Loop (llm-verifiability-asymmetry-code-world-action)

**Completed:**

Research item:
- `Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md` -- completed; the item concludes that Large Language Model (LLM)-assisted software engineering is the highest-confidence common deployment domain only when outputs pass external verifier gates such as compilers, type checkers, tests, analyzers, or proofs. It also concludes that consequential world actions remain structurally lower-confidence because correctness usually cannot be reduced to a domain-complete pre-consequence verifier, so governance and human control have to replace mechanical acceptance.

Sources consulted:
- https://arxiv.org/abs/2107.03374 (HumanEval benchmark paper)
- https://www.microsoft.com/en-us/research/project/dafny-a-language-and-program-verifier-for-functional-correctness/ (official Dafny verifier overview)
- https://www.bankofengland.co.uk/prudential-regulation/publication/2022/october/artificial-intelligence (Bank of England discussion paper on Artificial Intelligence governance)

## Mini-Retro

1. **Did the process work?** Yes, the research-loop workflow worked end to end, and the second review cycle plus final manual tightening produced a stronger completed item.
2. **What slowed down or went wrong?** The first two review passes exposed wording that slightly overclaimed beyond the cited evidence, and the review workflow updated `review_count` on `main`, which required a pull while local `learnings.md` edits were in progress.
3. **What single change would prevent this next time?** Nothing new; the existing self-review checklist already covers this class of issue, and I just needed to apply it more strictly to comparative and deployment-boundary claims.
4. **Is this a pattern?** No new pattern beyond the existing instruction-set warning that synthesis claims can outrun the cited evidence if comparative language is not narrowed carefully.
