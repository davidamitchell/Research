---
title: "Telegram bot as mobile memory capture and retrieval channel"
added: 2026-03-08
status: backlog
priority: medium
blocks: []
tags: [mobile, telegram, bot, capture, retrieval, memory-system, self-hosted]
started: ~
completed: ~
output: [tool, knowledge]
---

# Telegram bot as mobile memory capture and retrieval channel

## Research Question

Can a Telegram bot serve as a low-friction mobile capture and retrieval surface for the Memory-System? Specifically: (a) message received → file written to GitHub repo via API, (b) messages starting with `?` trigger semantic search via `search_brain` and reply with results, (c) what is the minimum hosting requirement (Raspberry Pi, VPS, free tier PaaS)?

## Scope

**In scope:**
- Telegram Bot API — long-polling vs webhook architecture
- Capture path: Telegram message → GitHub Contents API write (file created in `inbox/`)
- Retrieval path: `?<query>` message → `search_brain` → reply with top results
- Hosting options: Railway, Render, Fly.io free tier, Raspberry Pi + Tailscale
- Security model: bot token storage, GitHub PAT storage, restricting bot to owner only
- End-to-end latency for capture and retrieval
- Comparison with iOS Shortcuts path (no hosted component)

**Out of scope:**
- Slack (separate item: `2026-03-08-slack-bot-memory-capture-retrieval.md`)
- Self-hosted MCP server (separate item: `2026-03-08-self-hosted-mcp-server-options.md`)
- Android-specific considerations (Telegram is cross-platform; Android UX is implicitly covered)

**Constraints:** Free-tier hosting must sustain the bot continuously or handle cold starts gracefully. Bot token and GitHub PAT must not be committed to source.

## Context

Telegram bots have a simple, well-documented API. The UX is identical to messaging a contact — a `#brain` DM channel requires no app switching if Telegram is already installed. Unlike iOS Shortcuts, Telegram requires a hosted component, but free-tier PaaS options make this near-zero cost. The hosted component is unavoidable but manageable.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` notes that no production memory system has retrieval + write governance in a single surface. This item explores whether a Telegram bot can provide both in one chat-based interface, which is a novel combination not covered by the existing agent memory research. The completed `2026-03-02-ios-shortcuts-research.md` covers iOS-native capture; this item covers a different architecture (bot + hosted service) that is platform-agnostic.

## Related

**Memory-System backlog:** [W-0011 — Telegram bot as mobile memory capture and retrieval channel](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Survey Telegram Bot API: long-polling vs webhook, message handling, rate limits
2. Prototype message handler: receive text → write `.md` to GitHub repo via Contents API
3. Prototype retrieval handler: `?<query>` → call `search_brain` MCP tool → format and reply
4. Evaluate hosting options: Railway, Render, Fly.io free tier, and Raspberry Pi + Tailscale
5. Measure end-to-end latency for capture (message → commit) and retrieval (message → reply)
6. Document security model: restricting the bot to owner chat ID only, secret rotation
7. Compare against iOS Shortcuts path on friction, reliability, and maintenance burden

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production memory system patterns; context on why unified capture + retrieval surfaces are valuable
- [ ] Telegram Bot API docs: https://core.telegram.org/bots/api
- [ ] Telegram Bot API long-polling vs webhook guide: https://core.telegram.org/bots/api#getting-updates
- [ ] GitHub Contents API docs: https://docs.github.com/en/rest/repos/contents
- [ ] Railway free tier docs: https://docs.railway.app/reference/pricing
- [ ] Fly.io free tier docs: https://fly.io/docs/about/pricing/
- [ ] Render free tier docs: https://render.com/docs/free
- [ ] Tailscale docs (for Raspberry Pi home server): https://tailscale.com/kb/1017/install
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0011 — the corresponding discovery item that this research informs

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: tool, knowledge
- Description:
- Links:
