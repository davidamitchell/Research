---
review_count: 1
title: "Agent Operational Cost vs Gap Closure Cost"
added: 2026-05-16T05:29:47+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, organisation, evaluation]
started: 2026-05-16T06:27:49+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-05-13-agent-process-reliability-architecture
  - 2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance
  - 2026-02-28-ai-strategy-swe-focus
related:
  - 2026-03-10-agent-evaluation-cross-repo-analysis
  - 2026-03-12-ai-team-size-strike-team-thesis
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Agent Operational Cost vs Gap Closure Cost

## Research Question

What is the fully loaded operational cost of a production Artificial Intelligence (AI) agent used as a workaround for a missing system capability, relative to the cost of closing the underlying systems capability gap through software delivery across three-year and five-year horizons, and under what conditions does recurring agent operation produce positive return relative to closing the gap in software?

## Scope

**In scope:**
- Cost model components for production agent workarounds: build, inference, harness operations, governance, and failure recovery.
- Cost model components for software-gap closure across missing integration capability, missing application functionality, and missing governed data access.
- Breakeven analysis using plausible AI-assisted software engineering productivity multipliers over three-year and five-year horizons.

**Out of scope:**
- Vendor selection for a specific model provider or orchestration platform.
- Organisation-specific budgeting recommendations without comparable benchmark data.

**Constraints:**
- Prioritise empirical cost datasets and benchmark studies over anecdotal case studies.
- Keep assumptions explicit when source data is incomplete.

## Context

Recurring agent-workaround operation only outperforms system change when the underlying capability gap is too expensive, too uncertain, or too unstable to close within the planning horizon. [inference; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md]

Prior repository work shows that stable, repeatable side effects become more reliable when they move from probabilistic agent behavior into deterministic system capability, which makes long-horizon cost comparison the relevant decision test. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md]

## Approach

1. Compile production cost evidence for agent workarounds by complexity and task type, including inference, governance, and recovery overhead.
2. Compile delivery-cost evidence for closing underlying systems capability gaps with AI-assisted software engineering.
3. Model breakeven points and sensitivity to productivity multipliers for missing integration capability, missing application functionality, and missing governed data access.

## Sources

