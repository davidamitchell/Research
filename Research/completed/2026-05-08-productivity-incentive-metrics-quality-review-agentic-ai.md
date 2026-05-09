---
review_count: 2
title: "What metrics beyond code acceptance rates best capture net organisational value when Artificial Intelligence (AI) coding tools are adopted with productivity mandates, and how do speed-focused incentives create hidden quality costs in high-volume agentic AI workflows?"
added: 2026-05-08T10:05:24+00:00
status: completed
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, software-engineering, incentives, governance-behaviour, enterprise, measurement, technical-debt]
started: 2026-05-09T03:09:50+00:00
completed: 2026-05-09T03:31:23+00:00
output: [knowledge]
cites: [2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls, 2026-04-26-ai-governance-culture-incentives-behaviour, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-01-human-oversight-ai-software-development, 2026-05-01-compound-error-accumulation-ai-codebases]
related: [2026-04-22-enterprise-ai-capability-model, 2026-04-26-ai-lowcode-failure-modes-governance-mitigation, 2026-05-01-appropriate-task-selection-coding-agents]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What metrics beyond code acceptance rates best capture net organisational value when Artificial Intelligence (AI) coding tools are adopted with productivity mandates, and how do speed-focused incentives create hidden quality costs in high-volume agentic AI workflows?

## Research Question

What metrics beyond code acceptance rates and lines of code best capture net organisational value when Artificial Intelligence (AI) coding tools such as GitHub Copilot are adopted with productivity mandates, and to what extent do speed-focused incentive structures create hidden quality costs, including technical debt, error propagation, and systemic "review rubber-stamping", in high-volume agentic AI workflows, meaning workflows where AI tools generate or coordinate multi-step code changes with limited human friction?

## Scope

**In scope:**
- Empirical measurement frameworks for AI coding tool productivity that go beyond acceptance rates and velocity metrics
- Evidence on how speed-focused Key Performance Indicators (KPIs) and Objectives and Key Results (OKRs) drive quality degradation, technical debt accumulation, and rubber-stamp code review behaviours
- Multi-metric scorecard approaches, meaning metric sets that intentionally combine speed, quality, oversight effectiveness, and long-term capability signals
- Organisational reward structures, including bonuses, performance reviews, and team metrics, and their specific interaction with AI coding tool adoption mandates
- Governance interventions that align individual productivity incentives with enterprise quality and risk outcomes

**Out of scope:**
- Machine learning (ML) model quality metrics unrelated to organisational incentive structures
- Consumer-tier AI product measurement outside enterprise contexts
- General software engineering metrics not specific to AI-augmented development
- Full compensation system design or Human Resources (HR) policy per jurisdiction

**Constraints:**
- Ground all claims in observable enterprise patterns and flag inferences clearly
- Expand all acronyms on first use
- Distinguish empirical evidence from theoretical frameworks
- Prior completed research on incentive misalignment and Human-in-the-Loop (HITL) review collapse provides foundational context, and this item must extend rather than duplicate it

## Context

Existing repository research has established that governance circumvention is frequently driven by organisational incentives, and that human review degrades when queue volume outruns realistic attention. [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

The remaining gap is a measurement design that separates visible local speed gains from delayed organisational costs such as rework, maintainability drift, review collapse, and capability erosion in AI-assisted coding. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-01-compound-error-accumulation-ai-codebases.html]

## Approach

1. **Sub-question 1, measurement gap:** What metrics, beyond acceptance rate, velocity, and lines of code, have been proposed or validated empirically to capture net value versus hidden costs in AI-augmented development?
2. **Sub-question 2, incentive-quality interaction:** What is the empirical evidence that local speed incentives cause systemic quality degradation, including nominal review, accumulated debt, and error propagation, in high-volume AI coding systems?
3. **Sub-question 3, multi-metric scorecard and governance interventions:** What multi-metric scorecard models and governance interventions, including low-friction approved paths for bounded low-risk work, mandatory quality gates, and dual-metric Objectives and Key Results (OKRs), have been proposed or tested?

## Sources

