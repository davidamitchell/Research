---
title: "Slack and MS Teams integration for research delivery and capture"
added: 2026-03-02
status: backlog
priority: medium
tags: [slack, ms-teams, integration, delivery, notifications, bot, interface, distribution]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# Slack and MS Teams integration for research delivery and capture

## Research Question

What is the most practical way to integrate the research corpus with Slack and/or Microsoft Teams — for both outbound delivery (notifying when new research is completed) and inbound capture (receiving new research requests or queries via chat) — given the constraints of a personal, GitHub-hosted repository with no server infrastructure?

## Scope

**In scope:**
- Outbound delivery: posting to a Slack channel or Teams channel when a new research item is completed (push to `main` touching `Research/completed/**`)
- Inbound capture: receiving research questions or new backlog requests via a Slack slash command or Teams message
- Bot architecture options: GitHub Actions + Incoming Webhook (simplest), Slack app with slash commands, Teams bot via Azure Bot Framework or Power Automate
- Credential requirements: what secrets are needed and how they are stored as GitHub Actions secrets
- Digest mode: weekly summary of newly completed research items posted to a channel, rather than per-item notifications
- Query interface: asking the bot "what have I researched about X?" and getting a response (draws on `2026-03-02-chat-conversational-interface.md`)

**Out of scope:**
- Multi-user or team-wide research workflows (this is a personal research system)
- Full two-way conversation with the research corpus from within Slack/Teams (covered conceptually in `2026-03-02-chat-conversational-interface.md`)
- Enterprise Slack/Teams administration (compliance, data retention policies)
- Building or deploying a persistent bot server — must remain serverless or GitHub Actions-based

**Constraints:** The owner interacts exclusively via GitHub website and iOS app. Any Slack/Teams integration must be triggerable from GitHub Actions or be event-driven from GitHub events. No persistent server process; no local tooling required.

## Context

Research outputs currently flow to one channel: the GitHub wiki (implemented in `2026-03-01-github-wiki-research-content.md`). The wiki is accessible from the GitHub website and iOS app but requires the owner to navigate to it. There is no proactive delivery — the owner must pull, not be pushed.

The `2026-02-27-interface-and-delivery.md` backlog item lists "email digest" as a future option but does not address Slack or Teams. Given that most knowledge workers' attention lives in Slack or Teams rather than wiki browsers, push delivery to a chat platform is likely to produce higher engagement with completed research than a wiki.

Slack Incoming Webhooks are the simplest implementation: a GitHub Actions step POSTs a JSON payload to a webhook URL when a research item is completed. No persistent bot process, no OAuth flow for outbound notifications. Inbound capture (slash commands, query responses) requires a more sophisticated setup — either a Slack app with a request URL pointing to a GitHub Actions workflow via `workflow_dispatch`, or a third-party integration layer (Zapier, Make, Power Automate).

MS Teams offers similar capabilities: Incoming Webhooks for outbound, Power Automate flows or Azure Bot Framework for inbound. The Microsoft 365 ecosystem may be relevant if the owner already uses Teams for work.

This item does NOT require credentials that are currently documented. A new Slack webhook URL or Teams webhook URL would be a new secret. Per AGENTS.md constraints, these must be explicitly approved by the owner before implementation.

## Approach

1. **Clarify owner's chat platform** — Does the owner use Slack, MS Teams, or both? The choice of platform determines the implementation path. This is a clarifying question that must be answered before any implementation work begins.

2. **Outbound delivery design (simplest first)** — Design the GitHub Actions step for push-to-channel notifications:
   - Trigger: push to `main` that touches `Research/completed/**` (same trigger as `publish-wiki.yml`)
   - Action: call Slack Incoming Webhook or Teams Incoming Webhook with: item title, date, tags, executive summary (first 200 chars), link to wiki page
   - Assess: what secrets are required? (Slack: `SLACK_WEBHOOK_URL`; Teams: `TEAMS_WEBHOOK_URL`) — these would be new secrets requiring owner approval

3. **Digest mode design** — Instead of per-item notifications, a weekly digest job (scheduled GitHub Actions, Monday 08:00 local time) aggregates items completed in the past 7 days and posts a summary. Assess trade-offs: per-item = immediate but noisy; digest = lower frequency, higher signal.

4. **Inbound capture design** — Map the paths for receiving research requests via chat:
   - Option A: Slash command → webhook → GitHub Actions `workflow_dispatch` to create a new backlog item
   - Option B: Power Automate / Zapier flow: message → GitHub API to create a file in `Research/backlog/`
   - Option C: Share a GitHub issue link in chat; owner creates issue; existing issue-to-backlog workflow handles it
   Assess: what credentials and infrastructure does each option require?

5. **Query interface integration** — Assess whether the chat integration can answer "what have I researched about X?" by calling the conversational interface from `2026-03-02-chat-conversational-interface.md`. This requires a two-way bot (more complex than a webhook). Flag this as a separate implementation slice if the complexity is high.

6. **Credential and secret inventory** — Document exactly which new secrets are required and confirm with the owner before any implementation work begins. Per AGENTS.md: new credentials require explicit owner approval.

## Sources

- [ ] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream interface and delivery options item
- [ ] `Research/completed/2026-03-01-github-wiki-research-content.md` — existing delivery channel (wiki), same trigger pattern to reuse
- [ ] `Research/backlog/2026-03-02-chat-conversational-interface.md` — conversational query interface (inbound query path)
- [ ] Slack Incoming Webhooks docs: https://api.slack.com/messaging/webhooks
- [ ] Slack app slash commands: https://api.slack.com/interactivity/slash-commands
- [ ] MS Teams Incoming Webhook: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
- [ ] MS Teams bot framework: https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
- [ ] GitHub Actions: `workflow_dispatch` with `inputs` — for triggering backlog capture from external webhooks
- [ ] `8398a7/action-slack`: https://github.com/8398a7/action-slack — community Slack notification Action

---

## Findings

*(Fill in when completing. Follow the research skill synthesis structure.)*

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

- Type: knowledge, backlog-item
- Description: Recommended integration pattern (webhook-based vs. bot-based); credential inventory; implementation slice for `publish-wiki.yml`-adjacent notification workflow; decision on digest vs. per-item delivery
- Links:
  - `Research/backlog/2026-02-27-interface-and-delivery.md` (upstream item)
  - `Research/completed/2026-03-01-github-wiki-research-content.md` (existing delivery implementation to reuse trigger)
  - `Research/backlog/2026-03-02-chat-conversational-interface.md` (query interface dependency)
