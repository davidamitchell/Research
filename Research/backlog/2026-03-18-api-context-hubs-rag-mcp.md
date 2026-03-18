---
title: "API Context Hubs, Retrieval-Augmented Generation, and the Model Context Protocol: How Agents Discover and Use APIs"
added: 2026-03-18
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [api-discovery, context-hub, rag, mcp, model-context-protocol, retrieval-augmented-generation, agents, tooling, ai-agents, api-integration]
started: ~
completed: ~
output: [knowledge]
---

# API Context Hubs, Retrieval-Augmented Generation, and the Model Context Protocol: How Agents Discover and Use APIs

## Research Question

What approaches are being used to enable AI agents to discover, understand, and invoke external Application Programming Interfaces (APIs), and how do the three major emerging strategies — context hubs (exemplified by Andrew Ng's `context-hub`), Retrieval-Augmented Generation (RAG)-based API discovery, and the Model Context Protocol (MCP) — compare in their design choices, trade-offs, and scope? Is the core problem that `context-hub` addresses being solved in meaningfully different ways elsewhere, or do these approaches converge?

Supporting questions:
- What specific problem does `andrewyng/context-hub` solve, and what is its design model?
- How does RAG-based API discovery work, and what prior work exists (e.g., REST-GPT, Gorilla, ToolBench)?
- What is MCP, what problem does it solve, and how does its scope overlap with or differ from context hubs and RAG-based tooling?
- What are the key design axes across these approaches (static vs. dynamic discovery, structured vs. unstructured context, push vs. pull, standardised vs. proprietary protocol)?
- What gaps remain unaddressed across all three approaches?

## Scope

**In scope:**
- `andrewyng/context-hub` — architecture, intended use case, and design decisions
- MCP (Anthropic, 2024) — protocol specification, current adoption, and ecosystem
- RAG-based API/tool discovery research: REST-GPT, Gorilla Large Language Model (LLM) benchmark, ToolBench / ToolLLM, HuggingGPT, and related academic work
- OpenAPI / Swagger as a structured API description layer relevant to all three approaches
- Agent frameworks that bridge these approaches: LangChain tools, LlamaIndex tool use, AutoGPT plugins, OpenAI function calling / tool use
- Commercial API discovery products and analogues: Postman AI, RapidAPI AI search, AWS Bedrock Agents action groups
- Prior completed research in this repository that is directly adjacent: any items tagged with `rag`, `mcp`, or `agents`

**Out of scope:**
- Detailed implementation of a new API discovery system (this is a research item)
- API gateway infrastructure, rate limiting, or API management platforms (Kong, Apigee) unless directly tied to agent discovery
- Non-AI API catalogues and developer portals (Swagger Hub, ReadMe.io) unless compared as a baseline
- Security vulnerabilities in specific API implementations (a separate concern from discovery architecture)

**Constraints:** Publicly accessible sources. GitHub repository documentation, arXiv preprints, official protocol specifications, and vendor documentation (2022–2026). Web search at retrieval time for the most current state of `context-hub` and MCP ecosystem, as both are evolving rapidly.

## Context

AI agents are increasingly expected to use external tools — web search, code execution, data retrieval, and arbitrary APIs — to complete tasks. The core challenge is: *how does an agent know what tools exist, what they do, and how to call them correctly?*

Three distinct strategies have emerged in parallel:

1. **Context hubs** — curated, structured documents that describe APIs in a format optimised for LLM consumption. Andrew Ng's `context-hub` (https://github.com/andrewyng/context-hub) is a prominent public example. The model is essentially: give the LLM a well-structured API reference at prompt time, let it reason about how to call the API.

2. **RAG-based tool discovery** — rather than providing all API documentation upfront, retrieve the relevant portion at query time. Research projects like Gorilla (Berkeley, 2023) and ToolBench (2023) train or prompt models to retrieve correct API calls from a large indexed catalogue. This scales better than context hubs but requires a retrieval index and introduces retrieval failure modes.

3. **Model Context Protocol (MCP)** — Anthropic's 2024 open protocol for LLM–tool integration. MCP defines a standardised wire format for tool servers to expose capabilities to any compliant LLM client. Rather than baking tool knowledge into context, MCP externalises it into discoverable, invocable servers. It is closer in spirit to a Remote Procedure Call (RPC) protocol than a documentation format.

These three approaches are not mutually exclusive — an MCP server could use RAG internally to decide which sub-tools to expose; a context hub could be served via MCP. But they represent different philosophical starting points: documentation quality, retrieval accuracy, and protocol standardisation respectively.

The issue that seeds this item explicitly asks whether `context-hub` is solving a problem that is being addressed in different manners elsewhere. This is the central question to answer.

## Approach

1. **Characterise `context-hub`** — read the `andrewyng/context-hub` repository README, any associated documentation, and public discussion. What is the exact problem statement? What is the data model for a "context hub"? Who are the intended consumers (agents, humans, both)? What APIs are already represented?
2. **Map the RAG-based API discovery landscape** — survey key research papers: Gorilla (Patil et al., 2023), ToolBench/ToolLLM (Qin et al., 2023), REST-GPT (Song et al., 2023), HuggingGPT (Shen et al., 2023). For each: what problem does it solve, what is the corpus, and how does retrieval work?
3. **Characterise MCP** — read the Anthropic MCP specification (https://modelcontextprotocol.io), the GitHub repository (https://github.com/modelcontextprotocol), and the current server ecosystem. What is in-scope for MCP vs. out-of-scope? How does discovery work within MCP — does a client know what servers exist?
4. **Design axis comparison** — map all three approaches across key axes: static vs. dynamic context, structured vs. unstructured API description, push (context in prompt) vs. pull (retrieval or RPC), proprietary vs. open standard, training-time vs. inference-time knowledge, human-authored vs. auto-generated tool descriptions.
5. **Gap analysis** — what problems does none of the three approaches address well? Likely candidates: cross-API orchestration, API versioning and drift, authentication and credential management within agent context, cost-aware tool selection, privacy-preserving tool use.
6. **Convergence / divergence assessment** — is the field converging on a single dominant approach, or are context hubs / RAG / MCP targeting different segments of the problem space that are complementary rather than competing?
7. **Synthesis** — produce Executive Summary, Key Findings, and Evidence Map.

## Sources

- [ ] `andrewyng/context-hub` — https://github.com/andrewyng/context-hub — repository README, issues, and any linked documentation
- [ ] Anthropic MCP specification — https://modelcontextprotocol.io — protocol overview and specification
- [ ] MCP GitHub organisation — https://github.com/modelcontextprotocol — server ecosystem and community
- [ ] Gorilla paper — Patil, S. et al. (2023) — "Gorilla: Large Language Model Connected with Massive APIs" — arXiv:2305.15334
- [ ] ToolBench / ToolLLM — Qin, Y. et al. (2023) — "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs" — arXiv:2307.16789
- [ ] REST-GPT — Song, Y. et al. (2023) — "RestGPT: Connecting Large Language Models with Real-World RESTful APIs" — arXiv:2306.06624
- [ ] HuggingGPT — Shen, Y. et al. (2023) — "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace" — arXiv:2303.17580
- [ ] API-Bank — Li, M. et al. (2023) — "API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs" — arXiv:2304.08244
- [ ] OpenAPI Specification — https://swagger.io/specification/ — the structured API description standard underlying most tool integration work
- [ ] LangChain tools documentation — https://python.langchain.com/docs/modules/agents/tools/ — how the most widely used agent framework handles tool description and invocation
- [ ] OpenAI function calling / tool use documentation — https://platform.openai.com/docs/guides/function-calling
- [ ] Survey of LLM tool use — Qu, Y. et al. (2024) — "Tool Learning with Foundation Models" — arXiv:2304.08354

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
