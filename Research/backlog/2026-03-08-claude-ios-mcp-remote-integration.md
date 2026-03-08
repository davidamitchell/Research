---
title: "Claude for iOS: MCP remote integration for memory capture and retrieval"
added: 2026-03-08
status: backlog
priority: high
blocks: []
tags: [mobile, claude, ios, mcp, memory-system, self-hosted]
started: ~
completed: ~
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

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — MCP RFC #2043 (Memory Interchange Format); memory portability as first-class concern
- [ ] MCP specification (transport section): https://modelcontextprotocol.io/docs/concepts/transports
- [ ] Anthropic MCP remote transport docs: https://www.anthropic.com/news/model-context-protocol
- [ ] Claude iOS App Store page (release notes): https://apps.apple.com/app/claude-by-anthropic/id6473753684
- [ ] Anthropic developer docs: https://docs.anthropic.com/
- [ ] MCP GitHub repository (issues and discussions on remote transport): https://github.com/modelcontextprotocol/modelcontextprotocol
- [ ] `2026-03-08-self-hosted-mcp-server-options.md` — prerequisite infrastructure research

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

- Type: knowledge, backlog-item
- Description:
- Links:
