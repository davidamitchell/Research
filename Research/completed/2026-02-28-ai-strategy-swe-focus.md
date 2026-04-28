---
title: "AI Strategy Examples: Software Engineering Focus"
added: 2026-03-05T06:57:04+00:00
status: completed
priority: medium
tags: [ai-strategy, software-engineering, developer-productivity, code-generation, agentic-swe]
started: 2026-03-05T06:57:04+00:00
completed: 2026-03-05T06:57:04+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# AI Strategy Examples: Software Engineering Focus

## Research Question

Which organisations have published or disclosed coherent AI strategies specifically targeting software engineering, what outcomes have they measured, and what does the trajectory from AI-assisted coding (Type 2) to autonomous software agents (Type 3/4) look like in practice?

## Scope

**In scope:**
- Corporate AI strategies explicitly targeting SWE productivity: code generation, review, test generation, documentation, deployment automation
- Organisations that have disclosed SWE AI programme results with measurable outcomes (cycle time, defect rates, PR throughput, cost per feature)
- The progression from copilot-style augmentation (Type 1) through agentic builders (Type 2) toward autonomous coding agents (Type 3)
- Governance models for AI-generated code: review standards, liability, IP ownership
- NZ-relevant examples where accessible

**Out of scope:**
- Pure research papers on AI coding models (not implementation strategies)
- SWE AI tool comparisons (not a product review question)
- General developer experience surveys without strategy context

**Constraints:** Focus on implementation strategy and outcomes, not model benchmarks.

## Context

The AI strategy research item (completed 2026-02-28) used the four-type typology: augmentation, agentic builders, delegated authority agents, and fully agentic business units. SWE is the clearest near-term domain for Type 2 → Type 3 progression: AI building artefacts that are reviewed by humans (Type 2), then AI making deployment decisions within defined parameters (Type 3). Understanding which organisations are navigating this transition deliberately and what governance structures they are using is directly applicable to technology-led organisations in NZ.

The Jevons Paradox research item (completed 2026-02-28) raised the open question of whether AI reducing code production costs leads to proportional increases in code produced — the SWE AI strategy question is inseparable from that demand-response dynamic.

**Prior research:** The completed AI strategy item (2026-02-28-ai-strategy.md) established the four-type use-case typology and noted SWE as the clearest near-term Type 2 domain but did not investigate specific SWE programme outcomes. The AI business efficiency examples item (2026-02-28-ai-strategy-business-efficiency-examples.md) documented the ANZ Bank case in depth (40-55% faster code delivery, 3,000+ engineers) and McKinsey's DVI framework, but from an efficiency lens rather than a strategy and governance lens. This item must add: specificity about SWE governance models, the agentic coding agent frontier (SWE-bench, Copilot Workspace/Agent, Devin), IP/liability frameworks for AI-generated code, and NZ technology sector context.

## Approach

1. **Survey published cases** — identify 6–10 organisations that have disclosed SWE AI strategy and outcomes. Include at least one hyperscaler (e.g., Google, Microsoft), one large financial services firm, one smaller tech company.
2. **Extract design variables** — AI system type used, human oversight model, IP and liability governance, time to measurable outcome, failure modes encountered.
3. **Governance pattern analysis** — what review and approval processes for AI-generated code are being used? What quality gates exist?
4. **Agentic SWE frontier** — document current state of autonomous coding agents (e.g., Devin, SWE-agent, GitHub Copilot Workspace) and what the evidence says about their real-world performance.
5. **NZ context** — how do NZ technology organisations (typically smaller teams, less specialised) adapt global SWE AI strategies?

## Sources