- [x] [DevOps Research and Assessment (DORA) (2024) Accelerate State of DevOps Report](https://dora.dev/research/2024/dora-report/)
- [x] [DORA (2024) Artificial Intelligence preview](https://dora.dev/research/2024/ai-preview/)
- [x] [Google Cloud (2025) Impact of Generative Artificial Intelligence in Software Development](https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development)
- [x] [Google Cloud (2026) Return on investment of AI-assisted Software Development](https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development)
- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1)
- [x] [National Institute of Standards and Technology (NIST) (2024) Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [x] [Microsoft Research (2025) The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/)
- [x] [Peng et al. (2023) The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590)
- [x] [Anthropic (2026) Claude pricing](https://www.anthropic.com/pricing#api)
- [x] [Google Cloud (2026) Agent Platform generative AI pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
- [x] [GitHub Docs (2026) Kick off a task with Copilot agents on GitHub](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task)
- [x] [GitHub Docs (2026) Using GitHub Copilot code review on GitHub](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review)
- [x] [U.S. Bureau of Labor Statistics (2023) Software developers occupational wages](https://www.bls.gov/oes/2023/may/oes151252.htm)
- [x] [U.S. Bureau of Labor Statistics (2024) Employer costs for employee compensation table 1](https://www.bls.gov/news.release/ecec.t01.htm)
- [x] [Mitchell (2026) Architectural patterns for reliable organizational process identification, selection, and execution in Artificial Intelligence agent systems](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md)
- [x] [Mitchell (2026) Hybrid Architecture Design: Probabilistic Large Language Models for Interpretation, Deterministic Layers for Governance Enforcement](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md)
- [x] [Mitchell (2026) Artificial Intelligence strategy examples: software engineering focus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md)
- [ ] [McKinsey (2024) The state of Artificial Intelligence in early 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-early-2024)
- [ ] [Gartner (n.d.) Forecasts and research on generative Artificial Intelligence](https://www.gartner.com/en/topics/generative-ai)

---

## Research Skill Output

### §0 Initialise

- Question: compare the fully loaded cost of operating a production agent workaround against the cost of removing the same capability gap through software delivery over three-year and five-year horizons.
- Scope: compare recurring agent operation against software delivery that closes the missing integration capability, missing application functionality, or missing governed data-access capability in the underlying stack.
- Constraints: empirical benchmarks preferred, assumptions explicit, output is a full structured synthesis with evidence map and breakeven model.
- Output: knowledge, specifically a decision model for when to keep the agent and when to build out the missing system capability.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md
- Direct cross-reference selected for citation: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md

### §1 Question Decomposition

```text
What is the cost of operating a recurring agent workaround versus closing the gap in software?
|
|-- Q1. What costs are unavoidable for a production agent workaround?
|   |-- Q1a. What do model tokens, runtime, and search actually cost?
|   |-- Q1b. What governance, review, and risk-management work remains human?
|   `-- Q1c. What failure-recovery or retry burden remains after deployment?
|
|-- Q2. What delivery-cost assumptions are defensible for software-gap closure?
|   |-- Q2a. What is a reasonable loaded software-delivery labor cost anchor?
|   |-- Q2b. What productivity multiplier range is supported by current evidence?
|   `-- Q2c. What ongoing maintenance cost remains after the gap is closed?
|
|-- Q3. How do common capability-gap classes differ?
|   |-- Q3a. What is a representative missing-integration closure effort?
|   |-- Q3b. What is a representative missing-functionality closure effort?
|   `-- Q3c. What is a representative missing-governed-data-access closure effort?
|
`-- Q4. Under what conditions does recurring agent operation produce positive return?
    |-- Q4a. What are the three-year breakeven thresholds?
    |-- Q4b. What are the five-year breakeven thresholds?
    `-- Q4c. Which contextual factors favor recurring agent operation as a bridge rather than an end state?
```

### §2 Investigation

#### Prior completed-item cross-reference

- [fact] The completed process-reliability item concludes that stable side effects should be routed through explicit workflows, typed state, and governed escalation points rather than left to free-form agent behavior. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md. Source class: prior completed research.
- [fact] The completed hybrid-governance item concludes that Large Language Models (LLMs) are strongest as interpretation and proposal layers, while deterministic controls remain the authoritative allow, deny, or escalate boundary. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md. Source class: prior completed research.
- [fact] The completed software-engineering strategy item finds that enterprise deployments of coding agents still converge on human review gates and that benchmark gains overstate production autonomy. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md. Source class: prior completed research.
- [inference] Prior completed items therefore point in the same economic direction: if the task is stable enough to encode into deterministic software, the long-run case for permanently paying an agent to work around the gap is weak. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md. Source class: inference from prior completed research.

#### Q1a - Direct model, runtime, and search costs

- [fact] Anthropic's 2026 pricing page lists Sonnet 4.6 at $3 per million input tokens and $15 per million output tokens, managed agents at $0.08 per session-hour, and web search at $10 per 1,000 searches. Source: https://www.anthropic.com/pricing#api. Source class: primary.
- [fact] Google Cloud's Agent Platform pricing page lists Gemini 2.5 Pro at $1.25 per million input tokens and $10 per million output tokens, with Gemini 2.5 Flash substantially cheaper again. Source: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing. Source class: primary.
- [assumption] A representative medium-volume production agent handles 52,000 tasks per year, consumes about 15,000 input tokens and 5,000 output tokens per task, and averages five active runtime minutes per task. This assumption is used to compare cost structure rather than forecast a specific product. Justification: the question asks for horizon economics, and the pricing pages above are linear in token volume, so a moderate recurring workload is enough to test whether inference is first-order or second-order in the total cost stack. Source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing.
- [inference] Under that workload, annual model spend is about $6,240 on Anthropic Sonnet 4.6 and about $3,575 on Gemini 2.5 Pro, while managed-agent runtime adds about $347 and one web search per five tasks adds about $104 on Anthropic's published prices. Source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing. Source class: inference from primary pricing with explicit workload assumption.
- [inference] Token, runtime, and search charges are therefore usually a second-order cost component for a medium-volume production agent, because they remain in the low-thousands of dollars per year while labor and governance obligations remain in the tens or hundreds of thousands. Source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://doi.org/10.6028/NIST.AI.100-1. Source class: inference from primary pricing plus governance requirements.

#### Q1b - Governance, review, and oversight burden

- [fact] NIST Artificial Intelligence Risk Management Framework (AI RMF) 1.0 defines four operating functions, Govern, Map, Measure, and Manage, and treats governance as the cross-cutting activity that establishes policies, roles, monitoring, and accountability across the life cycle. Source: https://doi.org/10.6028/NIST.AI.100-1. Source class: primary.
- [fact] NIST's 2024 Generative Artificial Intelligence Profile extends the same framework to Generative Artificial Intelligence (GenAI) systems and emphasizes ongoing monitoring, documentation, and risk response for deployment, not just one-time design checks. Source: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf. Source class: primary.
- [fact] DORA's 2024 Artificial Intelligence preview reports that only 24% of respondents trust AI-generated code "a lot" or "a great deal." Source: https://dora.dev/research/2024/ai-preview/. Source class: primary.
- [fact] GitHub's agent workflow always creates a pull request when an issue is assigned to Copilot, and prompt-based tasks default to a branch so a person can review and iterate before opening a pull request. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task. Source class: primary.
- [fact] GitHub Copilot code review only leaves comment reviews and does not count toward required approvals or block merging, so formal approval remains human. Source: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review. Source class: primary.
- [inference] Production agent workarounds therefore do not eliminate human labor for control, because low trust, mandatory review surfaces, and explicit governance functions keep a recurring human oversight cost in the operating model even when the agent is technically autonomous between checkpoints. Source: https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review; https://doi.org/10.6028/NIST.AI.100-1. Source class: inference from primary sources.

#### Q1c - Failure recovery and reliability burden

- [fact] The 2024 DORA report says Artificial Intelligence increases individual productivity, flow, and job satisfaction, but negatively impacts software delivery stability and throughput. Source: https://dora.dev/research/2024/dora-report/. Source class: primary.
- [fact] Google Cloud's DORA report on the impact of Generative Artificial Intelligence in software development says a 25% increase in AI adoption is associated with a 2.1% increase in individual productivity and improved document quality, code quality, code review speed, and approval speed. Source: https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development. Source class: primary.
- [fact] The DORA preview and report together show the "productivity paradox": individual gains arrive before organizational reliability gains, and adoption can create a temporary performance dip that must be managed deliberately. Source: https://dora.dev/research/2024/ai-preview/; https://dora.dev/research/2024/dora-report/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development. Source class: primary.
- [inference] For recurring agent workarounds, this means failure recovery is not an exceptional edge case but a regular budget line, because retries, review, and recovery work remain necessary while the agent continues to operate on top of brittle or incomplete systems. Source: https://dora.dev/research/2024/dora-report/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md. Source class: inference from primary and prior completed sources.

#### Q2a - Loaded labor cost anchor for software-gap-closure delivery

- [fact] The U.S. Bureau of Labor Statistics reports a mean annual wage of $138,110 for software developers in 2023. Source: https://www.bls.gov/oes/2023/may/oes151252.htm. Source class: primary.
- [fact] The U.S. Bureau of Labor Statistics Employer Costs for Employee Compensation release reports that benefits account for roughly 30% to 35% of total compensation for professional workers, which is the appropriate direction for a loaded labor-cost estimate rather than wage alone. Source: https://www.bls.gov/news.release/ecec.t01.htm. Source class: primary.
- [inference] A defensible loaded labor-cost anchor for generalized software delivery is therefore about $203,000 per engineer-year, which implies about $16,908 per loaded engineer-month. Source: https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm. Source class: inference from primary labor data.

#### Q2b - Productivity multiplier range for AI-assisted software delivery

- [fact] Microsoft's 2025 field-experiment paper across Microsoft, Accenture, and a Fortune 100 company reports a 26.08% increase in completed tasks among developers using an Artificial Intelligence coding assistant. Source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/. Source class: primary.
- [fact] Peng et al. report that developers in a controlled GitHub Copilot experiment completed an HTTP server task 55.8% faster than the control group. Source: https://arxiv.org/abs/2302.06590. Source class: primary.
- [fact] DORA's 2024 work reports that a 25% increase in Artificial Intelligence adoption is associated with a 2.1% increase in individual productivity, but not with the same magnitude of team-level delivery improvement. Source: https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development; https://dora.dev/research/2024/dora-report/. Source class: primary.
- [inference] A reasonable multiplier band for planning is therefore about 1.02x as a conservative organizational case, 1.26x as a central field-evidence case, and 1.56x as an optimistic bounded-task case. Source: https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590. Source class: inference from primary productivity studies.

#### Q2c - Maintenance after software-gap closure

- [fact] DORA's ROI report says leaders should budget for an initial productivity dip, reinvest reclaimed capacity, and connect engineering improvements to sustainable financial outcomes instead of assuming one-time deployment instantly translates into durable value. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development. Source class: primary.
- [assumption] A 10% annual maintenance rate on the initial build cost is a reasonable generic planning assumption for a closed capability gap, because the delivered integration, function, or data-access layer still requires upkeep but no longer needs the full recurring operational workaround. Justification: the question asks for breakeven planning horizons, and DORA's ROI framing is about sustained but reduced post-rollout investment rather than zero maintenance. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development.

#### Q3 - Archetype capability-gap classes and total-cost model

- [assumption] A missing integration capability is modeled as six delivery-months, missing application functionality as nine delivery-months, and missing governed data-access capability as twelve delivery-months. These are archetypes, not vendor quotes, and they represent increasing complexity from interface closure to business-logic closure to governed data-surface closure. Justification: the research question explicitly asks for capability-gap comparison rather than a single undifferentiated project estimate. Source: https://doi.org/10.6028/NIST.AI.100-1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md.
- [assumption] A standard production agent workaround carries 0.50 full-time equivalent recurring labor, split across operator review, agent operations, and governance administration, plus about $10,000 per year in model and platform spend. A lean case uses 0.35 full-time equivalent and about $5,000 platform spend; a strict case uses 1.00 full-time equivalent and about $15,000 platform spend. Justification: NIST governance functions, low trust in generated code, and mandatory human review surfaces imply recurring labor even when token costs remain small. Source: https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review; https://www.anthropic.com/pricing#api.
- [inference] Using the central 1.26x delivery multiplier, the initial build cost is about $80,545 for a missing integration capability, $120,818 for missing application functionality, and $161,091 for missing governed data-access capability. Source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm. Source class: inference from primary evidence plus explicit effort assumptions.
- [inference] With 10% annual maintenance, the three-year total build cost is about $96,654 for a missing integration capability, $144,981 for missing application functionality, and $193,309 for missing governed data-access capability; the five-year totals are about $112,763, $169,145, and $225,527 respectively. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm. Source class: inference from primary evidence plus explicit maintenance assumption.
- [inference] The standard recurring agent workaround costs about $112,000 per year, or about $336,000 over three years and $560,000 over five years; the lean case is about $76,000 per year, and the strict case is about $218,000 per year. Source: https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/ai-preview/; https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing. Source class: inference from primary sources plus explicit staffing assumption.

#### Q4 - Breakeven thresholds and decision conditions

- [inference] Under the central 1.26x delivery multiplier and standard recurring agent-workaround assumption, software-gap closure breaks even against recurring agent operation at about 20.9 delivery-months over three years and about 29.8 delivery-months over five years. Source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development. Source class: inference from primary sources plus explicit model assumptions.
- [inference] In the lean recurring agent-workaround case the breakeven threshold falls to about 14.2 delivery-months over three years and 20.2 over five years, while in the strict oversight case it rises to about 40.6 and 58.0 delivery-months respectively. Source: https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/ai-preview/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development. Source class: inference from primary sources plus explicit model assumptions.
- [inference] Recurring agent operation produces positive return mainly when the gap is genuinely temporary, demand is uncertain, requirements are changing faster than delivery can stabilize them, or the underlying closure effort exceeds roughly two years of AI-assisted delivery. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md. Source class: inference from primary and prior completed sources.
- [inference] When the work is stable, high-frequency, and safety- or compliance-relevant, the economics and the control model both shift toward software-gap closure because recurring review and recovery costs dominate token costs. Source: https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md. Source class: inference from primary and prior completed sources.

### §3 Reasoning

- [fact] Primary evidence supports three strong anchors: token prices are low and transparent, governance obligations are real and recurring, and software-delivery productivity gains are meaningful but bounded. Source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://doi.org/10.6028/NIST.AI.100-1; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590.
- [inference] The decisive comparison is recurring governed workaround cost versus one-time closure cost plus maintenance, rather than a narrow comparison between token spend and developer salary. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md.
- [inference] Because the operational workaround continues to carry review, governance, and recovery labor every year, recurring agent operation only wins when closure effort is unusually large or the task is not yet stable enough to encode safely. Source: https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md.

### §4 Consistency Check

- [inference] The GitHub Copilot experiment reports 55.8% faster completion on one bounded task, while Microsoft's field experiments report a 26.08% increase across real organizations, so it is reasonable to treat the larger figure as a bounded-task ceiling rather than as an organization-wide planning baseline. Source: https://arxiv.org/abs/2302.06590; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/.
- [inference] DORA's productivity and stability findings support the software-gap-closure thesis because the report ties local productivity gains to broader process, documentation, and control-system changes rather than to automation alone. Source: https://dora.dev/research/2024/dora-report/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development.
- [inference] The cost model remains internally consistent because the same labor anchor and productivity multipliers are used across all three debt classes and across both three-year and five-year horizons. Source: https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/.

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the more a workflow can be converted from probabilistic interpretation into deterministic execution, the more it behaves like software-gap closure capital formation rather than recurring operational expense. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md.
- [inference] Economic lens: token-price competition matters at the margin, but the first-order cost variable is labor needed to review, govern, and recover the workflow. Source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://doi.org/10.6028/NIST.AI.100-1.
- [inference] Regulatory lens: the stricter the control environment, the more the recurring-agent breakeven threshold moves rightward because required human review and evidence capture increase recurring operating cost. Source: https://doi.org/10.6028/NIST.AI.100-1; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf.
- [inference] Behavioural lens: low trust in generated code and explicit pull-request review patterns mean most organizations will not accept an unattended agent workaround for consequential change, which limits the practical ceiling on labor savings. Source: https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review.
- [inference] Historical lens: DORA's return-on-investment framing favors temporary tuition costs that convert into durable workflow gains, not indefinite operational dependence on a workaround layer. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/.

### §6 Synthesis

#### Executive Summary

Closing the capability gap in software usually beats recurring agent operation over three-year and five-year horizons when the underlying missing capability can be built in roughly 14 to 21 delivery-months in a lean-to-standard operating model, and in roughly 20 to 30 delivery-months over five years. [inference; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]

Recurring human review, governance, and recovery labor dominate production agent-workaround cost, while published model prices remain comparatively low and risk-management duties remain persistent. [inference; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://dora.dev/research/2024/ai-preview/; https://doi.org/10.6028/NIST.AI.100-1]

Recurring agent operation earns positive return mainly as a bridge, when demand is uncertain, the workflow is changing too quickly to encode safely, or the build effort exceeds about two years of AI-assisted delivery. [inference; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md]

Stable, high-frequency, compliance-relevant work should usually migrate out of recurring agent operation and into deterministic system capability because recurring oversight cost compounds while software-gap closure converts the same need into a lower-maintenance asset. [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md]

#### Key Findings

1. **Published frontier-model prices imply that a medium-volume production agent's annual token, runtime, and search spend stays in the low-thousands of dollars, which makes labor rather than inference the dominant operational cost driver.** ([inference]; high confidence; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
2. **NIST governance requirements, low trust in generated code, and GitHub's documented review flow show that production agents retain recurring human oversight, approval, and monitoring cost even when the technical execution path is automated.** ([inference]; high confidence; source: https://doi.org/10.6028/NIST.AI.100-1; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf; https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review)
3. **Current software-engineering productivity evidence supports a planning multiplier band from about 1.02x at the organizational level to about 1.56x on bounded tasks, with about 1.26x as the strongest central estimate for real deployment economics.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590)
4. **Using the central 1.26x multiplier, representative three-year software-gap-closure totals are about $97,000 for a missing integration capability, $145,000 for missing application functionality, and $193,000 for missing governed data access, all materially below the standard $336,000 three-year recurring agent-workaround cost.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development)
5. **Under the modeled staffing range, software-gap closure breaks even against recurring agent workarounds at about 14.2 to 40.6 delivery-months over three years and about 20.2 to 58.0 delivery-months over five years, with the standard case centered at about 20.9 and 29.8 months.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/ai-preview/)
6. **Recurring agent operation keeps a positive return profile mainly when the closure effort is unusually large, the demand pattern is intermittent, or the operating design is explicitly temporary while the organization learns the workflow and validates the target state.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md)
7. **For regulated or safety-relevant workflows, the required review and evidence burden shifts the economics further toward software-gap closure because stricter oversight raises recurring agent-workaround cost faster than it raises post-build maintenance cost.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.AI.100-1; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md)
8. **The strategic role of recurring agent operation is therefore best understood as bridge capital for uncertain or rapidly changing work, not as the default steady-state operating model for stable high-frequency system gaps.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md)

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Medium-volume token and runtime spend remains small relative to labor. | https://www.anthropic.com/pricing#api ; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing | high | Depends on explicit workload assumption, but the order of magnitude is stable across providers. |
| [inference] Oversight and governance remain recurring costs in production. | https://doi.org/10.6028/NIST.AI.100-1 ; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; https://dora.dev/research/2024/ai-preview/ ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review | high | Multiple primary sources agree that review and governance are not optional. |
| [inference] The defensible productivity band is about 1.02x to 1.56x, centered around 1.26x. | https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development ; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://arxiv.org/abs/2302.06590 | medium | Uses organization, field, and bounded-task evidence together. |
| [inference] Three-year software-gap-closure totals for missing integration capability, missing application functionality, and missing governed data access remain below the standard three-year recurring agent-workaround total. | https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development | medium | Relies on explicit archetype effort assumptions. |
| [inference] Breakeven spans about 14.2 to 40.6 delivery-months over three years and about 20.2 to 58.0 over five years across the modeled staffing range, with the standard case at about 20.9 and 29.8 months. | https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://doi.org/10.6028/NIST.AI.100-1 ; https://dora.dev/research/2024/ai-preview/ | medium | Threshold is sensitive to staffing assumption but direction is robust. |
| [inference] Recurring agent operation is strongest as a temporary bridge for uncertain or fast-changing work. | https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://dora.dev/research/2024/dora-report/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md | medium | Supported by DORA's J-curve and prior repository architecture findings. |
| [inference] Stricter control environments move the economics further toward software-gap closure. | https://doi.org/10.6028/NIST.AI.100-1 ; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md | medium | Governance intensity increases recurring agent-workaround labor more than post-build maintenance. |
| [inference] Stable, high-frequency work should migrate from recurring agent operation into deterministic system capability. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development | medium | This is the combined economic and control-boundary conclusion. |

**Identified but not consulted**

- [ ] [McKinsey (2024) The state of Artificial Intelligence in early 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-early-2024)
- [ ] [Gartner (n.d.) Forecasts and research on generative Artificial Intelligence](https://www.gartner.com/en/topics/generative-ai)

#### Assumptions

- [assumption] **Loaded labor anchor:** $203,000 per engineer-year and $16,908 per engineer-month. **Justification:** derived from U.S. Bureau of Labor Statistics wage and compensation-share data, which is sufficient for a benchmark model but not a country-specific budgeting quote. Source: https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm
- [assumption] **Workload anchor:** 52,000 tasks per year, 15,000 input tokens and 5,000 output tokens per task, five active runtime minutes per task. **Justification:** needed to test whether inference or labor dominates the stack, and the published pricing is linear enough that the direction of the result is robust. Source: https://www.anthropic.com/pricing#api ; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing
- [assumption] **Recurring agent-workaround staffing bands:** lean 0.35 full-time equivalent, standard 0.50, strict 1.00, plus modest platform spend. **Justification:** NIST governance functions, DORA trust findings, and GitHub review mechanics imply non-trivial recurring labor. Source: https://doi.org/10.6028/NIST.AI.100-1 ; https://dora.dev/research/2024/ai-preview/ ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
- [assumption] **Capability-gap effort archetypes:** missing integration capability six delivery-months, missing application functionality nine, missing governed data access twelve. **Justification:** the item needs generalized capability-gap classes rather than vendor quotes, and the three classes represent increasing complexity and governance burden. Source: https://doi.org/10.6028/NIST.AI.100-1 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md
- [assumption] **Maintenance rate:** 10% of initial build cost per year after closure. **Justification:** DORA's return-on-investment framing implies continued but reduced upkeep after the capability gap is closed. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development

#### Analysis

This item relies mainly on published pricing schedules, governance frameworks, and software-engineering productivity studies rather than anecdotal case studies. [fact; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://doi.org/10.6028/NIST.AI.100-1; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590]

Token spend remains small in the modeled workload, while recurring human review, governance, and failure-recovery work account for most annual operating cost in the agent-workaround scenarios used here. [inference; source: https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review; https://doi.org/10.6028/NIST.AI.100-1; https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing]

The software-gap-closure side is more assumption-sensitive, so the analysis keeps the logic transparent: loaded labor, productivity multiplier, capability-gap effort, and maintenance rate are all visible, and changing them shifts the breakeven month threshold rather than reversing the direction for common stable gaps. [inference; source: https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]

The main competing interpretation is that model quality will keep rising fast enough to erase oversight cost, but the reviewed DORA and GitHub evidence does not support that today because organizations still route consequential changes through human review and still report reliability trade-offs from adoption. [inference; source: https://dora.dev/research/2024/dora-report/; https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review]

The second competing interpretation is to keep recurring agent operation indefinitely because it avoids the up-front project, but DORA's return-on-investment framing and prior repository architecture work both indicate that durable value comes from converting repeated workaround effort into a governed capability, not from paying the same workaround tax forever. [inference; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md]

#### Risks, Gaps, and Uncertainties

- [assumption] Cross-country labor rates, contractor mixes, and internal platform chargeback models can move the absolute dollar values materially even when the structural comparison stays directionally similar. Source: https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm
- [assumption] The capability-gap effort assumptions are archetypes rather than observed delivery distributions from one organization, so the exact breakeven threshold should be treated as a planning range instead of a quote. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://doi.org/10.6028/NIST.AI.100-1
- [assumption] The model omits option value from strategic flexibility, such as using recurring agent operation deliberately to learn the workflow before committing to a target-state design, which can make a temporary workaround more attractive than the base model shows. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development
- [assumption] Downstream defect externalities from long-running agent workarounds may change the economics in some domains because this item relies on DORA-level reliability evidence rather than incident-cost datasets. Source: https://dora.dev/research/2024/dora-report/ ; https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development

#### Open Questions

- What is the empirical maintenance ratio for production agent workarounds after twelve months in stable enterprise use, broken down by review, operations, and incident recovery?
- How different are the breakeven thresholds for low-frequency but high-value work compared with high-frequency transactional work?
- What project-history datasets could replace the six-month, nine-month, and twelve-month capability-gap archetypes with observed delivery distributions?
- How much option value does a deliberate recurring-agent pilot create when it is used to discover the right target-state system design rather than as an indefinite workaround?

#### Output

- Type: knowledge
- Description: A decision model showing that recurring governed agent operation is usually more expensive than closing stable system gaps once those gaps can be built in roughly 14 to 21 delivery-months over three years or 20 to 30 delivery-months over five years. [inference; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]
- Links: https://dora.dev/research/2024/dora-report/ ; https://doi.org/10.6028/NIST.AI.100-1 ; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/

### §7 Recursive Review

```text
review_status: self-review completed
acronym_audit: complete
domain_term_audit: rewritten into plain language where no authoritative external definition was used
claim_audit: complete
findings_parity: maintained
remaining_uncertainty: threshold values depend on effort and staffing assumptions
```

---

## Findings

### Executive Summary

Closing the capability gap in software usually beats recurring agent operation over three-year and five-year horizons when the underlying missing capability can be built in roughly 14 to 21 delivery-months in a lean-to-standard operating model, and in roughly 20 to 30 delivery-months over five years. [inference; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]

Recurring human review, governance, and recovery labor dominate production agent-workaround cost, while published model prices remain comparatively low and risk-management duties remain persistent. [inference; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://dora.dev/research/2024/ai-preview/; https://doi.org/10.6028/NIST.AI.100-1]

Recurring agent operation earns positive return mainly as a bridge, when demand is uncertain, the workflow is changing too quickly to encode safely, or the build effort exceeds about two years of AI-assisted delivery. [inference; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md]

Stable, high-frequency, compliance-relevant work should usually migrate out of recurring agent operation and into deterministic system capability because recurring oversight cost compounds while software-gap closure converts the same need into a lower-maintenance asset. [inference; source: https://doi.org/10.6028/NIST.AI.100-1; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md]

### Key Findings

1. **Published frontier-model prices imply that a medium-volume production agent's annual token, runtime, and search spend stays in the low-thousands of dollars, which makes labor rather than inference the dominant operational cost driver.** ([inference]; high confidence; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
2. **NIST governance requirements, low trust in generated code, and GitHub's documented review flow show that production agents retain recurring human oversight, approval, and monitoring cost even when the technical execution path is automated.** ([inference]; high confidence; source: https://doi.org/10.6028/NIST.AI.100-1; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf; https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review)
3. **Current software-engineering productivity evidence supports a planning multiplier band from about 1.02x at the organizational level to about 1.56x on bounded tasks, with about 1.26x as the strongest central estimate for real deployment economics.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590)
4. **Using the central 1.26x multiplier, representative three-year software-gap-closure totals are about $97,000 for a missing integration capability, $145,000 for missing application functionality, and $193,000 for missing governed data access, all materially below the standard $336,000 three-year recurring agent-workaround cost.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development)
5. **Under the modeled staffing range, software-gap closure breaks even against recurring agent workarounds at about 14.2 to 40.6 delivery-months over three years and about 20.2 to 58.0 delivery-months over five years, with the standard case centered at about 20.9 and 29.8 months.** ([inference]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://doi.org/10.6028/NIST.AI.100-1; https://dora.dev/research/2024/ai-preview/)
6. **Recurring agent operation keeps a positive return profile mainly when the closure effort is unusually large, the demand pattern is intermittent, or the operating design is explicitly temporary while the organization learns the workflow and validates the target state.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://dora.dev/research/2024/dora-report/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md)
7. **For regulated or safety-relevant workflows, the required review and evidence burden shifts the economics further toward software-gap closure because stricter oversight raises recurring agent-workaround cost faster than it raises post-build maintenance cost.** ([inference]; medium confidence; source: https://doi.org/10.6028/NIST.AI.100-1; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md)
8. **The strategic role of recurring agent operation is therefore best understood as bridge capital for uncertain or rapidly changing work, not as the default steady-state operating model for stable high-frequency system gaps.** ([inference]; medium confidence; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Medium-volume token and runtime spend remains small relative to labor. | https://www.anthropic.com/pricing#api ; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing | high | Depends on explicit workload assumption, but the order of magnitude is stable across providers. |
| [inference] Oversight and governance remain recurring costs in production. | https://doi.org/10.6028/NIST.AI.100-1 ; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; https://dora.dev/research/2024/ai-preview/ ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review | high | Multiple primary sources agree that review and governance are not optional. |
| [inference] The defensible productivity band is about 1.02x to 1.56x, centered around 1.26x. | https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development ; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://arxiv.org/abs/2302.06590 | medium | Uses organization, field, and bounded-task evidence together. |
| [inference] Three-year software-gap-closure totals for missing integration capability, missing application functionality, and missing governed data access remain below the standard three-year recurring agent-workaround total. | https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development | medium | Relies on explicit archetype effort assumptions. |
| [inference] Breakeven spans about 14.2 to 40.6 delivery-months over three years and about 20.2 to 58.0 over five years across the modeled staffing range, with the standard case at about 20.9 and 29.8 months. | https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/ ; https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://doi.org/10.6028/NIST.AI.100-1 ; https://dora.dev/research/2024/ai-preview/ | medium | Threshold is sensitive to staffing assumption but direction is robust. |
| [inference] Recurring agent operation is strongest as a temporary bridge for uncertain or fast-changing work. | https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://dora.dev/research/2024/dora-report/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md | medium | Supported by DORA's J-curve and prior repository architecture findings. |
| [inference] Stricter control environments move the economics further toward software-gap closure. | https://doi.org/10.6028/NIST.AI.100-1 ; https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md | medium | Governance intensity increases recurring agent-workaround labor more than post-build maintenance. |
| [inference] Stable, high-frequency work should migrate from recurring agent operation into deterministic system capability. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md ; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development | medium | This is the combined economic and control-boundary conclusion. |

**Identified but not consulted**

- [ ] [McKinsey (2024) The state of Artificial Intelligence in early 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-early-2024)
- [ ] [Gartner (n.d.) Forecasts and research on generative Artificial Intelligence](https://www.gartner.com/en/topics/generative-ai)

### Assumptions

- [assumption] **Loaded labor anchor:** $203,000 per engineer-year and $16,908 per engineer-month. **Justification:** derived from U.S. Bureau of Labor Statistics wage and compensation-share data, which is sufficient for a benchmark model but not a country-specific budgeting quote. Source: https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm
- [assumption] **Workload anchor:** 52,000 tasks per year, 15,000 input tokens and 5,000 output tokens per task, five active runtime minutes per task. **Justification:** needed to test whether inference or labor dominates the stack, and the published pricing is linear enough that the direction of the result is robust. Source: https://www.anthropic.com/pricing#api ; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing
- [assumption] **Recurring agent-workaround staffing bands:** lean 0.35 full-time equivalent, standard 0.50, strict 1.00, plus modest platform spend. **Justification:** NIST governance functions, DORA trust findings, and GitHub review mechanics imply non-trivial recurring labor. Source: https://doi.org/10.6028/NIST.AI.100-1 ; https://dora.dev/research/2024/ai-preview/ ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task ; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
- [assumption] **Capability-gap effort archetypes:** missing integration capability six delivery-months, missing application functionality nine, missing governed data access twelve. **Justification:** the item needs generalized capability-gap classes rather than vendor quotes, and the three classes represent increasing complexity and governance burden. Source: https://doi.org/10.6028/NIST.AI.100-1 ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md
- [assumption] **Maintenance rate:** 10% of initial build cost per year after closure. **Justification:** DORA's return-on-investment framing implies continued but reduced upkeep after the capability gap is closed. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development

### Analysis

This item relies mainly on published pricing schedules, governance frameworks, and software-engineering productivity studies rather than anecdotal case studies. [fact; source: https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; https://doi.org/10.6028/NIST.AI.100-1; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://arxiv.org/abs/2302.06590]

Token spend remains small in the modeled workload, while recurring human review, governance, and failure-recovery work account for most annual operating cost in the agent-workaround scenarios used here. [inference; source: https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review; https://doi.org/10.6028/NIST.AI.100-1; https://www.anthropic.com/pricing#api; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing]

The software-gap-closure side is more assumption-sensitive, so the analysis keeps the logic transparent: loaded labor, productivity multiplier, capability-gap effort, and maintenance rate are all visible, and changing them shifts the breakeven month threshold rather than reversing the direction for common stable gaps. [inference; source: https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]

The main competing interpretation is that model quality will keep rising fast enough to erase oversight cost, but the reviewed DORA and GitHub evidence does not support that today because organizations still route consequential changes through human review and still report reliability trade-offs from adoption. [inference; source: https://dora.dev/research/2024/dora-report/; https://dora.dev/research/2024/ai-preview/; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/kick-off-a-task; https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review]

The second competing interpretation is to keep recurring agent operation indefinitely because it avoids the up-front project, but DORA's return-on-investment framing and prior repository architecture work both indicate that durable value comes from converting repeated workaround effort into a governed capability, not from paying the same workaround tax forever. [inference; source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-13-agent-process-reliability-architecture.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md]

### Risks, Gaps, and Uncertainties

- [assumption] Cross-country labor rates, contractor mixes, and internal platform chargeback models can move the absolute dollar values materially even when the structural comparison stays directionally similar. Source: https://www.bls.gov/oes/2023/may/oes151252.htm ; https://www.bls.gov/news.release/ecec.t01.htm
- [assumption] The capability-gap effort assumptions are archetypes rather than observed delivery distributions from one organization, so the exact breakeven threshold should be treated as a planning range instead of a quote. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development ; https://doi.org/10.6028/NIST.AI.100-1
- [assumption] The model omits option value from strategic flexibility, such as using recurring agent operation deliberately to learn the workflow before committing to a target-state design, which can make a temporary workaround more attractive than the base model shows. Source: https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development
- [assumption] Downstream defect externalities from long-running agent workarounds may change the economics in some domains because this item relies on DORA-level reliability evidence rather than incident-cost datasets. Source: https://dora.dev/research/2024/dora-report/ ; https://cloud.google.com/resources/content/dora-impact-of-gen-ai-software-development

### Open Questions

- What is the empirical maintenance ratio for production agent workarounds after twelve months in stable enterprise use, broken down by review, operations, and incident recovery?
- How different are the breakeven thresholds for low-frequency but high-value work compared with high-frequency transactional work?
- What project-history datasets could replace the six-month, nine-month, and twelve-month debt-class archetypes with observed delivery distributions?
- How much option value does a deliberate recurring-agent pilot create when it is used to discover the right target-state system design rather than as an indefinite workaround?

### Output

- Type: knowledge
- Description: A decision model showing that recurring governed agent operation is usually more expensive than closing stable system gaps once those gaps can be built in roughly 14 to 21 delivery-months over three years or 20 to 30 delivery-months over five years. [inference; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]
- Links: https://dora.dev/research/2024/dora-report/ ; https://doi.org/10.6028/NIST.AI.100-1 ; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/

---

## Output

- Type: knowledge
- Description: A decision model showing that recurring governed agent operation is usually more expensive than closing stable system gaps once those gaps can be built in roughly 14 to 21 delivery-months over three years or 20 to 30 delivery-months over five years. [inference; source: https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/; https://www.bls.gov/oes/2023/may/oes151252.htm; https://www.bls.gov/news.release/ecec.t01.htm; https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development]
- Links: https://dora.dev/research/2024/dora-report/ ; https://doi.org/10.6028/NIST.AI.100-1 ; https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/
