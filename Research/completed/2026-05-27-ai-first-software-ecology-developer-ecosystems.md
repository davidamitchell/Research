---
review_count: 2
title: "AI-first software ecology in large engineering organisations (2025-2030)"
added: 2026-05-27T18:39:02+00:00
status: completed
priority: high
blocks: []
themes: [software-engineering, organisational-design, agentic-ai, tools-infrastructure, enterprise-adoption]
started: 2026-05-29T10:40:20+00:00
completed: 2026-05-29T11:31:43+00:00
output: [knowledge]
cites: [2026-02-28-ai-strategy-swe-focus, 2026-03-14-reliable-software-llm-era, 2026-03-12-volume-vs-correctness-ai-era, 2026-03-08-ai-coding-harnesses-agent-philosophy, 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate]
related: [2026-03-12-ai-team-size-strike-team-thesis, 2026-03-10-formal-spec-intent-alignment-agentic-coding, 2026-05-21-monolith-vs-cohesive-portfolio-tco]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: ""
    changed: "2026-05-29"
    progress: "progress/2026-05-29-ai-first-software-ecology-developer-ecosystems.md"
    summary: "Initial completion"
---

# AI-first software ecology in large engineering organisations (2025-2030)

## Research Question

What operating model, architecture strategy, and governance practices best improve developer productivity with Artificial Intelligence (AI) assistance in large software organisations, while preserving quality, security, maintainability, and socio-technical resilience through 2030?

## Scope

**In scope:**
- Software ecology definitions and socio-technical system mapping frameworks relevant to software organisations
- Systems-thinking methods that can be applied to developer workflows and organisational change
- Evidence from 2023-2026 on AI-assisted software development outcomes and second-order effects
- Comparative ecosystem signals from Google and other large technology companies
- Organisational and cultural adaptations for AI-first engineering

**Out of scope:**
- Building or benchmarking specific coding models
- Prescriptive legal advice for any single jurisdiction
- Company-confidential internal data not available in public or accessible organisational sources
- Forecasting beyond 2030

**Constraints:** (time, source types, access)
- Prioritise peer-reviewed research, major industry engineering reports, and primary technical documentation
- Use publicly available sources with verifiable URLs only
- Focus analysis on large engineering organisations (roughly 500+ engineers) for transferability

## Context

This research will inform strategic decisions about how to design an AI-first developer ecosystem and where to invest in process, tooling, platform, and capability-building so productivity gains do not create hidden quality, reliability, or coordination debt.

## Approach

1. Establish a usable definition and analytical framing for software ecology and socio-technical systems in software organisations.
2. Map core feedback loops in modern developer workflows and identify high-leverage intervention points using systems-thinking tools.
3. Evaluate empirical evidence for AI-related productivity shifts, including second-order and third-order effects.
4. Compare platform and process patterns (monorepo, large-scale change mechanisms, shared ownership) across major technology organisations.
5. Identify operational risks and adaptation strategies in review, testing, integration, security, and architectural control under high code-generation velocity.
6. Synthesize organisational implications, future-state ecosystem characteristics, and health metrics for 2028-2030 planning.

## Sources

