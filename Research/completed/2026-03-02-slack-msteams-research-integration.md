---
title: "Slack and MS Teams integration for research delivery and capture"
added: 2026-03-02
status: completed
priority: medium
tags: [slack, ms-teams, integration, delivery, notifications, bot, interface, distribution]
started: 2026-03-08
completed: 2026-03-08
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

**Prior research:** The `2026-03-01-github-wiki-research-content.md` item established the outbound delivery trigger pattern (`push` to `main` touching `Research/completed/**` + `workflow_dispatch`) and confirmed `GITHUB_TOKEN` with `contents: write` is sufficient for wiki pushes. This item reuses the same trigger. The `2026-03-02-chat-conversational-interface.md` item concluded that full two-way corpus queries require an MCP stdio server — making a full query bot (inbound question → search corpus → reply in Slack) out of scope for a GitHub Actions-only approach. The `2026-02-27-interface-and-delivery.md` item lists chat delivery as a future option but provides no detail; this item is the detailed investigation. No prior completed item addresses Slack or Teams webhook mechanics specifically.

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

- [x] `Research/backlog/2026-02-27-interface-and-delivery.md` — upstream interface and delivery options item
- [x] `Research/completed/2026-03-01-github-wiki-research-content.md` — existing delivery channel (wiki), same trigger pattern to reuse
- [x] `Research/completed/2026-03-02-chat-conversational-interface.md` — conversational query interface (inbound query path)
- [x] Slack Incoming Webhooks docs: https://api.slack.com/messaging/webhooks
- [x] Slack app slash commands: https://api.slack.com/interactivity/slash-commands
- [x] MS Teams Incoming Webhook: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
- [x] MS Teams bot framework: https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
- [ ] GitHub Actions: `workflow_dispatch` with `inputs` — for triggering backlog capture from external webhooks
- [x] `8398a7/action-slack`: https://github.com/8398a7/action-slack — community Slack notification Action (archived Sep 2025; replaced by `slackapi/slack-github-action`)

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is the most practical way to integrate this GitHub-hosted research corpus with Slack and/or Microsoft Teams for both outbound push notifications (completed research → chat channel) and inbound capture (research requests submitted via chat), given that no persistent server process is available and all operations must run via GitHub Actions?

**Scope:** Outbound webhook delivery; digest mode scheduling; inbound capture architecture; credential inventory. Out of scope: full two-way corpus queries (deferred to MCP server item); enterprise administration; persistent bots.

**Constraints:**
- No server infrastructure. All execution must happen within GitHub Actions runner lifetime.
- New credentials (`SLACK_WEBHOOK_URL`, `TEAMS_WEBHOOK_URL`) require explicit owner approval before implementation.
- Inbound from Slack slash commands requires an HTTPS endpoint that responds within 3 seconds — GitHub Actions cannot serve this directly.

**Output format:** Structured findings with evidence labels, evidence map table, implementation recommendations and credential inventory.

### §1 Question Decomposition

Root question decomposed into four branches:

**Branch A — Outbound delivery**
- A1: What protocol does Slack Incoming Webhook use, and what payload format is required?
- A2: What is the current status of `slackapi/slack-github-action` vs. `8398a7/action-slack`?
- A3: What secret(s) does outbound Slack delivery require, and how are they stored?
- A4: What is the current status of MS Teams Incoming Webhooks, and what protocol/format do they use?
- A5: Are the Slack and Teams trigger patterns compatible with the existing `publish-wiki.yml` push trigger?

**Branch B — Digest mode**
- B1: What GitHub Actions mechanism enables a weekly scheduled digest?
- B2: How can the digest workflow identify items completed in the last 7 days from `Research/completed/`?
- B3: What are the trade-offs between per-item notification and weekly digest?

**Branch C — Inbound capture**
- C1: What does a Slack slash command require as infrastructure (endpoint, response time)?
- C2: Can GitHub Actions serve as the endpoint for a Slack slash command without a persistent server?
- C3: What are the viable inbound capture paths under the no-server constraint?
- C4: What secrets does each inbound capture option require?

**Branch D — Query interface**
- D1: Can a Slack/Teams bot call the research corpus MCP server without a persistent process?
- D2: What is the simplest viable query path under the no-server constraint?

### §2 Investigation

**A1 — Slack Incoming Webhook protocol and payload format**

The Slack Incoming Webhooks page (api.slack.com/messaging/webhooks) describes the complete flow: create a Slack app, enable Incoming Webhooks, add a webhook to a workspace channel. This produces a unique HTTPS URL. Posting a JSON payload via HTTP POST delivers a message to the designated channel. Payloads use Block Kit (structured blocks) or simple `text` fields with `mrkdwn` formatting. **[fact]** Source: api.slack.com/messaging/webhooks (accessed 2026-03-08).

**A2 — Action status: `slackapi/slack-github-action` vs `8398a7/action-slack`**

`8398a7/action-slack` was archived on 2025-09-13 with an explicit notice: "No updates, fixes, or support will be provided. Recommended alternative: `slackapi/slack-github-action`." **[fact]** Source: github.com/8398a7/action-slack.

`slackapi/slack-github-action` (the official Slack-maintained GitHub Action) is the current recommended action. As of March 2026 it is at v2.1.1. It supports three sending techniques: (1) webhook to Slack Workflow Builder, (2) Slack API method with bot token, (3) Incoming Webhook URL. **[fact]** Source: raw.githubusercontent.com/slackapi/slack-github-action/main/README.md; docs.slack.dev/tools/slack-github-action.

The incoming webhook technique uses:
```yaml
- uses: slackapi/slack-github-action@v2.1.1
  with:
    webhook: ${{ secrets.SLACK_WEBHOOK_URL }}
    webhook-type: incoming-webhook
    payload: |
      text: "New research: *<title>*\n<executive summary>\n<wiki link>"
```
**[fact]** Source: docs.slack.dev/tools/slack-github-action/sending-techniques/sending-data-slack-incoming-webhook/.

**A3 — Slack outbound secret requirements**

One secret is required: `SLACK_WEBHOOK_URL`. This is the unique HTTPS URL generated by the Slack app's Incoming Webhook configuration. It must be stored as a GitHub Actions repository secret. **[fact]** Source: api.slack.com/messaging/webhooks; slackapi/slack-github-action docs. This is a new secret not currently listed in AGENTS.md; it requires explicit owner approval before implementation.

**A4 — MS Teams Incoming Webhook status**

The Teams documentation page (learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook, accessed 2026-03-08) opens with a prominent notice: "Microsoft 365 Connectors (previously called Office 365 Connectors) are nearing deprecation, and the creation of new Microsoft 365 Connectors will soon be blocked." **[fact]** Source: Microsoft Learn (updated 2025-06-10).

The replacement mechanism is Power Automate with the "When a Teams webhook request is received" trigger. This trigger generates a unique HTTPS URL that accepts JSON payloads and posts Adaptive Cards to a Teams channel. **[fact]** Source: Microsoft Learn, same page. The Power Automate webhook URL is functionally equivalent to the Slack Incoming Webhook URL: it is an HTTPS endpoint that accepts POST requests. It can be stored as a GitHub Actions secret (`TEAMS_WEBHOOK_URL`) and called with `curl` in a workflow step.

Limitations of the Teams webhook approach: (1) Workflows are linked to a specific user (the flow owner), not the team, so they become orphaned if the owner leaves. (2) Workflows can only be created in the default Power Automate environment. (3) Private channels are not supported. (4) Adaptive Cards only — old message card format is not supported. **[fact]** Source: Microsoft Learn, same page.

**A5 — Trigger pattern compatibility**

The `publish-wiki.yml` trigger uses:
```yaml
on:
  push:
    branches: [main]
    paths:
      - "Research/completed/**"
  workflow_dispatch:
```
This is directly reusable for a Slack/Teams notification workflow. The same `push` event fires when the research loop commits a completed item. A new workflow file (e.g., `.github/workflows/notify-research.yml`) can use the identical trigger. **[fact]** Source: `.github/workflows/publish-wiki.yml` (direct file inspection).

**B1–B3 — Digest mode**

A `schedule:` trigger with `cron: '0 8 * * 1'` (Monday 08:00 UTC) runs a weekly digest. The workflow reads `Research/completed/` file modification times (or front-matter `completed:` dates) to identify items completed in the last 7 days. A Python script (similar to `src/wiki/publish.py`) can read the YAML front-matter from each file and filter by `completed:` date. **[inference]** — derived from the existing wiki publish pattern and standard GitHub Actions cron syntax.

Per-item vs. digest trade-off:
- Per-item: immediate delivery; one message per completed item; potentially multiple messages on a single research-loop run (if 3 items complete); actionable immediately.
- Weekly digest: consolidated view; lower notification volume; appropriate if the research loop runs daily and produces 3–5 items per run; less suitable if the owner wants to act on findings immediately.

These are not mutually exclusive: both triggers can coexist in the same workflow file or separate files. **[inference]**

**C1–C4 — Inbound capture architecture**

Slack slash commands require an HTTPS endpoint that: (a) receives a POST from Slack within 3 seconds of the slash command being invoked, and (b) returns a 200 OK with a JSON response. **[fact]** Source: api.slack.com/interactivity/slash-commands (fetched 2026-03-08 — page contained the slash command specification alongside Block Kit examples).

GitHub Actions cannot serve as the slash command endpoint. A GitHub Actions `workflow_dispatch` can be triggered via the GitHub REST API, but the trigger-and-respond cycle takes 5–30 seconds — far exceeding Slack's 3-second acknowledgement window. A persistent server (Lambda, Cloud Run, Fly.io) would be required to bridge the Slack acknowledgement with the GitHub API call. **[inference]** — derived from the 3-second Slack requirement and the typical GitHub Actions queue latency.

Three viable inbound capture paths under the no-server constraint:

**Option A — GitHub issue as backlog proxy (no new credentials):** The owner creates a GitHub issue via the GitHub website or iOS app. A GitHub Actions workflow triggered on `issues: [opened]` reads the issue title and body, creates a file in `Research/backlog/` using the template, and closes the issue. This requires zero new secrets — `GITHUB_TOKEN` with `contents: write` is sufficient. The friction is two steps (open issue → workflow creates backlog file) vs. one (chat message). **[inference]**

**Option B — Zapier/Make free tier as Slack→GitHub bridge (new third-party service):** A Zapier or Make.com automation receives the Slack slash command acknowledgement, waits for the message, then calls the GitHub API to create a backlog file. This requires: (1) a Zapier/Make account (free tier sufficient), (2) a GitHub PAT with `contents: write` stored in Zapier/Make, (3) a Slack app with slash command configured. This introduces a new external service and new credentials — both require explicit owner approval per AGENTS.md. **[inference]**

**Option C — Scheduled harvest of a pinned Slack message (no server, low friction):** A GitHub Actions scheduled workflow reads messages from a designated Slack channel using the Slack Web API (bot token) and converts unprocessed messages tagged with a trigger emoji (e.g., 📌) into backlog items. This requires a Slack bot token (`SLACK_BOT_TOKEN`) — a new credential requiring approval. It is asynchronous (runs on a schedule, not instantly), which is acceptable for a personal workflow. **[inference]**

**D1–D2 — Query interface via chat**

The `2026-03-02-chat-conversational-interface.md` item concluded that corpus queries require an MCP stdio server. A Slack/Teams bot cannot call an MCP stdio server without a persistent process — the bot would need to fork the Python MCP server on each incoming message, which is only possible in a long-running process. **[fact]** Source: direct reading of completed research item; MCP stdio transport specification.

The simplest viable query path without a server: the bot receives a search query, constructs a wiki search URL or links to the Home wiki page, and replies with a pointer to the wiki. This is not a true query interface but makes the existing wiki discoverable from chat. **[inference]** True query capability requires either a hosted bot server or waits for the iOS Shortcuts integration item (`2026-03-02-ios-shortcuts-research.md`) to establish a proxy.

### §3 Reasoning

**Outbound delivery:** The Slack Incoming Webhook path is the lowest-complexity viable approach. It requires one new secret, one new workflow file, and zero new infrastructure. The official `slackapi/slack-github-action@v2.1.1` action handles the POST and is actively maintained by Slack. The trigger pattern is already validated by `publish-wiki.yml`. The implementation can be shipped as soon as `SLACK_WEBHOOK_URL` is approved and stored.

For Teams, the Power Automate webhook path is the current supported approach (connectors are deprecated). The workflow URL is called identically via `curl` in the Actions step, requiring one new secret (`TEAMS_WEBHOOK_URL`). The Teams path is slightly higher friction to set up (requires creating a Power Automate flow) but once the URL is obtained it behaves identically to the Slack webhook.

**Inbound capture:** The no-server constraint eliminates Slack slash commands as a direct implementation. Option A (GitHub issue → workflow) is immediately feasible with no new credentials and fits the existing owner interaction model (creating issues via the GitHub website and iOS app). Option B (Zapier/Make bridge) is feasible but introduces a new third-party service and new credentials — a hard-stop under AGENTS.md until the owner explicitly approves. Option C (scheduled Slack channel harvest) requires a new credential and is asynchronous, making it lower priority.

Option A is the correct default inbound path: it costs nothing, requires no new credentials, and fits how the owner already interacts with the repository.

**Digest vs. per-item:** Per-item notification is appropriate for a personal research system where each completed item represents discrete, actionable knowledge. The research loop completes up to 5 items per run; five notifications in a few minutes is not burdensome for a personal channel. A digest is additive (a weekly digest can coexist with per-item notifications) but is not the correct default.

### §4 Consistency Check

No internal contradictions identified. The three main claims are consistent:
1. Outbound via webhook (both platforms) is feasible — supported by direct inspection of official documentation.
2. Inbound slash commands require a server — supported by the 3-second Slack requirement and GitHub Actions queue latency characteristics.
3. Option A (GitHub issue proxy) is the only zero-credential inbound path — derived from first principles and consistent with the AGENTS.md credential constraint.

The MS Teams deprecation finding (connectors deprecated; Power Automate webhooks are the replacement) is a primary-source fact from the official Microsoft Learn page (updated 2025-06-10) and does not conflict with any other finding.

The `8398a7/action-slack` deprecation finding is confirmed by direct inspection of the repo and is consistent with the recommendation on that page to switch to `slackapi/slack-github-action`.

### §5 Depth and Breadth Expansion

**Economic lens:** For a personal research system with no budget, the Zapier free tier (100 tasks/month) is technically sufficient for the research volume (≤ 20–30 items/month), but introduces a dependency on a free tier that could be revoked or limited. The GitHub issue → workflow path has no ongoing cost.

**Historical lens:** Slack Incoming Webhooks have been stable since 2015 and show no signs of deprecation. MS Teams connectors, by contrast, have been deprecated — a meaningful signal that Microsoft is consolidating on Power Automate for webhook-based integrations. Teams webhook URLs generated via Power Automate are functionally identical to the old connector URLs but depend on Power Automate service availability.

**Behavioural lens:** Push delivery to Slack/Teams increases the probability that completed research is read. The pull model (wiki) requires the owner to remember to check; push model removes that friction. For a personal system where the owner is the sole consumer, a single message to a personal Slack channel or Teams channel is the most direct delivery path.

**Technical lens — extracting research metadata for the notification payload:** The existing wiki publisher (`src/wiki/publish.py`) already implements `load_frontmatter()` and `strip_frontmatter()`. A notification workflow can invoke a small Python script that reads the changed files (via `git diff --name-only HEAD~1`), loads their front-matter, and formats a Slack Block Kit payload containing: item title, tags, first 200 characters of the executive summary, and a link to the wiki page. No new library dependencies are required.

**Regulatory/compliance lens:** Storing the Slack webhook URL as a GitHub Actions repo secret is consistent with GitHub's recommended practice for sensitive values. The webhook URL, if leaked, allows anyone to post to the designated Slack channel — a low-severity risk for a personal channel but worth noting. Webhook URLs should be rotated if the secret is ever exposed.

### §6 Synthesis

**Structured synthesis:**

The most practical integration is a **two-component approach**:

1. **Outbound notification workflow** — a new GitHub Actions workflow file triggered on `push` to `main` touching `Research/completed/**`. It reads the changed files, extracts front-matter (title, tags, executive summary excerpt), and posts to Slack via `slackapi/slack-github-action@v2.1.1` (or to Teams via `curl` POST to a Power Automate webhook URL). Requires one new secret per platform (`SLACK_WEBHOOK_URL` or `TEAMS_WEBHOOK_URL`). This is low-complexity, immediately implementable after secret approval, and directly reuses the existing `publish-wiki.yml` trigger pattern.

2. **Inbound capture via GitHub Issues** — the owner creates a GitHub issue (via GitHub website or iOS app) with the research question as the title. A new GitHub Actions workflow triggered on `issues: [opened]` reads the issue title and body, creates a `Research/backlog/YYYY-MM-DD-<slug>.md` file from the template, commits it, and closes the issue with a confirmation comment. Requires zero new secrets. This is the only viable inbound path under the no-server, no-new-credentials constraint.

**Items not recommended without further owner decision:**
- Slack slash commands for inbound: requires a persistent server or approved third-party bridge (Zapier/Make).
- Query interface in chat: requires a persistent bot server; deferred to MCP server item.
- Digest mode: additive option; implement after per-item delivery is validated.

**New secrets required:**
- `SLACK_WEBHOOK_URL` — if Slack is the chosen platform.
- `TEAMS_WEBHOOK_URL` (Power Automate webhook URL) — if Teams is the chosen platform.
- Both require explicit owner approval before implementation per AGENTS.md.

### §7 Recursive Review

All threads are synthesised. Evidence labels are present. Sections contain substantive prose. Inbound capture inferences are clearly labelled `[inference]` with justifications. The deprecation of MS Teams connectors is a `[fact]` from a primary source. The no-server constraint on Slack slash commands is an `[inference]` derived from the 3-second acknowledgement requirement — it is well-established in the Slack developer community but was not independently confirmed by a second source (the slash command page was partially inaccessible). This is noted as a gap.

Outstanding uncertainty: which platform the owner uses (Slack or Teams). The research documents both; the owner must decide. If neither platform is in use, the entire integration question is moot. This is flagged as the top open question.

---

## Findings

### Executive Summary

Outbound push delivery to Slack or MS Teams is viable, low-complexity, and immediately implementable using a single new GitHub Actions workflow file and one new secret per platform (`SLACK_WEBHOOK_URL` for Slack, or a Power Automate webhook URL for Teams). The same trigger pattern as `publish-wiki.yml` (`push` to `main` touching `Research/completed/**`) applies directly; the official `slackapi/slack-github-action@v2.1.1` action handles the Slack POST. Inbound capture via Slack slash commands is blocked under the no-server constraint — Slack requires a 3-second HTTP response that GitHub Actions cannot provide — but a GitHub-issues-as-backlog-proxy workflow achieves equivalent inbound capture with zero new secrets. MS Teams Incoming Webhooks (old connector model) are deprecated; the supported replacement is a Power Automate workflow with a webhook trigger. Query-in-chat capability requires a persistent bot server and is out of scope without additional approved infrastructure.

### Key Findings

1. **`slackapi/slack-github-action@v2.1.1` is the only actively maintained official Slack notification action for GitHub Actions; `8398a7/action-slack` was archived on 2025-09-13 and its own README recommends migrating to the Slack-maintained action.** The Slack action supports incoming webhook delivery in four lines of workflow YAML.

2. **Outbound Slack notification requires exactly one new secret (`SLACK_WEBHOOK_URL`) stored as a GitHub Actions repository secret; this secret is the only new credential needed for per-item delivery and requires explicit owner approval before the workflow can be implemented.**

3. **The MS Teams Office 365 Connector model is deprecated; new Teams webhook integrations must use Power Automate with the "When a Teams webhook request is received" trigger, which produces a functionally equivalent HTTPS webhook URL.** The Power Automate URL is stored as `TEAMS_WEBHOOK_URL` and called via `curl` in the Actions step.

4. **The `publish-wiki.yml` trigger pattern (`push` to `main` touching `Research/completed/**` + `workflow_dispatch`) is directly reusable for the notification workflow, requiring no new trigger logic and ensuring the notification fires on the same commit that adds the completed research item.**

5. **Slack slash commands cannot be implemented under the no-server constraint because Slack requires an HTTPS endpoint that responds within 3 seconds of command invocation, and GitHub Actions `workflow_dispatch` has a typical queue latency of 5–30 seconds that makes it structurally incompatible as a direct slash command handler.**

6. **A GitHub-issues-as-proxy workflow achieves equivalent inbound capture with zero new secrets: the owner creates a GitHub issue (accessible from the iOS app) with the research question as the title, and a workflow triggered on `issues: [opened]` converts it to a `Research/backlog/` file and closes the issue.** This fits the owner's existing interaction model and costs nothing to implement.

7. **A weekly digest can be implemented by adding a `schedule: cron: '0 8 * * 1'` trigger to the notification workflow, which reads `Research/completed/` files with `completed:` dates in the past 7 days and posts a consolidated summary; digest and per-item notifications are not mutually exclusive.**

8. **Full query-in-chat capability (asking the bot "what have I researched about X?") requires a persistent bot server to receive the query, call the research MCP server, and post the reply; this is out of scope without approved persistent infrastructure and is already addressed architecturally by the `2026-03-02-chat-conversational-interface.md` MCP server item.**

9. **The existing `src/wiki/publish.py` `load_frontmatter()` function is directly reusable for the notification workflow's metadata extraction step, eliminating the need for a new library; the notification script reads the changed file paths via `git diff --name-only HEAD~1`, loads their front-matter, and formats the payload.**

10. **Per-item notification is the correct default delivery mode for a personal research system where each completed item is discrete and actionable; the weekly digest is an additive option, not a replacement.**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `slackapi/slack-github-action@v2.1.1` is the current recommended action | github.com/slackapi/slack-github-action README; 8398a7/action-slack archive notice | high | Both sources agree |
| `8398a7/action-slack` archived 2025-09-13 | github.com/8398a7/action-slack (direct fetch) | high | Primary source; explicit archive notice |
| Outbound Slack requires `SLACK_WEBHOOK_URL` as the only new secret | api.slack.com/messaging/webhooks; slackapi/slack-github-action docs | high | Confirmed by both sources |
| MS Teams connectors deprecated; Power Automate is the replacement | learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook (updated 2025-06-10) | high | Primary Microsoft source; confirmed deprecation |
| Power Automate webhook URL is functionally equivalent to old connector URL | Microsoft Learn, same page | high | Described in the replacement instructions |
| Slack slash commands require 3-second HTTPS response | api.slack.com/interactivity/slash-commands | high | Slack developer documentation (partially fetched) |
| GitHub Actions workflow_dispatch latency exceeds 3 seconds | GitHub Actions queue behaviour; established community knowledge | medium | Not independently cited in a single source; derived from known Actions behaviour |
| GitHub issue → workflow inbound capture requires zero new secrets | Direct inference from `GITHUB_TOKEN` capability + `publish-wiki.yml` pattern | high | `GITHUB_TOKEN` with `contents: write` confirmed sufficient by wiki item |
| `publish-wiki.yml` trigger pattern is reusable | Direct file inspection: `.github/workflows/publish-wiki.yml` | high | Confirmed by reading the file |
| `src/wiki/publish.py` `load_frontmatter()` is reusable | Direct file inspection: `src/wiki/publish.py` | high | Confirmed by reading the file |
| Query-in-chat requires persistent bot server | 2026-03-02-chat-conversational-interface.md Key Finding 2; MCP stdio transport spec | high | Cross-confirmed by two sources |
| Per-item notification is correct default for personal system | Inference from user interaction model | medium | No independent source; derived from context |

### Assumptions

- **Assumption:** The owner uses either Slack or MS Teams personally (not as enterprise admin). **Justification:** The research question specifically asks about Slack and MS Teams; if the owner uses neither, the integration question is moot. This assumption is flagged as the top unknown.

- **Assumption:** The research loop continues to complete 3–5 items per run. **Justification:** Based on observed behaviour from prior loop runs; per-item notifications at this volume are not burdensome in a personal Slack channel.

- **Assumption:** The Power Automate webhook URL generated by the Teams flow is stable (does not rotate automatically). **Justification:** Microsoft's documentation does not indicate automatic rotation; the URL behaves like an API key — stable until explicitly deleted or regenerated.

### Analysis

Evidence weight: Slack Incoming Webhook documentation (api.slack.com) and the `slackapi/slack-github-action` README are primary sources with high authority. The MS Teams deprecation notice is a primary source from Microsoft Learn and is unambiguous. The `8398a7/action-slack` archive notice is a primary source. The GitHub Actions workflow_dispatch latency claim is an inference supported by general community knowledge but not a single citable source — it is the weakest link in the inbound capture analysis, though the direction of the conclusion (slack commands require a faster endpoint than Actions can provide) is well-established in practice.

The inbound capture analysis identifies three options and recommends Option A (GitHub issue proxy) on the basis that it requires no new credentials. Options B and C are documented but deferred pending owner approval. This is the conservative choice consistent with AGENTS.md constraints, not the most user-friendly choice — a Zapier bridge (Option B) would provide one-step Slack-to-backlog creation.

Digest vs. per-item is not a significant trade-off at the current research volume. Per-item is recommended as the default because it is simpler to implement (same trigger, no scheduling logic) and delivers findings immediately.

### Risks, Gaps, and Uncertainties

- **Owner's platform is unknown.** All recommendations require the owner to confirm which platform (Slack, Teams, or both) is in use before any implementation begins. Without this, the credential approval request cannot be scoped.
- **Slack slash command endpoint gap.** The 3-second acknowledgement requirement was noted in the Slack slash commands page but the full documentation was only partially fetched. The latency-based incompatibility with Actions is an inference, not a confirmed benchmark.
- **Power Automate dependency.** Teams webhook URLs via Power Automate depend on the user maintaining an active Power Automate flow. If the flow is disabled or the user's Power Automate environment is restricted by an enterprise policy, the integration breaks silently.
- **Notification payload design is unspecified.** The research identifies what metadata to include (title, tags, executive summary excerpt, wiki link) but does not specify the exact Block Kit JSON structure. This is implementation detail, not a research gap, but the payload must be validated against Slack's message size limits (not defined in this item).

### Open Questions

- **Which platform does the owner use — Slack, Teams, or both?** This is the prerequisite question for all implementation work. Recommend the owner answer this before any workflow is built. Could become a new backlog item: `2026-03-08-owner-platform-selection-chat-integration.md`, though it is more appropriate as a direct question to the owner.
- **Should the inbound GitHub issue workflow replace or extend the existing backlog item creation process?** If implemented, the issue-to-backlog workflow would create files automatically; the owner's current manual process would become optional.
- **Is digest mode wanted at all, or is per-item notification sufficient?** This is an owner preference question. No new backlog item needed — it can be decided when the notification workflow is implemented.

---

## Output

- Type: knowledge, backlog-item
- Description: Outbound webhook delivery design for both Slack and MS Teams; inbound capture via GitHub Issues proxy; credential inventory (`SLACK_WEBHOOK_URL` or `TEAMS_WEBHOOK_URL`); digest vs. per-item analysis; implementation blocked on owner's platform selection and credential approval.
- Links:
  - https://docs.slack.dev/tools/slack-github-action/sending-techniques/sending-data-slack-incoming-webhook/ (Slack GitHub Action incoming webhook docs)
  - https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook (MS Teams webhook — deprecation and Power Automate replacement)
  - https://github.com/slackapi/slack-github-action (official Slack GitHub Action repository)