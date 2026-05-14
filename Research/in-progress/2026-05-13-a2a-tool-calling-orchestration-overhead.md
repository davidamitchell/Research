---
review_count: 1
title: "Agent-to-Agent (A2A)-to-tool-calling unification: impact on orchestration overhead and reasoning accuracy in hierarchical multi-agent systems"
added: 2026-05-13T09:01:36+00:00
status: reviewing
priority: medium
blocks: []
tags: [agentic-ai, agent-tooling, llm, governance, workflow]
started: 2026-05-14T09:29:21+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-03-18-api-context-hubs-rag-mcp
  - 2026-05-06-aibom-identity-attribution-multiagent-practice
  - 2026-04-26-ai-agent-identity-access-management-enterprise
related:
  - 2026-05-13-agent-process-reliability-architecture
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-03-23-agent-orchestration-anvil-max
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Agent-to-Agent (A2A)-to-tool-calling unification: impact on orchestration overhead and reasoning accuracy in hierarchical multi-agent systems

## Research Question

To what extent does unifying specialised Agent-to-Agent (A2A) protocols into a standardised tool-calling interface affect orchestration overhead and reasoning accuracy in hierarchical multi-agent systems?

## Scope

**In scope:**
- Comparative analysis of two communication abstractions: specialised A2A protocol versus universal tool-calling interface
- Effects on orchestration latency, token consumption, context bloat, and multi-step delegation success rate
- Hierarchical multi-agent orchestration patterns where planner, coordinator, and executor agents interact
- Enterprise-style distributed environments where capabilities are exposed as black-box endpoints
- Security and policy-enforcement boundary placement at protocol layer versus tool-interface layer

**Out of scope:**
- Single-agent benchmarks without delegation chains
- Vendor-specific implementation details not transferable across platforms
- Model training or fine-tuning changes unrelated to interface abstraction
- User-interface design concerns

**Constraints:**
- Prefer empirical evidence, benchmarks, experiments, and production reports over conceptual architecture diagrams alone
- Distinguish protocol-level capabilities from wrapper-level capabilities to avoid category errors
- Use sources that describe both interoperability mechanics and operational governance implications

## Context

- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] Teams deciding between remote-agent interoperability and subagent-as-tool patterns are choosing not only an implementation style but also a cost, latency, and accountability model, because extra coordination layers change both runtime overhead and where identity and policy boundaries remain visible.

## Approach

1. Define a comparison framework mapping equivalent delegation tasks across specialised A2A protocols and generic tool-calling abstractions.
2. Collect benchmark-style evidence on orchestration latency and token overhead for multi-hop delegation patterns.
3. Compare reasoning-quality outcomes, task completion, and error rates under controlled multi-step workflows.
4. Analyse governance and security control points, authentication, authorization, auditability, and policy propagation, in each abstraction.
5. Identify threshold conditions where an additional communication layer shifts from net benefit to net overhead.

## Sources