- [x] [Conway (1968) How Do Committees Invent?](https://www.melconway.com/Home/Conways_Law.html) - original Conway's Law framing
- [x] [Forsgren, Humble, Kim (2018) Accelerate](https://itrevolution.com/product/accelerate/) - evidence-based software delivery performance model
- [x] [Google Engineering Practices / Software Engineering at Google](https://abseil.io/resources/swe-book) - large-scale engineering practices and trade-offs
- [x] [Beyer et al. Site Reliability Engineering](https://sre.google/books/) - reliability and shared-fate operational principles
- [x] [Anthropic Economic Index (2025)](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) - AI usage patterns and labour/task impacts
- [x] [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) - ecosystem-level software development trend data
- [x] [Microsoft Work Trend Index 2026](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization) - organisational AI adoption effects; Frontier Firm archetype
- [x] [OECD AI Policy Observatory](https://oecd.ai/) - governance, risk, and policy context for AI deployment
- [x] [METR et al. (2025) Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) - primary RCT evidence for experienced-developer slowdown
- [x] [Paradis et al. (2024) How much does AI impact development speed? Google RCT](https://arxiv.org/abs/2410.12944) - Google 96-engineer enterprise RCT; 21% time reduction
- [x] [MIT GenAI / Microsoft (2024) RCT of GitHub Copilot](https://mit-genai.pubpub.org/pub/v5iixksv) - 4,867 developer RCT; 26% more PRs per week
- [x] [Microsoft Research (2023) The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/) - lab study; 55.8% faster task completion
- [x] [DORA (2025) AI-Assisted Software Development Report](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report) - 5,000 developer survey; 7 capabilities; AI amplifier thesis
- [x] [Faros AI (2026) Key Takeaways from the DORA Report 2025](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) - telemetry 22,000+ developers; Acceleration Whiplash pattern
- [x] [Forsgren et al. (2021) The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124) - SPACE framework; five dimensions of productivity
- [x] [Google Research Blog (2024) AI in software engineering at Google: Progress and the path ahead](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/) - Google internal AI tooling deployment learnings
- [x] [TechSpot (2026) Google says AI now generates 75% of its new code](https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html) - Google AI code generation scale statistics
- [x] [OWASP LLM Top 10 (2024)](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - security risks from LLM code generation
- [x] [Skelton and Pais Team Topologies (key concepts)](https://teamtopologies.com/key-concepts) - four team types; cognitive load; platform teams
- [x] [Parasuraman and Riley (1997) Humans and Automation](https://doi.org/10.1518/001872097778543886) - automation bias definition; over-trust in automated system outputs

---

## Research Skill Output

### §0 Initialise

```text
Research Question: What operating model, architecture strategy, and governance practices best
improve developer productivity with AI assistance in large software organisations, while
preserving quality, security, maintainability, and socio-technical resilience through 2030?

Decision/problem informed: How to design and govern an AI-first developer ecosystem at
organisational scale, where to invest in process, tooling, platform, and capability-building
so productivity gains do not create hidden quality, reliability, or coordination debt.

Scope: In scope - software ecology definitions, systems-thinking frameworks, empirical
AI-assisted development evidence 2023-2026, Google and large-tech comparisons, organisational
adaptation strategies. Out of scope - building or benchmarking coding models, legal advice,
company-confidential data, forecasting beyond 2030.

Constraints: peer-reviewed research, major industry engineering reports, primary technical
documentation; publicly verifiable URLs only; focus on large orgs (500+ engineers).

Output format: knowledge item - executive summary, 8-12 key findings, evidence map,
assumptions, analysis, risks/gaps, open questions.

Working hypotheses:
[assumption] AI tools universally increase productivity - unverified; empirical evidence shows
heterogeneous effects by task type and experience level. Justification: multiple studies exist
with contradictory findings; assumed as a baseline to be tested.
[assumption] Higher code-generation velocity linearly improves organisational delivery -
unverified; telemetry data suggests system-level quality effects may be negative.
Justification: see DORA 2025 and Faros AI evidence below.
```

### §1 Question Decomposition

From the six Approach sub-questions, the following atomic questions are derived:

**Sub-question 1: Software ecology definition and framing**
- 1a. What does "software ecology" mean in the context of large engineering organisations?
- 1b. What socio-technical systems concepts are most relevant for developer workflow analysis?
- 1c. How does Conway's Law (1968) apply to AI-generated code and architectural boundaries?

**Sub-question 2: Systems-thinking tools for developer workflows**
- 2a. What are the key feedback loops in modern AI-assisted developer workflows?
- 2b. Where are the highest-leverage intervention points in these feedback loops?
- 2c. What measurement frameworks (e.g., Satisfaction, Performance, Activity, Communication, Efficiency (SPACE), DevOps Research and Assessment (DORA) metrics) are most diagnostic?

**Sub-question 3: Empirical evidence for AI productivity effects**
- 3a. What Randomised Controlled Trial (RCT) evidence exists for AI coding tools in professional settings?
- 3b. Do productivity effects differ by developer experience level?
- 3c. What are the second-order effects - code quality, security, review burden, defect rates?
- 3d. What does telemetry data (not just surveys) show about organisational-level delivery outcomes?

**Sub-question 4: Ecosystem design lessons from large technology organisations**
- 4a. What platform and process patterns from Google (monorepo, Bazel, Rosie) still hold under AI code generation?
- 4b. What proportion of code is now AI-generated at Google and what are the implications?
- 4c. What platform engineering patterns show the strongest correlation with AI productivity amplification?

**Sub-question 5: Operational controls under high code-generation velocity**
- 5a. What are the primary security risks introduced by AI code generation?
- 5b. What governance patterns effectively manage architectural drift under AI assistance?
- 5c. What review, testing, and integration controls adapt best to higher change velocity?

**Sub-question 6: Future-state ecosystem characteristics and metrics**
- 6a. What organisational capabilities differentiate high-Return on Investment (ROI) organisations from low-AI-ROI organisations?
- 6b. What metrics best capture ecosystem health in an AI-first development context?
- 6c. What is the "Frontier Firm" archetype and what operating model does it imply?

### §2 Investigation

#### 2.A Software ecology framing and Conway's Law

Conway's Law (Melvin Conway, 1968) states that organisations design systems that mirror their own communication structures. [fact; source: https://www.melconway.com/Home/Conways_Law.html]

The Team Topologies framework (Skelton and Pais, 2019) operationalises Conway's Law into four team types - stream-aligned, complicated-subsystem, enabling, and platform - and defines interaction modes designed to maximise flow and minimise cognitive load on teams. [fact; source: https://teamtopologies.com/key-concepts] The framework explicitly states that platform teams provide self-service capabilities to reduce cognitive load for stream-aligned teams. [fact; source: https://teamtopologies.com/key-concepts]

A "software ecology" - the interdependency of tools, teams, processes, infrastructure, and human practices in a software organisation - is a useful framing from socio-technical systems theory. [inference; source: https://abseil.io/resources/swe-book] The term parallels biological ecology: each component evolves in response to others, creating emergent properties neither controllable nor predictable from any single actor's perspective. [assumption; justification: widely used analogy in software engineering literature; no single canonical definition found - nearest source: https://abseil.io/resources/swe-book]

Conway's Law creates a structural tension with AI-generated code: if AI tools suggest code without awareness of team boundaries or architectural conventions, AI assistance can accelerate architectural drift - the progressive deviation of a codebase from its intended design. [inference; source: https://arxiv.org/abs/2410.12944; https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/]

#### 2.B Feedback loops and measurement frameworks

The SPACE framework (Forsgren et al., 2021) defines five dimensions of developer productivity: Satisfaction and wellbeing, Performance, Activity, Communication and collaboration, and Efficiency. [fact; source: https://queue.acm.org/detail.cfm?id=3454124] A key finding from SPACE is that no single metric is sufficient; measuring only Activity (pull requests (PRs) merged, lines of code committed) systematically misrepresents developer productivity. [fact; source: https://queue.acm.org/detail.cfm?id=3454124]

AI tools demonstrably inflate Activity metrics (more PRs opened, more commits) while masking deterioration in Quality, Communication, and Satisfaction dimensions. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

The DORA (DevOps Research and Assessment) 2025 report (survey of ~5,000 developers) identified seven organisational capabilities that amplify AI benefits: (1) clear AI stance from leadership, (2) healthy data ecosystems, (3) AI-accessible internal data, (4) strong version control practices, (5) small-batch work discipline, (6) user-centric focus, and (7) quality internal platforms. [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

The Accelerate (Forsgren, Humble, Kim 2018) four DORA metrics - Deployment Frequency, Lead Time for Changes, Change Failure Rate, and Time to Restore Service - remain the most widely validated organisational-level delivery metrics. [fact; source: https://itrevolution.com/product/accelerate/]

#### 2.C Empirical evidence: RCT and telemetry studies

**Study 1 - METR Randomised Controlled Trial (July 2025):**
A Randomised Controlled Trial (RCT) conducted by Model Evaluation and Threat Research (METR) with 16 experienced open-source developers completing 246 real coding tasks in projects where developers had an average of five years prior experience. Each task was randomly assigned to allow or disallow AI tools (primarily Cursor Pro with Claude 3.5/3.7 Sonnet). Allowing AI increased task completion time by **19%** - AI tools slowed experienced developers down. [fact; source: https://arxiv.org/abs/2507.09089; https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/]

Developers forecasted a 24% speedup and perceived a 20% speedup after completing tasks - both directionally opposite to the measured 19% slowdown. [fact; source: https://arxiv.org/abs/2507.09089]

Expert economists and Machine Learning (ML) researchers predicted 39% and 38% speedups respectively - also opposite to the measured outcome. [fact; source: https://arxiv.org/abs/2507.09089]

**Study 2 - Google RCT (October 2024):**
An RCT with 96 full-time Google software engineers completing complex, enterprise-grade tasks found AI tools reduced time on task by approximately **21%** (wide confidence intervals). Developers who spent more hours on code per day benefited more. [fact; source: https://arxiv.org/abs/2410.12944]

**Study 3 - MIT/Microsoft large-scale RCT:**
A large-scale study involving ~4,867 developers found Copilot users achieved approximately **26% more PRs per week** compared to control groups. [fact; source: https://mit-genai.pubpub.org/pub/v5iixksv]

**Study 4 - GitHub Copilot lab study (Microsoft Research):**
A controlled task study found AI tools enabled ~55.8% faster task completion in isolated coding problems. [fact; source: https://www.microsoft.com/en-us/research/publication/the-impact-of-ai-on-developer-productivity-evidence-from-github-copilot/]

**Contradiction and reconciliation - METR vs MIT/Google:**
The METR result (experienced developers, real projects, 19% slowdown) contradicts the MIT/GitHub result (less experienced developers, isolated tasks, 26-55% speedup). [inference; source: https://arxiv.org/abs/2507.09089; https://mit-genai.pubpub.org/pub/v5iixksv; https://arxiv.org/abs/2410.12944] The most plausible reconciling inference is that productivity effects are heterogeneous by: (a) developer experience level - experienced developers pay a higher cognitive overhead reviewing AI suggestions for correctness relative to the time saved; (b) task type - isolated, well-defined tasks benefit more than complex, context-heavy real-world maintenance tasks; (c) codebase familiarity - working in an unfamiliar codebase benefits more from AI assistance than working in one's own long-maintained project. [inference; source: https://arxiv.org/abs/2507.09089]

**Study 5 - Faros AI telemetry analysis (2026):**
Faros AI analysis of telemetry from 22,000+ developers tracked the "AI Productivity Paradox" and "Acceleration Whiplash": individual output increased (21% more tasks completed, 98% more PRs opened per developer per month), but organisational delivery metrics degraded sharply. By 2026: epics per developer +66.2%, but median PR review time +**441%**, bugs per developer +**54%**, incidents per PR +**242.7%**. [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

**Study 6 - GitHub Octoverse 2025:**
In 2025, GitHub reported 180M+ active developers; 80% of new GitHub developers used Copilot in their first week; 43.2M PRs merged per month (+23% year-over-year); 986M commits in 2025 (+25% year-over-year). 72.6% of Copilot code review users reported improved effectiveness. [fact; source: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/]

**Study 7 - Microsoft Work Trend Index (WTI) 2026:**
Microsoft WTI 2026 introduced the "Frontier Firm" concept - organisations restructured around on-demand intelligence that lead in AI value. Only 19% of organisations surveyed reached this "sweet spot." Organisational factors account for 2× the AI impact of individual effort alone. 49% of Copilot conversations support cognitive work; 66% of AI users spend more time on high-value tasks. [fact; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization]

**Study 8 - DORA 2025 (survey-based):**
DORA 2025 concluded that AI amplifies existing conditions - high-maturity organisations benefit more, low-maturity organisations see fewer gains or deterioration. 90% of organisations surveyed now have platform engineering capability; the correlation between platform quality and AI amplification is direct. [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

**Contradiction - DORA survey vs Faros telemetry:**
DORA 2025 (survey-based) claims high-maturity organisations are better protected from AI downsides; Faros AI 2026 (telemetry-based) reports quality degradation even among organisations with high throughput capability. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report] This contradiction is partially resolvable: DORA measured survey-reported perceptions and four delivery metrics; Faros measured code-quality telemetry (review time, defects, incidents). Organisations can score "high" on DORA's delivery-throughput metrics while simultaneously accumulating quality debt measured in defect and incident rates. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

#### 2.D Platform and process patterns from large technology organisations

Google's internal software engineering at scale uses a unified monorepo (Piper), Bazel/Blaze build system, and automated large-scale refactoring tools (Rosie, Refaster, ClangMR). [fact; source: https://abseil.io/resources/swe-book]

Google reported ~25% of new code AI-generated as of late 2023, rising to ~50% in 2025 and approximately 75% by early 2026. [fact; source: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/; https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html]

Google's internal RCT of AI coding tools (2024) found: code completion acceptance rate of 37%, contributing to 50% of code characters - with AI and manual contributions approximately equal by volume. [fact; source: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/]

Google's key deployment lessons: (1) User Experience (UX) that blends naturally into workflow outperforms features requiring deliberate triggering; (2) the code author increasingly becomes a reviewer, requiring balance between review cost and added value; (3) rapid head-to-head comparison (A/B) iteration against usage logs is critical; (4) high-quality data from engineering activities enables model improvement. [fact; source: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/]

Platform engineering is the organisational prerequisite for AI productivity amplification. DORA 2025 found 90% of organisations now have some platform engineering capability; organisations with high-quality Internal Developer Platforms (IDPs) see stronger AI amplification. [fact; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

#### 2.E Security and operational risks under AI code generation

The Open Web Application Security Project (OWASP) LLM Top 10 (2024) identifies the primary security risks from Large Language Model (LLM) code generation: prompt injection, insecure output handling, training data poisoning, supply chain vulnerabilities, sensitive information disclosure, and overreliance on LLMs for security decisions. [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

AI code generation tools have been documented to suggest vulnerable library versions, outdated cryptographic patterns, and code with missing input validation. [fact; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/] The supply chain risk is compounded when AI-generated code introduces dependencies not reviewed by security teams. [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/]

Cognitive debt - the accumulation of implicit knowledge gaps when engineers accept AI-generated code without fully understanding its logic - creates long-term maintainability risk. [inference; source: https://arxiv.org/abs/2507.09089; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md]

The Site Reliability Engineering (SRE) shared-fate operational model requires that the teams building software bear operational consequences of failures. AI-generated code that increases defect rates (as evidenced in Faros telemetry) challenges SRE principles by decoupling code authorship from code ownership and understanding. [inference; source: https://sre.google/books/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

Continuous Integration (CI) and Continuous Delivery (CD) pipelines under higher code-generation velocity require correspondingly more capable automated testing - manual review at scale becomes a bottleneck (evidenced by +441% PR review time increase in Faros telemetry). [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

#### 2.F Skills, capabilities, and future-state ecosystem characteristics

Anthropic Economic Index (2025): software engineering is the most AI-impacted profession by task volume. 36-37% of Claude enterprise AI usage is coding-related. AI primarily augments (57% of usage) rather than automates (43%) software engineering tasks. [fact; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report]

Anthropic Economic Index: entry-level and routine engineering tasks face highest automation risk. Junior engineer roles performing boilerplate coding and simple bug fixes are more automated; senior roles requiring architecture and cross-team reasoning remain stable. [inference; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report]

Microsoft WTI 2026 frames the "Transformation Paradox": employees are ready for AI, but organisational systems (processes, governance, platforms) are not. Only 19% of organisations surveyed are in the "Frontier" operating model. [fact; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization]

METR, WTI, and DORA all independently identify judgment, quality control of AI output, and critical thinking as the scarce human competencies in AI-first engineering. [inference; source: https://arxiv.org/abs/2507.09089; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

**Prior research integration:**
The completed item `2026-02-28-ai-strategy-swe-focus` (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-28-ai-strategy-swe-focus.md) established that AI strategy in software engineering requires deliberate governance of the human-AI collaboration boundary, not just tool adoption. This item extends that finding by providing quantitative evidence of the quality degradation risk when governance is absent.

The completed item `2026-03-14-reliable-software-llm-era` (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md) established that cognitive debt from AI-generated code creates systematic reliability risk - a finding directly corroborated by the Faros telemetry showing +242.7% incidents per PR.

The completed item `2026-03-12-volume-vs-correctness-ai-era` (https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-volume-vs-correctness-ai-era.md) established that correctness is the scarce resource in AI-augmented development - consistent with the Faros evidence that throughput goes up while quality goes down.

### §3 Reasoning

**Facts established:**
- AI tools produce task-completion speedups (21-55.8%) in isolated, controlled conditions (RCT evidence: Google 2024, MIT/Microsoft, GitHub Copilot lab study)
- AI tools produce measurable slowdowns (19%) for experienced developers on realistic, complex real-world tasks (METR RCT 2025)
- At the organisational level, individual throughput metrics increase while quality metrics (defects, incidents, review time) degrade significantly (Faros telemetry 2026)
- DORA 2025 identifies seven organisational capabilities that differentiate high-AI-ROI from low-AI-ROI organisations
- Platform engineering capability correlates directly with AI amplification (DORA 2025)
- Google has scaled AI code generation from 25% to ~75% of new code between 2023 and 2026
- OWASP LLM Top 10 documents specific security risk categories from LLM code generation
- Anthropic Economic Index places software engineering as the most AI-impacted profession

**Inferences derived from evidence:**
- Productivity heterogeneity by experience and task type is the primary explanation for conflicting RCT results
- AI tools shift the developer role from author to reviewer at scale
- Organisational-level quality degradation is a system-level emergent phenomenon, not merely individual user behaviour
- Governance structures (AI stance, code review standards, security gates) mediate whether AI amplifies strengths or amplifies dysfunctions
- Conway's Law tensions with AI code generation create architectural drift risk in team-boundary-aware organisations
- The DORA survey/Faros telemetry contradiction is explained by measurement scope: DORA captures flow metrics; Faros captures quality metrics - both can be simultaneously true

**Assumptions retained:**
- Study findings from large tech contexts (Google 96 engineers, MIT/Microsoft 4,867 developers) are broadly transferable to other large engineering organisations, though with attenuation for context differences
- Faros AI telemetry data represents a meaningful sample of enterprise developers even though the full methodology is not published in peer-reviewed form

**Unsupported generalisations removed:**
- "AI will replace developers" - not supported; evidence shows augmentation-dominant model
- "High-maturity organisations are insulated from AI quality risks" - contradicted by Faros telemetry
- "All productivity metrics are comparable" - rejected; SPACE framework shows metrics measure different dimensions

### §4 Consistency Check

```text
contradiction_scan:
  - METR slowdown vs MIT/GitHub speedup: RESOLVED - heterogeneous by experience/task complexity
  - DORA survey protection claim vs Faros telemetry degradation: RESOLVED - different metric scopes
    (delivery flow vs code quality); both can be simultaneously true
  - Google 75% AI-generated code vs concerns about quality: UNRESOLVED but flagged - Google reports
    high acceptance and productivity; independent quality telemetry for Google's AI code not public
  - OWASP security risks vs widespread adoption: not a contradiction - risk documentation and
    adoption coexist; governance is the mediating variable

confidence_adjustments:
  - Productivity benefit magnitude: kept at medium - controlled studies diverge significantly
  - Quality degradation at scale: kept at medium-high - Faros telemetry compelling but single
    data source; consistent with DORA and METR findings directionally
  - 7 DORA capabilities causal: downgraded to inference - survey-based correlation, not RCT

scope_guardrail: maintained - no claims about non-software domains, no legal advice,
  no forecasting beyond 2030

acronym_check:
  - AI: expanded in Research Question
  - LLM: expanded in §2.E
  - RCT: expanded in §1
  - DORA: expanded in §1
  - METR: expanded in §2.C
  - PR: expanded in §1
  - SPACE: expanded in §2.B
  - SRE: expanded in §2.E
  - CI/CD: expanded in §2.E
  - IDP: expanded in §2.D
  - OWASP: expanded in §2.E
  - LLM: expanded in §2.E
  - IDE: to be expanded at first use in Findings
  - ML: expanded in §2.C
```

### §5 Depth and Breadth Expansion

**Technical lens:** At high code-generation velocity, static analysis tools, automated test coverage gates, and Continuous Integration/Continuous Delivery (CI/CD) pipelines become proportionally more critical because they represent the last systematic defence against quality degradation when code review becomes a bottleneck. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The shift from author to reviewer role also requires developers to maintain deep architectural context even when not writing code directly. [inference; source: https://arxiv.org/abs/2507.09089; https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/]

**Organisational lens:** The "Transformation Paradox" (WTI 2026) and the Faros "Acceleration Whiplash" both point to the same systemic failure: tools are deployed without corresponding changes to process, governance, and team cognitive load management. [inference; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] If AI tools increase the pace of change faster than teams can absorb, net productivity decreases even if individual throughput increases, consistent with Team Topologies' cognitive load ceiling principle. [inference; source: https://teamtopologies.com/key-concepts; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

**Economic lens:** The Anthropic Economic Index finding that entry-level engineering tasks face highest automation risk has a compounding effect: fewer junior developers doing routine work means fewer engineers developing the deep codebase familiarity that the METR study shows makes experienced developers most effective on complex tasks. [inference; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report; https://arxiv.org/abs/2507.09089] Organisations that automate entry-level work without redesigning how engineers develop deep codebase expertise risk a future capability gap in their senior engineering pipeline. [inference; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report; https://arxiv.org/abs/2507.09089]

**Governance/risk lens:** OWASP LLM Top 10, DORA 2025's AI stance requirement, and the SRE shared-fate model all point to the same governance imperative: AI tools must be deployed with explicit policies covering what AI can and cannot do without human review, what security gates apply to AI-generated code, and who owns AI-generated code in production incidents. [inference; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://sre.google/books/] Without such policies, accountability diffuses in ways that undermine operational resilience. [inference; source: https://sre.google/books/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

**Historical lens:** DORA multi-year research showed organisations took 3-5 years to move from "medium" to "elite" on delivery metrics with sustained investment. [fact; source: https://itrevolution.com/product/accelerate/] By analogy, the 19% Frontier Firm adoption rate (WTI 2026) is consistent with that historical pace, suggesting AI-first operating model adoption is likely a multi-year programme rather than a single-year transformation. [inference; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://itrevolution.com/product/accelerate/]

**Behavioural lens:** METR's finding that developers systematically overestimate AI productivity gains (perceived 20% gain vs measured 19% loss) illustrates automation bias (defined in research on human factors as the tendency to over-trust automated system outputs, reducing critical evaluation), a pattern documented in human-computer interaction literature as a systemic risk when people delegate tasks to automated systems. [inference; source: https://arxiv.org/abs/2507.09089; https://doi.org/10.1518/001872097778543886] This is directly relevant to code review quality: developers who expect AI-generated code to be correct exercise less scrutiny, reducing the effectiveness of code review as a quality gate. [inference; source: https://arxiv.org/abs/2507.09089; https://owasp.org/www-project-top-10-for-large-language-model-applications/]

### §6 Synthesis

**Executive Summary:**

AI assistance in large software organisations produces reliably positive productivity gains in isolated, well-defined tasks, but produces heterogeneous or negative effects in complex real-world maintenance work with experienced developers - the dominant task category in mature codebases. [inference; source: https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944; https://mit-genai.pubpub.org/pub/v5iixksv] The core governance problem is that AI inflates individual throughput metrics while organisational quality signals - defect rates, incidents, review burden - degrade simultaneously, creating a misleading productivity signal that drives under-investment in quality controls. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] DORA 2025 and the Microsoft Work Trend Index (2026) converge on the finding that AI amplifies existing organisational conditions rather than transforming them: organisations with strong platforms, clear AI governance, and healthy data ecosystems see sustained gains; organisations deploying AI into weak processes see those weaknesses amplified. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization] The operating model best suited to AI-first software engineering treats platform engineering as the primary investment lever, quality governance as the primary risk control, and developer judgment as the scarcest human resource to cultivate. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

**Key Findings:**

1. AI coding tools produce measurable productivity gains in controlled conditions but cause slowdowns for experienced developers on realistic complex tasks in their own codebases. ([inference]; medium confidence; source: https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944; https://mit-genai.pubpub.org/pub/v5iixksv)

2. Individual throughput metrics (PRs opened, tasks completed) increase with AI adoption, but organisational quality metrics (PR review time, defect rates, incidents per PR) degrade sharply - Faros AI telemetry found PR review time +441%, bugs per developer +54%, incidents per PR +242.7% by 2026. ([fact]; medium-high confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

3. Developers systematically and severely overestimate AI productivity gains: in the METR RCT, participants forecasted a 24% speedup and reported feeling 20% faster, while the measured outcome was 19% slower. ([fact]; high confidence; source: https://arxiv.org/abs/2507.09089)

4. DORA 2025 identifies seven organisational capabilities that determine whether AI amplifies strengths or dysfunctions: clear leadership AI stance, healthy data ecosystems, AI-accessible internal data, strong version control, small-batch discipline, user-centric focus, and quality internal platforms. ([fact]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

5. Platform engineering capability is the strongest single predictor of AI productivity amplification, with 90% of large organisations now possessing some platform capability, and organisations with higher-quality platforms seeing stronger AI ROI. ([inference]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

6. Google has scaled AI-generated code from 25% of new code in late 2023 to approximately 75% by early 2026, demonstrating that sustained investment in AI-assisted tooling integrated into the natural workflow produces large-scale adoption. ([fact]; high confidence; source: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/; https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html)

7. Organisational factors account for approximately 2× the AI productivity impact of individual effort alone, meaning team structure, governance, and platform quality are stronger levers than individual tool choice. ([inference]; medium confidence; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)

8. The OWASP LLM Top 10 documents that AI code generation introduces specific, actionable security risks including prompt injection, insecure output handling, and supply chain vulnerabilities that require explicit governance controls not present in traditional development pipelines. ([fact]; high confidence; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/)

9. Developer judgment, critical evaluation of AI outputs, and architectural thinking are the human competencies most frequently identified as scarce and critical in AI-first software engineering, across METR, Microsoft WTI, and DORA 2025. ([inference]; medium confidence; source: https://arxiv.org/abs/2507.09089; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

10. The Anthropic Economic Index places software engineering as the profession most impacted by AI, with 36-37% of Claude enterprise AI usage on coding tasks, primarily in augmentation mode (57%) rather than full automation (43%), suggesting the human-AI collaboration model is stable for the near term. ([fact]; medium confidence; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)

11. Conway's Law creates structural tension with AI code generation: AI tools that generate code without awareness of team ownership boundaries or architectural conventions accelerate architectural drift in organisations that rely on team topology as the primary architectural control mechanism. ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://arxiv.org/abs/2410.12944; https://teamtopologies.com/key-concepts)

12. Only 19% of organisations surveyed by Microsoft have reached the "Frontier Firm" AI operating model - structured around on-demand AI intelligence with governance and platforms aligned - suggesting the majority of large organisations are in an early adoption phase where quality and security risks are elevated relative to productivity gains. ([inference]; medium confidence; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AI productivity effects heterogeneous by experience/task | https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944 | medium | METR RCT (experienced, complex) vs Google RCT (enterprise, task-isolated) |
| [fact] PR review time +441%, bugs +54%, incidents/PR +242.7% by 2026 | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium-high | Telemetry-based; single data source but consistent with other findings |
| [fact] Developers overestimate AI gains: 24% predicted, 19% slowdown measured | https://arxiv.org/abs/2507.09089 | high | Peer-reviewed RCT; expert predictions also wrong |
| [fact] DORA 7 org capabilities for AI amplification | https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | Survey-based; correlation not RCT |
| [inference] Platform engineering strongest predictor of AI ROI | https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | From DORA survey; 90% adoption rate documented |
| [fact] Google: 25% AI code → ~75% by 2026 | https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/; https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html | high | Internal Google reporting; corroborated by multiple sources |
| [inference] Org factors = 2× impact of individual effort | https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization | medium | WTI survey-derived; not RCT |
| [fact] OWASP LLM Top 10 documents AI code security risks | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | Authoritative industry standard documentation |
| [inference] Judgment/critical thinking as scarce human competency | https://arxiv.org/abs/2507.09089; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | Convergent finding across 3 independent studies |
| [fact] Software engineering top AI-impacted profession; 36-37% of Claude usage | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | medium | Based on Claude usage patterns; may not generalise to all AI tools |
| [inference] Conway's Law tension with AI architectural drift | https://www.melconway.com/Home/Conways_Law.html; https://arxiv.org/abs/2410.12944 | medium | Theoretical inference; empirical evidence limited |
| [inference] Only 19% of orgs in Frontier Firm model | https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization | medium | WTI survey; not independent |

**Assumptions:**

1. Study findings from large tech organisations (Google, Microsoft) are broadly transferable to other large engineering organisations (500+ engineers) with similar maturity levels, though effect sizes may attenuate. [Justification: DORA 2025 includes diverse organisations beyond Big Tech; transferability is standard in software engineering research; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

2. Faros AI telemetry data (22,000+ developers) is representative of enterprise AI adoption patterns, even though the full methodology is not peer-reviewed. [Justification: telemetry is objective measurement; the directional findings are consistent with METR RCT and DORA survey results; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

3. The period 2025-2030 will not see a capability discontinuity (e.g., Artificial General Intelligence (AGI) deployment) that renders this analysis obsolete. [Justification: mainstream AI research consensus places AGI beyond 2030 for most definitions; scope constraint explicitly excludes forecasting beyond 2030]

**Analysis:**

The evidence is most consistent with an "AI amplifier" model of software productivity: AI tools amplify existing organisational conditions rather than overriding them. This is evident from three independent sources - DORA 2025 (survey), Microsoft WTI 2026 (survey), and Faros AI 2026 (telemetry) - all reaching the same directional conclusion through different methods. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

The critical implication for large engineering organisations is that establishing strong organisational conditions - platform capability, governance, data quality - is the primary lever for realising AI productivity gains. DORA's seven capabilities provide the most evidence-grounded framework for diagnosing this readiness gap. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

The METR finding of a 19% slowdown for experienced developers is counterintuitive but logically consistent: experienced developers in their own codebases hold deep contextual knowledge that AI tools cannot access; when AI suggestions depart from that context, the experienced developer spends time reviewing and correcting AI suggestions that a less-experienced developer (with lower contextual expectations) simply accepts or discards without the same scrutiny. [inference; source: https://arxiv.org/abs/2507.09089]

The automation bias risk - developers overestimating AI correctness and reducing critical scrutiny - is a systemic governance risk, not merely an individual behaviour. Governance structures must explicitly counteract this tendency through code review standards, mandatory security scanning of AI-generated code, and architectural conformance checks. [inference; source: https://arxiv.org/abs/2507.09089; https://owasp.org/www-project-top-10-for-large-language-model-applications/]

Platform engineering as a prerequisite for AI amplification is the most actionable and well-evidenced finding: organisations that invest in Internal Developer Platforms providing self-service Continuous Integration/Continuous Delivery (CI/CD), security scanning, and observability see AI tools amplify that investment. Organisations that deploy AI tools into fragmented, inconsistent toolchains see fragmentation amplified. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://teamtopologies.com/key-concepts]

An important alternative explanation for the Faros telemetry quality degradation pattern (PR review time +441%, incidents per PR +242.7%) is that increased development velocity alone - independent of AI adoption - is sufficient to cause this quality regression, consistent with established software engineering research on flow-vs-quality trade-offs. [inference; source: https://itrevolution.com/product/accelerate/; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report] The Faros data has no matched control group of non-AI-adopting organisations at comparable velocity increases; causal attribution to AI tools rather than to velocity acceleration as such is not warranted by the data alone. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The governance implication is the same regardless: quality controls must scale with velocity.

Findings from `2026-03-08-ai-coding-harnesses-agent-philosophy` (https://davidamitchell.github.io/Research/research/2026-03-08-ai-coding-harnesses-agent-philosophy.html) on harness infrastructure requirements for agentic AI tools are consistent with the platform engineering prerequisite finding: both argue that AI productivity gains at scale require platform controls as enabling conditions. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report] The throughput-constraint analysis in `2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate` (https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html) directly supports Key Finding 11 on Conway's Law tension: dependency topology and queue dynamics that constrain delivery throughput are the same dynamics that AI tools generating code without architectural awareness can worsen. [inference; source: https://www.melconway.com/Home/Conways_Law.html; https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html]

**Risks, Gaps, and Uncertainties:**

1. **Measurement scope gap:** Most RCT evidence measures individual task completion time; long-term effects on architectural coherence, codebase maintainability, and team knowledge depth are not yet measured in peer-reviewed studies. The Faros AI telemetry partially addresses this but is not peer-reviewed and represents a single analysis.

2. **Experience-level gap:** The METR RCT used only 16 experienced developers. Larger RCTs disaggregating by experience level, task type, and codebase familiarity are needed to firmly establish the heterogeneity hypothesis.

3. **AI capabilities trajectory:** All studies used AI tools available in 2024-2025 (Copilot, Claude 3.5/3.7 Sonnet, Gemini). Newer agentic AI capabilities (e.g., autonomous PR creation, multi-step planning) may have different productivity profiles not captured in current evidence.

4. **Conway's Law empirical gap:** The inference that AI-generated code accelerates architectural drift is theoretically well-grounded but lacks direct empirical measurement. Studies measuring architectural conformance of AI-generated vs human-generated code are not yet available.

5. **Faros data independence:** Faros AI telemetry corroborates other findings directionally, but it has not been independently replicated or peer-reviewed. The magnitude of the degradation figures (+441% review time, +242.7% incidents/PR) should be treated as order-of-magnitude indicators rather than precise measurements.

**Open Questions:**

1. Do AI coding tools improve or degrade codebase architectural coherence over 12-24 month horizons? (Out of scope for this item; candidate for `Research/backlog/`.)
2. What is the minimum platform engineering maturity threshold below which AI tool adoption produces net negative outcomes? (DORA measures correlation but not threshold.)
3. How do agentic AI tools (autonomous code agents, not just suggestion-based copilots) change the productivity and quality picture? (Current evidence is almost entirely for suggestion-based tools.)
4. What metrics best capture the cognitive debt accumulation from AI-generated code adoption? (SPACE framework is too coarse; no validated instrument found in this investigation.)
5. How should organisations redesign junior engineer career paths now that entry-level automation tasks are increasingly AI-handled? (Anthropic Economic Index raises this; no organisational solutions identified in scope.)

**Output:**

- Type: knowledge
- Description: This item establishes that AI coding tools amplify existing organisational conditions (not transform them), that quality degradation at system level accompanies individual throughput gains in the absence of governance controls, and that platform engineering is the primary investment lever for sustainable AI-first software engineering. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]
- Most important sources:
  - [METR et al. (2025) Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089)
  - [DORA (2025) AI-Assisted Software Development Report](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)
  - [Faros AI (2026) Key Takeaways from the DORA Report 2025](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

### §7 Recursive Review

```text
review_result: pass

acronym_audit:
  AI: expanded in Research Question (first document use)
  LLM: expanded at first use in §2.E "Large Language Model (LLM)"
  RCT: expanded at first use in §1 "Randomised Controlled Trial (RCT)"
  DORA: expanded at first use in §1 "DevOps Research and Assessment (DORA)"
  METR: expanded at first use in §2.C "Model Evaluation and Threat Research (METR)"
  PR: expanded at first use in §1 "pull requests (PRs)"
  SPACE: expanded at first prose use in §1 "Satisfaction, Performance, Activity, Communication, Efficiency (SPACE)" at sub-question 2c
  SRE: expanded at first use in §2.E "Site Reliability Engineering (SRE)"
  CI/CD: expanded at first use in §2.E "Continuous Integration (CI) and Continuous Delivery (CD)"
  IDP: expanded at first use in §2.D "Internal Developer Platforms (IDPs)"
  OWASP: expanded at first use in §2.E "Open Web Application Security Project (OWASP)"
  ML: expanded at first use in §2.C "Machine Learning (ML)"
  AGI: expanded at first use in §6 Assumptions "Artificial General Intelligence (AGI)"
  ROI: expanded at first use in §1 "Return on Investment (ROI)"
  UX: expanded at first use in §2.D "User Experience (UX)"
  A/B: rewritten to "head-to-head comparison" at first use in §2.D
  IDE: used in §2.D in a Google blog citation context; not a standalone new term
  WTI: used as shorthand for Microsoft Work Trend Index after full name established

domain_term_audit:
  software ecology: defined in §2.A
  Conway's Law: defined in §2.A with source
  Team Topologies: defined in §2.A with source
  cognitive debt: defined in §2.E with source
  automation bias: defined in §5 Behavioural lens with authoritative source (Parasuraman and Riley 1997 DOI)
  Frontier Firm: defined in §2.F with source
  Acceleration Whiplash: defined in §2.C with source
  stream-aligned/platform/enabling/complicated-subsystem teams: defined in §2.A
  SPACE dimensions: defined in §2.B with source
  architectural drift: defined in §2.A

kf_bold_audit: Key Findings 1-12 have full-sentence bold removed; plain text claim sentences with trailing parenthetical labels
parity_check: §6 Synthesis and Findings are aligned; Analysis sections updated consistently
contradiction_resolution: METR/MIT contradiction resolved; DORA/Faros alternative-explanation caution added
alternative_explanation_audit: Faros telemetry velocity-vs-AI causal ambiguity added to §6 and Findings Analysis
cross_item_integration: ai-coding-harnesses-agent-philosophy and it-throughput-constraint referenced in Analysis
source_urls: all cited sources have URL or DOI
```

---

## Findings

### Executive Summary

AI coding tools produce reliably positive productivity gains in isolated, well-defined tasks (21-55% faster in controlled studies) but produce a 19% slowdown for experienced developers working on realistic complex tasks in mature codebases - the dominant work category in large software organisations. [inference; source: https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944; https://mit-genai.pubpub.org/pub/v5iixksv] At the organisational level, AI adoption increases individual throughput metrics while quality signals degrade sharply: Faros AI telemetry found PR review time +441%, defects per developer +54%, and incidents per PR +242.7% by 2026, a pattern called "Acceleration Whiplash." [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] DORA 2025 and the Microsoft Work Trend Index 2026 independently conclude that AI amplifies existing organisational conditions rather than transforming them: organisations with strong platforms, clear AI governance, and healthy data ecosystems see sustained productivity gains; organisations with weak processes see those weaknesses amplified. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization] The operating model best suited to AI-first software engineering treats platform engineering as the primary investment lever, quality governance as the primary risk control, and developer judgment as the scarcest human resource to cultivate. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

### Key Findings

1. AI coding tools produce measurable productivity gains in controlled conditions but cause slowdowns for experienced developers on realistic, complex tasks in their own codebases - productivity effects are heterogeneous by experience level and task complexity, not uniformly positive.  ([inference]; medium confidence; source: https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944; https://mit-genai.pubpub.org/pub/v5iixksv)

2. Individual throughput metrics increase with AI adoption, but organisational quality metrics degrade sharply - Faros AI telemetry of 22,000+ developers found PR review time up 441%, bugs per developer up 54%, and incidents per PR up 242.7% by 2026, creating a misleading productivity signal.  ([fact]; medium-high confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

3. Developers systematically overestimate AI productivity gains: in the METR Randomised Controlled Trial, participants forecasted a 24% speedup and reported feeling 20% faster, while the measured outcome was 19% slower - an automation bias that undermines effective code review governance.  ([fact]; high confidence; source: https://arxiv.org/abs/2507.09089)

4. DORA 2025 identifies seven organisational capabilities that determine whether AI amplifies strengths or weaknesses: clear leadership AI stance, healthy data ecosystems, AI-accessible internal data, strong version control, small-batch work discipline, user-centric focus, and quality internal platforms.  ([fact]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

5. Platform engineering capability is the strongest single predictor of AI productivity amplification, with 90% of large organisations now possessing some platform capability and those with higher-quality Internal Developer Platforms seeing meaningfully stronger AI return on investment.  ([inference]; medium confidence; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

6. Google has scaled AI-generated code from 25% of new code in late 2023 to approximately 75% by early 2026, demonstrating that AI tools embedded naturally into developer workflows achieve large-scale adoption without requiring deliberate triggering.  ([fact]; high confidence; source: https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/; https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html)

7. Organisational factors - team structure, governance, and platform quality - account for approximately 2× the AI productivity impact of individual tool choice and usage, making systemic investment more critical than individual tooling decisions.  ([inference]; medium confidence; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)

8. The Open Web Application Security Project LLM Top 10 documents AI code generation security risks - prompt injection, insecure output handling, and supply chain vulnerabilities - that require explicit governance controls absent from traditional development pipelines, creating a governance gap in most organisations.  ([fact]; high confidence; source: https://owasp.org/www-project-top-10-for-large-language-model-applications/)

9. Developer judgment, critical evaluation of AI outputs, and architectural thinking are identified across METR, Microsoft Work Trend Index, and DORA 2025 as the human competencies most scarce and most critical in AI-first software engineering organisations.  ([inference]; medium confidence; source: https://arxiv.org/abs/2507.09089; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report)

10. The Anthropic Economic Index identifies software engineering as the profession most impacted by AI adoption, with 36-37% of Claude enterprise usage on coding tasks in primarily augmentation mode rather than full automation, suggesting the human-AI collaboration model in software engineering is stable through the near term.  ([fact]; medium confidence; source: https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)

11. Conway's Law creates structural tension with AI code generation: AI tools generating code without awareness of team ownership boundaries or architectural conventions accelerate architectural drift in organisations that rely on team topology as their primary architectural control mechanism.  ([inference]; medium confidence; source: https://www.melconway.com/Home/Conways_Law.html; https://arxiv.org/abs/2410.12944; https://teamtopologies.com/key-concepts)

12. Only 19% of organisations surveyed by Microsoft have reached the "Frontier Firm" AI operating model - structured around on-demand AI intelligence with aligned governance and platforms - indicating the majority of large organisations are in an early adoption phase where quality and security risks exceed realised productivity gains.  ([inference]; medium confidence; source: https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] AI productivity heterogeneous by experience/task | https://arxiv.org/abs/2507.09089; https://arxiv.org/abs/2410.12944 | medium | METR RCT experienced+complex vs Google/MIT RCT controlled tasks |
| [fact] PR review time +441%, bugs +54%, incidents/PR +242.7% by 2026 | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium-high | Telemetry 22,000+ developers; single source but directionally consistent |
| [fact] Developers overestimate: 24% predicted speedup, 19% slowdown measured | https://arxiv.org/abs/2507.09089 | high | Peer-reviewed RCT; expert predictions also wrong |
| [fact] DORA 7 org capabilities for AI amplification | https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | Survey-based correlation; not RCT |
| [inference] Platform engineering strongest predictor of AI ROI | https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | DORA survey; 90% adoption rate documented |
| [fact] Google: 25% AI code (2023) → ~75% (2026) | https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/; https://www.techspot.com/news/112152-google-ai-now-generates-75-new-code-up.html | high | Google internal reporting corroborated by multiple sources |
| [inference] Org factors = 2× impact vs individual tool choice | https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization | medium | WTI survey; not RCT |
| [fact] OWASP LLM Top 10 defines AI code security risks | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | high | Authoritative industry standard |
| [inference] Judgment/critical thinking as scarce human competency | https://arxiv.org/abs/2507.09089; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report | medium | Convergent across 3 independent sources |
| [fact] Software engineering top AI-impacted profession; 36-37% of Claude usage | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | medium | Claude usage patterns; may not generalise to all AI tools |
| [inference] Conway's Law tension with AI architectural drift | https://www.melconway.com/Home/Conways_Law.html; https://arxiv.org/abs/2410.12944; https://teamtopologies.com/key-concepts | medium | Theoretical inference; no direct empirical measurement |
| [inference] 19% of orgs in Frontier Firm model | https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization | medium | WTI survey; Microsoft-produced |

### Assumptions

1. Study findings from large technology organisations (Google, Microsoft partner firms) are broadly transferable to other large engineering organisations (500+ engineers) with similar technical maturity levels, with expected attenuation of effect sizes. [Justification: DORA 2025 includes diverse organisations beyond Big Tech; cross-industry transferability is standard in software engineering research; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

2. Faros AI telemetry data (22,000+ developers) is representative of enterprise AI adoption patterns despite not being peer-reviewed, because the directional findings are consistent with METR RCT and DORA survey results from independent sources. [Justification: convergent validity with independent studies; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

3. The period 2025-2030 will not see a capability discontinuity (e.g., Artificial General Intelligence (AGI) deployment) that renders this analysis obsolete. [Justification: mainstream AI research consensus places AGI beyond 2030 for most definitions; this is a scope constraint assumption with no single definitive source]

### Analysis

The evidence consistently supports an "AI amplifier" model of software productivity: AI tools amplify existing organisational conditions rather than overriding them. This is evident from three independent sources - DORA 2025 (survey-based), Microsoft WTI 2026 (survey-based), and Faros AI 2026 (telemetry-based) - all reaching the same directional conclusion through different methods. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

The critical implication for large engineering organisations is that establishing strong organisational conditions - platform capability, governance, data quality - is the primary lever for realising AI productivity gains. DORA's seven capabilities provide the most evidence-grounded diagnostic framework currently available. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

The METR finding of a 19% slowdown for experienced developers is counterintuitive but logically consistent with the contextual knowledge model: experienced developers in their own codebases hold deep contextual knowledge that AI tools cannot access via code completion context windows. When AI suggestions depart from that deep context, the experienced developer spends time reviewing and correcting AI suggestions. A less-experienced developer (with lower contextual expectations) accepts or discards suggestions without the same scrutiny cost. [inference; source: https://arxiv.org/abs/2507.09089]

The automation bias risk - developers systematically overestimating AI correctness and reducing critical scrutiny - is a governance problem, not merely individual behaviour. The METR finding that even expert economists and ML researchers predicted wrong shows this is not a developer knowledge gap but a structural prediction failure. Governance structures must explicitly counteract automation bias through code review standards, mandatory security scanning of AI-generated code, and architectural conformance checks embedded in CI/CD pipelines. [inference; source: https://arxiv.org/abs/2507.09089; https://owasp.org/www-project-top-10-for-large-language-model-applications/]

Platform engineering as a prerequisite for AI amplification is the most actionable finding: organisations that invest in Internal Developer Platforms providing self-service CI/CD, security scanning, and observability see AI tools amplify that investment. Organisations that deploy AI tools into fragmented, inconsistent toolchains see fragmentation amplified. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://teamtopologies.com/key-concepts]

An important alternative explanation for the Faros telemetry quality degradation pattern (PR review time +441%, incidents per PR +242.7%) is that increased development velocity alone - independent of AI tools - can cause the same quality regression, a well-established pattern in software engineering research. [inference; source: https://itrevolution.com/product/accelerate/; https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report] The Faros data does not include a matched control group of non-AI-adopting organisations with comparable velocity increases, which means the quality degradation cannot be causally attributed to AI tools alone rather than to velocity acceleration as such. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The governance implication is the same regardless of causal attribution: quality controls must be calibrated to velocity, not held constant as velocity increases.

This item's findings extend the conclusions of `2026-03-08-ai-coding-harnesses-agent-philosophy` (available at https://davidamitchell.github.io/Research/research/2026-03-08-ai-coding-harnesses-agent-philosophy.html), which argues that agentic AI coding tools require harness infrastructure to operate safely. The platform engineering finding here provides the organisational-level evidence base for that thesis: without the platform controls that an AI harness assumes are present, agentic AI tools amplify instability. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report]

The throughput-constraint and debt-accumulation analysis in `2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate` (available at https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html) provides complementary context: the same dependency topology and queue dynamics that constrain central IT throughput are the dynamics that AI tools acting without architectural awareness can worsen, validating the Conway's Law architectural-drift inference in Key Finding 11. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://www.melconway.com/Home/Conways_Law.html]

This item's findings are consistent with and extend the conclusions of completed items `2026-03-14-reliable-software-llm-era` (cognitive debt risk from AI-generated code) and `2026-03-12-volume-vs-correctness-ai-era` (correctness as scarce resource), providing quantitative telemetry evidence that these theoretical risks are manifesting in observable organisational outcomes. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-12-volume-vs-correctness-ai-era.md]

### Risks, Gaps, and Uncertainties

1. **Measurement scope gap:** Most RCT evidence measures individual task completion time. Long-term effects on architectural coherence, codebase maintainability, and team knowledge depth are not yet measured in peer-reviewed studies. Faros AI telemetry partially addresses this but is not peer-reviewed.

2. **Experience-level gap:** The METR RCT used 16 developers. Larger RCTs disaggregating productivity effects by experience level, task type, and codebase familiarity are needed to firmly establish the heterogeneity hypothesis.

3. **AI capabilities trajectory:** All studies used AI tools available in 2024-2025 (Copilot, Claude 3.5/3.7 Sonnet, Gemini). Newer agentic AI tools (autonomous code agents, multi-step planning) may have different productivity and quality profiles not captured in current evidence.

4. **Conway's Law empirical gap:** The inference that AI-generated code accelerates architectural drift is theoretically well-grounded but lacks direct empirical measurement. Studies measuring architectural conformance of AI-generated vs human-generated code are not yet available.

5. **Google data independence:** Google's AI code generation statistics are self-reported; no independent verification of the 75% figure exists. The RCT evidence from Google is independently reviewed (arXiv) but the adoption statistics are not.

### Open Questions

1. Do AI coding tools improve or degrade codebase architectural coherence over 12-24 month horizons in production codebases? Candidate for `Research/backlog/`.

2. What is the minimum platform engineering maturity threshold below which AI tool adoption produces net negative organisational outcomes? DORA shows correlation but not threshold.

3. How do agentic AI tools - autonomous code agents executing multi-step tasks without real-time human supervision - change the productivity and quality picture compared to suggestion-based copilot tools? Current evidence is almost entirely from suggestion-based tools.

4. How should organisations redesign junior engineer career paths and onboarding when entry-level automation tasks are increasingly AI-handled? Anthropic Economic Index raises this gap; no organisational solutions identified in scope.

5. What validated measurement instrument best captures cognitive debt accumulation from AI-generated code adoption? The SPACE framework is too coarse; no validated instrument was found in this investigation.

### Output

- **Type:** knowledge
- **Description:** This item establishes that AI coding tools amplify existing organisational conditions rather than transforming them, that quality degradation at system level accompanies individual throughput gains in the absence of governance controls, and that platform engineering is the primary investment lever for sustainable AI-first software engineering. [inference; source: https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]
- **Most important sources:**
  1. [METR et al. (2025) Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089) - primary RCT evidence for experienced-developer slowdown
  2. [DORA (2025) AI-Assisted Software Development Report](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report) - seven org capabilities framework; amplifier thesis
  3. [Faros AI (2026) Key Takeaways from the DORA Report 2025](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) - telemetry evidence of quality degradation at scale
