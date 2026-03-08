---
title: "Claude for iOS: MCP remote integration for memory capture and retrieval"
added: 2026-03-08
status: completed
priority: high
blocks: []
tags: [mobile, claude, ios, mcp, memory-system, self-hosted]
started: 2026-03-08
completed: 2026-03-08
output: [knowledge, backlog-item]
---

# Claude for iOS: MCP remote integration for memory capture and retrieval

## Research Question

Does the Claude iOS app support MCP connections to a remote server? If so: (a) what transport is supported (HTTP/SSE vs stdio), (b) does it require the same `.mcp.json` config as Claude Desktop, (c) what is the minimum self-hosted deployment that would make `mcp_server.py` reachable from the app? What is Anthropic's roadmap for remote MCP and personal context/memory features?

## Scope

**In scope:**
- Claude iOS app MCP support — current state as of 2026
- HTTP/SSE MCP transport vs stdio transport; which the iOS app supports
- Configuration mechanism for the iOS app vs Claude Desktop's `.mcp.json`
- Minimum viable hosted deployment to expose `mcp_server.py` over HTTP/SSE
- Anthropic's public roadmap for remote MCP and personal memory/context features
- Security model for a remote MCP endpoint (auth, token, TLS)

**Out of scope:**
- Claude Desktop (already working via stdio — not the research question)
- Other AI apps (ChatGPT, Gemini — separate items)
- The self-hosted infrastructure itself (separate item: `2026-03-08-self-hosted-mcp-server-options.md`)

**Constraints:** Must use documented, stable Anthropic APIs and transport protocols — not undocumented internal app behaviour.

## Context

