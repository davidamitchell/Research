---
title: "How do you capture a runtime-observed AI Bill of Materials (AIBOM) in practice using OpenTelemetry tracing and platform-native observability tools?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, observability, security, llm, runtime-monitoring, ai-platform, governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice, 2026-04-26-ai-lowcode-observability-telemetry-governance]
related: [2026-05-06-aibom-runtime-generation-divergence-theory, 2026-05-06-aibom-declared-construction-practice, 2026-05-06-aibom-platform-observability-control-comparison, 2026-05-06-aibom-effectiveness-risk-mitigation-limits]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do you capture a runtime-observed AI Bill of Materials (AIBOM) in practice using OpenTelemetry tracing and platform-native observability tools?

## Research Question

How do you instrument a real agentic AI workload to capture a runtime-observed AI Bill of Materials (AIBOM) — specifically, using OpenTelemetry (OTel) semantic conventions for Generative AI and platform-native observability tools (AWS Bedrock AgentCore Observability, LangSmith) — and what does the captured trace data reveal about divergence from the declared AIBOM constructed in `2026-05-06-aibom-declared-construction-practice`?

## Scope

**In scope:**
- Practical instrumentation of AWS Bedrock Agents using Bedrock AgentCore Observability and AWS CloudWatch trace capture
- Practical instrumentation of a LangGraph agent using LangSmith and the OpenTelemetry Python SDK with Generative AI semantic conventions
- Mapping execution trace data to runtime AIBOM fields defined in `2026-05-06-aibom-runtime-generation-divergence-theory`
- Observed divergence documentation: which components appeared at runtime that were absent from the declared AIBOM, and which declared components were never invoked
- Storage and query patterns for runtime AIBOM data at scale: how to store, index, and query trace data for security analysis
- Comparison of what each platform's native tooling captures vs. what requires bespoke OpenTelemetry instrumentation

**Out of scope:**
- Theoretical models of divergence (covered in `2026-05-06-aibom-runtime-generation-divergence-theory`)
- Schema design for the declared AIBOM (covered in `2026-05-06-aibom-schema-design-standards-alignment`)
- Cross-platform observability comparison (covered in `2026-05-06-aibom-platform-observability-control-comparison`)
- Identity and attribution in trace data (covered in `2026-05-06-aibom-identity-attribution-multiagent-practice`)

**Constraints:**
- Must use real platform documentation and publicly available tooling — no access to live production systems required
- OpenTelemetry semantic conventions must be the baseline for trace schema; platform-native formats treated as extensions
- Focus on what is achievable with generally available tooling as of 2025/2026

## Context

Runtime AIBOM capture is where theory meets operational reality. Even if a perfect declared AIBOM schema exists, it is only useful if the runtime state can actually be captured and compared against it. This item applies the theoretical framework from `2026-05-06-aibom-runtime-generation-divergence-theory` to real platform tooling — specifically instrumenting Bedrock Agents and a LangGraph agent with OpenTelemetry tracing and platform-native observability, then extracting the equivalent of a runtime AIBOM from the resulting trace data. The resulting gap analysis between declared and observed AIBOM feeds directly into `2026-05-06-aibom-effectiveness-risk-mitigation-limits`.

## Approach

1. **Instrumentation — Bedrock Agents:** Document the steps to enable and capture trace data from a Bedrock Agent execution using Bedrock AgentCore Observability and AWS CloudWatch. Identify which trace fields correspond to runtime AIBOM fields: model invocations, RAG (knowledge base) retrievals, tool calls, agent collaborator handoffs.

2. **Instrumentation — LangGraph with OpenTelemetry:** Document how to instrument a LangGraph agent with the OpenTelemetry Python SDK using the `gen_ai.*` semantic conventions. Supplement with LangSmith traces where OTel coverage is incomplete. Capture the same categories of events as step 1.

3. **Runtime AIBOM extraction:** From the captured trace data, construct a runtime AIBOM document for one representative execution. Map each trace event to a runtime AIBOM field per the model from `2026-05-06-aibom-runtime-generation-divergence-theory`. Document any fields the trace data cannot populate.

4. **Declared-vs-observed comparison:** Compare the runtime AIBOM from step 3 with the declared AIBOM from `2026-05-06-aibom-declared-construction-practice` for the same agent. Categorise each divergence by type (version drift, scope expansion, absent component, unexpected component).

5. **Storage and query patterns:** Assess practical options for storing and querying runtime AIBOM data at scale: OpenTelemetry Collector + backend (Jaeger, Grafana Tempo, AWS OpenSearch), retention periods, and query patterns required for security audit use cases.

## Sources

- [ ] [OpenTelemetry Semantic Conventions for Generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — canonical OpenTelemetry specification for instrumenting LLM and agent operations; the required baseline for runtime AIBOM trace schema
- [ ] [AWS Bedrock AgentCore Observability Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) — AWS Bedrock agent trace event reference; primary source for Bedrock-native runtime data
- [ ] [LangSmith Documentation](https://docs.smith.langchain.com/) — LangChain LangSmith tracing and evaluation platform documentation; primary source for LangGraph runtime trace capture
- [ ] [OpenTelemetry Python SDK](https://opentelemetry-python.readthedocs.io/) — OpenTelemetry Python instrumentation library; tooling for bespoke agent instrumentation
- [ ] [Grafana Tempo — Distributed Tracing Backend](https://grafana.com/oss/tempo/) — open-source trace storage and query backend; one practical option for runtime AIBOM data storage at scale
- [ ] [OpenLLMetry — OpenTelemetry for LLM Applications](https://github.com/traceloop/openllmetry) — Traceloop open-source OTel instrumentation library for LLM frameworks including LangChain; practical tool for trace capture
- [ ] [Arize AI Phoenix — ML Observability](https://phoenix.arize.com/) — open-source ML observability platform with OpenTelemetry support; practical reference for LLM trace storage and analysis

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

3–5 sentences. What is the answer to the research question? State the key conclusion directly. Write plain prose — no prefix labels. Bind sources as trailing inline citations: `Claim text. [inference; source: https://url]`

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim with confidence and source as a trailing parenthetical. Use **suffix style** — source at the end of the claim, not at the beginning.

1. **Claim text as a complete sentence.** (high confidence; source: https://url)
2. **Claim text as a complete sentence.** (medium confidence; source: https://url1; https://url2)

Source URLs must exactly match URLs in the `## Sources` section so the generated site can render `Author (Year)` citation links. List the primary source URL(s) from `## Sources` here.

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

- Type: # skill | tool | agent | knowledge | backlog-item
- Description:
- Links:
