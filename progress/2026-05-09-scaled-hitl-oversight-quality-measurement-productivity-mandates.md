# 2026-05-09 -- Research Loop (scaled-hitl-oversight-quality-measurement-productivity-mandates)

**Completed:**

Research item:
- `Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md` -- completed; the item concludes that scaled human oversight works best as a hybrid tiered model that keeps synchronous approval for the highest-consequence actions and uses exception review, sampling, and periodic audit for lower-risk work. It also argues that productivity mandates without explicit quality Key Performance Indicators (KPIs) turn per-item review into another transaction-cost queue, so organisations need dual productivity-plus-quality metrics, real reviewer authority, and no-blame challenge culture to keep oversight meaningful.

Sources consulted:
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 (official human-oversight requirements and override or stop capabilities)
- https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/ (official guidance on sampling, override logs, caseload, independence, and fallback)
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full (experimental evidence on verification intensity, error briefings, and review quality)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, local self-review, and one external review pass were enough to converge on a clean item.
2. **What slowed down or went wrong?** The first review pass flagged domain-term first-use issues for "verification intensity" and "automation bias", plus an overconfident synthesis claim about dual KPIs.
3. **What single change would prevent this next time?** Add "verification intensity" to the domain-term clarity examples in `research-prompt.md` so first-use audits catch it before the first draft review.
4. **Is this a pattern?** Yes. It is the same broader first-use terminology failure class that sits next to the repository's recurring acronym-expansion failures, so tightening the prompt examples is the right root fix here.

## Applied improvements

- Updated `research-prompt.md` to add "verification intensity" to the domain-term clarity checklist examples.
