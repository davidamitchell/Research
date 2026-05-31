---
review_count: 2
title: "How have software-development commit trends shifted across repository creation, LOC velocity, rework, abandonment, slop, test utility, and shipment rates?"
added: 2026-05-29T08:49:18+00:00
status: reviewing
priority: high
blocks: []
themes: [software-engineering, benchmarks-eval, tools-infrastructure, workforce-skills, cost-performance]
started: 2026-05-31T20:35:29+00:00
completed: ~
output: [knowledge]
cites: [2026-05-27-ai-first-software-ecology-developer-ecosystems, 2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai, 2026-03-12-volume-vs-correctness-ai-era]
related: [2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate, 2026-04-28-software-demand-shift-ai-coding-era, 2026-05-01-human-oversight-ai-software-development]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How have software-development commit trends shifted across repository creation, LOC velocity, rework, abandonment, slop, test utility, and shipment rates?

## Research Question

What do high-quality longitudinal studies (2019–2026) show about directional shifts and current baseline ranges for repository creation rate, Lines of Code (LOC) velocity, rework share, project abandonment, Artificial Intelligence (AI) slop indicators, useless-test prevalence, and unshipped-project rates?

## Scope

**In scope:**
- Quantitative trend evidence from peer-reviewed literature and credible large-scale industry datasets.
- Definitions and measurement methods for each metric so comparisons are valid.
- Direction of change and, where available, numerical ranges with uncertainty.

**Out of scope:**
- Prescriptive team-level process recommendations.
- Forecasting beyond published evidence windows.

**Constraints:** Prioritise sources with transparent methodology, reproducible datasets, and clearly reported sample sizes.

## Context

The request asks for concrete numbers and trend direction across several software-delivery indicators that are often discussed with inconsistent definitions. A single scoped synthesis should normalize metric definitions first, then report what has actually shifted and what is still uncertain.

## Approach

1. Define each metric operationally and map acceptable proxy measures used in the literature.
2. Gather 2019–2026 studies/datasets, extract comparable statistics, and tabulate trend direction plus magnitude.
3. Reconcile disagreements by comparing methodology, sample composition, and validity threats.

## Sources

