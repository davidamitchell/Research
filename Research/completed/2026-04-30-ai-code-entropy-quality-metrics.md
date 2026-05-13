---
review_count: 2
title: "Artificial Intelligence code entropy and complexity: does repeated AI code generation without architectural guardrails increase software entropy over time?"
added: 2026-04-30T20:31:45+00:00
status: completed
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, technical-debt, evaluation, llm]
ai_themes: [agentic-ai, ai-architecture, tools-infrastructure, software-sustainability, code-quality-metrics]
started: 2026-04-30T20:52:07+00:00
completed: 2026-04-30T21:16:17+00:00
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-14-reliable-software-llm-era, 2026-04-26-llm-verifiability-asymmetry-code-world-action, 2026-04-26-software-engineering-investment-case-llm, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis]
related: [2026-03-22-code-architecture-inspection, 2026-04-26-llm-verifiability-asymmetry-code-world-action, 2026-04-28-llm-as-judge-pipeline-validation-checkpoints]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Artificial Intelligence code entropy and complexity: does repeated AI code generation without architectural guardrails increase software entropy over time?

## Research Question

Does repeated Artificial Intelligence (AI) code generation without strong architectural guardrails demonstrably increase software entropy and complexity over time, as predicted by the entropy model described in *The Pragmatic Programmer*, and if so, what objective metrics (cyclomatic complexity, coupling, cognitive load, time-to-change, defect rate) best capture the difference between minimally guardrailed AI-assisted codebases and those maintained with explicit investment in clean interfaces and deep module structures?

## Scope

**In scope:**
- Theoretical framing: software entropy as defined in *The Pragmatic Programmer* (Hunt & Thomas); entropy as a measure of disorder, unpredictability, and resistance to change in software systems
- Empirical evidence of accelerated complexity growth in AI-generated codebases: before-and-after studies, longitudinal comparisons, or practitioner case studies
- Objective complexity metrics applicable to AI-generated code: cyclomatic complexity (McCabe metric), coupling (afferent/efferent), cohesion, cognitive complexity (SonarQube definition), time-to-change (lead time for a small well-understood change), defect rates per unit of new code
- Comparison between minimally guardrailed, prompt-first projects and projects with active architectural investment: how quickly maintainability degrades in the absence of guardrails
- The "broken windows" analogy: whether AI coding accelerates the broken-windows effect by generating locally reasonable but globally incoherent code at high velocity
- Shallow versus deep module structures as a complexity control mechanism: reference to John Ousterhout's *A Philosophy of Software Design*

**Out of scope:**
- Detailed architectural patterns for deep modules, covered in `2026-04-30-deep-modules-ai-augmented-codebases`
- Test-Driven Development (TDD) as a complexity control mechanism, covered in `2026-04-30-tdd-feedback-loops-ai-augmented-dev`
- Strategic roles and design investment, covered in `2026-04-30-strategic-tactical-division-ai-teams`

**Constraints:**
- Empirical evidence preferred; theoretical frameworks accepted as context
- Sources from 2020 onwards preferred for AI-specific evidence; foundational Software Engineering (SE) texts accepted regardless of date

## Context

- [fact; source: https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Foundational software design literature frames the problem as cumulative disorder: Hunt and Thomas advise teams not to live with "broken windows," while John Ousterhout argues that deep modules reduce system complexity by keeping interfaces smaller than implementations.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Current evidence on Artificial Intelligence (AI) coding tools is mixed across timescales: controlled task studies report better local code quality under bounded conditions, but longitudinal repository analysis reports more cloning, more short-term churn, and less refactoring activity in the AI-assistance era.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md] The practical decision is therefore not whether Large Language Model (LLM) output is always worse than human output, but whether teams have enough architectural structure, review discipline, and measurement coverage to stop locally useful generations from compounding into system-level entropy.

## Approach

1. **Establish the theoretical baseline** - Summarise the entropy model from *The Pragmatic Programmer* and the broken-windows theory as applied to software. Locate Ousterhout's deep modules / shallow modules framework and its predicted impact on long-term maintainability. Define the metrics that would operationalise each theory.

2. **Survey empirical evidence of AI-generated code complexity** - Search for studies that measure complexity trends in codebases with high AI code contribution. Include research on Copilot-generated code quality (Microsoft Research), academic papers, and practitioner longitudinal reports.

3. **Analyse metric sensitivity** - Which metrics are most sensitive to the shallow-vs-deep module distinction? Review the literature on cyclomatic complexity, cognitive complexity, coupling, cohesion, and time-to-change. Identify which are tractable to measure automatically.

