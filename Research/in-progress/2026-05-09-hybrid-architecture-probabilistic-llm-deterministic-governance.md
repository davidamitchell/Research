---
review_count: 1
title: "Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement"
added: 2026-05-09T22:44:23+00:00
status: reviewing
priority: high
blocks:
  - 2026-05-09-llm-determinism-limits-temperature-zero
tags: [agentic-ai, llm, ai-governance, workflow, policy-enforcement, human-oversight, enterprise-architecture]
started: 2026-05-09T23:02:09+00:00
completed: ~
output: []
cites:
  - 2026-04-26-ai-lowcode-governance-enforcement-architecture
  - 2026-04-26-ai-lowcode-observability-telemetry-governance
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-04-26-ai-agent-control-plane-architecture-enterprise
related:
  - 2026-04-26-ai-lowcode-failure-modes-governance-mitigation
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
  - 2026-04-26-data-governance-ai-lowcode-enterprise-enforcement
  - 2026-04-26-deployment-pipeline-citizen-development-governed-gate
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Hybrid Architecture Design: Probabilistic Large Language Models (LLMs) for Interpretation, Deterministic Layers for Governance Enforcement

## Research Question

How should hybrid architectures be designed so that probabilistic LLMs handle interpretation and insight generation while deterministic layers enforce final governance, compliance, and high-stakes decisions?

## Scope

**In scope:**
- Architectural patterns that separate probabilistic reasoning from deterministic enforcement, including guardrails, machine-readable policy engines such as Open Policy Agent (OPA), and explicit approval workflows
- Published reference architectures, design patterns, or case studies implementing this separation
- Interface design between the probabilistic and deterministic layers, including structured outputs, validation schemas, tool-call boundaries, and fallback triggers
- Failure modes and edge cases where the separation breaks down

**Out of scope:**
- Pure research on model capability without an architectural control boundary
- Consumer use cases with no governance, compliance, or enterprise operating context

**Constraints:** Focus on enterprise-scale deployments; consider latency, auditability, and operator override requirements.

## Context

- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] Enterprise governance only becomes enforceable when controls sit at concrete execution points instead of inside prompts or policy documents, so this item focuses on the architectural handoff between interpretation and enforcement.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] High-stakes review paths require real human override and safe-stop capability, which means the final control layer cannot be a free-form model response alone.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/] Auditability depends on combining model traces with policy-decision evidence, because either stream alone leaves important blind spots about why an action was or was not allowed.

## Approach

1. Survey published hybrid Artificial Intelligence (AI) architecture patterns that separate probabilistic reasoning from deterministic enforcement.
2. Review industry implementations, especially Amazon Web Services (AWS) Bedrock Guardrails, Azure AI Content Safety, Palantir Artificial Intelligence Platform (AIP), and Open Policy Agent (OPA), for design principles.
3. Identify interface-contract patterns, specifically how the LLM output is structured, validated, normalized, and passed to the deterministic layer.
4. Analyze failure modes, including invalid structured output, misaligned tool use, prompt injection exposure, and policy ambiguity.
5. Produce design recommendations with trade-off analysis, especially latency versus safety and expressiveness versus auditability.

## Sources

- [x] [Amazon Web Services Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [x] [Amazon Web Services Bedrock Guardrails: how it works](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html)
- [x] [Amazon Web Services Bedrock Guardrails: selective input tagging](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html)
- [x] [Amazon Web Services Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [x] [Azure AI Content Safety overview](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- [x] [Azure AI Content Safety task adherence concepts](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence)
- [x] [Anthropic tool use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
- [x] [Open Policy Agent documentation](https://www.openpolicyagent.org/docs/latest/)
- [x] [Open Policy Agent bundle management](https://www.openpolicyagent.org/docs/latest/management-bundles/)
- [x] [Open Policy Agent decision logs](https://www.openpolicyagent.org/docs/latest/management-decision-logs/)
- [x] [Yao et al. (2023) ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [x] [Weng (2023) LLM-powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF) Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [x] [European Union (EU) AI Act Service Desk, Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)
- [x] [Palantir AIP overview](https://www.palantir.com/docs/foundry/aip/overview)
- [x] [Palantir AI ethics and governance](https://www.palantir.com/docs/foundry/aip/ethics-governance)
- [x] [Where should governance enforcement points be implemented within enterprise architecture, and how should controls be applied consistently for AI and low-code systems?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html)
- [x] [What observability and telemetry model is required to govern Artificial Intelligence (AI) and low-code systems at scale?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html)
- [x] [When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
- [x] [What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)

## Related

- [What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
- [What are the primary failure modes in enterprise Artificial Intelligence (AI) and low-code deployments, and how can governance systems be designed to mitigate them?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.html)
- [Deployment pipeline as the only enforceable control gate for citizen-developed agents: DevOps literature support, low-code platform hook points, and architectural enforceability](https://davidamitchell.github.io/Research/research/2026-04-26-deployment-pipeline-citizen-development-governed-gate.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://www.openpolicyagent.org/docs/latest/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] **Research question restated:** this item asks how enterprises should let a Large Language Model (LLM) interpret ambiguous inputs and generate candidate reasoning while moving final allow, deny, escalate, and override decisions into deterministic control layers.
- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] **Scope confirmed:** the investigation covers planner or executor separation, structured tool-call boundaries, pre-inference and post-inference controls, tool-use validation, failure handling, and human override requirements for enterprise systems.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/] **Constraints confirmed:** the answer must remain operable at enterprise scale, preserve audit evidence, manage latency, and keep deterministic control logic externalized enough to change faster than application releases.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-governance-enforcement-architecture.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] **Prior work cross-reference:** prior completed items already established concrete enforcement surfaces, attributable telemetry, human-review failure modes, and central control-plane patterns, so this item narrows the problem to the boundary between generative interpretation and final governance.
- [fact; source: https://www.openpolicyagent.org/docs/latest/; https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] **Output format confirmed:** knowledge, specifically a reference pattern for hybrid architecture, interface contracts, control placement, and failure handling.

### §1 Question Decomposition

- **Root question:** what architecture lets an LLM add useful interpretation without allowing stochastic output to become the final governance authority?
- **A. Architectural split**
  - A1. Which reviewed sources explicitly separate planning, reasoning, or interpretation from execution and enforcement?
  - A2. Which reviewed sources show deterministic enforcement as a distinct control layer rather than an optional prompt pattern?
- **B. Interface contract**
  - B1. What should the LLM be allowed to emit, free text, structured proposals, or executable actions?
  - B2. What schema, validation, and normalization steps are required before a deterministic layer can decide?
- **C. Enforcement path**
  - C1. Which controls should run before model inference, after model inference, and before any side effect?
  - C2. When is vendor-native enforcement sufficient, and when is an external policy engine or approval layer still required?
- **D. Failure handling**
  - D1. What happens when the model produces invalid structure, unsafe content, misaligned tool plans, or unsupported states?
  - D2. Which failures should trigger deny, retry, degrade, or human review?
- **E. Governance evidence**
  - E1. Which logs and trace fields are needed to reconstruct both model behavior and deterministic decisions?
  - E2. Which human-stop and override capabilities are required for high-stakes deployments?

### §2 Investigation

#### A. Sources that already separate reasoning from execution

- [fact; source: https://lilianweng.github.io/posts/2023-06-23-agent/] Weng's agent overview describes a Large Language Model (LLM) as the system's core controller while planning, memory, and tool use are distinct components, which means the architectural unit is already a composition rather than a single model call.
- [fact; source: https://arxiv.org/abs/2210.03629] ReAct explicitly separates reasoning traces from environment actions and uses external interfaces such as a Wikipedia Application Programming Interface (API), showing that useful task performance can come from an LLM that proposes and sequences actions rather than directly owning the environment.
- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Anthropic's tool-use model returns structured `tool_use` blocks to the client application, which then executes the tool and returns a `tool_result`, so the runtime that performs side effects is intentionally outside the model.
- [inference; source: https://lilianweng.github.io/posts/2023-06-23-agent/; https://arxiv.org/abs/2210.03629; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The reviewed agent literature and current tool-use documentation therefore converge on the same control pattern: the model is useful as a planner, interpreter, or proposal engine, but the authoritative executor remains an external component.

#### B. Deterministic control surfaces in current vendor platforms

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] Amazon Bedrock Guardrails evaluates input prompts against configured policies before foundation model (FM) inference, discards inference entirely when the input violates guardrail policy, then evaluates model responses and can override them with blocked messaging or masking after generation.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] Bedrock evaluates configured input policies in parallel for improved latency, which shows that deterministic guardrails are treated as an execution-stage subsystem with their own performance budget rather than as a prompt-only convention.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview] Azure AI Content Safety exposes prompt-attack detection, groundedness checks, protected-material detection, harmful-content scoring, and custom categories, which means Microsoft also places a distinct moderation and control layer around model inputs and outputs.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence] Azure Task Adherence detects when an agent's planned tool invocation is misaligned with user intent, can block execution, and can escalate the case for human review, which makes the tool-approval boundary explicit rather than implicit.
- [fact; source: https://www.palantir.com/docs/foundry/aip/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance] Palantir AIP documents access controls, audit trails, structured approval workflows, checkpoints, workflow lineage, and human-oversight workflows that keep operational authority in governed platform processes instead of in raw model output.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.palantir.com/docs/foundry/aip/ethics-governance] The common vendor pattern is not "make the model safer and trust it completely" but "insert deterministic gates that can block, mask, route, or require approval before an unsafe or misaligned action is executed."

#### C. Policy engines and externalized governance logic

- [fact; source: https://www.openpolicyagent.org/docs/latest/] OPA decouples policy decision-making from policy enforcement, accepts structured input such as JavaScript Object Notation (JSON), and can return arbitrary structured output instead of only allow or deny booleans.
- [fact; source: https://www.openpolicyagent.org/docs/latest/management-bundles/] OPA bundles let policies and related data be updated on the fly, enforced immediately after activation, and distributed in an eventually consistent manner without restarting the governed service.
- [fact; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/] OPA decision logs include the queried policy path, input, result, bundle revision, decision identifier, trace identifier, span identifier, and timestamp, which provides deterministic evidence about what rule set produced a given decision.
- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST Artificial Intelligence Risk Management Framework (AI RMF) Govern 1.5 requires ongoing monitoring and periodic review with clearly defined roles and responsibilities, and Govern 2.1 requires documented roles and communication lines for managing AI risk.
- [inference; source: https://www.openpolicyagent.org/docs/latest/; https://www.openpolicyagent.org/docs/latest/management-bundles/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] For enterprise hybrid design, the deterministic layer should not be embedded only inside application code or prompts, because versioned external policy allows governance logic to evolve, be audited, and be assigned to accountable owners.

#### D. Interface contracts between the model and the deterministic layer

- [fact; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] Anthropic recommends defining tools with explicit schemas and allows `strict: true` so tool calls always match the declared schema exactly.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html] Bedrock input tagging allows an application to mark only selected spans, such as the current user request, for guardrail processing and recommends a random per-request tag suffix to reduce prompt-injection risk.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence] Azure Task Adherence compares proposed tool actions against user intent and flags or blocks plans that are premature or out of scope, such as sending an email when the user asked only for a draft.
- [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence] The architecture boundary should therefore be a typed proposal record, not a free-form paragraph, because the deterministic layer needs normalized fields it can validate against schemas, intent checks, policy rules, and approval thresholds.
- [inference; source: https://www.openpolicyagent.org/docs/latest/; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] A practical contract is for the LLM to emit structured fields such as requested action, target system, data sensitivity, user-intent summary, and supporting rationale, while the deterministic layer decides whether that proposed action is allowed, denied, rewritten, or escalated.

#### E. Failure modes and deterministic responses

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] Bedrock documents at least three distinct control outcomes, discard inference before model execution, override or mask unsafe output after execution, and return a configured blocked message, which implies that hybrid systems need more than one failure response.
- [fact; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence] Azure documents multiple postures, harmful-content scoring, prompt-attack detection, groundedness checks, and tool-plan misalignment checks, each of which can drive blocking or human-review escalation.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] Article 14 requires assigned overseers to understand system limitations, detect anomalies and unexpected performance, disregard, override, or reverse system output, and intervene or interrupt the system through a stop function or similar safe-state procedure.
- [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] Invalid structure, unsupported action types, misaligned tool plans, or policy ambiguities should fail closed to deny or escalate rather than degrade into free-text fallback, because those are precisely the moments when the deterministic layer has lost authoritative control.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] Human review should not be a blanket review of every model output, because that creates automation-bias and rubber-stamping risk; it should be a bounded exception path for consequential, ambiguous, or policy-conflicted proposals.

#### F. Auditability and operating model

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Bedrock model invocation logging can capture full request data, response data, and metadata for supported runtime calls and deliver that evidence to Amazon Simple Storage Service (Amazon S3) or CloudWatch Logs.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Bedrock also notes that calls through the `bedrock-mantle` Responses Application Programming Interface (API) path are not currently captured by invocation logging, so audit coverage depends on which runtime path an application uses.
- [fact; source: https://www.openpolicyagent.org/docs/latest/management-decision-logs/] OPA decision logs add deterministic reconstruction fields, including policy revision and decision identifiers, that model-invocation logs do not provide by themselves.
- [fact; source: https://www.palantir.com/docs/foundry/aip/ethics-governance] Palantir documents workflow lineage, audit logs, structured approvals, and checkpoints that tie actions and sign-offs to named actors and operational workflows.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://www.palantir.com/docs/foundry/aip/ethics-governance; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-observability-telemetry-governance.html] A governed hybrid architecture therefore needs at least two evidence streams, model execution traces and deterministic decision logs, joined by correlation identifiers so investigators can reconstruct both what the model proposed and why the control layer allowed, blocked, or escalated it.

### §3 Reasoning

- [inference; source: https://lilianweng.github.io/posts/2023-06-23-agent/; https://arxiv.org/abs/2210.03629; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview] The recurring architectural pattern across agent literature and current vendor tooling is that the model is strongest as an interpreter and planner, while execution authority remains outside the model.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.openpolicyagent.org/docs/latest/] That pattern becomes governance-ready only when the handoff object is structured enough for deterministic evaluation, because free-form text cannot be reliably joined to policy, approval, or audit controls.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] Human oversight belongs at bounded exception points and irreversible decision points, not as a universal substitute for deterministic controls, because manual review without authority and good routing collapses into nominal oversight.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/] Auditability requires both stochastic and deterministic evidence, because model logs show the proposal path while policy logs show the final governance decision and its governing rule revision.

### §4 Consistency Check

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] No reviewed primary source presents a general-purpose LLM response as a sufficient final governance mechanism for high-stakes action without separate blocking, approval, or override capability.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance] The reviewed vendors differ in native product surface and terminology, but not in the underlying need for a separate enforcement path that can reject or route model output.
- [inference; source: https://www.openpolicyagent.org/docs/latest/; https://www.openpolicyagent.org/docs/latest/management-bundles/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html] The synthesis is therefore consistent in treating external policy engines and enterprise control planes as portable architecture patterns rather than vendor-specific features.

### §5 Depth and Breadth Expansion

- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] **Technical lens:** selective guardrail tagging and parallel policy evaluation show that enterprises can narrow guarded input spans to reduce latency and cost while keeping the deterministic layer in the path.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://www.palantir.com/docs/foundry/aip/ethics-governance] **Regulatory lens:** the minimum compliant design for consequential systems includes anomaly detection, named oversight, override or reverse authority, and a safe-stop path, which pushes governance design beyond mere content moderation.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence] **Behavioral lens:** routing only policy-relevant exceptions to humans is more credible than asking humans to re-review every proposal, because exception-based review better preserves attention for the cases where human judgment actually changes the outcome.
- [inference; source: https://www.openpolicyagent.org/docs/latest/management-bundles/; https://www.palantir.com/docs/foundry/aip/ethics-governance] **Operating-model lens:** versioned policy distribution and structured approval workflows let governance controls evolve on a faster cadence than model retraining or application redeployment, which is essential when policies change more often than product code.

### §6 Synthesis

**Executive summary:**

Enterprises should design hybrid systems so the Large Language Model (LLM) produces structured proposals and explanations, while deterministic guardrails, policy engines, and approval workflows make the final allow, deny, rewrite, or escalate decision before any consequential side effect occurs. [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/]
That boundary should be implemented as a typed contract rather than free-form text, because current vendor control surfaces already compare tool plans, safety signals, and policy inputs against explicit schemas and rule sets. [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.openpolicyagent.org/docs/latest/]
For high-stakes or regulated decisions, the deterministic layer must also preserve auditable policy versions, trace identifiers, and human override or safe-stop capability, because model traces alone do not prove that governance controls actually operated. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]
The remaining design choice is how much of the guardrail, approval, and audit stack can stay vendor-native and how much should be centralized in a shared enterprise control plane. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.palantir.com/docs/foundry/aip/ethics-governance; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

**Key findings:**

1. **A governed hybrid architecture should treat the LLM as an interpretation and proposal subsystem, while a deterministic layer makes the final allow, deny, or escalate decision before any side effect is executed.** ([inference]; high confidence; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/)
2. **The interface between the probabilistic layer and the deterministic layer should be a schema-constrained proposal record with explicit action fields, because policy engines and tool-execution runtimes need normalized input instead of free-form narrative text.** ([inference]; high confidence; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.openpolicyagent.org/docs/latest/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence)
3. **Enterprises should usually run deterministic controls both before model inference and after model generation, because current guardrail products can discard unsafe prompts early and still override or mask unsafe responses after inference.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
4. **Action-capable agents need a second deterministic gate that checks the planned tool invocation against user intent and policy, because an apparently valid model response can still propose the wrong operational action.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
5. **For consequential or regulated use cases, the architecture should include explicit human override, reverse, and safe-stop capability at the final governance layer rather than relying on post hoc review of model output.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
6. **Auditability requires joining model-execution traces with deterministic decision logs and workflow approvals, because enterprises need evidence of both what the model proposed and which rule set or reviewer controlled the final outcome.** ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://www.palantir.com/docs/foundry/aip/ethics-governance)
7. **Governance logic should be versioned and distributed independently from application code or prompt templates, because policy changes, approval rules, and enforcement thresholds usually need a faster operational cadence than model or application releases.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/latest/management-bundles/; https://www.palantir.com/docs/foundry/aip/ethics-governance; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
8. **Failure handling in the hybrid boundary should default to deny, retry with tighter constraints, or human escalation when structured output is invalid, intent is ambiguous, or policy evaluation is indeterminate, because those are the moments when stochastic output is least trustworthy as a control signal.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The LLM should propose while a deterministic layer decides and executes. | https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://www.openpolicyagent.org/docs/latest/ | high | planner-executor split |
| [inference] The architecture boundary should be a schema-constrained proposal record. | https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://www.openpolicyagent.org/docs/latest/ ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence | high | typed contract |
| [inference] Deterministic controls should usually run before and after inference. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html | medium | pre and post filters |
| [inference] Tool-using agents need a second deterministic gate for action alignment. | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | high | tool-plan validation |
| [inference] Consequential systems should include explicit human override, reverse, and safe-stop capability. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 ; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | medium | stop and override |
| [inference] Auditability requires joined model traces, policy logs, and approval evidence. | https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html ; https://www.openpolicyagent.org/docs/latest/management-decision-logs/ ; https://www.palantir.com/docs/foundry/aip/ethics-governance | high | dual evidence streams |
| [inference] Governance logic should be versioned independently from prompts and application code. | https://www.openpolicyagent.org/docs/latest/management-bundles/ ; https://www.palantir.com/docs/foundry/aip/ethics-governance ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | medium | faster policy cadence |
| [inference] Invalid structure, ambiguous intent, or indeterminate policy should route to deny, retry, or escalation. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence ; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 | medium | fail-closed boundary |

**Assumptions:**

- [assumption; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.openpolicyagent.org/docs/latest/] Enterprises can require structured proposal objects before any action-capable tool call is executed. **Justification:** the reviewed tool-use and policy-engine patterns both assume a machine-readable request boundary that can be validated by the calling application.
- [assumption; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Even when a use case is not legally classified as an EU high-risk system, consequential internal decisions still benefit from Article 14-style override and monitoring controls. **Justification:** the regulatory and framework evidence supports using those controls as a governance design baseline for material enterprise decisions.

**Analysis:**

The weight of evidence favored sources that described runtime control behavior directly, because those sources reveal where the governance boundary actually sits in production systems. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.openpolicyagent.org/docs/latest/]
That weighting makes the strongest conclusion architectural rather than model-theoretic: the reviewed products and papers consistently assume that planning and interpretation can be stochastic while execution, approval, and policy enforcement remain outside the model. [inference; source: https://arxiv.org/abs/2210.03629; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance]
Plausible rivals, such as relying mainly on better model quality or adding more human reviewers, were not as persuasive because the reviewed control sources still add explicit blocking, intent checking, approval, or override steps even when the model is capable. [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html]
The practical trade-off is the boundary between vendor-native filtering and approval features and an external policy core with a joined evidence plane. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/management-bundles/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

**Risks, gaps, uncertainties:**

- [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance] Public vendor documentation exposes available control surfaces at a capability level, but it rarely publishes benchmark-quality false positive and false negative rates for prompt protection, task-adherence checks, or approval checkpoints.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] As a result, enterprises still need local threshold tuning and red-team testing, especially when narrowing evaluated spans for latency or cost reasons.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Audit completeness can vary by runtime path, because Bedrock documents that some Responses API calls are not captured by current invocation logging.

**Open questions:**

- Which proposal schema fields are sufficient across multiple enterprise domains without becoming so generic that policy decisions lose precision?
- When should an enterprise use vendor-native task-alignment checks alone, and when should it require a separate policy-decision point for every tool invocation?
- What is the minimum joined telemetry set that supports incident reconstruction across multi-vendor agent workflows without logging excessive sensitive content?

### §7 Recursive Review

- Coverage: complete
- Prior-work scan: repeated against adjacent completed governance items
- Claim labels in Research Skill Output: complete
- Inline citations in Findings: complete
- Acronym expansion audit: complete
- Confidence: medium

---

## Findings

### Executive Summary

Enterprises should design hybrid systems so the Large Language Model (LLM) produces structured proposals and explanations, while deterministic guardrails, policy engines, and approval workflows make the final allow, deny, rewrite, or escalate decision before any consequential side effect occurs. [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/]
That boundary should be implemented as a typed contract rather than free-form text, because current vendor control surfaces already compare tool plans, safety signals, and policy inputs against explicit schemas and rule sets. [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.openpolicyagent.org/docs/latest/]
For high-stakes or regulated decisions, the deterministic layer must also preserve auditable policy versions, trace identifiers, and human override or safe-stop capability, because model traces alone do not prove that governance controls actually operated. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]
The remaining design choice is how much of the guardrail, approval, and audit stack can stay vendor-native and how much should be centralized in a shared enterprise control plane. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.palantir.com/docs/foundry/aip/ethics-governance; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

### Key Findings

1. **A governed hybrid architecture should treat the LLM as an interpretation and proposal subsystem, while a deterministic layer makes the final allow, deny, or escalate decision before any side effect is executed.** ([inference]; high confidence; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/)
2. **The interface between the probabilistic layer and the deterministic layer should be a schema-constrained proposal record with explicit action fields, because policy engines and tool-execution runtimes need normalized input instead of free-form narrative text.** ([inference]; high confidence; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.openpolicyagent.org/docs/latest/; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence)
3. **Enterprises should usually run deterministic controls both before model inference and after model generation, because current guardrail products can discard unsafe prompts early and still override or mask unsafe responses after inference.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
4. **Action-capable agents need a second deterministic gate that checks the planned tool invocation against user intent and policy, because an apparently valid model response can still propose the wrong operational action.** ([inference]; high confidence; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
5. **For consequential or regulated use cases, the architecture should include explicit human override, reverse, and safe-stop capability at the final governance layer rather than relying on post hoc review of model output.** ([inference]; medium confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
6. **Auditability requires joining model-execution traces with deterministic decision logs and workflow approvals, because enterprises need evidence of both what the model proposed and which rule set or reviewer controlled the final outcome.** ([inference]; high confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html; https://www.openpolicyagent.org/docs/latest/management-decision-logs/; https://www.palantir.com/docs/foundry/aip/ethics-governance)
7. **Governance logic should be versioned and distributed independently from application code or prompt templates, because policy changes, approval rules, and enforcement thresholds usually need a faster operational cadence than model or application releases.** ([inference]; medium confidence; source: https://www.openpolicyagent.org/docs/latest/management-bundles/; https://www.palantir.com/docs/foundry/aip/ethics-governance; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html)
8. **Failure handling in the hybrid boundary should default to deny, retry with tighter constraints, or human escalation when structured output is invalid, intent is ambiguous, or policy evaluation is indeterminate, because those are the moments when stochastic output is least trustworthy as a control signal.** ([inference]; medium confidence; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The LLM should propose while a deterministic layer decides and executes. | https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://www.openpolicyagent.org/docs/latest/ | high | planner-executor split |
| [inference] The architecture boundary should be a schema-constrained proposal record. | https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview ; https://www.openpolicyagent.org/docs/latest/ ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence | high | typed contract |
| [inference] Deterministic controls should usually run before and after inference. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html | medium | pre and post filters |
| [inference] Tool-using agents need a second deterministic gate for action alignment. | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence ; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview | high | tool-plan validation |
| [inference] Consequential systems should include explicit human override, reverse, and safe-stop capability. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 ; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html | medium | stop and override |
| [inference] Auditability requires joined model traces, policy logs, and approval evidence. | https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html ; https://www.openpolicyagent.org/docs/latest/management-decision-logs/ ; https://www.palantir.com/docs/foundry/aip/ethics-governance | high | dual evidence streams |
| [inference] Governance logic should be versioned independently from prompts and application code. | https://www.openpolicyagent.org/docs/latest/management-bundles/ ; https://www.palantir.com/docs/foundry/aip/ethics-governance ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html | medium | faster policy cadence |
| [inference] Invalid structure, ambiguous intent, or indeterminate policy should route to deny, retry, or escalation. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html ; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence ; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14 | medium | fail-closed boundary |

### Assumptions

- [assumption; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.openpolicyagent.org/docs/latest/] Enterprises can require structured proposal objects before any action-capable tool call is executed. **Justification:** the reviewed tool-use and policy-engine patterns both assume a machine-readable request boundary that can be validated by the calling application.
- [assumption; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Even when a use case is not legally classified as an EU high-risk system, consequential internal decisions still benefit from Article 14-style override and monitoring controls. **Justification:** the regulatory and framework evidence supports using those controls as a governance design baseline for material enterprise decisions.

### Analysis

The weight of evidence favored sources that described runtime control behavior directly, because those sources reveal where the governance boundary actually sits in production systems. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://www.openpolicyagent.org/docs/latest/]
That weighting makes the strongest conclusion architectural rather than model-theoretic: the reviewed products and papers consistently assume that planning and interpretation can be stochastic while execution, approval, and policy enforcement remain outside the model. [inference; source: https://arxiv.org/abs/2210.03629; https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance]
Plausible rivals, such as relying mainly on better model quality or adding more human reviewers, were not as persuasive because the reviewed control sources still add explicit blocking, intent checking, approval, or override steps even when the model is capable. [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/task-adherence; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html]
The practical trade-off is the boundary between vendor-native filtering and approval features and an external policy core with a joined evidence plane. [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/management-bundles/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-agent-control-plane-architecture-enterprise.html]

### Risks, Gaps, and Uncertainties

- [inference; source: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview; https://www.palantir.com/docs/foundry/aip/ethics-governance] Public vendor documentation exposes available control surfaces at a capability level, but it rarely publishes benchmark-quality false positive and false negative rates for prompt protection, task-adherence checks, or approval checkpoints.
- [inference; source: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html] As a result, enterprises still need local threshold tuning and red-team testing, especially when narrowing evaluated spans for latency or cost reasons.
- [fact; source: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html] Audit completeness can vary by runtime path, because Bedrock documents that some Responses API calls are not captured by current invocation logging.

### Open Questions

- Which proposal schema fields are sufficient across multiple enterprise domains without becoming so generic that policy decisions lose precision?
- When should an enterprise use vendor-native task-alignment checks alone, and when should it require a separate policy-decision point for every tool invocation?
- What is the minimum joined telemetry set that supports incident reconstruction across multi-vendor agent workflows without logging excessive sensitive content?

---

## Output

- Type: knowledge
- Description: This item produces a reference architecture pattern for letting Large Language Models (LLMs) interpret and propose while deterministic guardrails, policy engines, and approval paths enforce the final governance decision. [inference; source: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview; https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html; https://www.openpolicyagent.org/docs/latest/]
- Links:
  - https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html
  - https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
  - https://www.openpolicyagent.org/docs/latest/