- [x] [Google Developers Blog (2025) A2A: A new era of agent interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [x] [A2A Project (2025) Agent2Agent Protocol Specification](https://a2a-protocol.org/latest/specification/)
- [x] [Anthropic (2024) Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [x] [Model Context Protocol Docs Introduction](https://modelcontextprotocol.io/introduction)
- [x] [Model Context Protocol Docs Architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
- [x] [Model Context Protocol Specification (2025) Authorization](https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx)
- [x] [Internet Engineering Task Force (2022) Hypertext Transfer Protocol (HTTP) Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [x] [JSON-RPC Working Group (2013) JavaScript Object Notation Remote Procedure Call (JSON-RPC) 2.0 Specification](https://www.jsonrpc.org/specification)
- [ ] [OpenAI Platform Docs Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [x] [OpenAI Cookbook (2024) How to call functions with chat models](https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb)
- [x] [Anthropic Docs Tool Use Overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
- [x] [Wu et al. (2023) AutoGen: Enabling Next-Gen Large Language Model (LLM) Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
- [x] [Microsoft Learn (2025) Choosing Between Building a Single-Agent System or Multi-Agent System](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents)
- [x] [LangChain Docs Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent)
- [x] [Zhu et al. (2025) MultiAgentBench: Evaluating the Collaboration and Competition of Large Language Model (LLM) agents](https://aclanthology.org/2025.acl-long.421/)
- [x] [OpenReview (2026) OrchestrationBench: Large Language Model-Driven Agentic Planning and Tool Use in Multi-Domain Real-World Scenarios](https://openreview.net/forum?id=Oljnxmf4pc)
- [x] [Mitchell (2026) Application Programming Interface Context Hubs, Retrieval-Augmented Generation, and the Model Context Protocol: How Agents Discover and Use APIs](https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)
- [x] [Mitchell (2026) How do Open Authorization (OAuth) 2.0, OpenID Connect, and Secure Production Identity Framework for Everyone (SPIFFE) token propagation work in real multi-agent pipelines, and where does end-to-end attribution break in practice?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html)
- [x] [Mitchell (2026) What identity and access management model is required for Artificial Intelligence agents and low-code artefacts operating within enterprise systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine how much orchestration overhead and reasoning quality change when a hierarchical multi-agent system collapses specialised Agent-to-Agent (A2A) interactions into a standard tool-calling interface.
- Scope: compare specialised A2A protocol versus tool calling for planner-coordinator-executor hierarchies, token and latency overhead, delegation reliability, and governance boundaries; exclude single-agent-only benchmarks, user-interface issues, and vendor-specific product tuning.
- Constraints: prefer primary protocol documents, official framework documentation, and public benchmarks; separate protocol-native capabilities from wrapper behavior; keep governance claims tied to explicit identity and authorization surfaces.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Prior completed items already establish three relevant baselines: protocol layers and retrieval layers are distinct, attribution often weakens across agent-to-agent and agent-to-tool hops, and production-safe agent systems need separate machine identities rather than borrowed human context.

### §1 Question Decomposition

- **Root question:** when does collapsing remote or specialist agents into tools reduce net system cost, and when does it remove capabilities that hierarchical multi-agent systems need?
  - **A. Protocol semantics**
    - A1. What capabilities does A2A define beyond a generic tool call?
    - A2. What capabilities do Model Context Protocol (MCP) and tool-calling patterns define, and where does execution occur?
  - **B. Overhead**
    - B1. How do extra handoffs change model-call count, token load, and latency?
    - B2. Which overhead components come from tool schemas, repeated context, and coordination state rather than from the wire protocol alone?
  - **C. Reasoning accuracy**
    - C1. Does a richer agent-interoperability layer improve reasoning by itself?
    - C2. How much do topology and planning quality matter relative to function-calling correctness?
  - **D. Governance**
    - D1. Where do identity, authorization, and audit boundaries live in A2A?
    - D2. What becomes less visible when remote agents are wrapped as tools?
  - **E. Decision threshold**
    - E1. In which cases is tool calling the lower-friction default?
    - E2. In which cases does a specialised A2A layer justify its own overhead?

### §2 Investigation

#### 2.1 Prior work cross-reference

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html] The completed API-context-hubs item concluded that documentation, retrieval, and invocation protocols solve different layers of the agent-tool problem, which is directly relevant here because A2A-versus-tool-calling is also a layer-comparison problem rather than a simple feature checklist.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] The completed identity-attribution practice item found that attribution often breaks across agent-to-agent delegation and agent-to-tool handoffs, which matters here because tool-wrapping a remote agent can hide the original delegation chain unless external audit metadata is preserved.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] The completed enterprise identity item found that autonomous agents should run as bounded machine identities rather than as durable extensions of human accounts, which matters here because specialised A2A endpoints and wrapped tools present different places to enforce machine identity and least privilege.

#### 2.2 What A2A standardises

Primary sources:
- https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- https://a2a-protocol.org/latest/specification/

Claims:
- [fact; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] Google and the A2A specification define A2A as an interoperability protocol for independent and potentially opaque agent systems, with capability discovery, task management, collaboration messages, modality negotiation, and support for long-running tasks.
- [fact; source: https://a2a-protocol.org/latest/specification/] The A2A specification centers interaction around stateful Tasks, Messages, Artifacts, Parts, and an Agent Card that advertises identity, capabilities, endpoint, skills, and authentication requirements.
- [fact; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] A2A is explicitly designed for async-first, multi-vendor, enterprise-style interactions that may involve human review, push notifications, or modal content beyond plain text.
- [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] A2A is not merely a prettier function schema, because it carries remote-agent identity, lifecycle, and negotiation semantics that survive outside a single orchestrator's local tool registry.

#### 2.3 What MCP and tool-calling standardise

Primary sources:
- https://www.anthropic.com/news/model-context-protocol
- https://modelcontextprotocol.io/introduction
- https://modelcontextprotocol.io/docs/concepts/architecture
- https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx
- https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb

Identified but not consulted:
- https://platform.openai.com/docs/guides/function-calling

Claims:
- [fact; source: https://modelcontextprotocol.io/introduction; https://modelcontextprotocol.io/docs/concepts/architecture] MCP defines a client-server protocol in which a host creates one client per server connection and servers expose tools, resources, and prompts over a JSON-RPC-based data layer with standard input and standard output transports or Streamable HTTP transports.
- [fact; source: https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx; https://modelcontextprotocol.io/docs/concepts/architecture] MCP authorization is transport-level, optional, and Open Authorization (OAuth)-based for HTTP transports, while local standard input and standard output transports are expected to retrieve credentials from the environment rather than from the protocol itself.
- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb] Anthropic and OpenAI tool-calling patterns both treat tool use as schema-driven call generation, where the model emits a structured tool call and the client application is responsible for executing the function and returning the result.
- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Anthropic documents explicit token overhead for tool use, including tool definitions, tool-result blocks, and a model-specific tool-use system prompt of 346 tokens for current Claude 4.x automatic tool choice.
- [assumption; source: https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb] Access note: the seeded OpenAI platform guide was not accessible from this runtime, so the OpenAI-maintained cookbook notebook was used as the closest public substitute for current OpenAI function-calling mechanics.
- [inference; source: https://modelcontextprotocol.io/docs/concepts/architecture; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb] MCP and direct tool calling optimise Artificial Intelligence (AI)-to-system connectivity, but neither by itself gives a remote specialist the richer protocol identity, stateful task, and artifact semantics that A2A makes first-class.

#### 2.4 Overhead evidence for hierarchical patterns

Primary sources:
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents
- https://docs.langchain.com/oss/python/langchain/multi-agent
- https://arxiv.org/abs/2308.08155

Claims:
- [fact; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] Microsoft states that multi-agent systems introduce extra coordination, explicit state management, protocol design, error handling, security surfaces, higher cost from redundant context processing, and latency at each handoff point.
- [fact; source: https://docs.langchain.com/oss/python/langchain/multi-agent] LangChain's performance comparison shows that a one-shot request takes four model calls with subagents-as-tools versus three with handoffs, skills, or router patterns, and that repeat requests stay more expensive for stateless subagent invocation because each call replays the full flow.
- [fact; source: https://docs.langchain.com/oss/python/langchain/multi-agent] For a multi-domain comparison task, LangChain reports about five model calls and about 9K tokens for Subagents or Router, versus seven or more calls and about 14K or more tokens for Handoffs, and about three calls but about 15K tokens for Skills because loaded context persists across later calls.
- [fact; source: https://arxiv.org/abs/2308.08155] AutoGen presents multi-agent conversation as a flexible infrastructure for planning, tool use, and human inputs, but its abstract frames effectiveness as a property of configurable agent interaction patterns rather than as a claim that extra protocol layers are free.
- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] In a bounded hierarchical system that already has a central orchestrator, unifying specialists behind tool calls usually reduces orchestration overhead because it removes at least one explicit agent handoff layer while retaining only the schema and tool-result token costs.

#### 2.5 Reasoning accuracy evidence

Primary sources:
- https://openreview.net/forum?id=Oljnxmf4pc
- https://aclanthology.org/2025.acl-long.421/
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents

Claims:
- [fact; source: https://openreview.net/forum?id=Oljnxmf4pc] OrchestrationBench reports that function-calling performance is relatively consistent across evaluated models, while planning capabilities vary substantially, which separates low-level tool execution from higher-level orchestration quality.
- [fact; source: https://aclanthology.org/2025.acl-long.421/] MultiAgentBench finds that coordination protocol choice affects outcomes, with graph structure performing best among tested coordination protocols in the research scenario and cognitive planning improving milestone achievement rates by 3 percent.
- [fact; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] Microsoft advises teams to prototype with a single agent first when role separation, data volume, throughput, or modality differences might be solvable through prompting, retrieval, caching, reranking, or tool design rather than through extra agents.
- [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/; https://docs.langchain.com/oss/python/langchain/multi-agent] Reasoning accuracy is driven more by planning decomposition, topology, and context management than by whether a specialist capability is reached through a remote-agent protocol or a tool wrapper.
- [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] When a task is mostly planner-to-specialist delegation inside one trust boundary, collapsing the specialist into a tool is more likely to preserve or modestly improve reasoning quality than to harm it, because fewer handoffs mean less duplicated context and fewer opportunities for coordination error.

#### 2.6 Governance and security control points

Primary sources:
- https://a2a-protocol.org/latest/specification/
- https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx
- https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html
- https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html

Claims:
- [fact; source: https://a2a-protocol.org/latest/specification/] A2A Agent Cards publish endpoint and authentication requirements and the protocol models a remote agent as an independently addressable service with its own task lifecycle.
- [fact; source: https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx] MCP places authorization at the transport layer for HTTP-based transports and expects clients to present bearer tokens on every request, but it does not redefine agent-to-agent identity semantics above that transport.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Prior repository findings show that attribution and least-privilege design depend on preserving machine identity and delegation context across hops, and that these surfaces weaken when multiple actors share one technical credential or opaque wrapper.
- [inference; source: https://a2a-protocol.org/latest/specification/; https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] Wrapping a remote A2A agent as a generic tool can lower local orchestration friction, but it also risks collapsing a service boundary into a function boundary, which makes identity, audit, and policy propagation easier to lose unless they are reintroduced in external logging and credential design.

#### 2.7 Threshold conditions

Primary sources:
- https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents
- https://docs.langchain.com/oss/python/langchain/multi-agent

Claims:
- [fact; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] Microsoft says teams should start with multi-agent architecture only when they must cross security and compliance boundaries, align with multiple domain teams, or plan for broad modular growth that exceeds roughly three to five distinct functions.
- [fact; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] A2A is explicitly aimed at cross-vendor agent interoperability, long-running tasks, modality negotiation, and opaque remote systems that do not share memory, tools, or internal state.
- [fact; source: https://docs.langchain.com/oss/python/langchain/multi-agent] LangChain recommends multi-agent patterns only when single-agent prompting and tools cannot adequately manage context, team boundaries, or parallel work, and it presents subagents-as-tools as the main pattern when a central agent remains in control.
- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://docs.langchain.com/oss/python/langchain/multi-agent] The tipping point is therefore not "multiple agents exist" but "independent remote control surfaces exist": if specialists live inside one orchestrated application boundary, tool calling is usually the lower-overhead default, while A2A becomes justified when specialists are separate services, need async task state, or must preserve their own trust and policy perimeter.

### §3 Reasoning

- [inference; source: https://a2a-protocol.org/latest/specification/; https://modelcontextprotocol.io/docs/concepts/architecture] The comparison is asymmetric at the protocol layer, because A2A standardises remote-agent collaboration, while MCP and tool calling standardise access to callable capabilities and context primitives.
- [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] Because planning quality varies more than function-calling correctness, a transport or invocation abstraction change cannot be credited with reasoning gains unless it also changes planning, topology, or context isolation.
- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent] Overhead claims should be interpreted at the orchestration-pattern level rather than as a property of A2A packets versus tool-call packets, because most public evidence measures repeated context loading, state synchronization, and handoff count.
- [inference; source: https://a2a-protocol.org/latest/specification/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] Governance conclusions remain valid even without a head-to-head benchmark because independent service identity and delegation visibility are first-class in A2A and only incidental in generic tool wrappers.

### §4 Consistency Check

- [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/; https://docs.langchain.com/oss/python/langchain/multi-agent] The consulted evidence consistently supports a split conclusion: tool unification lowers overhead in bounded hierarchies, but reasoning accuracy depends mainly on planning and topology rather than on the invocation abstraction itself.
- [inference; source: https://a2a-protocol.org/latest/specification/; https://modelcontextprotocol.io/docs/concepts/architecture; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] No contradiction remains between protocol documents once the control surfaces are separated, because A2A governs remote-agent interaction, MCP governs host-server context exchange, and tool calling governs schema-driven invocation inside an application loop.
- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/] The main unresolved uncertainty is quantitative rather than directional, because the sources do not provide a direct head-to-head public benchmark of the same hierarchy implemented once with A2A and once with tool wrappers.

### §5 Depth and Breadth Expansion

- [inference; source: https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html] Technical and security lenses both point to the same implication: once a remote agent is wrapped as a tool, the implementation must deliberately preserve machine identity and delegation metadata or the lower-friction interface will mask the real trust boundary.
- [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The economic lens favors tool-calling unification for intra-application hierarchies because each extra handoff layer adds token cost, latency, monitoring burden, and failure handling overhead.
- [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] The organizational lens favors A2A where different teams, vendors, or regulated domains need independently managed agent services, because a shared tool registry does not by itself encode service ownership or negotiated capability discovery.
- [inference; source: https://aclanthology.org/2025.acl-long.421/; https://openreview.net/forum?id=Oljnxmf4pc] The behavioral lens suggests that planner quality and coordination design remain the dominant determinants of whether multi-agent specialization helps, so teams that add A2A without improving planner discipline are likely to buy complexity faster than accuracy.

### §6 Synthesis

**Executive summary:**

Unifying specialised Agent-to-Agent (A2A) interactions into tool-calling interfaces usually reduces orchestration overhead for hierarchical multi-agent systems that operate inside one orchestrator and one trust boundary, because it removes extra handoff, lifecycle, and coordination layers while retaining only schema and tool-result costs. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The same unification does not reliably improve reasoning accuracy by itself, because public benchmarks show that planning quality and coordination topology vary far more than low-level function-calling correctness. [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] A2A still earns its overhead when agents are remote, opaque, independently governed, long-running, or multi-modal, because those cases need first-class service discovery, task state, and identity boundaries that plain tool schemas do not preserve. [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/; https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx] The practical threshold is therefore to default to subagents-as-tools for bounded internal hierarchies and to keep a specialised A2A layer only where interoperability and governance surfaces matter more than minimum latency and token efficiency. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

**Key findings:**

1. **In a hierarchical system that already has a central orchestrator, collapsing specialist agents into tool calls usually lowers net orchestration overhead because it removes at least one explicit coordination layer while preserving only tool-schema and tool-result costs.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
2. **A2A carries protocol-native features that plain tool calling does not natively preserve, including Agent Card discovery, stateful task lifecycle, artifacts, modality negotiation, and async updates for opaque remote services.** ([fact]; high confidence; source: https://a2a-protocol.org/latest/specification/; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
3. **MCP and vendor tool-calling patterns standardise how an Artificial Intelligence (AI) host discovers context primitives or emits callable schemas, but they still treat execution as a client-side responsibility rather than as a remote agent contract.** ([fact]; high confidence; source: https://modelcontextprotocol.io/docs/concepts/architecture; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb)
4. **Public benchmark evidence indicates that reasoning accuracy differences in multi-agent systems are driven mainly by planning quality and coordination topology, not by whether the final specialist is invoked through a tool wrapper or a richer interoperability protocol.** ([inference]; medium confidence; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/)
5. **Tool-mediated unification is most likely to preserve or modestly improve reasoning quality in bounded hierarchies because fewer handoffs reduce duplicated context, but it does not solve planner mistakes, poor decomposition, or weak coordination policy.** ([inference]; medium confidence; source: https://openreview.net/forum?id=Oljnxmf4pc; https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents)
6. **A specialised A2A layer becomes justified when the system crosses security boundaries, spans independently managed teams or vendors, needs long-running asynchronous tasks, or must preserve remote-agent identity and negotiated capabilities as first-class objects.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/)
7. **Wrapping remote agents as generic tools can reduce local friction while simultaneously weakening identity and audit visibility, unless machine identity, credential scoping, and delegation metadata are preserved outside the wrapper.** ([inference]; high confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
8. **The most defensible default is therefore a layered design in which internal specialist capabilities are exposed as tools, while truly independent remote agents keep an A2A boundary only when that boundary carries interoperability or governance value that tool calling would erase.** ([inference]; medium confidence; source: https://a2a-protocol.org/latest/specification/; https://docs.langchain.com/oss/python/langchain/multi-agent; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Internal hierarchies usually reduce overhead by using tools instead of extra agent handoffs. | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | high | Fewer coordination layers |
| [fact] A2A includes remote-agent discovery, task state, artifacts, async status, and modality negotiation. | https://a2a-protocol.org/latest/specification/ ; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ | high | Protocol-native surface |
| [fact] MCP and vendor tool calling standardise schema-driven invocation, but client applications still execute tools. | https://modelcontextprotocol.io/docs/concepts/architecture ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb | high | Host-centered execution |
| [inference] Planning and topology dominate reasoning accuracy more than invocation abstraction. | https://openreview.net/forum?id=Oljnxmf4pc ; https://aclanthology.org/2025.acl-long.421/ | medium | Planning variance larger |
| [inference] Tool unification can preserve or modestly improve reasoning in bounded hierarchies, but not fix poor planning. | https://openreview.net/forum?id=Oljnxmf4pc ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents | medium | Less duplicated context |
| [inference] A2A earns its cost when remote agents need independent trust, async state, or negotiated capabilities. | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents ; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ; https://a2a-protocol.org/latest/specification/ | high | Boundary-driven threshold |
| [inference] Tool-wrapping remote agents can weaken identity and audit visibility unless metadata is preserved externally. | https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Governance risk |
| [inference] The best default is a layered design: tools for internal specialists, A2A only for independent remote agents. | https://a2a-protocol.org/latest/specification/ ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html | medium | Layer separation |

**Assumptions:**

- [assumption; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] No public source consulted here provides a direct head-to-head benchmark of the same hierarchy implemented once with A2A and once with tool wrappers, so the comparison synthesizes protocol documents with adjacent orchestration benchmarks rather than reading off a single experiment. Justification: the available public evidence separates protocol capabilities and orchestration outcomes, but not in one controlled A2A-versus-tool study.
- [assumption; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] Framework documentation is treated as reliable evidence for relative model-call, token, and coordination mechanics even though it is vendor-authored rather than independently benchmarked. Justification: the documents expose concrete execution patterns and quantified examples that align with each other on the direction of overhead effects.
- [assumption; source: https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Vendor tool-calling semantics are close enough across OpenAI and Anthropic to support abstraction-level comparison. Justification: both document schema-driven call generation with client-side execution responsibility and separate tool-result return steps.

**Analysis:**

The strongest evidence does not support a blanket claim that A2A harms reasoning or that tool calling improves it automatically. [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] Instead, the evidence supports a layered interpretation: A2A adds service-boundary semantics, while tool calling optimises invocation efficiency inside a host-controlled loop. [inference; source: https://a2a-protocol.org/latest/specification/; https://modelcontextprotocol.io/docs/concepts/architecture] That means the cost question is easier than the accuracy question, because public framework documentation consistently shows that extra handoffs and repeated context raise latency and token load, whereas accuracy improves only when the added structure produces better planning or better context isolation. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://openreview.net/forum?id=Oljnxmf4pc] A rival interpretation is that richer remote-agent autonomy could improve quality by preserving specialist context and ownership, and the A2A documents support that value proposition for cross-vendor and long-running work. [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] The deciding factor is therefore boundary placement: if the remote-agent boundary encodes real interoperability, ownership, or governance requirements, keep it; if it only reproduces internal delegation that one orchestrator could express as a tool, the A2A layer is mostly overhead. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] Public evidence still lacks a controlled benchmark that holds task set, planner, and specialist capabilities constant while swapping only A2A versus tool-calling transport.
- [inference; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents] Some overhead evidence comes from framework documentation rather than peer-reviewed experiments, so the direction of the trade-off is well supported but the exact magnitude should be treated as implementation-specific.
- [inference; source: https://a2a-protocol.org/latest/specification/; https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx] Governance claims are strongest for identity and authorization surfaces, but public sources do not yet quantify how much auditability is lost in production when remote agents are wrapped as tools.

**Open questions:**

- Would a controlled benchmark that keeps the same planner and specialist models but swaps only A2A versus tool wrappers show a measurable reasoning difference beyond latency and token cost?
- Which telemetry schema best preserves delegation-chain evidence when an A2A service is intentionally exposed as a tool inside another orchestrator?
- At what point does async task state, human approval, or modality negotiation become frequent enough that an A2A boundary is cheaper than rebuilding those features ad hoc in tool wrappers?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Agent-to-Agent (A2A), Model Context Protocol (MCP), Large Language Model (LLM), Application Programming Interface (API), Open Authorization (OAuth), OpenID Connect, and Secure Production Identity Framework for Everyone (SPIFFE) were checked for first-use expansion in the visible prose of this item.
- Claim audit: every substantive claim in Research Skill Output sections 0-6 is labeled as fact, inference, or assumption and is bound to at least one Uniform Resource Locator (URL)-backed source.
- Uncertainty audit: quantitative comparison claims remain medium confidence where the public evidence base lacks a direct A2A-versus-tool benchmark.

---

## Findings

### Executive Summary

Unifying specialised Agent-to-Agent (A2A) interactions into tool-calling interfaces usually reduces orchestration overhead for hierarchical multi-agent systems that operate inside one orchestrator and one trust boundary, because it removes extra handoff, lifecycle, and coordination layers while retaining only schema and tool-result costs. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The same unification does not reliably improve reasoning accuracy by itself, because public benchmarks show that planning quality and coordination topology vary far more than low-level function-calling correctness. [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] A2A still earns its overhead when agents are remote, opaque, independently governed, long-running, or multi-modal, because those cases need first-class service discovery, task state, and identity boundaries that plain tool schemas do not preserve. [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/; https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx] The practical threshold is therefore to default to subagents-as-tools for bounded internal hierarchies and to keep a specialised A2A layer only where interoperability and governance surfaces matter more than minimum latency and token efficiency. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

### Key Findings

1. **In a hierarchical system that already has a central orchestrator, collapsing specialist agents into tool calls usually lowers net orchestration overhead because it removes at least one explicit coordination layer while preserving only tool-schema and tool-result costs.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
2. **A2A carries protocol-native features that plain tool calling does not natively preserve, including Agent Card discovery, stateful task lifecycle, artifacts, modality negotiation, and async updates for opaque remote services.** ([fact]; high confidence; source: https://a2a-protocol.org/latest/specification/; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
3. **MCP and vendor tool-calling patterns standardise how an Artificial Intelligence (AI) host discovers context primitives or emits callable schemas, but they still treat execution as a client-side responsibility rather than as a remote agent contract.** ([fact]; high confidence; source: https://modelcontextprotocol.io/docs/concepts/architecture; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb)
4. **Public benchmark evidence indicates that reasoning accuracy differences in multi-agent systems are driven mainly by planning quality and coordination topology, not by whether the final specialist is invoked through a tool wrapper or a richer interoperability protocol.** ([inference]; medium confidence; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/)
5. **Tool-mediated unification is most likely to preserve or modestly improve reasoning quality in bounded hierarchies because fewer handoffs reduce duplicated context, but it does not solve planner mistakes, poor decomposition, or weak coordination policy.** ([inference]; medium confidence; source: https://openreview.net/forum?id=Oljnxmf4pc; https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents)
6. **A specialised A2A layer becomes justified when the system crosses security boundaries, spans independently managed teams or vendors, needs long-running asynchronous tasks, or must preserve remote-agent identity and negotiated capabilities as first-class objects.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/)
7. **Wrapping remote agents as generic tools can reduce local friction while simultaneously weakening identity and audit visibility, unless machine identity, credential scoping, and delegation metadata are preserved outside the wrapper.** ([inference]; high confidence; source: https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html)
8. **The most defensible default is therefore a layered design in which internal specialist capabilities are exposed as tools, while truly independent remote agents keep an A2A boundary only when that boundary carries interoperability or governance value that tool calling would erase.** ([inference]; medium confidence; source: https://a2a-protocol.org/latest/specification/; https://docs.langchain.com/oss/python/langchain/multi-agent; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Internal hierarchies usually reduce overhead by using tools instead of extra agent handoffs. | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | high | Fewer coordination layers |
| [fact] A2A includes remote-agent discovery, task state, artifacts, async status, and modality negotiation. | https://a2a-protocol.org/latest/specification/ ; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ | high | Protocol-native surface |
| [fact] MCP and vendor tool calling standardise schema-driven invocation, but client applications still execute tools. | https://modelcontextprotocol.io/docs/concepts/architecture ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb | high | Host-centered execution |
| [inference] Planning and topology dominate reasoning accuracy more than invocation abstraction. | https://openreview.net/forum?id=Oljnxmf4pc ; https://aclanthology.org/2025.acl-long.421/ | medium | Planning variance larger |
| [inference] Tool unification can preserve or modestly improve reasoning in bounded hierarchies, but not fix poor planning. | https://openreview.net/forum?id=Oljnxmf4pc ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents | medium | Less duplicated context |
| [inference] A2A earns its cost when remote agents need independent trust, async state, or negotiated capabilities. | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents ; https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ; https://a2a-protocol.org/latest/specification/ | high | Boundary-driven threshold |
| [inference] Tool-wrapping remote agents can weaken identity and audit visibility unless metadata is preserved externally. | https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-identity-access-management-enterprise.html | high | Governance risk |
| [inference] The best default is a layered design: tools for internal specialists, A2A only for independent remote agents. | https://a2a-protocol.org/latest/specification/ ; https://docs.langchain.com/oss/python/langchain/multi-agent ; https://davidamitchell.github.io/Research/research/2026-03-18-api-context-hubs-rag-mcp.html | medium | Layer separation |

### Assumptions

- **Assumption:** No public source consulted here provides a direct head-to-head benchmark of the same hierarchy implemented once with A2A and once with tool wrappers. **Justification:** the available public evidence separates protocol capabilities and orchestration outcomes, but not in one controlled A2A-versus-tool study. [assumption; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/]
- **Assumption:** Framework documentation is reliable enough to support directional overhead claims even though it is vendor-authored rather than independently benchmarked. **Justification:** the documents expose concrete execution patterns and quantified examples that align with each other on the direction of overhead effects. [assumption; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents]
- **Assumption:** Vendor tool-calling semantics are close enough across OpenAI and Anthropic to support abstraction-level comparison. **Justification:** both document schema-driven call generation with client-side execution responsibility and separate tool-result return steps. [assumption; source: https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/How_to_call_functions_with_chat_models.ipynb; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview]

### Analysis

The strongest evidence does not support a blanket claim that A2A harms reasoning or that tool calling improves it automatically. [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/] Instead, the evidence supports a layered interpretation: A2A adds service-boundary semantics, while tool calling optimises invocation efficiency inside a host-controlled loop. [inference; source: https://a2a-protocol.org/latest/specification/; https://modelcontextprotocol.io/docs/concepts/architecture] That means the cost question is easier than the accuracy question, because public framework documentation consistently shows that extra handoffs and repeated context raise latency and token load, whereas accuracy improves only when the added structure produces better planning or better context isolation. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://docs.langchain.com/oss/python/langchain/multi-agent; https://openreview.net/forum?id=Oljnxmf4pc] A rival interpretation is that richer remote-agent autonomy could improve quality by preserving specialist context and ownership, and the A2A documents support that value proposition for cross-vendor and long-running work. [inference; source: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/; https://a2a-protocol.org/latest/specification/] The deciding factor is therefore boundary placement: if the remote-agent boundary encodes real interoperability, ownership, or governance requirements, keep it; if it only reproduces internal delegation that one orchestrator could express as a tool, the A2A layer is mostly overhead. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

### Risks, Gaps, and Uncertainties

- Public evidence still lacks a controlled benchmark that holds task set, planner, and specialist capabilities constant while swapping only A2A versus tool-calling transport. [inference; source: https://openreview.net/forum?id=Oljnxmf4pc; https://aclanthology.org/2025.acl-long.421/]
- Some overhead evidence comes from framework documentation rather than peer-reviewed experiments, so the direction of the trade-off is well supported but the exact magnitude should be treated as implementation-specific. [inference; source: https://docs.langchain.com/oss/python/langchain/multi-agent; https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents]
- Governance claims are strongest for identity and authorization surfaces, but public sources do not yet quantify how much auditability is lost in production when remote agents are wrapped as tools. [inference; source: https://a2a-protocol.org/latest/specification/; https://raw.githubusercontent.com/modelcontextprotocol/specification/main/docs/specification/2025-03-26/basic/authorization.mdx]

### Open Questions

- Would a controlled benchmark that keeps the same planner and specialist models but swaps only A2A versus tool wrappers show a measurable reasoning difference beyond latency and token cost?
- Which telemetry schema best preserves delegation-chain evidence when an A2A service is intentionally exposed as a tool inside another orchestrator?
- At what point does async task state, human approval, or modality negotiation become frequent enough that an A2A boundary is cheaper than rebuilding those features ad hoc in tool wrappers?

---

## Output

- Type: knowledge
- Description: This item concludes that tool-calling unification is the lower-overhead default for internal hierarchical delegation, while A2A is justified mainly when remote agents need independent interoperability and governance boundaries. [inference; source: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents; https://a2a-protocol.org/latest/specification/; https://docs.langchain.com/oss/python/langchain/multi-agent]
- Links:
  - https://a2a-protocol.org/latest/specification/
  - https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents
  - https://openreview.net/forum?id=Oljnxmf4pc
