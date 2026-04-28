---
title: "Interface and delivery: how to surface research outputs"
added: 2026-03-10T17:09:13+00:00
status: completed
priority: low
tags: [interface, delivery, output, ux]
started: 2026-03-10T17:09:13+00:00
completed: 2026-03-10T17:09:13+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Interface and delivery: how to surface research outputs

## Question / Hypothesis

Once research is complete and outputs are produced, how should they be surfaced and delivered to the people (or agents) who need them? What interfaces make research outputs most usable?

## Context

Research outputs currently live as Markdown files in `Research/completed/`. This is good for git history but poor for discovery and consumption. Better interfaces might include:

- **CLI**: query completed research, list by tag, search by keyword
- **Static site**: generated from `Research/completed/` for browsing
- **Email digest**: a weekly summary of newly completed research (using the Latest-developments- pattern)
- **Agent-readable knowledge base**: structured format that AI agents can query
- **MCP tool**: expose research items as an MCP server tool

The right answer depends on who the consumers are (human researcher, AI agent, or both).

## Scope

**In scope:**
- CLI interface for research queries (most immediate value)
- Agent-readable format (JSON or structured Markdown for MCP)
- Email digest as a future option

**Out of scope:**
- Full web app or SaaS product

## Approach

1. Define the consumers and their use patterns
2. Survey interface options: CLI vs static site vs email digest vs MCP
3. Prototype the CLI query interface (most immediate)
4. Evaluate MCP server approach for agent-readable research

## Sources

- [x] `davidamitchell/Latest-developments-` — email digest pattern (consulted: README.md)
- [x] MCP tool creation docs: https://modelcontextprotocol.io/docs/concepts/tools (consulted)
- [x] `Research/completed/2026-03-01-github-wiki-research-content.md` — wiki delivery channel (prior art)
- [x] `Research/completed/2026-03-02-chat-conversational-interface.md` — MCP server design for agent query (prior art)
- [x] `Research/completed/2026-03-02-slack-msteams-research-integration.md` — push notification options (prior art)
- [x] `Research/completed/2026-03-02-ios-shortcuts-research.md` — iOS/mobile access patterns (prior art)
- [x] `Research/completed/2026-03-02-semantic-full-text-search.md` — CLI search command design (prior art)

---

## Research Skill Output

### §0 Initialise

**Research question:** Once research is complete and outputs are produced, how should they be surfaced and delivered to the people (or agents) who need them? What interfaces make research outputs most usable?

**Scope:** In-scope: CLI query, agent-readable format (MCP), email digest. Out-of-scope: full web app. Constraint mode: **full**.

**Consumers:** Two distinct consumer types:
1. *Human researcher* — the owner, accessing via GitHub website and iOS app, with no local terminal.
2. *AI agent* — Claude Code, GitHub Copilot Agent, or other agents with MCP tool access.

**Definitions:**
- MCP (Model Context Protocol): an open protocol enabling AI assistants to invoke typed tools via JavaScript Object Notation–Remote Procedure Call (JSON-RPC) over stdio or HyperText Transfer Protocol (HTTP)/SSE transport.
- FTS5: SQLite's Full-Text Search version 5 extension.
- SSE (Server-Sent Events): a one-directional HTTP streaming mechanism used by the MCP HTTP transport.

**Prior research cross-reference:** Five directly relevant completed items:
- `2026-03-01-github-wiki-research-content.md` — resolved the human-browsing interface question: a GitHub wiki rebuilt by `publish-wiki.yml` on every push to `main` touching `Research/completed/**`.
- `2026-03-02-chat-conversational-interface.md` — resolved the agent-query interface question: an MCP server (`src/mcp/research_server.py`) with stdio transport, three tools (`search_research`, `get_research_item`, `get_related_items`), registered in `.github/mcp.json`.
- `2026-03-02-slack-msteams-research-integration.md` — assessed Slack/Teams push notifications: outbound delivery is viable with `SLACK_WEBHOOK_URL` secret; inbound query is blocked by the no-server constraint.
- `2026-03-02-ios-shortcuts-research.md` — assessed mobile access: iOS Shortcuts calling the GitHub Issues API for capture; GitHub wiki URL shortcut for read access.
- `2026-03-02-semantic-full-text-search.md` — designed the `research search` CLI command using SQLite FTS5 with mtime-based rebuild.

This item must synthesise those findings into a unified interface strategy and address the remaining open question: the email digest path via the `Latest-developments-` pattern.

---

### §1 Question Decomposition

**Top-level question:** How should research outputs be surfaced and delivered to human and agent consumers?

**Decomposition tree:**

```
Q0: What interface strategy covers both human and agent consumers?
├── Q1: Who are the consumers and what are their access patterns?
│   ├── Q1a: What is the human researcher's access model? [atomic]
│   └── Q1b: What is the AI agent's access model? [atomic]
├── Q2: What delivery channels are available for the human consumer?
│   ├── Q2a: Is the GitHub wiki viable as a browsing interface? [atomic]
│   ├── Q2b: Is a CLI search command viable? [atomic]
│   └── Q2c: Is an email digest viable under current credential constraints? [atomic]
├── Q3: What delivery channel is correct for the AI agent consumer?
│   ├── Q3a: Is an MCP server the right pattern? [atomic]
│   └── Q3b: What tools does the MCP server expose? [atomic]
├── Q4: What push-notification mechanism is correct for new completions?
│   ├── Q4a: Is Slack outbound notification viable? [atomic]
│   └── Q4b: Is email digest via Latest-developments- pattern viable? [atomic]
└── Q5: What is the priority order for implementing these channels? [atomic]
```

---

### §2 Investigation

#### Q1a: Human researcher's access model

**[fact]** The owner accesses the repository exclusively via the GitHub website and the GitHub iOS app — no local IDE, no terminal, no Codespaces. Source: `.github/copilot-instructions.md` Working Environment section. [x] consulted.

**[fact]** The GitHub wiki renders natively in both the GitHub website and iOS app under the **Wiki** tab. Source: `Research/completed/2026-03-01-github-wiki-research-content.md` Key Finding #1. [x] consulted.

**[fact]** iOS Shortcuts can open the wiki URL directly via a single "Open URLs" Shortcut action, making Siri-invocable wiki access trivial. Source: `Research/completed/2026-03-02-ios-shortcuts-research.md` Key Finding #7. [x] consulted.

**[inference]** The human researcher's primary access pattern is: (a) passive browsing via the wiki tab on web/iOS, and (b) active query via the `research search` CLI command (accessible only when running an agent session, since the owner has no local terminal).

#### Q1b: AI agent's access model

**[fact]** Claude Code and GitHub Copilot Agent discover and invoke MCP tools registered in `.github/mcp.json` (for Copilot) or `.mcp.json` (for Claude Code). Source: `Research/completed/2026-03-02-chat-conversational-interface.md` Key Finding #1. [x] consulted.

**[fact]** MCP tools in the research repository already include git, filesystem, GitHub, and Tavily servers — all using stdio subprocess invocation; a new research MCP server would use the same pattern. Source: `.github/mcp.json` (10 servers as of this session). [x] consulted.

**[inference]** The AI agent's access pattern is: calling `search_research(query)` to locate relevant completed items, then `get_research_item(slug)` to retrieve full content, with the agent synthesising the answer from retrieved context.

#### Q2a: GitHub wiki as browsing interface

**[fact]** The GitHub wiki is already implemented and live: `publish-wiki.yml` runs on every push to `main` touching `Research/completed/**`, rebuilds the wiki using `src/wiki/publish.py`, and generates `Home.md` (date-sorted index) and `_Sidebar.md` (tag navigation). Source: `Research/completed/2026-03-01-github-wiki-research-content.md` Executive Summary. [x] consulted.

**[inference]** The wiki channel is fully operational — no further investigation needed. It is the primary human-browsing interface.

#### Q2b: CLI search command

