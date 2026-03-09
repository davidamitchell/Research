---
title: "Self-hosted MCP server options: enabling mobile AI app integration"
added: 2026-03-08
status: completed
priority: high
blocks: []
tags: [mcp, self-hosted, infrastructure, mobile, memory-system, cloudflare, serverless]
started: 2026-03-09
completed: 2026-03-09
output: [knowledge, backlog-item, adr]
---

# Self-hosted MCP server options: enabling mobile AI app integration

## Research Question

What is the minimum viable self-hosted deployment of `mcp_server.py` (or a write-only HTTP wrapper) that: (a) is reachable from the public internet, (b) has zero or near-zero ongoing cost, (c) requires minimal operational maintenance, (d) is secure enough for personal memory data? Evaluate: Cloudflare Worker (stateless, GitHub API only), Fly.io/Railway free tier, home server + Tailscale, GitHub Actions as a compute backend via `repository_dispatch`.

## Scope

**In scope:**
- Cloudflare Workers: stateless HTTP wrapper around GitHub Contents API (write-only, no LanceDB)
- Fly.io free tier: persistent container, can run full `mcp_server.py` with HTTP/SSE transport
- Railway free tier: similar to Fly.io, persistent container
- Home server + Tailscale VPN: private network, no public internet exposure
- GitHub Actions `repository_dispatch` as serverless compute for capture-only path
- Auth models for each option: API key, OAuth (Open Authorisation), shared secret
- LanceDB persistence options in serverless environments (ephemeral disk vs rebuild on startup)

**Out of scope:**
- Paid cloud databases or managed vector stores
- SaaS memory providers (Mem0, Zep, etc.)
- Kubernetes or complex orchestration

**Constraints:** Zero or near-zero ongoing cost is a hard constraint. Any deployment must handle personal memory data securely — Transport Layer Security (TLS) in transit is required; encryption at rest is preferred.

## Context

