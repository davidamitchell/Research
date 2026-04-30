# 2026-04-30 -- Research Loop (strategic-tactical-division-ai-teams)

**Completed:**

Research item:
- `Research/completed/2026-04-30-strategic-tactical-division-ai-teams.md` -- completed; the item concludes that current evidence favors a human-strategic and AI-tactical division of labor, with humans concentrating on architecture, clarification, interfaces, and verification while AI handles bounded implementation. It also finds that Kent Beck's design-investment argument remains directionally strong in AI-heavy workflows and that downstream review and maintenance costs now matter more than raw code-generation cost.

Sources consulted:
- https://www.anthropic.com/engineering/claude-code-best-practices (workflow guidance on context, planning, and verification)
- https://arxiv.org/abs/2310.10996 (ClarifyGPT evidence for clarification before code generation)
- https://www.gitclear.com/ai_assistant_code_quality_2025_research (longitudinal evidence on duplication and reduced refactoring in AI-assisted code)

## Mini-Retro

1. **Did the process work?** Yes, the research loop worked end to end, and the review workflow surfaced concrete evidence-discipline issues that improved the final item.
2. **What slowed down or went wrong?** The first review pass exposed several subtle wording and source-scope problems, and the second pass still caught a few domain-term and phrasing issues that were easy to miss during manual self-review.
3. **What single change would prevent this next time?** Nothing beyond the current prompt checks; the final misses were already covered by the existing checklist and just needed stricter manual execution.
4. **Is this a pattern?** No new pattern beyond the repository's known recurring review failures around acronym expansion, domain-term definition, and over-broad claims.