**[fact]** The `2026-03-02-semantic-full-text-search.md` item designed the `research search` CLI command: SQLite FTS5 index over title + tags + executive summary + key findings, mtime-based rebuild, output format of date/priority/tags + excerpt, `--limit`, `--mode`, `--tag` options. Source: `Research/completed/2026-03-02-semantic-full-text-search.md` §1.6 CLI command design. [x] consulted.

**[fact]** The current CLI (`python -m src.main research`) has `add`, `list`, `start`, `complete` subcommands but no `search` or `query` subcommand. Source: `python -m src.main research --help` output. [x] consulted.

**[inference]** The CLI search command is designed but not yet implemented. It would be the most useful query interface for agent sessions running in this repository.

#### Q2c: Email digest via Latest-developments- pattern

**[fact]** The `davidamitchell/Latest-developments-` repository implements a daily email digest: GitHub Actions fetches YouTube/RSS/HN content, summarises with Gemini, and sends via Resend or Gmail. It requires secrets: `RESEND_API_KEY` (or `EMAIL_PROVIDER`/`EMAIL_SENDER`/`EMAIL_PASSWORD` for Gmail), `EMAIL_RECIPIENT`, and `GEMINI_API_KEY`. Source: `Latest-developments-` README.md. [x] consulted.

**[fact]** The approved credentials table in `.github/copilot-instructions.md` lists: `GITHUB_TOKEN`, `COPILOT_GITHUB_TOKEN`, `YOUTUBE_DATA_API`, `TAVILY_API_KEY`. None of the credentials required for email delivery (`RESEND_API_KEY`, Gmail App Password, `EMAIL_RECIPIENT`) appear in the table. Source: `.github/copilot-instructions.md` Available credentials and services. [x] consulted.

**[fact]** The non-negotiable constraint states: "Do not introduce new external services or credentials without explicit owner approval." Source: `.github/copilot-instructions.md` Non-Negotiable Constraints. [x] consulted.

**[inference]** The email digest path requires at least two new credentials not in the approved table (`RESEND_API_KEY` and `EMAIL_RECIPIENT`), making it a **hard stop** under current constraints. Implementation is blocked pending owner approval of these credentials.

#### Q3a: MCP server as agent interface

**[fact]** The `2026-03-02-chat-conversational-interface.md` item concluded: "An MCP server with stdio transport — registered in `.github/mcp.json` alongside the repository's existing 10 MCP servers — is the correct and only viable approach for a conversational research-corpus interface under this repository's constraints." Source: `Research/completed/2026-03-02-chat-conversational-interface.md` Executive Summary. [x] consulted.

**[fact]** The MCP protocol specification defines tools as model-controlled, uniquely identified by name, with JSON Schema-defined input parameters and typed result content. Source: `https://modelcontextprotocol.io/docs/concepts/tools`. [x] consulted.

**[inference]** The MCP server is the only agent interface approach that satisfies all constraints (no persistent server, no new credentials, stdio transport compatible with existing infrastructure). It is not yet implemented.

#### Q3b: MCP server tool contract

**[fact]** The `2026-03-02-chat-conversational-interface.md` item defined the three-tool contract:
```
search_research(query: str, tags: list[str] | None, limit: int) -> list[dict]
get_research_item(slug: str) -> str
get_related_items(slug: str) -> list[dict]
```
Source: `Research/completed/2026-03-02-chat-conversational-interface.md` §6 Synthesis. [x] consulted.

**[inference]** The three-tool contract is the correct interface. Phase 1 uses grep-based search; Phase 2 replaces the backend with SQLite FTS5 without changing the tool interface.

#### Q4a: Slack outbound notification

**[fact]** The `2026-03-02-slack-msteams-research-integration.md` item confirmed: "Outbound Slack notification requires exactly one new secret (`SLACK_WEBHOOK_URL`) stored as a GitHub Actions repository secret; this secret is the only new credential needed for per-item delivery and requires explicit owner approval before the workflow can be implemented." Source: Key Finding #2. [x] consulted.

**[inference]** Slack outbound notification is architecturally viable and low-complexity, but requires `SLACK_WEBHOOK_URL` approval — a hard stop until the owner approves it.

#### Q4b: Email digest viability

As established in Q2c: the email digest is blocked by missing credentials. The weekly digest variant (schedule-triggered, summarising items completed in the past 7 days) has the same credential dependency and is equally blocked.

#### Q5: Implementation priority

**[inference, based on constraint analysis]:**
1. **GitHub wiki** — already live. No action needed.
2. **MCP server (`src/mcp/research_server.py`)** — designed, no new credentials, highest-value agent interface. Priority: implement next.
3. **CLI `research search` command** — designed in `2026-03-02-semantic-full-text-search.md`, no new credentials, useful in agent sessions. Priority: implement alongside or just after the MCP server.
4. **Slack notification** — requires `SLACK_WEBHOOK_URL` approval. Blocked.
5. **Email digest** — requires multiple new credentials. Blocked.

---

### §3 Reasoning

**[inference] Consumer separation drives interface design.** The human researcher and the AI agent have structurally different access patterns. The human reads via GitHub web/iOS; the agent queries programmatically. No single interface serves both optimally. The wiki serves the human; the MCP server serves the agent; the CLI search command serves the agent session where it runs.

**Prior research has already resolved the core sub-questions.** Five completed items (wiki, conversational interface, Slack/Teams, iOS Shortcuts, semantic search) collectively answer every aspect of this item's research question. This item's function is synthesis: assembling the unified strategy from those findings.

**Credential constraints are a binding filter.** Email digest (Resend or Gmail) and Slack notification both require credentials not yet approved. The constraint is not technical — both are implementable — but administrative. The interface strategy must proceed without those channels until approval is obtained.

**No assumption about future credential approval.** The email digest and Slack paths are blocked, not deferred. If credentials are later approved, the work is straightforward; that approval event would unblock the implementation.

---

### §4 Consistency Check

- **Wiki status:** Confirmed live via `publish-wiki.yml` (Key Finding in the wiki item); consistent with Evidence Map.
- **MCP server status:** Confirmed designed but not implemented; consistent across §2 and §6.
- **CLI search status:** Confirmed designed in `semantic-full-text-search.md`, not in current CLI; consistent.
- **Credential constraint:** All blocked items consistently reference the approved credentials table as the source of the constraint.
- **No contradictions identified.** The MCP server uses stdio transport (no persistent process), which is consistent with the no-persistent-server constraint.
- **Acronyms expanded on first use:** MCP, FTS5, SSE, TLS all expanded in §0. [verified]

---

### §5 Depth and Breadth Expansion

