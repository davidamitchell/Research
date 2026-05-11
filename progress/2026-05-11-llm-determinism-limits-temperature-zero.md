# 2026-05-11 -- Research Loop (llm-determinism-limits-temperature-zero)

**Completed:**

Research item:
- `Research/completed/2026-05-09-llm-determinism-limits-temperature-zero.md` -- completed; the item concludes that temperature zero, fixed seeds, and constrained outputs improve stability but do not create hard determinism for current Large Language Model systems. The core limit sits in the wider inference stack, so governance-grade decisions still need deterministic external enforcement, versioned policy logic, or explicit human approval.

Sources consulted:
- https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter (OpenAI reproducibility guidance and `system_fingerprint` behavior)
- https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reproducible-output (Microsoft best-effort determinism guidance and residual variance caveats)
- https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ (Serving-path explanation for temperature-zero nondeterminism)

## Mini-Retro

1. **Did the process work?** Yes; one substantive review loop surfaced wording and terminology issues, and the second pass was enough to move the item forward cleanly.
2. **What slowed down or went wrong?** The quality review was stricter than the first self-review on review-metadata phrasing and on non-self-evident technical terms such as greedy decoding and prefix caching.
3. **What single change would prevent this next time?** Nothing new is needed beyond applying the existing domain-term clarity check earlier and more aggressively.
4. **Is this a pattern?** Yes; it matches the existing instruction-level pattern that acronym expansion and domain-term clarity are frequent review failure sources, so no new repo-wide rule is needed.
