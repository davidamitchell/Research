# 2026-03-29 -- Research Loop (agents-md-role-and-cross-agent-instructions)

**Completed:**

Research item:
- `Research/completed/2026-03-28-agents-md-role-and-cross-agent-instructions.md` -- completed; ADR-0006's deletion of AGENTS.md in favour of `.github/copilot-instructions.md` is the better-supported approach for this repo's primary tools (Copilot CLI and Copilot Coding Agent web). The Copilot CLI has a verified bug silently ignoring AGENTS.md when copilot-instructions.md is present, and the AGENTS.md spec has no import syntax that would make a thin pointer pattern viable. The one genuine gap is Claude iOS Code, which reads only CLAUDE.md and is served by neither existing file.

Sources consulted:
- https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions (Copilot CLI custom instructions official docs)
- https://github.com/github/copilot-cli/issues/489 (verified bug report: AGENTS.md ignored when copilot-instructions.md present)
- https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/ (Copilot Coding Agent web now reads AGENTS.md additively)
- https://code.claude.com/docs/en/memory (Claude Code memory/instruction file docs confirming CLAUDE.md only)
- https://github.com/agentsmd/agents.md/issues/11 (confirms AGENTS.md has no import/pointer syntax)
- https://github.com/davidamitchell/Research/blob/main/docs-adr/0006-standardise-agent-instruction-files.md (ADR-0006 primary source)

## Mini-Retro

1. **Did the process work?** Yes. The research loop completed two full review cycles and reached auto-pass (review_count 2). The violation-fix cycle added one extra iteration beyond what a cleaner first draft would have required.
2. **What slowed down or went wrong?** First-round violations were: (a) `[fact]` label on a blog-sourced CLAUDE.md claim, (b) use of "correct" as an evaluative term without an epistemic label, (c) "clearly" as an unqualified intensifier, (d) missing cross-reference to the prior item's conflicting recommendation. Second-round violations were: (e) "AI" and "iOS" not expanded on first use, (f) drift claim labelled as fact rather than inference. The most avoidable of these were (b), (c), (d), and (e) -- all detectable by the Step 6 self-review checklist.
3. **What single change would prevent this next time?** Run the full acronym audit at the document level (not per-section) before the first draft commit, and search for every evaluative adjective ("correct", "right", "better", "clearly") before committing to confirm each is labelled [inference] or backed by a direct source quote.
4. **Is this a pattern?** Yes -- evaluative terms without epistemic labels and missed first-use acronym expansions are the two most common repeat failures across review cycles. Both are already in the Step 6 self-review checklist; the issue is failing to apply them with sufficient rigour before the first commit.