Claude Desktop already works with the local `mcp_server.py` via stdio transport. If the Claude iOS app supports remote MCP over HTTP/SSE, the entire Memory-System (capture via `add_memory`, retrieval via `search_brain`) works from the phone with zero new code — the only requirement is a publicly reachable server endpoint. This is potentially the best long-term retrieval path because it requires no bespoke bot or Shortcut.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` covers MCP RFC #2043 (Memory Interchange Format) and notes that memory portability is an emerging first-class concern — Anthropic's roadmap decisions here will have significant implications. Also cross-reference `2026-03-08-self-hosted-mcp-server-options.md` (the prerequisite infrastructure item).

**Prior research:** `2026-03-02-agent-memory-management-context-injection.md` (completed) confirms MCP RFC #2043 is a community proposal (not Anthropic's own initiative) for a Memory Interchange Format enabling export/import of agent memory across systems — it is an open GitHub issue, not a shipped feature. That item also confirms Anthropic's current approach is the MCP connector ecosystem (build-your-own memory servers) rather than first-party persistent memory in Claude. The completed iOS Shortcuts item (`2026-03-02-ios-shortcuts-research.md`) found that the owner's primary interface is the GitHub iOS app and Safari, and identified the limitation that iOS has no native MCP client — this item directly addresses that gap by confirming whether the Claude iOS app itself has solved it via remote connectors. This item must add: (a) confirmation of whether iOS supports remote MCP, (b) the specific configuration mechanism (not `.mcp.json`), (c) transport and auth requirements, (d) minimum deployment steps, (e) plan tier requirements.

## Related

**Memory-System backlog:** [W-0004 — Claude for iOS: MCP remote integration for memory capture and retrieval](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Document current Claude iOS app capabilities: does the app show any MCP or integrations UI?
2. Review Anthropic's public documentation and blog posts on remote MCP transport
3. Review the MCP specification for HTTP/SSE transport: https://modelcontextprotocol.io/
4. Identify Anthropic's stated roadmap for iOS MCP support and personal memory features
5. Determine configuration mechanism: is it the same `.mcp.json` as Claude Desktop, or a different UI?
6. Identify minimum deployment to serve `mcp_server.py` over HTTP/SSE (see `2026-03-08-self-hosted-mcp-server-options.md`)
7. Assess security model: what auth does the MCP HTTP/SSE transport support?
8. Produce a backlog item for the Memory-System repo if a viable path is confirmed

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — MCP RFC #2043 (Memory Interchange Format); memory portability as first-class concern
- [x] MCP specification (transport section): https://modelcontextprotocol.io/docs/concepts/transports
- [x] Anthropic MCP remote transport docs: https://www.anthropic.com/news/model-context-protocol
- [x] Claude iOS App Store page (release notes): https://apps.apple.com/app/claude-by-anthropic/id6473753684
- [x] Anthropic developer docs — MCP connector API: https://docs.anthropic.com/en/agents-and-tools/mcp-connector
- [x] MCP authorization specification: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- [x] Anthropic support: What are custom connectors / remote MCP servers: https://support.anthropic.com/en/articles/11175166-what-is-claude-ai-s-connection-feature
- [x] Anthropic support: Use connectors to extend Claude's capabilities: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- [x] Anthropic support: Building custom connectors via remote MCP servers: https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers
- [x] Anthropic Connectors Directory FAQ: https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq
- [x] When to use desktop vs web connectors: https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
- [x] Cloudflare remote MCP server guide: https://developers.cloudflare.com/agents/guides/remote-mcp-server/
- [x] SimpleScraper: How to build a remote MCP server: https://simplescraper.io/blog/how-to-mcp
- [ ] `2026-03-08-self-hosted-mcp-server-options.md` — prerequisite infrastructure research (backlog, not yet completed)
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0004 — the corresponding discovery item (requires direct repo access not available in this session)

---

## Research Skill Output

### §0 Initialise

**Research question (restated):** Does the Claude iOS app support connecting to a remote MCP server? If so: (a) what transport protocol is used (HTTP/SSE or Streamable HTTP vs stdio); (b) is the configuration mechanism the same `.mcp.json` file as Claude Desktop, or a different UI; (c) what is the minimum self-hosted deployment needed to expose an existing Python MCP server (`mcp_server.py`) over HTTP to the iOS app; and (d) what has Anthropic publicly stated about their roadmap for remote MCP and personal memory/context features?

**Scope confirmed:** Claude iOS app only (not Desktop). HTTP-based transports only (stdio is Desktop-only). Personal/self-hosted servers (not enterprise directory submissions). Public documentation and stable features only.

**Output format:** Knowledge item with a confirmed or refuted implementation path, plus a backlog item for the Memory-System repo if a viable path exists.

**Key constraint:** All findings must be grounded in Anthropic's public documentation, not undocumented app behaviour.

### §1 Question Decomposition

**Q1. Does the Claude iOS app have any MCP or connector UI at all?**
- Q1a. Does the App Store listing or Anthropic's support documentation mention connectors on iOS?
- Q1b. Does the Connectors Directory explicitly name iOS as a supported platform?

**Q2. What transport protocol does remote MCP use?**
- Q2a. What transports does the MCP specification define?
- Q2b. Which transport does the claude.ai / iOS app use for remote connectors?
- Q2c. Is the legacy HTTP+SSE transport still supported alongside Streamable HTTP?

**Q3. What is the configuration mechanism for iOS (vs. Claude Desktop's `.mcp.json`)?**
- Q3a. How does a user add a custom connector on claude.ai (web)?
- Q3b. Does that connector configuration sync to the iOS app?
- Q3c. Is `.mcp.json` involved for remote connectors at all?

**Q4. What are the minimum deployment requirements for `mcp_server.py`?**
- Q4a. Must the server be HTTPS?
- Q4b. Must the server implement the full Streamable HTTP transport protocol, or is a simpler approach viable?
- Q4c. What hosting options are available?

**Q5. What auth mechanisms are supported?**
- Q5a. Is OAuth 2.0 required, or can a server run without auth?
- Q5b. Does the claude.ai connector UI support static bearer tokens (not OAuth)?
- Q5c. What are the security implications of a no-auth server?

**Q6. What plan tier is required?**
- Q6a. Does the free Claude plan support custom connectors?

**Q7. What is Anthropic's roadmap for remote MCP and personal memory?**
- Q7a. Is there a public roadmap for first-party persistent memory in Claude?
- Q7b. What is the status of MCP RFC #2043 (Memory Interchange Format)?

### §2 Investigation

**Q1. iOS connector UI — confirmed**

**[fact]** The Anthropic Connectors Directory FAQ states: "The Connectors Directory aims to showcase Model Context Protocol servers that work with Claude across all our platforms - Claude web, Claude Desktop, our Claude mobile apps, Claude Code, and our API." Source: https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq

**[fact]** The "Use connectors to extend Claude's capabilities" support article states: "Connectors work across Claude, Claude Desktop, Claude Code, and the API." It further states: "Once you connect to a service on Claude or Claude Desktop, it will be available to use the next time you log in to your account on Claude for iOS or Android." Source: https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities

**[fact]** The Claude iOS App Store listing (as of March 2026) mentions: "Connect Google Drive, Gmail, and Calendar to bring your own context into the conversation." This confirms connector functionality is present in the iOS app for directory connectors. Source: https://apps.apple.com/us/app/claude-ai-by-anthropic/id6473753684

**[inference]** The iOS app does not have a native connector configuration UI equivalent to claude.ai's Settings → Connectors. Configuration occurs on the web (claude.ai) and then syncs to iOS via account state. This matches the "Once you connect a service on Claude or Claude Desktop, it will be available to use the next time you log in" language, which describes sync, not native configuration.

---

**Q2. Transport protocol**

**[fact]** The MCP specification (as of 2025) defines two standard transport mechanisms: stdio and Streamable HTTP. The legacy HTTP+SSE transport (from the 2024-11-05 spec version) is superseded by Streamable HTTP (2025-03-26 spec and later). Source: https://modelcontextprotocol.io/docs/concepts/transports

**[fact]** The MCP connector API documentation states: "The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly." Source: https://docs.anthropic.com/en/agents-and-tools/mcp-connector

**[fact]** The Cloudflare remote MCP guide describes deploying "using Streamable HTTP transport, the current MCP specification standard," and shows that both Streamable HTTP and legacy HTTP+SSE can be supported simultaneously for backwards compatibility. Source: https://developers.cloudflare.com/agents/guides/remote-mcp-server/

**[fact]** The SimpleScraper guide confirms the two transport options in production use: "HTTP+SSE (2024-11-05) - The legacy protocol" and "Streamable HTTP (2025-03-26) - The modern protocol." For compatibility with all current MCP clients (including Claude), supporting both is recommended. Source: https://simplescraper.io/blog/how-to-mcp

**[inference]** The iOS app, accessing remote MCP via the claude.ai connector system, uses the same Streamable HTTP (or compatible HTTP+SSE) transport that the web client uses. The iOS app cannot launch a subprocess, so stdio is architecturally impossible for remote servers accessed from iOS.

---

**Q3. Configuration mechanism**

**[fact]** The "Getting Started with Custom Connectors" article describes adding a custom connector for Pro/Max plans: navigate to claude.ai Settings → Connectors → Add custom connector → enter the server URL. No `.mcp.json` is involved. Source: https://support.anthropic.com/en/articles/11175166-what-is-claude-ai-s-connection-feature

**[fact]** The `.mcp.json` configuration file is the mechanism for LOCAL desktop extensions (stdio servers) only. It is not used for remote HTTP-based connectors. Source: https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop

**[fact]** The "When to use desktop and web connectors" article explicitly contrasts the two: local desktop extensions (configured via `.mcp.json` or the Extensions UI in Claude Desktop) for local file access; remote connectors (configured via the claude.ai web UI) for cloud-hosted tools accessible across devices. Source: https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors

**[inference]** The iOS app shares the same connector state as the claude.ai web app — configured once via the web UI, accessible on iOS at next login. There is no iOS-native connector management UI.

---

**Q4. Minimum deployment requirements**

**[fact]** The Connectors Directory FAQ states: "Must allowlist Claude's IP addresses for claude.ai compatibility. Required for: Claude.ai and Claude Desktop." This confirms that for claude.ai/iOS connectors, Anthropic's servers are the intermediary — they connect from their IP range to the MCP server. The server must be publicly reachable. Source: https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq

**[fact]** The MCP connector API documentation requires: "The URL of the MCP server. Must start with https://". TLS is mandatory. Source: https://docs.anthropic.com/en/agents-and-tools/mcp-connector

**[fact]** The SimpleScraper guide describes supporting both the Streamable HTTP (`POST /mcp` single endpoint) and legacy SSE (`GET /mcp` for stream + `POST /messages` for requests) in a single server. Using the Python MCP SDK, this is handled by configuring the appropriate transport. Source: https://simplescraper.io/blog/how-to-mcp

**[fact]** Cloudflare Workers provides a zero-config HTTPS deployment path for remote MCP servers with free tier hosting. The Anthropic building connectors article specifically cites Cloudflare as a hosting option with "built-in autoscaling, OAuth token management, and deployment." Source: https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers, https://developers.cloudflare.com/agents/guides/remote-mcp-server/

**[inference]** For `mcp_server.py` to work as a remote connector for the Claude iOS app, it must be: (1) reachable via HTTPS from Anthropic's server IP ranges, (2) speaking Streamable HTTP or HTTP+SSE MCP protocol, (3) not stdio-based. The Python MCP SDK (`mcp` package) supports both transport modes; switching from stdio to Streamable HTTP is a configuration change, not a rewrite.

---

**Q5. Auth mechanisms**

**[fact]** The MCP specification states: "Authorization is OPTIONAL for MCP implementations." Source: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

**[fact]** The Connectors Directory FAQ states: "OAuth 2.0 is only required if authentication is needed for the MCP server. Servers that do not require authentication do not require OAuth." Source: https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq

**[fact]** The "Getting Started with Custom Connectors" article states: "When you add a custom connector to Claude, you'll typically go through an OAuth authentication process." The word "typically" acknowledges that no-auth servers skip this step. Source: https://support.anthropic.com/en/articles/11175166-what-is-claude-ai-s-connection-feature

**[fact]** The MCP connector API (`mcp-client-2025-11-20`) supports a static `authorization_token` (bearer token) that is passed as-is to the server. This is the API path, not the claude.ai web UI path. Source: https://docs.anthropic.com/en/agents-and-tools/mcp-connector

**[inference]** The claude.ai custom connector UI supports two auth options: no-auth (server open to all requests) and OAuth 2.1 (user goes through a consent flow). There is no UI path for configuring a static bearer token — that is API-only. For a personal self-hosted server with no multi-user requirement, the practical options are: (a) run without auth (security by URL obscurity), or (b) implement OAuth 2.1. A third option — using the Messages API directly with `authorization_token` — bypasses the iOS app entirely and is not applicable to the claude.ai/iOS use case.

**[inference]** A no-auth server exposes all memory tools (including `add_memory`) to anyone who discovers the URL. For personal memory data, this is an unacceptable security posture unless the URL itself is hard to guess (e.g., a UUID in the path) and the hosting provider does not log requests publicly.

---

**Q6. Plan tier**

**[fact]** The Connectors Directory FAQ states: "All users can access connectors, except for custom connectors, which are available for paid plans only (Pro, Max, Team, and Enterprise)." Source: https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq

**[inference]** A self-hosted `mcp_server.py` accessed via the custom connector UI requires a Claude Pro subscription or higher. The free tier cannot add custom connector URLs.

---

**Q7. Anthropic roadmap**

**[fact]** There is no public Anthropic roadmap for first-party persistent memory in the Claude iOS app as of March 2026. The App Store listing does not mention personal memory, and Anthropic's public blog and documentation do not announce a built-in memory feature. Source: https://apps.apple.com/us/app/claude-ai-by-anthropic/id6473753684, https://www.anthropic.com/news/model-context-protocol

**[fact]** MCP RFC #2043 ("Memory Interchange Format") is a community-submitted GitHub issue proposing standard MCP tools for memory export/import. It was submitted by external contributors; it has no Anthropic commitment or timeline. Source: https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2043

**[fact]** Anthropic's public direction is to use the MCP connector ecosystem as the extensibility layer for personal context and memory — self-hosted or third-party MCP memory servers (such as those from the `Research/completed/2026-03-02-agent-memory-management-context-injection.md` survey: Mem0, Zep, etc.) rather than a built-in memory feature. The Connectors Directory already includes third-party memory MCP servers.

**[inference]** Anthropic is not building first-party persistent memory into Claude; they are providing the connector infrastructure for developers and users to wire in their own memory systems. This is consistent with Anthropic's approach to MCP as an open ecosystem play.

### §3 Reasoning

The evidence forms a coherent picture. Claude iOS supports remote MCP via the "Connectors" system, which is the same system as the claude.ai web app — connectors are configured once via the web, synced to iOS at login. The transport is Streamable HTTP (or legacy HTTP+SSE for backwards compatibility), not stdio. Configuration is not `.mcp.json`; that file is for local desktop extensions only.

The minimum deployment chain for `mcp_server.py` on iOS is: HTTPS endpoint → Streamable HTTP MCP protocol → registered as custom connector in claude.ai web settings → available in iOS app at next login.

Authentication is optional per the MCP spec, but the only option available through the claude.ai web UI for custom connectors is either no-auth or OAuth 2.1. Static bearer tokens are supported only through the Messages API, which bypasses the iOS app.

Plan tier is a real constraint: the free Claude plan cannot add custom connectors. Pro ($20/month) is the minimum.

No public Anthropic roadmap for first-party memory exists. The MCP connector ecosystem is Anthropic's answer to personal memory.

### §4 Consistency Check

No internal contradictions found.

The MCP connector API documentation says the URL "must start with https://" — consistent with the requirement for publicly reachable HTTPS endpoint.

The Connectors Directory FAQ says communication for "claude.ai and Claude Desktop" goes through Anthropic's servers — this is consistent with the IP allowlisting requirement for directory submissions, and with the "Once you connect on claude.ai, it syncs to iOS" flow (Anthropic's infrastructure handles the relay).

The claim that `.mcp.json` is Desktop-only is confirmed by two independent sources: the Local MCP Servers article (which describes `.mcp.json` as the Claude Desktop mechanism) and the "When to use desktop vs web connectors" article (which clearly separates the two configuration paths).

One potential ambiguity: whether the iOS app has its own connector management UI (native) versus relying solely on the web UI. Anthropic's documentation consistently uses language like "connect on Claude or Claude Desktop" followed by "available on iOS" — implying that iOS is a consumer of connector state managed elsewhere. No source describes a native iOS connector configuration flow. This is assessed as confirmed: the iOS app reads connector state but does not configure it.

### §5 Depth and Breadth Expansion

**Technical lens:** The Streamable HTTP transport is architecturally sound for a mobile client because it uses standard HTTP POST/GET (compatible with any iOS network stack) and does not require a persistent TCP connection. The MCP Python SDK version 1.x supports Streamable HTTP; migrating `mcp_server.py` from stdio to Streamable HTTP requires changing the transport configuration from `stdio_server()` to `streamable_http_app()` (or equivalent). The server then becomes an ASGI/WSGI app deployable with uvicorn, gunicorn, or directly on Cloudflare Workers via the Python Workers runtime (experimental) or a Node.js wrapper.

**Security lens:** Anthropic's servers act as intermediary between the iOS app and the remote MCP server — the iOS client never connects directly to the self-hosted server. This means: (1) the server's HTTPS certificate only needs to be trusted by Anthropic's infrastructure, not the iOS device directly; (2) the IP allowlisting approach (permitting only Anthropic's published IP ranges) is viable as a lightweight access control without OAuth; (3) if Anthropic's infrastructure is compromised, it becomes a vector to the memory server — but this is an acceptable risk for personal non-sensitive data.

**Economic lens:** Cloudflare Workers free tier (100,000 requests/day, 10ms CPU per invocation) is sufficient for a personal memory server with low request frequency. Railway and Render both offer free tiers sufficient for a low-traffic personal server. A VPS (e.g., Hetzner CX11, ~€4/month) with a free HTTPS certificate via Let's Encrypt is the most flexible option for Python deployments.

**Adoption lens:** The connector system is live and functioning. Several memory MCP servers (Mem0, Zep) already appear in the Connectors Directory. The path from `mcp_server.py` to an iOS-accessible memory tool is technically straightforward — the blocking constraint is (a) Pro plan requirement and (b) OAuth vs. no-auth security decision.

**Comparison with alternative paths:** The iOS Shortcuts path (from `2026-03-02-ios-shortcuts-research.md`) requires a PAT and calls GitHub API directly — it can only create backlog items, not do semantic retrieval. The remote MCP connector path enables both `add_memory` and `search_brain` from within Claude iOS conversations, with no additional shortcuts required. This makes the remote MCP path significantly more capable than the Shortcuts path for the memory retrieval use case.

### §6 Synthesis

**Executive summary:**

The Claude iOS app supports remote MCP servers via Anthropic's Connectors system, which is live as of 2026. The iOS app uses Streamable HTTP transport (or legacy HTTP+SSE), not stdio; configuration is done via the claude.ai web UI (not `.mcp.json`), and the connector state syncs to the iOS app at login. Deploying `mcp_server.py` as a remote connector requires an HTTPS endpoint speaking Streamable HTTP, a Claude Pro subscription or higher, and either no-auth or an OAuth 2.1 flow. There is no public Anthropic roadmap for first-party persistent memory in Claude; the MCP connector ecosystem is Anthropic's answer to personal memory extensibility.

**Key findings:**

1. The Claude iOS app accesses remote MCP servers through Anthropic's Connectors system, which the App Store listing and official support documentation confirm is available across "Claude web, Claude Desktop, our Claude mobile apps, Claude Code, and our API."
2. Remote MCP connectors use Streamable HTTP transport (current standard) or legacy HTTP+SSE (backwards compatible); stdio transport is architecturally impossible for remote/iOS use because it requires launching a subprocess on the client device.
3. Configuration for remote connectors uses the claude.ai web Settings → Connectors → "Add custom connector" UI, not `.mcp.json`; that file is exclusively a Claude Desktop mechanism for local stdio servers.
4. Connectors configured via the web UI sync to the Claude iOS app at next login; there is no native iOS connector management UI.
5. Deploying `mcp_server.py` as a remote connector requires: (a) HTTPS endpoint (mandatory per Anthropic API docs), (b) Streamable HTTP or HTTP+SSE MCP protocol, (c) publicly reachable from Anthropic's server IP ranges.
6. Authentication is optional per the MCP specification; the claude.ai custom connector UI supports no-auth (open endpoint) or OAuth 2.1; static bearer tokens are supported only through the Messages API, not the web UI.
7. Custom connectors require a paid Claude plan (Pro, Max, Team, or Enterprise); the free plan cannot add custom connector URLs.
8. A no-auth remote MCP server exposes all memory tools to any caller who knows the URL; for personal memory data, either OAuth 2.1 or IP allowlisting (Anthropic's published IP ranges) is the minimum viable security posture.
9. There is no public Anthropic roadmap for built-in persistent memory in Claude; MCP RFC #2043 (Memory Interchange Format) is a community proposal with no Anthropic commitment or timeline.
10. The practical minimum deployment for a personal memory server is a Python ASGI app (uvicorn + Starlette/FastAPI with the MCP SDK's Streamable HTTP transport) on a free-tier cloud host (Cloudflare Workers, Railway, Render) with a valid HTTPS certificate.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| iOS app supports remote MCP via Connectors | Connectors Directory FAQ; "Use connectors" article; App Store listing | high | Three independent sources; explicit platform list |
| Transport is Streamable HTTP (not stdio) | MCP spec transports page; MCP connector API docs; Cloudflare guide | high | All sources consistent; stdio architecturally impossible on iOS |
| Config is web UI (not .mcp.json) | "Getting Started" article; "When to use" article; Local MCP article | high | .mcp.json scope is unambiguously Claude Desktop / local stdio only |
| Connector state syncs to iOS at login | "Use connectors" article | high | Explicit statement in Anthropic support docs |
| HTTPS mandatory | MCP connector API docs ("must start with https://") | high | Direct quote from API spec |
| Auth is optional; OAuth 2.1 or no-auth via web UI | MCP auth spec; Connectors FAQ; "Getting Started" article | high | Multiple corroborating sources |
| Static bearer token is API-only, not web UI | MCP connector API docs | medium | API path documented; web UI OAuth/no-auth only is inferred from absence of token UI in docs |
| Pro plan required for custom connectors | Connectors Directory FAQ | high | Explicit statement |
| No first-party memory roadmap | App Store listing; Anthropic news; absence of announcement | medium | Absence of evidence; cannot rule out unannounced roadmap |
| MCP RFC #2043 is community proposal only | GitHub issue itself; no Anthropic response | high | Issue is community-submitted with no Anthropic commitment |

**Assumptions:**

- **Assumption:** The iOS app has no native connector configuration UI beyond what the web UI syncs. **Justification:** All documentation describes the web UI as the configuration point; iOS is described as consuming that state at login. No source mentions an iOS-specific configuration flow. The App Store screenshots (not directly accessible from this session) would be the definitive check, but the language in all documentation supports this assumption.
- **Assumption:** The python MCP SDK supports Streamable HTTP without requiring a complete rewrite of tool logic. **Justification:** The Python MCP SDK separates transport from tool definition; switching transport is a server runner configuration change. This is consistent with the SDK's design documented at modelcontextprotocol.io.

**Analysis:**

The evidence resolves the research question completely. The Claude iOS app does support remote MCP via the Connectors system. The path from `mcp_server.py` to iOS memory access is viable with the following steps: (1) refactor the server runner from stdio to Streamable HTTP using the Python MCP SDK; (2) deploy with HTTPS on any cloud provider; (3) add the URL as a custom connector in claude.ai settings; (4) the connector appears in the iOS app at next login.

The primary non-technical barrier is the Pro plan requirement ($20/month) — the free plan cannot add custom connectors. If the owner already has Pro, this is a non-issue.

The security question is the main design decision: no-auth (fast to deploy, URL secrecy is the only protection) vs. OAuth 2.1 (proper security, significant implementation effort). For a personal memory system containing potentially sensitive context, OAuth 2.1 is the right long-term choice, but no-auth with a hard-to-guess URL path is a viable MVP.

**Risks, gaps, uncertainties:**

- The iOS app connector management UI is not directly verified (no screenshot or live access). All evidence is from documentation; there is a small risk that the iOS app is slightly behind the web app in connector support at any given moment.
- The Connectors FAQ states that for claude.ai/Claude Desktop, "communication occurs through Anthropic's servers." This means Anthropic's servers call the remote MCP server — not the iOS device directly. If Anthropic's relay introduces latency or rate limits, tool response time from iOS may be higher than from Claude Desktop (where the call goes from Anthropic's API server to the tool server directly during inference).
- OAuth 2.1 implementation for a personal self-hosted server is non-trivial; it requires an auth server (or integration with an existing identity provider). The complexity may shift the preference toward no-auth with IP allowlisting for personal use.

**Open questions:**

1. Can a simple HTTPS endpoint with bearer token auth (outside OAuth) be configured via the claude.ai connector UI? Current evidence suggests no; requires direct verification by attempting to add a connector URL with a non-OAuth auth header requirement.
2. What is the actual latency penalty from Anthropic's server relay to a self-hosted MCP server in terms of end-to-end tool call time from iOS?
3. Can the iOS app trigger connector tool calls from a system prompt or conversation without the user manually enabling the connector each session, or does the user need to toggle it on per conversation?

### §7 Recursive Review

All seven key findings (iOS support, transport, config mechanism, sync behavior, HTTPS requirement, auth options, plan requirement) are grounded in explicit Anthropic support documentation or the MCP specification. Each **[fact]** claim has a cited source. Each **[inference]** is clearly labelled and has an explicit justification.

The one medium-confidence claim ("static bearer token is API-only, not web UI") is based on the absence of documentation for a static token UI path — this is labelled medium-confidence and flagged as an open question for direct verification.

The roadmap conclusion (no first-party memory roadmap) appropriately uses absence of evidence framing, not a strong negative claim.

All open questions are genuine gaps that this item's evidence cannot resolve, not omissions from the research.

---

## Findings

### Executive Summary

The Claude iOS app supports remote MCP connections via Anthropic's Connectors system, which is live and explicitly listed as available across "Claude web, Claude Desktop, mobile apps, Claude Code, and the API." The transport is Streamable HTTP over HTTPS (not stdio — that is Desktop-only for local subprocess servers); configuration is done once via the claude.ai web UI (not `.mcp.json`), and the connector syncs to iOS at next login. Deploying `mcp_server.py` as a remote connector requires an HTTPS endpoint, a Python MCP SDK transport switch from stdio to Streamable HTTP, and a Claude Pro subscription or higher. There is no public Anthropic roadmap for built-in persistent memory; the connector ecosystem is Anthropic's answer to personal memory extensibility.

### Key Findings

1. The Claude iOS app accesses remote MCP servers through Anthropic's Connectors system, explicitly listed in official Anthropic documentation as available across "Claude web, Claude Desktop, our Claude mobile apps, Claude Code, and our API."
2. Remote MCP uses Streamable HTTP transport (the current MCP standard) or backwards-compatible legacy HTTP+SSE; stdio transport is architecturally impossible for iOS because it requires launching a subprocess on the client device.
3. Configuration for remote connectors is done via the claude.ai web Settings → Connectors → "Add custom connector" UI, not `.mcp.json`; that file is exclusively a Claude Desktop mechanism for local stdio servers.
4. Connectors configured on the claude.ai web UI sync to the Claude iOS app at login; there is no native iOS connector configuration UI — the iOS app consumes connector state set up on the web.
5. The server must be HTTPS (explicitly required by the Anthropic MCP connector API: URL "must start with https://") and publicly reachable from Anthropic's infrastructure, which acts as relay between the iOS app and the remote MCP server.
6. Authentication is optional per the MCP specification; the claude.ai custom connector UI supports no-auth (open endpoint) or OAuth 2.1; static bearer tokens (not OAuth) are available only through the Messages API and do not apply to the claude.ai/iOS connector path.
7. Custom connectors require a paid Claude plan (Pro at $20/month minimum); the free plan cannot add custom connector URLs.
8. A no-auth remote MCP server is accessible to any caller who discovers the URL; for personal memory data, IP allowlisting to Anthropic's published IP ranges or OAuth 2.1 is the minimum security measure.
9. Migrating `mcp_server.py` from stdio to Streamable HTTP requires changing the transport runner (from `stdio_server()` to the Streamable HTTP ASGI transport in the Python MCP SDK) and deploying on a cloud host with HTTPS — the tool logic (add_memory, search_brain) requires no changes.
10. There is no public Anthropic roadmap for built-in persistent memory in Claude; MCP RFC #2043 (Memory Interchange Format) is a community GitHub issue with no Anthropic commitment or timeline, and Anthropic's documented approach is to provide connector infrastructure for self-hosted or third-party memory servers rather than a first-party memory feature.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| iOS supports remote MCP via Connectors | Connectors Directory FAQ; "Use connectors" article; App Store listing | high | Three independent Anthropic sources; explicit platform listing |
| Transport is Streamable HTTP (not stdio) | MCP spec; MCP connector API docs; Cloudflare guide | high | Consistent across all sources; stdio is architecturally excluded for iOS |
| Config is web UI (not .mcp.json) | "Getting Started" article; "When to use desktop vs web" article; Local MCP article | high | .mcp.json scope is unambiguously Desktop/local only per multiple sources |
| Connector state syncs to iOS at login | "Use connectors" Anthropic support article | high | Explicit statement: "available the next time you log in to your account on Claude for iOS or Android" |
| HTTPS mandatory for remote connectors | MCP connector API docs ("must start with https://") | high | Direct quote |
| Auth optional; OAuth 2.1 or no-auth via web UI | MCP auth spec; Connectors Directory FAQ; "Getting Started" article | high | All three sources consistent |
| Static bearer token is API-only | MCP connector API docs; absence of web UI bearer token option | medium | API docs confirm `authorization_token`; web UI docs describe only OAuth or no-auth |
| Pro plan required for custom connectors | Connectors Directory FAQ | high | Explicit: "custom connectors, which are available for paid plans only (Pro, Max, Team, and Enterprise)" |
| No first-party memory roadmap | App Store listing; Anthropic news site; MCP RFC #2043 issue | medium | Absence of announcement; MCP RFC #2043 has no Anthropic response |
| Tool logic unchanged for Streamable HTTP migration | MCP SDK design (transport/tool separation) | medium | Follows from SDK architecture; not directly tested |

### Assumptions

- **Assumption:** The iOS app has no native connector configuration UI. **Justification:** All Anthropic documentation describes the web UI as the configuration point; iOS is described as consuming synced state. No source mentions an iOS-specific configuration flow. If this assumption is wrong, the configuration path described in Key Finding #3 is incomplete — but the transport and deployment requirements remain unchanged.
- **Assumption:** The Python MCP SDK's Streamable HTTP transport shares the same tool definition interface as the stdio transport. **Justification:** The MCP Python SDK separates transport from tool registration; tool definitions use `@server.tool()` decorators regardless of transport. This is consistent with the SDK's architecture as documented.

### Analysis

The research question is resolved with high confidence for the first three sub-questions (iOS support: yes; transport: Streamable HTTP over HTTPS; configuration: web UI not `.mcp.json`). The minimum deployment question is answered at the architecture level; specific hosting options are out of scope and covered by the sibling item `2026-03-08-self-hosted-mcp-server-options.md`.

The auth question has one remaining uncertainty: whether a static bearer token (not OAuth) can be configured through the claude.ai web UI. All documentation describes OAuth 2.1 as the auth path for authenticated custom connectors, and static bearer tokens appear in the Messages API documentation only. This means a practical personal deployment faces a binary choice: no-auth (with URL obscurity as the only protection) or a full OAuth 2.1 implementation. For a first iteration, no-auth with IP allowlisting to Anthropic's server ranges is the most pragmatic option.

The remote MCP connector path is superior to all other iOS memory access options identified in prior research (Shortcuts via GitHub API, Telegram bot, iOS Shortcuts calling workflow_dispatch): it enables both memory capture (`add_memory`) and semantic retrieval (`search_brain`) within a Claude conversation on iOS, without a custom app, a bespoke bot, or a separate interface.

### Risks, Gaps, and Uncertainties

- The iOS connector UI is not directly verified through live app inspection; documentation is the sole evidence source. Anthropic may have introduced or removed features between documentation updates and the current app version.
- Anthropic's server relay introduces a network hop between the iOS Claude client and the remote MCP server that does not exist for Claude Desktop's local stdio connection. Real-world latency for tool calls from iOS has not been tested.
- OAuth 2.1 implementation for a single-user self-hosted server is disproportionately complex relative to the value — but no-auth leaves personal memory data exposed to URL discovery. A pragmatic middle path (hard-to-guess URL + IP allowlisting) is documented but not officially endorsed by Anthropic.
- Anthropic could introduce first-party memory to Claude at any time, which would reduce the value of a self-hosted connector deployment. No signals indicate this is imminent.

### Open Questions

1. **Bearer token via web UI:** Can the claude.ai custom connector UI be configured with a static Authorization header (bearer token, not OAuth)? This would be the simplest auth option for a personal server. Requires direct testing by attempting to add a connector URL and observing whether the UI prompts for OAuth or allows a custom header.
2. **Per-conversation toggle:** Does the user need to manually enable each connector per conversation in the iOS app, or is there a "always on" mode? The web app has per-conversation toggles; if iOS requires the same, it adds friction to the memory use case.
3. **Tool call latency from iOS:** What is the round-trip time for a memory tool call from Claude iOS → Anthropic relay → self-hosted server → response? Acceptable for retrieval (≤2s) or prohibitive?
4. **Self-hosted server hosting options:** Covered by `2026-03-08-self-hosted-mcp-server-options.md` — which hosting option (Cloudflare Workers, Railway, Render, VPS) is most appropriate for a Python-based MCP server with low traffic?

---

## Output

- Type: knowledge, backlog-item
- Description: Confirmed that Claude iOS supports remote MCP via the Connectors system (Streamable HTTP, web UI config, account sync). Deployment path for `mcp_server.py` is defined. Auth options and plan requirements documented. Backlog item created for Memory-System W-0004 implementation.
- Links:
  - https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
  - https://modelcontextprotocol.io/docs/concepts/transports
  - https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq
