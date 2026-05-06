---
review_count: 2
title: "How do you capture a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) in practice using OpenTelemetry tracing and platform-native observability tools?"
added: 2026-05-06T08:52:41+00:00
status: completed
priority: medium
blocks: []
tags: [agentic-ai, observability, security, llm, runtime-monitoring, ai-platform, governance]
started: 2026-05-06T22:17:27+00:00
completed: 2026-05-06T22:34:00+00:00
output: [knowledge]
cites: [2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice, 2026-04-26-ai-lowcode-observability-telemetry-governance, 2026-05-06-aibom-platform-observability-control-comparison]
related: [2026-05-06-aibom-effectiveness-risk-mitigation-limits, 2026-05-06-aibom-identity-attribution-multiagent-practice]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 6b0efe1aa27c613a4b4298ed9ec54d97710b6da6
    changed: 2026-05-06
    progress: progress/2026-05-06-aibom-runtime-capture-opentelemetry-practice.md
    summary: "Initial completion"
---

# How do you capture a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) in practice using OpenTelemetry tracing and platform-native observability tools?

## Research Question

How do you instrument a real agentic Artificial Intelligence workload, meaning a tool-using workload that plans or acts across multiple steps, to capture a runtime-observed Artificial Intelligence Bill of Materials (AIBOM), specifically using OpenTelemetry (OTel) semantic conventions for Generative Artificial Intelligence and platform-native observability tools, Amazon Web Services (AWS) Bedrock AgentCore Observability and LangSmith, and what does the captured trace data reveal about divergence from the declared AIBOM constructed in `2026-05-06-aibom-declared-construction-practice`?

## Scope

**In scope:**
- Practical instrumentation of AWS Bedrock agents using Bedrock AgentCore Observability, Amazon CloudWatch, and Bedrock trace capture.
- Practical instrumentation of a LangGraph agent using LangSmith, the OpenTelemetry Python Software Development Kit (SDK), and optional framework auto-instrumentation.
- Mapping execution trace data to runtime AIBOM fields defined in `2026-05-06-aibom-runtime-generation-divergence-theory`.
- Observed divergence documentation: which runtime components appear that a declared AIBOM would not prove in advance, and which declared components may remain unobserved in one execution.
- Storage and query patterns for runtime AIBOM data at scale, including the OpenTelemetry Collector plus Jaeger, Grafana Tempo, and OpenSearch trace analytics.
- Comparison of what each platform's native tooling captures versus what requires bespoke instrumentation.

**Out of scope:**
- Theoretical divergence modelling, covered in `2026-05-06-aibom-runtime-generation-divergence-theory`.
- Schema design for the declared AIBOM, covered in `2026-05-06-aibom-schema-design-standards-alignment`.
- Broad multi-platform comparison beyond the two implementation surfaces used here, covered in `2026-05-06-aibom-platform-observability-control-comparison`.
- Identity schema design beyond the runtime authority fields needed for trace attribution, covered in `2026-05-06-aibom-identity-attribution-multiagent-practice`.

**Constraints:**
- Use publicly documented tooling only, with no access to live production tenants required.
- Treat OpenTelemetry semantic conventions as the baseline runtime vocabulary and platform-native formats as extensions.
- Focus on what is operationally achievable with generally available tooling in 2025 and 2026.

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Prior completed work in this repository already concluded that a runtime AIBOM must combine correlation structure, content-bearing runtime events, and governance-relevant state rather than rely on one telemetry stream alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] Prior completed practice work also showed that Bedrock and LangGraph expose strong declared surfaces, but it did not show how those declared artifacts translate into runtime evidence for one observed execution.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/specs/semconv/gen-ai/] This item therefore closes the operational gap by mapping concrete Bedrock AgentCore, Bedrock trace, LangSmith, and OpenTelemetry surfaces to the runtime AIBOM model and then asking which declared fields become observable, which new runtime fields appear, and which important fields still require custom capture.

## Approach

1. **Instrumentation, AWS Bedrock:** document the steps to enable trace data from Bedrock AgentCore Observability, CloudWatch transaction search, and Bedrock agent trace events, then identify which fields populate runtime AIBOM surfaces such as model invocation, Retrieval-Augmented Generation (RAG) retrieval, tool execution, and collaborator handoff.
2. **Instrumentation, LangGraph with OpenTelemetry:** document how to instrument a LangGraph application with LangSmith, the OpenTelemetry Python SDK, and optional LangGraph or LangChain auto-instrumentation such as OpenLLMetry, then identify which fields populate the same runtime AIBOM surfaces.
3. **Runtime AIBOM extraction:** construct a representative runtime AIBOM document for one execution using trace-derived placeholders and map each trace field to topology, content, or decision-state layers from `2026-05-06-aibom-runtime-generation-divergence-theory`.
4. **Declared-versus-observed comparison:** compare the runtime evidence surface with the declared AIBOM surface from `2026-05-06-aibom-declared-construction-practice` and categorize divergence as version drift, scope expansion, absent component, unexpected component, or missing observability.
5. **Storage and query patterns:** assess how an operator would retain, index, and query runtime AIBOM traces using the OpenTelemetry Collector plus common backends, and identify which query keys matter for security and governance review.

## Sources

- [x] [OpenTelemetry Semantic Conventions for Generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - canonical status page for the Generative Artificial Intelligence semantic conventions and their maturity level.
- [x] [OpenTelemetry Generative AI Events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/) - event-level fields for prompts, outputs, tools, system instructions, tokens, and seeds.
- [x] [OpenTelemetry Generative AI Agent Spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) - agent and tool span model for agent identifiers, versions, providers, and tool execution.
- [x] [OpenTelemetry AWS Bedrock Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/) - AWS Bedrock-specific fields such as guardrail and knowledge-base identifiers.
- [x] [OpenTelemetry Python Getting Started](https://opentelemetry.io/docs/instrumentation/python/getting-started/) - official Python instrumentation guidance for `opentelemetry-instrument`, automatic instrumentation, and manual child spans.
- [x] [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) - official guidance on collector roles, batching, retries, filtering, and backend fan-out.
- [x] [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) - official overview of AgentCore observability and its OpenTelemetry-compatible telemetry.
- [x] [Amazon Bedrock AgentCore Observability Get Started](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html) - official setup steps for runtime-hosted and non-runtime-hosted agents, including AWS Distro for OpenTelemetry (ADOT).
- [x] [Amazon Bedrock AgentCore Telemetry Concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) - official definitions of sessions, traces, spans, and their hierarchy for agent monitoring.
- [x] [Amazon Bedrock AgentCore Observability Views](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html) - official CloudWatch log-group, trace, span, and metrics viewing guidance.
- [x] [Amazon Bedrock Agent Trace Events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) - official Bedrock per-step trace fields for prompts, rationale, action invocations, observations, and caller chains.
- [x] [LangSmith Trace with OpenTelemetry](https://docs.langchain.com/langsmith/trace-with-opentelemetry) - official LangSmith OpenTelemetry tracing guide and attribute mapping.
- [x] [LangSmith Observability Concepts](https://docs.langchain.com/langsmith/observability-concepts) - official definitions of projects, traces, runs, threads, and retention behavior.
- [x] [Traceloop OpenLLMetry Introduction](https://www.traceloop.com/docs/openllmetry/introduction) - official overview of OpenLLMetry as OpenTelemetry-based observability for model applications.
- [x] [OpenTelemetry Instrumentation for LangChain](https://pypi.org/project/opentelemetry-instrumentation-langchain/) - official package page for LangChain auto-instrumentation behavior and privacy defaults.
- [x] [Arize Phoenix Tracing Instrumentation](https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument) - official Phoenix tracing patterns for manual spans and OpenInference attribute helpers.
- [x] [Grafana Tempo](https://grafana.com/oss/tempo/) - official overview of Tempo as a high-scale tracing backend using object storage.
- [x] [Grafana Tempo TraceQL](https://grafana.com/docs/tempo/latest/traceql/) - official query model for selecting traces and deriving metrics from traces.
- [x] [OpenSearch Trace Analytics](https://docs.opensearch.org/latest/observing-your-data/trace/index/) - official OpenSearch trace analytics overview for OpenTelemetry ingestion and visualization.
- [x] [Jaeger Storage](https://www.jaegertracing.io/docs/2.11/storage/) - official Jaeger storage backend guidance, including OpenSearch and archive storage.
- [x] [Jaeger Architecture](https://www.jaegertracing.io/docs/2.11/architecture/) - official Jaeger role and pipeline guidance, including placing the OpenTelemetry Collector in front of Jaeger.
- [x] [David Mitchell (2026) Runtime AIBOM generation divergence theory](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html) - prior repository item defining the runtime AIBOM model used here.
- [x] [David Mitchell (2026) Declared AIBOM construction practice](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html) - prior repository item defining the declared AIBOM surfaces compared here.
- [x] [David Mitchell (2026) AI low-code observability telemetry governance](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) - prior repository item on multi-stream governance evidence and telemetry correlation.
- [x] [David Mitchell (2026) AIBOM platform observability control comparison](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html) - prior repository comparison of Bedrock and other platform control surfaces.
- [x] [David Mitchell (2026) AIBOM identity attribution multiagent practice](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html) - adjacent practice item on runtime identity and delegation fields.

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: How can one instrument AWS Bedrock and LangGraph workloads so one run yields a runtime-observed AIBOM, and what divergence from the declared AIBOM becomes visible in the resulting traces?
- Scope: Bedrock AgentCore observability, Bedrock trace events, LangSmith OpenTelemetry tracing, LangGraph runtime instrumentation, runtime-to-declared comparison, and trace storage or query patterns.
- Constraints: Use public documentation only, treat OpenTelemetry as the baseline vocabulary, keep all citations URL-backed, and stay focused on what can be implemented with currently documented tooling.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html

### §1 Question Decomposition

- **Root question:** Which currently documented telemetry surfaces let an operator reconstruct one agent run well enough to materialize a runtime AIBOM and compare it with a declared one?
  - **A. AWS Bedrock runtime capture**
    - A1. What does AgentCore Observability collect automatically for runtime-hosted agents?
    - A2. What extra setup is required for non-runtime-hosted agents?
    - A3. Which Bedrock trace-event fields correspond to runtime AIBOM topology, content, and authority surfaces?
    - A4. Which runtime AIBOM fields remain missing even after native Bedrock tracing is enabled?
  - **B. LangGraph runtime capture**
    - B1. What structural object does LangSmith call a trace, run, and thread?
    - B2. Which OpenTelemetry attributes can LangSmith ingest and map to run metadata, prompts, outputs, tools, and token usage?
    - B3. What additional instrumentation options exist for LangGraph and LangChain through OpenLLMetry or Phoenix?
    - B4. Which runtime AIBOM fields still require custom spans or metadata beyond those defaults?
  - **C. Runtime AIBOM materialization**
    - C1. Which observed fields can populate topology, content, and decision-state layers?
    - C2. Which fields can be derived from spans and which need custom snapshots or metadata attachments?
  - **D. Declared-versus-observed divergence**
    - D1. Which declared fields from the prior AIBOM item are directly observable at runtime?
    - D2. Which runtime fields represent scope expansion beyond the declared AIBOM?
    - D3. Which declared fields can remain absent in one run without indicating configuration error?
  - **E. Storage and query model**
    - E1. What role should the OpenTelemetry Collector play in a runtime AIBOM pipeline?
    - E2. How do Jaeger, Tempo, OpenSearch, and LangSmith differ as query and retention surfaces?
    - E3. Which trace keys matter most for security and governance investigations?

### §2 Investigation

#### A. AWS Bedrock AgentCore and Bedrock-native runtime capture

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html] AgentCore Observability emits OpenTelemetry-compatible telemetry, stores its metrics, spans, and logs in Amazon CloudWatch, and exposes dashboards for traces, custom-span graphs, error breakdowns, and related runtime views.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html] Runtime-hosted AgentCore agents are automatically instrumented on deployment, while non-runtime-hosted agents require AWS Distro for OpenTelemetry and may also require framework-specific instrumentors such as `opentelemetry-instrumentation-langchain`.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html] AgentCore defines a three-level observability hierarchy in which sessions hold multiple traces and each trace holds multiple spans representing discrete operations.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html] For runtime-hosted agents, AgentCore provides service-generated metrics by default, but richer agent-level spans still depend on instrumenting the agent code itself.
- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html] CloudWatch viewing guidance places traces in `/aws/spans/default`, standard runtime logs in `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/[runtime-logs]<UUID>`, and structured OpenTelemetry runtime logs in `/aws/bedrock-agentcore/runtimes/<agent_id>-<endpoint_name>/otel-rt-logs`.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Bedrock trace events expose `agentId`, `agentName`, `agentAliasId`, `agentVersion`, `sessionId`, `callerChain`, step type, prompt text, inference configuration, parser mode, rationale, invocation inputs, observations, and token-usage metadata.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] The Bedrock orchestration trace can include action-group inputs and outputs, knowledge-base activity, raw model output, parsed output, and failure traces for individual steps.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Bedrock native tooling can therefore populate runtime AIBOM fields for session and trace identity, step ordering, prompt content, retrieval and tool activity, and collaborator lineage, which are the core topology and content surfaces used in the runtime AIBOM model.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] Bedrock still does not guarantee a full decision-state layer without custom instrumentation, because memory-resource spans are partial, authority context beyond `callerChain` is limited, and any application-specific state snapshot must be attached explicitly through instrumented spans or logs.

#### B. LangGraph instrumentation through LangSmith, OpenTelemetry, OpenLLMetry, and Phoenix

- [fact; source: https://docs.langchain.com/langsmith/observability-concepts] LangSmith structures observability as projects containing traces, traces containing runs, and threads linking related traces across a conversation through shared session or conversation identifiers.
- [fact; source: https://docs.langchain.com/langsmith/observability-concepts] LangSmith retains Software as a Service trace data for 400 days from ingestion, after which traces are deleted while limited metadata is retained for usage statistics.
- [fact; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry] LangSmith supports direct OpenTelemetry ingestion for LangChain and LangGraph applications and can also ingest traces from non-LangChain applications through a standard OpenTelemetry client.
- [fact; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry] LangSmith maps OpenTelemetry attributes for messages, tool names, model identifiers, request parameters, token usage, tags, metadata, and session identifiers into its run model.
- [fact; source: https://opentelemetry.io/docs/instrumentation/python/getting-started/] The OpenTelemetry Python tooling supports both zero-code automatic instrumentation through `opentelemetry-instrument` and manual child-span creation with explicit attributes inside application code.
- [fact; source: https://www.traceloop.com/docs/openllmetry/introduction; https://pypi.org/project/opentelemetry-instrumentation-langchain/] OpenLLMetry and the LangChain instrumentation package both build on OpenTelemetry and can auto-instrument LangChain or LangGraph-adjacent workloads, while the package defaults to logging prompts, completions, and embeddings unless `TRACELOOP_TRACE_CONTENT=false` is set.
- [fact; source: https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument] Phoenix supports manual span creation, decorators, and OpenInference attribute helpers so a developer can emit richer model, tool, input, output, and token metadata into OpenTelemetry spans.
- [inference; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/instrumentation/python/getting-started/; https://www.traceloop.com/docs/openllmetry/introduction; https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument] LangGraph runtime capture is therefore composable rather than native: LangSmith can supply the run tree and conversation grouping, OpenTelemetry can supply custom spans and attributes, and OpenLLMetry or Phoenix can accelerate framework-specific capture of model and tool events.
- [inference; source: https://docs.langchain.com/langsmith/observability-concepts; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] LangGraph still requires deliberate custom instrumentation for runtime AIBOM completeness, because thread identifiers and run spans do not themselves capture the exact memory snapshot, effective authority, or retrieved-content payload unless the application adds that state as attributes, events, or linked artifacts.

#### C. Mapping trace fields to runtime AIBOM layers

- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] OpenTelemetry defines agent spans for agent identifiers, versions, providers, models, system instructions, and tool execution, while events can optionally capture input messages, output messages, system instructions, tool definitions, request parameters, response identifiers, finish reasons, and token counts.
- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/] OpenTelemetry's AWS Bedrock semantic conventions add Bedrock-specific fields such as `aws.bedrock.guardrail.id`, `aws.bedrock.knowledge_base.id`, and `gen_ai.provider.name=aws.bedrock`.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry] Bedrock trace events and LangSmith OpenTelemetry ingestion both preserve trace identity and hierarchical step information, which means either surface can anchor the topology layer of a runtime AIBOM.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The runtime AIBOM topology layer can be populated from `trace_id`, `span_id`, parent-child span links, session or thread identifiers, agent identifiers, collaborator identifiers, and service names, while the content layer can be populated from prompt text, system instructions, tool definitions, tool-call payloads, retrieved knowledge-base identifiers, output messages, and token-usage attributes.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.langchain.com/langsmith/observability-concepts; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html] The decision-state layer still needs custom additions in both ecosystems, because effective permissions, authority scope, memory snapshots, checkpoint hashes, or external policy decisions are governance-relevant but not fully represented by default in the native trace schemas.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/] Because the Generative Artificial Intelligence semantic conventions remain in development status, a runtime AIBOM should treat the OpenTelemetry field names as a strong current substrate rather than a permanently frozen schema.

- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] A representative runtime AIBOM document for one execution can therefore be materialized as follows, with angle-bracket placeholders indicating trace-derived values rather than invented instance data.

```yaml
runtime_aibom:
  execution:
    trace_id: "<otel.trace_id or bedrock.trace.traceId>"
    session_id: "<bedrock.sessionId or langsmith.session_id>"
    thread_id: "<langgraph.thread_id if present>"
    platform: "<aws-bedrock-agentcore|langgraph>"
    observed_at: "<span start timestamp>"
  topology:
    agent_id: "<gen_ai.agent.id or TracePart.agentId>"
    agent_name: "<gen_ai.agent.name or TracePart.agentName>"
    agent_version: "<gen_ai.agent.version or TracePart.agentVersion>"
    caller_chain: "<TracePart.callerChain or custom authority metadata>"
    spans:
      - name: "<span name>"
        parent_span_id: "<parent span id>"
        operation: "<gen_ai.operation.name>"
        kind: "<client|internal|tool>"
  content:
    model_request: "<gen_ai.request.model or ModelInvocationInput.foundationModel>"
    model_response: "<gen_ai.response.model if returned>"
    system_instructions: "<gen_ai.system_instructions or platform prompt field>"
    input_messages: "<gen_ai.input.messages or Bedrock prompt text>"
    output_messages: "<gen_ai.output.messages or parsed model output>"
    tool_definitions: "<gen_ai.tool.definitions or declared tool schema>"
    tool_invocations: "<tool span inputs and outputs>"
    retrieval_activity: "<aws.bedrock.knowledge_base.id or custom retriever metadata>"
    usage:
      input_tokens: "<gen_ai.usage.input_tokens>"
      output_tokens: "<gen_ai.usage.output_tokens>"
  decision_state:
    memory_snapshot_ref: "<custom checkpoint id or memory hash>"
    authority_context: "<effective principal, session role, or delegated actor>"
    guardrail_or_policy_ref: "<aws.bedrock.guardrail.id or custom policy identifier>"
    observability_mode: "<native-only|native-plus-custom>"
```

#### D. Declared-versus-observed comparison

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html] The declared AIBOM item showed that Bedrock exposes foundation model, instruction, action groups, knowledge bases, memory configuration, guardrail configuration, and version surfaces, while LangGraph exposes model binding, graph topology, state schema, tools, and persistence through source code.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry] Runtime traces add fields that the declared AIBOM does not prove in advance, including session identifiers, observed alias-target version, actual prompt text after runtime assembly, tool invocation order, retrieved knowledge-base activity, token usage, error paths, and per-run outputs.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.langchain.com/langsmith/observability-concepts] Some declared components can remain unobserved in a single run without indicating drift, such as tools that were available but never called, graph branches that were not taken, or knowledge bases that were configured but not queried.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The main divergence classes visible in practical tracing are version and configuration divergence, absent-component divergence, scope expansion through runtime-only evidence, and missing-observability divergence where a behavior happened but was not captured because content tracing or custom spans were disabled.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://pypi.org/project/opentelemetry-instrumentation-langchain/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] Missing-observability divergence is itself governance-relevant, because a declared and even correctly configured agent can still produce an incomplete runtime AIBOM if transaction search, content capture, or application-specific spans are not enabled.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Runtime authority and delegation information remain more complete on Bedrock than on a default LangSmith trace, because Bedrock publishes `callerChain` while LangGraph applications must generally attach authority lineage themselves through custom metadata.

#### E. Storage and query patterns for runtime AIBOM data

- [fact; source: https://opentelemetry.io/docs/collector/] The OpenTelemetry Collector is designed to receive, process, and export telemetry, and the official guidance recommends using it in most non-trivial environments because it can batch, retry, encrypt, and filter sensitive data before fan-out to backends.
- [fact; source: https://www.jaegertracing.io/docs/2.11/architecture/] Jaeger separates collector and query roles, can be fronted by the OpenTelemetry Collector, and explicitly recommends the OpenTelemetry Collector when operators want pre-processing, enrichment, or multi-signal handling ahead of the tracing backend.
- [fact; source: https://www.jaegertracing.io/docs/2.11/storage/] Jaeger requires persistent storage, supports Cassandra, Elasticsearch, and OpenSearch as primary distributed backends, recommends OpenSearch over Cassandra for large-scale production deployment, and also distinguishes a short-lived primary store from longer-lived archive storage.
- [fact; source: https://grafana.com/oss/tempo/; https://grafana.com/docs/tempo/latest/traceql/] Grafana Tempo is a high-scale tracing backend built around object storage, avoids trace indexing for lower cost, and uses TraceQL to select traces and perform trace-based investigations.
- [fact; source: https://docs.opensearch.org/latest/observing-your-data/trace/index/] OpenSearch trace analytics ingests and visualizes OpenTelemetry trace data and can also analyze Jaeger trace data through its observability plugin.
- [fact; source: https://docs.langchain.com/langsmith/observability-concepts] LangSmith retains traces for 400 days and offers a developer-centric trace, run, and thread model rather than a general-purpose tracing backend for arbitrary multi-service analytics.
- [inference; source: https://opentelemetry.io/docs/collector/; https://www.jaegertracing.io/docs/2.11/architecture/; https://grafana.com/oss/tempo/; https://docs.opensearch.org/latest/observing-your-data/trace/index/] A practical runtime AIBOM pipeline should therefore treat the OpenTelemetry Collector as the ingress normalization and redaction point, then route traces to one or more backends according to purpose, for example LangSmith for developer debugging, Tempo for low-cost large-volume retention, and OpenSearch or Jaeger for richer search and governance workflows.
- [inference; source: https://grafana.com/docs/tempo/latest/traceql/; https://docs.opensearch.org/latest/observing-your-data/trace/index/; https://docs.langchain.com/langsmith/trace-with-opentelemetry] Query keys that directly support incident reconstruction include trace identifier, session or thread identifier, agent version, model identifier, tool name, knowledge-base identifier, guardrail or policy reference, error type, and token or latency outliers, because those keys let investigators pivot from one incident to the exact runtime path that produced it.
- [inference; source: https://www.jaegertracing.io/docs/2.11/storage/; https://docs.langchain.com/langsmith/observability-concepts] Retention remains backend-specific rather than standardized by the runtime AIBOM model itself, so operators need a policy that distinguishes short-lived hot traces, incident-linked archive traces, and bounded-retention developer traces instead of assuming one universal trace store is sufficient.

### §3 Reasoning

- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/specs/semconv/gen-ai/] The strongest answer to the research question is that runtime AIBOM capture is already feasible with existing tools, but only as a layered assembly of native traces plus custom instrumentation rather than as a single built-in export.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/observability-concepts; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] Bedrock's native trace surface is closer to the runtime AIBOM model than LangSmith's default surface because Bedrock publishes orchestration detail, collaborator lineage, and explicit invocation payloads without the application having to define its own span structure first.
- [inference; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/instrumentation/python/getting-started/; https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument] LangGraph becomes equally expressive only when the developer chooses to emit custom spans and state attributes, because the framework and observability stack expose the mechanism but not the full runtime AIBOM payload by default.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The declared and runtime AIBOMs should therefore be treated as linked but non-identical artifacts, with the declared object defining allowed structure and the runtime object recording one realized path through that structure.
- [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry] Because this item relies on vendor documentation rather than a live execution, the representative runtime AIBOM document uses trace-derived placeholders instead of claiming observed values from a production run.

### §4 Consistency Check

- [fact; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html] There is no contradiction between Bedrock automatic instrumentation and the need for custom agent spans, because the service provides default metrics while richer agent-level span coverage still depends on instrumenting the code path.
- [fact; source: https://docs.langchain.com/langsmith/observability-concepts; https://docs.langchain.com/langsmith/trace-with-opentelemetry] There is no contradiction between LangSmith treating runs as spans and this item calling for custom OpenTelemetry spans, because LangSmith can ingest and visualize both framework-generated runs and explicitly instrumented spans or attributes.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/] There is also no contradiction between recommending OpenTelemetry as the baseline schema and warning about schema evolution, because the semantic conventions are operationally useful today while still marked as development status.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The remaining tension is observational rather than conceptual, because the runtime AIBOM model asks for memory and authority snapshots that default trace pipelines only partly expose.

### §5 Depth and Breadth Expansion

- [inference; source: https://opentelemetry.io/docs/collector/; https://pypi.org/project/opentelemetry-instrumentation-langchain/] From a privacy and governance lens, runtime AIBOM value is constrained by content-capture policy, because prompt and completion logging improves reconstruction quality but also increases the sensitivity of the resulting trace corpus.
- [inference; source: https://grafana.com/oss/tempo/; https://www.jaegertracing.io/docs/2.11/storage/] From an economic lens, backend choice changes what a runtime AIBOM can cost to keep, because object-storage-heavy backends favor high-volume retention while richer search surfaces tend to shift cost into indexing or operator complexity.
- [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html; https://docs.langchain.com/langsmith/observability-concepts] From a workflow lens, Bedrock and LangSmith optimize for different operator personas, with CloudWatch centering operational traces and LangSmith centering developer runs, evaluations, and prompt debugging.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-effectiveness-risk-mitigation-limits.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-platform-observability-control-comparison.html] From a governance lens, the most important result is not that a runtime AIBOM can be generated, but that its completeness depends on explicit observability design choices, which means AIBOM assurance must include an audit of the telemetry pipeline itself.

### §6 Synthesis

**Executive summary:**

- Runtime-observed AIBOM capture is operationally feasible today for both AWS Bedrock and LangGraph, but only as a layered telemetry assembly rather than as a single native export. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/specs/semconv/gen-ai/]
- Bedrock provides the stronger native substrate because AgentCore and Bedrock trace events already expose session and trace structure, prompts, inference settings, tool or knowledge-base activity, and caller chains, while LangGraph usually reaches the same runtime AIBOM fidelity only when LangSmith is combined with custom OpenTelemetry spans or framework auto-instrumentation. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://www.traceloop.com/docs/openllmetry/introduction]
- The runtime trace surface consistently diverges from the declared AIBOM by adding execution-specific state such as session identifiers, actual tool-call order, retrieved context, token usage, and failure paths, while some declared but dormant components remain unseen in any single run. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html]
- A practical storage design therefore needs a collector-mediated pipeline plus backend-specific retention and query strategy, because the runtime AIBOM is only as useful as the ability to preserve, search, and correlate the traces that instantiate it. [inference; source: https://opentelemetry.io/docs/collector/; https://grafana.com/docs/tempo/latest/traceql/; https://docs.opensearch.org/latest/observing-your-data/trace/index/; https://www.jaegertracing.io/docs/2.11/storage/]

**Key findings:**

1. **AWS Bedrock can populate runtime AIBOM fields for session identity, trace hierarchy, prompt text, inference configuration, tool or knowledge-base activity, and caller chains, which makes its native telemetry unusually close to the topology and content layers required by the runtime AIBOM model.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
2. **LangGraph can also yield a usable runtime AIBOM when the operator composes LangSmith traces with OpenTelemetry spans and optional framework instrumentation, because default run trees do not automatically capture every governance-relevant state surface such as memory snapshots or delegated authority context.** ([inference]; medium confidence; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://docs.langchain.com/langsmith/observability-concepts; https://opentelemetry.io/docs/instrumentation/python/getting-started/; https://www.traceloop.com/docs/openllmetry/introduction)
3. **OpenTelemetry's Generative Artificial Intelligence events and agent spans already offer a workable field vocabulary for runtime AIBOMs, including models, messages, tools, tokens, agent identifiers, and versions, but decision-state fields such as checkpointed memory or effective permissions still require application-specific attributes or linked artifacts.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/)
4. **The runtime trace surface necessarily diverges from the declared AIBOM because one observed execution reveals actual session identifiers, tool-call order, retrieved context, token usage, and failure paths that a design-time inventory cannot fully specify in advance.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
5. **A single run can legitimately omit declared components such as unused tools, untaken graph branches, or unqueried knowledge bases, so absent-component divergence must be distinguished from real configuration drift before a runtime AIBOM is used as a compliance or incident-review artifact.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.langchain.com/langsmith/observability-concepts)
6. **Missing-observability divergence is a first-class governance risk because runtime AIBOM completeness depends on enabling transaction search, content capture, and custom span emission, which means an apparently well-instrumented system can still hide decisive execution detail if the telemetry path is only partially configured.** ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://pypi.org/project/opentelemetry-instrumentation-langchain/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
7. **The OpenTelemetry Collector is a practical ingress point for runtime AIBOM pipelines because it can batch, retry, redact, and fan out traces before they reach storage backends, allowing one instrumented workload to support both developer tooling and long-retention governance stores.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/collector/; https://www.jaegertracing.io/docs/2.11/architecture/; https://docs.langchain.com/langsmith/trace-with-opentelemetry)
8. **Backend choice determines how searchable and durable a runtime AIBOM becomes, with LangSmith optimizing for developer runs, Tempo optimizing for low-cost high-volume trace retention, and Jaeger or OpenSearch providing more explicit general-purpose trace-query and archive patterns for operational investigations.** ([inference]; medium confidence; source: https://docs.langchain.com/langsmith/observability-concepts; https://grafana.com/oss/tempo/; https://grafana.com/docs/tempo/latest/traceql/; https://www.jaegertracing.io/docs/2.11/storage/; https://docs.opensearch.org/latest/observing-your-data/trace/index/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AWS Bedrock native telemetry reaches the topology and content layers of the runtime AIBOM model more directly than a generic trace stack. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | medium | session, prompts, tool flow |
| [inference] LangGraph runtime capture can be composed from LangSmith plus OpenTelemetry or equivalent custom spans for fuller governance state. | https://docs.langchain.com/langsmith/trace-with-opentelemetry ; https://docs.langchain.com/langsmith/observability-concepts ; https://opentelemetry.io/docs/instrumentation/python/getting-started/ ; https://www.traceloop.com/docs/openllmetry/introduction | medium | composable, not single native export |
| [inference] OpenTelemetry gives a workable runtime vocabulary, but not every decision-state field. | https://opentelemetry.io/docs/specs/semconv/gen-ai/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/ | medium | content rich, state partial |
| [inference] Runtime traces add execution-specific evidence beyond the declared AIBOM. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | session, order, outputs, failures |
| [inference] One run can omit declared components without implying drift. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html ; https://docs.langchain.com/langsmith/observability-concepts | medium | dormant tools, untaken branches |
| [inference] Missing-observability divergence is itself a governance problem. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html ; https://pypi.org/project/opentelemetry-instrumentation-langchain/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | high | config-dependent completeness |
| [inference] The OpenTelemetry Collector is a practical ingress point for multi-backend runtime AIBOM pipelines. | https://opentelemetry.io/docs/collector/ ; https://www.jaegertracing.io/docs/2.11/architecture/ ; https://docs.langchain.com/langsmith/trace-with-opentelemetry | medium | batching, retries, fan-out |
| [inference] Backend choice changes runtime AIBOM queryability and retention behavior. | https://docs.langchain.com/langsmith/observability-concepts ; https://grafana.com/oss/tempo/ ; https://grafana.com/docs/tempo/latest/traceql/ ; https://www.jaegertracing.io/docs/2.11/storage/ ; https://docs.opensearch.org/latest/observing-your-data/trace/index/ | medium | developer, low-cost, archive, search |

**Assumptions:**

- [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry] The representative runtime AIBOM document uses placeholders because the research task asks for operational practice without access to a live production execution.
- [assumption; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html] The current OpenTelemetry field names are stable enough to use as the baseline runtime vocabulary for this item even though the Generative Artificial Intelligence semantic conventions are still marked as development status.
- [assumption; source: https://docs.langchain.com/langsmith/observability-concepts; https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument] LangGraph applications that need runtime AIBOM completeness will accept some amount of custom instrumentation overhead rather than relying solely on framework defaults.

**Analysis:**

- The evidence supports treating runtime AIBOM capture as an observability-architecture problem instead of only a schema problem, because the decisive question is not whether fields can be named, but whether they are emitted, retained, and queryable in one correlated trace path. [inference; source: https://opentelemetry.io/docs/collector/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- Bedrock currently offers the lower-friction implementation path for native runtime evidence, because the platform already couples agent execution with trace events and CloudWatch views, whereas LangGraph gives a more open but more operator-dependent stack that must be assembled deliberately. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry]
- The declared-versus-observed comparison becomes most useful when treated as a divergence classifier rather than a pass-fail diff, because some gaps are expected properties of single-run evidence while others indicate observability design failure or genuine runtime drift. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]
- The storage evidence favors a two-plane design in practice, with one plane optimized for engineering investigation and another optimized for durable governance queries or archives, because trace backends differ materially in retention posture, query language, and operational cost. [inference; source: https://docs.langchain.com/langsmith/observability-concepts; https://grafana.com/docs/tempo/latest/traceql/; https://www.jaegertracing.io/docs/2.11/storage/; https://docs.opensearch.org/latest/observing-your-data/trace/index/]
- The main unresolved weakness is decision-state capture, because prompt, tool, and model activity are now well-covered by current tooling while effective authority, exact memory state, and some policy outcomes still depend on application-specific instrumentation design. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

**Risks, gaps, uncertainties:**

- This item is grounded in official documentation rather than a live tenant execution, so it demonstrates what can be captured and how to wire it, not an empirically observed production trace from one named agent. [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry]
- OpenTelemetry's Generative Artificial Intelligence semantic conventions are still in development status, so field names and maturity assumptions may change after this item's completion. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/]
- Bedrock service-provided observability for runtime-hosted agents emphasizes default metrics, which means organizations can still end up with incomplete runtime AIBOM traces if they do not add custom agent spans or enable the required CloudWatch trace path. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html]
- LangSmith's retention and developer-oriented run model are useful for debugging and evaluation, but long-term governance archives may still require a separate backend under operator-controlled retention policy. [inference; source: https://docs.langchain.com/langsmith/observability-concepts; https://opentelemetry.io/docs/collector/]
- Content-bearing traces can improve runtime AIBOM completeness while simultaneously increasing the sensitivity of the stored trace corpus, so trace-capture scope must be aligned with data-governance policy rather than enabled indiscriminately. [inference; source: https://pypi.org/project/opentelemetry-instrumentation-langchain/; https://opentelemetry.io/docs/collector/]

**Open questions:**

- What minimum custom span schema is sufficient to make memory snapshots and effective authority portable across Bedrock, LangGraph, and other agent runtimes?
- When a runtime AIBOM is used for incident response, which fields should be stored directly in traces and which should be linked to colder content stores or checkpoint artifacts?
- Can a standards-aligned runtime AIBOM profile be defined on top of current OpenTelemetry semantic conventions without fragmenting as the conventions evolve?

### §7 Recursive Review

- Confidence: medium
- Prior-item rescan: complete
- Acronym audit: complete
- Inline source binding: complete
- Findings and synthesis parity: aligned
- Remaining uncertainty: no live run, development-status semantic conventions

---

## Findings

### Executive Summary

Runtime-observed AIBOM capture is operationally feasible today for both AWS Bedrock and LangGraph, but only as a layered telemetry assembly rather than as a single native export. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/specs/semconv/gen-ai/]

Bedrock provides the stronger native substrate because AgentCore and Bedrock trace events already expose session and trace structure, prompts, inference settings, tool or knowledge-base activity, and caller chains, while LangGraph usually reaches the same runtime AIBOM fidelity only when LangSmith is combined with custom OpenTelemetry spans or framework auto-instrumentation. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://www.traceloop.com/docs/openllmetry/introduction]

The runtime trace surface consistently diverges from the declared AIBOM by adding execution-specific state such as session identifiers, actual tool-call order, retrieved context, token usage, and failure paths, while some declared but dormant components remain unseen in any single run. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html]

A practical storage design therefore needs a collector-mediated pipeline plus backend-specific retention and query strategy, because the runtime AIBOM is only as useful as the ability to preserve, search, and correlate the traces that instantiate it. [inference; source: https://opentelemetry.io/docs/collector/; https://grafana.com/docs/tempo/latest/traceql/; https://docs.opensearch.org/latest/observing-your-data/trace/index/; https://www.jaegertracing.io/docs/2.11/storage/]

### Key Findings

1. **AWS Bedrock can populate runtime AIBOM fields for session identity, trace hierarchy, prompt text, inference configuration, tool or knowledge-base activity, and caller chains, which makes its native telemetry unusually close to the topology and content layers required by the runtime AIBOM model.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
2. **LangGraph can also yield a usable runtime AIBOM when the operator composes LangSmith traces with OpenTelemetry spans and optional framework instrumentation, because default run trees do not automatically capture every governance-relevant state surface such as memory snapshots or delegated authority context.** ([inference]; medium confidence; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://docs.langchain.com/langsmith/observability-concepts; https://opentelemetry.io/docs/instrumentation/python/getting-started/; https://www.traceloop.com/docs/openllmetry/introduction)
3. **OpenTelemetry's Generative Artificial Intelligence events and agent spans already offer a workable field vocabulary for runtime AIBOMs, including models, messages, tools, tokens, agent identifiers, and versions, but decision-state fields such as checkpointed memory or effective permissions still require application-specific attributes or linked artifacts.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/)
4. **The runtime trace surface necessarily diverges from the declared AIBOM because one observed execution reveals actual session identifiers, tool-call order, retrieved context, token usage, and failure paths that a design-time inventory cannot fully specify in advance.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
5. **A single run can legitimately omit declared components such as unused tools, untaken graph branches, or unqueried knowledge bases, so absent-component divergence must be distinguished from real configuration drift before a runtime AIBOM is used as a compliance or incident-review artifact.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.langchain.com/langsmith/observability-concepts)
6. **Missing-observability divergence is a first-class governance risk because runtime AIBOM completeness depends on enabling transaction search, content capture, and custom span emission, which means an apparently well-instrumented system can still hide decisive execution detail if the telemetry path is only partially configured.** ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://pypi.org/project/opentelemetry-instrumentation-langchain/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
7. **The OpenTelemetry Collector is a practical ingress point for runtime AIBOM pipelines because it can batch, retry, redact, and fan out traces before they reach storage backends, allowing one instrumented workload to support both developer tooling and long-retention governance stores.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/collector/; https://www.jaegertracing.io/docs/2.11/architecture/; https://docs.langchain.com/langsmith/trace-with-opentelemetry)
8. **Backend choice determines how searchable and durable a runtime AIBOM becomes, with LangSmith optimizing for developer runs, Tempo optimizing for low-cost high-volume trace retention, and Jaeger or OpenSearch providing more explicit general-purpose trace-query and archive patterns for operational investigations.** ([inference]; medium confidence; source: https://docs.langchain.com/langsmith/observability-concepts; https://grafana.com/oss/tempo/; https://grafana.com/docs/tempo/latest/traceql/; https://www.jaegertracing.io/docs/2.11/storage/; https://docs.opensearch.org/latest/observing-your-data/trace/index/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AWS Bedrock native telemetry reaches the topology and content layers of the runtime AIBOM model more directly than a generic trace stack. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | medium | session, prompts, tool flow |
| [inference] LangGraph runtime capture can be composed from LangSmith plus OpenTelemetry or equivalent custom spans for fuller governance state. | https://docs.langchain.com/langsmith/trace-with-opentelemetry ; https://docs.langchain.com/langsmith/observability-concepts ; https://opentelemetry.io/docs/instrumentation/python/getting-started/ ; https://www.traceloop.com/docs/openllmetry/introduction | medium | composable, not single native export |
| [inference] OpenTelemetry gives a workable runtime vocabulary, but not every decision-state field. | https://opentelemetry.io/docs/specs/semconv/gen-ai/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/ | medium | content rich, state partial |
| [inference] Runtime traces add execution-specific evidence beyond the declared AIBOM. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | session, order, outputs, failures |
| [inference] One run can omit declared components without implying drift. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html ; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html ; https://docs.langchain.com/langsmith/observability-concepts | medium | dormant tools, untaken branches |
| [inference] Missing-observability divergence is itself a governance problem. | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html ; https://pypi.org/project/opentelemetry-instrumentation-langchain/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | high | config-dependent completeness |
| [inference] The OpenTelemetry Collector is a practical ingress point for multi-backend runtime AIBOM pipelines. | https://opentelemetry.io/docs/collector/ ; https://www.jaegertracing.io/docs/2.11/architecture/ ; https://docs.langchain.com/langsmith/trace-with-opentelemetry | medium | batching, retries, fan-out |
| [inference] Backend choice changes runtime AIBOM queryability and retention behavior. | https://docs.langchain.com/langsmith/observability-concepts ; https://grafana.com/oss/tempo/ ; https://grafana.com/docs/tempo/latest/traceql/ ; https://www.jaegertracing.io/docs/2.11/storage/ ; https://docs.opensearch.org/latest/observing-your-data/trace/index/ | medium | developer, low-cost, archive, search |

### Assumptions

- **Assumption:** The representative runtime AIBOM document uses placeholders because the task scope is documented practice rather than a live tenant walkthrough. **Justification:** The official Bedrock and LangSmith setup guides are sufficient to specify capture mechanics, but they do not provide one shared public trace payload for this exact comparison. [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry]
- **Assumption:** Current OpenTelemetry field names are suitable as the baseline runtime vocabulary even though the Generative Artificial Intelligence semantic conventions are not yet stable. **Justification:** The conventions are already detailed enough to model prompts, tools, usage, and agent fields, which is the practical requirement for this item. [assumption; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
- **Assumption:** LangGraph teams that need governance-grade runtime AIBOM capture will accept custom span emission or metadata attachment rather than relying on default framework traces alone. **Justification:** The official LangSmith, Phoenix, and OpenTelemetry materials all present manual or semi-automatic instrumentation as the mechanism for richer trace semantics. [assumption; source: https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://arize.com/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument; https://opentelemetry.io/docs/instrumentation/python/getting-started/]

### Analysis

The evidence supports treating runtime AIBOM capture as an observability-architecture problem instead of only a schema problem, because the decisive question is not whether fields can be named, but whether they are emitted, retained, and queryable in one correlated trace path. [inference; source: https://opentelemetry.io/docs/collector/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]

Bedrock currently offers the lower-friction implementation path for native runtime evidence, because the platform already couples agent execution with trace events and CloudWatch views, whereas LangGraph gives a more open but more operator-dependent stack that must be assembled deliberately. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry]

The declared-versus-observed comparison becomes most useful when treated as a divergence classifier rather than a pass-fail diff, because some gaps are expected properties of single-run evidence while others indicate observability design failure or genuine runtime drift. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-declared-construction-practice.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-runtime-generation-divergence-theory.html]

The storage evidence favors a two-plane design in practice, with one plane optimized for engineering investigation and another optimized for durable governance queries or archives, because trace backends differ materially in retention posture, query language, and operational cost. [inference; source: https://docs.langchain.com/langsmith/observability-concepts; https://grafana.com/docs/tempo/latest/traceql/; https://www.jaegertracing.io/docs/2.11/storage/; https://docs.opensearch.org/latest/observing-your-data/trace/index/]

The main unresolved weakness is decision-state capture, because prompt, tool, and model activity are now well-covered by current tooling while effective authority, exact memory state, and some policy outcomes still depend on application-specific instrumentation design. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-attribution-multiagent-practice.html]

### Risks, Gaps, and Uncertainties

- This item is grounded in official documentation rather than a live tenant execution, so it demonstrates what can be captured and how to wire it, not an empirically observed production trace from one named agent. [assumption; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry]
- OpenTelemetry's Generative Artificial Intelligence semantic conventions are still in development status, so field names and maturity assumptions may change after this item's completion. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/]
- Bedrock service-provided observability for runtime-hosted agents emphasizes default metrics, which means organizations can still end up with incomplete runtime AIBOM traces if they do not add custom agent spans or enable the required CloudWatch trace path. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-service-provided.html; https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html]
- LangSmith's retention and developer-oriented run model are useful for debugging and evaluation, but long-term governance archives may still require a separate backend under operator-controlled retention policy. [inference; source: https://docs.langchain.com/langsmith/observability-concepts; https://opentelemetry.io/docs/collector/]
- Content-bearing traces can improve runtime AIBOM completeness while simultaneously increasing the sensitivity of the stored trace corpus, so trace-capture scope must be aligned with data-governance policy rather than enabled indiscriminately. [inference; source: https://pypi.org/project/opentelemetry-instrumentation-langchain/; https://opentelemetry.io/docs/collector/]

### Open Questions

- What minimum custom span schema is sufficient to make memory snapshots and effective authority portable across Bedrock, LangGraph, and other agent runtimes?
- When a runtime AIBOM is used for incident response, which fields should be stored directly in traces and which should be linked to colder content stores or checkpoint artifacts?
- Can a standards-aligned runtime AIBOM profile be defined on top of current OpenTelemetry semantic conventions without fragmenting as the conventions evolve?

---

## Output

- Type: knowledge
- Description: Runtime AIBOM capture is already implementable with today's AWS Bedrock, LangSmith, and OpenTelemetry tooling, but only when the operator treats observability configuration, custom span design, and backend retention as part of the bill-of-materials control surface itself. [inference; source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html; https://docs.langchain.com/langsmith/trace-with-opentelemetry; https://opentelemetry.io/docs/collector/]
- Links:
  - https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html
  - https://docs.langchain.com/langsmith/trace-with-opentelemetry
  - https://opentelemetry.io/docs/specs/semconv/gen-ai/
