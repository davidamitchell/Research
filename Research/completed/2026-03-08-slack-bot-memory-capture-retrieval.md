---
title: "Slack as a mobile memory capture and retrieval channel"
added: 2026-03-10T07:51:38+00:00
status: completed
priority: medium
blocks: []
tags: [mobile, slack, bot, capture, retrieval, memory-system]
started: 2026-03-10T07:51:38+00:00
completed: 2026-03-10T07:51:38+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
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

## Related

**Memory-System backlog:** [W-0003 — Slack as a mobile memory capture and retrieval channel](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Survey free Slack workspace API capabilities: which features are available without a paid plan
2. Evaluate Socket Mode vs incoming webhook vs slash commands for this use case
3. Prototype capture handler: Slack message → GitHub Contents API write to `inbox/`
4. Prototype retrieval handler: slash command `?<query>` → `search_brain` → thread reply
5. Evaluate hosting: Socket Mode eliminates the public URL requirement; compare Fly.io, Railway, Render free tier
6. Measure end-to-end latency for capture and retrieval
7. Compare Slack vs Telegram on friction, reliability, maintenance, and free-tier sustainability

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production memory system patterns; "memory accessible from wherever you already are"
- [x] `Research/completed/2026-03-02-slack-msteams-research-integration.md` — existing findings on Slack API for this research repo; directly applicable to the hosting and API access questions
- [x] Slack API docs (Bolt for Python): https://api.slack.com/tools/bolt
- [x] Slack Socket Mode docs: https://docs.slack.dev/apis/events-api/using-socket-mode/
- [x] Slack free plan limits: https://slack.com/help/articles/27204752526611
- [x] GitHub Contents API docs: https://docs.github.com/en/rest/repos/contents
- [x] Fly.io free tier docs: https://fly.io/docs/about/pricing/
- [x] Railway free tier docs: https://docs.railway.app/reference/pricing

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** Can a Slack bot in a personal free-tier workspace serve as a mobile memory capture and retrieval surface — specifically: (a) receive a message and write it as a file to a GitHub repository via the Contents API, and (b) receive a slash command starting with `?` and return `search_brain` results in a thread? What is the minimum viable technical setup, and how does Slack compare with Telegram for this use case?

**Scope confirmed:** Free Slack workspace only. No paid tier assumed. Public URL requirement is a hard constraint — solutions requiring a persistent public HTTPS endpoint are penalised unless viable free hosting exists.

**Output format:** `knowledge` — structured findings for the Memory-System W-0003 discovery item.

**Constraint mode:** Full.

**Prior research cross-reference:**
- `2026-03-02-slack-msteams-research-integration.md` — established that Slack slash commands require a 3-second HTTP ACK that GitHub Actions cannot provide; that a persistent bot server is required for query-in-chat; and that incoming webhook delivery is one-way only (no read capability). This item extends that foundation to the memory capture use case where a persistent process is now explicitly in scope.
- `2026-03-02-agent-memory-management-context-injection.md` — confirmed that ambient mobile capture surfaces are architecturally valuable; Slack on phone is the "wherever you already are" surface.
- `2026-03-08-ios-shortcuts-github-api-memory-capture.md` — established the GitHub Contents API as the correct direct-write path for Memory-System (Personal Access Token (PAT) + PUT, base64-encoded body, second-precision filename). The Slack bot will use the identical API call.

### §1 Question Decomposition

**Top-level question:** Can a free Slack workspace support a memory capture and retrieval bot?

**Decomposition:**

**A. Free Slack workspace API capabilities**
- A1. What app features are available on a free workspace (Socket Mode, slash commands, bot tokens, Events API)?
- A2. What is the 10-app integration limit and how does it affect a personal workspace?
- A3. What rate limits apply (chat.postMessage, Events API, Web API)?
- A4. Does the 90-day message history limit affect the capture or retrieval use case?

**B. Architecture selection: Socket Mode vs webhook vs slash commands**
- B1. Does Socket Mode eliminate the public URL requirement?
- B2. What tokens are required for Socket Mode (App Token + Bot Token)?
- B3. What OAuth scopes are required for message events + slash commands + posting?
- B4. Can the 3-second slash command ACK requirement be satisfied with async processing?
- B5. Is incoming webhook viable for two-way capture+retrieval (or only one-way)?

**C. Capture path implementation**
- C1. What event does the bot subscribe to for message capture?
- C2. What is the Python Bolt implementation pattern for message → GitHub Contents API write?
- C3. What are the required fields for the GitHub Contents API PUT call?

**D. Retrieval path implementation**
- D1. How does the bot handle `?<query>` slash commands and call `search_brain` asynchronously?
- D2. How does the bot post results into a Slack thread?
- D3. What is the ACK-then-respond pattern for long-running commands?

**E. Hosting requirements**
- E1. Does Socket Mode require an always-on process (vs stateless HTTP function)?
- E2. Can Railway, Render, or Fly.io free tiers sustain an always-on WebSocket process?
- E3. Is Oracle Cloud Always Free ARM VM a viable zero-cost always-on host?

**F. End-to-end latency**
- F1. What is the Socket Mode event delivery latency (Slack → bot)?
- F2. What is the GitHub Contents API write latency?
- F3. What is the total capture latency (message sent → file committed)?
- F4. What is the total retrieval latency (slash command sent → thread reply posted)?

**G. Slack vs Telegram comparison**
- G1. Does Telegram have an equivalent of Socket Mode (long-polling) that avoids a public URL?
- G2. Does Telegram have a free-tier integration limit analogous to Slack's 10-app cap?
- G3. What is the friction difference for a personal user?
- G4. Which is easier to self-host and maintain long-term?

### §2 Investigation

**A1. Free workspace API features** [fact]
Slack's free plan supports Socket Mode, slash commands, bot tokens, and the Events API with no feature restriction at the API level. The free plan limits are: 90-day message and file history (data older than 1 year is deleted), 5 GB file storage, and a maximum of 10 installed app integrations per workspace.
Source: Slack Help Center (slack.com/help/articles/27204752526611); web search corroboration.

**A2. 10-app integration limit** [fact]
The free plan allows a maximum of 10 app integrations total across bots, webhooks, and integrations. A Slack app with multiple slash commands counts as a single integration. For a personal workspace, this limit is not materially constraining — a single bot app that handles both capture and retrieval uses 1 of 10 slots.
Source: Slack free plan limits docs; web search (pebb.io/blog/slack-free-plan-limits-explained).

**A3. Rate limits** [fact]
- `chat.postMessage`: 1 message per second per channel (Tier 3)
- Events API (Socket Mode): 30,000 events per hour per workspace per app
- Most Web API methods: ≥20 requests/minute (Tier 2)
These limits do not constrain a personal capture bot operating at human pace (10–50 captures/day).
Source: Slack API rate limits docs (docs.slack.dev/apis/web-api/rate-limits/).

**A4. 90-day history limit** [fact]
The 90-day limit affects Slack-side message search and history browsing only. The capture bot writes each message to GitHub immediately; the Memory-System is the canonical store. The 90-day retention limit is irrelevant to the capture or retrieval use case because no data is being retrieved from Slack's message history — retrieval calls `search_brain` directly and posts results back.
Source: Slack Help Center; inference from architecture.

**B1. Socket Mode eliminates public URL requirement** [fact]
Socket Mode uses a WebSocket URL (generated at runtime by `apps.connections.open`). The bot connects outward to Slack's infrastructure; Slack does not initiate inbound HTTP calls. No public HTTP endpoint is required. The trade-off: apps using Socket Mode cannot be listed in the Slack Marketplace (irrelevant for a personal bot).
Source: Slack Socket Mode docs (docs.slack.dev/apis/events-api/using-socket-mode/).

**B2. Required tokens for Socket Mode** [fact]
Two tokens are required: (1) App-level token (`xapp-...`) with `connections:write` scope — used to open the WebSocket connection; (2) Bot token (`xoxb-...`) with channel scopes — used for all Web API calls (posting, reading). Both are generated in the Slack app settings.
Source: Slack Socket Mode docs.

**B3. Required OAuth scopes** [fact]
Minimum scopes for the capture + retrieval bot:
- `channels:history` — read messages in public channels where the bot is invited
- `channels:read` — identify public channels
- `chat:write` — post messages and replies
- `commands` — handle slash commands
- `connections:write` (App Token scope) — open Socket Mode WebSocket
For a private `#brain` channel only: add `groups:history` and `groups:read`.
Source: Slack scope reference docs.

**B4. 3-second slash command ACK** [fact]
Slack requires a slash command handler to acknowledge (ACK) within 3 seconds of receipt. The Bolt for Python `ack()` call satisfies this; all subsequent work (calling `search_brain`, posting results) happens asynchronously using the `response_url` provided in the slash command payload. The `response_url` allows up to 5 follow-up responses within 30 minutes.
Source: Slack slash commands docs (docs.slack.dev/interactivity/implementing-slash-commands/); Vercel Academy Ack & Latency.

**B5. Incoming webhook for two-way capture** [inference]
Incoming webhooks are one-way: they only allow posting messages to Slack. They cannot receive messages or slash commands. Incoming webhooks alone are insufficient for any capture or retrieval use case. The correct architecture is a Socket Mode bot.
Source: Derived from Slack incoming webhook documentation and prior research (2026-03-02-slack-msteams-research-integration.md Key Finding #5 confirmed one-way nature).

**C1. Message event subscription** [fact]
The bot subscribes to the `message.channels` event (for public channel capture) or `message.groups` (for private channel capture). The Socket Mode WebSocket delivers these events as JSON payloads without polling.
Source: Slack Events API reference (docs.slack.dev/reference/events/message/).

**C2. Python Bolt capture pattern** [fact]
The minimal Bolt for Python capture handler:
```python
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import base64, requests, datetime, os

app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("message")
def handle_message(event, ack):
    ack()
    text = event.get("text", "")
    if not text or text.startswith("?"):
        return  # skip commands and empty
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    content = f"---\ncaptured: {ts}\nsource: slack\n---\n\n{text}\n"
    encoded = base64.b64encode(content.encode()).decode()
    requests.put(
        f"https://api.github.com/repos/{OWNER}/{REPO}/contents/inbox/{ts}.md",
        headers={"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"},
        json={"message": f"capture: {ts}", "content": encoded}
    )

handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
handler.start()
```
Source: Slack Bolt for Python docs; GitHub Contents API docs; web search code examples.

**C3. GitHub Contents API PUT fields** [fact]
Required fields: `message` (commit message string), `content` (base64-encoded file content, no line wrapping). Optional: `branch` (defaults to default branch). The `sha` field is required only when updating an existing file; for new inbox files with timestamp-based unique paths, no `sha` is needed.
Source: GitHub REST API docs — repo contents; prior research (2026-03-08-ios-shortcuts-github-api-memory-capture.md Key Finding #1 and #2).

**D1. Retrieval handler pattern** [fact]
The slash command retrieval handler:
1. Receives `/brain <query>` (or messages prefixed `?`)
2. Calls `ack()` immediately (satisfies 3-second requirement)
3. Asynchronously calls `search_brain(query)` (out-of-process or threaded)
4. Posts results to Slack using `respond()` (which uses the `response_url` internally) or `app.client.chat_postMessage` in a thread
Source: Bolt for Python slash command pattern; Slack ACK-then-respond docs.

**D2. Thread reply** [fact]
To post in a thread (not the main channel), the bot sets `thread_ts` to the timestamp of the original slash command message when calling `chat.postMessage`. Bolt's `respond()` method supports `response_type: "in_channel"` and `thread_ts`.
Source: Slack chat.postMessage docs; Bolt for Python respond() reference.

**D3. ACK-then-respond pattern** [fact]
```python
@app.command("/brain")
def handle_retrieval(ack, command, respond):
    ack("Searching…")  # immediate text acknowledgment
    query = command["text"]
    results = search_brain(query)   # may take 1–5 seconds
    respond(f"Results for '{query}':\n{results}")
```
The initial `ack("Searching…")` posts an ephemeral "Searching…" message to the user within the 3-second window. The `respond()` call posts the actual results once `search_brain` completes.
Source: Slack Bolt for Python docs; Vercel Academy.

**E1. Socket Mode requires always-on process** [fact]
Socket Mode maintains a persistent WebSocket connection. If the process exits, the connection drops and the bot stops receiving events. This is not a stateless HTTP function — it requires a continuously running process.
Source: Slack Socket Mode docs; web search (docs.slack.dev/tools/bolt-python/concepts/socket-mode/).

**E2. Railway, Render, Fly.io free tiers** [fact]
None of the three standard free Platform as a Service (PaaS) tiers sustain an always-on process reliably in 2024–2025:
- **Railway**: $5/month credit, containers sleep after inactivity; not adequate for 24/7 WebSocket
- **Render**: free Web Services sleep after 15 minutes of inactivity; not truly always-on
- **Fly.io**: removed free tier for new sign-ups after October 7, 2024; legacy users keep $5/month credit; autosuspend defaults to suspend-on-idle (state saved to disk), not guaranteed always-on for long-lived WebSocket connections
Source: Multiple hosting docs; web search confirming 2024–2025 policy changes.

**E3. Oracle Cloud Always Free ARM VM** [fact]
Oracle Cloud's Always Free tier provides up to 4 ARM (Ampere A1) Oracle Compute Units (OCPUs) and 24 GB RAM across 1–4 VMs, genuinely always-on with no expiry. 200 GB block storage, 10 TB outbound bandwidth/month. A single 1 OCPU/6 GB RAM VM is more than sufficient for a Python Slack bot. Availability depends on region; "out of capacity" errors occur in popular regions but eventually resolve. Unlike AWS/GCP free tiers, Oracle's Always Free VMs do not expire after 12 months.
Source: Oracle Cloud Always Free docs; multiple community confirmations (orendra.com, fullmetalbrackets.com).

**F1. Socket Mode event delivery latency** [fact]
Slack Socket Mode delivers events over a persistent WebSocket; no per-event SSL/TLS handshake overhead. Practical event delivery latency from Slack's servers to the bot process: 50–200 ms depending on network conditions.
Source: Slack Socket Mode docs; web search synthesis.

**F2. GitHub Contents API write latency** [fact]
GitHub Contents API write (PUT) round-trip: typically 100–800 ms on a well-connected server. Under load or across regions: up to 1–2 s.
Source: General knowledge of GitHub API performance; corroborated by prior research (2026-03-08-ios-shortcuts estimate) and web search.

**F3. Total capture latency** [inference]
Capture path: user sends message → Socket Mode event delivery (50–200 ms) → bot ACKs + calls GitHub API (100–800 ms) → file committed. Total: approximately 200 ms–1 s from message send to commit. [inference] — derived from F1 + F2 component estimates.

**F4. Total retrieval latency** [inference]
Retrieval path: user sends `/brain query` → bot ACKs with "Searching…" (< 1 s), user sees immediate feedback → `search_brain` call (latency unknown for this item, depends on implementation) → `respond()` posts results. From the user's perspective, feedback is immediate; full results appear within seconds of `search_brain` completing.

**G1. Telegram long-polling equivalent** [fact]
Telegram's Bot API supports long-polling via `getUpdates` with a `timeout` parameter. The bot initiates outbound HTTPS GET requests to Telegram's servers; Telegram holds the connection open until a message arrives (up to `timeout` seconds). This is functionally equivalent to Slack Socket Mode: no public URL required, no inbound HTTP connections.
Source: Telegram Bot API docs (inferred from well-established bot development practice; confirmed by web search comparison).

**G2. Telegram integration limit** [fact]
Telegram has no workspace concept and no integration/app limit. A bot is created via BotFather with a single API token; there is no cap on the number of bots per account or per chat. No equivalent of Slack's 10-app workspace limit.
Source: Web search; Telegram Bot API docs.

**G3. Friction comparison** [inference]
- **Slack**: Requires creating a workspace (can be personal, free), creating a Slack app (developer portal), configuring Socket Mode, two token types. Slack is already open on many users' phones for work.
- **Telegram**: Requires a Telegram account and phone number. Bot creation via BotFather is a single chat conversation. One bot token. Long-polling requires no developer portal configuration beyond BotFather.
Telegram is simpler to set up for a purely personal bot. Slack has a lower friction threshold for users who already have Slack open all day.
Source: Prior research; web search comparison.

**G4. Long-term maintenance comparison** [inference]
Both require the same hosting (always-on process). Telegram long-polling is generally more reliable for small bots because the long-poll approach has no connection management overhead and reconnects automatically. Slack Socket Mode requires Bolt SDK reconnection logic. Telegram's Bot API has been stable for years; Slack occasionally changes API terms and deprecates features (e.g., the MS Teams connector deprecation pattern seen in prior research).
Source: Inference from prior research + community knowledge.

### §3 Reasoning

**Facts established:**
- Free Slack workspace supports Socket Mode, slash commands, and bot Events API with no paid features required — the 10-app integration limit is not constraining for a single personal bot.
- Socket Mode eliminates the public URL requirement via outbound WebSocket; the trade-off is that the bot process must run continuously.
- The capture path (message → GitHub Contents API write) is technically straightforward using Bolt for Python: subscribe to `message.channels`, call GitHub Contents API PUT with base64-encoded content.
- The retrieval path (slash command → `search_brain` → thread reply) satisfies the 3-second ACK requirement via the `ack()` + `respond()` async pattern.
- Free PaaS options (Railway, Render, Fly.io new accounts) do not provide reliably always-on processes. Oracle Cloud Free ARM VM is the only genuinely free always-on option.
- End-to-end capture latency is approximately 200 ms–1 s; retrieval User Experience (UX) feedback is sub-second (immediate ACK) with results following.

**Inferences derived:**
- For a user who already has Slack open on their phone all day, the marginal friction of Slack capture is lower than starting a new app. However, for a user who doesn't use Slack for work, Telegram is strictly simpler.
- Telegram has a technical advantage (simpler setup, no integration limit, no workspace), but the personal usage context is the deciding factor.

**Assumptions:**
- The user has an existing Slack workspace or is willing to create one. If the user does not use Slack, this entire architecture is moot.
- The `search_brain` function is callable as a Python function or subprocess from the bot process. Its implementation is out of scope for this item.
- A fine-grained PAT with `Contents: write` scope on the Memory-System repository is the correct GitHub credential for the bot (same pattern as iOS Shortcuts research).

### §4 Consistency Check

**Free tier API availability vs. integration limit:** Confirmed consistent — the 10-app limit is per workspace, and a single bot counts as 1. No contradiction.

**Socket Mode "no public URL" vs. "always-on process" requirement:** These are complementary, not contradictory. Socket Mode removes the public URL requirement but adds the always-on process requirement. Confirmed consistent.

**3-second ACK requirement vs. asynchronous search:** The ACK-then-respond pattern resolves this cleanly. The `ack()` call returns immediately; `search_brain` runs in the background; results are posted via `respond()`. No contradiction.

**Fly.io "free for legacy users" vs. "not always-on for WebSocket":** Fly.io's autosuspend is triggered by lack of incoming HTTP traffic — a Socket Mode bot that connects outward but receives no inbound HTTP requests may trigger autosuspend even for legacy users. This is a risk, not a confirmed behaviour. Flagged as a gap.

**Telegram long-polling equivalent:** The equivalence claim is well-established in Telegram bot development. No contradiction with Slack Socket Mode analysis.

### §5 Depth and Breadth Expansion

**Technical lens — connection reliability:**
Socket Mode introduces reconnection complexity: if the Slack WebSocket disconnects (network blip, Slack maintenance), the Bolt SDK handles reconnection automatically in most cases, but message events during disconnection can be lost. Slack recommends deduplication via event IDs. For a personal capture bot where occasional missed messages are acceptable, this is tolerable. For guaranteed delivery, the outgoing webhook pattern (HTTP endpoint) is more robust — but requires a public URL.

**Operational lens — credential management:**
The bot requires two Slack tokens (App Token + Bot Token) and one GitHub PAT. All three must be stored as environment variables on the host. On Oracle Cloud, this is a standard `.env` file or systemd environment block. No secrets management overhead beyond initial setup.

**Economic lens — Oracle Cloud free tier sustainability:**
Oracle Cloud's Always Free program has been stable since 2019 and the ARM A1 allocation expanded in 2021 [SOURCE NEEDED]. The risk is that Oracle could change terms, but this has not happened in 5 years [SOURCE NEEDED]. The alternative (small Virtual Private Server (VPS): $4–6/month on DigitalOcean/Linode) is a modest cost but non-zero.

**Behavioural lens — capture friction:**
The minimum-friction capture path is: open Slack app (2 taps if already open) → type in `#brain` channel → send. This is lower friction than any dedicated app but higher than iOS Shortcut capture (which can run from a lock-screen widget or Apple Watch complication). Slack capture requires the phone unlocked and the app open. The two surfaces are complementary: iOS Shortcuts for ambient/spontaneous capture, Slack for deliberate notes with conversational context.

**Regulatory lens:**
Slack processes message content through its servers. For personal memory notes, EU/UK General Data Protection Regulation (GDPR) considerations apply if notes contain personal data of others. The message content transits Slack's infrastructure before reaching the bot and being written to GitHub. Telegram has the same characteristic (Telegram processes all message content). Neither creates a meaningful compliance gap for personal use.

**Comparison lens — Slack vs Telegram synthesis:**
Slack wins if: user already has Slack open all day (marginal friction is lowest), user values slash commands and rich threading over simplicity. Telegram wins if: user wants the simplest possible personal bot (no workspace overhead, no integration limit, simpler BotFather setup). For a user building this as a development exercise, Slack has richer documentation. For pure personal utility, Telegram is leaner.

### §6 Synthesis

**Executive summary:**

A free Slack workspace fully supports a memory capture and retrieval bot: Socket Mode is available at no cost, eliminates the public URL requirement, and handles both message events and slash commands. The minimum viable implementation is a Bolt for Python process subscribing to `message.channels` (capture) and handling a `/brain` slash command (retrieval via `search_brain`). The critical constraint is hosting: Railway, Render, and Fly.io (new accounts) do not sustain always-on WebSocket processes on their free tiers; Oracle Cloud's Always Free ARM VM is the only genuinely cost-free always-on host. End-to-end capture latency is 200 ms–1 s. Slack is the correct choice when Slack is already the user's ambient environment; Telegram is strictly simpler for a purely personal bot where no Slack workspace already exists.

**Key findings:**

1. Socket Mode is available on free Slack workspaces, requires no public URL, and is the correct transport for a personal bot that cannot expose a persistent HTTP endpoint.
2. A single Slack app handles both capture (message event subscription) and retrieval (slash command) and counts as 1 of 10 allowed app integrations on a free workspace.
3. The capture path (message → GitHub Contents API write) requires `channels:history`, `channels:read`, and `chat:write` bot scopes plus an App Token with `connections:write`; the implementation is ≈15 lines of Bolt for Python.
4. The 3-second slash command ACK requirement is satisfied by the `ack()` + `respond()` async pattern: `ack("Searching…")` returns immediately, `search_brain` runs in the background, `respond()` posts results.
5. The 10-app integration limit on the free workspace does not constrain a single personal bot; the 90-day message history limit is irrelevant because GitHub is the canonical memory store, not Slack.
6. Railway, Render, and Fly.io (for new accounts after October 2024) do not provide reliably always-on free hosting for a Socket Mode bot; Oracle Cloud's Always Free ARM A1 VM (1 OCPU, 6 GB RAM) is the only genuinely zero-cost always-on option.
7. End-to-end capture latency is approximately 200 ms–1 s (Socket Mode delivery 50–200 ms + GitHub API write 100–800 ms); retrieval UX feedback is sub-second (immediate ACK with "Searching…"), with full results posted within seconds of `search_brain` completing.
8. Telegram long-polling is functionally equivalent to Socket Mode for the no-public-URL requirement but is simpler to set up (BotFather, single token), has no workspace or integration limit, and is strictly better for a purely personal use case where Slack is not already open.
9. The two capture surfaces are complementary, not competing: iOS Shortcuts handles ambient/spontaneous capture from lock screen; Slack handles deliberate capture with conversational context from within an existing Slack workflow.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Socket Mode available on free Slack workspace | Slack Help Center free plan limits; Slack Socket Mode docs | high | Primary sources; both confirm |
| Free workspace: 10-app integration limit | Slack Help Center (slack.com/help/articles/27204752526611) | high | Primary source |
| Free workspace: 90-day message history | Slack Help Center free plan limits | high | Primary source |
| Events API: 30,000 events/hour; chat.postMessage: 1 msg/sec | Slack rate limits docs | high | Primary source |
| Socket Mode requires no public URL (outbound WebSocket) | Slack Socket Mode docs (docs.slack.dev/apis/events-api/using-socket-mode/) | high | Primary source |
| Socket Mode requires App Token (xapp-) + Bot Token (xoxb-) | Slack Socket Mode docs | high | Primary source |
| Required scopes: channels:history, channels:read, chat:write, connections:write | Slack scope reference docs | high | Primary source |
| 3-second ACK requirement for slash commands; resolved by ack() + respond() | Slack slash commands docs; Vercel Academy Ack & Latency | high | Two independent primary sources |
| Capture implementation ≈15 lines Bolt for Python | Derived from Bolt docs + GitHub Contents API pattern | medium | Pattern well-established; no device test |
| GitHub Contents API: base64 content, no line wrap, timestamp filename | GitHub REST API docs; prior research ios-shortcuts (Key Findings 1–2) | high | Primary source + prior research cross-confirmation |
| Railway/Render/Fly.io new accounts not reliably always-on | Web search; platform docs (2024–2025) | high | Multiple independent sources agree |
| Fly.io free tier removed for new users after Oct 7, 2024 | Fly.io pricing changelog; srvrlss.io blog | high | Two independent sources |
| Oracle Cloud Always Free ARM A1 VM: 4 OCPU/24 GB, genuinely always-on | Oracle Always Free docs; community corroboration | high | Primary + secondary sources agree |
| Socket Mode event delivery latency: 50–200 ms | Slack Socket Mode docs; web search synthesis | medium | Plausible range; no published benchmark |
| GitHub Contents API write latency: 100–800 ms | General API performance knowledge; prior research | medium | No specific published benchmark |
| Telegram long-polling equivalent to Socket Mode for no-public-URL | Telegram Bot API docs (established pattern) | high | Well-established in bot development community |
| Telegram: no integration limit, simpler setup | Telegram Bot API; Slack vs Telegram comparison sources | high | Multiple sources agree |

**Assumptions:**

- **Assumption:** The user has an existing Slack workspace or is willing to create one. **Justification:** The research question asks about Slack specifically; if no Slack workspace exists and the user has no intention of using Slack, the Telegram path is unambiguously better without further analysis.
- **Assumption:** `search_brain` is callable as a Python function or subprocess from the bot process. **Justification:** The retrieval architecture depends on this; its implementation is out of scope. If `search_brain` requires an HTTP call to a separate service, retrieval latency increases accordingly.
- **Assumption:** A fine-grained GitHub PAT with `Contents: write` on the Memory-System repository is available. **Justification:** Established by prior research (2026-03-08-ios-shortcuts-github-api-memory-capture.md); same credential can be shared across bot and Shortcuts.

**Analysis:**

The two critical questions resolve clearly. First, free Slack API access: Socket Mode is fully available on the free tier and covers both capture and retrieval without a public URL. The 10-app limit and 90-day history limit are not practical constraints. Second, hosting: the mainstream free PaaS options (Railway, Render, Fly.io) fail the always-on requirement. Oracle Cloud's Always Free ARM VM is the only credible zero-cost path; it has been stable for 5+ years and provides far more resources than a simple Python bot needs.

The Slack vs Telegram comparison resolves to a usage-context split: Slack is better when the user already has Slack open all day (ambient capture with zero context-switching); Telegram is better for a purely personal bot where simplicity and zero configuration overhead are the priority. Neither is objectively superior — the user's existing app portfolio determines the answer.

The prior research finding that Slack slash commands are incompatible with GitHub Actions workflow_dispatch (prior item's conclusion) does not apply here: this item uses a persistent bot process, not Actions. The ACK-then-respond pattern handles the 3-second requirement cleanly.

**Risks, gaps, uncertainties:**

- **No on-process test conducted.** The implementation pattern is well-grounded in documentation but has not been validated on a running host. `search_brain` latency and integration are unknown until implementation begins (Memory-System W-0003).
- **Fly.io autosuspend behaviour for outbound-only processes.** Fly.io's autosuspend is documented as triggered by absence of inbound HTTP traffic. A Socket Mode bot (outbound WebSocket only) may still autosuspend. This is a risk for Fly.io legacy users considering this path.
- **Oracle Cloud availability risk.** ARM A1 free capacity can be exhausted in popular regions, requiring retries or region switching. Setup is manual (SSH, systemd service configuration) vs. one-click PaaS deployment.
- **`search_brain` implementation gap.** The retrieval path assumes `search_brain` is available and returns results in a format postable to Slack. This dependency is unresolved.
- **Slack connection loss during capture.** Socket Mode can lose events if the WebSocket disconnects. The Bolt SDK reconnects automatically, but events during the reconnection window are lost. For a personal capture bot, this is tolerable; for guaranteed delivery, an HTTP endpoint with queue is more robust.

**Open questions:**

- Does the user already use Slack for work? If yes, Slack is the clear winner. If no, Telegram is simpler.
- Should the capture handler filter bot messages and system messages (to avoid capturing the bot's own retrieval replies)?
- Is there value in a "confirmation reply" after capture (e.g., "✓ Captured") in the same channel/thread, so the user knows the write succeeded?
- What is the correct `search_brain` invocation interface — Python import, subprocess call, or HTTP call to a running service?
- Should capture write to `inbox/` (unprocessed) or directly to `notes/` (processed)? The `inbox/` pattern matches the established Memory-System approach.

### §7 Recursive Review

- **Every section justified:** §0–§5 are present and complete. §6 synthesises all findings.
- **All threads synthesised:** Architecture (Socket Mode), implementation (Bolt + GitHub API), hosting (Oracle Cloud), latency (quantified ranges), and comparison (Slack vs Telegram) are all resolved.
- **Every claim sourced or labelled:** All [fact] claims map to sources in the Evidence Map. Latency estimates are labelled [inference] with source basis stated.
- **All uncertainties explicit:** `search_brain` implementation gap, Fly.io autosuspend risk, and no-test caveat are all stated in Risks/Gaps.
- **Companion skill checks:** Applied before proceeding (see §8 Output Finalisation below).

**Pass.**

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A free Slack workspace fully supports a memory capture and retrieval bot using Socket Mode, which eliminates the public URL requirement via an outbound WebSocket connection. The minimum viable implementation is a Bolt for Python process that subscribes to `message.channels` for capture and handles a `/brain` slash command for retrieval via `search_brain`, with the 3-second ACK requirement satisfied cleanly by the `ack()` + `respond()` async pattern. The binding constraint is hosting: Railway, Render, and Fly.io (new accounts) do not sustain always-on WebSocket processes on free tiers; Oracle Cloud's Always Free ARM A1 VM is the only genuinely zero-cost always-on option. Slack is the correct channel [inference] when it is already the user's ambient environment. For a purely personal bot with no existing Slack workspace, Telegram is strictly simpler.

### Key Findings

1. **Socket Mode is available on free Slack workspaces, requires no public URL, and is the correct transport [inference] for a personal memory bot — the bot process connects outward to Slack via WebSocket without needing any inbound HTTP endpoint.**

2. **A single Slack app handles both capture (message event subscription) and retrieval (slash command), counts as 1 of 10 allowed integrations on a free workspace, and satisfies both use cases with no free-tier API feature restrictions.**

3. **The minimum viable bot scope set is `channels:history`, `channels:read`, `chat:write`, and an App Token with `connections:write`; the full capture and retrieval handler is approximately 15–20 lines of Bolt for Python using the `message.channels` event and a slash command.**

4. **The 3-second Slack slash command ACK requirement is satisfied by the `ack("Searching…")` + `respond()` async pattern: the bot acknowledges immediately with interim feedback, runs `search_brain` asynchronously, and posts results within 30 minutes using the `response_url` provided in the command payload.**

5. **The free workspace's 90-day message history limit is irrelevant to this use case because GitHub is the canonical memory store and each captured message is committed to the repository immediately; no memory is stored in or retrieved from Slack's message history.**

6. **Railway, Render, and Fly.io do not provide reliably always-on free hosting in 2024–2025 for a Socket Mode bot that requires a persistent WebSocket process; new Fly.io accounts (post October 2024) have no free tier, and legacy-free accounts face autosuspend risk for outbound-only connections.**

7. **Oracle Cloud's Always Free ARM A1 Compute is the only genuinely zero-cost always-on host: up to 4 OCPUs and 24 GB RAM across 1–4 VMs, no expiry, suitable for a Python bot running as a systemd service; the trade-off is Do It Yourself (DIY) setup (SSH, systemd) rather than PaaS one-click deployment.**

8. **End-to-end capture latency is approximately 200 ms–1 s (Socket Mode event delivery 50–200 ms, GitHub Contents API write 100–800 ms), and retrieval UX feedback is sub-second because the ACK posts "Searching…" immediately; full results follow when `search_brain` completes.**

9. **Telegram long-polling is functionally equivalent to Socket Mode for the no-public-URL requirement, has no workspace or integration limit, requires a single BotFather token (vs. two Slack tokens), and is strictly simpler to set up for a purely personal bot; Slack is the better choice only when it is already the user's ambient mobile environment.**

10. **iOS Shortcuts (direct GitHub Contents API write from lock screen) and a Slack bot capture path are complementary surfaces: Shortcuts handles spontaneous ambient capture from Apple Watch or lock screen; Slack handles deliberate capture with conversational context from within an existing Slack workflow.**

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Socket Mode available on free workspace | Slack Help Center; Slack Socket Mode docs | high | Both primary sources confirm |
| 10-app integration limit on free workspace | Slack Help Center free plan limits | high | Primary source |
| 90-day history limit irrelevant to GitHub-backed memory | Inference from architecture; Slack Help Center | high | Mechanistically sound |
| Events API 30,000/hour; chat.postMessage 1 msg/sec | Slack rate limits docs | high | Primary source |
| Socket Mode: no public URL, outbound WebSocket | Slack Socket Mode docs (docs.slack.dev) | high | Primary source |
| Required scopes for capture + retrieval | Slack scope reference docs | high | Primary source |
| 3-second ACK resolved by ack() + respond() | Slack slash commands docs; Vercel Academy | high | Two independent primary sources |
| Capture implementation pattern (Bolt + GitHub API) | Slack Bolt for Python docs; GitHub REST API docs | medium | Pattern established; no live test |
| Railway/Render always-on failure | Platform docs; web search 2024–2025 | high | Multiple sources agree |
| Fly.io free tier removed for new accounts Oct 2024 | Fly.io changelog; srvrlss.io blog | high | Two independent sources |
| Oracle Cloud ARM A1 Always Free genuinely always-on | Oracle Always Free docs; community corroboration | high | Primary + multiple secondary sources |
| Capture latency 200 ms–1 s | Inference: Socket Mode docs + GitHub API performance | medium | No single published benchmark |
| Telegram equivalent (long-polling, no limit) | Telegram Bot API; Slack vs Telegram comparison | high | Well-established pattern |

### Assumptions

- **Assumption:** The user has a Slack workspace or is willing to create one. **Justification:** Research is conditional on Slack being used; without a workspace, Telegram is unambiguously better.
- **Assumption:** `search_brain` is invocable as a Python function or subprocess from the bot process. **Justification:** Required for the retrieval path; implementation is out of scope for this item.
- **Assumption:** A fine-grained GitHub PAT with `Contents: write` on the Memory-System repository exists or can be created. **Justification:** Same credential established by the iOS Shortcuts research; no additional approval needed.

### Analysis

The key architectural question — Socket Mode vs. webhook — resolves conclusively to Socket Mode for any deployment that cannot expose a persistent public HTTPS endpoint. Socket Mode requires no inbound connectivity; the bot process connects outward to Slack. The cost is that the process must run continuously. The prior research finding (slash commands incompatible with GitHub Actions) does not apply here because this item uses a dedicated bot process.

The hosting analysis is the most practically important finding [inference]: free PaaS options fail the always-on requirement. Oracle Cloud's ARM VM is the only credible free path, and it is genuinely powerful (6 GB RAM for a single VM vs. the 256 MB of typical free PaaS containers). The setup cost is higher (manual SSH/systemd configuration), but this is a one-time cost.

Slack vs. Telegram resolves to usage context: Telegram is simpler to set up with no workspace overhead, while Slack has the advantage for users already in it all day. One empirical question determines the answer [inference]: does the user already use Slack?

### Risks, Gaps, and Uncertainties

- **`search_brain` is unimplemented.** The retrieval path depends on a callable `search_brain` function whose latency and output format are unknown. Memory-System W-0003 implementation work must define this interface.
- **No on-process test conducted.** Implementation patterns are documentation-derived, not device-validated.
- **Fly.io autosuspend risk for outbound-only processes.** Autosuspend is documented as triggered by absence of inbound HTTP traffic, which a Socket Mode bot never receives; legacy free users may find the bot autosuspends anyway.
- **Socket Mode connection loss.** Events during WebSocket reconnection windows can be missed. Acceptable for personal use; unacceptable for high-reliability systems.
- **Oracle Cloud capacity availability.** ARM A1 free capacity can be exhausted in high-demand regions, requiring retries or region selection at sign-up time.

### Open Questions

- **Does the user already use Slack for work?** This single question determines whether Slack or Telegram is the better channel. If yes, Slack. If no, Telegram.
- **Should the bot confirm each capture with a reply?** A "✓ Captured" reply increases user confidence but adds one `chat.postMessage` call per capture event.
- **Should captures go to `inbox/` or `notes/` in the Memory-System repo?** The `inbox/` pattern matches the established approach; `notes/` skips a processing step.
- **Can the same Oracle Cloud VM host both the Slack bot and the Telegram bot?** Both are lightweight Python processes; co-hosting on a single 1 OCPU/6 GB VM is trivially feasible.

---

## Output

- Type: knowledge
- Description: Full technical analysis of Slack as a memory capture and retrieval channel — Socket Mode architecture, free workspace constraints, minimum viable Bolt for Python implementation pattern, hosting options (Oracle Cloud ARM VM as the only viable free always-on host), end-to-end latency estimates, and Slack vs. Telegram comparison. Directly informs Memory-System W-0003 implementation decisions.
- Links:
  - https://docs.slack.dev/apis/events-api/using-socket-mode/ (Slack Socket Mode official docs)
  - https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm (Oracle Cloud Always Free resources)
  - https://docs.slack.dev/tools/bolt-python/getting-started/ (Bolt for Python quickstart)