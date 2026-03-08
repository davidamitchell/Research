---
title: "Self-hosted MCP server options for personal memory access"
added: 2026-03-08
status: backlog
priority: high
tags: [mcp, self-hosted, server, memory-access, remote, infrastructure]
started: ~
completed: ~
output: [tool, knowledge]
---

# Self-hosted MCP server options for personal memory access

## Research Question

What are the viable options for self-hosting an MCP server that exposes a personal memory system as callable tools — and which option best satisfies the constraints of low cost, low maintenance, and accessibility from mobile MCP clients?

## Scope

**In scope:**
- Hosting platforms suitable for a lightweight Python or Node MCP server (Fly.io, Railway, Render, Cloudflare Workers, VPS)
- MCP transport options for remote access: SSE, streamable HTTP (the emerging standard)
- TLS, auth, and security requirements for a publicly-accessible MCP endpoint
- Cold start latency and availability characteristics of each platform
- Cost: target < $5/month or free tier

**Out of scope:**
- Local MCP servers (not accessible from mobile)
- Managed MCP hosting services (unless they offer self-hosted configuration)
- MCP servers for non-memory use cases

**Constraints:** The server must be reachable from mobile MCP clients (Claude iOS if/when supported, other mobile AI apps). Must not require a home server or always-on personal hardware.

## Context

The Memory-System requires an MCP server to expose memory tools (search, add, tag, relate) to AI clients. For mobile access — specifically for the Claude iOS integration and any other AI assistant that gains remote MCP support — the server must be publicly accessible over HTTPS. This item researches the hosting landscape: what platforms can run a lightweight MCP server reliably, cheaply, and with the right transport support.

This is a prerequisite for several other research items: the Claude iOS MCP integration (`2026-03-08-claude-ios-mcp-remote-integration`) and any other remote-MCP capture paths.

## Related

**Memory-System backlog:** [W-0014 — Self-hosted MCP server for memory access](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the hosting options that would implement the W-0014 discovery item on making memory tools accessible via MCP.

## Approach

1. **Platform survey:** Evaluate Fly.io, Railway, Render, Cloudflare Workers, and a cheap VPS (Hetzner, DigitalOcean) on the relevant axes: cost, cold-start latency, persistent process vs serverless, TLS included, ease of deployment.
2. **MCP transport compatibility:** Determine which platforms support SSE and streamable HTTP without restriction. Cloudflare Workers in particular has constraints on long-lived connections.
3. **Auth design:** Evaluate options for securing the MCP endpoint: Bearer token (simplest), mTLS, or OAuth. What does each MCP client support?
4. **Deployment workflow:** Design the deployment pipeline — ideally a GitHub Actions push-to-deploy into the chosen platform, with the memory store backend (LanceDB/git) accessible.
5. **Latency test:** Measure round-trip latency from an iPhone to each candidate platform for a representative MCP tool call.
6. **Recommendation:** Select the best option and document the deployment recipe.

## Sources

- [ ] Fly.io free tier and pricing — https://fly.io/docs/about/pricing/
- [ ] Cloudflare Workers limits (connection duration) — https://developers.cloudflare.com/workers/platform/limits/
- [ ] MCP specification: streamable HTTP transport — https://modelcontextprotocol.io/docs/concepts/transports
- [ ] Railway free tier — https://railway.app/pricing
- [ ] Render free tier — https://render.com/pricing
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0014 — the corresponding discovery item that this research informs

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