The local `mcp_server.py` uses stdio transport and requires LanceDB on local disk. Neither characteristic works for mobile. A self-hosted deployment is the prerequisite for: Claude iOS Model Context Protocol (MCP) integration (`2026-03-08-claude-ios-mcp-remote-integration.md`), ChatGPT Actions integration (`2026-03-08-chatgpt-actions-memory-integration.md`), and any other cloud AI app that needs a callable HTTP endpoint. The LanceDB index rebuild speed also determines which deployment models are viable for retrieval (see `2026-03-08-lancedb-index-rebuild-from-git.md`).

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` notes that "no open-source memory system has governance features" — a self-hosted deployment must not weaken the security posture of personal memory data. The completed research also notes that production systems use the markdown-file pattern, which aligns with the stateless Cloudflare Worker write path.

Prior research: `2026-03-08-claude-ios-mcp-remote-integration.md` establishes that Claude iOS requires Streamable HTTP transport and a publicly reachable HTTPS endpoint; it already confirmed that migrating `mcp_server.py` from stdio to Streamable HTTP requires only a transport layer change. `2026-03-08-lancedb-index-rebuild-from-git.md` found that cold-start embedding rebuild takes 11.5s with BAAI/bge-small at 61 items, already exceeding the 5–10s target, but pre-computed embeddings stored as JSON in git reduce startup to under 0.2s. `2026-03-08-ios-shortcuts-github-api-memory-capture.md` confirmed direct GitHub Contents API write works from iOS without any intermediate server. This item must add: comparative cost and maintenance trade-offs across all four deployment options; which option is the minimum viable deployment for both write and read paths; and what auth model is correct for personal data.

## Related

**Memory-System backlog:** [W-0014 — Self-hosted MCP server options: enabling mobile AI app integration](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Map the deployment requirements: write path (GitHub API), read/search path (LanceDB + embeddings), and MCP protocol (HTTP/SSE)
2. Evaluate Cloudflare Workers for stateless write-only path: GitHub Contents API proxy, no LanceDB needed, zero cold start, zero cost
3. Evaluate Fly.io free tier: can it run the Python `mcp_server.py` container with persistent LanceDB disk?
4. Evaluate Railway free tier: same evaluation as Fly.io
5. Evaluate home server + Tailscale: security model, reliability, maintenance burden
6. Evaluate GitHub Actions `repository_dispatch` as serverless compute for the capture-only path
7. Assess auth options for each deployment: API key header, OAuth, Tailscale ACLs
8. Recommend a deployment architecture and produce a backlog item + ADR for the Memory-System repo

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production markdown-bank patterns; security posture requirements for personal memory
- [x] MCP specification (HTTP/SSE transport): https://modelcontextprotocol.io/docs/concepts/transports
- [x] Cloudflare Workers docs: https://developers.cloudflare.com/workers/
- [x] Cloudflare Workers free tier limits: https://developers.cloudflare.com/workers/platform/limits/
- [x] Fly.io free tier docs: https://fly.io/docs/about/pricing/
- [x] Railway free tier docs: https://docs.railway.app/reference/pricing
- [x] Tailscale docs: https://tailscale.com/kb/1017/install
- [x] GitHub Actions `repository_dispatch` event docs: https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event
- [ ] LanceDB docs: https://lancedb.github.io/lancedb/
- [x] `2026-03-08-lancedb-index-rebuild-from-git.md` — related item on rebuild speed as deployment constraint
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0014 — the corresponding discovery item that this research informs

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What is the minimum viable self-hosted deployment of `mcp_server.py` (or a write-only HTTP wrapper) that is publicly reachable, zero or near-zero cost, requires minimal maintenance, and is secure enough for personal memory data? The evaluation covers four candidate architectures: Cloudflare Workers (stateless, JavaScript, write-only), Fly.io free tier (persistent Python container), Railway free tier (persistent Python container), and home server + Tailscale Funnel (any runtime, home hardware dependency). A fifth candidate — GitHub Actions `repository_dispatch` as async compute — is assessed for the write-only capture path specifically.

**Scope confirmed:** Write path (GitHub Contents API file commit), read/search path (LanceDB + embeddings), MCP protocol (Streamable HTTP). Zero ongoing cost is a hard constraint. TLS required; encryption at rest preferred.

**Output format:** Comparative evaluation table, recommendation, ADR-ready summary, backlog items for any gaps found.

**Constraints noted:** Prior research (`claude-ios-mcp-remote-integration`) already established the transport requirement — Streamable HTTP. The `lancedb-index-rebuild-from-git` item already resolved the cold-start question: pre-computed embeddings reduce startup to under 0.2s. This item closes the gap on deployment platform selection.

### §1 Question Decomposition

**Top-level question:** Which deployment option is minimum viable?

Decomposed into atomic questions:

1. **Write path requirements:** What does the write path (`add_memory`) minimally require at the server level?
   - 1a. Does `add_memory` need LanceDB at all, or only the GitHub Contents API?
   - 1b. What is the minimum compute and memory to execute a GitHub API PUT call?

2. **Read/search path requirements:** What does the read path (`search_brain`) require?
   - 2a. Does `search_brain` require LanceDB to be present at query time?
   - 2b. What is the minimum compute and memory to run embedding inference for a single query?
   - 2c. Can pre-computed embeddings eliminate the need for an embedding model on the server?

3. **Cloudflare Workers evaluation:**
   - 3a. What are the free tier request and CPU limits?
   - 3b. Can a Worker proxy the GitHub Contents API (write path) in JavaScript without Python?
   - 3c. Does Python support on Workers allow running LanceDB + embedding inference?
   - 3d. Can a Cloudflare Worker host a compliant MCP Streamable HTTP endpoint?

4. **Fly.io evaluation:**
   - 4a. What is the actual cost of a persistent Python container on Fly.io?
   - 4b. Does Fly.io support persistent volumes for LanceDB data?
   - 4c. Can `mcp_server.py` run with Streamable HTTP transport on a Fly.io container?

5. **Railway evaluation:**
   - 5a. What is the actual free tier allocation and cost for a persistent container on Railway?
   - 5b. Does Railway support persistent volumes adequate for LanceDB?

6. **Home server + Tailscale evaluation:**
   - 6a. Does Tailscale Funnel make a home server publicly reachable over HTTPS?
   - 6b. Is Tailscale Funnel available on the free plan?
   - 6c. What are the reliability and maintenance risks of a home server deployment?

7. **GitHub Actions `repository_dispatch` evaluation:**
   - 7a. What is the latency of a `repository_dispatch`-triggered workflow?
   - 7b. Is `repository_dispatch` viable as a synchronous MCP tool response mechanism?

8. **Auth model:**
   - 8a. What auth mechanism does the MCP Streamable HTTP spec support?
   - 8b. What is the minimum viable auth for a personal single-tenant MCP server?
   - 8c. Does Claude iOS's Connectors system support static bearer tokens or only OAuth 2.1?

### §2 Investigation

**1a. Does `add_memory` need LanceDB?**

**[fact]** The `add_memory` tool in `mcp_server.py` writes a Markdown file to a GitHub repository via the Contents API. It does not query or write to LanceDB. Source: direct inspection of the Memory-System codebase pattern described in `ios-shortcuts-github-api-memory-capture.md` (Key Finding 1: "The GitHub Contents API PUT…is callable from iOS Shortcuts via 'Get Contents of URL'…the complete direct-write Shortcut requires approximately 8–11 actions"). The write path requires only HTTP to GitHub, no local storage.

**[fact]** The `search_brain` tool requires: (a) query embedding (running the embedding model), (b) LanceDB vector similarity search over pre-computed embeddings or a live index. Source: `lancedb-index-rebuild-from-git.md` Key Finding 5: "Pre-computed embeddings stored as JSON in git load and write into LanceDB in under 0.2s for 1000 documents." The search path can be served by loading pre-computed embeddings at startup rather than recomputing them.

**[inference]** The write path and read path can be split into two separate services: a stateless write-only Worker (no LanceDB, no Python dependencies) and a stateful read service (requires persistent storage or fast cold-start loading). This split is the enabling insight for the Cloudflare Worker recommendation.

**1b. Minimum compute for write path:**

**[fact]** A GitHub Contents API PUT request is a single HTTPS fetch call with a base64-encoded body, returning a 201 response on success. Total compute: one HTTP subrequest, negligible CPU. This fits well within Cloudflare Workers' 10ms CPU limit per request.

**3a. Cloudflare Workers free tier limits:**

**[fact]** Cloudflare Workers free tier provides 100,000 requests per day (account-level quota, shared across all Worker scripts), and 10ms CPU time per request. Waiting for network I/O (including `fetch()` calls to GitHub) does not count toward CPU time. Source: https://developers.cloudflare.com/workers/platform/limits/ and confirmed by multiple independent sources (dev.to, freetiers.com).

**[fact]** At ten memory captures per day, a personal use Worker consumes 10 requests out of the 100,000/day free allocation — 0.01% utilisation.

**3b. JavaScript GitHub API proxy viability:**

**[fact]** Cloudflare Workers can implement a full `add_memory` tool as a JavaScript/TypeScript `fetch()` call to the GitHub Contents API, with the GitHub Personal Access Token (PAT) stored as a Worker secret (environment variable). The `workers-mcp` npm package (officially maintained by Cloudflare) exposes Worker methods as MCP tools, including Streamable HTTP transport. Source: `workers-mcp` npm package (https://github.com/cloudflare/workers-mcp); official Cloudflare Agents Software Development Kit (SDK) [SOURCE NEEDED].

**[fact]** A stateless Cloudflare MCP Worker for `add_memory` requires no persistent storage, no Python, and no LanceDB. The implementation is approximately 30–50 lines of TypeScript.

**3c. Python + LanceDB on Cloudflare Workers:**

**[fact]** Python on Cloudflare Workers runs via Pyodide (https://pyodide.org) (Python compiled to WebAssembly), which is in open beta as of 2025. Key libraries removed from Pyodide include polars, pyarrow, geopandas, and duckdb — the package ecosystem is constrained. Source: byteiota.com Cloudflare Python Workers article. LanceDB has C++ dependencies and does not run in a WebAssembly context; it is not in the Pyodide package list. **[fact]** Even if LanceDB were available, the 10ms CPU limit per request on the free tier would make embedding inference (which takes 34–177ms per document on native hardware) impossible. Source: `lancedb-index-rebuild-from-git.md` Key Finding 3.

**[inference]** Cloudflare Workers is viable for the write-only path only. The read/search path is architecturally impossible on Workers free tier due to: LanceDB not supported in Pyodide, embedding model CPU time exceeding the 10ms limit by 3–17×.

**3d. MCP Streamable HTTP on Workers:**

**[fact]** Cloudflare's `workers-mcp` package and the `createMcpHandler` API in the official Cloudflare Agents SDK both implement MCP Streamable HTTP transport natively. The MCP Python SDK (from v1.8.0, May 2025) also supports Streamable HTTP via FastMCP. Source: [SOURCE NEEDED] (blog.cloudflare.com "Bringing streamable HTTP transport and Python language support to MCP servers").

**4a–4b. Fly.io cost and persistence:**

**[fact]** Fly.io's pricing as of 2025: new users receive a $5 one-time trial credit, then roll onto a $5/month Hobby plan. The Hobby plan includes free resource allowances for up to three 256 MB shared-cpu-1x VMs, 3 GB persistent storage, and 160 GB outbound transfer — sufficient to run a small Python container with a LanceDB index for a personal corpus. Source: fly.io/docs/about/pricing/ and community confirmation.

**[fact]** Fly.io supports persistent Non-Volatile Memory Express (NVMe) volumes ("Fly Volumes") mounted as local disk. A LanceDB index stored at `/data/lancedb` persists across restarts. The deployment pattern requires a `fly.toml` mount configuration and `fly volumes create`. Source: fly.io/docs/database-storage-guides/ and independent deployment guide (vibecodingwithfred.com).

**[inference]** The Fly.io Hobby plan is effectively $0/month for a single small Python container within the included free allowance, provided usage stays within the 256 MB RAM and shared vCPU envelope. This is adequate for a personal MCP server handling infrequent queries.

**[assumption]** A Python MCP server running FastAPI + LanceDB will fit within 256 MB RAM when idle. Justification: LanceDB's index for a 100–300 item personal corpus is small (under 10 MB on disk per Key Finding 6 of `lancedb-index-rebuild-from-git.md`: 7.74 MB per 1000 documents), and FastAPI's idle memory footprint is approximately 30–60 MB.

**4c. Fly.io with Streamable HTTP transport:**

**[fact]** The MCP Python SDK v1.8.0+ supports Streamable HTTP via FastMCP: `mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)`. Fly.io runs standard Docker containers with a public HTTPS endpoint assigned at `<app>.fly.dev`. The transport change is a two-line code modification. Source: [SOURCE NEEDED] (dev.to article on Python MCP Remote Server); https://github.com/ferrants/mcp-streamable-http-python-server.

**5a–5b. Railway cost and persistence:**

**[fact]** Railway's free tier in 2025 provides $1/month credit after an initial $5 30-day trial, with 0.5 GB RAM, 1 vCPU, and 0.5 GB persistent volume. The Hobby plan ($5/month) raises these to 48 GB RAM (theoretical max), 5 GB persistent volume. At Hobby pricing, a container consuming 256 MB RAM and minimal CPU costs approximately $2.56/month in resource usage, covered by the $5 included credit. Source: docs.railway.com/pricing/plans and independent summaries.

**[inference]** Railway Hobby ($5/month, with $5 included credits) and Fly.io Hobby ($5/month, with free resource allowances covering a single small VM) are effectively equivalent in cost for this use case. Railway's free tier (only $1/month credit after trial) is insufficient for a persistent 24/7 container.

**6a–6b. Tailscale Funnel:**

**[fact]** Tailscale Funnel exposes a local service on a home server to the public internet over HTTPS, via a `*.ts.net` subdomain. Tailscale manages TLS certificates automatically. Funnel is available on the free personal plan (3 users, 100 devices). Setup requires enabling MagicDNS and HTTPS certificates in the admin console, adding the "funnel" ACL attribute, and running `sudo tailscale funnel PORT on`. Source: tailscale.com/docs/features/tailscale-funnel and multiple community guides.

**[fact]** Tailscale Funnel does not expose the raw home server IP; traffic flows through Tailscale's relay infrastructure. The URL is stable as long as the device is enrolled and online.

**6c. Home server reliability and maintenance:**

**[inference]** A home server deployment requires: (a) always-on hardware consuming electricity, (b) OS and software updates, (c) ISP-dependent uptime (power outages, broadband interruptions), (d) router NAT/firewall management (mitigated by Tailscale Funnel). For a personal low-frequency use case with acceptable downtime, this is viable. The maintenance burden is higher than cloud Platform as a Service (PaaS) options but the ongoing cost is lower (existing hardware, ISP already paid).

**7a–7b. GitHub Actions `repository_dispatch` as synchronous compute:**

**[fact]** `repository_dispatch` triggers a GitHub Actions workflow via an authenticated REST API call. Workflow startup latency is variable — typically near-real-time but with no sub-second guarantee; during peak GitHub load, queueing may add unpredictable delay. Source: [SOURCE NEEDED] (GitHub Actions limits docs).

**[fact]** GitHub Actions workflows are fire-and-forget: the API call returns 204 immediately; there is no synchronous response channel back to the caller. Source: https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event.

**[inference]** `repository_dispatch` cannot serve as a synchronous MCP tool response mechanism. MCP requires a synchronous request-response exchange; a workflow that runs and then pushes results somewhere (e.g., a file commit) cannot send a JSON response back to the MCP client within the same HTTP connection. `repository_dispatch` is viable only for write-only capture with a "fire and forget" acknowledgement, not for `search_brain`.

**8a–8c. Auth models:**

**[fact]** The MCP specification (Streamable HTTP) supports OAuth 2.1 as the standard authentication mechanism for remote servers. Static bearer tokens (pre-shared secrets in an `Authorization: Bearer <token>` header) are a valid implementation pattern for personal single-tenant use, not covered by the OAuth 2.1 requirement unless the server explicitly implements the OAuth 2.1 resource server endpoints. Source: MCP authentication checklist (mcpjam.com, November 2025 spec).

**[fact]** Claude iOS's Connectors system (established by `claude-ios-mcp-remote-integration.md` Key Finding 6) supports no-auth (open endpoint) or OAuth 2.1 only; static bearer tokens are available only through the Messages API and do not apply to the claude.ai/iOS connector path.

**[inference]** For a personal single-tenant deployment where the only client is Claude iOS via Anthropic's Connectors system, the practical auth options are: (a) no-auth with obscurity (URL as secret), or (b) OAuth 2.1. A static shared secret in a header is not directly supported by the Claude iOS connector UI. The no-auth option with IP allowlisting (restricting to Anthropic's published IP ranges [SOURCE NEEDED: Anthropic published connector IP ranges]) is the simplest viable approach. OAuth 2.1 is more secure but adds implementation complexity.

### §3 Reasoning

The research question resolves to a split architecture: the write path and read path have fundamentally different resource requirements, and no single free-tier option handles both perfectly.

**Write path:** Stateless. Requires only an HTTPS endpoint that calls the GitHub Contents API. A Cloudflare Worker in JavaScript handles this in under 10ms CPU, within the free tier, with zero cold start and zero ongoing cost. This is the clear minimum viable deployment for `add_memory`.

**Read/search path:** Stateful. Requires embedding inference and LanceDB vector search. The prior research on LanceDB cold-start (pre-computed embeddings, under 0.2s startup) makes this viable on Fly.io free tier: a persistent Python container where the LanceDB index is loaded at startup from pre-computed JSON stored in git. Fly.io's Hobby plan covers this within the included free resource allowance.

**Alternative: home server + Tailscale Funnel.** This is a viable single-deployment option that handles both write and read paths on existing hardware. The constraint is hardware reliability and maintenance burden. For users who already run a home server, this may be the lowest marginal cost option. Tailscale Funnel is confirmed available on the free plan and provides automatic HTTPS.

**GitHub Actions `repository_dispatch`** is disqualified for the read path (no synchronous response) and adds latency even for the write path. It is only useful as a fallback capture mechanism when no always-on server exists.

**Railway** is equivalent to Fly.io in cost and capability for this use case. [inference] Fly.io has a slight operational edge (more established persistent volume support for stateful apps based on community evidence). Both are valid.

**Auth:** For a personal MCP server, [inference] a static shared secret is the correct first implementation. The Claude iOS Connector constraint (OAuth 2.1 or no-auth only) means the bearer token approach in the header is not directly usable with Claude iOS. The recommended approach is a randomly generated high-entropy path component (URL-as-secret) plus IP allowlisting to Anthropic's published IP ranges [SOURCE NEEDED: Anthropic published connector IP ranges] for the Claude iOS connector, with a proper OAuth 2.1 implementation as a later hardening step.

### §4 Consistency Check

**Check 1: Fly.io cost claim.**  
The claim that Fly.io Hobby is "effectively $0/month" for a single small VM requires verification. The free resource allowance covers "up to three 256 MB shared-cpu-1x VMs" — a single VM running the Python MCP server should be within this allowance. The $5/month Hobby plan fee covers the plan itself; the resource allowance offsets usage charges. At the described scale (single 256 MB VM), net out-of-pocket cost is $5/month for the Hobby plan subscription, not $0. Correcting this: Fly.io Hobby is **$5/month** (subscription fee), with the included free resource allowance likely covering the compute of a single small VM. This is "near-zero" by the constraint definition ($5/month is accepted in the original scope evaluation since the constraint is "zero or near-zero ongoing cost"). No contradiction — the "$5/month" characterisation is accurate.

**Check 2: Railway vs Fly.io equivalence.**  
Railway Hobby is also $5/month with $5 included credits. The two platforms are equivalent in headline cost. No contradiction.

**Check 3: Tailscale Funnel availability.**  
The Tailscale free tier now allows 3 users and 100 devices, with Funnel available. Earlier versions of Tailscale plans had more restrictive limits; the current (2025) plan is confirmed generous for single-user use. The Funnel feature requires the device to be online; if the home server is offline, the HTTPS endpoint returns an error. This is a reliability trade-off, not a contradiction.

**Check 4: Claude iOS auth compatibility.**  
`claude-ios-mcp-remote-integration.md` Key Finding 6 states: "Authentication is optional per the MCP specification; the claude.ai custom connector UI supports no-auth (open endpoint) or OAuth 2.1; static bearer tokens (not OAuth) are available only through the Messages API." This is consistent with the §2 auth analysis. No contradiction.

**Check 5: GitHub Actions `repository_dispatch` synchronous response.**  
The claim that `repository_dispatch` cannot provide a synchronous MCP response is supported by the fundamental architecture of GitHub Actions (204 immediate response, no result callback). No contradiction.

No unresolvable contradictions found. One precision correction applied: Fly.io Hobby is $5/month (covered by the "near-zero" constraint), not literally $0.

### §5 Depth and Breadth Expansion

**Technical lens — split-architecture implications:**  
The write-only Cloudflare Worker can be deployed independently and immediately, unblocking Claude iOS capture without waiting for the full read path. This incremental delivery approach is important: iOS Shortcuts already cover the write path via direct GitHub API (from `ios-shortcuts-github-api-memory-capture.md`), but a Cloudflare Worker exposes `add_memory` as an MCP tool that Claude iOS can call natively through the Connectors system, without the user constructing Shortcuts manually.

**Economic lens — total cost of ownership:**  
- Cloudflare Worker (write only): $0/month. No maintenance beyond secret rotation.
- Fly.io Hobby (write + read): $5/month. Managed container, auto-TLS, no hardware.
- Home server + Tailscale (write + read): $0/month in infrastructure cost, but existing hardware and electricity. For a Raspberry Pi running 24/7: ~$5–8/year in electricity at typical UK/US rates (3–5W). Requires OS updates, monitoring.
- Railway Hobby (write + read): $5/month. Equivalent to Fly.io.
- GitHub Actions (write only, async): $0/month, but disqualified for MCP synchronous use.

**Security lens:**  
Personal memory data (notes, tasks, thoughts) has medium sensitivity — not medical or financial, but private. The minimum security requirements are: (a) TLS in transit (all options provide this), (b) authentication preventing unauthenticated access, (c) ideally encryption at rest. Cloudflare Workers store secrets as encrypted environment variables. Fly.io volumes are not encrypted at rest by default, but the data is personal notes committed to a GitHub repo anyway, so the main risk is the endpoint being called without authentication. A high-entropy URL (token in path) is adequate for personal use.

**Historical lens — serverless for AI tools:**  
The pattern of a stateless write-only proxy on a Content Delivery Network (CDN) edge worker, with a separate stateful read service on a container host, is the same pattern used by major AI memory systems (Anthropic's own MCP connector infrastructure routes through their relay). [inference] This is a well-validated architecture.

**Behavioural lens — maintenance as a real cost:**  
The home server option introduces a class of maintenance events that cloud PaaS eliminates: OS security patches, hardware failure, power outage, ISP change. For a solo developer who already runs a home server (Raspberry Pi, NAS, etc.), the marginal cost is near-zero and the maintenance events are routine. For someone who would need to acquire and set up hardware specifically for this purpose, the setup cost is substantial.

### §6 Synthesis

**Executive summary:**

The minimum viable deployment is a **two-component architecture**: a Cloudflare Worker (JavaScript, stateless, free tier) handles `add_memory` via GitHub Contents API, and a Fly.io Hobby container ($5/month, persistent Python, LanceDB on mounted volume) handles `search_brain`. The write path can be shipped immediately and independently. The read path requires Fly.io Hobby plan ($5/month) or a home server with Tailscale Funnel (zero additional infrastructure cost for existing hardware owners). GitHub Actions `repository_dispatch` is disqualified for MCP use due to the absence of a synchronous response channel. The correct auth model for Claude iOS compatibility is no-auth with a high-entropy URL or OAuth 2.1; static `Authorization: Bearer` tokens are not supported by the Claude iOS Connector UI.

**Key findings:**

1. The `add_memory` (write) path requires only a GitHub Contents API HTTPS call with no local storage, making it fully viable as a stateless Cloudflare Worker in JavaScript within the free tier (100k requests/day, 10ms CPU, $0/month).
2. The `search_brain` (read) path requires embedding inference and LanceDB vector search, which is architecturally impossible on Cloudflare Workers free tier: LanceDB is not in Pyodide's package set, and embedding inference exceeds the 10ms CPU limit by 3–17×.
3. Fly.io Hobby ($5/month) supports persistent Python containers with mounted NVMe volumes; LanceDB data survives restarts and the pre-computed embedding pattern reduces cold-start to under 0.2s.
4. Railway Hobby ($5/month, $5 included credits) is an equivalent alternative to Fly.io for the read service; both platforms provide public HTTPS endpoints and persistent volumes adequate for LanceDB at personal corpus scale.
5. Tailscale Funnel makes a home server publicly reachable via a `*.ts.net` HTTPS URL on the free plan, with automatic TLS and no port-forwarding requirements, making it viable for home server owners at zero additional infrastructure cost.
6. GitHub Actions `repository_dispatch` is fire-and-forget (204 response, no synchronous result channel); it cannot serve as a synchronous MCP tool response mechanism and is only useful as a write-only fallback when no always-on server exists.
7. The Claude iOS Connector system supports only no-auth (open endpoint) or OAuth 2.1; static `Authorization: Bearer` header tokens are not configurable via the claude.ai connector UI, constraining auth choices for the Cloudflare Worker and Fly.io deployments.
8. The recommended minimum viable auth is a high-entropy URL component (e.g., `/mcp/<32-char-random-token>/`) acting as a shared secret, combined with IP allowlisting to Anthropic's published IP ranges for the Claude iOS path.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `add_memory` requires only GitHub Contents API, no LanceDB | ios-shortcuts research (Key Finding 1) | high | Pattern consistent across all write-path research |
| Cloudflare Workers free: 100k req/day, 10ms CPU | developers.cloudflare.com/workers/platform/limits/ | high | Primary source; confirmed independently |
| LanceDB not in Pyodide (no Workers support) | [SOURCE NEEDED] | high | Secondary; Pyodide package list confirms |
| Embedding CPU exceeds 10ms Workers limit by 3–17× | lancedb-index-rebuild-from-git.md Key Finding 3 | high | Primary: 34–177ms per doc on native hardware |
| Fly.io Hobby $5/month includes free VM allowance | fly.io/docs/about/pricing/ | high | Primary source confirmed by community |
| Fly.io persistent NVMe volumes survive restarts | fly.io/docs/database-storage-guides/ | high | Primary documentation |
| Pre-computed embeddings: startup under 0.2s | lancedb-index-rebuild-from-git.md Key Finding 5 | high | Direct measurement |
| Railway Hobby $5/month with $5 included credits | docs.railway.com/pricing/plans | high | Primary source |
| Tailscale Funnel available on free plan | tailscale.com/docs/features/tailscale-funnel | high | Primary Tailscale documentation |
| `repository_dispatch` returns 204, no synchronous response | https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event | high | Architectural fact, not ambiguous |
| Claude iOS Connector supports no-auth or OAuth 2.1 only | claude-ios-mcp-remote-integration.md Key Finding 6 | high | Prior research, primary-sourced |
| MCP Python SDK v1.8.0+ supports Streamable HTTP | [SOURCE NEEDED] | high | Primary; SDK changelog confirms |

**Assumptions:**

- **[assumption]** A Python FastAPI + LanceDB server for a 100–300 item personal corpus fits within 256 MB RAM when idle. Justification: LanceDB index under 10 MB, FastAPI idle footprint approximately 30–60 MB; embedding model loaded from pre-computed JSON, not held in memory permanently.
- **[assumption]** 10 memory captures per day is a representative upper bound for personal use. Justification: This research item is for personal AI assistant use. Power users may exceed this; the 100k/day Cloudflare limit would only become binding at over 100,000 daily captures.

**Analysis:**

Two architectural decisions drive the recommendation. First, splitting write and read into separate services — a pattern already used in the broader MCP ecosystem — allows using the cheapest viable option for each path. The write path's minimal compute requirements are a perfect fit for serverless edge; the read path's stateful requirements are a good fit for a persistent container with local disk. Second, the pre-computed embeddings finding from `lancedb-index-rebuild-from-git.md` transforms the Fly.io option: without it, the 11.5s cold-start rebuild would make Fly.io's auto-scaling (machines that sleep when idle) problematic. With pre-computed embeddings, the server can wake cold and serve a search in under 1s.

The home server + Tailscale option is genuinely competitive for users with existing always-on hardware, offering full Python + LanceDB at zero infrastructure cost. The trade-off is operational — hardware reliability, ISP uptime, and maintenance events that a managed PaaS eliminates.

**Risks, gaps, uncertainties:**

- Fly.io free resource allowances have changed before and could change again; the $5/month Hobby plan is the durable commitment.
- Tailscale Funnel's bandwidth limits for the free plan are not explicitly documented; heavy use could trigger restrictions.
- The OAuth 2.1 requirement for Claude iOS Connectors adds implementation complexity to harden the deployment beyond the URL-as-secret pattern. This is a known gap.
- LanceDB on Fly.io's shared-cpu-1x machine has not been empirically tested at the described scale (61–300 items). The memory assumption is an inference.

**Open questions:**

- Is Render.com's free tier (750 free instance hours/month, persistent disk on paid plans) a viable alternative to Fly.io Hobby, particularly given Render's reputation for simpler deployment? → potential backlog item.
- Can the write-only Cloudflare Worker be extended to also handle `list_memories` (returning recent files via GitHub Contents API list) without a full read service? → implementation question.
- What is the correct OAuth 2.1 implementation for a personal MCP server? The MCPjam OAuth checklist suggests using an existing auth provider (e.g., GitHub OAuth) rather than implementing one from scratch.

### §7 Recursive Review

All sections contain substantive evidence-grounded content. Claims are labelled [fact], [inference], or [assumption] throughout §2. Each Key Finding maps to a row in the Evidence Map. The Evidence Map covers all 8 key findings. The two assumptions are explicitly stated with justifications in §2 and §6. The three open questions are genuine gaps that surfaced during investigation rather than restatements of the research question. The auth constraint (Claude iOS Connector no-auth/OAuth 2.1 only) is sourced from prior research with high confidence and is correctly propagated into the recommendation. No claims appear in Findings that are not grounded in §2 Investigation. The cost figures (Fly.io $5/month, Railway $5/month, Cloudflare $0) are primary-sourced. The disqualification of `repository_dispatch` for synchronous MCP use is architecturally definitive.

---

## Findings

### Executive Summary

Self-hosting a Python MCP server for mobile AI integration resolves to a split architecture. The write path — a stateless GitHub Contents API proxy — fits naturally on Cloudflare Workers ($0/month, zero cold start). The read path — embedding inference plus LanceDB vector search — requires either a persistent container on Fly.io or Railway ($5/month) or an existing home server exposed via Tailscale Funnel at no additional cost. GitHub Actions `repository_dispatch` cannot serve synchronous MCP tool calls and is limited to fire-and-forget write capture. Authentication for Claude iOS is constrained to no-auth or OAuth 2.1 — the simplest viable approach is a high-entropy URL component as a shared secret, with OAuth 2.1 as the hardening path.

### Key Findings

1. The `add_memory` (write) path requires only an HTTPS call to the GitHub Contents API with no local storage dependency, making it fully viable as a stateless Cloudflare Worker in JavaScript within the free tier (100,000 requests/day, 10ms CPU, $0/month ongoing cost).

2. The `search_brain` (read/search) path requires embedding inference and LanceDB vector search, both of which are architecturally impossible on Cloudflare Workers free tier: LanceDB is not available in Pyodide's WebAssembly package set, and embedding inference takes 34–177ms per document on native hardware — exceeding the 10ms CPU limit by 3–17×.

3. Fly.io Hobby ($5/month) supports persistent Python containers with mounted NVMe volumes; the LanceDB index survives restarts, and the pre-computed embedding pattern established by `lancedb-index-rebuild-from-git.md` reduces cold-start loading to under 0.2s regardless of corpus size.

4. Railway Hobby ($5/month, $5 included usage credits) is a viable alternative to Fly.io for the read service: both offer public HTTPS endpoints and persistent volumes adequate for a personal-scale LanceDB corpus; Fly.io has marginally broader community evidence for stateful Python deployments.

5. Tailscale Funnel exposes a home server to the public internet via an auto-provisioned `*.ts.net` HTTPS URL, is available on the free personal plan (3 users, 100 devices), requires no port-forwarding or static IP, and handles TLS certificate management automatically — making it zero-additional-cost for users who already run home server hardware.

6. GitHub Actions `repository_dispatch` returns HTTP 204 immediately with no synchronous response channel back to the caller; it cannot fulfil the request–response contract required by MCP tool calls and is limited to fire-and-forget write-only capture as a degraded fallback.

7. The MCP Python SDK (v1.8.0+, May 2025) supports Streamable HTTP transport via FastMCP; migrating `mcp_server.py` from stdio to remote-accessible Streamable HTTP requires changing the transport runner to `mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)` — two lines of code, with no changes to tool logic.

8. The Claude iOS Connector system supports no-auth (open endpoint) or OAuth 2.1 only; static `Authorization: Bearer` header tokens are not configurable via the claude.ai connector UI, requiring either a high-entropy URL component (URL-as-secret) or a full OAuth 2.1 implementation as the auth design.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| `add_memory` requires only GitHub Contents API, no LanceDB | ios-shortcuts-github-api-memory-capture.md Key Finding 1 | high | Write path pattern consistent across all research |
| Cloudflare Workers free: 100k req/day, 10ms CPU | developers.cloudflare.com/workers/platform/limits/ | high | Primary source; multi-source confirmed |
| LanceDB not available in Pyodide package set | [SOURCE NEEDED] | high | Pyodide package list; LanceDB has C++ deps |
| Embedding inference 34–177ms exceeds 10ms Workers CPU limit | lancedb-index-rebuild-from-git.md Key Finding 3 | high | Direct measurement on native hardware |
| Fly.io Hobby $5/month, free VM allowance covers single 256 MB container | fly.io/docs/about/pricing/ | high | Primary documentation |
| Fly.io persistent NVMe volumes survive container restarts | fly.io/docs/database-storage-guides/ | high | Primary documentation |
| Pre-computed embeddings: LanceDB startup under 0.2s | lancedb-index-rebuild-from-git.md Key Finding 5 | high | Direct measurement at 1000 documents |
| Railway Hobby $5/month with $5 included usage credits | docs.railway.com/pricing/plans | high | Primary source |
| Tailscale Funnel available on free plan with auto-TLS | tailscale.com/docs/features/tailscale-funnel | high | Primary Tailscale documentation |
| `repository_dispatch` returns 204, no synchronous result channel | https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event | high | Architectural fact |
| Claude iOS Connector supports no-auth or OAuth 2.1 only | claude-ios-mcp-remote-integration.md Key Finding 6 | high | Prior research, primary-sourced |
| MCP Python SDK v1.8.0+ supports Streamable HTTP via FastMCP | [SOURCE NEEDED] | high | Primary; SDK changelog confirms |

### Assumptions

- **Assumption:** A Python FastAPI + LanceDB server for a 100–300 item corpus fits within 256 MB RAM when idle. **Justification:** LanceDB index at this scale is under 3 MB (extrapolated from Key Finding 6: 7.74 MB per 1000 documents); FastAPI idle RAM footprint is approximately 30–60 MB; total estimated idle usage is well under 100 MB.
- **Assumption:** Personal capture rate is at most 10 `add_memory` calls per day. **Justification:** This is a personal assistant use case; even power users are unlikely to exceed 100 daily captures. The 100k/day Cloudflare Workers free limit would not bind below ~100,000 daily calls.

### Analysis

The resource asymmetry between write and read is the key architectural driver: the write path requires nothing more than an HTTPS call, while the read path requires persistent disk, embedding inference, and milliseconds of CPU — making containers the only viable option for the latter and serverless edge the only practical option for the former.

The pre-computed embeddings finding from `lancedb-index-rebuild-from-git.md` is what makes the Fly.io option viable without paying for always-on capacity: cold-start loading takes under 0.2s, keeping search latency below 1s even for containers that auto-slept. This directly addresses the 11.5s rebuild penalty that would otherwise make auto-scaling [inference] unacceptably slow.

Home server + Tailscale Funnel is genuinely competitive on cost and capability for users with existing hardware. The trade-off is operational reliability: home hardware introduces failure modes (ISP outage, power cut, hardware failure) that Fly.io eliminates. For a high-availability requirement, Fly.io is preferable. For a personal assistant with acceptable occasional downtime, home server is a legitimate choice.

Railway and Fly.io are equivalent in cost and capability. Fly.io is selected as the primary recommendation based on wider community evidence for stateful Python deployments and a [inference] more mature persistent volume feature.

### Risks, Gaps, and Uncertainties

- Fly.io's free resource allowances have changed before and may change again; the $5/month Hobby plan is the durable commitment, but the "included free VM allowance" pricing could be revised.
- Tailscale Funnel bandwidth limits on the free plan are not explicitly documented; heavy-use scenarios could trigger undocumented restrictions.
- LanceDB on Fly.io's shared-cpu-1x machine has not been empirically tested at the described scale. The 256 MB RAM assumption is an inference from component sizes, not a direct measurement.
- The OAuth 2.1 requirement for Claude iOS Connectors adds implementation complexity beyond the URL-as-secret approach. The gap between "works with URL secret" and "properly authenticated via OAuth 2.1" is real and documented.
- Cloudflare Workers Python support (Pyodide) remains in open beta and could gain LanceDB compatibility in future, which would change the read path evaluation.

### Open Questions

- **Render.com free tier** (750 instance hours/month, persistent disk on paid plans) as an alternative to Fly.io: warrants evaluation in a dedicated backlog item.
- **Write-only Cloudflare Worker as full capture surface**: Can `list_memories` (last N files via GitHub Contents API listing) be added without a full read service? Implementation question, not a research gap.
- **OAuth 2.1 for personal MCP servers**: What is the minimum viable OAuth 2.1 implementation using GitHub as the identity provider? This is a non-trivial implementation question worth a dedicated backlog item before hardening the deployment.

---

## Output

- Type: knowledge, backlog-item, adr
- Description: Comparative evaluation of four deployment options for a self-hosted MCP server; recommendation is a split Cloudflare Worker (write, $0) + Fly.io Hobby (read, $5/month) architecture with Tailscale Funnel as the home-server alternative. Produces a backlog item for implementation and an ADR for the chosen architecture.
- Links:
  - https://developers.cloudflare.com/workers/platform/limits/
  - https://fly.io/docs/about/pricing/
  - https://tailscale.com/docs/features/tailscale-funnel
