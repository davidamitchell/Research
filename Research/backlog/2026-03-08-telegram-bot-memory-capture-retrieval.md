---
title: "Telegram bot for memory capture and retrieval"
added: 2026-03-08
status: backlog
priority: medium
tags: [telegram, bot, memory-capture, retrieval, mobile, chatbot]
started: ~
completed: ~
output: [tool, knowledge]
---

# Telegram bot for memory capture and retrieval

## Research Question

Is a Telegram bot a viable mobile-first interface for capturing and retrieving memory items in the Memory-System — and what does a minimal, production-quality implementation look like?

## Scope

**In scope:**
- Telegram Bot API capabilities for message handling, inline keyboards, and file attachments
- Hosting options for the bot backend (GitHub Actions, Fly.io, Railway, self-hosted VPS)
- Conversation flow design for capture (free text, URL, voice note transcription) and retrieval (keyword search, tag filter)
- Authentication: restricting the bot to a single user or allowlist
- Persistence: how the bot writes to and reads from the memory store

**Out of scope:**
- Group chat or multi-user memory sharing
- Slack or other messaging platforms (separate research items)

**Constraints:** Must be operable without a laptop. Bot infrastructure must have low ongoing cost (ideally free tier or < $5/month).

## Context

Telegram bots offer a conversational interface that is available on iOS, Android, and desktop — and the Telegram Bot API is straightforward to call from a lightweight server. For a personal memory system, a Telegram bot could provide a natural-language capture experience ("remember this: …") and retrieval interface ("what do I know about X?") without requiring a dedicated app.

The key questions are infrastructure cost and operational complexity: does the bot need a persistent server, or can it use webhooks with a serverless backend?

## Related

**Memory-System backlog:** [W-0011 — Telegram bot for capture and retrieval](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the implementation path for the W-0011 discovery item, evaluating Telegram as a viable capture/retrieval interface.

## Approach

1. **Bot API survey:** Review the Telegram Bot API for the capabilities needed: message types, webhook vs polling, inline query for retrieval, file handling for voice notes.
2. **Backend architecture options:** Compare webhook + serverless (GitHub Actions, Cloudflare Workers), webhook + lightweight server (Fly.io free tier), and long-polling on a VPS. Evaluate each on cost, latency, and maintenance burden.
3. **Capture flow design:** Define the conversation flows for the three main capture modes: free text, URL with optional comment, and voice note (requiring transcription).
4. **Retrieval flow design:** Design the query interface — likely an inline keyboard or natural-language query passed to the memory system's search.
5. **Auth and security:** Evaluate how to restrict the bot to a single user (user ID check) and handle the token secret safely in the deployment environment.
6. **Prototype:** Build a minimal working bot covering capture and one retrieval path; test latency and UX.

## Sources

- [ ] Telegram Bot API documentation — https://core.telegram.org/bots/api
- [ ] Fly.io free tier docs — https://fly.io/docs/about/pricing/
- [ ] python-telegram-bot library — https://python-telegram-bot.org/
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0011 — the corresponding discovery item that this research informs

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