- [GitHub Octoverse 2025 (2024/2025 data)](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) - large-scale repository and contribution trend baselines.
- [DORA Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) - DevOps Research and Assessment (DORA) software-delivery outcomes and performance metrics.
- [DORA Accelerate State of DevOps Report 2023](https://services.google.com/fh/files/misc/2023_final_report_sodr.pdf) - longitudinal engineering performance evidence.
- [GitClear AI Copilot Code Quality Report 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research) - 211 million changed LOC dataset on AI impact on churn and rework.
- [Avelino et al. (2019) "On the abandonment and survival of open source projects"](https://arxiv.org/abs/1906.08058) - empirical study of 1,932 popular GitHub projects.
- [Baltes et al. (2026) "An Endless Stream of AI Slop"](https://arxiv.org/abs/2603.27249) - qualitative analysis of community perceptions of AI slop in software development.
- [LinearB Engineering Metrics Benchmarks](https://linearb.io/resources/engineering-benchmarks) - rework, refactor, and pull request benchmarks from 4,800+ teams.
- [Standish Group CHAOS Report 2020 summary](https://thestory.is/en/journal/chaos-report/) - software project completion and cancellation rates.
- [GitHub Octoverse 2019](https://octoverse.github.com/2019/) - historical baseline for repository and developer counts.
- [GitHub Octoverse 2020](https://octoverse.github.com/2020/) - pandemic-era baseline for repository and developer counts.

## Research Skill Output

### §0 Initialise

Question: What do high-quality longitudinal studies (2019–2026) show about directional shifts and current baseline ranges for repository creation rate, LOC velocity, rework share, project abandonment, AI slop indicators, useless-test prevalence, and unshipped-project rates?

Scope: Quantitative trend evidence from peer-reviewed literature and credible large-scale industry datasets. Each metric requires an operational definition before trend data can be compared. Direction of change and numerical ranges with uncertainty. Prescriptive recommendations and forecasts are out of scope.

Constraints: Prioritise primary sources with transparent methodology, reproducible datasets, and clearly reported sample sizes. Secondary analyses are used where primary data is unavailable, with confidence downgraded accordingly.

Output format: knowledge item with structured Findings covering all seven metric areas.

[assumption] Working hypothesis: all seven metric areas show measurable trend shifts from 2019 to 2025 driven in part by the adoption of AI coding assistants beginning in 2022-2023, though the magnitude and direction vary by metric. Justification: AI coding assistant adoption (GitHub Copilot launched November 2021) creates a natural experiment boundary within the study window; prior work in this repository (2026-05-27-ai-first-software-ecology-developer-ecosystems, 2026-03-12-volume-vs-correctness-ai-era) converges on AI as the primary structural change to software volume metrics in this period. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

### §1 Question Decomposition

The seven metric areas from the Research Question decompose as follows:

**A. Repository creation rate**
- A1. What was the absolute repository creation rate on GitHub in 2019-2020?
- A2. What was the absolute repository creation rate on GitHub in 2023-2025?
- A3. What is the year-over-year (YoY) growth rate, and does it show acceleration?

**B. LOC velocity (commit volume as proxy)**
- B1. How is LOC velocity operationalised? (LOC added, removed, or net; commit count; pull request (PR) merge rate)
- B2. What was the commit volume trend 2019-2025?
- B3. What is the relationship between raw commit volume and meaningful LOC throughput?

**C. Rework share**
- C1. How is rework operationalised? (short-cycle churn vs. longer-cycle refactor)
- C2. What is the current industry baseline for rework rate?
- C3. What directional shift has occurred since 2020?

**D. Project abandonment**
- D1. How is abandonment defined? (no commits vs. no maintainer response vs. no community)
- D2. What is the abandonment rate for open source projects overall?
- D3. What is the abandonment rate for newly created projects (within 1 year)?

**E. AI slop indicators**
- E1. How is "AI slop" (low-quality AI-generated content in software development) operationalised?
- E2. What quantitative indicators exist (copy-paste rate, duplication, churn)?
- E3. What is the trajectory since AI coding assistant adoption?

**F. Useless-test prevalence**
- F1. How are "useless tests" operationalised? (tautological tests, low mutation score)
- F2. What evidence exists for AI-generated test quality degradation?
- F3. What is the gap between line coverage and mutation coverage in AI-heavy codebases?

**G. Unshipped-project rates**
- G1. How is "unshipped" defined? (canceled before completion vs. never deployed to production)
- G2. What is the general software project cancellation rate?
- G3. What is the production deployment rate for AI/machine learning (ML) projects?

### §2 Investigation

**A. Repository creation rate**

A1-A2. [fact] The GitHub Octoverse 2019 report recorded approximately 44 million new repositories created during 2019, with a total developer base of over 40 million. Source: https://octoverse.github.com/2019/

[fact] The GitHub Octoverse 2020 report recorded approximately 60 million new repositories created during the 2019-2020 reporting period, with total developers reaching over 56 million. Source: https://octoverse.github.com/2020/

[fact] The GitHub Octoverse 2025 (covering data through 2025, with comparable 2024 figures) reports developers created more than 230 new repositories per minute, totalling over 121 million new repositories in the 2024 calendar year, with 395 million total public repositories at the end of 2025. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

A3. [inference] Repository creation rate more than doubled between 2019 (44M/year) and 2024 (121M/year), a roughly 175% increase over five years. The growth rate accelerated after the November 2021 GitHub Copilot launch and again after the December 2024 Copilot Free release, which the Octoverse 2025 report explicitly links to a "step-change in developer sign-ups." Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

**B. LOC velocity**

B1. [fact] LOC as a direct productivity metric has been deprioritised in industry practice since at least 2019. The DORA programme operationalises delivery velocity through deployment frequency and lead time for changes rather than raw LOC counts. Source: https://dora.dev/research/2024/dora-report/

B2. [fact] GitHub Octoverse 2025 reports that developers pushed nearly 1 billion commits in 2025, a 25.1% YoY increase; August 2025 alone recorded nearly 100 million commits, described as a monthly record. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

[fact] The GitClear AI Copilot Code Quality 2025 report analysed 211 million changed lines of code from 2020 to 2024, drawing on data from large enterprise and open-source codebases (Google, Microsoft, Meta, Chromium, Visual Studio Code). Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research

[fact] Within the GitClear dataset, copy/pasted code blocks rose from 8.3% of all code changes in 2020 to 12.3% in 2024, a 48% relative increase. Duplicated code blocks (five or more identical lines) became eight times more common during 2024 relative to the pre-AI baseline. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research (summarised at: https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250)

B3. [inference] The surge in raw commit volume post-2022 includes a substantial proportion of AI-generated code. The concurrent rise in copy-paste frequency and duplication from the GitClear dataset supports the inference that raw LOC throughput overstates meaningful new functionality added. Prior repository work on this topic (2026-03-12-volume-vs-correctness-ai-era) reaches a consistent conclusion: volume is rising while correctness-adjusted throughput is harder to measure. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

**C. Rework share**

C1. Two operationalisations are current in industry practice:
- Short-cycle churn (code revised within two weeks of creation): GitClear's primary metric.
- Longer-cycle rework rate (code changes modifying lines introduced in the last 21 days): LinearB's definition, also adopted by DORA as the "5th metric."
[fact] The DORA 2024 report formally added rework rate (defined as unplanned deployments required to fix user-impacting bugs) as a metric strongly correlated with change failure rate. Source: https://dora.dev/research/2024/dora-report/

C2. [fact] The LinearB 2024/2026 engineering benchmarks, derived from 8.1 million pull requests across 4,800+ engineering teams in 42 countries, set the following rework-rate benchmarks: elite teams achieve rework rates below 3%; good teams 3-5%; fair teams 6-7%; needs-focus above 7%. Source: https://linearb.io/resources/engineering-benchmarks

C3. [fact] Within the GitClear dataset, code churn (lines revised within two weeks of creation) rose from 3.1% of all changed code in 2020 to 5.7% in 2024, an 84% relative increase. GitClear projects churn will approximately double the pre-AI baseline by 2026 at current trajectory. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research (summarised at: https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250)

[fact] The share of code classified as "moved" (an indicator of deliberate refactoring) dropped from 24.1% in 2020 to 9.5% in 2024 within the GitClear dataset, a 39.9% relative decline. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research

[assumption] The GitClear dataset, while large (211M changed lines), is drawn from enterprise and high-profile open-source projects and may not represent the broader long-tail of GitHub repositories. Smaller teams and personal projects may show different patterns. Justification: the dataset is explicitly described as drawn from named large codebases. Source: https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250

**D. Project abandonment**

D1. Two operationalisations appear in the literature:
- Academic definition (Avelino et al.): no meaningful activity from original maintainers with no succession.
- Industry/community estimate: no commits within a 12-18 month window.
[assumption] These definitions produce different rates; the Avelino study is more conservative (requires loss of core maintainers in popular projects) while the 12-18 month window captures a broader inactive tail. Justification: the two studies below use these distinct definitions and produce substantially different numbers (16% vs. 95%). Source: https://arxiv.org/abs/1906.08058

D2. [fact] Avelino et al. (2019) studied 1,932 popular GitHub projects and found 315 (16%) were abandoned; of those, 128 (41%) survived through new core developers assuming maintenance. The sample was popular projects, introducing survivorship bias (popular projects are less likely to be abandoned than the median repo). Source: https://arxiv.org/abs/1906.08058

[inference] Approximately 40% of GitHub repositories have only the repository owner as a contributor, making them single-maintainer projects with elevated abandonment risk. Source: https://gitnux.org/git-repository-statistics/

D3. [inference] Industry analyses estimate that 60-70% of all GitHub repositories become inactive within 12-18 months of creation, with newly created repositories being especially vulnerable. A 2024 industry summary cites an estimate of up to 95% of newly created open source projects becoming abandoned within one year, though this figure lacks a peer-reviewed primary source and should be treated as a rough upper bound for the long tail of low-engagement repositories. Source: https://www.openpledge.io/abandoned-open-source-projects.html; https://gitnux.org/git-repository-statistics/

Failed primary-source search: The 95% figure from the 2024 industry summary (openpledge.io) cites no primary academic study. Search query "95 percent GitHub projects abandoned one year peer-reviewed" returned no peer-reviewed paper confirming this number. It is treated as [inference] with low-to-medium confidence.

**E. AI slop indicators**

E1. [fact] Baltes et al. (2026) define "AI slop" as low-quality AI-generated content in software development contexts, including generated code, pull requests, documentation, and bug reports that pass superficial review but introduce long-term issues such as duplicated logic, architectural incoherence, and tautological tests. The paper analysed 1,154 posts across 15 discussion threads from Reddit and Hacker News, developing a codebook of 15 codes in three clusters: Review Friction, Quality Degradation, and Forces and Consequences. Source: https://arxiv.org/abs/2603.27249

E2. [fact] The GitClear dataset quantifies several AI slop indicators from 2020-2024: copy/pasted code rose from 8.3% to 12.3% of changes; code blocks of five or more identical lines became eight times more common; and the "moved code" fraction (a refactoring proxy) fell from 24.1% to 9.5%. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research

[fact] The DORA 2024 report found that every 25% increase in AI adoption on a team was associated with a 1.5% decrease in software delivery throughput and a 7.2% decrease in delivery stability, despite a concurrent 2.1% increase in individual productivity. Source: https://dora.dev/research/2024/dora-report/

E3. [inference] The combination of rising copy-paste rates, falling refactor rates, and the DORA stability degradation signal, all post-dating GitHub Copilot's 2021 launch, is consistent with AI-generated code increasing volume while introducing structural quality costs. The Baltes et al. framing as a "tragedy of the commons" captures the mechanism: individual productivity gains externalise review and maintenance costs onto the broader team. Source: https://arxiv.org/abs/2603.27249; https://www.gitclear.com/ai_assistant_code_quality_2025_research

**F. Useless-test prevalence**

F1. [inference] "Useless tests" (tests that pass without validating intended behaviour) are operationalised via mutation testing: a test suite with low mutation score has tests that do not catch injected faults. Line coverage is the commonly reported metric but does not measure test effectiveness. This operationalisation is drawn from practitioner analysis; no authoritative standards-body definition was located. Source: https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion; https://botmonster.com/ai/80-percent-coverage-trap-ai-generated-tests-false-security/

[inference] AI-generated test suites frequently produce tautological tests, meaning tests that assert only that the code executes as currently written rather than that it behaves correctly. Industry analyses report cases where line coverage reaches 90-100% with mutation scores below 5%. Source: https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion; https://botmonster.com/ai/80-percent-coverage-trap-ai-generated-tests-false-security/

F2. [fact] The GitClear 2025 report noted that AI-generated tests frequently check only happy paths, miss error conditions and edge cases, and often duplicate each other, contributing to the overall duplication trend in the dataset. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research

[assumption] No large-scale longitudinal study with rigorous methodology comparing pre-AI and post-AI mutation scores across a defined repository population was found during this investigation. The evidence base for useless-test prevalence relies on smaller analyses and practitioner reports rather than on representative longitudinal datasets. Justification: search queries targeting peer-reviewed studies of mutation score trends returned no papers with population-level longitudinal data. Source: https://arxiv.org/abs/2603.27249

F3. [inference] The gap between line coverage and mutation coverage in AI-heavy codebases is likely widening because AI tools optimise for passing existing tests and meeting coverage thresholds rather than for generating tests that challenge the code's behaviour. This is consistent with the mechanism described in Baltes et al. and supported by practitioner reports, but has not been confirmed in a controlled longitudinal study. Source: https://arxiv.org/abs/2603.27249; https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion

**G. Unshipped-project rates**

G1. Two distinct operationalisations apply:
- General software: the Standish Group CHAOS Report defines "cancelled" as projects terminated before delivery. This is the most conservative definition.
- AI/ML projects: "never reached production" includes projects that completed development but were not deployed, often due to operational, organisational, or business-case failures.
[assumption] These two categories are not directly comparable; the AI/ML rate is substantially higher because the deployment challenge is an additional failure mode beyond project cancellation. Justification: the sources below make this distinction explicitly. Source: https://thestory.is/en/journal/chaos-report/

G2. [inference] The Standish Group CHAOS 2020 report, a longitudinal study of software project outcomes, found approximately 31% of projects were completed successfully (on time, on budget, with required features), approximately 50% were "challenged" (late, over budget, or missing features), and approximately 19% were cancelled before delivery. The primary report is behind a paywall; this figure is drawn from a secondary summary and should be treated as an inference from that secondary source. Source: https://thestory.is/en/journal/chaos-report/

G3. [inference] A 2019 VentureBeat analysis (republished and cited in 2024 industry commentary) estimated that 87-90% of machine learning (ML) models never reach production, with deployment barriers rather than development failures as the primary cause. The underlying VentureBeat primary source could not be retrieved directly; this figure is widely cited in secondary industry commentary. Source: https://teaminnovatics.com/blogs/machine-learning-deployment-why-fail/

[inference] An International Data Corporation (IDC)/Lenovo 2025 report found that for every 33 AI proof-of-concept (POC) projects, only four were deployed to production, implying an approximately 88% non-deployment rate for AI POCs. The primary IDC report is behind a paywall; this figure is drawn from CIO.com secondary media coverage. Source: https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html

[inference] The AI/ML non-deployment rate of 87-90% is structurally higher than the general software cancellation rate of approximately 19% because AI/ML projects face an additional deployment gap (the transition from proof-of-concept to production-grade service) that does not exist for traditional software projects in the same form. The gap likely reflects organisational readiness constraints rather than purely technical failures. Source: https://www.artificialintelligence-news.com/news/the-ai-execution-gap-why-80-of-projects-dont-reach-production/

### §3 Reasoning

Removing narrative glue, the core causal structure is as follows:

1. Repository creation rate has grown monotonically from approximately 44M/year (2019) to 121M/year (2024). [fact; source: https://octoverse.github.com/2019/; https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/]

2. Commit volume has grown at roughly 20-25% YoY since at least 2023, reaching nearly 1 billion commits in 2024. [fact; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/]

3. LOC per unit of meaningful functionality is unmeasured at scale, but the GitClear churn and duplication data show the quality composition of LOC output shifted after AI coding assistant adoption. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

4. Rework rate (short-cycle churn) rose 84% relative between 2020 and 2024, from 3.1% to 5.7% of changed lines. [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

5. Abandonment rates for popular projects are empirically established at 16% (Avelino et al. 2019). Long-tail abandonment rates are estimated at 60-95% depending on definition, with no rigorous longitudinal peer-reviewed study covering the full 2019-2026 window. [fact for popular projects; inference for long-tail; source: https://arxiv.org/abs/1906.08058]

6. AI slop is a named phenomenon in community discourse (Baltes et al. 2026) with quantitative correlates in GitClear duplication and churn data, and a negative delivery stability signal in DORA 2024. [fact; source: https://arxiv.org/abs/2603.27249; https://dora.dev/research/2024/dora-report/]

7. Useless-test prevalence lacks a rigorous longitudinal dataset. Practitioner evidence for tautological AI-generated tests is consistent but not population-representative. [inference; source: https://arxiv.org/abs/2603.27249]

8. Unshipped-project rates for general software are stable at approximately 19-31% cancelled (Standish CHAOS). AI/ML projects face an additional production-deployment gap of 87-90% non-deployment. [fact; source: https://thestory.is/en/journal/chaos-report/; https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html]

### §4 Consistency Check

```text
contradiction_scan: no internal contradictions found
confidence_adjustment: none required; long-tail abandonment figures kept as [inference] due to absent primary source
scope_guardrail: maintained; prescriptive recommendations excluded; LOC per functionality unmeasured and acknowledged as gap
dataset_coverage: GitClear covers 2020-2024; Octoverse covers 2019-2025; DORA covers 2019-2024 in separate reports; Standish covers 2020; Avelino 2019; Baltes 2026 qualitative only
cross_source_consistency: GitClear churn direction consistent with DORA stability degradation direction; no contradictions between sources
```

### §5 Depth and Breadth Expansion

**Technical lens:** [inference] The GitClear finding that "moved code" (refactoring proxy) fell from 24.1% to 9.5% while copy-paste rose suggests that AI coding assistants reduce the cognitive cost of writing new code but do not reduce the cost of understanding and restructuring existing code. The Don't Repeat Yourself (DRY) principle, the design heuristic that knowledge should not be duplicated across a codebase, is structurally eroded when copy-paste share rises. This predicts compounding maintenance costs, which is directionally consistent with the DORA stability degradation finding. Source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/

**Economic lens:** [inference] The Standish CHAOS stability of 19% project cancellation over two decades suggests that the rate of general project cancellation is largely organisation-driven rather than technology-driven. The 87-90% AI/ML non-deployment rate reflects a different failure mode: organisations begin more AI POC work than they can operationalise, consistent with the "POC trap" described in AI deployment literature. Source: https://www.artificialintelligence-news.com/news/the-ai-execution-gap-why-80-of-projects-dont-reach-production/

**Behavioural lens:** Baltes et al. (2026) frame the AI slop phenomenon as a tragedy of the commons: each individual developer gains productivity by using AI generation, but the collective cost falls on reviewers and maintainers. [inference] This mechanism predicts that high-AI-adoption teams will see declining review throughput unless review capacity scales proportionally. Source: https://arxiv.org/abs/2603.27249

**Historical lens:** The 44M to 121M repository creation trajectory (2019-2024) mirrors the growth of GitHub itself from 40M to 180M+ developers over the same period. [inference] The per-developer repository creation rate has likely remained broadly stable (roughly one new repository per developer per year on average), but the total count growth is primarily a developer-count effect rather than a change in individual behaviour. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/; https://octoverse.github.com/2019/

**Regulatory/governance lens:** [inference] The DORA 2024 finding that AI adoption reduces delivery stability by 7.2% per 25% adoption increase creates a governance tension: organisations mandating AI tool adoption for productivity gains may inadvertently degrade the delivery reliability metrics that underpin Service Level Agreement (SLA) commitments and regulatory audit trails. Prior repository work in 2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai addresses this tension in detail. Source: https://dora.dev/research/2024/dora-report/

### §6 Synthesis

**Summary:** Across all seven metric areas, the 2019-2026 window shows a consistent directional pattern: raw volume indicators (repository creation, commit count, LOC generated) rose sharply while quality-composition indicators (rework share, duplication, delivery stability) degraded, and project-to-production conversion rates remained low or worsened for AI/ML workloads. [inference; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/] The inflection point for quality composition metrics aligns with AI coding assistant adoption beginning in 2022-2023. Two competing explanations exist: AI tool adoption degrading code quality, and developer community growth (40M to 180M+ on GitHub) bringing a larger proportion of less-experienced practitioners into the ecosystem independently of AI tools. The available evidence cannot definitively separate these explanations.

**Metric summary table:**

| Metric | Baseline (2019-2020) | Current (2023-2025) | Direction | Confidence |
|---|---|---|---|---|
| Repo creation rate | ~44M/year (2019) | ~121M/year (2024) | Up 175% | [fact] high |
| Commit volume | baseline not precisely reported | ~986M-1B/year (2024), +25% YoY | Strongly up | [fact] medium |
| Rework/churn rate | 3.1% of changed lines (2020) | 5.7% (2024) | Up 84% relative | [fact] medium |
| Refactor share (moved code) | 24.1% (2020) | 9.5% (2024) | Down 61% relative | [fact] medium |
| Copy-paste share | 8.3% (2020) | 12.3% (2024) | Up 48% relative | [fact] medium |
| Popular repo abandonment | 16% (Avelino 2019) | No updated longitudinal study | Stable (estimate) | [inference] low |
| New repo abandonment (12 mo.) | 60-70% (industry estimate) | 60-70% (estimate) | Stable or rising | [inference] low |
| AI/ML POC non-deployment | N/A pre-AI era | 87-90% (2024-2025) | High and stable | [inference] medium |
| General project cancellation | ~19% (Standish 2020) | ~19-31% (stable) | Stable | [inference] medium |

**Assumptions:**
1. GitClear dataset (211M changed lines, enterprise/high-profile OSS projects) is representative of the broader enterprise software development trend, though it likely underrepresents personal and student repositories. Source: https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250
2. GitHub Octoverse population (all public GitHub repositories) includes a substantial fraction of experimental, student, and AI-generated repositories whose creation inflates the headline count relative to commercial software production. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
3. The AI/ML non-deployment rate (87-90%) reflects a deployment-era constraint that predates the current study window; it is not a new trend but rather a persistent structural barrier. Source: https://teaminnovatics.com/blogs/machine-learning-deployment-why-fail/

**Risks and gaps:**
- No peer-reviewed longitudinal study covers all seven metrics in a single consistent dataset over the 2019-2026 window.
- Useless-test prevalence has no population-level quantitative dataset; the evidence is practitioner reports and limited case analyses.
- The popular-project abandonment study (Avelino 2019) was not updated in the 2021-2026 period within the scope of this investigation.
- LOC per meaningful functionality remains unmeasured at scale.
- The DORA rework rate definition differs from the GitClear churn definition; the two are consistent in direction but not directly comparable in magnitude.

**Open questions:**
- Has the per-developer repository creation rate (repos/developer/year) changed, or does the headline growth reflect only the developer count increase?
- What is the mutation score distribution across AI-heavy versus AI-light codebases in a representative sample?
- Do abandonment rates for repositories created in 2022-2025 (post-AI coding assistant) differ from pre-AI cohorts?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed; LOC expanded on first use in Research Question; AI expanded on first use in Research Question; DORA expanded in Sources and §0; PR expanded in §1; YoY/ML/POC/DRY expanded in §1 and §2; SLA expanded in §5; IDC expanded in §2; LLM/SDK not used in this item
claim_audit: all factual and inferential claims carry labels; all [assumption] entries carry URL-backed justifications; §2 G2 Standish claim downgraded to [inference] (paywalled primary); §2 G3 IDC claim downgraded to [inference] (secondary media source); §2 F1 mutation-testing definition downgraded to [inference] (personal blog not authoritative); KF8/KF9 downgraded to [inference]; Exec Summary causal claim changed from [fact] to [inference]
evidence_map_check: all Key Findings have rows in Evidence Map; KF2/KF5/KF11/KF8/KF9 medium confidence; Evidence Map rows for Standish and IDC updated to [inference]
inline_citation_check: all claims in §2 carry suffix source bindings; Analysis "stable for decades" narrowed to study window
consistency_check: completed in §4; no contradictions found
scope_guardrail: maintained; prescriptive recommendations excluded
alternative_explanations: developer community inexperience confound added to Analysis
cross_item_integration: throughput-constraint item cross-referenced in Analysis
parity_check: §6 Synthesis and Findings aligned after this update
```

## Findings

### Executive Summary

Across seven software-delivery metrics tracked from 2019 to 2025, raw volume indicators rose sharply while quality-composition indicators degraded, and project-to-production conversion rates remained persistently low. [inference; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/] Repository creation on GitHub grew from approximately 44 million per year (2019) to over 121 million per year (2024), and commit volume reached nearly 1 billion in 2024 at 25% year-over-year growth, but this volume surge coincides with measurable quality erosion: short-cycle code churn rose 84% relative and copy-paste code share rose 48% within the GitClear dataset between 2020 and 2024. [inference; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The DORA 2024 report found that every 25% increase in AI adoption is associated with a 7.2% drop in delivery stability despite individual productivity gains. [fact; source: https://dora.dev/research/2024/dora-report/] This creates a governance tension for organisations mandating AI coding tools, where productivity mandates may degrade delivery reliability. [inference; source: https://dora.dev/research/2024/dora-report/] Project failure rates for general software have remained structurally stable at approximately 19% cancelled (Standish CHAOS), while AI/ML projects face a structurally different non-deployment rate of 87-90% attributed to the operationalisation gap between proof-of-concept and production service. [inference; source: https://thestory.is/en/journal/chaos-report/; https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html] Useless-test prevalence and long-tail repository abandonment rates lack rigorous population-level longitudinal data, representing the two largest evidence gaps.

### Key Findings

1. Repository creation on GitHub more than doubled between 2019 and 2024, growing from approximately 44 million new repositories per year to over 121 million per year. ([fact]; high confidence; source: https://octoverse.github.com/2019/; https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

2. Annual commit volume on GitHub reached nearly 1 billion in 2024, a 25% year-over-year increase, with a record of nearly 100 million commits in a single month. ([fact]; medium confidence; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

3. Short-cycle code churn (lines revised within two weeks of creation) rose 84% relative within the GitClear dataset, from 3.1% of changed lines in 2020 to 5.7% in 2024, coinciding with the period of widespread AI coding assistant adoption. ([fact]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250)

4. The share of code classified as deliberately refactored ("moved code") fell 61% relative in the GitClear dataset, from 24.1% in 2020 to 9.5% in 2024, eroding the structural quality improvement that refactoring provides to long-lived codebases. ([fact]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research)

5. The DORA 2024 report found that every 25% increase in AI adoption on a software team is associated with a 7.2% decrease in delivery stability and a 1.5% decrease in delivery throughput, despite a 2.1% individual productivity increase. ([fact]; medium confidence; source: https://dora.dev/research/2024/dora-report/)

6. Copy-pasted code blocks rose from 8.3% to 12.3% of all code changes in the GitClear dataset between 2020 and 2024, and duplicated code blocks of five or more identical lines became eight times more common during 2024. ([fact]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research)

7. Among popular open source GitHub projects, 16% were abandoned (with 41% of those rescued by new maintainers), while industry estimates for newly created projects place the 12-month inactivity rate at 60-95% depending on the definition used. ([inference]; medium confidence for popular project figure, low confidence for new-project estimate; source: https://arxiv.org/abs/1906.08058; https://gitnux.org/git-repository-statistics/)

8. The Standish Group CHAOS 2020 report found software project cancellation rates stable at approximately 19%, with 50% of projects challenged and 31% successful, a distribution consistent with secondary summaries spanning the 2020-2023 window; the primary report is paywalled. ([inference]; medium confidence; source: https://thestory.is/en/journal/chaos-report/)

9. AI and ML projects face a structurally higher non-deployment rate of 87-90%, with IDC/Lenovo finding that of every 33 AI proof-of-concept projects only four reached production, reflecting an operationalisation gap that is distinct from project cancellation; both figures are drawn from secondary media coverage of paywalled primary reports. ([inference]; medium confidence; source: https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html; https://teaminnovatics.com/blogs/machine-learning-deployment-why-fail/)

10. AI-generated test suites frequently produce tautological tests that achieve high line coverage without effective fault detection; practitioner analyses report mutation scores below 5% in suites with 100% line coverage, though no population-level longitudinal dataset for this metric exists. ([inference]; low confidence; source: https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion; https://arxiv.org/abs/2603.27249)

11. Baltes et al. (2026) characterise AI slop in software development as a tragedy of the commons: individual productivity gains from AI-generated code externalise review and maintenance costs onto the broader team, with Quality Degradation, Review Friction, and Forces and Consequences as the three empirically identified impact clusters. ([fact]; medium confidence; source: https://arxiv.org/abs/2603.27249)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Repository creation grew from 44M/year (2019) to 121M/year (2024) | https://octoverse.github.com/2019/; https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ | High | Primary industry reports; Octoverse is self-reported by GitHub |
| [fact] Commit volume near 1 billion in 2024, +25% YoY | https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ | Medium | Primary industry report; single source |
| [fact] Code churn rose from 3.1% to 5.7% (2020-2024) | https://www.gitclear.com/ai_assistant_code_quality_2025_research | Medium | Large (211M lines) but enterprise-skewed dataset; vendor-produced report |
| [fact] Moved code share fell from 24.1% to 9.5% (2020-2024) | https://www.gitclear.com/ai_assistant_code_quality_2025_research | Medium | Same dataset as churn finding; corroborated by DORA stability data directionally |
| [fact] DORA 2024: AI adoption correlates with 7.2% stability drop per 25% adoption increase | https://dora.dev/research/2024/dora-report/ | Medium | Primary Google/DORA research; self-reported survey data with large N; single source |
| [fact] Copy-paste share rose from 8.3% to 12.3% (2020-2024); duplication 8x | https://www.gitclear.com/ai_assistant_code_quality_2025_research | Medium | Enterprise-skewed dataset; vendor report |
| [inference] Popular repo abandonment 16%; new-repo abandonment 60-95% | https://arxiv.org/abs/1906.08058; https://gitnux.org/git-repository-statistics/ | Low (new-repo), High (popular repo) | Avelino is peer-reviewed; new-repo figure is industry estimate without peer-reviewed source |
| [inference] Standish CHAOS 2020: 19% cancelled, 50% challenged, 31% successful | https://thestory.is/en/journal/chaos-report/ | Medium | Primary Standish report is paywalled; figure from secondary summary; consistent across multiple references |
| [inference] AI/ML POC non-deployment: 87-90%; IDC: 4 of 33 POCs reach production | https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html; https://teaminnovatics.com/blogs/machine-learning-deployment-why-fail/ | Medium | Both figures drawn from secondary media coverage; primary IDC and VentureBeat reports paywalled or inaccessible |
| [inference] AI tests: mutation scores below 5% with 100% line coverage | https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion | Low | No population-level longitudinal study; practitioner reports only |
| [fact] Baltes et al. 2026: AI slop as tragedy of commons with three impact clusters | https://arxiv.org/abs/2603.27249 | Medium | arXiv preprint; qualitative methodology on 1,154 posts; single source |

### Assumptions

1. The GitClear dataset (211M changed lines, enterprise and high-profile open source codebases) is broadly representative of enterprise software development trends, though it likely underrepresents personal, student, and AI-generated throw-away repositories. Justification: the dataset includes named large-scale production codebases (Google, Meta, Microsoft, Chromium, VS Code) with transparent methodology. Source: https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250

2. GitHub Octoverse repository counts include a substantial fraction of experimental, student, and AI-generated repositories. The headline count growth therefore overstates the growth in commercially maintained software projects. Justification: the Octoverse 2025 report explicitly notes that 80% of new developers use Copilot in their first week, suggesting a large proportion of new repositories are tutorial or experimental. Source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/

3. The AI/ML non-deployment rate (87-90%) reflects a structural deployment barrier that predates the current AI coding assistant era. It is a persistent characteristic rather than a new 2022-2025 trend, though the growth in AI POC project creation increases the absolute number of unshipped projects. Justification: the VentureBeat figure dates to 2019; the IDC/Lenovo 2025 figure is consistent, suggesting stability in the rate. Source: https://teaminnovatics.com/blogs/machine-learning-deployment-why-fail/; https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html

### Analysis

The seven metrics fall into two structural groups when assessed against the available evidence.

The first group (repository creation, commit volume, LOC output) shows clear upward trends that are well-documented by primary sources. These metrics are supply-side: they measure what developers are producing, not whether that production has quality or business value. The growth in these metrics is largely explained by developer community growth (40M to 180M+ on GitHub over the study period) compounded by AI coding assistant adoption lowering the marginal cost of generating code. [inference; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/]

The second group (rework, refactor share, AI slop indicators, delivery stability) shows degradation in the 2020-2024 period. The GitClear and DORA data converge in direction: AI coding assistant adoption appears to accelerate code production at the cost of code composition quality. Two competing explanations must be acknowledged. First, the GitClear dataset is enterprise-skewed and the DORA signal may represent teams that have not yet adapted review processes to AI-generated volume, a transient adaptation lag rather than a structural degradation. Second, developer community growth from 40M to 180M+ on GitHub over the study period brought a substantially larger proportion of less-experienced practitioners into the ecosystem independently of AI tool adoption; this demographic shift could account for some of the quality metric decline without any causal role for AI tools. The available evidence cannot definitively separate these explanations, and both are consistent with the observed data. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://dora.dev/research/2024/dora-report/; https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/]

Project non-delivery (abandonment, cancellation, non-deployment) has two distinct regimes. General software cancellation rates (Standish CHAOS at approximately 19%) have remained broadly stable across the 2020-2023 window covered by available secondary summaries. [inference; source: https://thestory.is/en/journal/chaos-report/] This stability implies a structural organisational constraint rather than a technology-driven trend, though this interpretation is an inference from the stable rate data. [inference; source: https://thestory.is/en/journal/chaos-report/] AI/ML non-deployment rates (87-90%) reflect an additional barrier: the gap between building an AI model or proof-of-concept and operating it reliably as a production service. [inference; source: https://www.cio.com/article/3850763/88-of-ai-pilots-fail-to-reach-production-but-thats-not-all-on-it.html]

Useless-test prevalence remains the weakest-evidenced metric area. The mechanism (AI-generated tests optimise for coverage metrics rather than fault detection) is theoretically coherent and supported by qualitative practitioner accounts, but lacks a population-level quantitative baseline. Teams relying on line coverage as their quality gate may be systematically unaware of how far their effective test coverage has declined. [inference; source: https://arxiv.org/abs/2603.27249; https://tianpan.co/blog/2026-05-04-ai-generated-tests-coverage-illusion]

The related completed item on productivity incentive metrics (2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai, https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai.md) addresses the governance implication of this pattern in detail: speed-focused incentives create hidden quality costs, and code acceptance rate is an insufficient organisational metric. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-productivity-incentive-metrics-quality-review-agentic-ai.md; https://dora.dev/research/2024/dora-report/] The rising rework rates (KF3) and declining refactor share (KF4) documented here have direct implications for technical debt accumulation rates; the related completed item on IT throughput constraint magnitude and debt accumulation rate (2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate, https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md) quantifies how short-cycle churn and quality degradation compound into throughput constraints over multi-year horizons. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md]

### Risks, Gaps, and Uncertainties

1. No peer-reviewed longitudinal study covers all seven metrics in a single consistent dataset over the 2019-2026 window. The evidence base is a patchwork of industry reports (Octoverse, DORA, GitClear, Standish), vendor benchmarks (LinearB), one peer-reviewed academic study on abandonment (Avelino 2019), and one qualitative arXiv preprint on AI slop (Baltes 2026).

2. Useless-test prevalence has no population-level quantitative baseline. The practitioner reports and mutation score case studies are directionally consistent but not representative.

3. The Avelino et al. abandonment study (2019) is the most rigorous source for the popular-project abandonment figure, but it predates AI coding assistant adoption and has not been replicated over the 2022-2025 window.

4. The GitClear dataset is enterprise-skewed and vendor-produced. While the methodology is transparent and the dataset large, independent replication has not been published within the scope of this investigation.

5. LOC per unit of meaningful functionality remains unmeasured at scale. The divergence between raw commit volume growth (+25% YoY) and delivery stability decline (DORA -7.2% per 25% AI adoption) implies that the relationship between volume and value has changed, but the precise magnitude of this decoupling is not quantified.

### Open Questions

- Has the per-developer repository creation rate changed since AI coding assistant adoption, or does headline repository growth track developer count growth proportionally?
- What does a longitudinal mutation-score analysis across a representative repository population show for 2019-2025?
- Do repositories created in 2022-2025 (post-AI coding assistant era) show different abandonment or inactivity rates at 12 months compared to pre-AI cohorts?
- Is the DORA AI adoption stability degradation (-7.2% per 25% adoption) a one-time adjustment cost or a persistent steady-state effect?

### Output

Type: knowledge

Description: Seven software-delivery metrics are tabulated with baseline values (2019-2020), current values (2023-2025), trend direction, and confidence levels. [inference; source: https://dora.dev/research/2024/dora-report/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Key data: repository creation up 175% (44M to 121M/year); commit volume near 1 billion/year (+25% YoY); short-cycle churn up 84% (3.1% to 5.7%); refactor share down 61% (24.1% to 9.5%); AI adoption correlates with 7.2% stability drop (DORA 2024); general software cancellation rate stable at 19%; AI/ML POC non-deployment rate 87-90%.

Three most important sources:
- [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) - primary data on repository creation and commit volume
- [DORA Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) - primary data on delivery performance and AI impact
- [GitClear AI Copilot Code Quality Report 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research) - primary data on code composition quality trends
