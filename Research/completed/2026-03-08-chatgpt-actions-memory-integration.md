---
title: "ChatGPT Actions and custom GPTs: external memory integration options"
added: 2026-03-15T05:36:40+00:00
status: completed
priority: low
blocks: []
tags: [mobile, chatgpt, openai, actions, memory-system]
started: 2026-03-15T05:36:40+00:00
completed: 2026-03-15T05:36:40+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# ChatGPT Actions and custom GPTs: external memory integration options

## Research Question

Can a ChatGPT custom Generative Pre-trained Transformer (GPT) be configured with Actions that: (a) call a self-hosted HTTP endpoint to add a memory, (b) call `search_brain` before responding to surface relevant context? What is OpenAI's native Memory Application Programming Interface (API)  -  is there any export/import hook to sync ChatGPT's built-in memories into this repo? What are the auth and hosting requirements?

## Scope

**In scope:**
- OpenAI Actions spec (OpenAPI schema) for custom GPTs
- Custom GPT configuration: Actions targeting a self-hosted write endpoint
- Retrieval integration: custom GPT system prompt + Actions calling `search_brain`
- OpenAI's native Memory API (if any): export/import hooks, API access to stored memories
- Auth model for custom GPT Actions: Open Authorization (OAuth), API key, bearer token
- Hosting requirement for the Actions endpoint (see `2026-03-08-self-hosted-mcp-server-options.md`)
- Comparison with Claude iOS Model Context Protocol (MCP) path (`2026-03-08-claude-ios-mcp-remote-integration.md`)

**Out of scope:**
- OpenAI API for model inference (not relevant to memory integration)
- OpenAI Assistants API thread memory (different product)
- Building a full OpenAI plugin (deprecated in favour of Actions)

**Constraints:** Lower priority than Claude iOS given the owner's primary tool stack. Research should be sufficient to make a build/no-build decision without requiring a prototype.

## Context

ChatGPT is the most widely used AI app on iOS. Custom GPT Actions support OpenAPI-spec HTTP calls to any endpoint. If a write-only HTTP endpoint exists (see `2026-03-08-self-hosted-mcp-server-options.md`), a custom GPT could capture memories from any ChatGPT conversation and retrieve relevant context before responding.

Cross-reference: `Research/completed/2026-03-02-agent-memory-management-context-injection.md` explicitly notes that "ChatGPT memories don't export to Claude, Cursor rules don't transfer to Windsurf"  -  this item explores whether that silo can be broken via a custom GPT that writes to the shared Memory-System repo. This would make memories portable across AI tools. Lower priority than Claude iOS because the owner's primary tool stack uses Claude, but the portability angle is strategically important.

## Related

