# 2026-04-19 -- Research Loop (ai-company-hiring-strategies)

**Completed:**

Research item:
- `Research/completed/2026-04-02-ai-company-hiring-strategies.md` - completed; the strongest public hiring signal across major AI labs is a shift from pure frontier-research staffing toward deployment, product surfaces, governance, and compute operations. Mistral showed the clearest historical visible-board expansion, xAI remained infrastructure-heavy, and Meta's strongest public signal came from executive concentration rather than an open job board.

Sources consulted:
- https://boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true (current Anthropic role mix)
- https://api.lever.co/v0/postings/mistral?mode=json (current Mistral role mix)
- https://web.archive.org/web/20240404003442/https://jobs.lever.co/mistral (historical Mistral snapshot)
- https://developers.openai.com/blog/openai-for-developers-2025 (official OpenAI developer strategy)

## Mini-Retro

1. **Did the process work?** Mostly yes. The item reached a defensible conclusion, and the review loop improved the precision of the Findings.
2. **What slowed down or went wrong?** Public hiring sources were uneven: several official or aggregator job pages were blocked or login-gated, and the first review pass showed that Findings needed stricter inline claim labeling than the initial draft used.
3. **What single change would prevent this next time?** State explicitly in the prompt that Findings and Analysis need inline `[fact]` or `[inference]` labels and inline source binding, not just a later Evidence Map.
4. **Is this a pattern?** Yes. This matches a broader review pattern where sourced investigation sections pass, but summarised Findings prose is still treated as unsupported unless the labels and sources are repeated inline.

## Applied improvements

- Updated `research-prompt.md` to require inline epistemic labels and inline source binding in `## Findings`, especially Executive Summary, Key Findings, and Analysis.

## Pending skill improvements

- Mirror the new `research-prompt.md` rule into `.github/skills/research/SKILL.md`: Findings and Analysis need inline `[fact]`, `[inference]`, or `[assumption]` labels plus source binding at the point of claim; the Evidence Map alone is not enough.
