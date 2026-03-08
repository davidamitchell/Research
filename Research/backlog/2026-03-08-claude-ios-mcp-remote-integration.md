---
title: "Claude iOS app + MCP remote server integration"
added: 2026-03-08
status: backlog
priority: high
tags: [claude, ios, mcp, remote-server, mobile, anthropic]
started: ~
completed: ~
output: [tool, knowledge]
---

# Claude iOS app + MCP remote server integration

## Research Question

Does the Claude iOS app support connecting to remote MCP servers, and if so, what does a working integration look like for exposing a personal memory system as an MCP tool callable from Claude on iPhone?

## Scope

**In scope:**
- Claude iOS app's current MCP support (remote servers, transport protocols)
- MCP transport options compatible with mobile clients (SSE, HTTP, WebSocket)
- Hosting a minimal remote MCP server accessible from the Claude iOS app
- Authentication between Claude iOS and the remote MCP server
- Practical latency and reliability considerations for mobile use

**Out of scope:**
- Claude Desktop MCP configuration (separate, well-documented)
- Local MCP servers running on a Mac (not relevant for iOS-only use)

**Constraints:** Must be operable from iPhone with no Mac required. Remote server must be hostable at low cost.

## Context

Claude Desktop has mature MCP support, but the iOS app's MCP capabilities are less documented. If Claude iOS can connect to remote MCP servers over SSE or HTTP, it becomes possible to expose the Memory-System as an MCP tool — letting Claude on iPhone query, search, and add memories in the course of a conversation. This would be a high-value integration with no new UI to build: the Claude app becomes the interface.

The critical unknown is whether the Claude iOS app currently supports remote MCP connections at all, and if so, what the configuration path looks like (there is no `~/.claude/mcp.json` on iOS).

## Related

**Memory-System backlog:** [W-0004 — Claude iOS MCP remote integration](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the technical feasibility and implementation path for the W-0004 discovery item.

## Approach

1. **Current state of Claude iOS MCP support:** Determine what MCP features (if any) are available in the Claude iOS app as of the research date — official documentation, release notes, community reports.
2. **Transport protocol requirements:** If remote MCP is supported, what transport is required? SSE (Server-Sent Events), streamable HTTP, or WebSocket? What are the URL format and auth header expectations?
3. **Server hosting design:** Design a minimal remote MCP server (using the Python or TypeScript MCP SDK) that exposes Memory-System read/write as tools. Identify the cheapest viable hosting option.
4. **Auth between Claude iOS and the server:** How does Claude iOS pass credentials to the remote MCP server? Bearer token? OAuth? Pre-configured per-server auth?
5. **End-to-end prototype:** If the iOS app supports remote MCP, build a working demo: Claude on iPhone calls a memory tool, the server queries the memory store, and a result is returned in the conversation.
6. **Fallback if iOS MCP is unsupported:** Document what is blocked and what timeline/signals suggest when this will become available.

## Sources

- [ ] Anthropic Claude iOS app release notes — https://support.anthropic.com/
- [ ] MCP specification: remote transport (SSE and streamable HTTP) — https://modelcontextprotocol.io/docs/concepts/transports
- [ ] MCP Python SDK — https://github.com/modelcontextprotocol/python-sdk
- [ ] Community reports on Claude iOS MCP support
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0004 — the corresponding discovery item that this research informs

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
