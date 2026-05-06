---
review_count: 1
title: "How do you construct a declared design-time Artificial Intelligence Bill of Materials (AIBOM) for a real tool-using, stateful Artificial Intelligence (AI) workload? A worked example using Amazon Web Services (AWS) Bedrock Agents and LangGraph"
added: 2026-05-06T08:52:41+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, supply-chain, llm, ai-platform, governance]
started: 2026-05-06T20:19:55+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-generation-divergence-theory]
related: [2026-05-06-aibom-identity-delegation-trust-theory, 2026-05-06-aibom-platform-observability-control-comparison]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do you construct a declared design-time Artificial Intelligence Bill of Materials (AIBOM) for a real tool-using, stateful Artificial Intelligence (AI) workload? A worked example using Amazon Web Services (AWS) Bedrock Agents and LangGraph

## Research Question

How do you extract and construct a declared design-time Artificial Intelligence Bill of Materials (AIBOM), covering model, prompt or system instruction, tools, Retrieval-Augmented Generation (RAG) knowledge bases, and memory configuration, from two representative tool-using and stateful AI platforms, specifically Amazon Web Services (AWS) Bedrock Agents and LangGraph, and what does the resulting AIBOM reveal about schema gaps between the declared configuration and a standards-aligned CycloneDX or Software Package Data Exchange (SPDX) representation?

## Scope

**In scope:**
- Step-by-step process for extracting an AIBOM from AWS Bedrock Agents through the AWS console, Infrastructure as Code (IaC), and Bedrock control-plane Application Programming Interfaces (APIs)
- Step-by-step process for extracting an AIBOM from LangGraph through graph definition, tool registry, model binding, state schema, and persistence configuration in source code
- Mapping extracted configuration fields to the CycloneDX Machine Learning Bill of Materials (ML-BOM) schema extensions proposed in `2026-05-06-aibom-schema-design-standards-alignment`
- Documentation of schema gaps, specifically fields present in platform configuration that have no CycloneDX or SPDX equivalent, and fields required by the proposed AIBOM schema that cannot be populated from the platform
- Feasibility assessment of what can be automated in a Continuous Integration and Continuous Deployment (CI/CD) pipeline versus what requires manual extraction or repository conventions
- Comparative analysis of which platform exposes more complete declared AIBOM-relevant configuration

**Out of scope:**
- Runtime or observed AIBOM, covered in `2026-05-06-aibom-runtime-generation-divergence-theory`
- Other platforms such as Microsoft 365 Copilot or Salesforce Agentforce, covered in `2026-05-06-aibom-platform-observability-control-comparison`
- Fresh schema invention from first principles, covered in `2026-05-06-aibom-schema-design-standards-alignment`

**Constraints:**
- Use real platform documentation and API surfaces as primary sources rather than fictional examples
- Produce at least one concrete representative AIBOM artifact per platform inside this item
- Treat AWS Bedrock Agents and LangGraph as contrasting declared surfaces, managed control plane versus code-native orchestration framework

## Context

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api] AWS Bedrock Agents and LangGraph both expose declared configuration, but Bedrock exposes it through service APIs while LangGraph exposes it through graph code, state schemas, and compile-time runtime arguments.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html; https://cyclonedx.org/capabilities/mlbom/] A standards-aligned AIBOM is only operationally useful if the design-time fields proposed by the schema item can be populated from real platform artifacts rather than described only conceptually.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] This practice item tests whether declared configuration alone is sufficient to inventory behavior-shaping dependencies, or whether important retrieval, memory, and execution surfaces remain outside a design-time snapshot.

## Approach

1. **Platform inventory, AWS Bedrock Agents:** document the configuration fields available for foundation model selection, system instruction, prompt overrides, action groups, knowledge bases, memory, guardrails, and versions, and identify the Application Programming Interface (API) or IaC surface for each field.

2. **Platform inventory, LangGraph:** document the equivalent configuration surface for graph structure, model binding, tool registry, state schema, persistence, memory, and routing logic, and identify where those fields live in code or documentation examples.

3. **AIBOM construction, AWS Bedrock Agents:** construct a representative AIBOM JSON document for a documented Bedrock agent configuration and annotate each field with its extraction source.

4. **AIBOM construction, LangGraph:** construct a representative AIBOM JSON document for a documented LangGraph agent and annotate each field with its extraction source.

5. **Gap analysis:** identify AIBOM fields with no platform source, platform configuration not captured by the schema, and fields requiring manual intervention; distinguish architectural gaps from tooling gaps.

6. **CI/CD feasibility:** assess whether AIBOM generation can be automated as a pipeline step for each platform and identify the minimum extraction tooling required.

## Sources

