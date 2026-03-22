# 2026-03-22 — Research Loop (coding-ai-agent-skills-survey)

**Completed:**

Research item:
- `Research/completed/2026-03-22-coding-ai-agent-skills-survey.md` — completed; the survey found that the strongest public adoption path is to standardize on portable agent-guidance formats such as `AGENTS.md` and `SKILL.md`, then selectively import curated assets from `awesome-copilot` and strong community catalogs for repetitive, framework-bound domains. It also found that public prompt coverage is strong for .NET, Python backend, API design, testing, security, and database work, but still thin for architecture-heavy domains such as DDD, CQRS, Kafka ECST, and data architecture.

Sources consulted:
- https://github.com/github/awesome-copilot (`awesome-copilot` catalog and install surface)
- https://raw.githubusercontent.com/anthropics/skills/main/README.md (Anthropic skills packaging model)
- https://agents.md/ (`AGENTS.md` portability convention)

## Mini-Retro

1. **Did the process work?** Yes. The queue-selection, draft, review, redraft, and completion loop all worked end-to-end, and the review workflow correctly forced tighter citation discipline.
2. **What slowed down or went wrong?** The first review pass exposed uncited synthesis sections and too much copy-forward from `§6` into `## Findings`, which required a substantial rewrite. The review workflow itself also takes a few minutes in the `Run quality review` step, so polling needed patience.
3. **What single change would prevent this next time?** Treat every claim-bearing sentence in `§3`–`§7`, `Assumptions`, and `Risks` as requiring inline sources from the start, and rewrite `## Findings` from scratch instead of copying `§6` forward too literally.
4. **Is this a pattern?** Yes. It matches the repository's known recurring pattern that research review is extremely strict about claim labels, URL-level citations, and near-verbatim duplication between `Research Skill Output` and `Findings`.