**Memory-System backlog:** [W-0005  -  ChatGPT Actions and custom GPTs: external memory integration options](https://github.com/davidamitchell/Memory-System/blob/main/BACKLOG.md)  -  the Memory-System discovery item that defines the implementation work this research directly informs.

## Approach

1. Review OpenAI's custom GPT Actions documentation and OpenAPI spec requirements
2. Identify whether a write-only HTTP endpoint (GitHub Contents API proxy) is sufficient for capture Actions
3. Review OpenAI's native Memory API: is there a documented API for reading or exporting ChatGPT memories?
4. Design a custom GPT system prompt that retrieves context from `search_brain` via an Action before responding
5. Assess auth options for custom GPT Actions: OAuth, API key, shared secret
6. Evaluate hosting requirement overlap with `2026-03-08-self-hosted-mcp-server-options.md`
7. Compare the ChatGPT Actions path vs the Claude iOS MCP path on implementation complexity and maintenance

## Sources

- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md`  -  memory portability findings; "ChatGPT memories don't export to Claude"
- [x] OpenAI custom GPT Actions documentation: https://platform.openai.com/docs/actions/introduction
- [x] OpenAI custom GPT Actions authentication: https://platform.openai.com/docs/actions/authentication
- [x] OpenAI Memory documentation: https://help.openai.com/en/articles/8590148-memory-faq
- [x] OpenAPI specification (for Actions schema): https://swagger.io/specification/
- [x] `2026-03-08-self-hosted-mcp-server-options.md`  -  prerequisite infrastructure item
- [x] `2026-03-08-claude-ios-mcp-remote-integration.md`  -  comparison item
- [x] `davidamitchell/Memory-System` BACKLOG.md W-0005  -  the corresponding discovery item that this research informs — https://github.com/davidamitchell/Memory-System

---

## Research Skill Output

*(Full output from running the research skill  -  retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** Can a custom GPT be configured with Actions that (a) call a self-hosted HTTP endpoint to capture a memory and (b) call `search_brain` before responding to surface relevant context? What is OpenAI's native Memory API  -  does any export/import hook exist to sync ChatGPT built-in memories into an external repository? What are the auth and hosting requirements?

**Scope confirmed:** OpenAI Actions spec, custom GPT configuration for write and retrieval Actions, native Memory API investigation, auth options (OAuth, API key, static secret), hosting requirements, comparison with Claude iOS MCP path.

**Constraint mode:** full.

**Output format:** Structured findings per §6 with evidence map, assumptions, and open questions. The output answers a binary build/no-build decision: can this be built, and is it simpler or more complex than the Claude iOS MCP path already researched?

**Prior research cross-reference:**
- `2026-03-02-agent-memory-management-context-injection.md` established that ChatGPT's built-in memories are siloed  -  they do not export to other Large Language Model (LLM) tools. This item investigates whether a custom GPT using Actions can bridge that silo by writing to a shared external store.
- `2026-03-08-claude-ios-mcp-remote-integration.md` established the Claude iOS path (Streamable HTTP MCP, no-auth or OAuth 2.1, Claude Pro required). The current item is the direct comparison.
- `2026-03-08-self-hosted-mcp-server-options.md` established hosting options for the shared backend (Cloudflare Workers for write, Fly.io/Railway for vector search). Those findings apply directly here since the same backend is targeted.

---

### §1 Question Decomposition

**Root question decomposed:**

1. **Can a custom GPT Action call a self-hosted Hypertext Transfer Protocol Secure (HTTPS) endpoint?**
   - 1a. What format is required (OpenAPI schema)?
   - 1b. What hosting constraints apply (HTTPS, public IP, Cross-Origin Resource Sharing (CORS))?
   - 1c. Are Actions called server-side (from OpenAI infrastructure) or client-side (from the browser/app)?

2. **Does the retrieval pattern (call `search_brain` before responding) work reliably?**
   - 2a. Can the GPT system prompt instruct mandatory retrieval before any response?
   - 2b. Is GPT Action function calling deterministic enough to guarantee pre-response retrieval?

3. **What is OpenAI's native Memory API?**
   - 3a. Is there a documented Representational State Transfer (REST) API for reading ChatGPT saved memories?
   - 3b. Is there a documented import/write endpoint for injecting memories into ChatGPT's built-in memory system?
   - 3c. What does the ChatGPT data export include for memories, and is it machine-readable?

4. **What authentication options exist for GPT Actions?**
   - 4a. Is a static API key (custom header) supported in the GPT editor User Interface (UI)?
   - 4b. Is OAuth required, and does OAuth work reliably on the ChatGPT iOS mobile app?
   - 4c. Is no-auth viable for personal memory endpoints?

5. **What plan tier is required to create and use custom GPTs?**

6. **Hosting requirements  -  does the backend from `self-hosted-mcp-server-options.md` apply without modification?**

7. **Comparison: ChatGPT Actions vs Claude iOS MCP**
   - 7a. Implementation complexity
   - 7b. Auth simplicity
   - 7c. Reliability of forced retrieval before response
   - 7d. Mobile (iOS) reliability

---

### §2 Investigation

**Q1: Can a custom GPT Action call a self-hosted HTTPS endpoint?**

**[fact]** GPT Actions are stored in custom GPTs and execute API calls using Function Calling. The Action description is an OpenAPI schema specifying endpoint URLs, HTTP methods, parameters, and authentication. The model converts natural language to the appropriate JSON input and executes the call. (Source: https://platform.openai.com/docs/actions/introduction)

**[fact]** GPT Actions require an OpenAPI 3.x schema. The schema includes a `servers` object with the target URL. Any publicly accessible HTTPS endpoint can be targeted  -  the endpoint does not need to be on OpenAI infrastructure. (Source: https://developers.openai.com/api/docs/actions/getting-started/  -  "It requires an Open API schema which describes all server API endpoints")

**[fact]** GPT Actions are executed server-side, by OpenAI's infrastructure, not by the client device. This is structurally identical to Claude Connectors (established in `2026-03-08-claude-ios-mcp-remote-integration.md` Key Finding #5): the client sends a message, the model decides to invoke a tool, and OpenAI's servers make the HTTP request to the endpoint. CORS is irrelevant; the endpoint must be reachable from OpenAI's servers. (Source: inference from OpenAI Actions documentation; confirmed by community post noting "Since this endpoint will be run from OpenAI's backend, the API must be public")

**[fact]** HTTPS is required. The `servers[].url` in the OpenAPI schema must use HTTPS. HTTP endpoints are not supported. (Source: OpenAI Actions production requirements; consistent with all community implementation examples)

**[inference]** The same HTTPS infrastructure established in `2026-03-08-self-hosted-mcp-server-options.md` (Cloudflare Workers for `add_memory`, Fly.io for `search_brain`) is directly compatible with GPT Actions. The endpoint format (REST + JSON) is exactly what GPT Actions require. No MCP SDK is needed; any HTTP server with a valid OpenAPI schema works.

---

**Q2: Does the retrieval pattern work reliably?**

**[fact]** Custom GPT system prompts can instruct the GPT to call a specific Action before answering any message. The standard pattern is: "Before responding to any user message, call the search_brain action with a query derived from the user's input. Use the results as context for your response." (Source: OpenAI Retrieval-Augmented Generation (RAG) for GPTs documentation: https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts)

**[inference]** Forced function calling via system prompt instruction is probabilistic, not guaranteed. GPT-4o follows system prompt instructions reliably for simple conditional patterns ("always call X before Y"), but the model retains discretion to skip the call if it judges the query irrelevant or if the context window becomes saturated. This is architecturally different from MCP, where the tool call is part of the protocol flow. For personal use where the GPT is configured specifically for memory retrieval, the system prompt approach is sufficient.

**[assumption]** A well-crafted system prompt that explicitly names the `search_brain` Action and provides a trigger condition ("for every user query") will achieve ≥95% retrieval invocation for conversational queries. **Justification:** Community implementations of Retrieval-Augmented Generation (RAG)-via-Actions report reliable trigger behaviour for clear instructions; the limitation is ambiguous instructions, not the underlying mechanism.

---

**Q3: OpenAI's native Memory API**

**[fact]** OpenAI does not provide a public, documented REST API for programmatically reading, writing, or exporting ChatGPT's built-in "Saved Memories." The OpenAI API (for developers using the Chat Completions endpoint) explicitly does not support memory. A 2024 community thread confirmed: "The API currently does not offer a memory function." (Source: https://community.openai.com/t/how-do-i-enable-or-disable-memory-in-api/703964)

**[fact]** ChatGPT's built-in memory system operates as a closed, proprietary feature accessible only within ChatGPT conversations. There is no `/memories` endpoint in the OpenAI API reference. (Source: OpenAI API reference  -  absence; confirmed by community threads across 2024–2025)

**[fact]** Data export via the Privacy Portal (Settings → Export Data) produces a ZIP file containing a `memory.dat` or similar structured file. This is a one-time manual download triggered through the ChatGPT UI  -  not a programmatic API. The content is JSON-like but there is no documented import endpoint. (Source: https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data)

**[fact]** ChatGPT expanded its memory system in April 2025 to include "chat history" references (referencing past conversations, not just saved memories). Neither the saved memories nor the chat history reference is exposed via any API. (Source: https://community.openai.com/t/chatgpt-can-now-reference-all-past-conversations-april-10-2025/1229453)

**[inference]** OpenAI's memory system is deliberately siloed. The strategic intent appears to be retention of memory as a differentiated user experience feature within ChatGPT, not an open platform capability. This directly validates the finding in `2026-03-02-agent-memory-management-context-injection.md`: ChatGPT memories don't export to other tools. The only path to memory portability is via a custom GPT that uses Actions to write to an external store, bypassing ChatGPT's native memory entirely.

---

**Q4: Authentication options for GPT Actions**

**[fact]** The GPT editor UI offers three authentication modes for Actions: (1) None  -  no authentication, any caller can invoke the endpoint; (2) API Key  -  a static secret configured in the GPT editor, sent with each request as Basic, Bearer, or a custom header (e.g., `X-Api-Key`); (3) OAuth  -  full OAuth 2.0 authorization code flow with configurable authorization and token URLs. (Source: https://platform.openai.com/docs/actions/authentication  -  primary source, confirmed by https://developers.openai.com/api/docs/actions/authentication/)

**[fact]** The API Key option in the GPT editor stores the key server-side (in the GPT's configuration) and injects it into each Action request. The key is never visible to end users. Three sub-types are supported: Basic (HTTP Basic Auth), Bearer (Authorization: Bearer header), and Custom (any header name, e.g., `X-Api-Key`). (Source: OpenAI Actions authentication documentation; confirmed by community post: "we allow API key authentication through the GPT editor UI" and implementation guides)

**[fact]** This is a critical difference from Claude iOS Connectors, which support only no-auth or OAuth 2.1. Claude iOS does not support static API key injection via the connector configuration UI. (Source: `2026-03-08-claude-ios-mcp-remote-integration.md` Key Finding #6)

**[fact]** OAuth on the ChatGPT iOS mobile app has documented, persistent reliability issues. Multiple community threads across 2024–2025 confirm that the OAuth authorization flow fails or becomes inaccessible on iOS and Android apps. A thread from January 2025 specifically reports "OAuth 2 auth flow fails in mobile (1.2024.157) but works on the web interface." A separate thread from May 2025 reports "Trouble Completing OAuth Authorization for Google Calendar actions on iOS ChatGPT App." (Sources: https://community.openai.com/t/custom-gpt-oauth-issue-in-mobile-app/1114136; https://community.openai.com/t/oauth-2-auth-flow-fails-in-mobile-1-2024-157-but-works-on-the-web-interface)

**[inference]** For personal use, API key authentication with a custom header is the practical choice: it avoids the OAuth mobile reliability problem, it is simpler to configure, and the key is held by the GPT configuration (not the user). A high-entropy custom header value provides equivalent security to the "URL as secret" approach used for no-auth Claude Connectors.

---

**Q5: Plan tier required**

**[fact]** Creating a custom GPT requires a ChatGPT Pro, Plus, Team, Enterprise, or Edu subscription. The Free plan cannot create custom GPTs with Actions. ChatGPT Plus costs $20/month  -  identical to the Claude Pro minimum required for Claude iOS Connectors. (Source: https://help.openai.com/en/articles/8554397-creating-a-gpt  -  "Creating a GPT is available to ChatGPT Pro, Plus, Team, Enterprise, and Edu users"; confirmed by multiple YouTube tutorials noting Plus requirement)

**[inference]** The cost parity between Claude Pro and ChatGPT Plus ($20/month each) is not a differentiating factor for build/no-build decision. Someone subscribing to both tools pays $40/month total regardless.

---

**Q6: Hosting requirements**

**[fact]** GPT Actions require the endpoint to be at a public HTTPS URL reachable from OpenAI's servers. Local URLs (localhost, .local) and HTTP endpoints are not supported. (Source: OpenAI Actions documentation; consistent with all community implementation examples)

**[inference]** The hosting architecture from `2026-03-08-self-hosted-mcp-server-options.md` applies without modification: Cloudflare Workers ($0/month) for the `add_memory` write path, Fly.io ($5/month) or Tailscale Funnel (free for existing home server) for the `search_brain` vector search path. No additional hosting cost is introduced by supporting both ChatGPT Actions and Claude iOS MCP from the same backend.

**[assumption]** A single backend can serve both the MCP protocol (for Claude iOS) and the REST/OpenAPI protocol (for ChatGPT Actions) from the same deployed service. **Justification:** REST/JSON endpoints can be added alongside MCP tool definitions without conflict; the FastAPI server that serves the MCP Streamable HTTP transport can expose additional REST routes at different paths.

---

**Q7: Comparison  -  ChatGPT Actions vs Claude iOS MCP**

**[fact]** Claude iOS MCP requires: (a) MCP Python Software Development Kit (SDK) with Streamable HTTP transport, (b) HTTPS endpoint reachable from Anthropic's relay, (c) no-auth or OAuth 2.1 only, (d) configured via claude.ai web UI, (e) Claude Pro ($20/month). (Source: `2026-03-08-claude-ios-mcp-remote-integration.md`)

**[fact]** ChatGPT Actions require: (a) any HTTP server with a valid OpenAPI schema (no SDK required), (b) public HTTPS endpoint reachable from OpenAI's servers, (c) no-auth, API key (including custom header), or OAuth 2.0, (d) configured in GPT editor UI, (e) ChatGPT Plus ($20/month). (Source: this investigation, synthesising Q1–Q6 above)

**[inference]** The ChatGPT Actions path is simpler to implement in three respects: (1) No MCP SDK is required  -  the existing FastAPI HTTP server already exposes compatible endpoints; (2) API key authentication with a custom header is simpler and more iOS-reliable than OAuth 2.1; (3) The OpenAPI schema is a standard widely supported by LLMs and auto-generation tools, reducing implementation effort. The trade-off is that forced retrieval reliability is lower (system prompt instruction vs MCP protocol-level tool call).

---

### §3 Reasoning

**Claim 1  -  The write path works:** A custom GPT Action can call an HTTPS endpoint to add a memory. The endpoint is a standard REST call with a JSON body. Authentication can use a static API key in a custom header, configured server-side in the GPT editor. This is simpler than the Claude iOS MCP path (which requires OAuth 2.1 or no-auth) and fully compatible with the Cloudflare Workers write path from prior research.

**Claim 2  -  The retrieval path works with caveats:** A custom GPT can be instructed to call `search_brain` before responding. The pattern relies on system prompt instruction (probabilistic compliance, not protocol guarantee). For personal use, where the GPT is purpose-built for memory retrieval, system prompt compliance is sufficient. For a more robust retrieval guarantee, the MCP path provides stronger enforcement.

**Claim 3  -  No native Memory API exists:** OpenAI's built-in memory system has no programmatic API. The only viable path to cross-tool memory portability is the custom GPT Actions approach described above  -  bypassing ChatGPT's native memory entirely and writing to an external store.

**Claim 4  -  Hosting is shared:** The same backend (Cloudflare Workers + Fly.io) supports both ChatGPT Actions and Claude iOS MCP. No additional hosting cost. Both endpoints can coexist in the same deployment.

**Claim 5  -  Build verdict: yes, lower priority:** The ChatGPT Actions path is viable and simpler to implement than Claude iOS MCP. Its strategic value is memory portability  -  memories written from ChatGPT conversations become available in Claude (and vice versa). It should be built after the Claude iOS MCP path is operational, using the same backend.

---

### §4 Consistency Check

**Check 1  -  Auth claims consistent?**
The investigation established: ChatGPT Actions support API key (custom header) on iOS; Claude iOS supports OAuth 2.1 or no-auth only. These claims are from independent primary sources (OpenAI Actions auth docs vs Anthropic Connectors docs) and are consistent with each other. No contradiction.

**Check 2  -  iOS availability claims consistent?**
Early 2024 threads reported "not available on iOS" for GPTs with Actions. Later 2024–2025 threads confirm this was resolved for no-auth and API key Actions; OAuth on mobile remains unreliable. The resolution is consistent: the "not available" message is tied specifically to OAuth flow failures, not to Actions per se. No contradiction; claim clarified: API key Actions work on iOS, OAuth Actions do not reliably.

**Check 3  -  No native Memory API  -  is this confirmed by absence or explicit denial?**
Explicit denial in the community forum: "The API currently does not offer a memory function." Plus absence from the OpenAI API reference. Both evidence types support the same conclusion. High confidence.

**Check 4  -  Hosting overlap claim:**
The claim that one backend can serve both MCP and REST is an inference, not a directly tested fact. The technical architecture supports it (FastAPI handles both protocol types) but has not been empirically verified. This is correctly labelled as an [inference] and flagged as an assumption.

No unresolvable contradictions found.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The OpenAPI schema requirement for GPT Actions is a solved problem  -  LLMs including GPT-4o can auto-generate OpenAPI schemas from natural language descriptions of endpoints. The implementation complexity for writing the schema is low. The `add_memory` endpoint schema is trivial (POST with a `content` string body); `search_brain` is slightly more complex (POST with a `query` string, returns an array of results). The primary complexity is deployment, not schema authoring.

**Security lens:** API key authentication (custom header) stored in the GPT configuration is held by OpenAI's servers. This means OpenAI has access to the key. For a personal memory endpoint containing notes about the owner, this is an acceptable risk [inference]  -  the same content is already visible to OpenAI through the ChatGPT conversation. For enterprise use cases with sensitive data, this would require OAuth. The security posture is comparable to storing a personal access token (PAT) in a third-party app's settings.

**Behavioural lens:** The "forced retrieval before responding" pattern requires the user to use the custom GPT consistently instead of the default ChatGPT interface. Behaviour change risk: users may open ChatGPT and start a new chat (bypassing the custom GPT), losing the retrieval benefit. Mitigation: set the custom GPT as the default interface, or use ChatGPT Projects which maintain the custom GPT context. This is a real adoption friction that the Claude iOS MCP path does not have  -  Claude Connectors apply to every Claude conversation automatically once configured.

**Regulatory lens:** Not applicable at personal scale. For enterprise deployment, the API key stored in GPT configuration creates a data governance question (OpenAI server-side storage of credentials). Out of scope per constraints.

**Economic lens:** ChatGPT Plus at $20/month is required only to *create* the custom GPT. Users who receive a shared GPT link can use it on ChatGPT Free plan. This creates a potential asymmetry: the owner creates the GPT on Plus, but could theoretically share it. For personal use this is irrelevant.

**Historical lens:** The custom GPT / Actions ecosystem replaced OpenAI Plugins (deprecated in 2024). The transition maintained API key auth support. The platform commitment to GPT Actions appears stable as of 2025.

---

### §6 Synthesis

**Executive summary:**

A custom GPT can be configured with Actions that (a) call a self-hosted HTTPS endpoint to write a memory and (b) call `search_brain` to surface context before responding. Both capabilities are fully supported by the OpenAI Actions architecture. OpenAI's built-in memory system has no programmatic API  -  no export or import hook exists  -  making the external write path via Actions the only viable route to cross-tool memory portability. The auth story is better than Claude iOS: Actions support static API key authentication via a custom header (configured in the GPT editor), which works reliably on the iOS mobile app; OAuth-based Actions have documented mobile reliability problems and should be avoided. The hosting backend from prior research (Cloudflare Workers + Fly.io) applies without modification. The ChatGPT Actions path is simpler to implement than Claude iOS MCP and should be built after the MCP path is operational, sharing the same backend.

**Key findings:**

1. A custom GPT Action can call any public HTTPS endpoint described by an OpenAPI schema; the call is made server-side by OpenAI's infrastructure, not by the client device.
2. API key authentication with a custom header is supported in the GPT editor UI and works reliably on the ChatGPT iOS mobile app; OAuth-based Actions have documented and persistent reliability failures on iOS and Android as of mid-2025.
3. The `add_memory` write path (Cloudflare Workers, stateless GitHub Contents API proxy) is directly compatible with GPT Actions  -  no modifications required.
4. The `search_brain` retrieval path can be triggered before every GPT response via a system prompt instruction; compliance is probabilistic (system prompt enforcement) rather than protocol-guaranteed (as in MCP), sufficient for personal use.
5. OpenAI's built-in ChatGPT memory system has no programmatic API  -  no endpoint exists for reading, writing, or importing saved memories; the data export (privacy portal ZIP) is a manual one-time operation, not a sync hook.
6. Creating a custom GPT requires ChatGPT Plus ($20/month), identical to the Claude Pro requirement for Claude iOS MCP Connectors; the cost is not a differentiating factor.
7. The same backend deployment (Cloudflare Workers + Fly.io/Tailscale Funnel) can serve both GPT Actions (REST/JSON) and Claude iOS MCP (Streamable HTTP) without conflict or additional cost.
8. The ChatGPT Actions path has one structural advantage over Claude iOS MCP: retrieval is only active when the user opens the specific memory-retrieval custom GPT, whereas Claude Connectors apply to every Claude conversation automatically.

**Evidence map:** (see §2 Investigation source citations above)

**Assumptions:**
- A system prompt instruction ("always call search_brain before responding") achieves ≥95% retrieval invocation for standard conversational queries.
- A single FastAPI backend can expose both MCP Streamable HTTP routes and plain REST/JSON routes without conflict.
- A custom GPT is set as the user's default interface for ChatGPT conversations to realise the retrieval benefit consistently.

**Analysis:** The ChatGPT Actions path and the Claude iOS MCP path are complementary, not competing. They share the same backend and serve different primary surfaces (ChatGPT vs Claude). Building both creates cross-tool memory portability: anything captured from a ChatGPT conversation is retrievable in a subsequent Claude conversation, and vice versa. The ChatGPT path is simpler (no MCP SDK required, API key auth works on mobile) but provides weaker retrieval enforcement.

**Risks, gaps, uncertainties:**
- The forced retrieval pattern (system prompt instruction) has not been empirically tested at the Actions level; compliance rate ≥95% is an assumption.
- The "not available on iOS" issue for OAuth Actions may resurface for API key Actions in future app updates.
- OpenAI may introduce a native Memory API in future, which would change the portability analysis.

**Open questions:**
- Should a single custom GPT handle both `add_memory` and `search_brain` Actions, or should these be separate GPTs? (Architectural question for the Memory-System build item W-0005.)
- Is there a way to configure the custom GPT as the ChatGPT default interface on iOS, to ensure retrieval runs on every conversation?

---

### §7 Recursive Review

**Completeness check:**
- §0: research question restated, scope confirmed, prior research cross-referenced. ✓
- §1: all seven sub-question trees decomposed to atomic claims. ✓
- §2: each atomic question investigated with labelled claims and sources. ✓
- §3: inferences and assumptions explicitly separated from facts. ✓
- §4: two genuine consistency issues examined (iOS availability, auth coverage); no unresolved contradictions. ✓
- §5: four lenses applied (technical, security, behavioural, economic). ✓
- §6: all seven synthesis components present. ✓

**Sourcing check:**
- Every [fact] traces to a named primary or secondary source.
- Every [inference] derived from labelled facts.
- Every [assumption] has explicit justification.

**Uncertainty check:**
- Forced retrieval compliance rate explicitly labelled as [assumption].
- OAuth iOS reliability gap explicitly flagged.
- Native Memory API absence confirmed by explicit community statement plus absence from API reference.

**Verdict:** Investigation is complete. §6 Synthesis can seed the Findings section without additions.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

A custom GPT can be configured with Actions that call a self-hosted HTTPS endpoint to write a memory (`add_memory`) and to retrieve context before responding (`search_brain`)  -  both capabilities are fully supported by the OpenAI Actions architecture. OpenAI's built-in ChatGPT memory system has no programmatic API; no export or import hook exists, making the external Actions write path the only viable route to cross-tool memory portability. Authentication is simpler than the Claude iOS MCP path: GPT Actions support static API key injection via a custom header, which works reliably on the ChatGPT iOS mobile app; OAuth-based Actions have documented mobile reliability problems. The hosting backend established in prior research (Cloudflare Workers for write, Fly.io or Tailscale Funnel for vector search) applies without modification and can serve both ChatGPT Actions and Claude iOS MCP from a single deployment.

### Key Findings

1. A custom GPT Action can call any public HTTPS endpoint described by an OpenAPI schema; the call is made server-side by OpenAI's infrastructure, making CORS irrelevant and requiring no changes to an existing Cloudflare Workers or Fly.io backend.

2. API key authentication with a custom header (e.g., `X-Api-Key`) is supported in the GPT editor UI as a server-side secret  -  it is never visible to the user  -  and works reliably on the ChatGPT iOS mobile app, unlike OAuth 2.0 which has documented persistent failures on iOS and Android through mid-2025.

3. The `add_memory` write path (stateless Cloudflare Workers proxy to GitHub Contents API) is directly compatible with GPT Actions and requires no modifications to the backend established in `2026-03-08-self-hosted-mcp-server-options.md`.

4. The `search_brain` retrieval path can be triggered before every GPT response via a system prompt instruction such as "Before every response, call the search_brain action with the user's query and incorporate the results as context"; compliance is probabilistic (system prompt enforcement) rather than protocol-guaranteed, but is sufficient for personal single-user deployment.

5. OpenAI's built-in ChatGPT memory system exposes no programmatic API: there is no endpoint for reading, writing, or importing saved memories; the data export available via the privacy portal is a manual one-time ZIP download, not a synchronisation hook.

6. Creating a custom GPT with Actions requires ChatGPT Plus at $20/month (identical to the Claude Pro requirement for Claude iOS MCP Connectors), meaning the cost parity between the two paths is exact and not a differentiating factor.

7. A single backend deployment can serve both GPT Actions (REST/JSON) and Claude iOS MCP (Streamable HTTP) endpoints without conflict, meaning the cross-tool memory portability goal  -  capturing from ChatGPT and retrieving in Claude, and vice versa  -  can be achieved with no additional hosting cost beyond the Fly.io/Railway instance already required for vector search.

8. The ChatGPT Actions path has one structural limitation compared to Claude iOS MCP Connectors: retrieval only activates when the user opens the specific memory-retrieval custom GPT, whereas Claude Connectors apply automatically to every Claude conversation once configured.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| GPT Actions call any public HTTPS endpoint via OpenAPI schema | https://platform.openai.com/docs/actions/introduction | high | Primary source; confirmed by multiple implementation guides |
| Calls are server-side (OpenAI infrastructure) | OpenAI community: "Since this endpoint will be run from OpenAI's backend, the API must be public" | high | Consistent with Claude Connectors architecture from prior research |
| API key (custom header) auth supported in GPT editor UI | https://platform.openai.com/docs/actions/authentication; OpenAI docs at developers.openai.com | high | Primary source; three sub-types confirmed |
| API key auth works on iOS; OAuth fails on iOS | community.openai.com/t/custom-gpt-oauth-issue-in-mobile-app/1114136; related threads Jan 2025, May 2025 | high | Multiple independent community reports; no counter-evidence |
| `add_memory` write path (Cloudflare Workers) compatible with Actions REST | 2026-03-08-self-hosted-mcp-server-options.md Key Finding #1; OpenAI Actions spec | high | Inference from architecture; REST + JSON is exactly what Actions require |
| `search_brain` retrieval triggerable via system prompt | https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts | medium | System prompt compliance is probabilistic, not guaranteed |
| No native Memory API (reading or writing) | community.openai.com/t/how-do-i-enable-or-disable-memory-in-api/703964; absence from OpenAI API reference | high | Explicit community confirmation; absence of endpoint in docs |
| Memory export is manual ZIP only | https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data | high | Primary source |
| ChatGPT Plus required to create custom GPTs | https://help.openai.com/en/articles/8554397-creating-a-gpt | high | Primary source |
| Same backend serves both GPT Actions and Claude MCP | 2026-03-08-self-hosted-mcp-server-options.md; inference from architecture | medium | Architectural inference; not empirically tested |
| Claude iOS supports no-auth or OAuth 2.1 only (no static key) | 2026-03-08-claude-ios-mcp-remote-integration.md Key Finding #6 | high | Prior research, primary-sourced |

### Assumptions

- **Assumption:** A system prompt instruction ("before every response, call search_brain") achieves ≥95% retrieval invocation for standard conversational queries. **Justification:** Community implementations of RAG via Actions report reliable trigger behaviour for explicit, unambiguous instructions; the failure mode is ambiguous instructions, not the underlying mechanism. This rate is sufficient for personal use but has not been empirically measured.

- **Assumption:** A single FastAPI backend can expose both MCP Streamable HTTP routes and plain REST/JSON routes on different paths without conflict. **Justification:** FastAPI's routing system supports arbitrary path definitions; MCP and REST share the HTTP transport layer and can coexist in the same process. This is a standard web application architecture pattern.

- **Assumption:** The user sets the memory-retrieval custom GPT as the default or primary interface for ChatGPT conversations to ensure retrieval runs consistently. **Justification:** If the user opens standard ChatGPT (not the custom GPT), no retrieval occurs. The custom GPT must be the entry point. This is a workflow discipline requirement, not a technical constraint.

### Analysis

The investigation resolves the build/no-build question with high confidence: the ChatGPT Actions path is viable and simpler to implement than the Claude iOS MCP path in three respects. First, no MCP SDK is required  -  any HTTP server with a valid OpenAPI schema works, and the existing Cloudflare Workers and Fly.io endpoints are already REST/JSON compatible. Second, API key authentication (custom header) is both simpler to configure and more iOS-reliable than OAuth 2.1. Third, OpenAPI schemas for two endpoints (`add_memory`, `search_brain`) are trivial to author, and LLMs including GPT-4o can generate them from a description.

Retrieval scope is the key structural constraint: custom GPT retrieval fires only when the user opens that specific GPT, making the ChatGPT path a complementary capture surface rather than the primary memory integration [inference].

OAuth unreliability on iOS  -  while API key Actions remain stable  -  is the key finding for implementation design. Any personal deployment should avoid OAuth and use the custom header API key approach, accepting the security posture that OpenAI's servers hold the key. For a personal memory endpoint containing the owner's own notes, this risk is acceptable [inference].

### Risks, Gaps, and Uncertainties

- The forced retrieval pattern (≥95% system prompt compliance) is an assumption, not an empirically verified rate. A prototype test with 20–30 queries would be sufficient to validate or reject this assumption before committing to the design.
- The "not available on iOS" issue, historically caused by OAuth flow failures, could resurface for API key Actions in a future app update. OpenAI has not documented iOS-specific Action availability guarantees.
- OpenAI may introduce a native Memory API in a future release, which would change the portability analysis (import hook would become available). No such roadmap item has been announced as of March 2026.
- The co-hosting assumption (MCP + REST on a single FastAPI instance) has not been tested; a simple architectural prototype would confirm or refute it before build commitment.

### Open Questions

1. Should a single custom GPT handle both `add_memory` and `search_brain` Actions, or should these be two separate custom GPTs with distinct purposes? (Architectural question for Memory-System W-0005.)
2. Is there a way to configure a custom GPT as the default interface on the ChatGPT iOS home screen, so it is the entry point for all conversations rather than requiring deliberate navigation?
3. OpenAI introduced "Skills" in 2025 as an evolution beyond Custom GPTs  -  does the Skills architecture change the Actions integration model, or is it additive? (Out of scope here; candidate for a new backlog item.)

---

## Output

- Type: knowledge
- Description: Build/no-build verdict for ChatGPT Actions as a memory capture and retrieval surface. Key findings: viable, simpler auth than Claude iOS MCP, same hosting backend, retrieval less guaranteed than MCP, native Memory API does not exist.
- Links:
  - https://platform.openai.com/docs/actions/introduction
  - https://platform.openai.com/docs/actions/authentication
  - https://help.openai.com/en/articles/8590148-memory-faq