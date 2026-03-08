---
title: "ChatGPT Actions for memory system integration"
added: 2026-03-08
status: backlog
priority: medium
tags: [chatgpt, openai, actions, memory-integration, gpt, custom-gpt]
started: ~
completed: ~
output: [tool, knowledge]
---

# ChatGPT Actions for memory system integration

## Research Question

Can OpenAI's ChatGPT Actions (formerly plugins) be used to connect a Custom GPT to a personal memory system — enabling memory read/write within ChatGPT conversations — and what does a working implementation look like?

## Scope

**In scope:**
- ChatGPT Actions: how they work (OpenAPI schema, authentication, HTTP calls)
- Custom GPT configuration for memory read and write actions
- Hosting the Actions backend: what the endpoint must provide and where to host it
- Auth options: API key (service HTTP auth), OAuth, no-auth
- Behaviour: how ChatGPT invokes actions automatically vs on explicit request
- iOS app support: do Actions work from the ChatGPT iOS app?

**Out of scope:**
- OpenAI Assistants API (separate product from Custom GPTs)
- ChatGPT Enterprise memory features (focus on individual/Plus tier)
- Comparison with Claude MCP (separate research item)

**Constraints:** Must work on ChatGPT Plus (individual tier). Must be operable from the ChatGPT iOS app. Backend must be self-hostable at low cost.

## Context

ChatGPT Custom GPTs support "Actions" — HTTP calls defined by an OpenAPI schema that the GPT can make during a conversation. This is functionally similar to MCP tools but uses a different protocol (REST + OpenAPI rather than the MCP JSON-RPC protocol). For users who use ChatGPT as a primary interface, Actions could provide memory read/write without requiring MCP support.

This item evaluates whether ChatGPT Actions are a viable path for memory integration, and what the implementation effort and limitations are compared to MCP-based approaches.

## Related

**Memory-System backlog:** [W-0005 — ChatGPT Actions memory integration](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — this research item investigates the ChatGPT Actions implementation path for the W-0005 discovery item.

## Approach

1. **Actions mechanism:** Understand how ChatGPT Custom GPT Actions work: OpenAPI schema definition, how the GPT decides when to invoke an action, what data is passed, and how the response is used.
2. **Auth options:** Document the three auth options (no auth, API key, OAuth) and which is appropriate for a personal memory system endpoint.
3. **Backend design:** Design the HTTP API the Actions backend must expose (GET for search/retrieval, POST for capture). Define the OpenAPI schema.
4. **Hosting options:** Identify where to host the backend — same options as the MCP server research (`2026-03-08-self-hosted-mcp-server-options`), but with HTTP/REST rather than MCP transport.
5. **iOS app behaviour:** Test or research whether Actions work from the ChatGPT iOS app (same as desktop, or restricted?).
6. **Prototype:** Build a minimal Custom GPT with a search action pointing at a test memory endpoint. Evaluate the UX: how naturally does ChatGPT invoke the action?
7. **Limitations vs MCP:** Summarise the key differences and trade-offs between Actions and MCP for this use case.

## Sources

- [ ] OpenAI Custom GPT Actions documentation — https://platform.openai.com/docs/actions
- [ ] OpenAI Actions authentication guide — https://platform.openai.com/docs/actions/authentication
- [ ] OpenAI plugin/actions community examples
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0005 — the corresponding discovery item that this research informs

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
