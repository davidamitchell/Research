# 2026-04-29 -- Research Loop (software-demand-shift-ai-coding-era)

**Completed:**

Research item:
- `Research/completed/2026-04-28-software-demand-shift-ai-coding-era.md` -- completed; the item concludes that AI-assisted coding is most likely to compress demand for narrow logic-heavy application software whose premium was mostly implementation effort. It also finds that demand shifts toward coordination-bearing layers such as platform engineering, identity, deployment, observability, and agent-facing interfaces, while incumbents can preserve value by moving up into orchestration, proprietary context, and bundled control surfaces.

Sources consulted:
- https://retool.com/blog/ai-build-vs-buy-report-2026 (category-level evidence on which software classes buyers are replacing first)
- https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report (evidence that platform engineering demand rises as software volume and delivery complexity increase)
- https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/ (case evidence on selective rebuilds and the limits of generalising from Klarna)

## Mini-Retro

1. **Did the process work?** Yes, the research loop, review workflow, and final completion flow worked end to end.
2. **What slowed down or went wrong?** The review workflow auto-passed on the second run even though it still surfaced one substantive phrasing issue, so I had to treat the log as authoritative instead of the pass outcome alone.
3. **What single change would prevent this next time?** Nothing in-repo needs changing right now; the current prompt already says to inspect `OVERALL:` and individual violations rather than trusting the workflow conclusion.
4. **Is this a pattern?** Yes, it matches the existing known pattern that the review workflow conclusion can say success while the quality log still contains `OVERALL: FAIL`.
