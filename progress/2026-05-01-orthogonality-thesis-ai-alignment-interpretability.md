# 2026-05-01 -- Research Loop (orthogonality-thesis-ai-alignment-interpretability)

**Completed:**

Research item:
- `Research/completed/2026-04-30-orthogonality-thesis-ai-alignment-interpretability.md` -- completed; the item concludes that the orthogonality thesis still works as an in-principle warning that capability does not determine goals, while current interpretability and alignment evidence only partially constrains behavior rather than recovering stable model-wide objectives. It translates that result into an audit position: explainability should support claims about behavior, mechanisms, controls, and validation limits, not anthropomorphic motive attribution.

Sources consulted:
- https://nickbostrom.com/superintelligentwill.pdf (orthogonality and instrumental-convergence thesis)
- https://arxiv.org/abs/2307.09458 (frontier-model interpretability scaling limits)
- https://www.anthropic.com/research/tracing-thoughts-language-model (partial circuit tracing and fake-reasoning evidence)

## Mini-Retro

1. **Did the process work?** Yes. The draft-review-fix loop surfaced one real citation-scope bug and the final synthesis held up after tightening it.
2. **What slowed down or went wrong?** The review workflow was stricter than the first self-review about mixed-clause Executive Summary sentences, so one sentence cited the thesis sources correctly but under-cited the frontier-model interpretability clause.
3. **What single change would prevent this next time?** Add an explicit self-review check for Executive Summary sentences that combine philosophical and empirical claims, and require each clause to have direct source support.
4. **Is this a pattern?** Yes, it is a narrower version of the recurring unsupported-synthesis problem: one sentence made two different claims, but only one source family clearly covered both.

## Applied improvements

- Added a new Step 6 self-review rule to `research-prompt.md` requiring clause-by-clause source coverage for mixed theoretical and frontier-empirical Executive Summary sentences.
