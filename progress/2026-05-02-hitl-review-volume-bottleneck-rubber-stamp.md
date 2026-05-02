# 2026-05-02 -- Research Loop (hitl-review-volume-bottleneck-rubber-stamp)

**Completed:**

Research item:
- `Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md` -- completed; the item concludes that high-volume per-action human review becomes a weak control because overload drives bottlenecks and nominal sign-off. It recommends narrowing pre-execution review to consequential actions and shifting lower-risk bounded work toward exception review, sampling, monitoring, and fallback paths, while keeping real human authority, logs, and stop rights.

Sources consulted:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ (systematic review of automation bias drivers and mitigators)
- https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/ (official guidance on meaningful human review, caseload, sampling, and overrides)
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 (official human-oversight requirements for high-risk Artificial Intelligence systems)

## Mini-Retro

1. **Did the process work?** Mostly yes. The review loop surfaced real issues that the manual pass missed, especially domain-term clarity and sentence-level labeling inside Findings Analysis.
2. **What slowed down or went wrong?** The review workflow's second-pass auto-pass path still required manual log inspection, and non-acronym domain terms such as "automation bias", "alert fatigue", and "approval-by-exception" were easier to miss than acronym expansions.
3. **What single change would prevent this next time?** Add a self-review checkpoint that scans Scope, Context, Executive Summary, and Findings for first-use domain terms, not just acronyms, and require one sentence that compares the preferred control model against plausible rival remedies.
4. **Is this a pattern?** Yes. It matches the recurring citation-discipline and first-use-clarity failure class, and it also suggests a companion-skill improvement for non-acronym domain terms and rival-remedy checks.

## Applied improvements

- Updated `research-prompt.md` to require first-use definition checks for non-acronym domain terms across the full item and to require a competing-remedy check when recommending a preferred governance or control model.

## Pending skill improvements

- `research` skill: add explicit first-use checks for non-acronym domain terms such as automation bias, alert fatigue, and approval-by-exception.
- `remove-ai-slop` or companion review skill: add a check that preferred-model recommendations engage plausible rival remedies instead of presenting one control shape as self-evidently superior.
