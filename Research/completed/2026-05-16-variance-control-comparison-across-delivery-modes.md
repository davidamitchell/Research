---
review_count: 2
title: "Variance Control Comparison Across Delivery Modes"
added: 2026-05-16T05:29:48+00:00
status: completed
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, evaluation, workflow]
started: 2026-05-16T09:26:53+00:00
completed: 2026-05-16T09:52:54+00:00
output: []
cites:
  - 2026-04-26-access-control-amplification-agentic-operations
  - 2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal
  - 2026-04-26-deployment-pipeline-citizen-development-governed-gate
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
related:
  - 2026-05-01-sustainable-ai-software-development-synthesis
  - 2026-05-01-terminal-bench-minimal-coding-agent-benchmarks
  - 2026-05-01-self-modifying-agent-architectures
  - 2026-05-13-anthropic-4d-framework-ai-agent-taxonomy
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Variance Control Comparison Across Delivery Modes

## Research Question

What is the empirical failure-rate distribution of Artificial Intelligence (AI)-assisted code that has passed a standard software delivery pipeline compared with AI-agent-executed business processes at comparable task complexity, and what proportion of failures in each mode is detectable before external effects occur?

## Scope

**In scope:**
- Residual defect evidence for code that passes typed, tested, and gated pipelines.
- Incident evidence for production agent process execution, including pre-effect and post-effect detection ratios.
- Formal comparison of structural controls versus behavioural controls and resulting risk implications.

**Out of scope:**
- Internal proprietary incident data unavailable to the research corpus.
- Performance benchmarking of specific coding assistants or agent products.

**Constraints:**
- Use task-complexity-normalised comparisons wherever available.
- Keep regulated financial services as a primary risk interpretation lens.

## Context

Build mode, using AI to produce code artifacts that still pass typed, tested, and reviewed delivery gates, concentrates most controllable variance before release. [inference; source: https://sre.google/sre-book/testing-reliability/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md]

Do mode, using AI agents to execute business-process steps directly, pushes more variance into live decision-making, permissions, and external state changes. [inference; source: https://www.anthropic.com/research/building-effective-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]

## Approach

1. Establish baseline software reliability metrics for gated delivery pipelines and identify how AI-assisted development alters those baselines.
2. Collect production agent incident data with failure-mode and detection-timing breakdowns.
3. Compare structural control efficacy versus behavioural control efficacy and derive implications for regulated operations.

## Sources

- [x] [Google Site Reliability Engineering (SRE) Book: Testing Reliability](https://sre.google/sre-book/testing-reliability/)
- [x] [DevOps Research and Assessment (DORA) (2024) Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)
- [x] [Google Cloud (2024) Announcing the 2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report)
- [x] [Liang et al. (2025) The Security of Large Language Model (LLM)-assisted Programming: An Empirical Study](https://arxiv.org/abs/2310.02059)
- [x] [Anthropic (2024) Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework (AI RMF 1.0)](https://doi.org/10.6028/NIST.AI.100-1)
- [x] [Open Worldwide Application Security Project (OWASP) (2025) Large Language Model (LLM) 08: Excessive Agency](https://genai.owasp.org/llm08-excessive-agency/)
- [x] [Basel Committee on Banking Supervision (2021) Principles for operational resilience](https://www.bis.org/bcbs/publ/d516.htm)
- [x] [Zhou et al. (2024) WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854)
- [x] [Drouin et al. (2024) WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?](https://arxiv.org/abs/2403.07718)
- [x] [arXiv (2024) tau-bench: A benchmark for tool-agent-user interaction in real-world domains](https://arxiv.org/abs/2406.12045)
- [x] [Ruan et al. (2024) ToolEmu: Identifying the Risks of Large Language Model (LLM) Agents with an LLM Emulator](https://arxiv.org/abs/2309.15817)
- [x] [Debenedetti et al. (2024) AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)
- [x] [Kambhampati et al. (2024) Large Language Models (LLMs) Can't Plan, But Can Help Planning in LLM-Modulo Frameworks](https://arxiv.org/abs/2402.01817)
- [x] [European Union (2024) Artificial Intelligence Act Article 9](https://artificialintelligenceact.eu/article/9/)
- [x] [Canadian Broadcasting Corporation (CBC) News (2024) Air Canada ordered to pay over chatbot advice](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)
- [x] [Mitchell (2026) Access control amplification under agentic operations: whether existing frameworks address the worst-case permission inheritance problem](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)
- [x] [Mitchell (2026) Implicit rate-limiting controls removed by agentic Artificial Intelligence (AI): blast radius amplification and the operational risk literature gap](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md)
- [x] [Mitchell (2026) Deployment pipeline as the only enforceable control gate for citizen-developed agents: DevOps literature support, low-code platform hook points, and architectural enforceability](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md)
- [x] [Mitchell (2026) When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md)

---

## Research Skill Output

### §0 Initialise

- Question: compare the observable failure distribution of Artificial Intelligence (AI)-assisted code after a standard gated delivery pipeline with the observable failure distribution of AI-agent-executed business processes, and assess what share of failures in each mode is detectable before external effects occur.
- Scope: gated software-delivery reliability proxies, empirical agent-task reliability proxies, structural versus behavioural controls, and a regulated financial-services risk lens.
- Constraints: use task-complexity-normalised comparisons where public evidence allows, prefer primary or authoritative sources, keep all citations tied to direct web addresses, and state evidence gaps explicitly.
- Output: structured knowledge item with mirrored synthesis and Findings.
- Prior completed items selected for direct citation:
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md

### §1 Question Decomposition

```text
What is the failure-rate distribution of build mode versus do mode, and what proportion of failures is detectable before external effects?
|
|-- A. Build mode: AI-assisted code through a gated delivery pipeline
|   |-- A1. What does the software-delivery literature measure as externally realized failure after release?
|   |-- A2. What evidence exists that testing, review, and staged release catch failures before deployment?
|   |-- A3. What public evidence exists on the defect or security profile of AI-assisted code before and after gates?
|   `-- A4. What is missing from the public evidence for a precise post-pipeline AI-specific distribution?
|
|-- B. Do mode: AI agents executing business processes
|   |-- B1. What do realistic agent benchmarks show about end-to-end task success and failure?
|   |-- B2. What failure modes dominate in tool-using and policy-constrained agents?
|   |-- B3. Which failures are detectable only after an external action, side effect, or downstream reconciliation?
|   `-- B4. What public incident evidence exists outside benchmarks?
|
|-- C. Comparative control structure
|   |-- C1. How do predefined workflows differ from dynamically self-directed agents?
|   |-- C2. What does that difference imply for pre-effect versus post-effect detectability?
|   `-- C3. How should regulated financial-services teams interpret the difference?
|
`-- D. Synthesis
    |-- D1. What answer is supported directly by evidence?
    |-- D2. What remains an inference because public head-to-head data is missing?
    `-- D3. What open questions should become future research?
```

### §2 Investigation

#### Prior completed-item cross-reference

- **[fact]** The completed deployment-pipeline item concludes that release-time gating is the strongest enforceable control point for citizen-developed agents because it is the point where governance checks can be bound to formal promotion rules rather than to voluntary behaviour. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md. Source class: prior completed research.
- **[fact]** The completed access-control-amplification item concludes that agentic operation changes the risk profile of a permission set because automated principals can exercise granted scope continuously and at machine speed. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md. Source class: prior completed research.
- **[fact]** The completed implicit-rate-limiting item concludes that human speed, attention, fatigue, and working hours have historically acted as de facto limiting mechanisms even when frameworks did not name them explicitly. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-implicit-rate-limiting-controls-agentic-ai-removal.md. Source class: prior completed research.
- **[fact]** The completed human-intervention item concludes that meaningful human review requires actual authority, manageable review volume, and real stop or override points rather than nominal human presence. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md. Source class: prior completed research.

#### Build mode, gated software delivery

- **[fact]** The Google Site Reliability Engineering (SRE) testing chapter says testing is the mechanism used to demonstrate reliability equivalence when changes occur, that more test coverage reduces uncertainty, and that a system-level test can identify a bug with zero Mean Time to Repair (MTTR) by blocking the push before it reaches production. Source: https://sre.google/sre-book/testing-reliability/. Source class: primary.
- **[fact]** The DevOps Research and Assessment (DORA) metrics guide defines change fail rate as the ratio of deployments that require immediate intervention after deployment and deployment rework rate as the ratio of unplanned deployments caused by incidents in production. Source: https://dora.dev/guides/dora-metrics-four-keys/. Source class: primary.
- **[fact]** The 2024 DORA report says a 25% increase in AI adoption is associated with a 7.5% increase in documentation quality, a 3.4% increase in code quality, and a 3.1% increase in code review speed, while also being associated with an estimated 1.5% decrease in delivery throughput and a 7.2% reduction in delivery stability. Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://dora.dev/research/2024/dora-report/. Source class: primary.
- **[fact]** Liang et al. analyzed 733 AI-generated code snippets from GitHub projects and found security weaknesses in 29.5% of Python snippets and 24.2% of JavaScript snippets, while reporting that up to 55.5% of those issues could be fixed when static-analysis warnings were fed back into Copilot Chat. Source: https://arxiv.org/abs/2310.02059. Source class: primary.
- **[inference]** The public evidence therefore supports treating post-pipeline build-mode failure as an escaped-defect proxy rather than as a directly measured Artificial Intelligence-specific production-failure distribution, because the public literature measures either before-release code quality or aggregate post-release delivery instability, but not the subset of released changes that are both AI-assisted and fully cleared by delivery gates. Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://dora.dev/guides/dora-metrics-four-keys/; https://arxiv.org/abs/2310.02059. Source class: inference from primary sources.
- **[assumption]** In the absence of a published code-level trace that separates AI-assisted and human-authored changes after release, DORA instability metrics are the least misleading public proxy for failures that survive a standard software-delivery pipeline. Source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/. Justification: DORA explicitly measures interventions required after deployment, which is the closest public measure of escaped failure once tests, review, and staged release have already run.

#### Structural control distinction

- **[fact]** Anthropic distinguishes workflows, where Large Language Models (LLMs) and tools are orchestrated through predefined code paths, from agents, where LLMs dynamically direct their own processes and tool usage, and recommends choosing the simplest solution possible before adding more autonomous-system complexity. Source: https://www.anthropic.com/research/building-effective-agents. Source class: primary.
- **[inference]** Build mode is closer to Anthropic's workflow pattern because control is concentrated in predefined promotion paths and quality gates, while do mode is closer to the agent pattern because the system makes context-dependent tool choices during live execution. Source: https://www.anthropic.com/research/building-effective-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-deployment-pipeline-citizen-development-governed-gate.md. Source class: inference from primary and prior completed sources.

#### Do mode, empirical agent reliability

- **[fact]** WebArena reports that its best Generative Pre-trained Transformer 4 (GPT-4)-based agent achieved an end-to-end task success rate of 14.41%, versus human performance of 78.24%, on diverse long-horizon web tasks designed to emulate tasks humans routinely perform on the internet. Source: https://arxiv.org/abs/2307.13854. Source class: primary.
- **[fact]** WorkArena introduces a benchmark of 33 ServiceNow-based knowledge-work tasks and reports that current agents show promise but still have a considerable gap to full task automation on enterprise software workflows. Source: https://arxiv.org/abs/2403.07718. Source class: primary.
- **[fact]** tau-bench reports that even state-of-the-art function-calling agents succeed on fewer than 50% of tasks, and that pass raised to the eighth power is below 25% in the retail domain, indicating poor consistency across repeated policy-constrained conversations. Source: https://arxiv.org/abs/2406.12045. Source class: primary.
- **[fact]** ToolEmu reports that 68.8% of failures identified by its evaluator would be valid real-world agent failures under human review and that even the safest tested agent exhibits potentially severe failures 23.9% of the time in its benchmark. Source: https://arxiv.org/abs/2309.15817. Source class: primary.
- **[fact]** AgentDojo reports that state-of-the-art LLMs fail at many realistic tasks even in the absence of attacks, across domains including email, e-banking, and travel booking, and that prompt injection, untrusted text that steers the model toward unintended actions, further weakens security properties. Source: https://arxiv.org/abs/2406.13352. Source class: primary.
- **[assumption]** Public web and enterprise-agent benchmarks are the closest available proxy for AI-agent-executed business processes because public production incident datasets do not yet publish a normalised failure distribution by task class, severity, and detection timing. Source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2403.07718; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352. Justification: these benchmarks expose realistic multi-step tasks with tools, policy constraints, and externally visible actions, which are the core characteristics of the do-mode risk surface.

#### Do-mode failure modes and detectability

- **[fact]** OWASP's Large Language Model (LLM) 08 guidance says excessive functionality, excessive permissions, or excessive autonomy can cause damaging actions, and it recommends least privilege, restricting a system to only the minimum permissions needed for the task, alongside granular tools, downstream authorization, human approval for actions, and rate limiting. Source: https://genai.owasp.org/llm08-excessive-agency/. Source class: primary.
- **[fact]** Kambhampati et al. argue that autoregressive LLMs cannot by themselves do planning or self-verification and that reliable planning requires external model-based verifiers in an LLM-Modulo framework. Source: https://arxiv.org/abs/2402.01817. Source class: primary.
- **[fact]** The Canadian Broadcasting Corporation (CBC) News report on the Air Canada tribunal decision says the airline's chatbot gave incorrect bereavement-fare guidance, that the customer bought tickets before the error was discovered, and that the tribunal held Air Canada responsible for the misinformation. Source: https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416. Source class: credible secondary reporting on a legal case.
- **[inference]** These sources imply that many do-mode failures are only fully observable after an external action, a tool side effect, or downstream reconciliation step has occurred, unless a separate approval or verification layer intercepts the action first. Source: https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2402.01817; https://arxiv.org/abs/2309.15817; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416. Source class: inference from primary and credible secondary sources.

#### Regulated-operations lens

- **[fact]** Article 9 of the European Union Artificial Intelligence Act requires a continuous lifecycle risk-management system for high-risk AI systems, including reasonably foreseeable misuse analysis, residual-risk acceptance, mitigation, and testing against prior-defined metrics and probabilistic thresholds. Source: https://artificialintelligenceact.eu/article/9/. Source class: accessible public legal text.
- **[fact]** The Basel Committee's operational-resilience principles define operational resilience as the ability to deliver critical operations through disruption and require ongoing identification of threats and potential failures in people, processes, and systems, regular assessment of controls, testing under severe but plausible scenarios, and incident-management improvement from lessons learned. Source: https://www.bis.org/bcbs/publ/d516.htm; https://www.bis.org/fsi/fsisummaries/op_resilience.htm. Source class: primary.
- **[fact]** The NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0) says organizations designing, developing, deploying, or using AI systems should manage AI risks throughout design, development, use, and evaluation in order to support trustworthy and responsible AI. Source: https://doi.org/10.6028/NIST.AI.100-1. Source class: primary.
- **[inference]** For regulated financial services, build mode can usually remain inside established release-governance and incident-response disciplines, whereas do mode requires runtime authorization, approval, monitoring, and recovery design because the consequential action occurs during live operation rather than at software release time. Source: https://www.bis.org/bcbs/publ/d516.htm; https://artificialintelligenceact.eu/article/9/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md. Source class: inference from primary and prior completed sources.

### §3 Reasoning

- **[inference]** The cleanest public build-mode denominator is not "all AI-generated code" but "changes that escape tests, review, and release controls into production," because those are the failures that users or operators actually experience after a gated pipeline. Source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/testing-reliability/; https://arxiv.org/abs/2310.02059.
- **[inference]** The cleanest public do-mode denominator is not static code quality but end-to-end task execution, because the decisive risk event is often an action taken with tools or permissions in a live environment rather than a defect sitting passively in a code artifact. Source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2309.15817; https://genai.owasp.org/llm08-excessive-agency/.
- **[inference]** The comparison is therefore structurally asymmetrical: build mode concentrates variance before release, while do mode carries more variance into runtime where the system is already interacting with external state. Source: https://www.anthropic.com/research/building-effective-agents; https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/.
- **[inference]** The absence of a published task-complexity-normalised head-to-head dataset lowers confidence, but the directional conclusion still holds because every accessible evidence family points the same way: stronger before-release control in build mode and weaker before-action control in do mode. Source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://artificialintelligenceact.eu/article/9/.

### §4 Consistency Check

- **[fact]** The DORA evidence contains an apparent tension: AI adoption is associated with improved documentation quality, code quality, and code-review speed, but also with lower delivery stability and throughput. Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report.
- **[inference]** This is not an internal contradiction because local assistance quality and system-level release stability are measured at different layers: AI can improve authoring speed or suggestion quality while still increasing escaped-failure risk if batch size, review depth, or test coverage are not tightened. Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://sre.google/sre-book/testing-reliability/.
- **[fact]** Anthropic recommends simpler workflows for predictable tasks and reserving agents for tasks where flexibility and model-driven decision making are truly needed. Source: https://www.anthropic.com/research/building-effective-agents.
- **[inference]** This is consistent with the benchmark evidence because the lowest reliability appears where agents must choose tools, interpret policy, and recover from environmental ambiguity during live execution, not where systems follow predefined code paths. Source: https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352.

### §5 Depth and Breadth Expansion

- **[inference]** Technical lens: build mode mainly needs strong artifact-quality controls, typed interfaces, tests, reviews, and staged release, while do mode additionally needs runtime least privilege, action scoping, reversible operations, and external verification because the risky decision point moves into live execution. Source: https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2402.01817.
- **[inference]** Regulatory lens: build mode fits naturally into existing software-change governance, whereas do mode behaves more like an operational-resilience problem because it can degrade critical operations through people, process, and system interactions after deployment. Source: https://www.bis.org/bcbs/publ/d516.htm; https://artificialintelligenceact.eu/article/9/; https://doi.org/10.6028/NIST.AI.100-1.
- **[inference]** Economic lens: build mode front-loads cost into reviews, tests, and release friction, while do mode shifts more cost into live monitoring, exception handling, incident response, reconciliation, and customer remediation when actions go wrong. Source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://www.bis.org/fsi/fsisummaries/op_resilience.htm; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416.
- **[inference]** Behavioural lens: humans can usually inspect bounded artifacts more meaningfully than they can supervise large volumes of autonomous actions, so do mode is more exposed to passive approval and delayed recognition unless review is reserved for narrow high-impact checkpoints. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md; https://genai.owasp.org/llm08-excessive-agency/; https://artificialintelligenceact.eu/article/9/.

### §6 Synthesis

#### Executive Summary

Public evidence does not currently provide a task-complexity-normalised head-to-head failure distribution, but the strongest available proxy comparison indicates that AI-assisted code that clears a standard gated delivery pipeline is more pre-effect-detectable than AI agents executing business processes directly, and it points toward, rather than directly proves, fewer externally realised failures. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045]

Build mode is buffered by structural controls, tests, review, staged release, and deployment blocking, so many failures are converted into pre-production findings; public AI-specific evidence shows elevated before-release defect and security risk but also shows that static-analysis feedback can remediate a substantial share of those issues before release. [inference; source: https://sre.google/sre-book/testing-reliability/; https://arxiv.org/abs/2310.02059]

Do mode faces much lower baseline end-to-end reliability on realistic multi-step tasks, with WebArena reporting 14.41% GPT-4 success, tau-bench reporting fewer than 50% successful tasks and less than 25% reliability across repeated retail trials, and ToolEmu still finding severe failures 23.9% of the time even for the safest tested agent. [fact; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2309.15817]

For regulated financial services, this means build mode can usually be governed through existing release-management and incident processes, whereas do mode needs runtime least privilege, approval checkpoints, monitoring, rate limits, and kill switches because many failures are only visible after an external action or downstream reconciliation. [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://artificialintelligenceact.eu/article/9/; https://genai.owasp.org/llm08-excessive-agency/]

#### Key Findings

1. **No public source located for this item provides a task-complexity-normalised, post-pipeline, head-to-head production failure distribution that directly compares AI-assisted code changes with AI-agent-executed business-process actions.** ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2310.02059; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045)
2. **Build-mode failure is most visibly measured as post-release intervention after release gates, while Site Reliability Engineering guidance supports the inference that equivalent failures can also be blocked before production by system-level tests.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/testing-reliability/)
3. **Public evidence on AI-assisted coding shows elevated before-release security and defect risk, but it also shows that static-analysis feedback can eliminate a substantial share of those issues before release, which makes build-mode variance materially filterable before external effects occur.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.02059; https://sre.google/sre-book/testing-reliability/)
4. **The 2024 DORA evidence shows local development gains alongside lower delivery stability and throughput, which supports the inference that AI assistance still requires small batches, robust tests, and disciplined review if teams want low escaped-failure rates.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://dora.dev/research/2024/dora-report/)
5. **When compared with gated build-mode proxies, realistic do-mode benchmarks indicate materially lower baseline reliability, because WebArena reports 14.41% GPT-4 success, tau-bench reports fewer than 50% successful tasks and less than 25% reliability across repeated retail trials, and AgentDojo still reports many failures even without attacks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352; https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/testing-reliability/)
6. **Do-mode failures are harder to catch before impact because many of them arise from live tool use, policy misapplication, excessive permissions, prompt injection, or wrong action selection, all of which often become fully visible only after an external step has already been taken.** ([inference]; medium confidence; source: https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2309.15817; https://arxiv.org/abs/2402.01817; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)
7. **The strongest public legal and regulatory material places autonomous process execution inside lifecycle risk-management and operational-resilience disciplines, which supports the inference that teams cannot govern it only as a conventional pre-release software-quality problem.** ([inference]; medium confidence; source: https://artificialintelligenceact.eu/article/9/; https://www.bis.org/bcbs/publ/d516.htm; https://doi.org/10.6028/NIST.AI.100-1)
8. **The best-supported comparative conclusion is therefore that build mode is structurally more controllable than do mode, because the dominant control point in build mode is release gating before deployment while the dominant control point in do mode must remain a runtime control layer around live decisions and actions.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm)

#### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No direct public head-to-head production distribution was found for post-pipeline AI-assisted code versus AI-agent-executed business processes. | https://dora.dev/research/2024/dora-report/ ; https://arxiv.org/abs/2310.02059 ; https://arxiv.org/abs/2307.13854 ; https://arxiv.org/abs/2406.12045 | high | Evidence-gap statement |
| [inference] Build-mode external failure is most visibly measured as post-release intervention, while tests can also block equivalent failures before production. | https://dora.dev/guides/dora-metrics-four-keys/ ; https://sre.google/sre-book/testing-reliability/ | medium | Escaped-failure framing |
| [inference] AI-assisted code risk is materially filterable before release because static-analysis feedback fixes many issues before they become deployed defects. | https://arxiv.org/abs/2310.02059 ; https://sre.google/sre-book/testing-reliability/ | medium | Pre-effect filterability |
| [inference] AI adoption improves local development metrics while reducing delivery stability and throughput at the system level, so disciplined review and testing remain necessary. | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://dora.dev/research/2024/dora-report/ | medium | Local versus system-level distinction |
| [inference] Realistic do-mode benchmarks indicate lower baseline reliability than gated build-mode proxies. | https://arxiv.org/abs/2307.13854 ; https://arxiv.org/abs/2406.12045 ; https://arxiv.org/abs/2406.13352 ; https://dora.dev/guides/dora-metrics-four-keys/ ; https://sre.google/sre-book/testing-reliability/ | medium | Cross-mode proxy comparison |
| [inference] Many do-mode failures are only fully visible after action because live tools, permissions, and external state mediate the harm. | https://genai.owasp.org/llm08-excessive-agency/ ; https://arxiv.org/abs/2309.15817 ; https://arxiv.org/abs/2402.01817 ; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416 | medium | Post-effect detectability |
| [inference] Regulatory and resilience frameworks place autonomous process execution inside lifecycle testing, monitoring, mitigation, and incident-learning disciplines. | https://artificialintelligenceact.eu/article/9/ ; https://www.bis.org/bcbs/publ/d516.htm ; https://doi.org/10.6028/NIST.AI.100-1 | medium | Regulated-operations lens |
| [inference] Build mode is structurally more controllable than do mode because release gates constrain artifacts before impact, while runtime controls must constrain live decisions after deployment. | https://www.anthropic.com/research/building-effective-agents ; https://sre.google/sre-book/testing-reliability/ ; https://genai.owasp.org/llm08-excessive-agency/ ; https://www.bis.org/bcbs/publ/d516.htm | medium | Core synthesis claim |

#### Assumptions

- **Assumption:** DORA instability metrics are the least misleading public proxy for post-pipeline build-mode failure because no accessible public dataset separates AI-assisted and human-authored changes after release. **Justification:** DORA explicitly measures interventions required after deployment, which matches the escaped-failure concept once tests and review have already run. [assumption; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/]
- **Assumption:** Web and enterprise-agent benchmarks are the least misleading public proxy for AI-agent-executed business-process failure because public incident reporting for deployed agents is still sparse and not normalised by task type or detection timing. **Justification:** the retrieved benchmarks expose multi-step tasks with tools, policy constraints, and externally visible actions, which are the defining properties of the do-mode surface. [assumption; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2403.07718; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352]

#### Analysis

The evidence weighs more strongly on control structure than on exact percentages, because the public literature does not yet publish a common denominator for "released AI-assisted changes" and "production agent actions" in the same dataset. [inference; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045]

Build mode is still risky, and the 2024 DORA findings show that AI adoption can reduce stability if teams allow larger or less disciplined changes through the pipeline, but the failure is still mediated by typed interfaces, tests, code review, staged release, and rollback. [inference; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://sre.google/sre-book/testing-reliability/]

Do mode is different because the model is not only producing an artifact for later verification, it is selecting tools, interpreting policy, and causing state changes in a live environment, which means the same error can carry customer, operational, or compliance consequences immediately. [inference; source: https://www.anthropic.com/research/building-effective-agents; https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2309.15817]

The practical trade-off is therefore between front-loaded verification cost in build mode and runtime supervision cost in do mode. [inference; source: https://sre.google/sre-book/testing-reliability/; https://www.bis.org/fsi/fsisummaries/op_resilience.htm]

Part of the observed difference could still be explained by unmatched proxies and benchmark immaturity rather than by delivery mode alone, because public build-mode evidence is measured as escaped post-release failure while public do-mode evidence is measured as benchmark task success and severe-action frequency. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2309.15817]

For regulated financial services, the stronger recommendation is not "never use do mode," but "treat do mode as a runtime control problem from day one," with narrow permissions, approval checkpoints for high-impact actions, monitoring, incident playbooks, and reversible operations. [inference; source: https://artificialintelligenceact.eu/article/9/; https://www.bis.org/bcbs/publ/d516.htm; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md]

#### Risks, Gaps, and Uncertainties

- Public evidence still lacks a common, task-complexity-normalised dataset that traces AI-assisted code from authoring through release and then compares its escaped-failure rate directly with autonomous business-process execution. [fact; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2310.02059]
- Benchmark evidence for do mode is stronger than public production-incident evidence, so the exact relationship between benchmark failure rates and real production incident rates remains uncertain even though the directional signal is clear. [inference; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352]
- The Air Canada case is a strong public example of post-action detection and liability, but it is a chatbot case rather than a fully autonomous multi-tool agent case. [fact; source: https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416]
- WorkArena confirms a considerable gap to full enterprise-task automation, but the abstract alone does not provide a single summary percentage for all ServiceNow tasks, which limits precision in the enterprise-task comparison. [fact; source: https://arxiv.org/abs/2403.07718]

#### Open Questions

- What released-change telemetry would be needed inside a real software-delivery organisation to measure post-pipeline failure separately for AI-assisted and human-authored changes? [assumption; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/]
- Which runtime controls, approval checkpoints, rate limits, and reversal mechanisms reduce do-mode incident rates most effectively in regulated operations without destroying the economic case for automation? [assumption; source: https://artificialintelligenceact.eu/article/9/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm]
- How much of the current do-mode benchmark failure is due to model capability limits versus control-plane design limits such as poor scoping, inadequate verification, or overly broad permissions? [assumption; source: https://arxiv.org/abs/2402.01817; https://arxiv.org/abs/2406.13352; https://www.anthropic.com/research/building-effective-agents]

#### Output

- Type: knowledge
- Description: This item concludes that delivery mode changes where variance is controlled: mostly before release for build mode, and mostly during live operation for do mode, which is why do mode needs a stronger runtime control layer than build mode. [inference; source: https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm]
- Links:
  - https://sre.google/sre-book/testing-reliability/
  - https://arxiv.org/abs/2406.12045
  - https://artificialintelligenceact.eu/article/9/

### §7 Recursive Review

- Review result: pass
- Confidence: medium
- Acronym audit: Artificial Intelligence (AI), Site Reliability Engineering (SRE), DevOps Research and Assessment (DORA), Large Language Model (LLM), National Institute of Standards and Technology (NIST), and Artificial Intelligence Risk Management Framework (AI RMF) expanded on first use
- Claim audit: substantive claims in §2 through §6 carry explicit labels and direct-web-address sources
- Parity audit: §6 Synthesis and Findings aligned
- Retained gaps: no public post-pipeline AI-assisted-code distribution; no public production incident distribution for business-process agents

## Findings

### Executive Summary

Public evidence does not currently provide a task-complexity-normalised head-to-head failure distribution, but the strongest available proxy comparison indicates that AI-assisted code that clears a standard gated delivery pipeline is more pre-effect-detectable than AI agents executing business processes directly, and it points toward, rather than directly proves, fewer externally realised failures. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045]

Build mode is buffered by structural controls, tests, review, staged release, and deployment blocking, so many failures are converted into pre-production findings; public AI-specific evidence shows elevated before-release defect and security risk but also shows that static-analysis feedback can remediate a substantial share of those issues before release. [inference; source: https://sre.google/sre-book/testing-reliability/; https://arxiv.org/abs/2310.02059]

Do mode faces much lower baseline end-to-end reliability on realistic multi-step tasks, with WebArena reporting 14.41% GPT-4 success, tau-bench reporting fewer than 50% successful tasks and less than 25% reliability across repeated retail trials, and ToolEmu still finding severe failures 23.9% of the time even for the safest tested agent. [fact; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2309.15817]

For regulated financial services, this means build mode can usually be governed through existing release-management and incident processes, whereas do mode needs runtime least privilege, approval checkpoints, monitoring, rate limits, and kill switches because many failures are only visible after an external action or downstream reconciliation. [inference; source: https://www.bis.org/bcbs/publ/d516.htm; https://artificialintelligenceact.eu/article/9/; https://genai.owasp.org/llm08-excessive-agency/]

### Key Findings

1. **No public source located for this item provides a task-complexity-normalised, post-pipeline, head-to-head production failure distribution that directly compares AI-assisted code changes with AI-agent-executed business-process actions.** ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2310.02059; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045)
2. **Build-mode failure is most visibly measured as post-release intervention after release gates, while Site Reliability Engineering guidance supports the inference that equivalent failures can also be blocked before production by system-level tests.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/testing-reliability/)
3. **Public evidence on AI-assisted coding shows elevated before-release security and defect risk, but it also shows that static-analysis feedback can eliminate a substantial share of those issues before release, which makes build-mode variance materially filterable before external effects occur.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.02059; https://sre.google/sre-book/testing-reliability/)
4. **The 2024 DORA evidence shows local development gains alongside lower delivery stability and throughput, which supports the inference that AI assistance still requires small batches, robust tests, and disciplined review if teams want low escaped-failure rates.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://dora.dev/research/2024/dora-report/)
5. **When compared with gated build-mode proxies, realistic do-mode benchmarks indicate materially lower baseline reliability, because WebArena reports 14.41% GPT-4 success, tau-bench reports fewer than 50% successful tasks and less than 25% reliability across repeated retail trials, and AgentDojo still reports many failures even without attacks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352; https://dora.dev/guides/dora-metrics-four-keys/; https://sre.google/sre-book/testing-reliability/)
6. **Do-mode failures are harder to catch before impact because many of them arise from live tool use, policy misapplication, excessive permissions, prompt injection, or wrong action selection, all of which often become fully visible only after an external step has already been taken.** ([inference]; medium confidence; source: https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2309.15817; https://arxiv.org/abs/2402.01817; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)
7. **The strongest public legal and regulatory material places autonomous process execution inside lifecycle risk-management and operational-resilience disciplines, which supports the inference that teams cannot govern it only as a conventional pre-release software-quality problem.** ([inference]; medium confidence; source: https://artificialintelligenceact.eu/article/9/; https://www.bis.org/bcbs/publ/d516.htm; https://doi.org/10.6028/NIST.AI.100-1)
8. **The best-supported comparative conclusion is therefore that build mode is structurally more controllable than do mode, because the dominant control point in build mode is release gating before deployment while the dominant control point in do mode must remain a runtime control layer around live decisions and actions.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] No direct public head-to-head production distribution was found for post-pipeline AI-assisted code versus AI-agent-executed business processes. | https://dora.dev/research/2024/dora-report/ ; https://arxiv.org/abs/2310.02059 ; https://arxiv.org/abs/2307.13854 ; https://arxiv.org/abs/2406.12045 | high | Evidence-gap statement |
| [inference] Build-mode external failure is most visibly measured as post-release intervention, while tests can also block equivalent failures before production. | https://dora.dev/guides/dora-metrics-four-keys/ ; https://sre.google/sre-book/testing-reliability/ | medium | Escaped-failure framing |
| [inference] AI-assisted code risk is materially filterable before release because static-analysis feedback fixes many issues before they become deployed defects. | https://arxiv.org/abs/2310.02059 ; https://sre.google/sre-book/testing-reliability/ | medium | Pre-effect filterability |
| [inference] AI adoption improves local development metrics while reducing delivery stability and throughput at the system level, so disciplined review and testing remain necessary. | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://dora.dev/research/2024/dora-report/ | medium | Local versus system-level distinction |
| [inference] Realistic do-mode benchmarks indicate lower baseline reliability than gated build-mode proxies. | https://arxiv.org/abs/2307.13854 ; https://arxiv.org/abs/2406.12045 ; https://arxiv.org/abs/2406.13352 ; https://dora.dev/guides/dora-metrics-four-keys/ ; https://sre.google/sre-book/testing-reliability/ | medium | Cross-mode proxy comparison |
| [inference] Many do-mode failures are only fully visible after action because live tools, permissions, and external state mediate the harm. | https://genai.owasp.org/llm08-excessive-agency/ ; https://arxiv.org/abs/2309.15817 ; https://arxiv.org/abs/2402.01817 ; https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416 | medium | Post-effect detectability |
| [inference] Regulatory and resilience frameworks place autonomous process execution inside lifecycle testing, monitoring, mitigation, and incident-learning disciplines. | https://artificialintelligenceact.eu/article/9/ ; https://www.bis.org/bcbs/publ/d516.htm ; https://doi.org/10.6028/NIST.AI.100-1 | medium | Regulated-operations lens |
| [inference] Build mode is structurally more controllable than do mode because release gates constrain artifacts before impact, while runtime controls must constrain live decisions after deployment. | https://www.anthropic.com/research/building-effective-agents ; https://sre.google/sre-book/testing-reliability/ ; https://genai.owasp.org/llm08-excessive-agency/ ; https://www.bis.org/bcbs/publ/d516.htm | medium | Core synthesis claim |

### Assumptions

- **Assumption:** DORA instability metrics are the least misleading public proxy for post-pipeline build-mode failure because no accessible public dataset separates AI-assisted and human-authored changes after release. **Justification:** DORA explicitly measures interventions required after deployment, which matches the escaped-failure concept once tests and review have already run. [assumption; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/]
- **Assumption:** Web and enterprise-agent benchmarks are the least misleading public proxy for AI-agent-executed business-process failure because public incident reporting for deployed agents is still sparse and not normalised by task type or detection timing. **Justification:** the retrieved benchmarks expose multi-step tasks with tools, policy constraints, and externally visible actions, which are the defining properties of the do-mode surface. [assumption; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2403.07718; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352]

### Analysis
The evidence weighs more strongly on control structure than on exact percentages, because the public literature does not yet publish a common denominator for "released AI-assisted changes" and "production agent actions" in the same dataset. [inference; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045]

Build mode is still risky, and the 2024 DORA findings show that AI adoption can reduce stability if teams allow larger or less disciplined changes through the pipeline, but the failure is still mediated by typed interfaces, tests, code review, staged release, and rollback. [inference; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://sre.google/sre-book/testing-reliability/]

Do mode is different because the model is not only producing an artifact for later verification, it is selecting tools, interpreting policy, and causing state changes in a live environment, which means the same error can carry customer, operational, or compliance consequences immediately. [inference; source: https://www.anthropic.com/research/building-effective-agents; https://genai.owasp.org/llm08-excessive-agency/; https://arxiv.org/abs/2309.15817]

The practical trade-off is therefore between front-loaded verification cost in build mode and runtime supervision cost in do mode. [inference; source: https://sre.google/sre-book/testing-reliability/; https://www.bis.org/fsi/fsisummaries/op_resilience.htm]

Part of the observed difference could still be explained by unmatched proxies and benchmark immaturity rather than by delivery mode alone, because public build-mode evidence is measured as escaped post-release failure while public do-mode evidence is measured as benchmark task success and severe-action frequency. [inference; source: https://dora.dev/guides/dora-metrics-four-keys/; https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2309.15817]

For regulated financial services, the stronger recommendation is not "never use do mode," but "treat do mode as a runtime control problem from day one," with narrow permissions, approval checkpoints for high-impact actions, monitoring, incident playbooks, and reversible operations. [inference; source: https://artificialintelligenceact.eu/article/9/; https://www.bis.org/bcbs/publ/d516.htm; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md]

### Risks, Gaps, and Uncertainties

- Public evidence still lacks a common, task-complexity-normalised dataset that traces AI-assisted code from authoring through release and then compares its escaped-failure rate directly with autonomous business-process execution. [fact; source: https://dora.dev/research/2024/dora-report/; https://arxiv.org/abs/2310.02059]
- Benchmark evidence for do mode is stronger than public production-incident evidence, so the exact relationship between benchmark failure rates and real production incident rates remains uncertain even though the directional signal is clear. [inference; source: https://arxiv.org/abs/2307.13854; https://arxiv.org/abs/2406.12045; https://arxiv.org/abs/2406.13352]
- The Air Canada case is a strong public example of post-action detection and liability, but it is a chatbot case rather than a fully autonomous multi-tool agent case. [fact; source: https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416]
- WorkArena confirms a considerable gap to full enterprise-task automation, but the abstract alone does not provide a single summary percentage for all ServiceNow tasks, which limits precision in the enterprise-task comparison. [fact; source: https://arxiv.org/abs/2403.07718]

### Open Questions

- What released-change telemetry would be needed inside a real software-delivery organisation to measure post-pipeline failure separately for AI-assisted and human-authored changes? [assumption; source: https://dora.dev/guides/dora-metrics-four-keys/; https://dora.dev/research/2024/dora-report/]
- Which runtime controls, approval checkpoints, rate limits, and reversal mechanisms reduce do-mode incident rates most effectively in regulated operations without destroying the economic case for automation? [assumption; source: https://artificialintelligenceact.eu/article/9/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm]
- How much of the current do-mode benchmark failure is due to model capability limits versus control-plane design limits such as poor scoping, inadequate verification, or overly broad permissions? [assumption; source: https://arxiv.org/abs/2402.01817; https://arxiv.org/abs/2406.13352; https://www.anthropic.com/research/building-effective-agents]

---

## Output

- Type: knowledge
- Description: This item concludes that delivery mode changes where variance is controlled: mostly before release for build mode, and mostly during live operation for do mode, which is why do mode needs a stronger runtime control layer than build mode. [inference; source: https://sre.google/sre-book/testing-reliability/; https://genai.owasp.org/llm08-excessive-agency/; https://www.bis.org/bcbs/publ/d516.htm]
- Links:
  - https://sre.google/sre-book/testing-reliability/
  - https://arxiv.org/abs/2406.12045
  - https://artificialintelligenceact.eu/article/9/
