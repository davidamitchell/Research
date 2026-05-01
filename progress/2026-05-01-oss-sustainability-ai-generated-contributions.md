# 2026-05-01 -- Research Loop (oss-sustainability-ai-generated-contributions)

**Completed:**

Research item:
- `Research/completed/2026-05-01-oss-sustainability-ai-generated-contributions.md` -- completed; the item concludes that low-quality Artificial Intelligence (AI)-generated open-source software (OSS) contribution pressure is primarily a maintainer review-capacity problem, not only a content-quality problem. The strongest supported response is a layered intake model: structured templates, disclosure and understanding requirements, trust gates such as Vouch, and hard throttles only when overload is already acute. It also ties this governance response to fragile maintainer capacity data, showing that the scarce resource is maintainer attention across the whole contribution funnel.

Sources consulted:
- https://arxiv.org/html/2603.26487v1 (open-source software governance corpus on Generative Artificial Intelligence (GenAI) policies)
- https://github.com/mitchellh/vouch (trust-gate implementation and workflow)
- https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en (maintainer-capacity baseline)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, review workflow, and second-pass auto-approval behaved as intended.
2. **What slowed down or went wrong?** The first two review passes surfaced the same core issue: I drafted a few synthesis claims as facts when they were better labeled as inferences, and one summary sentence generalized beyond the cited project examples.
3. **What single change would prevent this next time?** Nothing new needs to be added to the repo process; the existing checklist already warns about exactly this failure mode, and I need to apply it earlier.
4. **Is this a pattern?** Yes. It matches the existing pattern that synthesis claims and confidence levels can overreach the direct evidence if fact-versus-inference labeling is not tightened before the first draft commit.
