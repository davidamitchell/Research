# 2026-03-09 — Fix Research Quality Violations (Issues #71, #74, #75, #76, #77)

## Session summary

Resolved all quality violations filed by the automated research review workflow across five completed research items. Fixes cover citation-discipline, speculation-control, and remove-ai-slop violations.

## Files fixed

### `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md` (Issue #71)
- `CoT` expanded to `chain-of-thought (CoT)` at first use (§1 B1)
- `MBCPP` expanded to `MBCPP (Mostly Basic C++ Programming Problems)` at first use
- `[inference]` added to §3 bimodal-finding prediction sentence
- `[inference]` added to §5 economic lens AI-assisted batch-size claim
- Analysis: four consecutive "The [noun]" paragraph openings varied (two changed)
- Analysis: symmetrical contrast scaffold ("Acceleration-mode...work when / Exploration-mode...work when") rewritten as direct design rule
- `[inference]` added to Findings Analysis "most practically actionable result" and "most plausible long-term resolution"

### `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md` (Issue #74)
- "web search synthesis" replaced with `[SOURCE NEEDED]` in §4, §6 Evidence Map, and Findings Evidence Map
- Lines ~189-195: URL-unverified sources (Jade Global, Beyond20, Sofigate, Plat4mation, Infocenter DORA, ServiceNow FSO Core docs) changed to `[SOURCE NEEDED]`
- `[inference]` added to §3 "three-layer model avoids the conflation that causes boundary disputes"
- `[inference]` added to Findings Analysis "accountability gaps at the record level cause accuracy to decay"

### `Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md` (Issue #75)
- `LLM` expanded to `Large Language Model (LLM)` at first use
- `LSP` expanded to `Language Server Protocol (LSP)` at first use
- `RAG` expanded to `Retrieval-Augmented Generation (RAG)` at first use
- `TUI` expanded to `Terminal User Interface (TUI)` at first use
- `[inference]` added to Findings Executive Summary "most detailed public treatment"
- `[inference]` added to Findings Key Finding 5 "most detailed public architecture"
- `[inference]` added to Findings Analysis "emerging middle ground"
- "Both prioritise transparency and recoverability over raw throughput" rewritten with evidence-backed replacement
- Four consecutive "X but/at the cost of Y" constructions varied in two clauses

### `Research/completed/2026-03-08-context-engineering-first-principles.md` (Issue #76)
- `LLM` expanded to `Large Language Model (LLM)` at first prose use
- `RAG` expanded to `Retrieval-Augmented Generation (RAG)` at first use
- `RLHF` expanded to `Reinforcement Learning from Human Feedback (RLHF)` at first use (line ~31); duplicate expansion removed from Open Questions
- `DORA` expanded to `DevOps Research and Assessment (DORA)` at first use
- §2 D1–D3 control theory source changed to include full URLs: `https://x-engineer.org` and `https://electronics-tutorials.ws`
- `[inference]` added to §3 "LLMs exhibit exactly the same framing, priming, and presupposition dynamics as humans"
- `[inference]` added to Findings Analysis "practitioner prompt engineering...optimises token-level quality"
- `[inference]` added to "Sycophancy, specification gaming...token-level quality masked goal-level failure"
- §6 Key Finding 3 trailing narration "because these dynamics are embedded in training data" removed
- Three consecutive "Question? — Answer." pairs rewritten as varied prose

### `Research/completed/2026-03-08-self-hosted-mcp-server-options.md` (Issue #77)
- `MCP` expanded to `Model Context Protocol (MCP)` at first prose use
- `OAuth` expanded to `OAuth (Open Authorisation)` at first use
- `TLS` expanded to `Transport Layer Security (TLS)` at first use
- `PAT` expanded to `Personal Access Token (PAT)` at first use
- `NVMe` expanded to `Non-Volatile Memory Express (NVMe)` at first use
- `PaaS` expanded to `Platform as a Service (PaaS)` at first use
- `CDN` expanded to `Content Delivery Network (CDN)` at first use
- `SDK` expanded to `Software Development Kit (SDK)` at first use (kept in context with SDK label)
- Pyodide annotated with `(https://pyodide.org)` at first definition
- Source citations fixed: workers-mcp URL added; dev.to article → `[SOURCE NEEDED]`; GitHub REST API → full URL; blog.cloudflare.com references → `[SOURCE NEEDED]`; byteiota.com → `[SOURCE NEEDED]`
- §2 and §3: "Anthropic's published IP ranges" annotated with `[SOURCE NEEDED: Anthropic published connector IP ranges]`
- `[inference]` added to §3 "Fly.io has a slight operational edge"
- `[inference]` added to §3 "a static shared secret is the correct first implementation"
- `[inference]` added to §5 "This is a well-validated architecture"
- `[inference]` added to Findings Analysis "more mature persistent volume feature"
- `[inference]` added to Findings Analysis "degrading search latency unacceptably"
- Findings Executive Summary rewritten (different phrasing, structure, and level of detail from RSO §6)
- Findings Analysis pre-computed embeddings paragraph rewritten (non-repetitive vs RSO §6 version)
- Symmetrical contrast scaffold rewritten to state design choice directly

## Issues closed

- Closed #71 (sdlc-ai-prompt-patterns violations)
- Closed #74 (servicenow-csdm-data-modelling violations)
- Closed #75 (ai-coding-harnesses-agent-philosophy violations)
- Closed #76 (context-engineering-first-principles violations)
- Closed #77 (self-hosted-mcp-server-options violations)
