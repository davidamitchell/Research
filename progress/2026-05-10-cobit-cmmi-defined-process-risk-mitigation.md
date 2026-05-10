# 2026-05-10 -- Research Loop (cobit-cmmi-defined-process-risk-mitigation)

**Completed:**

Research item:
- `Research/completed/2026-05-09-cobit-cmmi-defined-process-risk-mitigation.md` -- completed; COBIT 2019 and CMMI both place durable workforce-risk mitigation above project-local fixes and at the point where the process is standardized, owned, evidenced, and fed back into shared organizational assets. The item turns that threshold into a practical checklist for deciding whether a mitigation is merely repeatable or actually sustainable.

Sources consulted:
- https://www.isaca.org/resources/news-and-trends/industry-news/2019/defining-target-capability-levels-in-cobit-2019-a-proposal-for-refinement (COBIT capability-level threshold descriptions)
- https://www.isaca.org/resources/news-and-trends/industry-news/2019/using-cobit-2019-performance-management-model-to-assess-governance-and-management-objectives (COBIT evidence and assessment requirements)
- https://cmmiinstitute.com/learning/appraisals/levels (official CMMI capability and maturity level definitions)

## Mini-Retro

1. **Did the process work?** Mostly; the review loop caught framework-term clarity and confidence-overreach issues that were easier to fix than to predict from the prompt alone.
2. **What slowed down or went wrong?** Small prose choices in `§7` metadata and Findings Analysis triggered a second-pass review even though the core evidence and synthesis were already in place.
3. **What single change would prevent this next time?** Add an explicit self-review rule that `§7` lines must be pure metadata fragments or labeled claims, and ban unsupported `not X but Y` contrast framing in Findings Analysis.
4. **Is this a pattern?** Not yet as a standalone recurring pattern, but it is clearly the same class of avoidable research-review failure caused by small synthesis-wording choices.

## Applied improvements

- Updated `research-prompt.md` to require pure-metadata or labeled claims in `§7 Recursive Review` and to ban unsupported binary-contrast phrasing in Findings Analysis.

## Pending skill improvements

- Mirror the new `§7` metadata and binary-contrast checks into `.github/skills/research/SKILL.md` or the companion output-finalisation guidance in the Skills source repository, because the local prompt now enforces checks that the read-only skill files do not yet spell out.
