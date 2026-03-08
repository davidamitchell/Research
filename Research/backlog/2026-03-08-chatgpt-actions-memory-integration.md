---
title: "ChatGPT Actions and custom GPTs: external memory integration options"
added: 2026-03-08
status: backlog
priority: low
blocks: []
tags: [mobile, chatgpt, openai, actions, memory-system]
started: ~
completed: ~
output: [knowledge]
---

# ChatGPT Actions and custom GPTs: external memory integration options

## Research Question

Can a ChatGPT custom GPT be configured with Actions that: (a) call a self-hosted HTTP endpoint to add a memory, (b) call `search_brain` before responding to surface relevant context? What is OpenAI's native Memory API — is there any export/import hook to sync ChatGPT's built-in memories into this repo? What are the auth and hosting requirements?

## Scope

**In scope:**
- OpenAI Actions spec (OpenAPI schema) for custom GPTs
- Custom GPT configuration: Actions targeting a self-hosted write endpoint
- Retrieval integration: custom GPT system prompt + Actions calling `search_brain`
- OpenAI's native Memory API (if any): export/import hooks, API access to stored memories
- Auth model for custom GPT Actions: OAuth, API key, bearer token
- Hosting requirement for the Actions endpoint (see `2026-03-08-self-hosted-mcp-server-options.md`)
- Comparison with Claude iOS MCP path (`2026-03-08-claude-ios-mcp-remote-integration.md`)

**Out of scope:**
- OpenAI API for model inference (not relevant to memory integration)
- OpenAI Assistants API thread memory (different product)
- Building a full OpenAI plugin (deprecated in favour of Actions)

**Constraints:** Lower priority than Claude iOS given the owner's primary tool stack. Research should be sufficient to make a build/no-build decision without requiring a prototype.

## Context

ChatGPT is the most widely used AI app on iOS. Custom GPT Actions support OpenAPI-spec HTTP calls to any endpoint. If a write-only HTTP endpoint exists (see `2026-03-08-self-hosted-mcp-server-options.md`), a custom GPT could capture memories from any ChatGPT conversation and retrieve relevant context before responding.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` explicitly notes that "ChatGPT memories don't export to Claude, Cursor rules don't transfer to Windsurf" — this item explores whether that silo can be broken via a custom GPT that writes to the shared Memory-System repo. This would make memories portable across AI tools. Lower priority than Claude iOS because the owner's primary tool stack uses Claude, but the portability angle is strategically important.

## Related

**Memory-System backlog:** [W-0005 — ChatGPT Actions and custom GPTs: external memory integration options](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md) — the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Review OpenAI's custom GPT Actions documentation and OpenAPI spec requirements
2. Identify whether a write-only HTTP endpoint (GitHub Contents API proxy) is sufficient for capture Actions
3. Review OpenAI's native Memory API: is there a documented API for reading or exporting ChatGPT memories?
4. Design a custom GPT system prompt that retrieves context from `search_brain` via an Action before responding
5. Assess auth options for custom GPT Actions: OAuth, API key, shared secret
6. Evaluate hosting requirement overlap with `2026-03-08-self-hosted-mcp-server-options.md`
7. Compare the ChatGPT Actions path vs the Claude iOS MCP path on implementation complexity and maintenance

## Sources

- [ ] `Research/completed/2026-03-02-agent-memory-management-context-injection.md` — memory portability findings; "ChatGPT memories don't export to Claude"
- [ ] OpenAI custom GPT Actions documentation: https://platform.openai.com/docs/actions/introduction
- [ ] OpenAI custom GPT Actions authentication: https://platform.openai.com/docs/actions/authentication
- [ ] OpenAI Memory documentation: https://help.openai.com/en/articles/8590148-memory-faq
- [ ] OpenAPI specification (for Actions schema): https://swagger.io/specification/
- [ ] `2026-03-08-self-hosted-mcp-server-options.md` — prerequisite infrastructure item
- [ ] `2026-03-08-claude-ios-mcp-remote-integration.md` — comparison item
- [ ] `davidamitchell/Memory-System` BACKLOG.md W-0005 — the corresponding discovery item that this research informs

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

- Type: knowledge
- Description:
- Links:
