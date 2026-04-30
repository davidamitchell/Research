# 2026-04-30 -- Research Loop (ai-code-entropy-quality-metrics)

**Completed:**

Research item:
- `Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md` -- completed; the item concludes that repeated Artificial Intelligence (AI) code generation is more likely than not to raise repository-scale entropy when architectural guardrails are weak, even if bounded task-level quality often improves. The strongest warning signals are rising clone share, short-term churn, refactoring decline, hotspot code-health deterioration, and hidden change coupling, which together operationalise the verification bottleneck at repository scale.

Sources consulted:
- https://www.gitclear.com/ai_assistant_code_quality_2025_research (repository-scale trends in cloning, churn, and refactoring)
- https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ (randomized evidence on bounded task-level quality)
- https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign (deep modules and information hiding as the guardrail model)

## Mini-Retro

1. **Did the process work?** Yes, the draft-review loop surfaced the remaining confidence, cross-reference, and acronym issues before completion.
2. **What slowed down or went wrong?** The missing `.github/skills/` submodule content and a few inaccessible seeded sources forced the process to rely on the prompt and source substitution notes rather than the intended local skill files.
3. **What single change would prevent this next time?** Nothing beyond the existing fallback rule, because the current instructions already cover how to proceed when the skills submodule is absent.
4. **Is this a pattern?** Yes, missing skill content is a recurring workflow-environment pattern rather than an item-specific problem, but it already matches an existing instruction and does not need a new rule.