- [x] [DevOps Research and Assessment (DORA) Research](https://dora.dev/research/) - core model and report archive for software delivery outcomes
- [x] [DevOps Research and Assessment (DORA) (2025) Choosing measurement frameworks to fit your organizational goals](https://dora.dev/research/2025/measurement-frameworks/) - official guidance on combining frameworks, self-reported data, logs-based data, and AI-specific measures
- [x] [DevOps Research and Assessment (DORA) (2026) DORA Metrics](https://dora.dev/guides/dora-metrics/) - official five-metric delivery model, anti-gaming guidance, and improvement-loop recommendations
- [x] [Forsgren, Humble, and Kim (2018) Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/) - book page summarising the research-backed software delivery performance framing
- [x] [GitHub (2022) Research: quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) - first-party productivity study structured around the Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow (SPACE) framework
- [x] [Ziegler et al. (2022) Productivity assessment of neural code completion](https://arxiv.org/abs/2205.06537) - study showing suggestion acceptance predicts perceived productivity better than persistence metrics
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/) - bounded-task randomized controlled trial on unit-test pass rate, review quality, and approval
- [x] [Google Cloud (2024) Announcing the 2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) - official summary of AI adoption effects on code quality, documentation quality, review speed, throughput, and stability
- [x] [Google Cloud (2025) DORA AI Capabilities Model report](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report) - official summary of the capability foundations for scaling AI value
- [x] [Golubev et al. (2024) Using AI-Based Coding Assistants in Practice: State of Affairs, Perceptions, and Ways Forward](https://arxiv.org/abs/2406.07765) - survey evidence on where developers delegate work and what blocks trust
- [x] [He et al. (2025) Does AI-Assisted Coding Deliver? A Difference-in-Differences Study of Cursor's Impact on Software Projects](https://arxiv.org/html/2511.04427v2) - repository-level evidence on transient velocity gains and persistent quality degradation in agentic coding adoption
- [x] [GitClear (2025) AI Copilot Code Quality: 2025 Look Back at 12 Months of Data](https://www.gitclear.com/ai_assistant_code_quality_2025_research) - large-scale telemetry on code duplication, churn, and refactoring decline
- [x] [Massachusetts Institute of Technology (MIT) Sloan Management Review (2025) The Hidden Costs of Coding With Generative AI](https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/) - management synthesis linking isolated-task gains to legacy-environment debt risk
- [x] [National Institute of Standards and Technology (NIST) (2023) AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - official governance, monitoring, training, inventory, and accountability guidance

## Related

- [Mitchell (2026) What capability and control design is needed to mitigate incentive misalignment, shadow Artificial Intelligence (AI), rail bypass, and skill decay at enterprise scale?](https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html)
- [Mitchell (2026) How should human-in-the-loop (HITL) design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
- [Mitchell (2026) What is the evidence for human oversight as an effective quality gate in Artificial Intelligence (AI)-assisted software development?](https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html)
- [Mitchell (2026) How do errors compound in Artificial Intelligence (AI)-agent-heavy codebases, and what review strategies can manage this risk?](https://davidamitchell.github.io/Research/research/2026-05-01-compound-error-accumulation-ai-codebases.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings below.)*

### §0 Initialise

- Question: Which metrics capture net organisational value from AI coding tools once short-term speed gains are offset against delayed quality, review, and capability costs?
- Scope: Enterprise AI-assisted software delivery measurement, incentive design, and governance intervention, not consumer tooling or general compensation design.
- Constraints: Observable enterprise patterns first, explicit epistemic labels, acronym expansion on first use, and repository cross-reference before synthesis.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html; https://davidamitchell.github.io/Research/research/2026-05-01-compound-error-accumulation-ai-codebases.html] Prior completed items already establish that local incentives shape governance adherence, high review volume collapses into nominal oversight, human quality gates matter more than nominal sign-off, and AI-heavy code generation can accumulate maintainability debt when verification does not scale with output.
- [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] This item therefore needs to convert local productivity evidence into a service-level measurement system that captures both visible gains and delayed losses, because official measurement guidance already warns against relying on one metric or one time horizon.

### §1 Question Decomposition

- **Root question:** What measurement and governance design tells an organisation whether AI coding adoption is creating net value rather than only visible activity?
- **A. What does the visible speed signal actually measure?**
  - A1. What does suggestion acceptance rate measure?
  - A2. What do bounded-task speed studies measure well?
  - A3. What do those local measures fail to capture at repository or service level?
- **B. Which broader outcomes best represent net organisational value?**
  - B1. Which delivery outcomes do DORA and Accelerate treat as organisation-level value?
  - B2. Which developer-experience or trust measures matter in AI-assisted development?
  - B3. Which review and quality metrics expose hidden costs?
- **C. What evidence shows hidden quality costs after AI adoption?**
  - C1. What evidence exists for code complexity, static warnings, duplication, or churn increases?
  - C2. What evidence exists for delivery instability despite local speed gains?
  - C3. What evidence shows review queues or oversight quality degrade under high volume?
- **D. How do incentives distort the picture?**
  - D1. What do official measurement frameworks say about turning metrics into targets?
  - D2. What evidence suggests local speed mandates will hide delayed costs?
- **E. Which governance interventions best realign value?**
  - E1. Which team-level scorecard components should coexist?
  - E2. Which process controls preserve speed without sacrificing quality or oversight?
  - E3. Which metrics indicate that human capability to challenge AI output is decaying?

### §2 Investigation

- Prior completed-item sweep:
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html; https://davidamitchell.github.io/Research/research/2026-05-01-compound-error-accumulation-ai-codebases.html] The closest corpus items already connect incentives to circumvention, review overload to rubber-stamping, and AI-heavy output to verification-capacity stress and maintainability drift.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The gap left by prior corpus work is not whether these failure modes exist, but how to measure them early enough that a productivity mandate does not turn them into invisible cost transfer.

- **A. Acceptance rate and bounded-task measures capture local experience, not whole-system value.**
  - [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] GitHub's 2022 study explicitly rejected output-only productivity and used the Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow (SPACE) framework, surveying more than 2,000 developers and running a controlled task experiment where Copilot users completed the task 55% faster.
  - [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] The same study found that perceived value included satisfaction, flow, and reduced mental effort, not only task speed, which means even the vendor study frames productivity as multidimensional.
  - [fact; source: https://arxiv.org/abs/2205.06537] Ziegler et al. report that suggestion acceptance rate, rather than more specific persistence metrics for code that remains over time, drives developers' perception of productivity.
  - [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized controlled trial found that code written with Copilot on a bounded web-server task passed more unit tests, was rated slightly more readable, reliable, maintainable, and concise, and was 5% more likely to be approved by reviewers.
  - [inference; source: https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Acceptance rate, task-completion speed, and one-task approval rate are therefore valid local signals, but they cannot by themselves show whether an organisation is gaining maintainable system throughput over time.

- **B. Official measurement frameworks recommend a broader outcome set.**
  - [fact; source: https://dora.dev/research/2025/measurement-frameworks/] DORA's 2025 measurement guidance says organisations should choose frameworks based on the decisions they need to inform, and it explicitly distinguishes self-reported data from logs-based measures because each captures different parts of software development reality.
  - [fact; source: https://dora.dev/research/2025/measurement-frameworks/] In the AI section, DORA says organisations may need to add AI-specific metrics such as suggestion acceptance, model quality, trust, perceived productivity, and time spent reviewing code, while keeping their broader framework intact.
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA's delivery guide says five software delivery performance metrics predict better organisational performance and employee well-being: change lead time, deployment frequency, failed deployment recovery time, change fail rate, and deployment rework rate.
  - [fact; source: https://dora.dev/guides/dora-metrics/] The same guide warns that setting metrics as goals increases gaming risk, that one metric cannot represent complex systems, and that teams should add leading indicators such as code review time or test quality when improving the system.
  - [fact; source: https://itrevolution.com/product/accelerate/] Accelerate describes its contribution as rigorous measurement of software delivery performance and the capabilities that drive it, which supports treating delivery outcomes, not only developer activity, as the core value surface.
  - [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] The best-supported measurement baseline is therefore a multi-metric scorecard that joins AI-local signals to service-level delivery outcomes, review-load signals, and developer-experience signals rather than replacing the older framework with a single AI adoption metric.

- **C. Repository-scale and service-scale evidence exposes hidden quality costs that local speed metrics miss.**
  - [fact; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report] Google's 2024 DORA report found that a 25% increase in AI adoption was associated with a 7.5% increase in documentation quality, a 3.4% increase in code quality, and a 3.1% increase in code review speed.
  - [fact; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report] The same DORA report found that higher AI adoption was also associated with an estimated 1.5% decrease in delivery throughput and a 7.2% reduction in delivery stability, which shows that local process gains did not automatically convert into better whole-system delivery.
  - [fact; source: https://arxiv.org/html/2511.04427v2] He et al. estimate that adopting Cursor caused significant but transient project-level velocity gains, while static analysis warnings increased by about 30% and code complexity increased by about 41%, with the added debt contributing to later velocity slowdown.
  - [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear's 2025 telemetry analysis of 211 million changed lines reports that moved or refactoring-associated code fell from 25% of changed lines in 2021 to under 10% in 2024, while copy-pasted or cloned code rose from 8.3% to 12.3%.
  - [fact; source: https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/] MIT Sloan argues that isolated-task productivity studies do not capture legacy-environment risk, and it uses interview evidence plus external telemetry to argue that unmanaged AI coding can compound technical debt and destabilize scaling.
  - [inference; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/] Hidden quality costs are most visible in maintainability and recovery surfaces, including warnings, complexity, duplication, rework, and instability, rather than in acceptance or raw code volume.

- **D. Trust, context limits, and review effort remain part of the value equation.**
  - [fact; source: https://arxiv.org/abs/2406.07765] Golubev et al. found that developers most often want to delegate writing tests and natural-language artifacts, while lack of trust, company policies, and lack of project-size context are major reasons not to use AI assistants.
  - [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] DORA's 2025 AI capabilities summary says AI is an amplifier, that success depends more on foundational systems and culture than on the tool itself, and that internal platforms are crucial for turning individual gains into systemic improvement.
  - [inference; source: https://arxiv.org/abs/2406.07765; https://dora.dev/research/2025/measurement-frameworks/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] Organisations therefore need trust and review-effort measures, including time spent reviewing code, because low-context generation that requires expensive human reconstruction can erase visible coding speed gains.

- **E. Speed-focused incentives distort behaviour when they reward visible output and hide delayed remediation.**
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA explicitly warns that broad performance goals built directly from metrics increase the likelihood that teams will game the metrics.
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html] Prior corpus work shows that people route around governance when the sanctioned path imposes visible local cost while the cost of policy breach or debt is diffuse, delayed, or carried by someone else.
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html] Prior corpus work also shows that queue growth, low disagreement, low override rates, and thin verification intensity are credible indicators that human review has become nominal rather than meaningful.
  - [inference; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] AI suggestion acceptance, lines of code, or AI-generated pull request volume are especially poor choices for individual performance mandates because they reward visible activity while masking delayed rework and degraded review quality.

- **F. The strongest governance interventions combine process, platform, and oversight metrics.**
  - [fact; source: https://dora.dev/guides/dora-metrics/] DORA recommends small batch sizes, cross-functional improvement work, and leading indicators such as code review time and test quality when trying to improve delivery performance.
  - [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report] DORA's 2025 AI capabilities summary says organisations maximise AI value by investing in foundational capabilities such as a clear and communicated AI stance, healthy data ecosystems, user-centricity, and internal platforms.
  - [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST's Artificial Intelligence Risk Management Framework says governance is cross-cutting and should include ongoing monitoring, inventory, defined roles, training, periodic review, and mechanisms to align technical practice with organisational risk tolerance.
  - [inference; source: https://dora.dev/guides/dora-metrics/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The most defensible intervention set is a team-level scorecard with paired speed and quality targets, low-friction approved paths for low-risk bounded work, mandatory escalation for high-blast-radius changes, and monitoring that makes review collapse visible before incidents force attention.

- **G. Capability preservation is a real but weaker-measured part of net value.**
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html] Prior completed work found that AI assistance can weaken human verification and judgment capability when work is continuously delegated and no deliberate practice remains.
  - [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] NIST requires training, clear lines of responsibility, and periodic review of risk-management outcomes, which supports tracking whether people still have the competence to challenge automated outputs.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://dora.dev/research/2025/measurement-frameworks/] Net organisational value should therefore include a capability-retention surface, such as periodic unaided task performance or review-quality calibration, even though the public coding-specific evidence for this metric is still thinner than the delivery evidence.

- **H. Evidence limits**
  - [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/] GitClear and MIT Sloan are directionally useful for maintainability risk, but they are not substitutes for peer-reviewed longitudinal enterprise field studies on every claim in this item.
  - [assumption; source: https://arxiv.org/html/2511.04427v2; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report] The He et al. repository-level results and the DORA 2024 survey findings are transferable enough to enterprise AI coding governance because both describe post-adoption system behavior rather than only isolated-task performance, but they still come from mixed populations rather than one common enterprise panel.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://dora.dev/research/2025/measurement-frameworks/] Acceptance rate is a perception-adjacent metric because it mostly explains how useful the tool feels at the point of suggestion, while framework guidance says organisational measurement must instead be tied to the decision the organisation is trying to make.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2] The evidence is coherent if bounded-task gains and repository-scale losses are treated as different levels of analysis rather than as competing truths.
- [inference; source: https://dora.dev/guides/dora-metrics/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The hidden-cost problem appears because speed metrics surface instantly while rework, review burden, and maintainability penalties accumulate later and are often owned by a wider team.
- [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://dora.dev/guides/dora-metrics/] The right governance answer is therefore not to reject speed measurement, but to place it inside a system that also measures stability, review quality, and capability health and that gives leaders a sanctioned path for low-risk use.

### §4 Consistency Check

- [fact; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/] Official DORA guidance is internally consistent that organisations should choose multiple metrics based on decision context and should not let one metric become the goal.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2] Bounded-task evidence and repository-level evidence point in different directions on some outcomes, but they do not conflict once task scope, time horizon, and scale are held constant.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html] The prior repository evidence is also consistent that review quality must be measured directly, because nominal review can coexist with formal human touchpoints.
- [inference; source: https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/guides/dora-metrics/] The strongest unresolved uncertainty is not whether hidden quality costs exist, but how quickly and at what scale each leading indicator becomes predictive enough for operational gating.

### §5 Depth and Breadth Expansion

- **Technical lens**
  - [fact; source: https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/guides/dora-metrics/] The most useful technical hidden-cost indicators are static warnings, code complexity, duplication, deployment rework, and change failure, because they connect fast local generation to later maintenance and recovery work.
- **Behavioural lens**
  - [fact; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Behaviourally, the failure occurs when the organisation rewards visible activity and leaves review quality and remediation work weakly owned, because that combination makes gaming and rubber-stamping rational.
- **Economic lens**
  - [fact; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/] Economically, the key mistake is to book near-term coding-time savings as full value while leaving debt service, rollback work, and legacy-codebase integration costs off the scorecard.
- **Governance lens**
  - [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Governance-wise, AI value scales best when the sanctioned platform is useful, clearly governed, and observable, because culture and platform maturity determine whether local gains can become organisational gains.
- **Workforce lens**
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Workforce-wise, a multi-metric scorecard should include some check that humans still know how to evaluate what the tool produced, because otherwise the review surface decays even if delivery speed looks strong.

### §6 Synthesis

**Executive summary:**

AI coding adoption creates net organisational value only when leaders measure service-level speed and stability, code quality, and review load together rather than relying on acceptance rate or code volume alone. [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://arxiv.org/abs/2205.06537]

Acceptance rate and bounded-task speed studies capture real local gains, but they mostly describe perceived usefulness and constrained-task performance rather than whether the organisation is building better software faster over time. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]

Repository-scale evidence shows that higher AI adoption can coexist with more static warnings, greater code complexity, more duplication, and worse delivery stability, which means hidden costs appear in rework, maintainability, and recovery surfaces before they appear in suggestion metrics. [inference; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Speed-focused individual mandates are therefore risky because they reward visible activity while shifting debt service and review failure onto the wider system, so the defensible operating model is a team-level multi-metric scorecard plus risk-tiered governance, not an AI acceptance quota. [inference; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

**Key findings:**

1. **Suggestion acceptance rate and lines of code should not be treated as standalone net-value measures because acceptance mainly tracks perceived usefulness, while official measurement guidance says organisational value must be judged with a broader decision-aligned framework.** ([inference]; high confidence; source: https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://dora.dev/research/2025/measurement-frameworks/)
2. **A defensible AI coding scorecard must combine local AI signals with organisation-level delivery outcomes, specifically DORA throughput and instability measures, review-effort signals, and developer trust or experience measures, because official guidance says no single framework captures the whole system.** ([inference]; high confidence; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://itrevolution.com/product/accelerate/)
3. **Bounded-task experiments show that AI coding tools can improve local speed and even local code quality, but those positive results should be treated as local evidence rather than proof of repository-scale gains because the studies use constrained tasks with clear success criteria and short time horizons.** ([inference]; medium confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2)
4. **Repository-level and service-level evidence indicates that AI adoption can create hidden quality costs, because higher adoption has been associated with lower delivery stability, more static warnings, and greater code complexity even when some local quality metrics improve.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2)
5. **The most decision-useful hidden-cost metrics are maintainability and recovery indicators, including static analysis warnings, code complexity, duplicated code, deployment rework, change fail rate, and failed deployment recovery time, because those metrics surface debt that speed metrics hide.** ([inference]; medium confidence; source: https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/guides/dora-metrics/)
6. **Speed-focused performance mandates are likely to distort behaviour because DORA warns that turning metrics into goals invites gaming, and adjacent repository evidence shows that queue pressure and weak incentives convert formal review into rubber-stamping rather than meaningful scrutiny.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
7. **A defensible governance intervention set is a team-level scorecard with paired speed and stability or maintainability targets, plus low-friction approved paths for bounded low-risk work, small batches, robust testing, and mandatory escalation for high-blast-radius changes.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
8. **High-volume agentic AI workflows require direct oversight-quality metrics, such as review latency, disagreement or override rate, verification intensity, and post-merge defect or rollback signals, because human touchpoints alone do not prove that review remains real.** ([inference]; medium confidence; source: https://dora.dev/research/2025/measurement-frameworks/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html)
9. **A complete net-value scorecard should include a capability-retention signal, such as periodic unaided review or calibration tasks, because organisations lose part of AI's long-term value if humans stop being able to challenge or repair what the tools produce.** ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Acceptance rate is useful for local tool value, but it is not enough to represent durable organisational value on its own. | https://arxiv.org/abs/2205.06537 ; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ ; https://dora.dev/research/2025/measurement-frameworks/ | high | local-usefulness surface |
| [inference] Balanced measurement must combine AI-local signals with DORA delivery outcomes, review effort, and trust. | https://dora.dev/research/2025/measurement-frameworks/ ; https://dora.dev/guides/dora-metrics/ ; https://itrevolution.com/product/accelerate/ | high | framework synthesis |
| [inference] Bounded-task studies show genuine local gains, but those results should not be read as repository-scale proof without broader evidence. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ ; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://arxiv.org/html/2511.04427v2 | medium | constrained tasks |
| [inference] Repository-scale studies indicate hidden quality costs despite some local gains. | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://arxiv.org/html/2511.04427v2 | medium | scale and time-horizon effect |
| [inference] Maintainability and recovery metrics expose debt better than speed-only metrics. | https://arxiv.org/html/2511.04427v2 ; https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://dora.dev/guides/dora-metrics/ | medium | debt visibility |
| [inference] Individual speed mandates will likely distort behaviour and degrade review quality. | https://dora.dev/guides/dora-metrics/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html ; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | behaviour transfer |
| [inference] Team-level paired speed and quality metrics, small batches, robust testing, and risk-tiered escalation form a defensible alignment package. | https://dora.dev/guides/dora-metrics/ ; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | medium | governance package |
| [inference] Review-quality metrics must be measured directly in high-volume AI workflows. | https://dora.dev/research/2025/measurement-frameworks/ ; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html ; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html | medium | oversight surface |
| [inference] Capability-retention should stay on the scorecard even though public coding-specific evidence is thinner. | https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | low | weaker evidence base |

**Assumptions:**

- [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/] GitClear's telemetry is treated as directionally useful for maintainability drift even though it is not peer-reviewed, because it aligns with the repository-level debt pattern reported elsewhere.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://dora.dev/research/2025/measurement-frameworks/] Oversight-quality measures from adjacent review-volume research are transferable to AI-assisted code review because the shared mechanism is queue pressure and evidence-checking burden.
- [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Capability-retention metrics belong on the scorecard even though public coding-specific field data is limited, because governance guidance and adjacent evidence both require competent humans who can still evaluate automated output.

**Analysis:**

The strongest public evidence does not support a simple "AI helps" or "AI harms" conclusion, because the sign of the effect changes with level of analysis. [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2]

Bounded-task studies are credible evidence that AI can improve local execution, while DORA and repository-level studies are credible evidence that local execution gains can still produce worse system outcomes when integration, review, and maintenance costs are counted. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2]

That tension means the right numerator is not "more accepted suggestions" but "more stable, recoverable, maintainable delivery per unit of human attention and platform cost." [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/]

The incentive problem is central because delayed costs, such as rollback work, duplication cleanup, and exhausted reviewers, are easier to hide than accepted suggestions or merged changes, so metric design determines whether leaders even see the transfer. [inference; source: https://dora.dev/guides/dora-metrics/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]

The most plausible rival remedy is simply to add more reviewers and keep the mandate, but adjacent review-volume evidence shows that review quality is limited by vigilance and verification intensity as well as staffing, so adding headcount without narrowing the approval surface is unlikely to solve the problem cleanly. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html]

**Risks, gaps, uncertainties:**

- Direct public field experiments on AI-specific productivity mandates, such as individual suggestion-acceptance quotas or lines-of-code targets, remain scarce, so the incentive conclusions are partly inferential rather than experimentally isolated. [inference; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]
- He et al. provides strong repository-level evidence, but it is an arXiv preprint on open-source projects rather than a single-enterprise longitudinal panel. [fact; source: https://arxiv.org/html/2511.04427v2]
- GitClear and MIT Sloan are useful for maintainability-risk direction, but both are weaker than peer-reviewed longitudinal enterprise studies. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/]
- Capability-retention metrics are the least mature part of the scorecard, because public coding-specific evidence on skill retention under AI-heavy development is still sparse. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]

**Open questions:**

- Which review-quality signal, such as disagreement rate, latency, or post-merge defect discovery, is most predictive of future incidents in AI-assisted repositories?
- At what change size or blast radius should an AI-authored change automatically leave the fast lane and require architecture or ownership review?
- Which team-level scorecard design most effectively balances AI experimentation with production stability in large legacy codebases?

### §7 Recursive Review

- Acronym audit: AI, KPIs, OKRs, HITL, DORA, ML, and NIST are expanded on first use in the document.
- Prior-work sweep repeated: adjacent completed items on incentives, review overload, human oversight, and compounding error were cited where they materially sharpened the same control surface.
- Confidence check: medium overall, because the strongest conclusions rely on official DORA guidance plus one strong repository-level preprint and one large telemetry study rather than a mature body of enterprise field experiments.
- Findings parity check: the Findings section below mirrors the synthesis claims, confidence levels, and source sets without adding new substantive claims.

---

## Findings

### Executive Summary

AI coding adoption creates net organisational value only when leaders measure service-level speed and stability, code quality, and review load together rather than relying on acceptance rate or code volume alone. [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://arxiv.org/abs/2205.06537]

Acceptance rate and bounded-task speed studies capture real local gains, but they mostly describe perceived usefulness and constrained-task performance rather than whether the organisation is building better software faster over time. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]

Repository-scale evidence shows that higher AI adoption can coexist with more static warnings, greater code complexity, more duplication, and worse delivery stability, which means hidden costs appear in rework, maintainability, and recovery surfaces before they appear in suggestion metrics. [inference; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Speed-focused individual mandates are therefore risky because they reward visible activity while shifting debt service and review failure onto the wider system, so the defensible operating model is a team-level multi-metric scorecard plus risk-tiered governance, not an AI acceptance quota. [inference; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

### Key Findings

1. **Suggestion acceptance rate and lines of code should not be treated as standalone net-value measures because acceptance mainly tracks perceived usefulness, while official measurement guidance says organisational value must be judged with a broader decision-aligned framework.** ([inference]; high confidence; source: https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://dora.dev/research/2025/measurement-frameworks/)
2. **A defensible AI coding scorecard must combine local AI signals with organisation-level delivery outcomes, specifically DORA throughput and instability measures, review-effort signals, and developer trust or experience measures, because official guidance says no single framework captures the whole system.** ([inference]; high confidence; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://itrevolution.com/product/accelerate/)
3. **Bounded-task experiments show that AI coding tools can improve local speed and even local code quality, but those positive results should be treated as local evidence rather than proof of repository-scale gains because the studies use constrained tasks with clear success criteria and short time horizons.** ([inference]; medium confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2)
4. **Repository-level and service-level evidence indicates that AI adoption can create hidden quality costs, because higher adoption has been associated with lower delivery stability, more static warnings, and greater code complexity even when some local quality metrics improve.** ([inference]; medium confidence; source: https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2)
5. **The most decision-useful hidden-cost metrics are maintainability and recovery indicators, including static analysis warnings, code complexity, duplicated code, deployment rework, change fail rate, and failed deployment recovery time, because those metrics surface debt that speed metrics hide.** ([inference]; medium confidence; source: https://arxiv.org/html/2511.04427v2; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/guides/dora-metrics/)
6. **Speed-focused performance mandates are likely to distort behaviour because DORA warns that turning metrics into goals invites gaming, and adjacent repository evidence shows that queue pressure and weak incentives convert formal review into rubber-stamping rather than meaningful scrutiny.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
7. **A defensible governance intervention set is a team-level scorecard with paired speed and stability or maintainability targets, plus low-friction approved paths for bounded low-risk work, small batches, robust testing, and mandatory escalation for high-blast-radius changes.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
8. **High-volume agentic AI workflows require direct oversight-quality metrics, such as review latency, disagreement or override rate, verification intensity, and post-merge defect or rollback signals, because human touchpoints alone do not prove that review remains real.** ([inference]; medium confidence; source: https://dora.dev/research/2025/measurement-frameworks/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html)
9. **A complete net-value scorecard should include a capability-retention signal, such as periodic unaided review or calibration tasks, because organisations lose part of AI's long-term value if humans stop being able to challenge or repair what the tools produce.** ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Acceptance rate is useful for local tool value, but it is not enough to represent durable organisational value on its own. | https://arxiv.org/abs/2205.06537 ; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ ; https://dora.dev/research/2025/measurement-frameworks/ | high | local-usefulness surface |
| [inference] Balanced measurement must combine AI-local signals with DORA delivery outcomes, review effort, and trust. | https://dora.dev/research/2025/measurement-frameworks/ ; https://dora.dev/guides/dora-metrics/ ; https://itrevolution.com/product/accelerate/ | high | framework synthesis |
| [inference] Bounded-task studies show genuine local gains, but those results should not be read as repository-scale proof without broader evidence. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ ; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://arxiv.org/html/2511.04427v2 | medium | constrained tasks |
| [inference] Repository-scale studies indicate hidden quality costs despite some local gains. | https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report ; https://arxiv.org/html/2511.04427v2 | medium | scale and time-horizon effect |
| [inference] Maintainability and recovery metrics expose debt better than speed-only metrics. | https://arxiv.org/html/2511.04427v2 ; https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://dora.dev/guides/dora-metrics/ | medium | debt visibility |
| [inference] Individual speed mandates will likely distort behaviour and degrade review quality. | https://dora.dev/guides/dora-metrics/ ; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html ; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html | medium | behaviour transfer |
| [inference] Team-level paired speed and quality metrics, small batches, robust testing, and risk-tiered escalation form a defensible alignment package. | https://dora.dev/guides/dora-metrics/ ; https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | medium | governance package |
| [inference] Review-quality metrics must be measured directly in high-volume AI workflows. | https://dora.dev/research/2025/measurement-frameworks/ ; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html ; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html | medium | oversight surface |
| [inference] Capability-retention should stay on the scorecard even though public coding-specific evidence is thinner. | https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html ; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | low | weaker evidence base |

### Assumptions

- GitClear's telemetry is treated as directionally useful for maintainability drift even though it is not peer-reviewed, because it aligns with the repository-level debt pattern reported elsewhere. [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/]
- Oversight-quality measures from adjacent review-volume research are transferable to AI-assisted code review because the shared mechanism is queue pressure and evidence-checking burden. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://dora.dev/research/2025/measurement-frameworks/]
- Capability-retention metrics belong on the scorecard even though public coding-specific field data is limited, because governance guidance and adjacent evidence both require competent humans who can still evaluate automated output. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]

### Analysis

The strongest public evidence does not support a simple "AI helps" or "AI harms" conclusion, because the sign of the effect changes with level of analysis. [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2]

Bounded-task studies are credible evidence that AI can improve local execution, while DORA and repository-level studies are credible evidence that local execution gains can still produce worse system outcomes when integration, review, and maintenance costs are counted. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report; https://arxiv.org/html/2511.04427v2]

That tension means the right numerator is not "more accepted suggestions" but "more stable, recoverable, maintainable delivery per unit of human attention and platform cost." [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/]

The incentive problem is central because delayed costs, such as rollback work, duplication cleanup, and exhausted reviewers, are easier to hide than accepted suggestions or merged changes, so metric design determines whether leaders even see the transfer. [inference; source: https://dora.dev/guides/dora-metrics/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]

The most plausible rival remedy is simply to add more reviewers and keep the mandate, but adjacent review-volume evidence shows that review quality is limited by vigilance and verification intensity as well as staffing, so adding headcount without narrowing the approval surface is unlikely to solve the problem cleanly. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-01-human-oversight-ai-software-development.html]

### Risks, Gaps, and Uncertainties

- Direct public field experiments on AI-specific productivity mandates, such as individual suggestion-acceptance quotas or lines-of-code targets, remain scarce, so the incentive conclusions are partly inferential rather than experimentally isolated. [inference; source: https://dora.dev/guides/dora-metrics/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html]
- He et al. provides strong repository-level evidence, but it is an arXiv preprint on open-source projects rather than a single-enterprise longitudinal panel. [fact; source: https://arxiv.org/html/2511.04427v2]
- GitClear and MIT Sloan are useful for maintainability-risk direction, but both are weaker than peer-reviewed longitudinal enterprise studies. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://sloanreview.mit.edu/article/the-hidden-costs-of-coding-with-generative-ai/]
- Capability-retention metrics are the least mature part of the scorecard, because public coding-specific evidence on skill retention under AI-heavy development is still sparse. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]

### Open Questions

- Which review-quality signal, such as disagreement rate, latency, or post-merge defect discovery, is most predictive of future incidents in AI-assisted repositories?
- At what change size or blast radius should an AI-authored change automatically leave the fast lane and require architecture or ownership review?
- Which team-level scorecard design most effectively balances AI experimentation with production stability in large legacy codebases?

---

## Output

- Type: knowledge
- Description: This item produces a measurement and governance synthesis showing that AI coding value should be judged with a team-level multi-metric scorecard that pairs delivery speed with stability, maintainability, review quality, and capability-retention signals rather than with suggestion acceptance or code-volume mandates alone. [inference; source: https://dora.dev/research/2025/measurement-frameworks/; https://dora.dev/guides/dora-metrics/; https://arxiv.org/abs/2205.06537; https://arxiv.org/html/2511.04427v2]
- Links:
  - https://dora.dev/research/2025/measurement-frameworks/
  - https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report
  - https://arxiv.org/html/2511.04427v2
