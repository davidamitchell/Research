# 2026-03-14 — Research Loop (ai-team-size-strike-team-thesis)

**Completed:**

Research item:
- `Research/completed/2026-03-12-ai-team-size-strike-team-thesis.md` — completed; establishes the mathematical case for the 5-person strike team using Brooks' n(n-1)/2 coordination formula, demonstrates that AI-driven per-person output gains make each coordination channel proportionally more expensive, and validates the scout/strike team archetypes with Steinberger/OpenClaw as existence proof and Shopify's April 2025 mandate as institutional operationalisation.

Sources consulted:
- https://youtu.be/hnwM01CpzmA (Nate Jones — "45 People, $200M Revenue" — primary video source, reconstructed via digest summary)
- https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/ (Shopify Lütke memo — AI before headcount mandate)
- https://electroiq.com/stats/midjourney-statistics/ (Midjourney 2025 revenue and headcount data)
- https://fortune.com/2026/02/19/openclaw-who-is-peter-steinberger-openai-sam-altman-anthropic-moltbook/ (Steinberger/OpenClaw existence proof)
- https://8thlight.com/insights/mythical-man-month-the-cliff-notes (Brooks' n(n-1)/2 coordination formula)
- https://natesnewsletter.substack.com/p/executive-briefing-ai-raised-output (Nate Jones newsletter — scout/strike team framework)

## Mini-Retro

1. **Did the process work?** Yes. The research skill sections ran cleanly. The review passed without any violations on the first attempt.

2. **What slowed down or went wrong?** Two things: (a) the target item (`ai-force-multiplier-ambition-expansion`) had already been completed in a previous session but the backlog version had survived — likely due to a git reset. This required cleanup before picking the second item. (b) The primary video transcript was not directly accessible, requiring reconstruction from context and the digest summary — flagged explicitly as an assumption in §2.

3. **What single change would prevent this next time?** The stale backlog item issue could be caught by checking whether a corresponding file already exists in `completed/` before running `research start`. A pre-check step in the research loop prompt would prevent this.

4. **Is this a pattern?** Yes — this matches the known pattern of uncommitted or orphaned backlog files surviving git operations. The instructions already note to use `git add -A` + conditional commit to preserve agent work. The inverse problem (stale backlog items from previous sessions) is not yet documented as a known pattern.