- [x] GitHub Octoverse: developer productivity impact of AI coding tools (2023, 2024) — https://octoverse.github.com/
- [x] Google AI impact on engineering productivity (internal reports surfaced in press)
- [x] McKinsey "Developer Velocity" report (AI-assisted coding outcomes) — https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/developer-velocity-at-work-key-lessons-from-industry-digital-leaders
- [ ] Proxify, MomoView, Kamiwaza — cited in Jevons Paradox research as early indicators
- [x] SWE-bench evaluations: autonomous coding agent performance data — https://www.swebench.com/
- [ ] NZ tech company case studies: Xero, Trade Me, Datacom AI SWE programmes (if disclosed)
- [ ] ACM and IEEE published SWE AI governance frameworks

---

## Research Skill Output

### §0 Initialise

**Research question restated:** Which organisations have published or disclosed coherent AI strategies specifically targeting software engineering, what outcomes have they measured, and what does the trajectory from AI-assisted coding (Type 2) to autonomous software agents (Type 3) look like in practice?

**Scope confirmed:** Organisational strategies and disclosed outcomes only — not model benchmarks, not tool reviews. Focus areas: (a) concrete productivity/quality metrics from named organisations, (b) governance models for AI-generated code, (c) current state of autonomous coding agents, (d) NZ context.

**Constraints:** Evidence must be from named organisations with disclosed data. Speculative claims about future states must be labelled [inference] or [assumption]. Primary sources (peer-reviewed papers, earnings calls, official company disclosures) receive higher weight than secondary aggregators.

**Output format:** Structured synthesis with evidence map, key findings, governance patterns, and NZ-specific section.

---

### §1 Question Decomposition

Root question broken into atomic sub-questions:

**Branch A — Organisational strategies and outcomes**
- A1: What specific productivity metrics has Microsoft/GitHub disclosed for GitHub Copilot adoption at scale?
- A2: What has Google disclosed about AI's share of code production and its impact on engineering workflows?
- A3: What outcomes has ANZ Bank reported from its 3,000-engineer GitHub Copilot deployment?
- A4: What has DORA (Google's State of DevOps) found about AI's effect on delivery performance metrics?
- A5: What productivity outcomes do financial services firms (JPMorgan, Goldman Sachs) report from AI coding programmes?

**Branch B — Governance models**
- B1: What human oversight models are organisations using for AI-generated code?
- B2: What is the IP and copyright status of AI-generated code?
- B3: What security and quality gate practices are documented?

**Branch C — Agentic SWE frontier**
- C1: What is Devin's documented performance on SWE-bench and how has the benchmark evolved?
- C2: What is GitHub Copilot Workspace/Coding Agent's current capability profile?
- C3: Where does autonomous coding agent performance fall short of human parity?

**Branch D — NZ context**
- D1: Have NZ technology companies (Xero, Trade Me, Datacom) disclosed SWE AI outcomes?
- D2: What does the ANZ case (Australian parent) imply for the NZ technology sector?

---

### §2 Investigation

**A1 — GitHub Copilot controlled study (Microsoft/GitHub/MIT, 2023)**

A peer-reviewed RCT (arXiv 2302.06590, published Microsoft Research) assigned ~95 professional developers from Upwork to treatment (GitHub Copilot) and control (no Copilot) groups on a single task: implement an HTTP server in JavaScript. Results: Copilot group completed the task 55.8% faster (1h11m vs 2h41m; 95% CI: 21–89%; P=0.0017). Less experienced and older developers benefited most. The task scope was narrow — a single well-specified algorithmic task — and the result does not generalize directly to complex multi-file enterprise work. [fact — source: arxiv 2302.06590]

GitHub's enterprise Accenture study (GitHub blog, 2024) found 90%+ of enterprise developers report greater job fulfilment when using Copilot, and code suggestion acceptance rates of 21–24%. [fact — source: GitHub blog enterprise study] The study is vendor-sponsored; treat quantitative claims as directional.

**A2 — Google's AI-generated code share**

Sundar Pichai confirmed on Alphabet earnings calls (confirmed for Q3 2024) that more than 25% of Google's new code is now AI-generated, reviewed by engineers before submission. This applies to production code across Search, Cloud, and YouTube products. [fact — source: Alphabet investor relations, earnings calls 2024] The specific figure was not audited independently; [assumption] it is treated as directional rather than precise.

**A3 — ANZ Bank GitHub Copilot deployment**

ANZ deployed GitHub Copilot to 3,000 engineers following an internal controlled trial of 1,000 engineers. Reported outcomes: 40–55% faster code development; improvement in code quality (fewer bugs, fewer "code smells"); improved documentation and unit test creation practices. The CTO (Tim Hogarth) framed the deployment as part of a broader generative AI programme with regulatory compliance safeguards. [fact — sources: Finextra 43689, iTnews 601195, The Register 2024-02-10] This is the most relevant regional case for NZ financial services organisations. Note: the 40-55% figure is from an internal trial using structured tasks; the external validity to broader engineering work is unclear but consistent with the GitHub Copilot RCT directionally.

**A4 — DORA 2024 (Google Cloud, Accelerate State of DevOps)**

The 2024 DORA report (tens of thousands of survey respondents) found: 75%+ of developers use AI tools daily; for every 25% increase in AI adoption, teams report +2.1% productivity and +2.6% job satisfaction. However, higher AI adoption is associated with –7.2% delivery stability and –1.5% delivery throughput. Documented individual gains in code quality (+3.4%) and documentation (+7.5%) do not translate to organisational-level delivery performance improvement for most teams. 40% of developers report little to no trust in AI-generated code. [fact — source: Google Cloud DORA 2024 report, cloud.google.com/blog]

This finding is the most important empirical counterweight to the productivity headline numbers: individual speed gains do not automatically convert to team-level delivery improvement without process redesign.

**A5 — Financial services AI coding programmes**

JPMorgan Chase deployed OmniAI and LLM Suite internally (200,000+ employees), with AI-assisted coding boosting developer productivity by 10–20%. All AI-generated code goes through human-in-the-loop review before production. The COiN platform (legal document review automation) is a documented precedent for AI handling high-volume structured tasks. [fact — source: Harvard Business School case study JPMorganChase GenAI, 5dvision.com case study]

Goldman Sachs piloted Devin (Cognition AI's autonomous coding agent) for code writing, review, and debugging under strict guardrails. No specific outcome metrics were disclosed publicly. [fact — source: qa-financial.com 2024] Morgan Stanley uses human-augmented AI workflows with model inventories and audit trails for all AI-generated code. [fact — source: qa-financial.com 2024, Phoenix Strategy Group]

**B1 — Human oversight models**

All documented financial services firms (JPMorgan, Goldman Sachs, Morgan Stanley, ANZ) require human review before AI-generated code enters production. GitHub's Copilot Coding Agent is designed with human-in-the-loop as a mandatory step: agents push to a draft pull request; branch protection rules and required human review apply before merge. [fact — source: GitHub newsroom, Azure DevOps blog] The industry pattern is: agentic code generation (Type 2) with human gate before deployment — not yet autonomous deployment (Type 3). [inference]

**B2 — IP and copyright status of AI-generated code**

AI-generated code without meaningful human authorship cannot be copyrighted in most jurisdictions (US Copyright Office rulings, UK IPO guidance). Organisations must document human contributions during AI-assisted code creation to maintain copyright eligibility. Up to 45% of AI-generated code may contain flaws at creation time, amplifying security review requirements. Code provenance checking tools (e.g., Tabnine Provenance and Attribution) have emerged to flag AI-generated outputs that match open-source code with restrictive licences. [fact — sources: MBHB law firm analysis, Tabnine blog, Norton Rose Fulbright IP analysis 2024]

**B3 — Security and quality gates**

The dominant enterprise pattern: AI coding tool → developer review → CI/CD pipeline → code review by human (mandatory) → merge. Autonomous coding agents (Copilot Coding Agent, Devin) add an outer loop: issue assigned to agent → agent creates PR → human reviews draft PR → human approves merge. Fine-grained access controls (GitHub Actions permissions, MCP integration) restrict what the agent can access during autonomous execution. [fact — source: GitHub newsroom Coding Agent, Azure blog Agentic DevOps]

**C1 — SWE-bench performance trajectory**

Devin (Cognition AI, March 2024): 13.86% on full SWE-bench (2,294 real-world GitHub issues); this was a new watermark at the time, more than doubling the prior baseline of ~4.8% (assisted) and the SWE-Agent result of 12.29%. [fact — source: Cognition AI SWE-bench technical report]

By early 2026: top agents (Claude Opus 4.5 + Live-SWE-agent scaffold) resolve ~79.2% on SWE-bench Verified (a curated, human-verified subset of 500 issues). On SWE-bench Pro (harder, multi-file enterprise tasks), best agents reach ~45.8%. On SWE-bench-Live (rolling monthly updates, mixed languages), top combinations reach ~36%. [fact — source: live-swe-agent.github.io, llm-stats.com/benchmarks/swe-bench-verified, swe-bench-live.github.io]

**Critical SWE-bench caveat:** A June 2025 analysis found that on discriminative subsets of SWE-bench Verified (problems not solvable by any agent two months prior), performance dropped from headline ~73% to ~11%. This suggests headline scores overstate generalised capability because agents cluster on solved/solvable problems. [fact — source: jatinganhotra.dev/blog/swe-agents/2025/06/05]

**C2 — GitHub Copilot Workspace / Coding Agent**

Copilot Workspace (technical preview, April 2024): users assign plain-English GitHub Issues; agent plans, generates code, and runs tests. Evolved into Copilot Coding Agent (September 2025 GA). By early 2025: 10,000+ organisations using agentic Copilot services; 15+ million developers using Copilot in some form. Best performance: low-to-medium complexity, well-specified tasks in well-maintained codebases. Documented limitations: struggles with architectural decisions, ambiguous requirements, and poorly documented legacy codebases. [fact — source: CIO Dive 2025, GitHub newsroom, Azure DevOps blog]

**C3 — Gaps in autonomous coding agent capability**

~10% of SWE-bench Verified problems remain unsolved by all current agents. Long-horizon, multi-repository, complex enterprise tasks are not well served. Real-world production performance is consistently lower than benchmark scores, typically by 10–20% for large or messy codebases. Autonomous deployment (no human review gate) is not in production use at any disclosed enterprise at scale. [inference — based on no documented counterexample in reviewed sources] The current industry state is Type 2 (agentic builder, human-reviewed artefact) not Type 3 (autonomous deployment with delegated authority).

**D1 — NZ technology company disclosures**

No public disclosures found for Xero, Trade Me, or Datacom on specific SWE AI programme outcomes or metrics as of early 2026. [fact — confirmed by search, no results returned] This absence is itself informative: NZ technology companies at this scale do not appear to be publishing outcome data. [assumption] The absence of disclosure does not mean absence of programmes; it reflects NZ organisations' typical preference for private implementation over public case study.

**D2 — ANZ implication for NZ financial sector**

ANZ's NZ operations are part of the same engineering organisation that deployed Copilot to 3,000+ engineers. The productivity gains documented in Australia are therefore directly applicable to ANZ NZ engineers. For other NZ financial services organisations (BNZ, Westpac NZ, Kiwibank), the ANZ case provides a comparable-scale data point. NZ team sizes are typically smaller (fewer than 200 engineers at most NZ tech companies outside Xero and large bank engineering functions), which may amplify or reduce the ANZ results depending on task mix and codebase maturity. [inference]

---

### §3 Reasoning

The evidence across A1–D2 supports three conclusions:

**Productivity gains are real but task-scoped.** The RCT evidence (55.8% faster in controlled experiment) and the ANZ deployment data (40–55% faster) are methodologically the strongest individual data points. Both measure task completion speed on well-specified coding tasks. The DORA 2024 finding that higher AI adoption associates with *worse* delivery stability and throughput at the team/organisational level is not contradictory — it reflects that individual speed gains do not automatically convert to delivery improvement without process redesign. McKinsey's Developer Velocity Index research corroborates: workflow integration, not tool deployment alone, determines business outcome.

**The agentic frontier is advancing faster than enterprise deployment.** SWE-bench performance has gone from ~14% (Devin, March 2024) to ~80% on curated tasks and ~46% on harder multi-file work in under two years. But the discriminative subset analysis shows headline leaderboard numbers are inflated relative to general capability. Real enterprise deployment is still predominantly Type 2 (agentic builder, human gate before deployment). No documented enterprise is operating Type 3 (autonomous deployment) at scale for production software.

**Governance has consolidated around the human-review gate.** All documented financial services firms and the major platform providers (GitHub, Microsoft) treat mandatory human review before code deployment as the non-negotiable control. IP ownership requires human authorship documentation. Security scanning of AI-generated code is mandatory in regulated environments. This governance pattern is likely to be durable regardless of how capable autonomous agents become, because liability frameworks have not shifted.

---

### §4 Consistency Check

The productivity data from the GitHub/MIT RCT (55.8%, controlled experiment) and the ANZ Bank internal trial (40–55%, internal) are directionally consistent and use similar methodology (measuring task completion time with/without AI assistance). Both measure individual developer speed on bounded tasks, not team-level delivery metrics. This distinction is preserved consistently across §2 and §3.

The DORA 2024 finding (delivery stability –7.2%, throughput –1.5% with higher AI adoption) appears to contradict the productivity gains, but the contradiction is resolved: the DORA metrics are organisational delivery metrics; the RCT/ANZ metrics are individual task-completion speed. Both can be true simultaneously if organisations deploy AI tools without redesigning their QA, review, and deployment processes.

The SWE-bench performance numbers (Devin 13.86% in 2024, ~80% Verified in early 2026) represent rapid progress but the discriminative subset caveat (73% headline → 11% on unsolved problems) means these numbers cannot be extrapolated to enterprise generalisability. This is noted consistently.

No unresolvable contradictions identified.

---

### §5 Depth and Breadth Expansion

**Economic lens (Jevons intersection):** The Jevons Paradox research item found no structural demand suppressors for AI-assisted code production. The DORA 2024 finding that faster individual coding does not translate to better delivery performance suggests a new bottleneck is emerging: human review capacity. As autonomous code agents produce more code faster, the binding constraint shifts from code generation to code review and QA. [inference] This creates a secondary demand for AI-assisted code review tools (a distinct market from AI coding tools), which is already emerging (GitHub Copilot code review, SonarQube AI features, CodeRabbit).

**Regulatory lens:** AI-generated code IP uncertainty (uncopyrightable without human authorship) creates a strategic risk for organisations that do not document human contributions. Organisations in regulated industries (financial services, healthcare) face additional scrutiny: audit trails for AI-generated decisions that affect customers or financial systems must meet existing regulatory standards regardless of how the code was produced. NZ's Privacy Act 2020 and the proposed AI-specific guidance from the Privacy Commissioner apply to AI systems that make or assist decisions about individuals, which includes AI-assisted code that implements algorithmic decision systems.

**Behavioural lens:** The 40% of developers who distrust AI-generated code (DORA 2024) represent a governance risk: developers who override AI suggestions without documenting why create inconsistent code quality outcomes. Organisations with strong engineering cultures (documented coding standards, mandatory peer review) are better positioned to absorb AI coding tools than organisations where code review is informal. [inference]

**Historical lens:** The trajectory from IDE autocomplete (1990s) to IntelliSense (2000s) to GitHub Copilot (2021) to autonomous coding agents (2024–2025) follows a consistent pattern: each increment automates more of the routine production work and shifts developer value-add toward design, architecture, and review. Type 2 (agentic builder) is not a final state; it is a transitional stage toward Type 3. The governance question is not whether Type 3 will happen but under what conditions human review gates will be relaxed.

---

### §6 Synthesis

**Core answer:** SWE AI strategies at leading organisations produce real, measurable individual-level productivity gains (40–55% faster on bounded tasks) but do not automatically translate to team-level delivery improvement without process redesign. The current frontier is Type 2 (agentic builder, human-gated deployment). Autonomous deployment (Type 3) is not in enterprise production at scale. Governance has converged on mandatory human review as the non-negotiable control.

**Key findings:**
1. The controlled evidence for individual task speed improvement is strong: 55.8% faster (RCT) and 40–55% faster (ANZ internal trial) for well-specified coding tasks. These numbers do not generalise to complex multi-file or architectural work.
2. Google (Sundar Pichai, 2024 earnings): >25% of new code is AI-generated, reviewed by engineers. This is the largest single documented deployment of AI code generation in production.
3. DORA 2024: higher AI adoption associates with worse delivery stability (–7.2%) and throughput (–1.5%) at the team level, not better. The individual-to-team translation requires workflow redesign.
4. The agentic frontier has advanced from 14% (Devin, SWE-bench, March 2024) to ~80% on curated tasks and ~46% on multi-file enterprise tasks by early 2026. Headline leaderboard scores overstate generalised capability.
5. All major enterprise deployments maintain mandatory human review before deployment. Type 3 (autonomous deployment) is not in production at scale.
6. IP: AI-generated code without meaningful human authorship is uncopyrightable. Code provenance tracking is an emerging governance practice.
7. No NZ technology companies have published SWE AI outcome data. ANZ's deployment (Australian parent) is the closest regional case.

**Risks/gaps:** No independent audits of the 25% Google AI code figure. NZ-specific case data absent. The SWE-bench discriminative subset finding means agent capability progress is less generalised than headline numbers suggest.

---

### §7 Recursive Review

All major claims are sourced or labelled. The individual-vs-team productivity distinction is maintained consistently. The agentic frontier section uses the SWE-bench caveat appropriately. NZ context acknowledges data absence rather than extrapolating from global evidence. IP governance section draws from legal sources, not AI vendor marketing. The Type 2/3 framework is applied consistently with the typology established in the prior AI strategy research item. No claim in §6 Synthesis appears in §2 without sourcing. Review complete.

---

## Findings

### Executive Summary

Organisations deploying AI coding assistants at scale achieve real but task-scoped individual productivity gains of 40–55% on well-specified coding tasks; however, these gains do not automatically translate to team-level delivery improvement without process redesign, and Google's DORA 2024 data shows higher AI adoption is associated with worse delivery stability. Google reports that over 25% of its new production code is now AI-generated, reviewed by engineers — the largest disclosed deployment. The current enterprise state is Type 2 (agentic builder, human-reviewed artefact before deployment), not Type 3 (autonomous deployment); all major financial services and technology firms maintain mandatory human review gates as a non-negotiable governance control. Autonomous coding agents have advanced rapidly on benchmarks (from 14% in March 2024 to ~80% on curated tasks by early 2026), but headline scores overstate generalised capability, and no enterprise is running Type 3 SWE autonomy at scale.

### Key Findings

1. **The Microsoft/GitHub/MIT RCT (2023) found that developers using GitHub Copilot completed a specified JavaScript task 55.8% faster** (1h11m vs 2h41m; 95% CI: 21–89%; P=0.0017), with the strongest benefit for less experienced and older developers — but the result applies to a single bounded task and does not generalize to complex multi-file enterprise work.

2. **Google's CEO disclosed in 2024 earnings calls that over 25% of Google's new code is AI-generated,** reviewed by human engineers before submission to production systems across Search, Cloud, and YouTube — the largest publicly disclosed AI code generation deployment.

3. **ANZ Bank deployed GitHub Copilot to 3,000 engineers following an internal controlled trial of 1,000 engineers** that showed 40–55% faster code development and improvements in code quality; ANZ is the most relevant documented case for the NZ financial services sector.

4. **Google's DORA 2024 report (tens of thousands of respondents) found that higher AI adoption associates with a 7.2% decline in delivery stability and a 1.5% decline in throughput** at the organisational level, even while individual developer productivity improves — confirming that individual speed gains require workflow redesign to convert into team-level delivery improvement.

5. **Autonomous coding agents went from 14% on SWE-bench (Devin, March 2024) to ~80% on a curated 500-issue subset and ~46% on harder multi-file enterprise tasks by early 2026,** representing roughly two years of rapid progress — but a discriminative subset analysis found performance drops from 73% headline to ~11% on problems that no agent had previously solved, indicating headline leaderboard scores significantly overstate generalised capability.

6. **GitHub Copilot Coding Agent (GA September 2025) and comparable agentic tools operate as Type 2 (agentic builder, human-gated):** the agent creates a draft pull request; mandatory human review and branch protection rules apply before any merge to production, and this model is consistent across all major enterprise deployments reviewed.

7. **No major enterprise is documented as running Type 3 (autonomous deployment with delegated authority) for production software at scale;** all financial services firms (JPMorgan, Goldman Sachs, Morgan Stanley, ANZ) and major platform providers (GitHub/Microsoft) maintain mandatory human review as the non-negotiable control point for AI-generated code before deployment.

8. **AI-generated code without meaningful human authorship is uncopyrightable in most jurisdictions,** including the US and UK, requiring organisations to document human contributions during AI-assisted development; code provenance tracking tools have emerged specifically to flag AI-generated outputs that match open-source code with restrictive licences.

9. **JPMorgan Chase (200,000+ employees, OmniAI and LLM Suite) reports 10–20% developer productivity gains from AI-assisted coding,** lower than the GitHub Copilot RCT figure, consistent with the DORA finding that broader enterprise deployment yields more modest aggregate gains than controlled task experiments.

10. **No NZ technology companies (Xero, Trade Me, Datacom) have published SWE AI outcome data;** the closest regional case is ANZ (Australian parent), whose deployment is directly relevant to ANZ NZ engineering teams and provides a useful benchmark for NZ financial services organisations considering similar programmes.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 55.8% faster task completion with GitHub Copilot | arXiv 2302.06590 / Microsoft Research | high | RCT, ~95 developers, single task; 95% CI 21-89% |
| >25% of Google's new code is AI-generated | Alphabet earnings call Q3 2024, Sundar Pichai | medium | CEO statement, not independently audited |
| ANZ Bank: 40-55% faster code with Copilot, 3,000 engineers | Finextra 43689, iTnews 601195, The Register 2024-02-10 | high | Internal controlled trial, multiple corroborating sources |
| Higher AI adoption: –7.2% delivery stability, –1.5% throughput | Google Cloud DORA 2024 report | high | 10+ years research, tens of thousands of respondents |
| Devin 13.86% on SWE-bench (March 2024) | Cognition AI SWE-bench technical report | high | Publicly released methodology and results |
| ~80% on SWE-bench Verified (early 2026) | live-swe-agent.github.io, llm-stats.com/benchmarks | high | Multiple leaderboards consistent |
| ~46% on SWE-bench Pro (multi-file, harder tasks) | scaleapi.github.io/SWE-bench_Pro-os | medium | Newer benchmark; fewer independent validations |
| 73% → 11% on discriminative subsets | jatinganhotra.dev/blog/swe-agents/2025/06/05 | medium | Single analysis; methodology described; important caveat |
| Copilot Coding Agent: 10,000+ orgs, mandatory human review gate | GitHub newsroom, Azure DevOps blog | high | Official product documentation |
| AI code without human authorship is uncopyrightable | MBHB law firm, Norton Rose Fulbright, US Copyright Office | high | Consistent across multiple legal jurisdictions |
| JPMorgan: 10–20% developer productivity gains | Harvard Business School case study, 5dvision.com | medium | Vendor-adjacent sourcing; plausible range |
| No NZ company SWE AI disclosures found | Search results: no matching results | medium | Absence of evidence; not evidence of absence of programmes |

### Assumptions

- **Assumption:** Sundar Pichai's >25% figure is directionally accurate for Google's production code. **Justification:** Statement made in an investor earnings call context, where material misstatement has legal consequences; independent audit not available.
- **Assumption:** Absence of NZ company SWE AI disclosures reflects NZ organisational culture around case study publication, not absence of AI coding programmes. **Justification:** AI Forum NZ survey data shows broad AI adoption in NZ; the gap is in public outcome disclosure, consistent with NZ organisations' typical preference for private implementation.
- **Assumption:** ANZ Australian engineering results are applicable to ANZ NZ teams. **Justification:** ANZ operates as a single trans-Tasman engineering organisation; the Copilot deployment was described as bank-wide.

### Analysis

Individual productivity gains from AI coding tools are real and consistent across the strongest evidence (RCT, ANZ internal trial). The consistency across diverse methods (controlled experiment, internal trial, self-reported survey) increases confidence. The DORA counterevidence (delivery stability decline) is critical: it confirms that the right question is not "does AI make developers faster?" (yes, on bounded tasks) but "does AI improve software delivery?" (not automatically, and possibly negatively without process redesign).

The Type 2 / Type 3 distinction is doing real analytical work here. All documented enterprises are operating Type 2. The agentic frontier (SWE-bench, Copilot Coding Agent) is clearly advancing toward Type 2 GA and probing Type 3 at the margins. The speed of benchmark improvement (14% → 80% in two years on curated tasks) is genuine but the discriminative subset finding is an important corrective: agents are getting better at problems that have been seen before, and the genuinely hard novel problems remain unsolved.

The IP governance finding is underweighted in most corporate AI strategy discussions. An organisation that cannot assert copyright over its AI-generated code has a weaker IP position than one that carefully documents human authorship contributions. This is a non-obvious strategic implication that deserves prominence in any NZ technology governance framework.

### Risks, Gaps, and Uncertainties

- The ANZ 40–55% figure is from a controlled internal trial on structured tasks; its applicability to complex enterprise software work (e.g., architectural changes, multi-system integration) is unverified.
- No independent audit of Google's >25% AI code claim. The figure may be subject to definitional variation (AI-suggested code that is accepted vs. AI-drafted code with minimal human modification).
- NZ-specific outcome data is entirely absent from the public record. Any NZ strategy built on global evidence is extrapolating from different scale, team composition, and codebase maturity contexts.
- The SWE-bench discriminative subset finding raises questions about whether benchmark improvement trajectories overstate progress on genuinely novel software engineering problems. If true, the path from Type 2 to Type 3 may be longer than headline numbers suggest.
- Governance frameworks for AI-generated code are evolving faster than case law. The IP positions documented here reflect current rulings and may change.

### Open Questions

- What is the actual productivity impact of AI coding tools on complex multi-system software work (architectural decisions, integration design) as opposed to task-completion speed on bounded coding exercises?
- At what agent capability threshold (SWE-bench score, real-world deployment rate) will enterprises begin relaxing human review gates for lower-risk production changes?
- How are NZ technology organisations (Xero, Trade Me, Datacom) actually deploying AI coding tools, and what governance frameworks are they using? A structured interview programme would be needed to answer this question.
- Does AI code review (not just code generation) address the DORA delivery stability problem — i.e., can AI-assisted review compensate for AI-accelerated code volume?

---

## Output

- Type: knowledge
- Description: Comparative analysis of SWE AI strategies and outcomes across 6+ organisations, with governance pattern analysis, agentic frontier assessment (SWE-bench trajectory), and NZ context.
- Links:
  - https://arxiv.org/abs/2302.06590 (GitHub Copilot productivity RCT)
  - https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report (DORA 2024)
  - https://www.swebench.com/ (SWE-bench leaderboard)