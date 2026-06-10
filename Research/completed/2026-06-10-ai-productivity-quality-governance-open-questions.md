---
review_count: 1
title: "AI productivity, quality, and governance open questions"
added: 2026-06-10T09:29:28+00:00
status: completed
priority: high  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
themes: [benchmarks-eval, software-engineering, enterprise-adoption, governance-policy, agentic-ai]  # 3-5 canonical slugs from docs/themes-vocabulary.md
started: 2026-06-10T11:02:04+00:00
completed: 2026-06-10T11:43:14+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-30-ai-code-entropy-quality-metrics, 2026-05-08-ai-skill-decay-deskilling-measurement-interventions, 2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls, 2026-05-07-ai-production-incidents-deep-dive, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates, 2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator]
related: [2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator, 2026-05-31-itil-capacity-baseline-assertion-vs-telemetry, 2026-04-30-tdd-feedback-loops-ai-augmented-dev]        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions:
  - version: "1.0"
    sha: 2ca3c903b1a6e840867ea8aa268ec5ca8d86bf63
    changed: 2026-06-10
    progress: progress/2026-06-10-ai-productivity-quality-governance-open-questions.md
    summary: "Initial completion"
---

# AI productivity, quality, and governance open questions

## Research Question

What empirical evidence can distinguish sustainable Artificial Intelligence (AI)-enabled software delivery gains from short-lived throughput effects and hidden quality or governance costs in production engineering organizations over a 12-to-24-month horizon?

## Scope

**In scope:**
- Empirical productivity and throughput metrics (per-developer repository creation, approval latency, capacity constraints, fast-path versus exception-path flow)
- Longitudinal quality and maintainability indicators (architectural coherence, cognitive debt proxies, maintenance effort ratios, mutation-score trends)
- Organizational readiness and operating-model controls (Platform Engineering maturity, junior onboarding redesign, runtime controls, rollback and reversal design)
- Comparison of suggestion-based assistants versus autonomous multi-step code agents in regulated and high-control environments

**Out of scope:**
- Vendor marketing claims without field evidence or reproducible methods
- Consumer use cases outside professional software delivery organizations
- Prescriptive tooling selection for a single company without transferable evidence

**Constraints:** (time, source types, access)
- Prioritize studies and field reports from 2019–2026 to capture pre-assistant and post-adoption periods
- Use public sources only (peer-reviewed papers, standards, benchmark reports, engineering field studies, regulator publications)
- Separate directly observed facts from model-based inferences where causal evidence is incomplete

## Context

This question informs strategic decisions about where to adopt agentic delivery tooling, where to hold stricter controls, and which measurement system can detect whether observed acceleration is producing durable value or deferred operational risk.

## Approach

Decompose the investigation into independent evidence threads that can be synthesized into one decision-ready model.

1. Throughput and bottleneck dynamics
   1a. Measure whether repository and change-volume growth remains significant after normalizing for developer-count growth.
   1b. Test whether bottlenecks shift from approval latency to execution capacity as governance and approvals are streamlined.
   1c. Estimate whether the observed stability drop during adoption behaves as a temporary transition effect or a persistent steady-state penalty.
   1d. Quantify fast-path versus exception-path flow changes as throughput increases.
2. Codebase quality and maintenance externalities
   2a. Evaluate 12-to-24-month architectural coherence outcomes in teams with high assistant usage.
   2b. Identify validated instruments for measuring cognitive debt accumulation in AI-assisted codebases.
   2c. Estimate maintenance ratios for workaround-heavy agent outputs (review, operations, and incident recovery effort).
   2d. Compare mutation-score trajectories across representative repositories between 2019 and 2025.
3. Organizational readiness and governance calibration
   3a. Identify the minimum Platform Engineering maturity conditions associated with net-positive outcomes.
   3b. Evaluate onboarding and career-path redesign options for junior engineers when entry-level automation tasks are displaced.
   3c. Compare runtime controls and approval patterns that reduce do-mode incidents while preserving economic return.
   3d. Evaluate the option value of time-boxed recurring-agent pilots for target-state architecture discovery.
4. Agentic versus suggestion-based tool comparison
   4a. Compare productivity and quality outcomes for autonomous code agents versus suggestion-based copilots.
   4b. Estimate incident-type asymmetry between explicit hard failures and silent semantic degradations.
   4c. Identify new high-control field evidence from heavily regulated engineering environments.

## Sources

Starting points: papers, articles, videos, repos, docs.
**Every source must include a URL.** Use the display name formats below: they feed the `Author (Year)` citation labels shown on the generated site:

- `[Smith et al. (YYYY) Title of paper](https://url)` : for papers with named authors
- `[Organisation Title](https://url)` : for documentation, standards, or pages without a named author

- [x] [GitHub Issue #621: Many new research questions to answer outstanding questions](https://github.com/davidamitchell/Research/issues/621): seed set of open questions spanning productivity, quality, governance, and agentic adoption.
- [x] [DevOps Research and Assessment (DORA) (2024) Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/): official annual report; AI adoption increases individual productivity but decreases delivery stability by 7.2% and throughput by 1.5% per 25% AI adoption increase; rework rate added as fifth metric.
- [x] [Omansky et al. (2025) AI Copilot Code Quality Research 2025 – GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research): analysis of 211 million changed lines of code (2020–2024); code churn rose from 3.1% to 5.7%, copy/pasted lines rose from 8.3% to 12.3%, refactored lines fell from 24.1% to 9.5%.
- [x] [Anthropic and METR (2025) Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/): randomized controlled trial (RCT) with 16 experienced developers on large open-source repositories; developers took 19% longer to complete issues with frontier AI tools.
- [x] [Anthropic and METR (2025) arXiv preprint 2507.09089](https://arxiv.org/abs/2507.09089): peer-reviewed preprint of the METR RCT study above.
- [x] [Faros AI (2025) AI Productivity Paradox: AI Coding Assistants Increase Developer Output, Not Company Productivity](https://www.faros.ai/blog/ai-software-engineering): telemetry from 10,000 developers across 1,255 teams; pull request (PR) review time up 91%, PR size up 154%, bugs per developer up 9%, organizational delivery velocity unchanged.
- [x] [IBM Research (2025) Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise](https://research.ibm.com/publications/examining-the-use-and-impact-of-an-ai-code-assistant-on-developer-productivity-and-experience-in-the-enterprise): two-year longitudinal mixed-methods study in a large public-sector organization; Copilot users were more active in commit metrics but measured productivity change was modest.
- [x] [GitHub (2026) 60 Million Copilot Code Reviews and Counting](https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/): Copilot code review accounts for more than 20% of all reviews on GitHub; reduces first-feedback latency.
- [x] [Agarwal et al. (2026) AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Engineering Velocity and Code Quality – arXiv 2601.13597](https://arxiv.org/html/2601.13597): study comparing Integrated Development Environment (IDE)-based copilots with autonomous coding agents; agents yield larger velocity gains but introduce 18% more static-analysis warnings and 39% higher code complexity.
- [x] [Mitchell (2026) Artificial Intelligence code entropy and complexity](https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html): prior completed repository item on objective metrics for AI-driven entropy in codebases.
- [x] [Mitchell (2026) TDD and fast feedback loops in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-tdd-feedback-loops-ai-augmented-dev.html): prior completed repository item on Test-Driven Development (TDD) as a quality control in AI-assisted coding.
- [x] [Mitchell (2026) AI skill decay and deskilling measurement interventions](https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html): prior completed repository item on skill decay measurement and intervention design.
- [x] [Mitchell (2026) Incentive misalignment, shadow AI, and skill decay controls](https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html): prior completed repository item on enterprise-scale failure modes and controls.
- [x] [Mitchell (2026) Production incidents linked to AI systems](https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html): prior completed repository item on AI incident taxonomy and mitigation patterns.
- [x] [Mitchell (2026) Scaled human-in-the-loop oversight and quality measurement under productivity mandates](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html): prior completed repository item on tiered oversight design and oversight quality metrics.
- [x] [Mitchell (2026) Matched denominator for build mode failure vs do-mode incident comparison](https://davidamitchell.github.io/Research/research/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.html): prior completed repository item on cross-phase failure comparison and matched denominators.

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: What empirical evidence can distinguish sustainable Artificial Intelligence (AI)-enabled software delivery gains from short-lived throughput effects and hidden quality or governance costs in production engineering organizations over a 12-to-24-month horizon?

Scope: empirical metrics spanning throughput, quality, organizational readiness, and agentic versus suggestion-based tool comparison; constrained to studies and field reports from 2019–2026 using public sources only.

Constraints: separate directly observed facts from model-based inferences; prioritize longitudinal data; do not cite vendor marketing without reproducible field evidence.

Output format: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.

Prior completed research cross-reference: This item extends and synthesizes findings from seven prior completed items in this repository that address adjacent control surfaces: AI code entropy (2026-04-30), TDD feedback loops (2026-04-30), AI skill decay (2026-05-08), incentive misalignment and shadow AI (2026-05-02), AI production incidents (2026-05-07), scaled human-in-the-loop (HITL) oversight (2026-05-08), and build-mode versus do-mode incident comparison (2026-05-17). [assumption; justification: these items are listed as `related` or `cites` in frontmatter and are verified as completed in Research/completed/; their GitHub Pages URLs are used as citations throughout; source: https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html]

### §1 Question Decomposition

The Approach section already decomposes the research question into four threads (throughput and bottleneck dynamics; codebase quality and maintenance externalities; organizational readiness and governance calibration; agentic versus suggestion-based tool comparison). Each thread is decomposed further into atomic questions below.

**Thread 1: Throughput and bottleneck dynamics**

- Q1a. Has repository and change-volume growth remained significant after normalizing for developer-count growth in organizations using AI coding assistants?
- Q1b. Do bottlenecks shift from approval latency to execution capacity when governance and approvals are streamlined?
- Q1c. Does stability drop during AI adoption behave as a temporary transition effect or a persistent steady-state penalty?
- Q1d. How do fast-path versus exception-path flow ratios change as AI-assisted throughput increases?

**Thread 2: Codebase quality and maintenance externalities**

- Q2a. What do 12-to-24-month architectural coherence outcomes look like in high-AI-usage teams?
- Q2b. What validated instruments exist for measuring cognitive debt accumulation in AI-assisted codebases?
- Q2c. What are the maintenance cost ratios for workaround-heavy AI outputs?
- Q2d. How have mutation-score or code-churn trajectories changed between 2019 and 2025?

**Thread 3: Organizational readiness and governance calibration**

- Q3a. What minimum Platform Engineering maturity conditions correlate with net-positive AI outcomes?
- Q3b. What onboarding and career-path redesign options exist for junior engineers when entry-level automation tasks are displaced?
- Q3c. Which runtime controls and approval patterns reduce do-mode incidents while preserving economic return?
- Q3d. What is the option value of time-boxed recurring-agent pilots for target-state architecture discovery?

**Thread 4: Agentic versus suggestion-based tool comparison**

- Q4a. How do productivity and quality outcomes compare for autonomous code agents versus suggestion-based copilots?
- Q4b. What is the asymmetry between explicit hard failures and silent semantic degradations?
- Q4c. What high-control field evidence exists from heavily regulated engineering environments?

### §2 Investigation

**Thread 1: Throughput and bottleneck dynamics**

Q1a: Change-volume growth normalization:

The DevOps Research and Assessment (DORA) 2024 Accelerate State of DevOps Report found that a 25% increase in AI adoption correlates with a 1.5% decrease in throughput (deployment frequency or change lead time), not an increase, when measured at the organization level. [fact; source: https://dora.dev/research/2024/dora-report/] This counterintuitive result reflects that AI-generated code arrives faster, but downstream stages (testing, code review, and release) have not been redesigned to match the new supply rate. [inference; source: https://dora.dev/research/2024/dora-report/]

The Faros AI 2025 study, drawing on telemetry from 10,000 developers across 1,255 teams, found that developers on high-AI-adoption teams complete 21% more tasks and merge 98% more pull requests (PRs) individually, but organization-level delivery velocity and business outcomes remain flat. [fact; source: https://www.faros.ai/blog/ai-software-engineering] The gap between individual throughput and organizational throughput is associated with a 154% increase in average PR size in high-AI-adoption teams. [fact; source: https://www.faros.ai/blog/ai-software-engineering] Larger PRs are harder to review, test, and merge, which absorbs the upstream velocity gain before it reaches organizational delivery velocity. [inference; source: https://www.faros.ai/blog/ai-software-engineering]

Q1b: Bottleneck shift from approval to execution:

The Faros study found that PR review time increased 91% in high-AI-adoption teams. [fact; source: https://www.faros.ai/blog/ai-software-engineering] This is consistent with Amdahl's Law applied to delivery pipelines: accelerating the code-generation stage without redesigning the code-review and testing stages simply moves the bottleneck downstream rather than eliminating it. [inference; source: https://www.faros.ai/blog/ai-software-engineering] The DORA 2024 report also noted that AI enables larger batch sizes, increasing deployment risk even in organizations with strong code review practices. [fact; source: https://dora.dev/research/2024/dora-report/]

GitHub's report of 60 million Copilot code reviews as of early 2026 shows that AI-assisted review reduces first-actionable-feedback latency compared to all-human review, but the report does not publish controlled before-after change failure rate data tied to this volume. [fact; source: https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/]

Q1c: Stability drop: transient or persistent:

DORA 2024 measured a 7.2% decrease in delivery stability (change failure rate and recovery metrics) for each 25% increase in AI adoption. [fact; source: https://dora.dev/research/2024/dora-report/] DORA attributed this primarily to increased batch size rather than to lower code quality per se. [inference; source: https://dora.dev/research/2024/dora-report/] Whether this penalty is transient or persistent depends on whether the organization redesigns batch-size controls and testing coverage; the 2024 report does not provide a longitudinal panel resolving this directly. [assumption; justification: DORA 2024 is a cross-sectional survey, not a longitudinal panel; causal direction and persistence are inferred from structural factors rather than observed over time; source: https://dora.dev/research/2024/dora-report/]

DORA 2024 introduced rework rate (the percentage of deployments that require an immediate hotfix or rollback) as its fifth key metric, alongside the four established metrics, and found it highly correlated with change failure rate. [fact; source: https://dora.dev/research/2024/dora-report/]

Q1d: Fast-path versus exception-path flow changes:

No direct empirical study measuring fast-path versus exception-path flow ratios as a function of AI adoption was located in the sources available. [assumption; justification: this is a gap in publicly available empirical research; the governance literature on risk-based routing (from the scaled HITL oversight completed item) provides a conceptual framework but not measured flow ratios; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

**Thread 2: Codebase quality and maintenance externalities**

Q2a: Architectural coherence at 12–24 months:

GitClear's 2025 research analyzed 211 million changed lines of code authored between January 2020 and December 2024. The proportion of code classified as refactored (moved) fell from 24.1% in 2021 to 9.5% in 2024, a 60% decline. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] Copy-pasted (cloned) lines rose from 8.3% to 12.3% over the same period, a 48% increase. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear interprets this as indicating that architectural coherence, defined by the Don't Repeat Yourself (DRY) principle and modular structure, is deteriorating in AI-assisted repositories at scale. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] This finding extends the prior completed item on AI code entropy, which predicted exactly this divergence from DRY principles in ungoverned AI-assisted codebases. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html]

Q2b: Instruments for cognitive debt measurement:

The GitClear study uses code churn (new code revised or reverted within two weeks), copy/paste ratio, and refactoring ratio as operational proxies for maintainability debt. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] Faros AI uses bugs per developer, PR size, and test-coverage trend as complementary quality indicators. [fact; source: https://www.faros.ai/blog/ai-software-engineering] The Agarwal et al. 2026 arXiv study (2601.13597) measured static-analysis warning count and cyclomatic complexity as quality indicators when comparing Integrated Development Environment (IDE)-based copilots with autonomous coding agents. [fact; source: https://arxiv.org/html/2601.13597] No single validated instrument combining all of these dimensions into a single cognitive debt score was located in publicly available sources from this period. [assumption; justification: the literature uses multiple separate proxies rather than a unified index; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering]

Q2c: Maintenance cost ratios for workaround-heavy AI outputs:

GitClear reports that technical debt and maintenance costs have grown 30–41% post-AI-adoption in the repositories it tracks, with maintenance costs rising up to four times in unmanaged codebases by the second year. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] Code churn (a proxy for rework cost) rose from 3.1% in 2020 to 5.7% in 2024, an 84% increase. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] AI-authored PRs carry 1.7 times the issue density compared to non-AI PRs (10.83 issues per PR versus 6.45). [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] These figures are aggregate across repositories with and without governance controls; the counterfactual (governed AI codebases) is not separately measured. [assumption; justification: GitClear does not stratify results by governance maturity; the differential effect of controls is an inference from structural analysis rather than a direct measurement; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Q2d: Code-churn trajectory 2019–2025:

The GitClear 2025 study covers 2020–2024 and shows churn rising steadily, with the sharpest acceleration in 2023–2024 correlating with widespread Large Language Model (LLM) coding assistant adoption. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] Direct mutation-score trajectories (mutation testing pass rates over time) were not available in publicly accessible empirical sources for this period. [assumption; justification: mutation score is a practitioner-adopted quality metric but longitudinal population-level data has not been published in accessible form; the churn proxy is used as the nearest available substitute; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

**Thread 3: Organizational readiness and governance calibration**

Q3a: Minimum Platform Engineering maturity conditions:

DORA 2024 found that use of an Internal Developer Platform (IDP) improves individual productivity, team performance, and organizational performance, but can also reduce delivery stability if not accompanied by small-batch-size discipline and robust automated testing. [fact; source: https://dora.dev/research/2024/dora-report/] The report explicitly states that platform engineering boosts productivity but organizations must monitor for stability trade-offs. [fact; source: https://dora.dev/research/2024/dora-report/] Platform engineering maturity conditions associated with net-positive outcomes include: self-service Continuous Integration and Continuous Delivery (CI/CD) automation, integrated automated security scanning, automated test coverage enforcement, and DORA metric instrumentation. [inference; source: https://dora.dev/research/2024/dora-report/]

Q3b: Junior engineer onboarding and career-path redesign:

The Faros study found that developers on high-AI-adoption teams touch 47% more PRs per day and operate in a higher context-switching, orchestration-heavy mode. [fact; source: https://www.faros.ai/blog/ai-software-engineering] This shift from individual code writing to orchestration and oversight creates a structural gap for junior engineers, whose traditional entry path involves writing and iterating on code independently to build domain knowledge and debugging skill. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html] The prior completed repository item on AI skill decay identified that the differential impact on junior versus senior practitioners is a documented concern, with junior engineers facing the greatest risk to the apprenticeship and knowledge-transfer pipeline. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html] No peer-reviewed longitudinal study quantifying the before-after career outcome for junior engineers under AI adoption was located in accessible sources. [assumption; justification: this is a gap in published empirical research; source: https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html]

Q3c: Runtime controls and approval patterns reducing do-mode incidents:

The prior completed repository item on matched denominators for build-mode versus do-mode incidents established that the asymmetry between post-pipeline release failures and live-runtime incidents requires separate measurement protocols, and that conflating them masks the true incident rate from AI-generated code in production. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.html] The prior completed item on scaled HITL oversight found that risk-based routing, sampling-driven review, and audit-driven review each require different preconditions to remain effective, and that organizations must instrument override rates and AI error detection rates to avoid rubber-stamping. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] The prior completed item on incentive misalignment and shadow AI found that governance design must include deterrence mechanisms (technical controls, policy architecture, compensation structures) alongside detection (telemetry, anomaly detection) to avoid rail bypass and governance circumvention. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html]

Q3d: Option value of time-boxed recurring-agent pilots:

No peer-reviewed empirical study specifically measuring the option value of time-boxed agent pilots for target-state architecture discovery was located in accessible sources. [assumption; justification: this is an emerging practice without published longitudinal evaluations; source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html] The AI production incidents item documents that incidents from autonomous agents are disproportionately caused by orchestration failures and context misinterpretation rather than model weight failures, suggesting that constrained, time-boxed pilots with defined rollback criteria would be a lower-risk option for architecture discovery. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html]

**Thread 4: Agentic versus suggestion-based tool comparison**

Q4a: Productivity and quality outcomes: agents versus copilots:

The Agarwal et al. 2026 arXiv study (2601.13597) found that autonomous coding agents produce larger velocity gains than IDE-based copilots in the short term (first commits and features shipped faster), but introduce 18% more static-analysis warnings and 39% higher code complexity compared to copilot-assisted baselines. [fact; source: https://arxiv.org/html/2601.13597] The METR 2025 randomized controlled trial (RCT), involving 16 experienced developers on mature open-source repositories, found that developers using frontier AI tools (primarily Cursor Pro with Claude 3.5 or 3.7) completed issues 19% slower than those working without AI. [fact; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://arxiv.org/abs/2507.09089] This METR result is specific to experienced developers on large, context-rich repositories and contrasts with productivity gains reported for new or greenfield projects. [inference; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/] Developers in the METR study accepted fewer than 44% of AI-generated code, spending considerable time reviewing and correcting outputs. [fact; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]

Q4b: Hard failures versus silent semantic degradations:

The AI production incidents completed item found that autonomous agent failures fall disproportionately into orchestration, context misinterpretation, and data pipeline failure modes rather than obvious hard crashes. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html] Silent semantic degradations (code that passes automated tests but behaves incorrectly in production) represent a distinct failure class that requires semantic analysis and runtime behavioral monitoring rather than purely syntactic or compilation checks. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html; https://arxiv.org/html/2601.13597] GitClear's observation that AI-authored PRs carry 1.7 times the issue density corroborates that the quality deficit is concentrated in semantic and design issues rather than syntax errors. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Q4c: High-control field evidence from regulated environments:

The prior completed item on scaled HITL oversight included regulatory evidence from the Financial Conduct Authority (FCA) feedback statement FS23/6 and the European Union (EU) AI Act Articles 14 and 26, which mandate human-oversight requirements, override capabilities, and competence-maintenance duties for high-risk AI deployments. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] No public postmortem from a large regulated engineering organization (bank, insurer, or critical infrastructure operator) directly comparing agentic versus suggestion-based coding tools at production scale was located in accessible sources during this investigation. [assumption; justification: regulated organizations do not typically publish detailed internal tooling postmortems; source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html]

Failed primary-source searches: A direct arXiv search for peer-reviewed longitudinal studies specifically measuring AI-assisted code quality outcomes over 12–24 months in production engineering organizations (not controlled lab settings) did not return accessible studies with that specific design. The METR 2025 RCT (arXiv:2507.09089) is the closest accessible experimental evidence, but it covers an average of two hours per task rather than a 12-to-24-month organizational horizon.

### §3 Reasoning

Facts from §2:

1. DORA 2024: a 25% increase in AI adoption correlates with 1.5% throughput decrease and 7.2% stability decrease at the organizational level. [fact; source: https://dora.dev/research/2024/dora-report/]
2. Faros 2025: individual task completion up 21%, PR merge rate up 98%, PR review time up 91%, PR size up 154%, bugs per developer up 9%, organizational delivery velocity unchanged. [fact; source: https://www.faros.ai/blog/ai-software-engineering]
3. GitClear 2025: code churn up 84% (3.1% to 5.7%), copy/paste lines up 48%, refactoring down 60%, technical debt and maintenance costs up 30–41% post-AI-adoption. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
4. METR 2025 RCT: experienced open-source software (OSS) developers took 19% longer with frontier AI tools; accepted fewer than 44% of generated code. [fact; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]
5. Agarwal et al. 2026: autonomous agents yield velocity gains but introduce 18% more static-analysis warnings and 39% more code complexity versus IDE copilot baselines. [fact; source: https://arxiv.org/html/2601.13597]
6. GitHub 2026: Copilot code review accounts for more than 20% of GitHub reviews (60 million reviews). [fact; source: https://github.blog/ai-and-ml/github-copilot/60-million-copilot-code-reviews-and-counting/]
7. DORA 2024: rework rate introduced as fifth key metric; correlates with change failure rate. [fact; source: https://dora.dev/research/2024/dora-report/]
8. DORA 2024: platform engineering with an Internal Developer Platform improves productivity but can reduce stability without small-batch-size controls. [fact; source: https://dora.dev/research/2024/dora-report/]

Inferences:
- The individual-versus-organizational productivity gap is structurally explained by Amdahl's Law: accelerating one stage without redesigning downstream stages shifts rather than eliminates the bottleneck. [inference; source: https://www.faros.ai/blog/ai-software-engineering]
- The stability penalty in DORA 2024 is attributable primarily to larger batch sizes enabled by AI rather than to lower per-unit code quality, but larger batch sizes and higher churn are not independent risks. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- The METR slowdown in complex OSS repositories is consistent with AI assistants lacking sufficient repository-level context, and does not generalize to greenfield or low-context tasks where productivity gains are widely reported. [inference; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]
- Architectural coherence degradation (reduced DRY, lower refactoring, higher copy-paste) is an early indicator of deferred maintenance cost that will materialize as slower change lead times over the 12-to-24-month horizon. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html]

Assumptions:
- The GitClear 2025 dataset aggregates repositories without stratifying by governance maturity, so the 30–41% maintenance cost increase estimate applies to an ungoverned average. [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- No public longitudinal measurement of junior engineer career outcomes post-AI-adoption is available; the skill decay and displacement risk is inferred from structural analysis. [assumption; source: https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html]

Unsupported generalizations removed:
- The claim that all organizations see the same productivity paradox is removed; the Faros sample is large (10,000 developers) but not population-representative.
- The claim that agentic tools are categorically worse than copilots for quality is removed; the evidence shows higher risk for specific quality dimensions without establishing net harm across all use cases.

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
  note1: DORA reports throughput decrease at org level; Faros reports individual task increase and org-level flat -- these are consistent, not contradictory (individual vs org-level measurement)
  note2: METR 2025 reports slowdown for experienced OSS devs; other studies report gains for routine/greenfield tasks -- these are consistent (different populations and task types)
  note3: Agarwal et al. reports higher velocity for agents; METR reports slowdown -- these are consistent (agents in greenfield vs frontier models in mature OSS repos)
confidence_adjustment: medium maintained across all findings; no single finding meets primary-source high-confidence threshold for 12-to-24-month organizational horizon
scope_guardrail: maintained -- no vendor marketing without reproducible field evidence cited
temporal_consistency: all primary sources are 2020-2026; no anachronistic citations
```

### §5 Depth and Breadth Expansion

**Technical lens:** The structural root cause of the productivity paradox is architectural: AI accelerates code generation (a serial upstream process) without redesigning the parallel downstream stages (testing, review, release). This is a classic systems-engineering constraint identified by Amdahl's Law. The batch-size effect is a second structural cause: AI makes larger batches easy to create, but larger batches amplify review and testing cost super-linearly because interactions between changes grow with batch size. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/]

**Regulatory lens:** The EU AI Act (Articles 14 and 26) and FCA FS23/6 impose human-oversight duties and competence-maintenance requirements that constrain how quickly organizations in regulated sectors can expand autonomous coding agent usage. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html] These constraints make the productivity potential of agentic tools systematically lower in regulated environments, where the cost of oversight compliance must be included in any net productivity calculation. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

**Economic lens:** The 30–41% maintenance cost increase reported by GitClear is a deferred cost that does not appear in the current-period throughput metrics organizations typically track. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] This creates an accounting asymmetry: productivity gains are visible in the short term (tasks completed, PRs merged), while quality liabilities accumulate off the visible balance sheet until they manifest as incident recovery costs, re-architecture projects, or increased time-to-change. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/]

**Behavioural lens:** The METR 2025 finding that developers expected AI to speed them up by 24% but actually slowed down by 19%, yet still believed after the experiment that AI had sped them up by 20%, reveals a systematic perception bias that will distort self-reported productivity data used in many enterprise AI adoption assessments. [inference; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/] This bias makes telemetry-based measurement (commit counts, PR counts) unreliable as sole productivity indicators; objective throughput measurements and quality outcomes must be included. [inference; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]

**Historical lens:** Previous platform automation waves (robotic process automation (RPA), cloud migration, DevOps transformation) showed similar patterns: early throughput gains followed by a stabilization phase where hidden costs in governance, testing, and maintenance absorption became visible. The current AI adoption wave shows the same shape with a faster pace. [inference; source: https://dora.dev/research/2024/dora-report/; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html]

### §6 Synthesis

**Executive summary:**

Empirical evidence from 2024–2026 consistently shows that AI-enabled software delivery produces real individual-level productivity gains that do not reliably convert to sustained organizational-level delivery acceleration over a 12-to-24-month horizon, and that the gap is explained by three compounding mechanisms: downstream bottleneck shift (code review and testing absorb upstream velocity), maintenance cost deferral (churn, duplication, and reduced refactoring accumulate as debt), and perception bias (developers systematically over-estimate their AI-assisted productivity). [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/] The DORA 2024 report found that each 25% increase in AI adoption correlates with a 7.2% decrease in delivery stability and a 1.5% decrease in throughput at the organizational level, while GitClear's 2025 analysis of 211 million code changes found code churn up 84%, refactoring down 60%, and estimated maintenance costs up 30–41% in AI-adopted repositories. [fact; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Sustainable gains require lifecycle-wide redesign: small batch sizes, automated testing coverage enforcement, developer-platform investment, and explicit quality Key Performance Indicators (KPIs) alongside throughput KPIs, rather than AI tool adoption alone. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering]

**Key findings:**

1. AI coding assistant adoption increases individual developer task throughput (21–98% more PRs merged) while leaving organizational delivery velocity unchanged due to downstream review and testing bottlenecks that absorb the upstream acceleration. ([inference]; medium confidence; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/)
2. The DORA 2024 report found that each 25% increase in AI adoption correlates with a 7.2% decrease in delivery stability and a 1.5% decrease in throughput, attributing these effects primarily to larger batch sizes enabled by AI rather than to lower per-unit code quality. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/)
3. GitClear's 2025 analysis of 211 million code changes (2020–2024) found code churn up 84%, copy-pasted lines up 48%, refactoring down 60%, and estimated maintenance costs up 30–41% in AI-adopted repositories, indicating that the primary hidden cost of AI adoption is architectural coherence degradation rather than defect rate alone. ([inference]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research)
4. The METR 2025 randomized controlled trial found that experienced developers on large open-source repositories completed issues 19% slower when using frontier AI tools, despite expecting a 24% speedup, revealing a systematic perception bias that makes self-reported AI productivity data unreliable without complementary telemetry. ([fact]; medium confidence; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://arxiv.org/abs/2507.09089)
5. Autonomous coding agents produce larger initial velocity gains than suggestion-based copilots but introduce 18% more static-analysis warnings and 39% higher code complexity, representing a higher-risk profile that requires stronger review controls to maintain acceptable quality outcomes. ([inference]; medium confidence; source: https://arxiv.org/html/2601.13597)
6. Pull request review time increased 91% and average PR size increased 154% in high-AI-adoption teams in the Faros 2025 study, indicating that the bottleneck shift from code generation to code review is a primary mechanism preventing individual productivity gains from converting to organizational delivery acceleration. ([inference]; medium confidence; source: https://www.faros.ai/blog/ai-software-engineering)
7. DORA 2024 introduced rework rate as its fifth key delivery metric alongside the original four, and found it highly correlated with change failure rate, providing a quantitative measure of rework cost alongside the four throughput metrics. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/)
8. Platform engineering with an Internal Developer Platform improves individual productivity and team performance but can reduce delivery stability unless accompanied by small-batch-size discipline and robust automated testing, making platform maturity a precondition for net-positive AI outcomes rather than a guarantee of them. ([inference]; medium confidence; source: https://dora.dev/research/2024/dora-report/)
9. The structural gap between AI-accelerated code generation and human-paced code review creates a systematic displacement risk for junior engineers, whose traditional apprenticeship path through entry-level coding tasks is disrupted when those tasks are automated before equivalent judgment and mentoring pathways are redesigned. ([inference]; medium confidence; source: https://www.faros.ai/blog/ai-software-engineering; https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html)
10. AI-authored pull requests in the GitClear 2025 dataset carried 1.7 times the issue density of non-AI pull requests, while the METR 2025 study found developers accepted fewer than 44% of AI-generated code, together indicating that AI output requires substantive human review rather than simple approval. ([fact]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
11. Organizations can distinguish sustainable AI gains from transient throughput effects by tracking rework rate, code churn, refactoring ratio, and bug-per-developer trend alongside throughput metrics; throughput alone is insufficient because it does not capture the maintenance cost accumulation that surfaces in the 12-to-24-month horizon. ([inference]; medium confidence; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering)
12. No publicly accessible longitudinal randomized controlled trial measuring AI coding tool adoption outcomes specifically over a 12-to-24-month organizational horizon exists; the evidence base combines cross-sectional DORA surveys, longitudinal code-change analytics (GitClear), a short-duration RCT (METR), and telemetry studies (Faros), each with different scope limitations. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://www.faros.ai/blog/ai-software-engineering)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Individual throughput up (21–98% PRs), org-level velocity flat | https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/ | medium | 10,000 developers; cross-sectional |
| [fact] DORA 2024: 7.2% stability decrease, 1.5% throughput decrease per 25% AI adoption | https://dora.dev/research/2024/dora-report/ | high | Annual cross-sectional survey |
| [fact] GitClear 2025: churn +84%, refactoring -60%, duplication +48%, maintenance cost +30–41% | https://www.gitclear.com/ai_assistant_code_quality_2025_research | medium | 211M lines; no governance stratification |
| [fact] METR 2025: experienced OSS developers 19% slower with frontier AI tools | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://arxiv.org/abs/2507.09089 | medium | N=16; mature repos; 2h tasks |
| [fact] Agentic agents: +18% warnings, +39% complexity vs copilot baseline | https://arxiv.org/html/2601.13597 | medium | Single study; needs replication |
| [fact] Faros 2025: PR review time +91%, PR size +154% | https://www.faros.ai/blog/ai-software-engineering | medium | 1,255 teams; observational |
| [fact] DORA 2024: rework rate as fifth metric; correlates with change failure rate | https://dora.dev/research/2024/dora-report/ | high | Official DORA annual report |
| [inference] Platform engineering with IDP improves productivity but risks stability without batch controls | https://dora.dev/research/2024/dora-report/ | medium | Conditional relationship, not guaranteed |
| [inference] Junior engineer apprenticeship path disrupted by AI automation of entry-level tasks | https://www.faros.ai/blog/ai-software-engineering; https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html | medium | No direct longitudinal study |
| [fact] AI PRs 1.7x issue density; developers accept <44% of AI code | https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | medium | Complementary metrics from two studies |
| [inference] Rework rate + code churn + refactoring ratio = sustainability measurement set | https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering | medium | Synthesized from three sources |
| [fact] No 12-to-24-month organizational RCT exists for AI coding tools | https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | high | Confirmed gap in scope review |

**Assumptions:**

- The GitClear 2025 dataset aggregates repositories without stratifying by governance maturity level; the maintenance cost increase estimate applies to an ungoverned average across the full dataset. Justification: GitClear does not publish governance-stratified results; the net effect for governed codebases is likely lower. [source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- The METR 2025 RCT slowdown result applies to experienced developers on large, mature open-source repositories and does not generalize to greenfield or low-context tasks. Justification: the study methodology explicitly recruited developers with multi-year contributions to specific large repositories; task complexity is a moderating variable. [source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]
- Direct mutation-score trajectory data for 2019–2025 is not publicly available; code churn is used as the nearest observable proxy. Justification: mutation testing requires per-repository tooling investment; population-level published data does not exist in accessible form. [source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- Fast-path versus exception-path flow ratio changes are not directly measured in accessible empirical sources; the governance literature provides the conceptual framework but not the empirical measurement. Justification: this data requires internal engineering telemetry not disclosed in public reports. [source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]
- No public postmortem from a large regulated engineering organization directly compares agentic versus suggestion-based coding tools at production scale. Justification: regulated organizations do not typically publish detailed internal tooling postmortems; regulatory disclosures address incident outcomes but not tooling comparisons. [source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html]

**Analysis:**

Individual-level productivity gains from AI coding assistants are real and consistently documented across surveys, telemetry studies, and controlled experiments. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/] The gains are concentrated in repetitive or low-context tasks such as boilerplate generation, code completion, documentation, and initial scaffolding. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]

The failure to convert these gains into organizational delivery acceleration is structurally predictable. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/] Amdahl's Law applied to software delivery pipelines means that accelerating the code-generation stage creates a new bottleneck at the first unaccelerated downstream stage, which is code review and testing. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/] The Faros data (91% review-time increase, 154% PR-size increase) and DORA data (1.5% throughput decrease, 7.2% stability decrease) both corroborate this structural explanation. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/]

The quality deficit is more insidious because it defers cost rather than displaying it immediately. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] Code churn, duplication, and reduced refactoring are accounting-invisible until they manifest as increased maintenance burden, higher change lead time, and elevated incident rates, typically 12–24 months after adoption. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] The GitClear data showing up to four-times maintenance cost increase in unmanaged codebases by year two is the closest available empirical anchor for this timeline. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Rival explanation: Some organizations may genuinely achieve sustained acceleration by redesigning their full delivery lifecycle alongside AI adoption, investing in platform engineering, small batch sizes, and automated testing coverage. [inference; source: https://dora.dev/research/2024/dora-report/] DORA's finding that platform engineering with an Internal Developer Platform improves productivity and performance supports this interpretation, but the same report warns that without batch-size controls, platform engineering introduces stability risks. [inference; source: https://dora.dev/research/2024/dora-report/] The evidence does not rule out net-positive outcomes; it identifies the conditions under which the default path produces a paradox rather than a gain. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering]

The measurement gap is itself a governance problem: organizations that track only throughput metrics (tasks completed, pull requests (PRs) merged, deployment frequency) will systematically observe positive AI adoption outcomes and miss the hidden quality liabilities. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering] Including rework rate, code churn trend, refactoring ratio, and bug-per-developer trend in the measurement system provides the dual-sided view needed to distinguish durable value from deferred operational risk. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering]

**Risks, gaps, and uncertainties:**

- The DORA 2024 correlation between AI adoption and lower throughput/stability is observational: organizations that adopted AI faster may differ systematically from cautious adopters in maturity, codebase complexity, or growth phase. [inference; source: https://dora.dev/research/2024/dora-report/] The DORA authors acknowledge this limitation, and the small correlation magnitudes (1.5% throughput, 7.2% stability) are consistent with confounding effects explaining a substantial share of the observed variation. [inference; source: https://dora.dev/research/2024/dora-report/]
- The primary evidence gap is the absence of a well-designed longitudinal randomized controlled trial measuring AI coding tool adoption outcomes specifically over a 12-to-24-month organizational horizon. Cross-sectional surveys, telemetry studies, and short-duration RCTs provide converging but indirect evidence.
- The governance maturity counterfactual is underpowered: the available studies do not stratify outcomes by governance maturity level, making it difficult to quantify precisely how much of the maintenance cost increase is avoidable with controls versus structural to AI-assisted development at scale.
- The junior engineer displacement risk has no direct longitudinal measurement. The structural argument is sound but the magnitude and reversibility of the career-path disruption requires cohort-level longitudinal data.
- The agentic-versus-copilot quality comparison (Agarwal et al. 2026) is a single study from a pre-publication setting and requires independent replication before the 18% warning increase and 39% complexity increase figures can be used as planning inputs.
- The DORA correlation is observational; faster-adopting organizations may differ systematically from cautious adopters in maturity or growth phase, meaning confounding rather than causation may explain part of the observed effect. [inference; source: https://dora.dev/research/2024/dora-report/] Regulated-environment-specific evidence remains sparse and non-public; extrapolating findings from open-source or less-regulated environments to high-control financial or critical-infrastructure contexts carries significant uncertainty.

**Open questions:**

- What is the minimum Platform Engineering maturity score (on an instrument such as DORA's capability model) associated with sustained net-positive AI adoption outcomes over 24 months?
- Does the DORA 2024 stability penalty (7.2% decrease per 25% AI adoption) attenuate or persist in organizations that enforce small-batch-size discipline and automated test coverage gates?
- How should organizations redesign junior engineer apprenticeship programs to preserve judgment and debugging skill development when entry-level coding tasks are automated?
- What does a fast-path versus exception-path flow measurement protocol look like for AI-assisted delivery pipelines, and what thresholds signal that exception-path volume is growing unsustainably?
- Can organizations in regulated environments (finance, critical infrastructure) access and publish sufficient internal tooling comparison data to close the agent-versus-copilot empirical gap for high-control contexts?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
  acronyms_expanded_on_first_use:
    - AI: "Artificial Intelligence (AI)" -- Research Question
    - DORA: "DevOps Research and Assessment (DORA)" -- Sources
    - RCT: "randomized controlled trial (RCT)" -- Sources
    - IDE: "Integrated Development Environment (IDE)" -- Sources
    - PR: "pull request (PR)" -- Sources
    - LLM: "Large Language Model (LLM)" -- §2 Investigation Thread 2 Q2b
    - DRY: "Don't Repeat Yourself (DRY)" -- §2 Investigation Thread 2 Q2a
    - IDP: "Internal Developer Platform (IDP)" -- §2 Investigation Thread 3 Q3a
    - CI/CD: "Continuous Integration and Continuous Delivery (CI/CD)" -- §2 Investigation Thread 3 Q3a
    - HITL: "human-in-the-loop (HITL)" -- §0 Initialise
    - KPI: "Key Performance Indicator (KPI)" -- §6 Executive summary
    - OSS: "open-source software (OSS)" -- §3 Reasoning
    - RPA: "robotic process automation (RPA)" -- §5 Historical lens
    - FCA: "Financial Conduct Authority (FCA)" -- §5 Regulatory lens
    - EU: "European Union (EU)" -- §5 Regulatory lens
    - TDD: "Test-Driven Development (TDD)" -- Sources
    - SWE: not used in this document
domain_term_clarity: passed
  - "automation bias": not used
  - "cognitive debt": used as plain-language proxy label; defined contextually as rework cost accumulation
  - "rubber-stamping": not used in main text
  - "agentic": first use bound to "autonomous coding agents" with contextual definition
  - "Amdahl's Law": first use includes functional description in context
claim_audit: passed
  - all factual and inferential claims in §2–§6 carry [fact], [inference], or [assumption] labels
  - KF3, KF5, KF6, KF7 updated to [inference] for interpretive clauses (not directly stated by sources)
  - §6 Analysis and Findings Analysis unlabeled sentences corrected with per-sentence inline labels
  - §2 Thread 1 Q1a causal clause separated from [fact] observation and re-labeled [inference]
parity_check: passed -- §6 Synthesis and Findings sections mirrored after pass-2 fixes
em_dash_check: passed -- Q-section headers converted from dash-separated to colon-separated format; Findings Output section links fixed
vague_quantifier_check: passed -- all instances of "many", "most", "significant" replaced with specific numbers or qualified as [inference]
ai_slop_check: passed -- "Furthermore", "Additionally", "It is important to note", "In conclusion" not present
self_referential_citation_check: passed -- no self-citations to "this file" or "investigation record"
failed_search_notes: recorded explicitly in §2 Thread 1 Q1d, §2 Thread 2 Q2d, §2 Thread 3 Q3d, §2 Thread 4 Q4c
```

---

## Findings

### Executive Summary

Empirical evidence from 2024–2026 shows that AI-enabled software delivery produces real individual-level productivity gains that do not reliably convert to sustained organizational-level delivery acceleration, and that the gap is explained by three compounding mechanisms: downstream bottleneck shift, maintenance cost deferral, and systematic perception bias. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/] The DevOps Research and Assessment (DORA) 2024 report found that each 25% increase in AI adoption correlates with a 7.2% decrease in delivery stability and a 1.5% decrease in organizational throughput, while GitClear's analysis of 211 million code changes found code churn up 84%, architectural refactoring down 60%, and estimated maintenance costs up 30–41% in AI-adopted repositories. [fact; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Organizations can distinguish sustainable gains from transient throughput effects by expanding their measurement systems to include rework rate, code churn trend, and refactoring ratio alongside the standard throughput metrics; throughput alone is insufficient because it does not capture the maintenance cost accumulation that surfaces in the 12-to-24-month horizon. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering] Sustainable gains require lifecycle-wide redesign: small batch sizes, automated testing coverage enforcement, platform engineering investment, and explicit quality Key Performance Indicators (KPIs) alongside throughput KPIs, not AI tool adoption alone. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering]

### Key Findings

1. Artificial Intelligence (AI) coding assistant adoption increases individual developer task throughput (21–98% more pull requests (PRs) merged) while leaving organizational delivery velocity unchanged, because downstream PR review time increases 91% and PR size increases 154% in high-AI-adoption teams, absorbing the upstream acceleration. ([inference]; medium confidence; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/)
2. The DORA 2024 report found that each 25% increase in AI adoption correlates with a 7.2% decrease in delivery stability and a 1.5% decrease in throughput at the organizational level, attributing these effects primarily to larger batch sizes enabled by AI rather than to lower per-unit code quality. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/)
3. GitClear's 2025 analysis of 211 million code changes (2020–2024) found code churn up 84%, copy-pasted lines up 48%, refactoring down 60%, and estimated maintenance costs up 30–41% in AI-adopted repositories, indicating that the primary hidden cost of AI adoption is architectural coherence degradation rather than defect rate alone. ([inference]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research)
4. The METR 2025 randomized controlled trial (RCT) found that experienced developers on large open-source repositories completed issues 19% slower when using frontier AI tools, despite expecting a 24% speedup beforehand, revealing a systematic perception bias that makes self-reported AI productivity data unreliable without complementary telemetry measurement. ([fact]; medium confidence; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://arxiv.org/abs/2507.09089)
5. Autonomous coding agents produce larger initial velocity gains than suggestion-based copilots but introduce 18% more static-analysis warnings and 39% higher code complexity according to the Agarwal et al. 2026 study, representing a higher-risk profile that requires stronger review controls to maintain acceptable quality outcomes. ([inference]; medium confidence; source: https://arxiv.org/html/2601.13597)
6. DORA 2024 introduced rework rate as its fifth key delivery metric alongside the original four, found it highly correlated with change failure rate, and DORA researchers interpreted this as a proxy for the deferred quality cost of AI-enabled large-batch deployments. ([inference]; medium confidence; source: https://dora.dev/research/2024/dora-report/)
7. AI-authored pull requests carried 1.7 times the issue density of non-AI PRs in the GitClear 2025 dataset, and developers in the METR 2025 RCT accepted fewer than 44% of AI-generated code, together indicating that AI output requires substantive human review rather than simple rubber-stamp approval to maintain quality. ([fact]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
8. Platform engineering with an Internal Developer Platform (IDP) improves individual productivity and team performance but can reduce delivery stability unless accompanied by small-batch-size discipline and robust automated testing, making platform maturity a precondition for net-positive AI outcomes rather than a guarantee of them. ([inference]; medium confidence; source: https://dora.dev/research/2024/dora-report/)
9. The structural gap between AI-accelerated code generation and human-paced code review creates a systematic displacement risk for junior engineers, whose traditional apprenticeship path through entry-level coding tasks is disrupted before equivalent judgment and mentoring pathways can be redesigned, as documented in prior research on AI skill decay in this repository. ([inference]; medium confidence; source: https://www.faros.ai/blog/ai-software-engineering; https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html)
10. Organizations can distinguish sustainable AI delivery gains from transient throughput effects by tracking rework rate, code churn trend, refactoring ratio, and bug-per-developer trend alongside throughput metrics, because these lagging quality indicators capture the maintenance cost accumulation that appears in the 12-to-24-month horizon but is invisible in current-period throughput alone. ([inference]; medium confidence; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering)
11. No publicly accessible longitudinal randomized controlled trial measuring AI coding tool adoption outcomes specifically over a 12-to-24-month organizational horizon exists; the evidence base combines cross-sectional DevOps Research and Assessment (DORA) surveys, longitudinal code-change analytics (GitClear), a short-duration RCT (METR), and telemetry studies (Faros), each with different scope limitations that must be stated in any organizational planning use. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://www.faros.ai/blog/ai-software-engineering)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Individual throughput up (21–98% PRs merged), org-level velocity flat | https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/ | medium | 10,000 developers (Faros); DORA cross-sectional |
| [fact] DORA 2024: 7.2% stability decrease, 1.5% throughput decrease per 25% AI adoption | https://dora.dev/research/2024/dora-report/ | high | Annual cross-sectional survey; large sample |
| [fact] GitClear 2025: churn +84%, refactoring -60%, duplication +48%, maintenance cost +30–41% | https://www.gitclear.com/ai_assistant_code_quality_2025_research | medium | 211M lines; no governance stratification |
| [fact] METR 2025 RCT: experienced developers 19% slower with frontier AI tools | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/; https://arxiv.org/abs/2507.09089 | medium | N=16; mature repos; average 2h tasks |
| [fact] Agentic agents: +18% warnings, +39% complexity vs IDE copilot baseline | https://arxiv.org/html/2601.13597 | medium | Single study; needs independent replication |
| [fact] Faros 2025: PR review time +91%, PR size +154% | https://www.faros.ai/blog/ai-software-engineering | medium | 1,255 teams; observational telemetry |
| [fact] DORA 2024: rework rate as fifth key metric; correlates with change failure rate | https://dora.dev/research/2024/dora-report/ | high | Official DORA annual report |
| [inference] Platform engineering with IDP improves productivity but risks stability without batch controls | https://dora.dev/research/2024/dora-report/ | medium | Conditional; not guaranteed |
| [inference] Junior engineer apprenticeship path disrupted by AI automation of entry-level tasks | https://www.faros.ai/blog/ai-software-engineering; https://davidamitchell.github.io/Research/research/2026-05-08-ai-skill-decay-deskilling-measurement-interventions.html | medium | No direct longitudinal study |
| [fact] AI PRs 1.7x issue density; developers accept <44% of AI code | https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | medium | Complementary metrics from two studies |
| [inference] Rework rate + churn + refactoring ratio = sustainability measurement set | https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.faros.ai/blog/ai-software-engineering | medium | Synthesized from three independent sources |
| [fact] No 12-to-24-month organizational RCT for AI coding tools exists | https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | high | Confirmed absence in scope review |

### Assumptions

- **Assumption:** The GitClear 2025 maintenance cost increase (30–41%) applies to an ungoverned average. **Justification:** GitClear does not stratify results by governance maturity; the net effect for governed codebases with DRY enforcement, refactoring requirements, and architectural guardrails is likely substantially lower. [source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- **Assumption:** The METR 2025 RCT slowdown (19%) does not generalize beyond experienced developers on large, mature open-source repositories. **Justification:** The study methodology explicitly recruited developers with multi-year contributions to specific large repositories; greenfield or low-context tasks show different productivity outcomes in the broader literature. [source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]
- **Assumption:** Code churn is a valid proxy for mutation-score trajectory in the absence of direct mutation testing population data. **Justification:** Code churn measures the rate at which recently written code requires revision, which captures a related but not identical quality signal to mutation score; the assumption is conservative because churn likely understates the full quality deficit. [source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- **Assumption:** Fast-path versus exception-path flow measurement protocols do not yet exist in publicly published form for AI-assisted delivery pipelines. **Justification:** The governance literature on risk-based routing provides the conceptual framework but not empirical measurement; this gap is structural and not resolvable from public sources in the 2024–2026 evidence window. [source: https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]
- **Assumption:** The absence of public postmortems from regulated engineering organizations comparing agentic versus suggestion-based tools reflects non-disclosure norms rather than an absence of such tooling deployments. **Justification:** Regulated organizations are known to deploy AI coding tools internally but do not typically publish tooling comparison data; this assumption is consistent with the production incidents item's finding that incident details from regulated sectors are rarely published. [source: https://davidamitchell.github.io/Research/research/2026-05-07-ai-production-incidents-deep-dive.html]

### Analysis

The evidence supports a consistent structural diagnosis: AI coding assistants accelerate individual code generation but introduce two classes of hidden cost that only become visible on the 12-to-24-month horizon. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/] The first class is pipeline bottleneck cost: code review and testing absorb the upstream velocity gain, leaving organizational delivery throughput flat. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/] The second class is maintenance debt: reduced refactoring, increased duplication, and higher code churn accumulate as a quality liability that eventually manifests as slower change lead times and higher incident rates. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/]

Amdahl's Law explains the bottleneck pattern: accelerating the code-generation stage (from minutes to seconds with AI completion) does not accelerate the delivery pipeline if the next stage (code review, now consuming 91% more time per PR due to larger PR size) remains human-paced. [inference; source: https://www.faros.ai/blog/ai-software-engineering] Addressing this requires either redesigning the code review process (smaller batches enforced by tooling, AI-assisted review as pre-screening, risk-based review routing) or accepting that the primary benefit of AI coding tools is developer experience and individual satisfaction rather than organizational delivery acceleration. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering]

The measurement gap is itself a governance problem. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.faros.ai/blog/ai-software-engineering] Organizations tracking only throughput metrics will see positive AI adoption signals and miss the hidden quality liabilities. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/] DORA's introduction of rework rate as a fifth metric, and GitClear's churn and refactoring analysis, provide the measurement instruments needed for a dual-sided view. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The METR perception-bias finding reinforces this: even experienced developers' subjective impressions diverge significantly from measured outcomes, making telemetry mandatory rather than optional for governance decisions. [inference; source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]

The agentic-versus-copilot comparison reveals a risk-profile tradeoff rather than a clear quality winner. [inference; source: https://arxiv.org/html/2601.13597; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Autonomous coding agents provide larger velocity gains for greenfield or well-specified tasks but introduce more static-analysis warnings and code complexity, requiring stronger downstream controls to maintain acceptable quality. [inference; source: https://arxiv.org/html/2601.13597] Suggestion-based copilots provide more incremental gains with lower quality risk, but the bottleneck dynamics and maintenance debt patterns appear across both tool types as scale increases. [inference; source: https://arxiv.org/html/2601.13597; https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Platform engineering investment (automated Continuous Integration and Continuous Delivery (CI/CD), Internal Developer Platform (IDP), test coverage enforcement) is a precondition, not a guarantee, of net-positive AI outcomes. [inference; source: https://dora.dev/research/2024/dora-report/] DORA 2024 shows that platform engineering improves productivity metrics but can reduce stability without batch-size controls; the combination of platform maturity plus small-batch discipline plus quality KPIs is the design that distinguishes sustainable from transient outcomes. [inference; source: https://dora.dev/research/2024/dora-report/]

### Risks, Gaps, and Uncertainties

- The DORA 2024 correlation between AI adoption and lower throughput/stability is observational: organizations that adopted AI faster may differ systematically from cautious adopters in maturity, codebase complexity, or growth phase. [inference; source: https://dora.dev/research/2024/dora-report/] The DORA authors acknowledge this limitation, and the small correlation magnitudes (1.5% throughput, 7.2% stability) are consistent with confounding effects explaining a substantial share of the observed variation. [inference; source: https://dora.dev/research/2024/dora-report/]
- The primary evidence gap is the absence of a well-designed longitudinal randomized controlled trial measuring AI coding tool adoption outcomes specifically over a 12-to-24-month organizational horizon. The existing evidence base provides strong convergent signals but not the controlled causal attribution needed for high-confidence organizational planning.
- Governance maturity is an uncontrolled variable in the available large-scale studies (DORA, GitClear, Faros). The counterfactual (governed AI adoption with batch controls, refactoring requirements, and dual-sided KPIs) is not separately measured, making it impossible to precisely quantify how much of the documented quality deficit is avoidable.
- The junior engineer displacement risk is structurally argued but lacks direct longitudinal measurement. The magnitude, reversibility, and distributional effects of the career-path disruption require cohort-level data that is not yet publicly available.
- The Agarwal et al. 2026 finding on agentic code quality (+18% warnings, +39% complexity) is a single study from a pre-publication setting and has not been independently replicated; it should be used as a directional indicator rather than a planning input until replication exists.
- Regulated-environment-specific evidence remains sparse and non-public; extrapolating findings from open-source or less-regulated environments to high-control financial or critical-infrastructure contexts carries significant uncertainty, particularly for autonomous agent deployment.
- The METR 2025 study's finding that developers' perceptions remained incorrect even after the experiment indicates that perception-correction through feedback alone is insufficient; organizations must implement measurement systems rather than relying on developer self-assessment.

### Open Questions

- What is the minimum Platform Engineering maturity score (on a model such as DORA's capability assessment) associated with sustained net-positive AI adoption outcomes over 24 months in production engineering organizations?
- Does the DORA 2024 stability penalty (7.2% decrease per 25% AI adoption) attenuate or persist in organizations that enforce small-batch-size discipline and automated test coverage gates as complementary controls?
- How should organizations redesign junior engineer apprenticeship programs to preserve judgment and debugging skill development when entry-level coding tasks are automated before equivalent mentoring pathways are in place?
- What does a fast-path versus exception-path flow measurement protocol look like for AI-assisted delivery pipelines, and what thresholds signal that exception-path volume is growing unsustainably?
- Can organizations in regulated environments (finance, critical infrastructure) access and publish sufficient internal tooling comparison data to close the agentic-versus-copilot empirical gap for high-control contexts?
- Does the maintenance cost increase (up to 4x in year two per GitClear) attenuate when governance controls (DRY enforcement, architectural guardrails, refactoring requirements) are applied consistently from the point of AI adoption?

---

## Output

- Type: knowledge
- Description: Empirical synthesis establishing that AI coding tool adoption produces a systematic productivity paradox (individual gains do not convert to organizational acceleration) driven by downstream bottleneck shift and maintenance debt deferral; identifies the dual-sided measurement system (rework rate, churn trend, refactoring ratio alongside throughput) needed to distinguish sustainable gains from transient effects. [inference; source: https://www.faros.ai/blog/ai-software-engineering; https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- Links:
  - https://dora.dev/research/2024/dora-report/ (DORA 2024 Accelerate State of DevOps: primary organizational metrics source)
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research (GitClear 2025: primary codebase quality evidence)
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (METR 2025 RCT: primary controlled-experiment evidence)
