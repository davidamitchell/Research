---
review_count: 2
title: "Artificial Intelligence coding harness quality benchmarks: what measures are used to evaluate Artificial Intelligence coding tools and who scores highest?"
added: 2026-05-01T06:58:37+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
tags: [agentic-coding, evaluation, benchmarks, agentic-ai, llm, agent-tooling, developer-tooling]
started: 2026-05-01T08:22:25+00:00
completed: ~
output: []  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-08-ai-coding-harnesses-agent-philosophy, 2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-04-30-ai-code-entropy-quality-metrics]
related: [2026-03-08-ai-coding-harnesses-agent-philosophy, 2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-04-30-ai-code-entropy-quality-metrics, 2026-03-10-agent-evaluation-cross-repo-analysis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Artificial Intelligence coding harness quality benchmarks: what measures are used to evaluate Artificial Intelligence coding tools and who scores highest?

## Research Question

What benchmarks, metrics, and evaluation methodologies are used to measure the quality of Artificial Intelligence (AI) coding harnesses, including Integrated Development Environment (IDE) plugins, agentic coding assistants, and code completion tools, and which vendors and open-source projects score highest on those measures as of 2025-2026?

## Scope

**In scope:**
- Published benchmark suites and public leaderboards: Software Engineering Benchmark (SWE-bench), SWE-bench Verified, HumanEval, Mostly Basic Programming Problems (MBPP), LiveCodeBench, BigCodeBench, AgentEval, and any comparable coding-specific evaluation frameworks
- Evaluation metrics: pass@k (probability at least one of k generated samples passes all unit tests, as defined in [Chen et al. (2021)](https://arxiv.org/abs/2107.03374)), task completion rate, regression rate, cost-per-task, edit acceptance rate, hallucination rate on code, and any composite or vendor-defined quality scores
- Commercial AI coding tools: GitHub Copilot, Cursor, Devin (Cognition), Replit Agent, Amazon Q Developer, Google Gemini Code Assist, JetBrains AI, Microsoft Copilot (IDE)
- Open-source and community-maintained tools: Aider, Continue.dev, Cline, OpenHands (formerly OpenDevin), SWE-agent, and comparable projects
- Independent evaluations (academic papers, neutral third-party benchmarks, developer surveys such as Stack Overflow Developer Survey)
- Vendor-published benchmark results, with explicit credibility assessment (self-reported vs. independently reproduced)

**Out of scope:**
- Pure Large Language Model (LLM) benchmark evaluations not tied to coding tooling (e.g., MMLU, HellaSwag, general reasoning benchmarks)
- Infrastructure or deployment benchmarks (Application Programming Interface (API) latency, token cost) as primary quality measures, relevant only as secondary factors
- Security and vulnerability scanning tools as a distinct concern

**Constraints:**
- Prioritise published, reproducible benchmarks over anecdotal developer reviews or marketing claims
- Flag clearly where numbers are vendor self-reported versus independently verified
- Focus on the 2024-2026 window: this is a fast-moving field and older evaluations may not reflect current tool capabilities
- "Quality" is scoped to coding task effectiveness (correctness, completeness, regression safety), not to ergonomics or pricing alone

## Context

- [fact; source: https://www.swebench.com/; https://arxiv.org/abs/2403.07974; https://openreview.net/forum?id=YrycTjllL0] Public evaluation of AI coding systems is fragmented across at least three layers: function-level code generation benchmarks, broader contamination-resistant model benchmarks, and end-to-end software engineering agent benchmarks.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] Product teams also publish private or semi-private evidence such as randomized controlled trials, internal eval suites, and user survey results, which means tool comparison now depends as much on credibility and scope as on raw scores.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md] Prior completed work in this repository covers harness architecture, selection artifacts, and quality outcomes, but it does not map the benchmark layer itself or distinguish public harness scores from vendor-specific evidence.
- [inference; source: https://www.swebench.com/verified.html; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] A benchmark map is therefore a decision prerequisite for harness selection, because missing public scores, benchmark contamination concerns, and mixed practitioner trust all materially affect what a reported result is worth.

## Approach

1. **Map the benchmark landscape** - Identify the major published benchmark suites used to evaluate AI coding tools: SWE-bench family, HumanEval, MBPP, LiveCodeBench, BigCodeBench, and others. For each: what tasks are included, what does a passing grade mean, who created it, and how widely adopted is it as an evaluation standard?

2. **Catalogue evaluation metrics** - What does each benchmark measure (pass@k, task completion rate, regression rate, cost-per-task, etc.)? How do these metrics relate to real-world coding utility? Are there any composite scoring frameworks that integrate multiple dimensions?

3. **Assess evaluation credibility** - Which benchmarks are independently maintained and reproducible? Which scores are vendor self-reported versus externally verified? What are the known limitations, gaming risks, or blind spots of each benchmark?

4. **Score the major tools** - For the highest-profile commercial and open-source coding tools, locate their most recent published scores on the major benchmarks. Produce a structured comparison table. Flag where scores are missing, outdated, or methodologically suspect.

5. **Identify leaders and laggards** - Based on the evidence map, which tools consistently score highest across credible benchmarks? Are there tools that excel on one dimension but underperform on another? Are there emerging tools showing strong upward momentum?

6. **Surface gaps and open questions** - Where is the benchmark coverage weakest? What aspects of coding tool quality remain unmeasured by current frameworks? What do practitioners report that benchmarks miss?

## Sources

- [x] [Princeton Natural Language Processing Group SWE-bench](https://www.swebench.com/)
- [x] [Jimenez et al. (2024) SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)
- [x] [Princeton Natural Language Processing Group SWE-bench Verified](https://www.swebench.com/verified.html)
- [x] [Princeton Natural Language Processing Group SWE-bench Lite](https://www.swebench.com/lite.html)
- [x] [Chen et al. (2021) Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)
- [x] [OpenAI HumanEval repository](https://github.com/openai/human-eval)
- [x] [Google Research Mostly Basic Programming Problems dataset](https://github.com/google-research/google-research/tree/master/mbpp)
- [x] [Jain et al. (2024) LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://arxiv.org/abs/2403.07974)
- [x] [LiveCodeBench leaderboard](https://livecodebench.github.io/)
- [x] [BigCodeBench leaderboard](https://bigcode-bench.github.io/)
- [x] [BigCodeBench OpenReview submission](https://openreview.net/forum?id=YrycTjllL0)
- [x] [Aider leaderboards](https://aider.chat/docs/leaderboards/)
- [x] [Stack Overflow 2024 Developer Survey, AI](https://survey.stackoverflow.co/2024/ai)
- [x] [Cognition Labs technical report, SWE-bench results for Devin](https://www.cognition.ai/blog/swe-bench-technical-report)
- [x] [Cognition Labs introducing Devin](https://www.cognition.ai/blog/introducing-devin)
- [x] [GitHub Copilot productivity study](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [x] [GitHub Copilot code quality study](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [GitHub Copilot coding agent announcement](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/)
- [x] [Amazon Q Developer](https://aws.amazon.com/q/developer/)
- [x] [Google Developers Blog, The next chapter of the Gemini era for developers](https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)
- [x] [Cursor blog, CursorBench](https://cursor.com/blog/cursorbench)
- [x] [OpenHands](https://all-hands.dev/)

## Related

- [AI coding harnesses: agent execution model, memory, and context management across commercial and open-source software tools](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)
- [Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md)
- [Artificial Intelligence code entropy and complexity: does repeated AI code generation without architectural guardrails increase software entropy over time?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md)
- [Agent evaluation framework: cross-repo pattern analysis, commonality detection, and regression identification](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench] Research question restated: which public benchmarks, metrics, and evaluation methods are actually used to judge AI coding harness quality, and which named products or open-source projects currently lead those measures in a way that is decision-useful for 2025-2026 tool selection?
- [fact; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://arxiv.org/abs/2403.07974; https://openreview.net/forum?id=YrycTjllL0] Scope confirmed: the item covers end-to-end harness benchmarks, function-level code generation benchmarks, broader code benchmarks, vendor-published studies, and practitioner survey evidence, while excluding general non-coding model benchmarks and pure infrastructure metrics.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md] Prior repository work already establishes harness architecture, selection artifacts, and the importance of quality controls, so this item focuses on the missing empirical layer: benchmarks, metrics, score availability, and credibility differences across products.
- [fact; source: https://www.swebench.com/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] Constraints confirmed: prioritize public and reproducible sources, flag self-reported scores, treat leaderboard absence as missing public evidence rather than proof of private underperformance, and keep fast-moving 2025-2026 score claims tied to currently accessible public pages.
- [fact; source: https://www.swebench.com/verified.html; https://aider.chat/docs/leaderboards/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Output format confirmed: structured synthesis with benchmark map, metric map, credibility assessment, product comparison, evidence map, assumptions, analysis, risks, and open questions.

### §1 Question Decomposition

- **Root question:** Which measures are used to evaluate AI coding harnesses, and who leads those measures in public evidence?
- **A. Benchmark families**
  - A1. Which benchmarks directly test end-to-end software engineering work in repositories?
  - A2. Which benchmarks test standalone code generation or editing rather than full harness behavior?
  - A3. Which benchmarks were created to address contamination or benchmark saturation?
- **B. Metrics**
  - B1. What does pass@k measure, and where is it standard?
  - B2. What does percent resolved or task completion rate measure in software engineering agent benchmarks?
  - B3. Which secondary metrics appear in product studies or harness-specific leaderboards?
- **C. Credibility**
  - C1. Which measures are benchmark-maintained and reproducible?
  - C2. Which results are vendor self-reported or based on internal eval suites?
  - C3. What benchmark limitations or gaming risks are publicly acknowledged?
- **D. Product score coverage**
  - D1. Which named commercial tools have public, attributable benchmark entries?
  - D2. Which named open-source harnesses have public, attributable benchmark entries?
  - D3. Which popular products rely mainly on internal studies, internal evals, or model-level evidence instead of public comparable harness scores?
- **E. Decision relevance**
  - E1. Which benchmarks are strongest for selecting agentic coding harnesses?
  - E2. Which metrics matter for real-world harness quality but remain weakly measured?
  - E3. What should a reader treat as leader status versus missing-data status?

### §2 Investigation

- #### Benchmark families
- [fact; source: https://www.swebench.com/; https://arxiv.org/abs/2310.06770] SWE-bench is the most widely adopted public end-to-end software engineering benchmark in the retrieved sources: it contains 2,294 real GitHub issue and pull request pairs from 12 Python repositories and scores systems by the percentage of instances they resolve through code changes that satisfy the benchmark's test harness.
- [fact; source: https://www.swebench.com/verified.html] SWE-bench Verified is a 500-task human-filtered subset of SWE-bench designed to remove ambiguous, underspecified, or broken tasks so that public leaderboard results are more comparable and meaningful.
- [fact; source: https://www.swebench.com/lite.html] SWE-bench Lite is a 300-task cost-reduced subset that preserves distribution and difficulty while filtering for more self-contained bug fixes, which makes it a faster but narrower proxy for full SWE-bench style evaluation.
- [fact; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval] HumanEval is a hand-written evaluation set for code synthesis from docstrings that measures functional correctness with unit tests and reports pass@1, pass@10, and pass@100 rather than full repository issue resolution.
- [fact; source: https://github.com/google-research/google-research/tree/master/mbpp] Mostly Basic Programming Problems (MBPP) is an approximately 1,000-problem Python dataset aimed at entry-level programming competence, with task descriptions, reference solutions, and three automated test cases per problem.
- [fact; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/] LiveCodeBench was introduced because HumanEval and MBPP were no longer sufficient for modern code models; it continuously collects new contest problems and evaluates not only code generation but also self-repair, code execution, and test output prediction.
- [fact; source: https://openreview.net/forum?id=YrycTjllL0; https://bigcode-bench.github.io/] BigCodeBench evaluates practical programming tasks that require diverse tool or library use across 1,140 tasks, 139 libraries, and 7 domains, and ranks models primarily by calibrated pass@1 on both full and hard subsets.
- [fact; source: https://aider.chat/docs/leaderboards/] Aider's public leaderboard is a harness-specific code editing benchmark rather than a generic model benchmark: it tests 225 challenging Exercism exercises across C++, Go, Java, JavaScript, Python, and Rust, using Aider's editing loop to measure whether a model can follow instructions and successfully edit code without human intervention.
- [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp; https://aider.chat/docs/leaderboards/] The benchmark family most directly relevant to harness selection is the SWE-bench family, because it requires repository navigation, patch generation, and regression-safe task completion, while HumanEval and MBPP mostly measure model code synthesis and Aider mostly measures editing performance inside one specific harness.

- #### Metric landscape
- [fact; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval] pass@k measures the probability that at least one of k generated samples passes all unit tests for a problem, which makes it the dominant metric for stochastic code generation benchmarks such as HumanEval.
- [fact; source: https://www.swebench.com/; https://www.swebench.com/verified.html; https://www.swebench.com/lite.html] SWE-bench family leaderboards report percent resolved, which is the share of benchmark tasks a system fully solves under the benchmark's evaluation procedure.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's Copilot research adds a different metric family: time to completion, unit-test pass rate, readability, reliability, maintainability, conciseness, and approval likelihood in controlled developer studies.
- [fact; source: https://cursor.com/blog/cursorbench] CursorBench explicitly evaluates correctness, code quality, efficiency, and interaction behavior, and supplements offline results with controlled online experiments to detect regressions that offline grading misses.
- [fact; source: https://aider.chat/docs/leaderboards/] The Aider leaderboard exposes both percent correct and cost-per-run information, which makes it one of the few accessible public coding evals in the retrieved set that surfaces an explicit correctness-versus-cost trade-off.
- [inference; source: https://www.swebench.com/verified.html; https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Public measurement is strongest on correctness and weaker on regression rate, hallucination rate, collaboration quality, and long-horizon task robustness, so score leaders are only partially comparable on the dimensions practitioners care about most.

- #### Credibility, contamination, and benchmark fit
- [fact; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/] LiveCodeBench positions itself as contamination-free and explicitly argues that models can overfit HumanEval, which is why it tracks problems by release date and adds post-training tasks over time.
- [fact; source: https://cursor.com/blog/cursorbench] Cursor publicly argues that static public benchmarks are increasingly misaligned with real developer work, rely on narrow grading, and are vulnerable to contamination because tasks come from public repositories that can enter training data.
- [fact; source: https://survey.stackoverflow.co/2024/ai] Stack Overflow's 2024 survey shows the practitioner side of the credibility problem: 62% of respondents were already using AI tools, 43% felt good about output accuracy, and 45% of professional developers rated AI tools bad or very bad at handling complex tasks.
- [inference; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai; https://livecodebench.github.io/] Benchmark credibility is now a first-order evaluation dimension rather than a methodological footnote, because public leaderboard wins can coexist with mixed real-world trust, and vendors themselves are now disputing which public benchmarks remain decision-useful.

- #### Public score coverage for named tools and projects
- [fact; source: https://www.swebench.com/; https://www.swebench.com/verified.html] The strongest public 2025-2026 harness scores visible in the official SWE-bench Verified leaderboard are mostly attached to simple or open agent scaffolds paired with frontier models rather than to IDE brands; retrieved top entries include live-SWE-agent plus Claude 4.5 Opus medium at 79.2%, mini-SWE-agent plus Claude 4.5 Opus at 76.8%, and mini-SWE-agent plus GPT-5-2 Codex at 72.8%.
- [fact; source: https://www.swebench.com/; https://all-hands.dev/] Among branded open-source harnesses with directly attributable public Verified entries, OpenHands reaches 65.8% as a generic branded entry and 70.4% when paired with Claude 4 Sonnet, with higher model-paired variants also listed.
- [fact; source: https://www.swebench.com/; https://aws.amazon.com/q/developer/] Among named commercial products with directly attributable public Verified entries in retrieved official sources, Amazon Q Developer Agent reaches 65.4% on the official Verified leaderboard and Amazon's product page explicitly markets leadership on SWE-bench style leaderboards.
- [fact; source: https://www.swebench.com/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/] Google Jules appears as a public Verified entry at 52.2%, while Google's own launch post reports 51.8% on SWE-bench Verified for the Gemini 2.0 Flash research system that underpins Jules.
- [fact; source: https://www.swebench.com/; https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin] Devin's accessible official public score remains 13.86% on a random 25% subset of original SWE-bench from Cognition's 2024 report, which was historically important but is not a current public SWE-bench Verified leaderboard result.
- [fact; source: https://aider.chat/docs/leaderboards/] Aider's own benchmark paints a different picture because it measures editing inside the Aider harness rather than repository issue resolution: the retrieved current top rows are GPT-5 (high) at 88.0%, GPT-5 (medium) at 86.7%, and o3-pro (high) at 84.9%.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/] GitHub's public evidence for Copilot in the retrieved official sources centers on randomized studies and product documentation rather than on a first-party, Copilot-branded SWE-bench style leaderboard entry: GitHub reports 55% faster task completion in one controlled study and a 53.2% greater likelihood of passing all ten unit tests in a later code-quality study.
- [fact; source: https://cursor.com/blog/cursorbench] Cursor's public evidence in the retrieved official sources centers on CursorBench, an internal benchmark built from real Cursor sessions, and on an explicit critique of public benchmark fit rather than on a public Cursor-branded SWE-bench style score.
- [inference; source: https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench] The result is a public evidence asymmetry: open or benchmark-native harnesses are easier to compare on reproducible correctness leaderboards, while popular IDE assistants are easier to compare on productivity studies or internal eval narratives.

- #### Gaps that current benchmarks do not close
- [fact; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] Public benchmarks do not yet measure the full developer experience of long-running agents, ambiguous requests, and iterative collaboration very well, which is why Cursor moved toward online-offline eval loops and why professional developers still rate complex-task performance cautiously.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://aider.chat/docs/leaderboards/] The weakest measured surfaces are regression safety over long horizons, human-review burden after agent output, external-system integration quality, and whether an agent's work feels acceptable to developers before it is merely test-passing.

### §3 Reasoning

- [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp] The benchmark families form a hierarchy of decision relevance: standalone function synthesis benchmarks say most about base model coding ability, harness-specific editing benchmarks say more about one interaction loop, and repository issue-resolution benchmarks say most about end-to-end coding harness effectiveness.
- [inference; source: https://www.swebench.com/; https://all-hands.dev/; https://aws.amazon.com/q/developer/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/] Public leader status must therefore be interpreted by benchmark family rather than by a single global rank, because OpenHands, Amazon Q Developer Agent, Google Jules, mini-SWE-agent, and Aider are being measured on partially different tasks.
- [inference; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] The products most widely used in practice can have weaker public benchmark comparability than open benchmark-native harnesses, because the commercial incentive is often to optimize internal eval alignment rather than public reproducibility.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://aider.chat/docs/leaderboards/] Productivity studies and editing benchmarks are not invalid, but they should be treated as complementary evidence rather than substitutes for end-to-end issue-resolution benchmarks.

### §4 Consistency Check

- [fact; source: https://www.swebench.com/; https://www.swebench.com/verified.html] Score comparisons in this item are limited to benchmark-family-consistent claims wherever possible, and where family boundaries differ, the text explicitly states that the figures are not directly interchangeable.
- [fact; source: https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin] Devin is treated as an original SWE-bench result, not as a current Verified result, because that is what the accessible official Cognition sources support.
- [fact; source: https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] Cursor and GitHub Copilot are described as having public evidence, but that evidence is explicitly classified as internal benchmark methodology or controlled study evidence rather than public leaderboard parity.
- [inference; source: https://www.swebench.com/; https://aider.chat/docs/leaderboards; https://survey.stackoverflow.co/2024/ai] Confidence remains medium overall because benchmark definitions come from primary sources, but several high-interest product comparisons depend on heterogeneous evaluation types and on absence of public comparable scores rather than on a single uniform scoreboard.

### §5 Depth and Breadth Expansion

- [inference; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] **Behavioural lens:** benchmark wins do not settle adoption risk, because developer trust, perceived handling of complex tasks, and willingness to accept or merge generated code remain partially social and workflow-dependent.
- [inference; source: https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/; https://aws.amazon.com/q/developer/; https://all-hands.dev/] **Operating-model lens:** asynchronous cloud agents, secure sandboxes, and Git-based review workflows are now central product claims, which means future benchmark suites may need to measure reviewability, traceability, and environment safety in addition to raw correctness.
- [inference; source: https://arxiv.org/abs/2403.07974; https://openreview.net/forum?id=YrycTjllL0; https://cursor.com/blog/cursorbench] **Technical lens:** benchmark evolution is moving toward harder, fresher, and less overfit-prone tasks, but the field still lacks a universally accepted public benchmark for long-running, ambiguous, externally integrated engineering work.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md] **Repository cross-reference lens:** this benchmark item sharpens earlier repository findings by showing that evaluation quality is itself a control surface; a team can have strong architectural guidance yet still make poor harness choices if its evidence is benchmark-incoherent.

### §6 Synthesis

**Executive summary:**
- Public evidence for AI coding harness quality is strongest when it comes from end-to-end software engineering benchmarks such as SWE-bench Verified, while function-level benchmarks such as HumanEval and Mostly Basic Programming Problems (MBPP) are useful mainly as base-model screens rather than as direct harness rankings. [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp]
- The public leaders visible in current accessible benchmark data are mostly simple or open harnesses paired with high-performing current models, while several branded assistants in this item are represented instead by controlled studies or internal evals rather than directly comparable leaderboard entries. [inference; source: https://www.swebench.com/; https://all-hands.dev/; https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]
- GitHub Copilot and Cursor both publish public evidence, but that evidence is controlled-study or internal-eval evidence rather than first-party public leaderboard parity with benchmark-native harnesses such as mini-SWE-agent, OpenHands, or Amazon Q Developer Agent. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/]
- The right decision rule is therefore not "pick the tool with the biggest number," but "weight end-to-end public benchmark results highest, treat vendor studies as complementary, and discount comparisons where the benchmark family or scoring regime is not actually shared." [inference; source: https://www.swebench.com/verified.html; https://aider.chat/docs/leaderboards/; https://survey.stackoverflow.co/2024/ai]
**Key findings:**
- 1. [inference] **SWE-bench Verified is currently the most decision-useful public benchmark for comparing agentic coding harnesses, because it uses human-filtered real GitHub issue tasks and scores whether a system actually resolves repository problems rather than merely generating plausible standalone code.** (medium confidence; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2310.06770)
- 2. [inference] **HumanEval and Mostly Basic Programming Problems (MBPP) remain important coding benchmarks, but they are weak direct proxies for harness quality because they evaluate standalone Python problem solving and unit-test passing rather than repository navigation, multi-file editing, and regression-safe issue resolution.** (medium confidence; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://github.com/google-research/google-research/tree/master/mbpp; https://www.swebench.com/verified.html)
- 3. [fact] **LiveCodeBench and BigCodeBench extend benchmark coverage beyond older standalone-function tests by emphasizing contamination resistance, self-repair, code execution, tool or library use, and harder instructions, yet they still rank models more directly than branded coding products or end-to-end harnesses.** (high confidence; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://openreview.net/forum?id=YrycTjllL0; https://bigcode-bench.github.io/)
- 4. [fact] **The dominant public metrics are pass@k for sampled code generation and percent resolved for software engineering agents, while productivity studies add unit-test pass rates, approval rates, and readability or maintainability ratings that capture important but different aspects of coding-tool quality.** (high confidence; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- 5. [fact] **The highest public SWE-bench Verified scores visible in accessible official sources are attached primarily to simple or open harnesses such as live-SWE-agent and mini-SWE-agent paired with current top-scoring models, with retrieved top entries at 79.2% for live-SWE-agent plus Claude 4.5 Opus medium and 76.8% for mini-SWE-agent plus Claude 4.5 Opus.** (medium confidence; source: https://www.swebench.com/)
- 6. [fact] **Among named open-source platform entries with direct public attribution, OpenHands has become a serious top-tier benchmark participant, appearing at 65.8% as a branded entry and 70.4% when paired with Claude 4 Sonnet on the retrieved SWE-bench Verified leaderboard.** (medium confidence; source: https://www.swebench.com/; https://all-hands.dev/)
- 7. [inference] **Among named commercial products with directly attributable public Verified entries in retrieved official sources, Amazon Q Developer Agent presently has stronger public end-to-end benchmark evidence than Google Jules, at 65.4% versus 52.2% on SWE-bench Verified.** (medium confidence; source: https://www.swebench.com/; https://aws.amazon.com/q/developer/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)
- 8. [inference] **Devin's published 13.86% result on original SWE-bench was historically important because it normalized agent-style evaluation, but it should not be read as a current leaderboard position because it used a 25% subset of the older benchmark and not the current Verified leaderboard regime.** (medium confidence; source: https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin; https://www.swebench.com/verified.html)
- 9. [inference] **GitHub Copilot and Cursor both publish public evidence, but GitHub's evidence is primarily randomized controlled productivity and code-quality research while Cursor's evidence is primarily its internal CursorBench methodology, so neither currently offers first-party public leaderboard comparability with benchmark-native open harnesses.** (medium confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/)
- 10. [inference] **Benchmark credibility is now part of the quality question itself, because contamination risk, narrow grading, and benchmark-workflow mismatch are explicit public concerns in both LiveCodeBench and CursorBench, and practitioner trust in complex-task performance remains mixed even as usage grows.** (medium confidence; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai)
**Evidence map:**
| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] SWE-bench Verified is the strongest public benchmark for end-to-end harness comparison. | https://www.swebench.com/verified.html; https://arxiv.org/abs/2310.06770 | medium | Comparative judgment derived from the benchmark design and public coverage. |
| [inference] HumanEval and MBPP are weaker direct proxies for harness quality than SWE-bench family benchmarks. | https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://github.com/google-research/google-research/tree/master/mbpp; https://www.swebench.com/verified.html | medium | Comparative judgment based on benchmark task design differences. |
| [fact] LiveCodeBench and BigCodeBench broaden evaluation beyond older standalone-function tests. | https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://openreview.net/forum?id=YrycTjllL0; https://bigcode-bench.github.io/ | high | Freshness, contamination resistance, and tool or library use are central design goals. |
| [fact] pass@k and percent resolved are the dominant quantitative benchmark metrics, while product studies add approval, quality, and speed metrics. | https://arxiv.org/abs/2107.03374; https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ | high | Metric families should not be collapsed into one scalar. |
| [fact] The strongest current public Verified scores visible in accessible official sources belong mostly to live-SWE-agent and mini-SWE-agent variants. | https://www.swebench.com/ | medium | Retrieved top entries are 79.2% and 76.8%. |
| [fact] OpenHands is a leading open-source branded platform entry on the public Verified leaderboard. | https://www.swebench.com/; https://all-hands.dev/ | medium | Branded OpenHands entries appear from 65.8% to 70.4% in retrieved data. |
| [inference] Amazon Q Developer Agent currently has stronger directly attributable public Verified evidence than Google Jules. | https://www.swebench.com/; https://aws.amazon.com/q/developer/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/ | medium | Comparative synthesis based on the retrieved official public entries. |
| [inference] Devin's best accessible official public score is still its original 13.86% SWE-bench result, not a current Verified score. | https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin; https://www.swebench.com/verified.html | medium | Important historical result, weak for current direct ranking. |
| [inference] GitHub Copilot and Cursor publish public evidence that is not directly leaderboard-comparable with benchmark-native harnesses. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/ | medium | Public evidence exists, but it is not presented as a first-party shared benchmark score. |
| [inference] Benchmark credibility and benchmark-family fit now matter as much as raw score. | https://arxiv.org/abs/2403.07974; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai | medium | Public critiques and mixed practitioner trust justify the weighting rule. |
**Assumptions:**
- [assumption; source: https://www.swebench.com/; https://cursor.com/blog/cursorbench] If a popular branded tool did not appear in the retrieved official public leaderboard sources, this item treats that as missing public evidence, not as proof that the tool lacks any strong internal or private benchmark performance.
- [assumption; source: https://www.swebench.com/; https://all-hands.dev/; https://aider.chat/docs/leaderboards/] When a score is reported for a harness paired with a frontier model, the analysis attributes the result to the combined system rather than claiming the harness alone deserves the full score.
- [assumption; source: https://aider.chat/docs/leaderboards; https://www.swebench.com/verified.html] Aider benchmark results are used as evidence for harness-specific editing quality even though they are not directly comparable to SWE-bench Verified issue-resolution results.
**Analysis:**
- End-to-end harness selection should weight benchmark families by how much real software engineering behavior they contain, not by historical fame alone. [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp]
- That weighting puts SWE-bench Verified at the top for public harness comparison, followed by adjacent repository-scale proxies such as SWE-bench Lite and harness-specific editing suites such as Aider, while HumanEval and MBPP become supporting evidence about base-model coding ability. [inference; source: https://www.swebench.com/verified.html; https://www.swebench.com/lite.html; https://aider.chat/docs/leaderboards; https://arxiv.org/abs/2107.03374]
- The public leaderboard leaders now show that simple scaffolds plus strong models can outperform more elaborate branded products, which means a vendor's user interface or market visibility should not be mistaken for public benchmark leadership. [inference; source: https://www.swebench.com/; https://all-hands.dev/]
- At the same time, products such as GitHub Copilot and Cursor are not evidence-free; they simply publish different evidence types, namely controlled studies and internal eval loops, which are useful for workflow fit but weaker for external comparability. [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench]
- The resulting decision rule is to combine public benchmark strength, benchmark-family fit, and evidence credibility, and to treat any ranking that crosses those boundaries without adjustment as methodologically unsound. [inference; source: https://www.swebench.com/verified.html; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai]
**Risks, gaps, uncertainties:**
- Public benchmark scores move quickly, so any 2025-2026 leader table is time-sensitive. [fact; source: https://www.swebench.com/; https://aider.chat/docs/leaderboards]
- Several major products do not publish first-party public scores on shared harness benchmarks, which limits apples-to-apples comparison. [fact; source: https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.swebench.com/]
- Static public benchmarks may miss long-running, ambiguous, externally integrated, or highly collaborative engineering tasks. [fact; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai]
- Official OpenAI explanatory pages about SWE-bench Verified were linked from the SWE-bench site but not directly fetchable in this runtime, so Verified methodology claims here rely on the accessible SWE-bench Verified page itself rather than on the linked OpenAI copy. [fact; source: https://www.swebench.com/verified.html]
**Open questions:**
- What public benchmark can reliably measure multi-day or multi-session engineering work that crosses external services, review loops, and deployment boundaries?
- Which metric best captures post-generation review burden, not just whether tests eventually pass?
- Will major commercial IDE assistants converge on shared public harness benchmarks, or will internal evals such as CursorBench become the dominant decision surface?
### §7 Recursive Review

- [fact; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://arxiv.org/abs/2403.07974; https://openreview.net/forum?id=YrycTjllL0] All benchmark-definition claims in this item are bound to primary benchmark pages or primary benchmark papers.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] Non-leaderboard product claims are explicitly separated into controlled-study, internal-eval, or practitioner-survey evidence rather than being blended into the same score column as public benchmark results.
- [inference; source: https://www.swebench.com/; https://aider.chat/docs/leaderboards; https://survey.stackoverflow.co/2024/ai] Confidence remains medium overall because the benchmark map itself is well sourced, but several product comparisons are constrained by heterogeneous evaluation types and by missing public comparable scores.
- [fact; source: https://www.swebench.com/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai] Remaining uncertainties and benchmark-fit limitations are surfaced in Risks, Gaps, and Uncertainties rather than hidden inside the Key Findings.

---

## Findings

### Executive Summary
Public evidence for AI coding harness quality currently favors end-to-end software engineering benchmarks, with SWE-bench Verified carrying the most decision weight because it evaluates whether systems actually resolve real repository issues rather than merely emit plausible standalone code. [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2310.06770]

The strongest public leaderboard positions visible in accessible official sources are mostly held by simple or open harnesses paired with high-performing current models, while several branded assistants in this item are represented instead by controlled studies or internal evals rather than directly comparable leaderboard entries. [inference; source: https://www.swebench.com/; https://all-hands.dev/; https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]

That means tool selection in 2025-2026 should weight benchmark family and evidence credibility before raw score, because HumanEval, Mostly Basic Programming Problems (MBPP), Aider, GitHub Copilot studies, and CursorBench all measure different slices of quality. [inference; source: https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp; https://aider.chat/docs/leaderboards; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench]

GitHub Copilot and Cursor both publish public evidence, but their retrieved official evidence is controlled-study or internal-eval evidence rather than first-party public leaderboard parity with benchmark-native harnesses such as mini-SWE-agent, OpenHands, Amazon Q Developer Agent, or Google Jules. [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/]

The best-supported answer to the research question is therefore that no single benchmark is authoritative, but SWE-bench Verified is the strongest public anchor, and the current visible leaders in directly comparable public leaderboard evidence are open or benchmark-native agent systems. [inference; source: https://www.swebench.com/verified.html; https://www.swebench.com/]

### Key Findings

1. **SWE-bench Verified is currently the most decision-useful public benchmark for comparing agentic coding harnesses, because it uses human-filtered real GitHub issue tasks and scores whether a system actually resolves repository problems rather than merely generating plausible standalone code.** ([inference]; medium confidence; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2310.06770)
2. **HumanEval and Mostly Basic Programming Problems (MBPP) remain important coding benchmarks, but they are weak direct proxies for harness quality because they evaluate standalone Python problem solving and unit-test passing rather than repository navigation, multi-file editing, and regression-safe issue resolution.** ([inference]; medium confidence; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://github.com/google-research/google-research/tree/master/mbpp; https://www.swebench.com/verified.html)
3. **LiveCodeBench and BigCodeBench extend benchmark coverage beyond older standalone-function tests by emphasizing contamination resistance, self-repair, code execution, tool or library use, and harder instructions, yet they still rank models more directly than branded coding products or end-to-end harnesses.** ([fact]; high confidence; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://openreview.net/forum?id=YrycTjllL0; https://bigcode-bench.github.io/)
4. **The dominant public metrics are pass@k for sampled code generation and percent resolved for software engineering agents, while productivity studies add unit-test pass rates, approval rates, and readability or maintainability ratings that capture important but different aspects of coding-tool quality.** ([fact]; high confidence; source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
5. **The highest public SWE-bench Verified scores visible in accessible official sources are attached primarily to simple or open harnesses such as live-SWE-agent and mini-SWE-agent paired with current top-scoring models, with retrieved top entries at 79.2% for live-SWE-agent plus Claude 4.5 Opus medium and 76.8% for mini-SWE-agent plus Claude 4.5 Opus.** ([fact]; medium confidence; source: https://www.swebench.com/)
6. **Among named open-source platform entries with direct public attribution, OpenHands has become a serious top-tier benchmark participant, appearing at 65.8% as a branded entry and 70.4% when paired with Claude 4 Sonnet on the retrieved SWE-bench Verified leaderboard.** ([fact]; medium confidence; source: https://www.swebench.com/; https://all-hands.dev/)
7. **Among named commercial products with directly attributable public Verified entries in retrieved official sources, Amazon Q Developer Agent presently has stronger public end-to-end benchmark evidence than Google Jules, at 65.4% versus 52.2% on SWE-bench Verified.** ([inference]; medium confidence; source: https://www.swebench.com/; https://aws.amazon.com/q/developer/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/)
8. **Devin's published 13.86% result on original SWE-bench was historically important because it normalized agent-style evaluation, but it should not be read as a current leaderboard position because it used a 25% subset of the older benchmark and not the current Verified leaderboard regime.** ([inference]; medium confidence; source: https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin; https://www.swebench.com/verified.html)
9. **GitHub Copilot and Cursor both publish public evidence, but GitHub's evidence is primarily randomized controlled productivity and code-quality research while Cursor's evidence is primarily its internal CursorBench methodology, so neither currently offers first-party public leaderboard comparability with benchmark-native open harnesses.** ([inference]; medium confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/)
10. **Benchmark credibility is now part of the quality question itself, because contamination risk, narrow grading, and benchmark-workflow mismatch are explicit public concerns in both LiveCodeBench and CursorBench, and practitioner trust in complex-task performance remains mixed even as usage grows.** ([inference]; medium confidence; source: https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] SWE-bench Verified is the strongest public benchmark for end-to-end harness comparison. | https://www.swebench.com/verified.html; https://arxiv.org/abs/2310.06770 | medium | Comparative judgment derived from the benchmark design and public coverage. |
| [inference] HumanEval and MBPP are weaker direct proxies for harness quality than SWE-bench family benchmarks. | https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval; https://github.com/google-research/google-research/tree/master/mbpp; https://www.swebench.com/verified.html | medium | Comparative judgment based on benchmark task design differences. |
| [fact] LiveCodeBench and BigCodeBench broaden evaluation beyond older standalone-function tests. | https://arxiv.org/abs/2403.07974; https://livecodebench.github.io/; https://openreview.net/forum?id=YrycTjllL0; https://bigcode-bench.github.io/ | high | Freshness, contamination resistance, and tool or library use are central design goals. |
| [fact] pass@k and percent resolved are the dominant quantitative benchmark metrics, while product studies add approval, quality, and speed metrics. | https://arxiv.org/abs/2107.03374; https://www.swebench.com/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ | high | Metric families should not be collapsed into one scalar. |
| [fact] The strongest current public Verified scores visible in accessible official sources belong mostly to live-SWE-agent and mini-SWE-agent variants. | https://www.swebench.com/ | medium | Retrieved top entries are 79.2% and 76.8%. |
| [fact] OpenHands is a leading open-source branded platform entry on the public Verified leaderboard. | https://www.swebench.com/; https://all-hands.dev/ | medium | Branded OpenHands entries appear from 65.8% to 70.4% in retrieved data. |
| [inference] Amazon Q Developer Agent currently has stronger directly attributable public Verified evidence than Google Jules. | https://www.swebench.com/; https://aws.amazon.com/q/developer/; https://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/ | medium | Comparative synthesis based on the retrieved official public entries. |
| [inference] Devin's best accessible official public score is still its original 13.86% SWE-bench result, not a current Verified score. | https://www.cognition.ai/blog/swe-bench-technical-report; https://www.cognition.ai/blog/introducing-devin; https://www.swebench.com/verified.html | medium | Important historical result, weak for current direct ranking. |
| [inference] GitHub Copilot and Cursor publish public evidence that is not directly leaderboard-comparable with benchmark-native harnesses. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench; https://www.swebench.com/ | medium | Public evidence exists, but it is not presented as a first-party shared benchmark score. |
| [inference] Benchmark credibility and benchmark-family fit now matter as much as raw score. | https://arxiv.org/abs/2403.07974; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai | medium | Public critiques and mixed practitioner trust justify the weighting rule. |

### Assumptions

- [assumption; source: https://www.swebench.com/; https://cursor.com/blog/cursorbench] If a popular branded tool did not appear in the retrieved official public leaderboard sources, this item treats that as missing public evidence, not as proof that the tool lacks any strong internal or private benchmark performance.
- [assumption; source: https://www.swebench.com/; https://all-hands.dev/; https://aider.chat/docs/leaderboards/] When a score is reported for a harness paired with a frontier model, the analysis attributes the result to the combined system rather than claiming the harness alone deserves the full score.
- [assumption; source: https://aider.chat/docs/leaderboards; https://www.swebench.com/verified.html] Aider benchmark results are used as evidence for harness-specific editing quality even though they are not directly comparable to SWE-bench Verified issue-resolution results.

### Analysis

- End-to-end harness selection should weight benchmark families by how much real software engineering behavior they contain, not by historical fame alone. [inference; source: https://www.swebench.com/verified.html; https://arxiv.org/abs/2107.03374; https://github.com/google-research/google-research/tree/master/mbpp]
- That weighting puts SWE-bench Verified at the top for public harness comparison, followed by adjacent repository-scale proxies such as SWE-bench Lite and harness-specific editing suites such as Aider, while HumanEval and MBPP become supporting evidence about base-model coding ability. [inference; source: https://www.swebench.com/verified.html; https://www.swebench.com/lite.html; https://aider.chat/docs/leaderboards; https://arxiv.org/abs/2107.03374]
- The public leaderboard leaders now show that simple scaffolds plus strong models can outperform more elaborate branded products, which means a vendor's user interface or market visibility should not be mistaken for public benchmark leadership. [inference; source: https://www.swebench.com/; https://all-hands.dev/]
- At the same time, products such as GitHub Copilot and Cursor are not evidence-free; they simply publish different evidence types, namely controlled studies and internal eval loops, which are useful for workflow fit but weaker for external comparability. [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://cursor.com/blog/cursorbench]
- The resulting decision rule is to combine public benchmark strength, benchmark-family fit, and evidence credibility, and to treat any ranking that crosses those boundaries without adjustment as methodologically unsound. [inference; source: https://www.swebench.com/verified.html; https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai]

### Risks, Gaps, and Uncertainties

- Public benchmark scores move quickly, so any 2025-2026 leader table is time-sensitive. [fact; source: https://www.swebench.com/; https://aider.chat/docs/leaderboards]
- Several major products do not publish first-party public scores on shared harness benchmarks, which limits apples-to-apples comparison. [fact; source: https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.swebench.com/]
- Static public benchmarks may miss long-running, ambiguous, externally integrated, or highly collaborative engineering tasks. [fact; source: https://cursor.com/blog/cursorbench; https://survey.stackoverflow.co/2024/ai]
- Official OpenAI explanatory pages about SWE-bench Verified were linked from the SWE-bench site but not directly fetchable in this runtime, so Verified methodology claims here rely on the accessible SWE-bench Verified page itself rather than on the linked OpenAI copy. [fact; source: https://www.swebench.com/verified.html]

### Open Questions

- What public benchmark can reliably measure multi-day or multi-session engineering work that crosses external services, review loops, and deployment boundaries?
- Which metric best captures post-generation review burden, not just whether tests eventually pass?
- Will major commercial IDE assistants converge on shared public harness benchmarks, or will internal evals such as CursorBench become the dominant decision surface?

---

## Output

- Type: knowledge
- Description: Structured benchmark map and evidence-backed comparison of public coding-harness evaluation measures, with explicit separation between public leaderboard evidence, vendor studies, and internal evals. [fact; source: https://www.swebench.com/verified.html; https://cursor.com/blog/cursorbench; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]
- Links:
  - https://www.swebench.com/verified.html
  - https://cursor.com/blog/cursorbench
  - https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/
