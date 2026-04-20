# 2026-04-20 -- Research Loop (harness-selection-tools-agents-skills-prompts-instructions)

**Completed:**

Research item:
- `Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md` -- completed; the item concludes that teams should separate durable policy, reusable workflows, manual task launchers, and specialist workers into different artifact classes instead of overloading one Markdown file. It also finds that `AGENTS.md` is the strongest portable repository core, but real cross-harness use still needs native shims such as `CLAUDE.md` where vendors do not load the same entrypoint directly.

Sources consulted:
- https://docs.github.com/en/copilot/reference/custom-instructions-support (GitHub Copilot instruction-surface matrix)
- https://docs.anthropic.com/en/docs/claude-code/memory (Claude Code always-on instruction behavior)
- https://developers.openai.com/codex/guides/agents-md (Codex `AGENTS.md` guidance and discovery order)

## Mini-Retro

1. **Did the process work?** Yes. The research-and-review loop produced a solid item, and the second review cycle surfaced only citation-discipline cleanup rather than missing research coverage.
2. **What slowed down or went wrong?** Internal references were initially cited as repo-relative paths or self-referential labels, and a few cross-vendor conclusions were phrased more comparatively than the cited evidence justified.
3. **What single change would prevent this next time?** Require URL-backed links whenever prior completed items are cited inside the research output, not just in the Sources section.
4. **Is this a pattern?** Yes. It is another citation-discipline pattern: internal or prior-work references feel "obvious" during drafting but still fail review unless they are bound to verifiable URLs.

## Applied improvements

- Updated `research-prompt.md` so the prior-work check now explicitly requires URL-backed links when prior completed items are cited in §0, Findings, or the Evidence Map.

## Pending skill improvements

- Add the same URL-backed prior-work citation rule to `.github/skills/research/SKILL.md` §0 or §8 so the skill and the fallback prompt enforce the same citation discipline.