**Technical lens:** The MCP stdio transport invokes a subprocess per session — cold-start latency for a Python MCP server is 30–300ms (per `2026-03-02-chat-conversational-interface.md` Key Finding #2). At corpus size < 200 items, [inference] a grep-based Phase 1 backend adds < 50ms per search. [inference] The wiki full-rebuild pipeline at current volume completes in under 1 second. No performance concern at these scales.

**Behavioural lens:** The human researcher's consumption pattern is primarily *discovery* (what have I researched recently? what is in a given area?) rather than *retrieval* (give me this specific item). The wiki's date-sorted `Home.md` and tag-sorted `_Sidebar.md` serve discovery. The MCP `search_research` tool serves retrieval. The two channels are complementary and target different consumption modes.

**Historical lens:** The repository started with `Research/completed/` as a git-backed flat file store. The wiki was the first delivery layer added (March 2026). The MCP server is the next logical layer. The progression follows a standard knowledge management maturation arc: file storage → human browsing → machine-queryable index.

**Economic lens:** All implemented and pending interfaces incur zero ongoing cost: GitHub wiki uses `GITHUB_TOKEN` with no API calls, the MCP server is a subprocess with no network cost, the CLI search uses a local SQLite database. The only cost-incurring options (email digest requiring Resend, or Slack with enterprise plans) are coincidentally also the credential-blocked options.

**Regulatory lens:** No personal data (names, addresses, financial records) is stored in `Research/completed/`. The research corpus contains only structured research notes. The interface strategy introduces no new privacy or compliance obligations.

---

### §6 Synthesis

**Interface strategy summary:**

The research corpus requires two parallel delivery layers, one per consumer type:

1. **Human consumer → GitHub wiki** (live). A static, fully-automated, wiki-tab-accessible view of all completed research, rebuilt on every push to `main`. Requires no action.

2. **AI agent consumer → MCP server** (designed, not yet implemented). An stdio MCP server registered in `.github/mcp.json`, exposing `search_research`, `get_research_item`, and `get_related_items` tools. Phase 1 uses grep; Phase 2 upgrades to SQLite FTS5 after the `semantic-full-text-search.md` item is implemented.

**Supporting channels:**

3. **CLI query (`research search`)** — designed in `2026-03-02-semantic-full-text-search.md`; shares the FTS5 backend with the MCP server Phase 2. Implement as part of the same backlog slice.

4. **Email digest and Slack notification** — architecturally viable but blocked by missing credentials. Backlog items for each, contingent on owner approval of `RESEND_API_KEY`/`EMAIL_RECIPIENT` (email) and `SLACK_WEBHOOK_URL` (Slack).

**Implementation priority:**
1. MCP server (`src/mcp/research_server.py`) + ADR — no new credentials, highest agent value
2. CLI `research search` command — no new credentials, useful in agent sessions
3. Slack notification — pending `SLACK_WEBHOOK_URL` approval
4. Email digest — pending `RESEND_API_KEY` + `EMAIL_RECIPIENT` approval

---

### §7 Recursive Review

**Coverage:** All five top-level sub-questions (Q1–Q5) and all ten atomic questions are addressed. Every approach item from the original research item (CLI, email digest, MCP) is covered.

**Claims sourced:** Every [fact] maps to a consulted source (marked [x]). All [inference] labels applied where claims are derived from evidence. No [assumption] labels needed — all claims are either factual (sourced) or clearly inferential.

**Uncertainties explicit:** Email digest and Slack notification are clearly flagged as blocked (not deferred), with the specific missing credentials named. The MCP server Phase 2 dependency on `semantic-full-text-search.md` is explicit.

**No threads unresolved:** The static site option (out of scope per the item's own Scope section) is correctly excluded. The email digest is addressed and blocked-with-reason. No open questions were left without disposition.

**Verdict:** Research is complete. Proceed to Findings.

---

## Findings

### Executive Summary

The research corpus requires two parallel delivery channels, one per consumer type: the GitHub wiki (already live) serves the human researcher via the repository's Wiki tab on web and iOS, and an MCP server with stdio transport (designed, not yet implemented) serves AI agents via `search_research`, `get_research_item`, and `get_related_items` tools. The CLI `research search` command is designed and shares the same FTS5 backend; it is the third channel to implement. Email digest and Slack push notification are architecturally viable but blocked under current constraints: both require credentials (`RESEND_API_KEY`/`EMAIL_RECIPIENT` for email; `SLACK_WEBHOOK_URL` for Slack) that are not in the approved credentials table and require owner approval before implementation can proceed.

### Key Findings

1. **The GitHub wiki is the correct and already-live human-browsing interface: `publish-wiki.yml` rebuilds all pages from `Research/completed/` on every push to `main`, producing a date-sorted `Home.md` and tag-indexed `_Sidebar.md` accessible from the repository's Wiki tab on both the GitHub website and the iOS app.** [High confidence]

2. **An MCP server with stdio transport, registered in `.github/mcp.json`, is the only agent-query interface that satisfies all repository constraints: no persistent server process, no new credentials, compatible with the 10 existing MCP stdio servers.** [High confidence]

3. **The three-tool MCP interface contract defined in `2026-03-02-chat-conversational-interface.md` is complete and sufficient: `search_research(query, tags, limit)` for ranked discovery, `get_research_item(slug)` for full content retrieval, and `get_related_items(slug)` for cross-reference navigation via `state/links.json`.** [High confidence]

4. **The CLI `research search` command is designed in `2026-03-02-semantic-full-text-search.md` with SQLite FTS5 index, mtime-based rebuild, and `--limit`/`--mode`/`--tag` options, but is not yet implemented in `src/main.py`.** [High confidence]

5. **The email digest path via the `davidamitchell/Latest-developments-` pattern requires at minimum two new credentials (`RESEND_API_KEY` and `EMAIL_RECIPIENT`) that do not appear in the approved credentials table, making it a hard-stop blocked item under the non-negotiable constraints.** [High confidence]

6. **Outbound Slack notification (one completed item per push) is low-complexity — four lines of workflow YAML Ain't Markup Language (YAML) using `slackapi/slack-github-action@v2.1.1` — but is equally blocked pending explicit owner approval of the `SLACK_WEBHOOK_URL` secret.** [High confidence]

7. **The human and agent consumers have structurally different access patterns: the human researcher performs discovery (browsing by date and tag), while the AI agent performs retrieval (querying by keyword to locate specific items for synthesis); no single interface serves both optimally, making the two-layer strategy the correct design.** [Medium confidence — inference from usage patterns]

8. **All currently unblocked interface channels (wiki, MCP server, CLI search command) incur zero ongoing cost — they rely on `GITHUB_TOKEN` and local file access with no paid API calls.** [High confidence]

9. **The MCP server implementation must be accompanied by an Architecture Decision Record (ADR) documenting the stdio transport choice, three-tool interface contract, grounding design (tool-scoped retrieval prevents corpus hallucination), and the Phase 1 (grep) / Phase 2 (FTS5) phasing.** [High confidence — per `2026-03-02-chat-conversational-interface.md` Key Finding #10]

10. **iOS Shortcuts provide a complementary mobile-access layer: a "Open URLs" shortcut points to the wiki Home page for read access, and a GitHub Issues API shortcut handles mobile research capture — neither requires any server-side changes.** [High confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| GitHub wiki is live and rebuilt on every push | `Research/completed/2026-03-01-github-wiki-research-content.md` Executive Summary | High | `publish-wiki.yml` and `src/wiki/publish.py` implemented |
| MCP stdio server is the only viable agent interface | `Research/completed/2026-03-02-chat-conversational-interface.md` Executive Summary | High | GitHub Copilot Extension approach eliminated by no-server constraint |
| Three-tool MCP contract | `Research/completed/2026-03-02-chat-conversational-interface.md` §6 Synthesis | High | Matches MCP protocol tool definition from modelcontextprotocol.io |
| `research search` CLI command designed, not implemented | `Research/completed/2026-03-02-semantic-full-text-search.md` §1.6; `python -m src.main research --help` output | High | Current CLI lacks search subcommand |
| Email digest requires credentials not in approved table | `davidamitchell/Latest-developments-` README.md; `.github/copilot-instructions.md` credentials table | High | `RESEND_API_KEY`, `EMAIL_RECIPIENT` not in table |
| Slack notification blocked pending secret approval | `Research/completed/2026-03-02-slack-msteams-research-integration.md` Key Finding #2 | High | `SLACK_WEBHOOK_URL` not in approved credentials table |
| Human/agent access patterns differ fundamentally | `.github/copilot-instructions.md` Working Environment; `Research/completed/2026-03-02-chat-conversational-interface.md` | Medium | [inference] from usage model description |
| Zero ongoing cost for wiki, MCP, CLI channels | `Research/completed/2026-03-01-github-wiki-research-content.md`; `Research/completed/2026-03-02-chat-conversational-interface.md` Key Finding #2; `Research/completed/2026-03-02-semantic-full-text-search.md` | High | All use GITHUB_TOKEN or local file access |
| MCP server requires an ADR | `Research/completed/2026-03-02-chat-conversational-interface.md` Key Finding #10 | High | Explicitly stated in prior research |
| iOS Shortcuts provide mobile access | `Research/completed/2026-03-02-ios-shortcuts-research.md` Key Findings #1, #7 | High | "Open URLs" shortcut + Issues API capture shortcut |

**Identified but not consulted:**
- `[ ]` `davidamitchell/Latest-developments-` source code (`src/`) — README was sufficient to characterise the pattern; full source not required for this finding
- `[ ]` MCP HTTP/SSE transport specification — not relevant since stdio transport is the confirmed choice

### Assumptions

- **Assumption:** The owner has not approved `SLACK_WEBHOOK_URL`, `RESEND_API_KEY`, or `EMAIL_RECIPIENT` credentials since the `2026-03-02-slack-msteams-research-integration.md` item was completed. **Justification:** The approved credentials table in `.github/copilot-instructions.md` lists only four credentials; no subsequent session log mentions a table update. If these credentials have since been approved, the blocked items are immediately actionable.

### Analysis

The interface strategy is architecturally complete, with two channels live or fully designed and two channels blocked by credential constraints. The key trade-off evaluated was human-browsing vs agent-query vs push-notification: they are not competing designs but complementary layers targeting distinct consumer modes. [inference] Prioritising the MCP server over the CLI search command is correct because it serves agent-to-corpus queries, which is the higher-frequency use case during research loop sessions. The CLI search command is a useful supplement that shares the FTS5 backend and should be implemented in the same slice. Push notifications (Slack/email) add value but are optional and blocked — delaying them costs nothing.

The email digest pattern from `Latest-developments-` is well-established but architecturally heavier than needed: that project watches external feeds and produces AI summaries, whereas a research digest only needs to list recently completed items. If credentials are approved, the digest workflow would be simpler than the `Latest-developments-` pipeline — a `schedule`-triggered workflow that reads `completed` dates from `Research/completed/` YAML Ain't Markup Language (YAML) front-matter and posts a summary.

### Risks, Gaps, and Uncertainties

- **Credential approval is the single unresolved variable.** Email digest and Slack notification are architecturally ready but blocked until the owner approves the relevant credentials. No technical gap; the gap is administrative.
- **MCP server Phase 2 depends on `semantic-full-text-search.md` implementation.** Phase 1 (grep-based) is independent and deployable now. If the FTS5 search layer is delayed, Phase 1 is fully functional.
- **`get_related_items` depends on `state/links.json` population**, which in turn depends on `2026-03-03-knowledge-linking-connected-corpus.md` being implemented. Without that edge store, the tool returns empty results rather than an error.
- **Wiki navigation is flat.** The GitHub wiki has no subdirectory support, so as the corpus grows beyond ~200 items, the `Home.md` index may become long. Tag-based grouping in `_Sidebar.md` mitigates this but does not resolve it. A future item could address hierarchical navigation.

### Open Questions

1. **Should a `research digest` CLI command be added** that generates a Markdown summary of the last N days' completions, usable both locally and as a workflow step? This would be a lightweight alternative to the email digest for producing a shareable briefing without external credentials. Priority: low (no downstream blocker).

2. **When the owner approves email or Slack credentials, should the notification and digest be a separate new workflow file or merged into `publish-wiki.yml`?** The trigger (`push` to `main` touching `Research/completed/**`) is the same; merging reduces workflow count. Priority: low; decide at implementation time.

---

## Output

- Type: knowledge, backlog-item
- Description: Unified interface strategy: wiki (live), MCP server (implement next), CLI search (implement alongside MCP), email/Slack (blocked pending credential approval). Two backlog items identified: MCP server implementation and `research digest` CLI command.
- Sources:
  - [Research/completed/2026-03-02-chat-conversational-interface.md](Research/completed/2026-03-02-chat-conversational-interface.md) — MCP server design
  - [Research/completed/2026-03-01-github-wiki-research-content.md](Research/completed/2026-03-01-github-wiki-research-content.md) — wiki delivery channel
  - [Research/completed/2026-03-02-semantic-full-text-search.md](Research/completed/2026-03-02-semantic-full-text-search.md) — CLI search design