- [x] [Amazon Web Services Bedrock Agents overview](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) - official high-level description of Bedrock agent components and lifecycle
- [x] [Amazon Web Services Bedrock GetAgent API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html) - official control-plane API for model, instruction, prompt overrides, memory, orchestration type, and guardrail configuration
- [x] [Amazon Web Services Bedrock GetAgentActionGroup API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html) - official action-group detail API
- [x] [Amazon Web Services Bedrock ListAgentActionGroups API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html) - official action-group discovery API
- [x] [Amazon Web Services Bedrock ListAgentKnowledgeBases API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html) - official knowledge-base association discovery API
- [x] [Amazon Web Services Bedrock GetKnowledgeBase API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html) - official knowledge-base detail API
- [x] [Amazon Web Services Bedrock trace events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) - official trace schema showing which prompt and invocation details are runtime rather than design-time
- [x] [Amazon Web Services Bedrock deploy-agent guide](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html) - official version and alias behavior
- [x] [Amazon Web Services CloudFormation AWS::Bedrock::Agent](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html) - official IaC declaration surface for Bedrock agents
- [x] [Amazon Web Services Bedrock action groups](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html) - official action-group design surface
- [x] [Amazon Web Services Bedrock knowledge bases for agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-add.html) - official knowledge-base association guidance
- [x] [LangChain LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) - official overview of LangGraph as a low-level orchestration runtime
- [x] [LangChain LangGraph graph Application Programming Interface (API) overview](https://docs.langchain.com/oss/python/langgraph/graph-api) - official documentation for state, nodes, edges, schemas, and compilation
- [x] [LangChain LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) - official documentation for checkpoints, threads, and checkpointers
- [x] [LangChain memory concepts](https://docs.langchain.com/oss/python/concepts/memory) - official documentation for short-term and long-term memory concepts used with LangGraph
- [x] [LangChain tools](https://docs.langchain.com/oss/python/langchain/tools) - official documentation for tool definitions, schemas, runtime access, and ToolNode
- [x] [LangChain LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) - official end-to-end example showing model binding, tools, state, nodes, edges, and compiled graph
- [x] [CycloneDX AI and Machine Learning Bill of Materials](https://cyclonedx.org/capabilities/mlbom/) - official CycloneDX statement of current AI and machine-learning bill-of-materials coverage
- [x] [OWASP AIBOM project](https://owaspaibom.org/) - official Open Worldwide Application Security Project (OWASP) AIBOM project framing
- [x] [GenAI Security Project AIBOM Generator](https://github.com/GenAI-Security-Project/aibom-generator) - public implementation reference for current AIBOM generator behavior
- [x] [Rajbahadur et al. (2026) Building an Open AIBOM Standard in the Wild](https://arxiv.org/abs/2510.07070) - peer-reviewed experience report on extending SPDX for AI supply chains
- [x] [AI Bill of Materials Generator (AIBoMGen) (2026) Generating an AI Bill of Materials for Secure, Transparent, and Compliant Model Training](https://doi.org/10.48550/arXiv.2601.05703) - recent academic paper on generated AIBOMs for model-training settings
- [x] [David Mitchell (2026) Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence (AI) workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html) - prior completed corpus item defining conceptual gaps this practice item tests
- [x] [David Mitchell (2026) What is the minimal viable schema for an Artificial Intelligence bill of materials for prompt, retrieval, memory, and tool-using AI systems, and how should it align with CycloneDX and SPDX?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html) - prior completed corpus item defining the target schema used for mapping and gap analysis
- [x] [David Mitchell (2026) How can a runtime-observed AIBOM be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html) - prior completed corpus item used to qualify declared-versus-observed limits

## Related

- [Why does Software Bill of Materials (SBOM) fail as a complete inventory model for agentic Artificial Intelligence (AI) workloads, and what new conceptual abstractions are required?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html)
- [What is the minimal viable schema for an Artificial Intelligence bill of materials for prompt, retrieval, memory, and tool-using AI systems, and how should it align with CycloneDX and SPDX?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html)
- [How can a runtime-observed AIBOM be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How can a declared design-time AIBOM be constructed for AWS Bedrock Agents and LangGraph, and what schema gaps appear when each declared surface is mapped to a standards-aligned CycloneDX or SPDX representation?
- Scope: AWS Bedrock Agents APIs and IaC, LangGraph code-native graph configuration, representative AIBOM artifacts, schema mapping, gap classification, and CI/CD feasibility.
- Constraints: Use documented platform surfaces, distinguish declared state from runtime evidence, keep citations URL-backed, and use canonical repository tags only.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-sbom-conceptual-gaps-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html

### §1 Question Decomposition

- **Root question:** Which declared artifacts can be extracted from each platform to construct an AIBOM, and where do platform surfaces or current standards leave important design-time dependencies underspecified?
  - **A. AWS Bedrock declared surface**
    - A1. Which Bedrock fields are returned directly by `GetAgent`?
    - A2. Which additional calls are required to inventory action groups, knowledge bases, and deployment versions?
    - A3. Which Bedrock-relevant fields exist only in IaC or runtime traces rather than in a single control-plane object?
  - **B. LangGraph declared surface**
    - B1. Which agent-shaping artifacts are explicit in LangGraph state, nodes, edges, model binding, tools, and persistence configuration?
    - B2. Which of those artifacts are extractable mechanically from repository code versus requiring execution or conventions?
  - **C. AIBOM construction**
    - C1. What representative declared AIBOM artifact can be built for a Bedrock agent from documented fields?
    - C2. What representative declared AIBOM artifact can be built for a LangGraph agent from documented fields?
  - **D. Schema mapping**
    - D1. Which extracted fields map cleanly to CycloneDX or SPDX-style model, data, service, or configuration objects?
    - D2. Which extracted fields require custom properties, custom component types, or manual annotations?
  - **E. Feasibility and gaps**
    - E1. What parts of AIBOM generation can be automated in CI/CD for each platform?
    - E2. Which missing fields are architectural platform gaps, and which are tooling gaps that a custom extractor could close?

### §2 Investigation

#### Source substitutions and failed-search notes

- Search note: query `"AIBOM: Towards a Standard Bill of Materials for AI Systems"` -> no exact title match found; working academic replacements used here: https://arxiv.org/abs/2510.07070 ; https://doi.org/10.48550/arXiv.2601.05703

#### A. AWS Bedrock Agents, what the declared design surface exposes

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html] AWS documents Bedrock Agents as configurations that combine a foundation model, action groups, optional knowledge bases, prompt templates, memory, and deployment aliases or versions.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html] `GetAgent` returns agent identity and high-value design-time fields including `foundationModel`, `instruction`, `orchestrationType`, `promptOverrideConfiguration`, `memoryConfiguration`, `guardrailConfiguration`, `agentVersion`, and timestamps.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html] Bedrock action groups are not fully embedded inside `GetAgent`; they require enumeration through `ListAgentActionGroups` and detail retrieval through `GetAgentActionGroup`, which exposes executor settings plus `apiSchema` or `functionSchema`.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html] Knowledge-base inventory is also split across calls, because the agent-level association list comes from `ListAgentKnowledgeBases` while storage, embedding-model, vector-store, and data-source details come from `GetKnowledgeBase`.
- [fact; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html] The CloudFormation `AWS::Bedrock::Agent` resource exposes an IaC declaration surface for `FoundationModel`, `Instruction`, `ActionGroups`, `KnowledgeBases`, `MemoryConfiguration`, `GuardrailConfiguration`, `PromptOverrideConfiguration`, and `AgentCollaborators`.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] Bedrock deployment versions are immutable snapshots created through aliasing, and aliases can be redirected or paused independently of application integration code.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock trace events expose prompt text, inference parameters, rationale, invocation inputs, observations, and token usage at runtime, which means some behavior-relevant detail is richer in runtime traces than in the declared control-plane object.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] A declared Bedrock AIBOM is automatable, but it is not a single-call export, because a practical extractor must join agent metadata, action groups, knowledge-base associations, knowledge-base detail, and deployment version or alias data.
- [inference; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html] Bedrock offers two design-time extraction strategies, IaC-first extraction from templates before deployment and control-plane extraction from live agent configuration after deployment, and both strategies expose overlapping but not identical fields.

#### B. LangGraph, what the declared design surface exposes

- [fact; source: https://docs.langchain.com/oss/python/langgraph/overview] LangGraph positions itself as a low-level orchestration runtime for long-running, stateful agents rather than as a managed control plane with a single inventory API.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/graph-api] LangGraph graphs are declared through `State`, `Nodes`, and `Edges`, and the main `StateGraph` class is parameterized by a user-defined state schema.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart] Compilation is explicit through `.compile(...)`, and the compiled graph can include runtime arguments such as checkpointers and breakpoints.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langchain/tools] The documented agent pattern binds tools to a model by declaring tool functions with `@tool`, building a tool list, and calling `model.bind_tools(tools)`, which means the tool registry and its argument schema live in adjacent Python code rather than in a platform API payload.
- [fact; source: https://docs.langchain.com/oss/python/concepts/memory; https://docs.langchain.com/oss/python/langgraph/persistence] LangGraph short-term memory is part of graph state and is persisted through thread-scoped checkpoints, while long-term memory can be provided through stores that survive across conversations.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/persistence] Persistence depends on compiling the graph with a checkpointer and invoking the graph with a `thread_id`, so memory and resumability are declared partly in graph construction and partly in runtime configuration.
- [fact; source: https://docs.langchain.com/oss/python/langchain/tools] Tool definitions can access state, context, store, execution info, and server info through `ToolRuntime`, which means tool capability and authority are shaped not only by function names but also by the runtime channels exposed to the tool.
- [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langchain/tools; https://docs.langchain.com/oss/python/langgraph/persistence] A LangGraph declared AIBOM is extractable primarily from repository code and configuration conventions, because the graph topology, prompt, model binding, tool registry, state schema, and persistence choices are distributed across code artifacts instead of exposed through one control-plane API.
- [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/concepts/memory] LangGraph exposes more explicit routing and state-shape information than Bedrock does, but that exposure is only useful to automation if the repository keeps prompts, tool definitions, model initialization, and persistence configuration in machine-discoverable locations.

#### C. Representative declared AIBOM artifacts

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] The following Bedrock artifact is a representative declared AIBOM template built only from documented Bedrock fields and the schema classes defined in the prior schema-alignment item; angle-bracket values indicate extraction targets rather than observed instance values.

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.7",
  "metadata": {
    "component": {
      "type": "application",
      "name": "bedrock-agent::<GetAgent.agentId>",
      "version": "<GetAgent.agentVersion or alias target version>",
      "properties": [
        { "name": "aibom.platform", "value": "aws-bedrock-agent" },
        { "name": "aibom.extraction.mode", "value": "declared-control-plane" },
        { "name": "aibom.source.get_agent.field", "value": "instruction" }
      ]
    }
  },
  "components": [
    {
      "type": "machine-learning-model",
      "name": "foundation-model",
      "version": "<GetAgent.foundationModel>",
      "properties": [
        { "name": "aibom.source", "value": "GetAgent.foundationModel" }
      ]
    },
    {
      "type": "data",
      "name": "knowledge-base::<ListAgentKnowledgeBases.knowledgeBaseId>",
      "properties": [
        { "name": "aibom.embedding_model_arn", "value": "GetKnowledgeBase.knowledgeBaseConfiguration.vectorKnowledgeBaseConfiguration.embeddingModelArn" },
        { "name": "aibom.vector_store", "value": "GetKnowledgeBase.storageConfiguration.type" }
      ]
    },
    {
      "type": "service",
      "name": "action-group::<GetAgentActionGroup.actionGroupName>",
      "properties": [
        { "name": "aibom.schema.kind", "value": "functionSchema" },
        { "name": "aibom.source", "value": "GetAgentActionGroup.functionSchema" }
      ]
    }
  ],
  "services": [
    {
      "name": "bedrock-agent-alias",
      "properties": [
        { "name": "aibom.agent_alias", "value": "<GetAgentAlias.agentAliasId or deployment alias>" },
        { "name": "aibom.agent_version", "value": "<alias target version>" },
        { "name": "aibom.guardrail_version", "value": "<GetAgent.guardrailConfiguration.guardrailVersion>" }
      ]
    }
  ],
  "properties": [
    { "name": "aibom.instruction", "value": "GetAgent.instruction" },
    { "name": "aibom.prompt_override_configuration", "value": "GetAgent.promptOverrideConfiguration" },
    { "name": "aibom.memory_configuration", "value": "GetAgent.memoryConfiguration" }
  ]
}
```

- [inference; source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools] The following LangGraph artifact is a representative declared AIBOM template built from the documented quickstart and graph API surfaces rather than from a managed platform export; angle-bracket values indicate extraction targets rather than observed instance values.

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.7",
  "metadata": {
    "component": {
      "type": "application",
      "name": "langgraph-agent",
      "version": "<git commit, release tag, or repository revision>",
      "properties": [
        { "name": "aibom.platform", "value": "langgraph" },
        { "name": "aibom.extraction.mode", "value": "declared-source-code" }
      ]
    }
  },
  "components": [
    {
      "type": "machine-learning-model",
      "name": "<init_chat_model model identifier>",
      "properties": [
        { "name": "aibom.source", "value": "<init_chat_model(...) call site>" },
        { "name": "aibom.temperature", "value": "<init_chat_model temperature>" }
      ]
    },
    {
      "type": "service",
      "name": "tool-registry",
      "properties": [
        { "name": "aibom.tools", "value": "<tool function names discovered in source>" },
        { "name": "aibom.source", "value": "<model.bind_tools(tools) call site>" }
      ]
    },
    {
      "type": "data",
      "name": "messages-state",
      "properties": [
        { "name": "aibom.state_schema", "value": "<StateGraph state schema name>" },
        { "name": "aibom.reducer", "value": "<state reducer declaration>" }
      ]
    }
  ],
  "services": [
    {
      "name": "compiled-graph",
      "properties": [
        { "name": "aibom.graph_nodes", "value": "<builder.add_node names>" },
        { "name": "aibom.graph_edges", "value": "<builder.add_edge and add_conditional_edges wiring>" },
        { "name": "aibom.checkpointer", "value": "<compile checkpointer argument if configured>" }
      ]
    }
  ],
  "properties": [
    { "name": "aibom.system_prompt", "value": "<SystemMessage literal or prompt module path>" },
    { "name": "aibom.thread_binding", "value": "<thread_id configured at invocation when persistence is enabled>" }
  ]
}
```

#### D. Mapping to standards-aligned schema and identifying gaps

- [fact; source: https://cyclonedx.org/capabilities/mlbom/] CycloneDX ML-BOM already claims coverage for datasets, models, configurations, dataset provenance, and training methodologies.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] The prior schema-alignment item proposed extending standards-aligned AIBOMs with typed fields for prompts, retrieval surfaces, memory schemas, execution bindings, and tool permission manifests.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] Bedrock foundation model identifiers, prompt overrides, memory configuration, guardrail identifiers, action-group schemas, and knowledge-base identifiers map cleanly enough to model, service, data, and configuration objects plus typed custom properties.
- [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] LangGraph graph topology, state reducers, checkpoint threads, and tool runtime channels do not map cleanly to current CycloneDX ML-BOM primitives without custom properties or a graph-oriented extension, because the meaningful declared object is not only a package or model but an orchestrated state machine.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/concepts/memory; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Retrieval query parameters, concrete retrieved documents, evolving memory contents, and per-run rationale belong partly or wholly outside a purely declared AIBOM for both platforms, so the declared artifact must be paired conceptually with a runtime-observed companion for complete accountability.

#### E. Gap classification and CI/CD feasibility

- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html] Bedrock declared AIBOM generation is CI/CD-friendly because a pipeline can either parse CloudFormation before deployment or call control-plane APIs after deployment to produce a structured inventory without reading application source code.
- [inference; source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langchain/tools] LangGraph declared AIBOM generation is also CI/CD-feasible, but only if the repository adopts custom extraction logic or conventions that can find prompts, tool definitions, model initialization, and graph compilation sites across code files.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html; https://docs.langchain.com/oss/python/concepts/memory] Some missing fields are architectural platform gaps, for example concrete retrieved corpus snapshots or live memory contents, while other gaps are tooling gaps, for example prompt hashing, prompt-module discovery, or tool-permission manifest synthesis.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] Bedrock is the stronger declared AIBOM substrate when the goal is low-friction automated export from a managed platform, while LangGraph is the stronger declared AIBOM substrate when the goal is faithful capture of explicit orchestration topology from source-controlled code.

### §3 Reasoning

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html] Bedrock exposes declarative agent state through documented APIs, but that state is fragmented across agent, action-group, knowledge-base, and deployment resources.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools] LangGraph exposes declarative agent state through code artifacts that define graph structure, persistence, and tools.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api] Therefore, the main practical difference is not whether a declared AIBOM can be built, but whether the extractor targets a platform control plane or a code repository.
- [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] Current standards-aligned schemas can absorb much of the extracted model, data, and configuration metadata, but they still under-represent graph routing logic, prompt modules, and memory semantics without extensions.
- [assumption; source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langchain/tools] The representative LangGraph extractor assumes prompts, models, and tools remain in source-controlled code rather than being injected dynamically at runtime from external systems, because the official examples place those artifacts directly in Python code.

### §4 Consistency Check

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html] No contradiction remains on Bedrock field coverage: agent core fields come from `GetAgent`, while action groups and knowledge bases require separate list or detail calls.
- [fact; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence] No contradiction remains on LangGraph memory representation: short-term state is part of graph state and persistence is activated through checkpointers and thread-scoped checkpoints rather than through a hidden platform-managed memory object.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The main unresolved tension is not evidentiary inconsistency but boundary choice, because some behavior-shaping details are available only at runtime even when the declared design surface is rich.

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] From a software delivery perspective, Bedrock treats declared agent configuration more like a managed deployable resource, which supports audit snapshots, alias promotion, and pre-production diffing.
- [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart] From a software engineering perspective, LangGraph treats declared agent configuration more like source code for a stateful workflow, which makes orchestration logic explicit but shifts governance onto repository structure, code review, and static analysis quality.
- [inference; source: https://owaspaibom.org/; https://github.com/GenAI-Security-Project/aibom-generator; https://doi.org/10.48550/arXiv.2601.05703] Current AIBOM tooling still centers more naturally on model and training artifacts than on tool-using orchestration stacks, which explains why a practical declared-construction workflow still needs custom logic for both Bedrock and LangGraph.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The comparison sharpens a broader governance point already visible elsewhere in the corpus: managed platforms simplify extraction of sanctioned configuration, while open frameworks preserve richer design intent but require stronger local extraction discipline to make that intent inspectable.

### §6 Synthesis

**Executive summary:**

AWS Bedrock Agents and LangGraph both support declared design-time AIBOM construction, but they do so through fundamentally different extraction surfaces: Bedrock through fragmented but documented control-plane resources, and LangGraph through source-controlled graph code plus adjacent model, tool, and persistence definitions. [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart] Bedrock is easier to inventory automatically in CI/CD because its model, instruction, memory, guardrails, action groups, knowledge-base associations, and immutable versions are exposed through stable APIs and IaC resources. [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] LangGraph exposes richer orchestration topology and state semantics, but automation must recover them from repository code conventions rather than from a single platform export. [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools] In both platforms, declared AIBOMs still miss some behavior-shaping runtime facts, especially retrieved content, live memory contents, and per-run rationale, so declared construction is necessary but not sufficient for full accountability. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/concepts/memory; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

**Key findings:**

1. Bedrock exposes enough documented control-plane and IaC fields to build a declared AIBOM automatically, but the extractor must join `GetAgent`, action-group, knowledge-base, and deployment-version resources rather than relying on a single export endpoint. ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html)
2. Bedrock gives first-class declared fields for model selection, system instruction, prompt overrides, memory configuration, guardrail versioning, action schemas, and knowledge-base identifiers, which makes it a low-friction substrate for pipeline-generated declared inventories. ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html)
3. LangGraph also supports declared AIBOM construction, but its authoritative design-time artifacts are source code objects such as state schemas, nodes, edges, tool bindings, prompt literals, and checkpointer configuration instead of a managed platform manifest. ([inference]; high confidence; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools)
4. LangGraph exposes richer orchestration topology than Bedrock does, because graph structure, reducers, thread-scoped persistence, and tool runtime channels are explicit in code, but that richness is harder to inventory automatically without repository conventions or static-analysis tooling. ([inference]; medium confidence; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools)
5. Current CycloneDX and SPDX-aligned AIBOM representations can absorb much of the model, data, service, and configuration metadata from both platforms, but they still need custom properties or extensions for prompts, routing logic, memory semantics, and execution bindings. ([inference]; medium confidence; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html)
6. Declared AIBOMs for both platforms remain incomplete without a runtime companion artifact, because retrieved documents, live memory contents, query-time overrides, and per-run rationale materially affect behavior but are not fully captured in design-time configuration alone. ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/concepts/memory; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
7. The practical automation trade-off is asymmetric: Bedrock is easier to inventory from deployment infrastructure, while LangGraph is easier to inventory from source control, so the better declared AIBOM substrate depends on whether governance centers on platform APIs or repository analysis. ([inference]; medium confidence; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Bedrock declared extraction requires multiple joined resources rather than one export endpoint. | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html | high | Control-plane join |
| [inference] Bedrock exposes first-class declared fields for model, instruction, memory, guardrails, tool schema, and knowledge-base identifiers. | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html | high | API and IaC |
| [inference] LangGraph declared extraction targets source code artifacts such as graph schemas, prompts, tools, and checkpointers. | https://docs.langchain.com/oss/python/langgraph/graph-api ; https://docs.langchain.com/oss/python/langgraph/quickstart ; https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langchain/tools | high | Code-native |
| [inference] LangGraph exposes richer topology, but automation depends on repository conventions and extractor quality. | https://docs.langchain.com/oss/python/langgraph/graph-api ; https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langchain/tools | medium | Static analysis needed |
| [inference] Current standards handle much of the metadata but still need extensions for prompts, routing, memory semantics, and execution bindings. | https://cyclonedx.org/capabilities/mlbom/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html | medium | Standards gap |
| [inference] Declared AIBOMs need a runtime companion to capture retrieved content, live memory, and per-run rationale. | https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html ; https://docs.langchain.com/oss/python/concepts/memory ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Declared versus observed |
| [inference] Bedrock is stronger for platform-side inventory, while LangGraph is stronger for source-side orchestration capture. | https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.langchain.com/oss/python/langgraph/graph-api ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html | medium | Comparative synthesis |

**Assumptions:**

- [assumption; source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langchain/tools] LangGraph prompts, model bindings, and tool definitions remain in source-controlled modules that a repository scanner can parse. Justification: the official quickstart and tool examples keep those declarations in Python code.
- [assumption; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html] A Bedrock deployment either has accessible IaC templates or API permissions for control-plane reads. Justification: one of those two surfaces is required to reconstruct the declared state automatically.

**Analysis:**

The evidence weighs in favor of declared AIBOM construction being practical for both platforms, because each platform exposes stable design-time artifacts for model choice, tool surfaces, memory configuration, and orchestration structure. [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence] The stronger Bedrock case comes from its explicit control-plane resources and immutable deployment versions, which reduce extractor ambiguity and make post-deploy inventory straightforward. [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html] The stronger LangGraph case comes from explicit graph topology and state semantics, which preserve more of the orchestration design than a typical managed platform object does. [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence] A plausible rival interpretation is that stronger runtime tracing could make declared extraction less valuable, but the documented Bedrock and LangGraph surfaces still show that change control, code review, and pre-deployment governance need a design-time artifact that exists before any runtime session occurs. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/langgraph/persistence; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

**Risks, gaps, uncertainties:**

- Bedrock trace documentation shows that some prompt text, rationale, and invocation details are richer at runtime than in the declared agent object, so a declared-only AIBOM can still understate effective behavior. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html]
- LangGraph documentation describes the building blocks directly, but it does not provide a native manifest format for complete graph export, so custom extraction quality becomes a governance risk. [inference; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart]
- Current standards evidence is stronger for models, datasets, and training artifacts than for tool-using orchestration stacks, so some of the recommended mapping still depends on custom-property design from the prior schema item. [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html]
- The external literature used here is stronger on schema extension and model-training inventory than on declared agent-orchestration worked examples, which leaves the practice guidance more dependent on platform documentation than on peer-reviewed comparative case studies. [inference; source: https://arxiv.org/abs/2510.07070; https://doi.org/10.48550/arXiv.2601.05703]

**Open questions:**

- What static-analysis rules are sufficient to extract LangGraph prompts, tools, and persistence configuration robustly from larger multi-file repositories?
- Can a future CycloneDX or SPDX profile represent graph topology and tool authority as first-class edges rather than as custom properties?
- What minimum runtime companion fields are required to reconcile Bedrock session-state overrides and LangGraph thread-state mutations with the declared artifact?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-06-aibom-declared-construction-practice.md] Acronym audit result: complete for Artificial Intelligence Bill of Materials (AIBOM), Artificial Intelligence (AI), Amazon Web Services (AWS), Retrieval-Augmented Generation (RAG), Infrastructure as Code (IaC), Application Programming Interface (API), Continuous Integration and Continuous Deployment (CI/CD), Machine Learning Bill of Materials (ML-BOM), Software Package Data Exchange (SPDX), Open Worldwide Application Security Project (OWASP), and Large Language Model (LLM).
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-06-aibom-declared-construction-practice.md] Source audit result: complete; Findings and the Evidence Map use URL-backed citations, and same-repository citations use published GitHub Pages URLs.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-06-aibom-declared-construction-practice.md] Consistency audit result: complete; Key Findings, Evidence Map, and Analysis use the same comparative claims, confidence levels, and source sets.
- [inference; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html] Remaining uncertainty: standards coverage for orchestration-specific fields is still inferential rather than fully ratified by an official CycloneDX or SPDX agent profile, so overall confidence remains medium.

---

## Findings

### Executive Summary

Hypothesis: AWS Bedrock Agents and LangGraph both support declared design-time AIBOM construction, but they expose the necessary inputs through different governance surfaces, Bedrock through control-plane APIs and IaC resources, and LangGraph through source-controlled graph code plus adjacent tool and persistence definitions. [source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart]
Hypothesis: Bedrock is easier to inventory automatically in CI/CD because the declared fields that matter for model choice, instructions, memory, guardrails, action groups, and versions are all documented and machine-addressable, even though they are fragmented across several APIs. [source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html]
Hypothesis: LangGraph exposes richer orchestration topology and state semantics than Bedrock does, but extracting that declared state requires repository analysis rather than platform export because the meaningful configuration lives in code objects, prompts, tool definitions, and checkpointer setup. [source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools]
Hypothesis: In both cases, a declared AIBOM still omits important runtime facts such as retrieved documents, live memory contents, and per-run rationale, so it should be treated as the design-time half of a two-artifact accountability model. [source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/concepts/memory; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Key Findings

1. **Hypothesis: Bedrock exposes enough documented control-plane and IaC fields to build a declared AIBOM automatically, but the extractor must join `GetAgent`, action-group, knowledge-base, and deployment-version resources rather than relying on a single export endpoint.** (high confidence; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html)
2. **Hypothesis: Bedrock gives first-class declared fields for model selection, system instruction, prompt overrides, memory configuration, guardrail versioning, action schemas, and knowledge-base identifiers, which makes it a low-friction substrate for pipeline-generated declared inventories.** (high confidence; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html)
3. **Hypothesis: LangGraph also supports declared AIBOM construction, but its authoritative design-time artifacts are source code objects such as state schemas, nodes, edges, tool bindings, prompt literals, and checkpointer configuration instead of a managed platform manifest.** (high confidence; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools)
4. **Hypothesis: LangGraph exposes richer orchestration topology than Bedrock does, because graph structure, reducers, thread-scoped persistence, and tool runtime channels are explicit in code, but that richness is harder to inventory automatically without repository conventions or static-analysis tooling.** (medium confidence; source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence; https://docs.langchain.com/oss/python/langchain/tools)
5. **Hypothesis: Current CycloneDX and SPDX-aligned AIBOM representations can absorb much of the model, data, service, and configuration metadata from both platforms, but they still need custom properties or extensions for prompts, routing logic, memory semantics, and execution bindings.** (medium confidence; source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html)
6. **Hypothesis: Declared AIBOMs for both platforms remain incomplete without a runtime companion artifact, because retrieved documents, live memory contents, query-time overrides, and per-run rationale materially affect behavior but are not fully captured in design-time configuration alone.** (medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/concepts/memory; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html)
7. **Hypothesis: The practical automation trade-off is asymmetric: Bedrock is easier to inventory from deployment infrastructure, while LangGraph is easier to inventory from source control, so the better declared AIBOM substrate depends on whether governance centers on platform APIs or repository analysis.** (medium confidence; source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Bedrock declared extraction requires multiple joined resources rather than one export endpoint. | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentActionGroups.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListAgentKnowledgeBases.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html | high | Control-plane join |
| [inference] Bedrock exposes first-class declared fields for model, instruction, memory, guardrails, tool schema, and knowledge-base identifiers. | https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgentActionGroup.html ; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html | high | API and IaC |
| [inference] LangGraph declared extraction targets source code artifacts such as graph schemas, prompts, tools, and checkpointers. | https://docs.langchain.com/oss/python/langgraph/graph-api ; https://docs.langchain.com/oss/python/langgraph/quickstart ; https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langchain/tools | high | Code-native |
| [inference] LangGraph exposes richer topology, but automation depends on repository conventions and extractor quality. | https://docs.langchain.com/oss/python/langgraph/graph-api ; https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langchain/tools | medium | Static analysis needed |
| [inference] Current standards handle much of the metadata but still need extensions for prompts, routing, memory semantics, and execution bindings. | https://cyclonedx.org/capabilities/mlbom/ ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html | medium | Standards gap |
| [inference] Declared AIBOMs need a runtime companion to capture retrieved content, live memory, and per-run rationale. | https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html ; https://docs.langchain.com/oss/python/concepts/memory ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html | medium | Declared versus observed |
| [inference] Bedrock is stronger for platform-side inventory, while LangGraph is stronger for source-side orchestration capture. | https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html ; https://docs.langchain.com/oss/python/langgraph/graph-api ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html | medium | Comparative synthesis |

### Assumptions

- **Assumption:** LangGraph prompts, model bindings, and tool definitions remain in source-controlled modules that a repository scanner can parse. **Justification:** The official quickstart and tool documentation keep those artifacts in Python code, which makes static extraction a reasonable default. (source: https://docs.langchain.com/oss/python/langgraph/quickstart; https://docs.langchain.com/oss/python/langchain/tools)
- **Assumption:** A Bedrock deployment either preserves IaC templates or grants API read access to control-plane resources. **Justification:** Automated declared extraction requires at least one stable machine-readable source of truth for live or intended configuration. (source: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html; https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html)

### Analysis

Hypothesis: The evidence supports a practical declared-construction workflow for both platforms because each exposes durable design-time artifacts for models, tools, memory, and orchestration, even though those artifacts live in very different places. [source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence]
Hypothesis: Bedrock's main advantage is operational simplicity, because deployment resources and immutable versions can be queried or parsed with less ambiguity than application source code. [source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html; https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html]
Hypothesis: LangGraph's main advantage is semantic richness, because the workflow graph, state channels, reducers, and persistence choices are explicit rather than hidden behind a vendor-managed abstraction layer. [source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/persistence]
Hypothesis: A competing strategy would prioritize runtime traces only and skip declared inventories, but the source evidence shows that pre-deployment governance, change review, and version comparison still require a design-time artifact that exists before any runtime session is run. [source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/oss/python/langgraph/persistence; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

### Risks, Gaps, and Uncertainties

- Hypothesis: Bedrock trace documentation shows that prompt text, rationale, and invocation details can be richer at runtime than in the declared agent object, so a declared-only AIBOM can still understate effective behavior. [source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html]
- Hypothesis: LangGraph documentation describes the building blocks directly, but it does not provide a native manifest format for complete graph export, so custom extraction quality becomes a governance risk. [source: https://docs.langchain.com/oss/python/langgraph/graph-api; https://docs.langchain.com/oss/python/langgraph/quickstart]
- Hypothesis: Standards evidence is stronger for models, datasets, and training artifacts than for tool-using orchestration stacks, so some recommended mapping still depends on custom-property design from the prior schema item. [source: https://cyclonedx.org/capabilities/mlbom/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html]
- Hypothesis: The external literature used here is stronger on schema extension and model-training inventory than on declared agent-orchestration worked examples, which leaves the practice guidance more dependent on platform documentation than on peer-reviewed comparative case studies. [source: https://arxiv.org/abs/2510.07070; https://doi.org/10.48550/arXiv.2601.05703]

### Open Questions

- What static-analysis rules are sufficient to extract LangGraph prompts, tools, and persistence configuration robustly from larger multi-file repositories?
- Can a future CycloneDX or SPDX profile represent graph topology and tool authority as first-class edges rather than as custom properties?
- What minimum runtime companion fields are required to reconcile Bedrock session-state overrides and LangGraph thread-state mutations with the declared artifact?

---

## Output

- Type: knowledge
- Description: This item documents a concrete declared-AIBOM construction workflow for one managed agent platform and one code-native orchestration framework, and embeds representative artifacts for both. [inference; source: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html; https://docs.langchain.com/oss/python/langgraph/graph-api]
- Links:
  - https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html
  - https://docs.langchain.com/oss/python/langgraph/graph-api
  - https://davidamitchell.github.io/Research/research/2026-05-06-aibom-schema-design-standards-alignment.html
