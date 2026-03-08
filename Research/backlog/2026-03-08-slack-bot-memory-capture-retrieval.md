---
title: "Slack as a mobile memory capture and retrieval channel"
added: 2026-03-08
status: backlog
priority: medium
blocks: []
tags: [mobile, slack, bot, capture, retrieval, memory-system]
started: ~
completed: ~
output: [knowledge]
---

# Slack as a mobile memory capture and retrieval channel

## Research Question

Can a Slack bot in a personal or team workspace serve as a memory capture and retrieval surface? What is the minimum viable setup: slash command vs bot, incoming webhook vs Socket Mode, and does a free Slack workspace support enough API access? Can the bot call `search_brain` and return results into a thread?

## Scope

**In scope:**
- Slack API options: Slash commands, Socket Mode, incoming webhooks
- Free Slack workspace API access limits and constraints
- Capture path: Slack message / slash command → GitHub Contents API write
- Retrieval path: bot call → `search_brain` → reply in thread
- Hosting requirements: Socket Mode (no public URL) vs webhook (requires public URL)
- Comparison with Telegram option (`2026-03-08-telegram-bot-memory-capture-retrieval.md`)

**Out of scope:**
- Slack as a team knowledge base (different use case — this is personal memory)
- MS Teams (covered in `2026-03-02-slack-msteams-research-integration.md` for research delivery; not a focus for memory capture)

**Constraints:** Free Slack workspace limitations are a hard constraint — no paid tier assumed. Socket Mode avoids the need for a public URL, which simplifies hosting.

## Context

Slack is open on many people's phones all day. A dedicated `#brain` channel means capture is 2 taps — no app switching beyond what is already happening. Compare against Telegram (`2026-03-08-telegram-bot-memory-capture-retrieval.md`): Slack requires a workspace but may already be open for work; Telegram is cleaner for personal use but adds another app. The hosted component requirement is the same for both paths.

A completed research item already exists for Slack/MS Teams as a *research delivery* channel (`2026-03-02-slack-msteams-research-integration.md`). This item is distinct: it focuses on Slack as a *memory system capture and retrieval* surface (writing to the Memory-System repo, calling `search_brain`), not on notifying about completed research items.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` confirms the value of memory being accessible from wherever you already are — Slack on mobile is exactly this "ambient" surface.

## Approach

1. Survey free Slack workspace API capabilities: which features are available without a paid plan
2. Evaluate Socket Mode vs incoming webhook vs slash commands for this use case
3. Prototype capture handler: Slack message → GitHub Contents API write to `inbox/`
4. Prototype retrieval handler: slash command `?<query>` → `search_brain` → thread reply
5. Evaluate hosting: Socket Mode eliminates the public URL requirement; compare Fly.io, Railway, Render free tier
6. Measure end-to-end latency for capture and retrieval
7. Compare Slack vs Telegram on friction, reliability, maintenance, and free-tier sustainability

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production memory system patterns; "memory accessible from wherever you already are"
- [ ] `Research/completed/2026-03-02-slack-msteams-research-integration.md` — existing findings on Slack API for this research repo; directly applicable to the hosting and API access questions
- [ ] Slack API docs (Bolt for Python): https://api.slack.com/tools/bolt
- [ ] Slack Socket Mode docs: https://api.slack.com/apis/connections/socket
- [ ] Slack free plan limits: https://slack.com/intl/en/help/articles/218688717-What-is-Slack-s-message-retention-policy
- [ ] GitHub Contents API docs: https://docs.github.com/en/rest/repos/contents
- [ ] Fly.io free tier docs: https://fly.io/docs/about/pricing/
- [ ] Railway free tier docs: https://docs.railway.app/reference/pricing

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

- Type: knowledge
- Description:
- Links:
