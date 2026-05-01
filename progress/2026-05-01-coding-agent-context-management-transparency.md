# 2026-05-01 -- Research Loop (coding-agent-context-management-transparency)

**Completed:**

Research item:
- `Research/completed/2026-05-01-coding-agent-context-management-transparency.md` -- completed; the item concludes that coding-agent harnesses need explicit, user-visible mutation boundaries for prompts, tools, retrieval, and compaction rather than opaque context automation. It also finds that trust should be treated as a calibration problem, so the best current operating model is explicit automation with inspectable summaries, stable control surfaces, and bounded user overrides.

Sources consulted:
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Anthropic guidance on context engineering patterns and trade-offs)
- https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json (public transcript archive for Mario Zechner's talk about Claude Code and Pi)
- https://doi.org/10.1371/journal.pone.0229132 (trust calibration evidence used to frame transparency as a calibration problem)

## Mini-Retro

1. **Did the process work?** Yes. The research-loop structure plus the repository's review workflow forced the epistemic labels, source quality, and mirrored Findings sections into a much cleaner final state.
2. **What slowed down or went wrong?** The main slowdown was that the review workflow can report success at the run level while still surfacing substantive `VIOLATION:` lines in the logs, so the first apparent pass was not actually clean.
3. **What single change would prevent this next time?** Nothing new beyond the existing practice of checking the final workflow log for `VIOLATION:` lines before treating a review run as truly complete.
4. **Is this a pattern?** Yes, but it matches an already-documented pattern in the repository instructions about review workflows and log inspection, so no new instruction update is needed.
