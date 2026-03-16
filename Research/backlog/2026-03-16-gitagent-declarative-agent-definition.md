---
title: "GitAgent and declarative agent definition: concepts, adoption, and cross-platform integration"
added: 2026-03-16
status: backlog  # backlog | in-progress | reviewing | completed
priority: high
blocks: []
tags: [agent, declarative-agent, gitagent, copilot, aws, azure, microsoft-365, git, ai-platform, multi-agent]
started: ~
completed: ~
output: [knowledge, backlog-item]
---

# GitAgent and declarative agent definition: concepts, adoption, and cross-platform integration

## Research Question

What is GitAgent (https://github.com/open-gitagent/gitagent), how can it be used in this repository, what concepts does it build on and produce, and how does the broader idea of declarative agent definition apply across Microsoft 365 Copilot, Amazon Web Services (AWS) Agent Core, and the Azure agentic platform?

Supporting questions:
- What is GitAgent, what problem does it solve, and what is its architecture?
- What concepts (e.g. declarative agent manifests, tool use, event-driven triggers, policy-as-code) does GitAgent build on?
- How could GitAgent be adopted or integrated in this repository's research tooling?
- How does the declarative agent definition pattern manifest across Microsoft 365 (M365) Copilot extensions, AWS Agent Core, and Azure AI Agent Service — and what are the similarities and differences?
- What is the general "declarative agent definition" concept, and what prior art or standards does it draw from (e.g. OpenAI plugin manifests, Model Context Protocol (MCP), OpenAPI specs)?

## Scope

**In scope:**
- GitAgent repository: architecture, manifest format, key concepts, and usage patterns
- Declarative agent definition as a design pattern: what it means to describe an agent's capabilities, tools, triggers, and policies in a configuration file rather than in code
- Microsoft 365 Copilot: declarative agent extensions (previously Copilot plugins), Teams AI Library, Graph connectors, and the Copilot Studio declarative agent manifest format
- AWS Agent Core: Amazon Bedrock Agents, agent action groups, knowledge bases, and how agents are declared via CloudFormation/CDK vs. code-first approaches
- Azure AI Foundry / Azure AI Agent Service: agent definitions, Azure AI Studio agent builder, Semantic Kernel agent framework
- Cross-platform comparison: what is portable, what is platform-specific, and what standards (MCP, OpenAPI, OpenAI function-calling schema) bridge the platforms
- How GitAgent relates to or uses Git as a trigger/event source for agents

**Out of scope:**
- Low-level LLM fine-tuning or training
- Pricing and commercial comparisons
- Identity and access management implementation details for each platform (beyond what is needed to understand agent authentication)
- General prompt engineering not specific to declarative agent definitions

**Constraints:** Prefer primary sources (official documentation, GitHub repositories, published specifications). GitAgent is an open-source project — inspect the repository directly. For M365, AWS, and Azure — use official documentation from 2024–2026 to capture current state.

## Context

The issue asks two interrelated questions: (1) what is GitAgent and how can it be used here; and (2) what is the general pattern of declarative agent definition across major agentic platforms. These are worth researching together because GitAgent appears to instantiate the declarative agent pattern in a Git-native way, making it a concrete reference implementation for a broader architectural concept.

This repository already uses GitHub Actions workflows and the Model Context Protocol (MCP) for agent tooling (see `.github/mcp.json`). Understanding GitAgent may reveal integration opportunities — for example, using Git events as agent triggers or defining agent capabilities declaratively rather than in procedural Python. Understanding the cross-platform landscape (M365, AWS, Azure) informs decisions about which platforms are worth targeting when exporting or deploying research agents beyond this repository.

The "declarative agent definition" concept is significant: it is the pattern by which agents advertise their capabilities, constraints, and required tools to a runtime, enabling composition, marketplace distribution, and governance. Understanding this pattern across platforms provides a foundation for future tooling decisions in this repository.

## Approach

1. **Inspect GitAgent** — clone or browse https://github.com/open-gitagent/gitagent; read the README, manifest format, architecture docs, and any examples. Identify: what runtime executes the agent, what triggers are supported, what the manifest declares, and what the agent can do.
2. **Declarative agent definition taxonomy** — survey the concept across platforms: M365 Copilot declarative agent manifest (JSON), AWS Bedrock Agent resource definitions (CloudFormation), Azure AI Agent definitions (Bicep/Azure AI Studio). Identify common fields (name, description, tools/actions, authentication, guardrails) and platform-specific extensions.
3. **Standards and prior art** — trace the genealogy of declarative agent definitions: OpenAI plugin manifests → ChatGPT plugin spec → OpenAI Assistants API → Model Context Protocol (MCP) → platform-specific formats. What standards (OpenAPI, JSON Schema) underpin each?
4. **GitAgent × this repository** — given the architecture understood in step 1, identify specific integration opportunities: could GitAgent replace or augment the research-loop workflow? Could Git push events trigger research steps? What would a GitAgent manifest for this repo look like?
5. **Cross-platform integration** — research how a GitAgent-style declarative agent can be surfaced in M365 Copilot (via Copilot Studio or Teams Toolkit), AWS (via Bedrock Agent or Agent Core), and Azure (via Azure AI Foundry). What adapters, manifests, or connectors are required?
6. **Synthesise** — produce a cross-platform comparison table and an actionable recommendation for this repository.

## Sources

- [ ] https://github.com/open-gitagent/gitagent — GitAgent source, README, and manifest specification
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agents-overview — M365 Copilot declarative agents overview
- [ ] https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/declarative-agent-manifest — M365 Copilot declarative agent manifest format
- [ ] https://learn.microsoft.com/en-us/azure/ai-services/agents/ — Azure AI Agent Service documentation
- [ ] https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html — AWS Bedrock Agents documentation
- [ ] https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore/ — AWS Agent Core announcement (verify availability during research; fall back to https://aws.amazon.com/bedrock/agents/ if not publicly documented)
- [ ] https://modelcontextprotocol.io — Model Context Protocol (MCP) specification
- [ ] https://platform.openai.com/docs/assistants/overview — OpenAI Assistants API (prior art for declarative agent pattern)
- [ ] https://semantic-kernel.readthedocs.io/en/latest/agents/ — Semantic Kernel agent framework (Azure-aligned)

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

- Type: knowledge, backlog-item
- Description:
- Links:
