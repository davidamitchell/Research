# 2026-05-02 -- Add backlog item (meta-analysis-standards-and-ai-skill-evaluation)

**Completed:**
- `Research/backlog/2026-05-02-meta-analysis-standards-and-ai-skill-evaluation.md` — added from issue "A meta analysis skill"; the validated question asks what established standards and best practices govern meta-analysis (MA) and systematic review, and how do existing AI research skills in this repository measure up against them

## Mini-Retro

1. **Did the process work?** Yes. The issue description was multi-part but internally coherent — it asked simultaneously about professional MA standards, study selection, synthesis best practices, evaluation frameworks, and existing skill quality. The research-question skill's five-test check (Specific, Answerable, Scoped, Motivated, Decomposable) applied cleanly: the question is specific (professional standards vs. existing AI skills), answerable (PRISMA/Cochrane/etc. are documented; skills are inspectable), scoped (non-clinical, non-statistical MA methods plus this repo's skills), motivated (active research loop benefits from higher synthesis quality), and decomposable (7 concrete sub-questions).
2. **What slowed down or went wrong?** The skills submodule (`.github/skills/`) was not initialised in the sandbox, so I could not directly inspect current skill content. The approach section flags this as a conditional step ("if the submodule is initialised") and falls back to inspecting `research-prompt.md` and `research-review-prompt.md` as proxy sources.
3. **What single change would prevent this next time?** No change needed for backlog item creation itself. The uninitialised submodule is a known environment limitation documented in the instructions.
4. **Is this a pattern?** No new pattern. The uninitialised submodule limitation is already noted in the instructions under "Session-start MCP availability check".
