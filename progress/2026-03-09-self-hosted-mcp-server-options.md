# 2026-03-09 — Research Loop (self-hosted-mcp-server-options)

**Completed:**

Research item:
- `Research/completed/2026-03-08-self-hosted-mcp-server-options.md` — completed; the minimum viable deployment is a split architecture: a Cloudflare Worker (JavaScript, stateless, $0/month) for the `add_memory` write path, and a Fly.io Hobby container ($5/month) running full Python `mcp_server.py` with LanceDB on persistent disk for `search_brain`. GitHub Actions `repository_dispatch` is disqualified for MCP use (no synchronous response channel); Tailscale Funnel is a viable zero-cost alternative for home server owners. The Claude iOS Connector system constrains auth to no-auth or OAuth 2.1 only.

Sources consulted:
- https://developers.cloudflare.com/workers/platform/limits/ (Cloudflare Workers free tier limits: 100k req/day, 10ms CPU)
- https://fly.io/docs/about/pricing/ (Fly.io Hobby plan $5/month, includes free VM allowance)
- https://tailscale.com/docs/features/tailscale-funnel (Tailscale Funnel: public HTTPS on free plan, auto-TLS)
