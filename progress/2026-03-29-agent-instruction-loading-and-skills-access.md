# 2026-03-29 -- Research Loop (agent-instruction-loading-and-skills-access)

**Completed:**

Research item:
- `Research/completed/2026-03-28-agent-instruction-loading-and-skills-access.md` -- completed; The Copilot coding agent loads `.github/copilot-instructions.md` automatically and has supported `AGENTS.md` since August 2025; Claude Code (used by the Claude iOS `code` feature) reads `CLAUDE.md` and `AGENTS.md` but not `.github/copilot-instructions.md`, meaning the current repo leaves Claude Code with zero project instructions. The fix is to restore `AGENTS.md` at the repo root and to add `copilot-setup-steps.yml` for submodule access.

Sources consulted:
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (GitHub changelog confirming coding agent AGENTS.md support since August 2025)
- https://support.claude.com/en/articles/12618689-claude-code-on-the-web (Anthropic help article confirming Claude iOS code feature is Claude Code on the web)
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Anthropic engineering blog: CLAUDE.md loaded into context up front)
- https://code.visualstudio.com/docs/copilot/customization/custom-instructions (VS Code docs confirming AGENTS.md and CLAUDE.md cross-tool recognition)
- https://github.com/orgs/community/discussions/180953 (GitHub community: Copilot coding agent submodule initialisation workaround)
- https://zenn.dev/kesin11/articles/20251210_ai_agent_symlink (Practitioner article: symlink pattern confirming Claude Code ignores .github/copilot-instructions.md)

## Mini-Retro

1. **Did the process work?** Yes -- the research question was fully answered with evidence from primary and secondary sources. The research loop structure produced a well-organised deliverable.

2. **What slowed down or went wrong?** Two review cycles were needed. First review: em-dashes (replaced with --), missing VS Code and CI expansions, scope mismatch on the dual-file-loading claim (CLI docs used to support a coding-agent claim). Second review: residual [fact] label at Q3b that should have been [inference], vague "Multiple sources" quantifier backed by one URL, OAuth unexpanded in prose, and unlabelled historical claims in §5. The second review auto-passed at review_count=2.

3. **What single change would prevent this next time?** Run a targeted grep for `[fact]` before submitting to check that every [fact] has a primary source that directly and explicitly supports the claim -- not a cross-product source or absence-of-evidence argument. Downgrade to [inference] whenever the source is secondary, cross-product, or relies on silence.

4. **Is this a pattern?** Yes -- matches the known pattern of [fact]/[inference] boundary failures seen in multiple prior reviews. The core failure is asserting [fact] when the evidence is a secondary or cross-product source. The consistent fix: if the cited source is not an authoritative primary source for the specific product making the claim, the label must be [inference].
