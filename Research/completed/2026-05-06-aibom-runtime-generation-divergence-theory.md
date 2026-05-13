---
review_count: 2
title: "How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?"
added: 2026-05-06T08:52:41+00:00
status: completed
priority: high
blocks: [2026-05-06-aibom-runtime-capture-opentelemetry-practice]
tags: [agentic-ai, governance, llm, observability, runtime-monitoring, security]
ai_themes: [agentic-ai, governance-policy, observability-monitoring, ai-architecture]
started: 2026-05-06T10:14:22+00:00
completed: 2026-05-06T10:33:39+00:00
output: [knowledge]
cites: [2026-04-26-ai-lowcode-observability-telemetry-governance, 2026-05-06-aibom-identity-delegation-trust-theory]
related: [2026-04-27-cryptographic-intent-preservation-runtime-evaluation, 2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How can a runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic Artificial Intelligence (AI) system, and how much does it diverge from the declared design-time AIBOM?

## Research Question

How can a dynamic, runtime-observed Artificial Intelligence Bill of Materials (AIBOM) be generated for an agentic Artificial Intelligence (AI) system, capturing execution traces, transient Retrieval-Augmented Generation (RAG) retrievals, tool call outputs, and memory state at decision points, and what formal models describe the divergence between a declared design-time AIBOM and what actually executes at inference time?

## Scope

**In scope:**
- Theoretical models for runtime AIBOM generation, including event-sourcing analogies, execution-trace schemas, and causality-graph capture
- What constitutes "ground truth" for a non-deterministic agent run, including snapshots, full causality graphs, and aggregated statistical representations
- Divergence taxonomy, including schema drift, version drift, tool-scope expansion, RAG retrieval variation, and memory-state divergence
- Replayability analysis, including which parts of an agent run can be replayed deterministically and which cannot
- Analogies from distributed-systems tracing and event-sourcing patterns that can be adapted for runtime AIBOMs
- Runtime provenance, traceability, and governance requirements relevant to agentic systems

**Out of scope:**
- Platform-specific tooling implementation details
- Declared AIBOM schema design
- Identity and attribution schema design beyond what is needed to explain runtime divergence

**Constraints:**
- Focus on formal and conceptual modelling
- Treat specific platform APIs as examples, not as the answer to the whole problem
- Address stochastic behaviour explicitly
- Prefer 2023+ sources where the topic is fast-moving, but allow older foundational standards where they define the underlying model

## Context

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://opentelemetry.io/docs/concepts/signals/traces/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Existing observability work in this repository and in production agent platforms already shows that runtime evidence is split across traces, content-bearing events, and audit logs rather than captured in a single self-sufficient record.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html] A runtime AIBOM is therefore best understood as a provenance and event-history problem, not only as a static inventory problem, because the relevant object is an execution history plus derived state rather than a fixed component list.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://www.nist.gov/itl/ai-risk-management-framework] The governance value of a runtime AIBOM comes from comparing declared intent with observed execution, because the highest-risk failures arise when retrieval scope, delegated authority, model configuration, or tool path differ from what was approved at design time.

## Approach

1. **Runtime AIBOM capture model:** define the minimum event and state surfaces required to reconstruct one agent run.
2. **Ground-truth problem:** compare event streams, state snapshots, and statistical summaries as competing representations of a non-deterministic run.
3. **Divergence taxonomy:** classify declared-versus-observed divergence types, including their triggers, detection methods, and governance relevance.
4. **Replayability analysis:** separate evidence-preserving replay from behaviour-reproducing replay and identify which runtime surfaces support each.
5. **Distributed-systems analogies:** map OpenTelemetry, W3C PROV, and event sourcing concepts onto a runtime AIBOM design.

## Sources

- [x] [OpenTelemetry Generative AI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) - overall standard surface for Generative Artificial Intelligence (AI) telemetry
- [x] [OpenTelemetry Traces Concept](https://opentelemetry.io/docs/concepts/signals/traces/) - trace, span, event, link, and correlation model
- [x] [OpenTelemetry Generative AI Events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/) - request, response, seed, token, tool, and conversation event fields
- [x] [OpenTelemetry Generative AI Agent Spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) - agent and tool execution span model
- [x] [OpenTelemetry Project](https://opentelemetry.io/) - vendor-neutral observability substrate
- [x] [World Wide Web Consortium (W3C) Trace Context Recommendation](https://www.w3.org/TR/trace-context/) - standard trace propagation model
- [x] [World Wide Web Consortium (W3C) PROV Overview](https://www.w3.org/TR/prov-overview/) - provenance concepts, constraints, and reproducibility goals
- [x] [Amazon Web Services (AWS) Bedrock Agent Trace Events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) - concrete runtime agent trace schema
- [x] [Amazon Web Services (AWS) Bedrock Model Invocation Logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) - request, response, metadata, and log-destination behaviour
- [x] [Fowler (2005) Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) - event-log, replay, temporal-query, and snapshot pattern
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - lifecycle governance context for runtime evidence
- [x] [David Mitchell (2026) AI low-code observability telemetry governance](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html) - completed repository item on governance telemetry surfaces
- [x] [David Mitchell (2026) AIBOM identity delegation trust theory](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html) - completed repository item on delegation-chain persistence and runtime authority
- [x] [David Mitchell (2026) UELGF runtime monitoring for non-deterministic behaviour](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html) - adjacent completed repository item on runtime precursor signals for stochastic agent systems

## Related

- [What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
- [How should identity, delegation chains, and permission scopes be formally modelled in an Artificial Intelligence Bill of Materials (AIBOM) schema to enable end-to-end attribution across agentic Artificial Intelligence (AI) systems?](https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
- [UELGF extension: agentic Artificial Intelligence (AI)-specific risks and runtime monitoring for non-deterministic behaviour](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What runtime evidence model lets a reviewer reconstruct what an agentic AI system actually used, did, and observed during one execution, and then compare that run against the declared design-time AIBOM?
- Scope: Runtime event capture, state snapshots, divergence taxonomy, replayability, and distributed-systems analogies.
- Constraints: Stay conceptual, handle stochastic behaviour explicitly, and use platform traces as exemplars rather than as a full answer.
- Output: knowledge.
- Prior completed items reviewed: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html ; https://davidamitchell.github.io/Research/research/2026-04-27-cryptographic-intent-preservation-runtime-evaluation.html

### §1 Question Decomposition

- **Root question:** What formal structure should a runtime AIBOM use so one run is attributable, reconstructable, comparable to the declared design, and useful for audit?
  - **A. Runtime capture**
    - A1. Which execution objects must be captured for one run?
    - A2. Which fields belong in traces, events, links, and state snapshots?
  - **B. Ground truth**
    - B1. Is the authoritative representation an event stream, a causality graph, a state snapshot, or a statistical summary?
    - B2. Which representation is sufficient for audit, and which is only sufficient for monitoring?
  - **C. Divergence**
    - C1. Which divergence classes arise between declared and observed AIBOMs?
    - C2. Which divergence classes are security-relevant or governance-relevant?
  - **D. Replayability**
    - D1. Which runtime surfaces can be replayed deterministically?
    - D2. Which surfaces can only be preserved as evidence, not reproduced behaviourally?
  - **E. Analogy mapping**
    - E1. How do OpenTelemetry traces map to runtime AIBOM structure?
    - E2. How do World Wide Web Consortium (W3C) PROV and event sourcing map to provenance and reconstruction?

### §2 Investigation

#### Source substitution and failed-search notes

- Search note: query `"Toward a Framework for Agentic AI Provenance"` -> no retrievable primary source matched the seeded title in this session.
- Search note: query `"Provenance-Aware Machine Learning Systems"` -> no retrievable primary source matched the seeded title in this session.

#### A. Runtime AIBOM capture model

- [fact; source: https://opentelemetry.io/docs/concepts/signals/traces/] OpenTelemetry defines a trace as correlated spans that share a `trace_id`, preserve parent-child hierarchy through `parent_id`, and carry attributes, events, links, status, and timestamps across the request path.
- [fact; source: https://www.w3.org/TR/trace-context/; https://opentelemetry.io/docs/concepts/signals/traces/] W3C Trace Context standardizes `traceparent` and `tracestate` so trace identity can cross service boundaries without breaking correlation across heterogeneous systems.
- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/] OpenTelemetry's Generative AI semantic conventions define dedicated agent and tool execution spans, including agent identity, provider, model, operation name, and optional system-instruction fields.
- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] OpenTelemetry's Generative AI events model allows opt-in capture of chat history, tool definitions, tool-call responses, system instructions, request model, sampling parameters, seed, output messages, finish reasons, and token usage.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] AWS Bedrock trace events expose concrete runtime fields for `agentId`, `agentVersion`, `sessionId`, `callerChain`, orchestration traces, knowledge-base activity, action invocations, prompt text, inference configuration, rationale, observations, and failure traces.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] AWS Bedrock model invocation logging can capture full request data, response data, and metadata for supported model calls, but it is disabled by default and only records traffic through the `bedrock-runtime` endpoint.
- [inference; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] A complete runtime AIBOM for one execution therefore needs three layers: a topology layer that records causality and correlation, a content layer that records prompts, retrievals, tool inputs, and outputs, and a decision-state layer that snapshots memory and authority context at each material choice point.

#### B. Ground truth for a non-deterministic run

- [fact; source: https://www.w3.org/TR/prov-overview/] W3C PROV defines provenance as information about entities, activities, and people involved in producing a thing, and it explicitly treats reproducibility, versioning, derivation, and procedure representation as first-class provenance requirements.
- [fact; source: https://martinfowler.com/eaaDev/EventSourcing.html] Event sourcing stores every state change as an event sequence and supports complete rebuild, temporal query, and event replay, while also recognizing that practical systems often keep application-state snapshots for performance.
- [fact; source: https://www.w3.org/TR/trace-context/] Trace Context carries portable correlation identifiers and vendor-specific context, but it does not itself encode payload semantics, state snapshots, or authorization history.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/] For a single agent run, the strongest candidate for ground truth is a full causality graph backed by immutable events, because snapshots are derived views of selected state and statistical summaries collapse away the ordering and dependency information needed for forensics.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html] A runtime AIBOM still needs decision-point snapshots in addition to the event log, because retrieval sets, prompt windows, memory state, and delegated authority may be transient at execution time even when the event stream retains the surrounding chronology.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://www.nist.gov/itl/ai-risk-management-framework] Statistical summaries across repeated runs are useful as governance evidence about behavioural envelopes, but they are not the ground truth of any single execution and should be treated as second-order projections over many runtime AIBOMs.

#### C. Divergence taxonomy between declared and observed AIBOMs

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] The completed observability item found that governance evidence is usually split across trace data, payload logging, lifecycle audit logs, and runtime execution logs, which means a declared design artifact will rarely align one-to-one with a single observed telemetry stream.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The completed identity item found that full delegation history has to be persisted outside runtime token formats because standards preserve the current authorization decision more reliably than the whole prior chain.
- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST frames Artificial Intelligence risk management as a lifecycle activity spanning design, development, use, and evaluation, which implies that design-time declarations and runtime evidence are complementary rather than substitutable governance objects.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The major divergence classes are coverage divergence, version and configuration divergence, retrieval divergence, memory-state divergence, authority divergence, topology divergence, external-state divergence, and control-policy divergence.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Coverage divergence occurs when the declared AIBOM names a component or parameter that the runtime log never observes, or when the runtime log shows content, tool traffic, or model settings that the declared AIBOM never listed.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Version and configuration divergence occurs when the observed model, prompt template, sampling parameters, tool definitions, or orchestration path differ from the declared baseline at execution time.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://www.w3.org/TR/prov-overview/] Retrieval divergence and memory-state divergence occur because context windows, retrieved chunks, and accumulated agent state are generated or selected during the run, not fixed completely at design time.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] Authority divergence and topology divergence occur when the observed caller chain, delegated actor set, or agent-to-agent path differs from the declared authority graph or task graph.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.nist.gov/itl/ai-risk-management-framework] External-state divergence and control-policy divergence occur when the same declared component set encounters different world state, or when runtime logging and guardrail settings are disabled or changed, altering auditability even if the task graph stays nominally constant.

#### D. Replayability and its limits

- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] OpenTelemetry's Generative AI events define `gen_ai.request.seed` as a field whose reuse makes repeated requests more likely to return the same result, which implies improved repeatability but not guaranteed determinism.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] AWS Bedrock traces record prompt text and inference configuration at each traced model step, which preserves key replay inputs even when the later model output is still stochastic.
- [fact; source: https://martinfowler.com/eaaDev/EventSourcing.html] Event sourcing distinguishes the event log from projections and shows that replay can rebuild prior state or support temporal query when the full ordered event history is retained.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] AWS Bedrock invocation logging stores small JSON request and response bodies in CloudWatch Logs or Amazon Simple Storage Service (Amazon S3), and offloads larger bodies or binary data to S3, which makes evidence preservation possible even when live re-execution later differs.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html] Deterministic replay is realistic for correlation structure, recorded prompts, declared tool arguments, recorded tool outputs, and policy decisions that are fully captured, but not for live re-execution of stochastic model output, mutable external APIs, or changing retrieval stores.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Incident response should therefore prefer evidence-preserving replay, meaning reconstruction from recorded artifacts, over behaviour-reproducing replay, meaning re-running the live stack and expecting the same outputs.

#### E. Distributed-systems analogies for runtime AIBOM design

- [fact; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://www.w3.org/TR/trace-context/] OpenTelemetry plus W3C Trace Context already provide a portable representation for causality, ordering, timing, parent-child structure, and cross-system correlation.
- [fact; source: https://www.w3.org/TR/prov-overview/] W3C PROV contributes the entity, activity, and agent triad plus derivation and attribution semantics, which are directly useful for representing models, prompts, retrieval artifacts, tool responses, and human or machine actors.
- [fact; source: https://martinfowler.com/eaaDev/EventSourcing.html] Event sourcing contributes the idea that the immutable event log is the system of record and that snapshots and derived views are projections built for speed or usability.
- [inference; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html] The best formal model for a runtime AIBOM is therefore an event-sourced provenance graph whose edges come from trace correlation, whose nodes are PROV-style entities, activities, and agents, and whose decision-state snapshots are projections anchored to specific graph nodes.
- [inference; source: https://opentelemetry.io/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] This model also explains why a runtime AIBOM diverges from a declared AIBOM by default, because one is a design-time capability declaration while the other is an observed run history assembled from telemetry, state capture, and provenance linkage.

### §3 Reasoning

- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] The most directly evidenced part of the model is what modern trace systems can already record: prompts, inference parameters, tool activity, retrieval activity, conversation identifiers, and caller chains.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html] The most useful formal analogies are provenance modelling and event logs, because both disciplines are explicitly designed for reconstruction, derivation, and temporal reasoning.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://opentelemetry.io/docs/concepts/signals/traces/; https://martinfowler.com/eaaDev/EventSourcing.html] Combining those sources supports a runtime AIBOM model in which the immutable record is a provenance-aware event graph rather than a flat manifest or a single point-in-time snapshot.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] The divergence taxonomy follows from the difference between declared potential and observed actuals, especially around retrieval, delegated authority, model settings, and accumulated state.
- [assumption; source: https://www.w3.org/TR/prov-overview/; https://www.nist.gov/itl/ai-risk-management-framework] Because matched academic primary sources for the two seeded provenance paper titles were not retrievable here, the conceptual conclusions lean more heavily on formal standards and platform documentation than on one named provenance-framework paper.

### §4 Consistency Check

- [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] OpenTelemetry marks the Generative AI semantic conventions as development status, so these fields are usable evidence for current practice but not yet a fully stable normative schema.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html] AWS Bedrock exposes both per-step agent traces and broader invocation logging, which supports the claim that one telemetry stream is insufficient for a full runtime AIBOM.
- [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html] There is no contradiction between calling the causality graph the strongest single-run ground truth and also requiring snapshots, because the graph is the authoritative record while snapshots are materialized evidence needed to preserve transient state that the graph alone may not retain in convenient form.
- [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] There is also no contradiction between partial replayability and persistent divergence, because recorded inputs improve reconstruction without eliminating stochastic generation or changing external world state.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.w3.org/TR/prov-overview/] From a governance lens, the runtime AIBOM should be treated as evidence infrastructure rather than only as engineering telemetry, because its purpose is to support lifecycle evaluation, accountability, and post-incident reconstruction.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] From an economic lens, the expensive surfaces are content-bearing events and large response bodies, so a practical design should preserve full-fidelity evidence for decision points and policy crossings while allowing lower-value projections elsewhere.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html] From a security lens, the most consequential divergence classes are authority divergence, retrieval divergence, and control-policy divergence, because they directly affect who could act, what information entered the decision, and whether the action remained observable.
- [inference; source: https://opentelemetry.io/; https://www.w3.org/TR/trace-context/] From an interoperability lens, using shared trace-context and telemetry conventions matters because a runtime AIBOM assembled from vendor-specific islands will fail exactly where multi-tool agent paths cross system boundaries.

### §6 Synthesis

**Executive summary:**

- A runtime-observed AIBOM is best generated as an event-sourced provenance graph plus decision-point state snapshots, and divergence should be expected whenever runtime retrieval, delegated authority, mutable external state, or dynamic orchestration choices shape the run. [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
- The strongest single-run ground truth is the causality graph of entities, activities, and agents linked by trace correlation and backed by immutable runtime events, while snapshots preserve transient context such as retrieved chunks, prompt windows, memory state, and delegated authority. [inference; source: https://www.w3.org/TR/prov-overview/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
- Declared-to-observed divergence should be modelled explicitly across coverage, configuration, retrieval, memory, authority, topology, external-state, and control-policy surfaces rather than treated as a generic drift label. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]
- Replayability is partial: evidence-preserving reconstruction is often achievable, but behaviour-reproducing re-execution is inherently limited by stochastic generation, mutable external systems, and evolving retrieval corpora. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html]

**Key findings:**

1. **A usable runtime AIBOM needs a layered representation that records trace topology, content-bearing runtime events, and decision-point state snapshots, because none of those layers alone is sufficient to reconstruct one agent run faithfully.** ([inference]; high confidence; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
2. **The best formal ground truth for a single non-deterministic run is a full causality graph backed by immutable events, while snapshots and statistical summaries are derived projections for transient-state preservation and cross-run governance analysis respectively.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/)
3. **Declared-versus-observed divergence is structurally multi-dimensional, because observed runs can differ in component coverage, model configuration, retrieval set, memory state, caller authority, orchestration path, external world state, and active logging or guardrail policy.** ([inference]; high confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
4. **Runtime AIBOM generation should treat OpenTelemetry and W3C Trace Context as the correlation substrate, W3C PROV as the provenance vocabulary, and event sourcing as the persistence pattern for the immutable run record.** ([inference]; high confidence; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://www.w3.org/TR/trace-context/; https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html)
5. **Deterministic replay is realistic for captured prompts, tool arguments, recorded tool outputs, and policy decisions, but live re-execution of model output or external API results remains only partially reproducible even when seeds and parameters are logged.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html)
6. **Authority information must be part of the runtime AIBOM itself rather than inferred later, because delegated identity chains and effective permissions are not fully preserved by runtime token formats or trace correlation alone.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
7. **For governance purposes, the most consequential runtime AIBOM divergences are not generic variance but the ones that change what information, authority, or control setting shaped the decision, because those are the divergences that alter risk exposure and auditability.** ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

**Evidence map:**

| claim | source | confidence | notes |
|---|---|---|---|
| [inference] Runtime AIBOMs need topology, content, and decision-state layers. | https://opentelemetry.io/docs/concepts/signals/traces/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | Correlation plus content plus state capture |
| [inference] Single-run ground truth is the causality graph backed by immutable events. | https://www.w3.org/TR/prov-overview/ ; https://martinfowler.com/eaaDev/EventSourcing.html ; https://opentelemetry.io/docs/concepts/signals/traces/ | high | Snapshots remain derived aids |
| [inference] Divergence is multi-dimensional rather than a single drift scalar. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | high | Coverage, config, retrieval, memory, authority, topology, external state, policy |
| [inference] OpenTelemetry, W3C PROV, and event sourcing fill different layers of the formal model. | https://opentelemetry.io/docs/concepts/signals/traces/ ; https://www.w3.org/TR/trace-context/ ; https://www.w3.org/TR/prov-overview/ ; https://martinfowler.com/eaaDev/EventSourcing.html | high | Correlation, vocabulary, persistence pattern |
| [inference] Replayability is partial even when prompts, parameters, and seeds are logged. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html ; https://martinfowler.com/eaaDev/EventSourcing.html | medium | Reconstruct evidence more reliably than behaviour |
| [inference] Delegation and authority must be recorded inside the runtime AIBOM. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | Caller chain and effective scope are decision inputs |
| [inference] Governance should prioritize divergences that alter information, authority, or active controls. | https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | Risk significance is governance-weighted |

**Assumptions:**

- [assumption; source: https://www.w3.org/TR/prov-overview/; https://opentelemetry.io/docs/specs/semconv/gen-ai/] The unmatched seeded provenance-paper titles do not overturn the core model here, because the conceptual conclusions rely mainly on accessible standards that already define provenance, trace correlation, and replay-oriented event history.
- [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/] Memory state can be treated as a snapshot surface rather than as a continuously logged stream, because the governance question is what state informed a decision point rather than every intermediate token-level mutation.

**Analysis:**

- The evidence supports modelling the runtime AIBOM as an immutable run-history object rather than as a mutable inventory record, because the strongest sources all describe provenance, tracing, and event history in terms of ordered activities and correlated state changes. [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/]
- OpenTelemetry contributes the practical correlation and field vocabulary, but its Generative AI semantic conventions are still in development, so it is a useful substrate rather than a complete stable specification for the whole runtime AIBOM. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/]
- AWS Bedrock is useful because it demonstrates that production agent traces already include the run objects this theory needs, including caller chain, prompt text, orchestration step types, rationale, observations, and failure traces, and it supports the inference that runtime evidence remains fragmented across multiple log modes. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html]
- The declared design-time AIBOM and the runtime AIBOM should therefore be treated as linked but non-identical artifacts: the first declares allowed capability and expected structure, while the second records an actual realized path through that design space. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
- A practical governance program should explicitly reject the rival idea that one can preserve per-run truth using only summary metrics or only a final-state snapshot, because both approaches lose causal structure and make later incident reconstruction materially weaker. [inference; source: https://martinfowler.com/eaaDev/EventSourcing.html; https://www.w3.org/TR/prov-overview/]

**Risks, gaps, uncertainties:**

- The OpenTelemetry Generative AI conventions are still marked development status, so a runtime AIBOM built directly on those field names may need later schema adaptation. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/]
- The unmatched seeded provenance-paper titles leave the academic framing thinner than ideal, even though the standards and platform sources are sufficient to support the core conceptual model presented here. [assumption; source: https://www.w3.org/TR/prov-overview/; https://www.nist.gov/itl/ai-risk-management-framework]
- The boundary between "memory state snapshot" and "continuous memory provenance" remains implementation-sensitive, so some systems may need deeper state capture than this conceptual baseline assumes. [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]

**Open questions:**

- What minimum snapshot schema is sufficient to preserve agent memory state at a decision point without storing every intermediate memory mutation?
- How should a declared AIBOM express acceptable retrieval variance so that normal Retrieval-Augmented Generation (RAG) behaviour is not misclassified as harmful divergence?
- Which divergence classes should trigger immediate policy intervention versus post-run audit only?

### §7 Recursive Review

- Outcome: pass.
- Confidence: medium.
- Rationale: key claims are supported by accessible standards, vendor documentation, and adjacent completed repository items, but the Generative AI telemetry conventions remain development status and the two seeded provenance-paper titles were not retrievable as matching primary sources in this session.
- Acronym audit: Artificial Intelligence (AI), Artificial Intelligence Bill of Materials (AIBOM), Retrieval-Augmented Generation (RAG), Large Language Model (LLM), World Wide Web Consortium (W3C), Amazon Web Services (AWS), Amazon Simple Storage Service (Amazon S3), National Institute of Standards and Technology (NIST), and OpenTelemetry were expanded on first use in the document where applicable.
- Findings parity check: §6 Synthesis and `## Findings` are substantively aligned.

---

## Findings

### Executive Summary

A runtime-observed AIBOM is best generated as an event-sourced provenance graph plus decision-point state snapshots, and divergence should be expected whenever runtime retrieval, delegated authority, mutable external state, or dynamic orchestration choices shape the run. [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
The strongest single-run ground truth is the causality graph of entities, activities, and agents linked by trace correlation and backed by immutable runtime events, while snapshots preserve transient context such as retrieved chunks, prompt windows, memory state, and delegated authority. [inference; source: https://www.w3.org/TR/prov-overview/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]
Declared-to-observed divergence should be modelled explicitly across coverage, configuration, retrieval, memory, authority, topology, external-state, and control-policy surfaces rather than treated as a generic drift label. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html]
Replayability is partial: evidence-preserving reconstruction is often achievable, but behaviour-reproducing re-execution is inherently limited by stochastic generation, mutable external systems, and evolving retrieval corpora. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html]

### Key Findings

1. **A usable runtime AIBOM needs a layered representation that records trace topology, content-bearing runtime events, and decision-point state snapshots, because none of those layers alone is sufficient to reconstruct one agent run faithfully.** ([inference]; high confidence; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
2. **The best formal ground truth for a single non-deterministic run is a full causality graph backed by immutable events, while snapshots and statistical summaries are derived projections for transient-state preservation and cross-run governance analysis respectively.** ([inference]; high confidence; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/)
3. **Declared-versus-observed divergence is structurally multi-dimensional, because observed runs can differ in component coverage, model configuration, retrieval set, memory state, caller authority, orchestration path, external world state, and active logging or guardrail policy.** ([inference]; high confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html)
4. **Runtime AIBOM generation should treat OpenTelemetry and W3C Trace Context as the correlation substrate, W3C PROV as the provenance vocabulary, and event sourcing as the persistence pattern for the immutable run record.** ([inference]; high confidence; source: https://opentelemetry.io/docs/concepts/signals/traces/; https://www.w3.org/TR/trace-context/; https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html)
5. **Deterministic replay is realistic for captured prompts, tool arguments, recorded tool outputs, and policy decisions, but live re-execution of model output or external API results remains only partially reproducible even when seeds and parameters are logged.** ([inference]; medium confidence; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://martinfowler.com/eaaDev/EventSourcing.html)
6. **Authority information must be part of the runtime AIBOM itself rather than inferred later, because delegated identity chains and effective permissions are not fully preserved by runtime token formats or trace correlation alone.** ([inference]; high confidence; source: https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
7. **For governance purposes, the most consequential runtime AIBOM divergences are not generic variance but the ones that change what information, authority, or control setting shaped the decision, because those are the divergences that alter risk exposure and auditability.** ([inference]; medium confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Runtime AIBOMs need topology, content, and decision-state layers. | https://opentelemetry.io/docs/concepts/signals/traces/ ; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | Correlation plus content plus state capture |
| [inference] Single-run ground truth is the causality graph backed by immutable events. | https://www.w3.org/TR/prov-overview/ ; https://martinfowler.com/eaaDev/EventSourcing.html ; https://opentelemetry.io/docs/concepts/signals/traces/ | high | Snapshots remain derived aids |
| [inference] Divergence is multi-dimensional rather than a single drift scalar. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html ; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html | high | Coverage, config, retrieval, memory, authority, topology, external state, policy |
| [inference] OpenTelemetry, W3C PROV, and event sourcing fill different layers of the formal model. | https://opentelemetry.io/docs/concepts/signals/traces/ ; https://www.w3.org/TR/trace-context/ ; https://www.w3.org/TR/prov-overview/ ; https://martinfowler.com/eaaDev/EventSourcing.html | high | Correlation, vocabulary, persistence pattern |
| [inference] Replayability is partial even when prompts, parameters, and seeds are logged. | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/ ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html ; https://martinfowler.com/eaaDev/EventSourcing.html | medium | Reconstruct evidence more reliably than behaviour |
| [inference] Delegation and authority must be recorded inside the runtime AIBOM. | https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html | high | Caller chain and effective scope are decision inputs |
| [inference] Governance should prioritize divergences that alter information, authority, or active controls. | https://www.nist.gov/itl/ai-risk-management-framework ; https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-agentic-ai-specific-risks-runtime-monitoring.html ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html | medium | Risk significance is governance-weighted |

### Assumptions

- **Assumption:** The unmatched seeded provenance-paper titles do not overturn the core model here. **Justification:** the conceptual conclusions rely mainly on accessible standards that already define provenance, trace correlation, and replay-oriented event history. [assumption; source: https://www.w3.org/TR/prov-overview/; https://opentelemetry.io/docs/specs/semconv/gen-ai/]
- **Assumption:** Memory state can be treated as a snapshot surface rather than as a continuously logged stream. **Justification:** the governance question is what state informed a decision point rather than every intermediate token-level mutation. [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]

### Analysis

The evidence supports modelling the runtime AIBOM as an immutable run-history object rather than as a mutable inventory record, because the strongest sources all describe provenance, tracing, and event history in terms of ordered activities and correlated state changes. [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/]
OpenTelemetry contributes the practical correlation and field vocabulary, but its Generative AI semantic conventions are still in development, so it is a useful substrate rather than a complete stable specification for the whole runtime AIBOM. [inference; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/]
AWS Bedrock is useful because it demonstrates that production agent traces already include the run objects this theory needs, including caller chain, prompt text, orchestration step types, rationale, observations, and failure traces, and it supports the inference that runtime evidence remains fragmented across multiple log modes. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html]
The declared design-time AIBOM and the runtime AIBOM should therefore be treated as linked but non-identical artifacts: the first declares allowed capability and expected structure, while the second records an actual realized path through that design space. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://davidamitchell.github.io/Research/research/2026-05-06-aibom-identity-delegation-trust-theory.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html]
A practical governance program should explicitly reject the rival idea that one can preserve per-run truth using only summary metrics or only a final-state snapshot, because both approaches lose causal structure and make later incident reconstruction materially weaker. [inference; source: https://martinfowler.com/eaaDev/EventSourcing.html; https://www.w3.org/TR/prov-overview/]

### Risks, Gaps, and Uncertainties

The OpenTelemetry Generative AI conventions are still marked development status, so a runtime AIBOM built directly on those field names may need later schema adaptation. [fact; source: https://opentelemetry.io/docs/specs/semconv/gen-ai/]
The unmatched seeded provenance-paper titles leave the academic framing thinner than ideal, even though the standards and platform sources are sufficient to support the core conceptual model presented here. [assumption; source: https://www.w3.org/TR/prov-overview/; https://www.nist.gov/itl/ai-risk-management-framework]
The boundary between "memory state snapshot" and "continuous memory provenance" remains implementation-sensitive, so some systems may need deeper state capture than this conceptual baseline assumes. [assumption; source: https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html; https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/]

### Open Questions

- What minimum snapshot schema is sufficient to preserve agent memory state at a decision point without storing every intermediate memory mutation?
- How should a declared AIBOM express acceptable Retrieval-Augmented Generation (RAG) variance so that normal retrieval behaviour is not misclassified as harmful divergence?
- Which divergence classes should trigger immediate policy intervention versus post-run audit only?

---

## Output

- Type: knowledge
- Description: This item produces a formal model for generating a runtime-observed AIBOM as an event-sourced provenance graph with decision-point snapshots, plus a divergence taxonomy and replayability boundary suitable for governance and audit design. [inference; source: https://www.w3.org/TR/prov-overview/; https://martinfowler.com/eaaDev/EventSourcing.html; https://opentelemetry.io/docs/concepts/signals/traces/]
- Links:
  - https://www.w3.org/TR/prov-overview/
  - https://opentelemetry.io/docs/concepts/signals/traces/
  - https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html
