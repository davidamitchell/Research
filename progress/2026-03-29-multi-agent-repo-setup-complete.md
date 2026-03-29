# 2026-03-29 -- Research Loop (multi-agent-repo-setup)

**Completed:**

Research item:
- `Research/completed/2026-03-29-multi-agent-repo-setup.md` -- completed; the minimum viable configuration for all currently-reachable agent surfaces requires three additions: `copilot-setup-steps.yml` (environment setup), `AGENTS.md` (cross-vendor pointer), and `CLAUDE.md` (Claude Code instructions). The Claude-via-GitHub-Issues surface is blocked by missing credentials. Copilot Spaces and the Claude iOS GitHub integration are reading tools that load no instruction files automatically and require no per-repo configuration changes.

Sources consulted:
- https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot (Copilot custom instructions: which surfaces load the file and additive AGENTS.md behaviour)
- https://docs.github.com/en/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent (copilot-setup-steps.yml schema and when it runs)
- https://docs.anthropic.com/en/docs/claude-code/github-actions (Claude Code GitHub Actions: required credentials and CLAUDE.md loading)

## Mini-Retro

1. **Did the process work?** Yes. The item was already at review_count 2 so it auto-passed; the complete step ran cleanly and the file moved to completed/.
2. **What slowed down or went wrong?** Nothing significant. The item was fully researched and reviewed in a prior session; this session only needed to complete and log.
3. **What single change would prevent this next time?** Nothing to change; the handoff from prior session was clean.
4. **Is this a pattern?** No new pattern identified. Auto-pass on review_count 2 worked as designed.
