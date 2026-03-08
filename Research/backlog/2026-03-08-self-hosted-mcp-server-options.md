---
title: "Self-hosted MCP server options: enabling mobile AI app integration"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [mcp, self-hosted, infrastructure, mobile, memory-system, cloudflare, serverless]
started: ~
completed: ~
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
- Auth models for each option: API key, OAuth, shared secret
- LanceDB persistence options in serverless environments (ephemeral disk vs rebuild on startup)

**Out of scope:**
- Paid cloud databases or managed vector stores
- SaaS memory providers (Mem0, Zep, etc.)
- Kubernetes or complex orchestration

**Constraints:** Zero or near-zero ongoing cost is a hard constraint. Any deployment must handle personal memory data securely — encryption in transit (TLS) is required; encryption at rest is preferred.

## Context

The local `mcp_server.py` uses stdio transport and requires LanceDB on local disk. Neither characteristic works for mobile. A self-hosted deployment is the prerequisite for: Claude iOS MCP integration (`2026-03-08-claude-ios-mcp-remote-integration.md`), ChatGPT Actions integration (`2026-03-08-chatgpt-actions-memory-integration.md`), and any other cloud AI app that needs a callable HTTP endpoint. The LanceDB index rebuild speed also determines which deployment models are viable for retrieval (see `2026-03-08-lancedb-index-rebuild-from-git.md`).

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` notes that "no open-source memory system has governance features" — a self-hosted deployment must not weaken the security posture of personal memory data. The completed research also notes that production systems use the markdown-file pattern, which aligns with the stateless Cloudflare Worker write path.

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

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — production markdown-bank patterns; security posture requirements for personal memory
- [ ] MCP specification (HTTP/SSE transport): https://modelcontextprotocol.io/docs/concepts/transports
- [ ] Cloudflare Workers docs: https://developers.cloudflare.com/workers/
- [ ] Cloudflare Workers free tier limits: https://developers.cloudflare.com/workers/platform/limits/
- [ ] Fly.io free tier docs: https://fly.io/docs/about/pricing/
- [ ] Railway free tier docs: https://docs.railway.app/reference/pricing
- [ ] Tailscale docs: https://tailscale.com/kb/1017/install
- [ ] GitHub Actions `repository_dispatch` event docs: https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event
- [ ] LanceDB docs: https://lancedb.github.io/lancedb/
- [ ] `2026-03-08-lancedb-index-rebuild-from-git.md` — related item on rebuild speed as deployment constraint
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0014 — the corresponding discovery item that this research informs

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

- Type: knowledge, backlog-item, adr
- Description:
- Links:
