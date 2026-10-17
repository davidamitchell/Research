---
title: "Optionality and Control Across AI Model Consumption Stages"
added: 2026-10-17T07:35:56+00:00
status: backlog
priority: medium
blocks: []
themes: [enterprise-adoption, ai-architecture, cost-performance, regulatory-compliance, benchmarks-eval]
started: ~
completed: ~
output: []
cites: [2026-08-13-llm-consumption-maturity-ladder, 2026-03-19-layered-org-llm-architecture]
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Optionality and Control Across AI Model Consumption Stages

## Research Question

When an organisation progresses from Artificial Intelligence (AI) capabilities embedded in vendor subscriptions, through managed model platforms, to self-hosting model weights on infrastructure it controls, how do model choice, per-request selection, and operational and data controls change? Which capabilities become available at each stage, and does model tuning begin on managed platforms or require self-hosting?

## Scope

**In scope:**
- Compare model optionality, per-request selection, control of weights, serving, data paths, and change cadence across subscription, managed-platform, and self-hosted stages; test whether the stages stack or replace one another.
- Identify evaluation, routing, confidence, escalation, and data-classification prerequisites for dynamic model selection.
- Verify platform-native fine-tuning, custom-weight import for serverless serving, and dedicated managed-endpoint paths on Amazon Bedrock, Microsoft Foundry, and Google Vertex AI, including regional availability.
- Compare retrieval, prompting, tuning, and smaller domain-specific models for policy question answering, compliance checking, classification, and extraction.
- Find independent self-hosting cost evidence; model break-even and sensitivity to workload and operating assumptions, including multi-agent orchestration.
- Assess named evidence for regulated organisations' self-hosting decisions, relevant residency and extraterritorial-access laws, exit planning, open-weight licensing and provenance, and model-risk governance.

**Out of scope:**
- Re-deriving the maturity-model mapping and routing survey covered by the cited research.
- Harness and runtime concerns.

**Constraints:** Use primary vendor documentation and pricing, statutes, regulator publications, and peer-reviewed or disclosed-methodology cost studies. Treat the three named managed platforms as representative examples, not an exhaustive survey. Bound legal analysis to the United States, European Union, and United Kingdom, adding another jurisdiction only where direct case evidence warrants it. Report source dates and regional availability explicitly.

## Context

The cited maturity-ladder research found that consumption stages can be mixed and that routing can bridge managed and self-hosted models, but left open independent cost evidence, regulated-organisation case evidence, and whether tuning is actually a self-hosting capability. This research informs where organisations should place stage boundaries and what capabilities, controls, and costs they take on when choosing a model-consumption path.

## Approach

1. Compare optionality, control, and responsibilities across the three stages.
   1a. Which models and vendors can be selected at each stage, and can selection vary per request?
   1b. Which controls over model weights, serving, data paths, and change cadence become available at each stage?
   1c. What team responsibilities and capabilities does each stage require?
   1d. Does evidence show that stages stack, preserving frontier-model access, or that moving stages replaces prior options?
2. Establish prerequisites and constraints for dynamic selection.
   2a. What workload-specific evaluation datasets, human-calibrated model judges, and regression gates are needed before routing can be trusted?
   2b. What evidence supports calibrated confidence and escalation from smaller models to frontier models?
   2c. How should data classification and regional inference restrictions constrain eligible models and routes?
3. Locate where tuning begins on managed platforms.
   3a. Which of the three named platforms offer platform-native fine-tuning, for which models and regions?
   3b. Which support importing externally trained custom weights for serverless serving, and where?
   3c. Which offer dedicated managed endpoints, and what control and operating responsibilities do they leave with the customer?
   3d. Where do these paths sit on the optionality and control axes, and does imported-weight serving count as platform use or self-hosting?
4. Compare tuning with retrieval, prompting, and smaller models.
   4a. For the four specified regulated-industry workloads, what evidence and criteria favor retrieval or prompting over tuning?
   4b. When do domain-specific smaller models outperform frontier models on cost and quality?
5. Estimate self-hosting break-even with independent evidence.
   5a. What independent cost studies and disclosed assumptions exist beyond the study in the cited item?
   5b. What break-even formula captures monthly tokens, input/output ratio, cache hit rate, batch share, graphics processing unit (GPU) hourly cost, throughput per GPU, utilisation, and operations-staff cost?
   5c. How do sensitivity scenarios and multi-agent orchestration alter the estimate?
6. Examine regulatory, licensing, and model-risk drivers.
   6a. Is there named, sourced case evidence that regulated organisations self-host for residency, extraterritorial data-access, or exit-planning reasons rather than cost?
   6b. How do applicable statutes and regulator guidance shape the control required at each stage?
   6c. How do open-weight licence and provenance obligations change across managed and self-hosted use?
   6d. What model-risk management controls apply when models inform consequential decisions?

## Sources

Starting points from prior repository research:

- [How Do Enterprise Artificial Intelligence (AI) Maturity Frameworks Map onto the Large Language Model (LLM) Consumption Ladder?](https://davidamitchell.github.io/Research/research/2026-08-13-llm-consumption-maturity-ladder.html) — prior work on consumption stages, routing, and self-hosting economics.
- [Layered Organisation Large Language Model: Feasibility and Architecture of Organisation-Customised LLMs](https://davidamitchell.github.io/Research/research/2026-03-19-layered-org-llm-architecture.html) — prior work on organisation-customised models and adaptation.
- [Amazon Web Services (AWS) Bedrock capabilities](https://davidamitchell.github.io/Research/research/2026-05-17-aws-bedrock-capabilities.html) — starting point for managed-platform capability evidence.

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
