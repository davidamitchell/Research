---
title: "Slack bot for memory capture and retrieval"
added: 2026-03-08
status: backlog
priority: medium
tags: [slack, bot, memory-capture, retrieval, mobile, workspace]
started: ~
completed: ~
output: [tool, knowledge]
---

# Slack bot for memory capture and retrieval

## Research Question

Can a Slack bot serve as a low-friction capture and retrieval interface for a personal memory system — and what are the trade-offs compared to other messaging-based interfaces (Telegram, iOS Shortcuts)?

## Scope

**In scope:**
- Slack Bolt SDK (Python/Node) for bot implementation
- Slack API features relevant to capture: slash commands, message actions, shortcuts, home tab
- Hosting requirements and cost for a personal-use Slack bot
- Retrieval via Slack: search-like query flow, returning formatted memory snippets
- Slack free tier limitations (message history, app limits)

**Out of scope:**
- Slack for team/shared memory — personal use only
- Slack workflow automations (focus on bot interactions, not no-code workflows)

**Constraints:** Must work on Slack's free tier if possible. Must be operable from the Slack iOS app.

## Context

Slack is a familiar interface for many knowledge workers, and a personal Slack workspace costs nothing on the free tier. A Slack bot could act as a capture channel ("DM the bot to remember something") and a retrieval surface (slash command queries). The Slack Block Kit UI is richer than plain text, enabling formatted memory cards with action buttons.

However, Slack's free tier has message retention limits (90 days as of 2022), and hosting a responsive bot requires a persistent server or webhook endpoint — which adds infrastructure. This item weighs Slack against simpler alternatives for the same use case.

## Related

**Memory-System backlog:** [W-0003 — Slack bot capture and retrieval](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the Slack implementation path for the W-0003 discovery item on messaging-based memory interfaces.

## Approach

1. **Slack API capability audit:** Identify the Slack API features applicable to capture (slash commands, message actions, shortcuts, DMs) and retrieval (home tab, modal views, Block Kit cards).
2. **Free tier constraints:** Document the Slack free tier limits that affect this use case — message retention, app limits, API rate limits.
3. **Hosting options:** Compare webhook hosting approaches: Slack Socket Mode (no public URL needed) vs HTTPS webhook (requires server). Evaluate serverless (Cloudflare Workers, Vercel) vs always-on (Fly.io).
4. **UX flow design:** Map the capture and retrieval flows for the Slack iOS app. How many taps to capture? How readable are retrieval results on mobile?
5. **Comparison with Telegram:** Directly compare Slack vs Telegram on the axes that matter: cost, hosting complexity, UX on iOS, API richness, lock-in risk.

## Sources

- [ ] Slack Bolt SDK documentation — https://slack.dev/bolt-python/
- [ ] Slack API Block Kit reference — https://api.slack.com/block-kit
- [ ] Slack free tier limits — https://slack.com/intl/en-gb/pricing
- [ ] Slack Socket Mode docs — https://api.slack.com/apis/socket-mode
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0003 — the corresponding discovery item that this research informs

---

## Research Skill Output

*(To be populated when research is conducted.)*

### §0 Initialise

-

### §1 Question Decomposition

-

### §2 Investigation

-

### §3 Reasoning

-

### §4 Consistency Check

-

### §5 Depth and Breadth Expansion

-

### §6 Synthesis

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

-

---

## Findings

*(To be populated when research is completed.)*

### Executive Summary

### Key Findings

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

- **Assumption:** ... **Justification:** ...

### Analysis

### Risks, Gaps, and Uncertainties

-

### Open Questions

-

---

## Output

- Type:
- Description:
- Links:
