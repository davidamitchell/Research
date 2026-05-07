# 2026-05-07 -- Research Loop (ai-production-incidents-deep-dive)

**Completed:**

Research item:
- `Research/completed/2026-05-07-ai-production-incidents-deep-dive.md` -- completed; the item validated six well-documented incidents across consumer chatbots, generative search, hiring, housing screening, and service-wrapper privacy failures. The main conclusion is that recent production AI incidents recur across four operational classes: wrong authoritative guidance, discriminatory decision logic, infrastructure privacy defects, and accumulated control gaps where deployment outpaced validation.

Sources consulted:
- https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416 (Air Canada chatbot liability case)
- https://openai.com/index/march-20-chatgpt-outage/ (OpenAI privacy incident postmortem)
- https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit (official hiring-discrimination enforcement action)

## Mini-Retro

1. **Did the process work?** Yes. The incident databases were useful for candidate discovery, and the repository review workflow caught a few over-strong synthesis claims before completion.
2. **What slowed down or went wrong?** The main slowdown was review churn on undefined shorthand and on cross-case claims that sounded factual but were only inferential at the evidence level used here.
3. **What single change would prevent this next time?** Nothing new is needed in the prompt; the existing domain-term and inference-vs-fact checks were sufficient once applied strictly.
4. **Is this a pattern?** Yes. It matches the repository's known review pattern that shorthand and synthesis phrasing are more likely to fail than raw sourcing, so stricter self-auditing of domain terms and claim strength remains necessary.
