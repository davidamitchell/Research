---
title: "How do you construct a declared design-time AI Bill of Materials (AIBOM) for a real agentic workload — a worked example using AWS Bedrock Agents and LangGraph?"
added: 2026-05-06T08:52:41+00:00
status: backlog  # backlog | in-progress | reviewing | completed
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, security, supply-chain, llm, ai-platform, governance]
started: ~
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment]
related: [2026-05-06-aibom-sbom-conceptual-gaps-theory, 2026-05-06-aibom-schema-design-standards-alignment, 2026-05-06-aibom-runtime-capture-opentelemetry-practice, 2026-05-06-aibom-platform-observability-control-comparison]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hair>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# How do you construct a declared design-time AI Bill of Materials (AIBOM) for a real agentic workload — a worked example using AWS Bedrock Agents and LangGraph?

## Research Question

How do you extract and construct a declared design-time AI Bill of Materials (AIBOM) — covering model, prompt/system instruction, tools, Retrieval-Augmented Generation (RAG) knowledge bases, and memory configuration — from two representative agentic platforms (Amazon Web Services (AWS) Bedrock Agents and LangGraph), and what does the resulting AIBOM reveal about schema gaps between the declared configuration and a standards-aligned CycloneDX or SPDX representation?

## Scope

**In scope:**
- Step-by-step process for extracting an AIBOM from AWS Bedrock Agents: via the AWS console, Infrastructure as Code (IaC) (AWS CloudFormation/CDK), and the Bedrock Agents API
- Step-by-step process for extracting an AIBOM from LangGraph: agent graph definition, tool registry, model binding, state schema
- Mapping extracted configuration fields to the CycloneDX ML-BOM / Agent BOM schema from `2026-05-06-aibom-schema-design-standards-alignment`
- Documentation of schema gaps: fields present in the platform configuration that have no CycloneDX/SPDX equivalent, and fields required by the AIBOM schema that cannot be populated from the platform
- Feasibility assessment: what can be automated in a Continuous Integration / Continuous Deployment (CI/CD) pipeline vs. what requires manual extraction
- Comparative analysis: which platform exposes more complete AIBOM-relevant configuration

**Out of scope:**
- Runtime/observed AIBOM (covered in `2026-05-06-aibom-runtime-capture-opentelemetry-practice`)
- Other platforms such as Microsoft 365 Copilot or Salesforce Agentforce (covered in `2026-05-06-aibom-platform-observability-control-comparison`)
- Conceptual schema design (covered in `2026-05-06-aibom-schema-design-standards-alignment`)

**Constraints:**
- Must use real platform documentation and APIs as primary sources — not hypothetical configurations
- Must produce at least one concrete example AIBOM artefact (JSON or YAML) per platform
- AWS Bedrock Agents and LangGraph chosen for contrast: managed Runtime Environment (RTE) vs. open orchestration framework

## Context

An AIBOM schema is only useful if it can actually be populated from real systems. This item tests that claim against two representative platforms — one managed (Bedrock Agents) and one open (LangGraph) — by attempting to construct a declared AIBOM from each using publicly available documentation, APIs, and IaC definitions. The result will be a concrete set of findings about: what is easily extractable, what requires bespoke tooling, what is not exposed at all, and how the two platforms compare. This practice item depends on the schema design work in `2026-05-06-aibom-schema-design-standards-alignment` and produces concrete input for the effectiveness and limits analysis in `2026-05-06-aibom-effectiveness-risk-mitigation-limits`.

## Approach

1. **Platform inventory — AWS Bedrock Agents:** Document all configuration fields available when defining a Bedrock Agent: foundation model selection, system prompt/instruction, action groups (tools), knowledge bases (RAG), agent collaborators, agent alias/version. Identify the API and IaC mechanisms for extracting each field.

2. **Platform inventory — LangGraph:** Document the equivalent configuration surface for a LangGraph agent: node definitions, model binding, tool/function registry, state schema (memory), conditional edges (routing logic), checkpointer configuration. Identify how to serialise the graph definition.

3. **AIBOM construction — Bedrock:** Construct a complete AIBOM JSON document for a representative Bedrock Agent using the CycloneDX ML-BOM schema extended per `2026-05-06-aibom-schema-design-standards-alignment`. Annotate each field with its source (API response field, CloudFormation property, manual entry).

4. **AIBOM construction — LangGraph:** Construct the equivalent AIBOM for a representative LangGraph agent. Annotate each field with its source.

5. **Gap analysis:** Produce a structured gap report: (a) fields in the AIBOM schema with no platform source, (b) platform configuration not captured by the schema, (c) fields requiring manual intervention. Assess which gaps are architectural (platform will never expose) vs. tooling (platform exposes but no tool extracts it).

6. **CI/CD feasibility:** Assess whether AIBOM generation can be automated as a pipeline step for each platform. Identify the minimum tooling required.

## Sources

- [ ] [AWS Bedrock Agents API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Agents_for_Amazon_Bedrock.html) — Amazon Web Services Bedrock Agents API; primary source for all programmatically accessible agent configuration fields
- [ ] [AWS Bedrock Agents User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) — AWS documentation covering Bedrock agent creation, knowledge bases, action groups, and agent aliases
- [ ] [LangGraph Documentation](https://langchain-ai.github.io/langgraph/) — LangChain LangGraph framework documentation; primary source for LangGraph agent graph definition, state schema, and tool integration
- [ ] [CycloneDX ML-BOM Specification](https://cyclonedx.org/capabilities/mlbom/) — CycloneDX machine learning component schema; the target schema for AIBOM construction
- [ ] [OWASP AIBOM Generator Project](https://owasp.org/www-project-aibom-generator/) — OWASP project providing reference implementations and tooling for AIBOM generation; potential starting point for CI/CD automation
- [ ] [AWS CloudFormation Resource Reference — AWS::Bedrock::Agent](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html) — AWS CloudFormation schema for Bedrock Agent resources; infrastructure-as-code source for declared AIBOM extraction
- [ ] [Lin et al. (2024) AIBOM: Towards a Standard Bill of Materials for AI Systems](https://arxiv.org/abs/2404.01089) — academic paper with worked AIBOM examples; reference for comparison with findings from this practical construction exercise

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
