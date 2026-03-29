# 2026-03-29 -- Research Loop (agent-instruction-loading-and-skills-access)

**Completed:**

Research item:
- `Research/completed/2026-03-28-agent-instruction-loading-and-skills-access.md` — completed; the Copilot coding agent reads `.github/copilot-instructions.md` automatically and this repo's setup is correct, but the `.github/skills/` git submodule is silently absent from the agent's context because the ephemeral Actions environment does not materialise submodules. The Claude iOS GitHub connector loads no instruction files automatically; adding a root `CLAUDE.md` and adding `.github/copilot-instructions.md` to the Claude Project knowledge base would close both identified gaps.

Sources consulted:
- https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot (GitHub Docs: custom instructions; confirms AGENTS.md and copilot-instructions.md are additive)
- https://github.com/orgs/community/discussions/180953 (Community Discussion: Copilot coding agent cannot access git submodules, December 2025 reports)
- https://support.claude.com/en/articles/10167454-using-the-github-integration (Anthropic Help: Claude GitHub integration connector, manual file selection, no auto-loading)
- https://code.claude.com/docs/en/memory (Claude Code Docs: CLAUDE.md loading by directory-tree walk)
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (GitHub Changelog: AGENTS.md support added August 2025)

## Mini-Retro

1. **Did the process work?** Yes, the research loop produced a complete, well-sourced item with four distinct investigation threads. Evidence gathering via Tavily was effective for both official docs and community reports.

2. **What slowed down or went wrong?** Em-dash removal required a Python scripting pass that took multiple iterations to resolve all 76 instances. Two review cycles were needed; the first review caught 5 violations (VS Code expansion, evaluative terms, a [fact]/[inference] mislabel, an unsourced statistic, and an overconfident claim). The second review caught 7 more (missing labels in §5, an unsourced claim in the Analysis section, and an ADR URL missing from the Evidence Map). Both sets were fixable and reflected known patterns.

3. **What single change would prevent this next time?** Run the evaluative-terms scan and vague-quantifier check as a dedicated inline step before the first draft commit rather than relying on the review workflow to catch them. Specifically: search for "most", "clearly", "adequate", "widely", "all major" and label or remove each before committing.

4. **Is this a pattern?** Yes. Evaluative terms without epistemic labels and vague quantifiers without sources are the recurring violation class. This matches the pattern in the instructions. The ADR without a URL is a new variant: internal repo paths without GitHub URLs fail the sources-must-have-URLs rule when the Evidence Map is read by an external reviewer. Fix: always use the full GitHub URL for ADR references.
