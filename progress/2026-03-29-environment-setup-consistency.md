# 2026-03-29 -- Research Loop (environment-setup-consistency)

**Completed:**

Research item:
- `Research/completed/2026-03-28-environment-setup-consistency.md` -- completed; `copilot-setup-steps.yml` is the correct mechanism for Copilot coding agent environment setup (supports Python install and submodule init via PAT, runs before agent starts). Claude Code on the web uses a UI-configured Bash setup script on Ubuntu 24.04, not any repository file. `devcontainer.json` serves neither primary agent surface; no single file covers both agents.

Sources consulted:
- https://docs.github.com/copilot/customizing-copilot/customizing-the-development-environment-for-copilot-coding-agent (authoritative copilot-setup-steps.yml schema and OS/runner documentation)
- https://code.claude.com/docs/en/claude-code-on-the-web (authoritative Claude Code on the web environment, setup script, and VM documentation)
- https://github.com/orgs/community/discussions/180953 (community confirmation of submodule gap and PAT workaround for Copilot coding agent)

## Mini-Retro

1. **Did the process work?** Yes. The research skill output structure worked well for a multi-surface technical investigation. Both primary sources answered the core questions directly; community discussions filled in the gaps official docs were silent on.
2. **What slowed down or went wrong?** The first review pass flagged 7 violations: OS not expanded on first use (in §1 decomposition tree, not found by the pre-review scan because the replacement used a slightly different string), several KF confidence levels set too high with single-source evidence, and the §5 "significant governance gap" claim missing an [inference] label. The S7 source reference lacked a URL. All fixable.
3. **What single change would prevent this next time?** Run a Python script to check that every acronym used in the document has its expansion on the line with the EARLIEST occurrence, not just "somewhere in the document." The first-use check needs to find line numbers, not just presence.
4. **Is this a pattern?** Yes. The OS/first-use miss is the same pattern noted in the instructions (19+ review failures for acronym expansion). The confidence-level over-rating for single-source claims is also a recurring pattern: the standard requires multiple independent sources for high confidence, but the instinct is to label primary-source claims as high confidence. Both patterns are in the Known Recurring Patterns instructions.