4. **Compare minimally guardrailed versus guardrailed projects** - Survey available case studies, open-source project analyses, and practitioner retrospectives comparing projects built with strict SE fundamentals versus those built with minimal architectural guidance. If controlled studies are unavailable, document inference chains and label accordingly.

5. **Assess the compounding rate** - Does the evidence suggest that entropy growth is linear or super-linear in AI-heavy workflows? Is there a threshold effect beyond which recovery becomes infeasible?

6. **Synthesise** - Produce a structured assessment: does the evidence support the entropy hypothesis? What are the key metrics for monitoring code health in AI-augmented teams? What early warning signs indicate a codebase is accumulating entropy faster than it can be repaid?

## Sources

- [x] [Hunt and Thomas (2019) The Pragmatic Programmer, 20th Anniversary Edition](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/)
- [x] [Pragmatic Bookshelf Tip 5: Don't Live with Broken Windows](https://pragprog.com/tips/)
- [x] [Ousterhout (2021) A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php)
- [x] [Ousterhout (2018) Modular Design lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
- [x] [McCabe (1976) A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837)
- [x] [SonarSource Cognitive Complexity because testability != understandability](https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/)
- [x] [Pearce et al. (2021) Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/abs/2108.09293)
- [x] [Dakhel et al. (2023) GitHub Copilot AI Pair Programmer: Asset or Liability?](https://arxiv.org/abs/2206.15331)
- [x] [Yetistiren et al. (2023) Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT](https://arxiv.org/abs/2304.10778)
- [x] [Liang et al. (2023) Practices and Challenges of Using GitHub Copilot: An Empirical Study](https://arxiv.org/abs/2303.08733)
- [x] [Welter et al. (2025) From Developer Pairs to AI Copilots: A Comparative Study on Knowledge Transfer](https://arxiv.org/abs/2506.04785)
- [x] [GitHub (2023) Research: Quantifying GitHub Copilot's impact on code quality](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/)
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [GitHub (2022) Research: Quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [x] [GitClear (2025) AI Copilot Code Quality: 2025 Look Back at 12 Months of Data](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
- [x] [CodeScene Change coupling: visualize the cost of change](https://codescene.com/blog/change-coupling-visualize-the-cost-of-change)
- [x] [CodeScene Improve code quality and ensure product stability](https://codescene.com/improve-code-quality-and-software-stability)
- [x] [CodeScene Measure code health of your codebase](https://codescene.com/blog/measure-code-health-of-your-codebase)
- [x] [Martinovic and Rozic (2025) Perceived Impact of AI-Based Tooling on Software Development Code Quality](https://link.springer.com/article/10.1007/s42979-024-03608-4)
- [x] [Mitchell (2026) Reliable Software in the LLM Era](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md)
- [x] [Mitchell (2026) LLM verifiability asymmetry between code and world action](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md)
- [x] [Mitchell (2026) Software engineering investment case for LLM value](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md)
- [x] [Mitchell (2026) Systems capability debt, citizen development, and agentic AI risk synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md)

## Related

- [Reliable Software in the LLM Era](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md)
- [LLM verifiability asymmetry: what exactly is the difference between domains like code, mathematics, and text, where LLMs can often be made useful, and domains that require writes to external systems or real-world action?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md)
- [What is the strongest evidence-based argument that investing in software engineering capability rather than citizen development tooling is simultaneously the correct response to systems capability debt and the correct way to capture genuine LLM value in a regulated financial institution?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md)
- [Systems capability debt, citizen development, and agentic AI risk: is the causal chain and sequencing imperative a novel contribution?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Research question restated: do repeated Artificial Intelligence (AI)-generated code changes, when produced without strong architectural guardrails, increase software entropy over time, and which objective metrics detect that drift earliest and most reliably?
- [fact; source: https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2304.10778; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Scope confirmed: the item covers both theory and evidence, distinguishes bounded task quality from longitudinal codebase health, and treats direct controlled comparisons between minimally guardrailed and architecturally guarded projects as sparse.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/] Output format confirmed: structured knowledge note with explicit confidence levels, evidence map, assumptions, analysis, early warning metrics, and open questions.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md] Prior completed repository work already supports four adjacent claims used here: deterministic verifiers matter more than raw generation speed, engineering investment is the main way to capture durable Large Language Model (LLM) value, verifier-gated software engineering is the highest-confidence common LLM domain, and compounding control failures make small local degradations strategically important at system scale.

### §1 Question Decomposition

- **Root question:** Does Artificial Intelligence (AI)-assisted coding increase software entropy over time without architectural guardrails, and how should teams measure that risk?
- **A. Theory**
  - A1. What do Hunt and Thomas mean by broken windows and software rot?
  - A2. How do deep modules and information hiding change the expected entropy trajectory?
  - A3. Which classic and modern complexity metrics map to these theories?
- **B. Task-level empirical evidence**
  - B1. Do controlled studies show better or worse local code quality with GitHub Copilot and related tools?
  - B2. What kinds of defects or weaknesses appear even when task-level quality improves?
- **C. Longitudinal empirical evidence**
  - C1. Do repository-scale studies show more duplication, churn, or refactoring decline in the AI era?
  - C2. What evidence exists for weaker human scrutiny or degraded feedback loops?
- **D. Metric sensitivity**
  - D1. Which metrics are most sensitive to local understandability problems?
  - D2. Which metrics are most sensitive to cross-module cost-of-change problems?
  - D3. Which metrics behave as early indicators versus lagging indicators?
- **E. Synthesis**
  - E1. Is the entropy hypothesis supported directly, indirectly, or not at all?
  - E2. Is growth best described as linear, super-linear, or thresholded?
  - E3. What warning signs should guarded teams watch before maintainability collapses?

### §2 Investigation

#### Source-access and search notes

- [fact; source: https://arxiv.org/abs/2208.04416; https://dl.acm.org/doi/10.1145/3544548.3581067] Access note: seeded arXiv URL `https://arxiv.org/abs/2208.04416` does not match the cited Copilot pair-programming paper and resolves to an unrelated route-planning paper; search for `"Is GitHub Copilot a Substitute for Human Pair-programming? An Empirical Study"` identified the Association for Computing Machinery (ACM) Digital Object Identifier (DOI) `https://dl.acm.org/doi/10.1145/3544548.3581067`, but the full text was blocked in this runtime, so no downstream factual claim depends on that paper.
- [fact; source: https://www.mdpi.com/1999-5903/16/6/188; https://link.springer.com/article/10.1007/s42979-024-03608-4] Access note: the Multidisciplinary Digital Publishing Institute (MDPI) page returned 403 in this runtime, so downstream claims about survey perceptions rely on the accessible Springer abstract rather than the blocked page.
- [fact; source: https://arxiv.org/abs/2208.04416; https://dl.acm.org/doi/10.1145/3544548.3581067] Failed primary-source search record: exact-title search for the mismatched seeded Copilot pair-programming paper succeeded only to the blocked Association for Computing Machinery (ACM) landing page after the incorrect arXiv identifier was ruled out; the blocked full text remains a gap.

#### A. Theoretical baseline

- [fact; source: https://pragprog.com/tips/] Hunt and Thomas state Tip 5 as "Don't Live with Broken Windows" and define the practice operationally as fixing bad designs, wrong decisions, and poor code when they are seen.
- [fact; source: https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/; https://pragprog.com/tips/] The Pragmatic Programmer's published materials frame maintainability as resisting software rot through ongoing repair rather than allowing visible disorder to accumulate.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout's modular design notes define deep classes as modules with small interfaces and lots of hidden functionality, and argue that the most important design goal is for the interface to be much simpler than the implementation.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout also states that information hiding reduces cross-module knowledge requirements because changes confined to implementation do not force other modules to change.
- [inference; source: https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Broken-windows theory and deep-module theory point in the same direction: entropy increases when small local accommodations leak design knowledge across interfaces, and it decreases when complexity is pulled downward into modules and repaired quickly.
- [fact; source: https://doi.org/10.1109/TSE.1976.233837; https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/] McCabe's cyclomatic complexity was introduced as a graph-theoretic complexity measure for managing program complexity, while SonarSource argues that it is better at approximating testability than maintainability.
- [fact; source: https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/] Cognitive Complexity measures understandability by incrementing for breaks in linear flow and for nesting, so it is explicitly aimed at the human mental effort required to understand and maintain a method.
- [fact; source: https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase] CodeScene's change coupling and hotspot analysis use version-control history to show which files co-evolve and where declining code health overlaps with active change, which makes them direct cost-of-change indicators rather than purely static structure indicators.

#### B. Task-level empirical evidence on AI-assisted code quality

- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized controlled trial reports that developers with GitHub Copilot access had a 53.2% greater likelihood of passing all ten unit tests in the study task, and their submissions were rated as more readable, reliable, maintainable, and concise by statistically significant margins.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/] GitHub's 2023 Copilot Chat study reports that reviews were completed 15% faster and were judged more actionable, while participants also reported greater confidence in code quality.
- [fact; source: https://arxiv.org/abs/2304.10778] Yetistiren et al. report HumanEval correctness rates of 46.3% for GitHub Copilot, 31.1% for Amazon CodeWhisperer, and 65.2% for ChatGPT, and estimate average technical debt from code smells at 9.1 minutes for Copilot outputs.
- [fact; source: https://arxiv.org/abs/2206.15331] Dakhel et al. report that human programmers produced a higher ratio of correct solutions than Copilot on their benchmark tasks, although buggy Copilot solutions often required less effort to repair.
- [fact; source: https://arxiv.org/abs/2108.09293] Pearce et al. generated 1,689 Copilot-completed programs across 89 security-relevant scenarios and found that approximately 40% contained vulnerabilities.
- [fact; source: https://link.springer.com/article/10.1007/s42979-024-03608-4] Martinovic and Rozic's survey-based study reports generally positive perceived effects of AI tooling on productivity and satisfaction, but only middling scores on readability, maintainability, efficiency, and precision.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2304.10778; https://arxiv.org/abs/2108.09293] The controlled evidence shows that AI assistance can improve bounded task outcomes, but it does not remove the need for review and verification because correctness remains below expert-human baselines in some studies and security failure rates remain material.

#### C. Longitudinal evidence on entropy pressure

- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear analyzes 211 million changed lines of code from 2020 to 2024 and reports that lines classified as moved or refactored fell from 25% of changed lines in 2021 to less than 10% in 2024.
- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] The same GitClear report finds that changed lines classified as copy-pasted or cloned rose from 8.3% in 2021 to 12.3% in 2024.
- [fact; source: https://arxiv.org/abs/2506.04785] Welter et al. find that developers accept GitHub Copilot suggestions with less scrutiny than suggestions from human pair-programming partners, even though knowledge-transfer episodes still occur.
- [fact; source: https://arxiv.org/abs/2303.08733] Liang et al. characterize Copilot as a "double-edged sword" in practitioner usage data, with useful generation benefits alongside integration difficulties and limitations that require careful use.
- [fact; source: https://codescene.com/blog/measure-code-health-of-your-codebase] CodeScene argues that once a development hotspot declines in code health it tends to stay that way unless teams intervene early, because restoration competes with feature pressure.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://codescene.com/blog/measure-code-health-of-your-codebase] The strongest available evidence for AI-driven entropy is therefore not an isolated spike in cyclomatic complexity but a pattern of more duplication, weaker scrutiny, and lower refactoring share across time, which is exactly the pattern broken-windows theory would predict.

#### D. Metric sensitivity and operationalization

- [fact; source: https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://doi.org/10.1109/TSE.1976.233837] Cyclomatic complexity and Cognitive Complexity are both automatable, but Cognitive Complexity is the more direct proxy for local understandability because it distinguishes between equally branchy code that is easier or harder to mentally follow.
- [fact; source: https://codescene.com/blog/change-coupling-visualize-the-cost-of-change] Change coupling captures hidden logical dependencies that static dependency graphs miss because it measures which files, functions, or modules repeatedly change together in commits.
- [fact; source: https://codescene.com/improve-code-quality-and-software-stability; https://codescene.com/blog/measure-code-health-of-your-codebase] CodeScene's hotspot framing treats overlap between high change frequency and low code health as the most actionable maintenance bottleneck, and reports unhealthy code as associated with 15x more defects, 2x slower development, and 10x higher delivery uncertainty.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase] For AI-heavy codebases, the most entropy-sensitive leading indicators are clone ratio, short-term churn, refactoring-share decline, hotspot code health decline, and unexpected change coupling, because they detect structural disorder before defect counts fully surface.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2108.09293] Defect rates and test-pass rates still matter, but they are better treated as lagging indicators of entropy because a codebase can be locally functional today while still accumulating duplicated or weakly structured code that raises tomorrow's change cost.

#### E. Guardrailed versus unguardrailed projects

- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] No accessible controlled study in this evidence set directly randomizes projects into minimally guardrailed and architecturally guardrailed conditions over a long period.
- [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md] The available evidence supports an inference chain instead: where interfaces are explicit and deterministic feedback loops exist, AI can improve bounded output quality, but where those guardrails are weak, higher throughput tends to amplify duplication and maintenance drag rather than architectural coherence.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md] This matches prior completed repository work arguing that LLMs are strongest when translation is constrained by external verifiers and weakest when teams rely on unconstrained text generation as a substitute for design discipline.

#### F. Compounding rate and threshold behavior

- [fact; source: https://codescene.com/blog/measure-code-health-of-your-codebase; https://codescene.com/improve-code-quality-and-software-stability] CodeScene's published guidance claims that unhealthy hotspots are costlier to change and that early detection matters because declining health tends to persist and later remediation competes with delivery pressure.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase] The evidence does not prove a precise super-linear mathematical law for AI-driven entropy growth, but it does support threshold behavior: once duplication rises, refactoring share falls, and hot modules accumulate hidden coupling, the cost of safe change appears to increase faster than linearly with additional code volume.
- [inference; source: https://pragprog.com/tips/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/measure-code-health-of-your-codebase] The best-supported operational interpretation of the entropy hypothesis is therefore compounding maintenance risk rather than simple "AI makes every file more complex."

### §3 Reasoning

- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The apparent contradiction between positive Copilot quality results and negative GitClear maintainability signals resolves once the unit of analysis changes from short tasks to evolving repositories.
- [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/] Ousterhout's deep-module theory predicts that entropy should surface first as interface leakage, cross-module coupling, and rising cognitive burden, so metrics tied to duplication, coupling, and hotspot decline should be more sensitive than defect counts alone.
- [inference; source: https://arxiv.org/abs/2506.04785; https://arxiv.org/abs/2303.08733; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Human acceptance of AI suggestions with less scrutiny provides a plausible mechanism for why repository-scale structural drift can worsen even when local developer experience improves.

### §4 Consistency Check

- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/] The GitHub studies report bounded improvements in task quality and review speed, not long-run architecture health, so they do not directly refute the entropy hypothesis.
- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear reports aggregate code-change patterns rather than controlled causal isolation, so its results support entropy pressure and maintenance-risk inference rather than a definitive "AI caused all observed decline" claim.
- [inference; source: https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2304.10778; https://arxiv.org/abs/2108.09293] Academic benchmark studies and security studies align with the mixed view: AI outputs can be useful and repairable, but they still carry correctness and safety deficits that become strategically relevant when generation volume rises.

### §5 Depth and Breadth Expansion

- [inference; source: https://arxiv.org/abs/2506.04785; https://arxiv.org/abs/2303.08733] Behavioural lens: entropy risk is partly sociotechnical, because weaker scrutiny and convenience biases reduce the human friction that normally catches shallow or duplicated contributions.
- [inference; source: https://codescene.com/improve-code-quality-and-software-stability; https://codescene.com/blog/measure-code-health-of-your-codebase] Economic lens: the operational pain of entropy appears not only as bugs but also as slower feature delivery, higher delivery uncertainty, and more expensive refactoring later.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md] Governance lens: teams that invest in interfaces, tests, static checks, and deterministic review loops are not merely being conservative; they are creating the only conditions under which higher AI coding throughput is likely to remain net-positive over time.
- [inference; source: https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Historical lens: AI-generated code does not invalidate classic software design advice; it makes the old anti-rot disciplines more economically important because the rate of code introduction is higher.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] The best-supported conclusion is that repeated AI code generation without architectural guardrails increases entropy pressure at the system level, even though it can improve bounded task-level code quality.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2304.10778; https://arxiv.org/abs/2206.15331] Controlled studies mainly show that AI can help developers produce locally functional, readable, and maintainable code for specific tasks.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://codescene.com/blog/measure-code-health-of-your-codebase] Longitudinal and behavioural evidence shows the opposite pressure at repository scale: more duplication, less refactoring, weaker scrutiny, and more persistent hotspot decline.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4] That repository-scale signal is observational rather than causally isolating, so broader tooling and process shifts remain a live competing explanation even though the AI-without-guardrails interpretation fits the available data best.
- [inference; source: https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase] The most useful monitoring stack is therefore a layered one: local understandability metrics, structural coupling metrics, and longitudinal change metrics together.

**Key findings:**

1. [inference] Repeated Artificial Intelligence (AI) code generation does not reliably degrade short, bounded programming tasks, because randomized and benchmark studies show that GitHub Copilot can improve unit-test success, readability, maintainability, and review throughput under controlled conditions. (medium confidence; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/; https://arxiv.org/abs/2304.10778)
2. [inference] The strongest current evidence for software entropy appears at repository timescale, where GitClear's multi-year dataset shows more cloned code and less moved or refactored code, although that observational pattern does not isolate Artificial Intelligence (AI) from broader tooling and process shifts. (low confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4)
3. [inference] Human review appears easier to overload than many teams assume in AI-assisted coding because security studies still find vulnerable suggestions at meaningful rates and human-AI collaboration studies show developers scrutinize Copilot suggestions less than human pair-programming input. (medium confidence; source: https://arxiv.org/abs/2108.09293; https://arxiv.org/abs/2506.04785)
4. [inference] Ousterhout's deep-module model explains why architectural guardrails matter: when interfaces stay small and implementation complexity stays hidden, locally generated code is less able to leak design knowledge across the system and create compounding change costs. (medium confidence; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md)
5. [inference] The most sensitive early-warning metrics for AI-driven entropy are clone ratio, short-term churn, refactoring-share decline, and hotspot code-health decline, because they capture structural drift before defect counts or incident reports fully catch up. (medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/measure-code-health-of-your-codebase; https://codescene.com/improve-code-quality-and-software-stability)
6. [inference] Cognitive Complexity and change coupling are more useful maintainability indicators than cyclomatic complexity alone in this problem setting, because one measures human understandability and the other measures hidden cost-of-change relationships across commits rather than just control-flow branches. (medium confidence; source: https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://doi.org/10.1109/TSE.1976.233837)
7. [inference] The evidence supports a threshold interpretation rather than a clean linear law, because hotspot decline, hidden coupling, and duplication reinforce each other until teams face markedly slower and less predictable change. (low confidence; source: https://codescene.com/blog/measure-code-health-of-your-codebase; https://codescene.com/improve-code-quality-and-software-stability; https://www.gitclear.com/ai_assistant_code_quality_2025_research)
8. [inference] The practical distinction between minimally guardrailed and guarded codebases is not that one uses AI and the other does not, but that guarded teams force generated code through interfaces, verifiers, and review loops that keep local gains from turning into system-level entropy. (low confidence; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Bounded task quality can improve with Copilot under controlled conditions. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/ ; https://arxiv.org/abs/2304.10778 | medium | short-horizon evidence |
| [inference] Repository-scale entropy pressure shows up as more clones and less refactoring, but the observational pattern does not isolate AI from broader tooling or process shifts. | https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://link.springer.com/article/10.1007/s42979-024-03608-4 | low | observational and confounded |
| [inference] Human review appears easier to overload when AI suggestions are accepted with reduced scrutiny and security defects persist. | https://arxiv.org/abs/2108.09293 ; https://arxiv.org/abs/2506.04785 | medium | review-control weakness |
| [inference] Deep modules reduce the chance that generated code leaks complexity across the system. | https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md | medium | theory plus repository companion |
| [inference] Clone ratio, churn, and hotspot decline are the best early-warning indicators. | https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://codescene.com/blog/measure-code-health-of-your-codebase ; https://codescene.com/improve-code-quality-and-software-stability | medium | leading indicators |
| [inference] Cognitive Complexity and change coupling are more useful maintainability indicators than branch counting alone in this problem setting. | https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/ ; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change ; https://doi.org/10.1109/TSE.1976.233837 | medium | local plus cross-commit metrics |
| [inference] Entropy growth behaves more like a thresholded compounding process than a clean linear trend. | https://codescene.com/blog/measure-code-health-of-your-codebase ; https://codescene.com/improve-code-quality-and-software-stability ; https://www.gitclear.com/ai_assistant_code_quality_2025_research | low | nonlinear cost signal |
| [inference] Guardrails convert AI coding from entropy amplifier to constrained productivity aid. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md | low | governance interpretation |

**Assumptions:**

- [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear's repository-scale trends are treated as partly AI-associated rather than fully AI-isolated, because the report is observational and cannot eliminate every confounder across 2020 to 2024.

**Analysis:**

- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The main analytical move is to separate local code quality from system entropy, because the evidence is genuinely positive on the first and cautionary on the second.
- [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change] Deep interfaces, local understandability, and historical coupling should be treated as different control surfaces, since a codebase can score well on one while degrading on another.
- [inference; source: https://arxiv.org/abs/2506.04785; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2108.09293] Human behavior is part of the mechanism: if AI output is accepted quickly and at scale, review quality becomes the scarce resource and structural debt can accumulate faster than teams notice.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4] The competing explanation, that some repository-scale deterioration reflects broader tooling or process changes rather than AI specifically, is credible, but it does not explain away the specific AI-era combination of rising clone share, declining moved-code share, and reduced scrutiny documented in the cited evidence.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md] This is why prior repository work on verifier pipelines and engineering investment sharpens the conclusion here: entropy control is less about banning AI generation than about raising the strength of the architecture and verification envelope around it.

**Risks, gaps, uncertainties:**

- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The evidence base does not yet include a strong independent longitudinal experiment that directly randomizes entire codebases into guardrailed and unguardrailed AI workflows.
- [fact; source: https://dl.acm.org/doi/10.1145/3544548.3581067; https://arxiv.org/abs/2208.04416] The originally seeded Copilot pair-programming source had an incorrect arXiv identifier and the corrected ACM paper was blocked, which limits direct use of that specific comparison.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4] Repository-wide trend data and survey data are directionally useful but cannot fully isolate which observed maintainability changes come from AI, broader tooling changes, or shifting development practices.

**Open questions:**

- Which metric bundle best predicts future remediation cost in AI-heavy repositories: clone ratio plus hotspot decline, or change coupling plus Cognitive Complexity?
- Can a controlled longitudinal study instrument two otherwise similar teams, one with enforced architectural review and one with prompt-first generation, to estimate entropy-growth differentials directly?
- What review-process changes most effectively restore scrutiny when developers grow accustomed to accepting AI suggestions?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-30-ai-code-entropy-quality-metrics.md] Coverage, prior-work cross-reference, claim-label, findings-parity, and evidence-map audits were completed for this draft.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-30-ai-code-entropy-quality-metrics.md] Acronym audit completed: Artificial Intelligence (AI), Software Engineering (SE), Test-Driven Development (TDD), Large Language Model (LLM).
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-30-ai-code-entropy-quality-metrics.md] Domain-term clarity audit completed with informal shorthand removed in favor of plain-language phrasing, and the confidence outcome remains medium for the item as a whole.

---

## Findings

### Executive Summary

Repeated Artificial Intelligence (AI) code generation without architectural guardrails is more likely than not to increase software entropy at the system level, even though it can improve bounded task-level code quality. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]

The evidence is mixed only if task-level and repository-level outcomes are treated as the same thing: randomized studies show better local correctness and review outcomes, while longitudinal repository data shows more duplication and less refactoring over time. [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Architectural guardrails matter because deep modules, explicit interfaces, and deterministic verification loops limit how much locally generated code can leak hidden design decisions across the rest of the system. [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md]

The repository-scale signal is observational rather than causally isolating, so broader tooling and process shifts remain a live competing explanation even though the AI-without-guardrails interpretation fits the available evidence best. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4]

The best early warning signs are not defect counts alone, but rising clone ratio, short-term churn, refactoring-share decline, hotspot code-health decline, and unexpected change coupling. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase]

### Key Findings

1. **Repeated Artificial Intelligence (AI) code generation does not reliably degrade short, bounded programming tasks, because randomized and benchmark studies show that GitHub Copilot can improve unit-test success, readability, maintainability, and review throughput under controlled conditions.** ([inference]; medium confidence; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/; https://arxiv.org/abs/2304.10778)
2. **The strongest current evidence for software entropy appears at repository timescale, where GitClear's multi-year dataset shows more cloned code and less moved or refactored code, although that observational pattern does not isolate Artificial Intelligence (AI) from broader tooling and process shifts.** ([inference]; low confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4)
3. **Human review appears easier to overload than many teams assume in AI-assisted coding because security studies still find vulnerable suggestions at meaningful rates and human-AI collaboration studies show developers scrutinize Copilot suggestions less than human pair-programming input.** ([inference]; medium confidence; source: https://arxiv.org/abs/2108.09293; https://arxiv.org/abs/2506.04785)
4. **John Ousterhout's deep-module model explains why architectural guardrails matter: when interfaces stay small and implementation complexity stays hidden, locally generated code is less able to leak design knowledge across the system and create compounding change costs.** ([inference]; medium confidence; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md)
5. **The most sensitive early-warning metrics for AI-driven entropy are clone ratio, short-term churn, refactoring-share decline, and hotspot code-health decline, because they capture structural drift before defect counts or incident reports fully catch up.** ([inference]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://codescene.com/blog/measure-code-health-of-your-codebase; https://codescene.com/improve-code-quality-and-software-stability)
6. **Cognitive Complexity and change coupling are more useful maintainability indicators than cyclomatic complexity alone in this problem setting, because one measures human understandability and the other measures hidden cost-of-change relationships across commits rather than just control-flow branches.** ([inference]; medium confidence; source: https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://doi.org/10.1109/TSE.1976.233837)
7. **The evidence supports a threshold interpretation rather than a clean linear law, because hotspot decline, hidden coupling, and duplication reinforce each other until teams face markedly slower and less predictable change.** ([inference]; low confidence; source: https://codescene.com/blog/measure-code-health-of-your-codebase; https://codescene.com/improve-code-quality-and-software-stability; https://www.gitclear.com/ai_assistant_code_quality_2025_research)
8. **The practical distinction between minimally guardrailed and guarded codebases is not that one uses AI and the other does not, but that guarded teams force generated code through interfaces, verifiers, and review loops that keep local gains from turning into system-level entropy.** ([inference]; low confidence; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Bounded task quality can improve with Copilot under controlled conditions. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/ ; https://arxiv.org/abs/2304.10778 | medium | short-horizon evidence |
| [inference] Repository-scale entropy pressure shows up as more clones and less refactoring, but the observational pattern does not isolate AI from broader tooling or process shifts. | https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://link.springer.com/article/10.1007/s42979-024-03608-4 | low | observational and confounded |
| [inference] Human review appears easier to overload when AI suggestions are accepted with reduced scrutiny and security defects persist. | https://arxiv.org/abs/2108.09293 ; https://arxiv.org/abs/2506.04785 | medium | review-control weakness |
| [inference] Deep modules reduce the chance that generated code leaks complexity across the system. | https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md | medium | theory plus repository companion |
| [inference] Clone ratio, churn, and hotspot decline are the best early-warning indicators. | https://www.gitclear.com/ai_assistant_code_quality_2025_research ; https://codescene.com/blog/measure-code-health-of-your-codebase ; https://codescene.com/improve-code-quality-and-software-stability | medium | leading indicators |
| [inference] Cognitive Complexity and change coupling are more useful maintainability indicators than branch counting alone in this problem setting. | https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/ ; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change ; https://doi.org/10.1109/TSE.1976.233837 | medium | local plus cross-commit metrics |
| [inference] Entropy growth behaves more like a thresholded compounding process than a clean linear trend. | https://codescene.com/blog/measure-code-health-of-your-codebase ; https://codescene.com/improve-code-quality-and-software-stability ; https://www.gitclear.com/ai_assistant_code_quality_2025_research | low | nonlinear cost signal |
| [inference] Guardrails convert AI coding from entropy amplifier to constrained productivity aid. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis.md | low | governance interpretation |

### Assumptions

- "Vibe-coded" is treated here as AI-heavy coding with weak architectural and review guardrails, because the literature does not offer a standardized formal term for that working style. [assumption; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- GitClear's repository-scale trends are treated as partly AI-associated rather than fully AI-isolated, because the report is observational and cannot eliminate every confounder across 2020 to 2024. [assumption; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research]

### Analysis

The main analytical move is to separate local code quality from system entropy, because the evidence is genuinely positive on the first and cautionary on the second. [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]

Deep interfaces, local understandability, and historical coupling should be treated as different control surfaces, since a codebase can score well on one while degrading on another. [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.sonarsource.com/blog/cognitive-complexity-because-testability-understandability/; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change]

Human behavior is part of the mechanism: if Artificial Intelligence (AI) output is accepted quickly and at scale, review quality becomes the scarce resource and structural debt can accumulate faster than teams notice. [inference; source: https://arxiv.org/abs/2506.04785; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2108.09293]

The competing explanation, that some repository-scale deterioration reflects broader tooling or process changes rather than AI specifically, is credible, but it does not explain away the specific AI-era combination of rising clone share, declining moved-code share, and reduced scrutiny documented in the cited evidence. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4]

This is why prior repository work on verifier pipelines and engineering investment sharpens the conclusion here: entropy control is less about banning AI generation than about raising the strength of the architecture and verification envelope around it. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-14-reliable-software-llm-era.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-software-engineering-investment-case-llm.md]

### Risks, Gaps, and Uncertainties

- The evidence base does not yet include a strong independent longitudinal experiment that directly randomizes entire codebases into guardrailed and unguardrailed Artificial Intelligence (AI) workflows. [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research]
- The originally seeded Copilot pair-programming source had an incorrect arXiv identifier and the corrected Association for Computing Machinery (ACM) paper was blocked, which limits direct use of that specific comparison. [fact; source: https://dl.acm.org/doi/10.1145/3544548.3581067; https://arxiv.org/abs/2208.04416]
- Repository-wide trend data and survey data are directionally useful but cannot fully isolate which observed maintainability changes come from AI, broader tooling changes, or shifting development practices. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://link.springer.com/article/10.1007/s42979-024-03608-4]

### Open Questions

- Which metric bundle best predicts future remediation cost in AI-heavy repositories: clone ratio plus hotspot decline, or change coupling plus Cognitive Complexity?
- Can a controlled longitudinal study instrument two otherwise similar teams, one with enforced architectural review and one with prompt-first generation, to estimate entropy-growth differentials directly?
- What review-process changes most effectively restore scrutiny when developers grow accustomed to accepting AI suggestions?

---

## Output

- Type: knowledge
- Description: Evidence-based assessment of when AI-assisted coding improves local task quality versus when it increases system-level entropy, including a recommended monitoring stack for early detection.
- Links:
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research
  - https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/
  - https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign
