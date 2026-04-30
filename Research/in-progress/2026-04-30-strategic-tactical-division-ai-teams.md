---
review_count: 1
title: "Strategic versus tactical roles in Artificial Intelligence (AI)-augmented software teams: division of labour, daily design investment, and the cost of bad code at scale"
added: 2026-04-30T20:31:45+00:00
status: reviewing
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, agentic-ai, llm, organisational-design]
started: 2026-04-30T22:28:28+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-30-grill-me-ai-alignment-shared-design, 2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-02-org-shape-software-cost-zero]
related: [2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis, 2026-03-14-reliable-software-llm-era]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Strategic versus tactical roles in Artificial Intelligence (AI)-augmented software teams: division of labour, daily design investment, and the cost of bad code at scale

## Research Question

In an Artificial Intelligence (AI)-augmented software team, what is the optimal division of labour between the human developer, who owns strategic design, interface definition, and architectural oversight, and the AI assistant, which handles tactical implementation, and does Kent Beck's advice to invest daily in system design provide compounding returns in AI-heavy workflows, particularly if AI's ability to generate large volumes of code rapidly is making bad code more expensive, not cheaper, in 2026 and beyond?

## Scope

**In scope:**
- Human strategic roles in AI-augmented teams: system design, architectural decision-making, interface definition, test specification, review, and validation
- AI tactical roles: implementing within well-defined interfaces, filling in bodies of specified functions, generating boilerplate, and refactoring within a defined scope
- Kent Beck's design-investment argument: the claim that repeated small investments in naming, reducing coupling, where changing one element forces changes in another, and improving test safety create cumulative returns over time
- The "code is cheap" assumption: whether low marginal cost of AI-generated code changes the economics of technical debt, review, and maintenance
- Opportunity cost of human attention: where human time has the highest leverage in an AI-augmented workflow
- Evidence from practitioner accounts, workflow guidance, and academic studies on human-AI collaboration patterns in software development
- Kent Beck's published views on AI-augmented development from 2024 to 2025

**Out of scope:**
- Multi-agent orchestration beyond what is directly relevant to single-team software delivery
- Non-software industry parallels unless they directly clarify software-team design
- Direct empirical measurement of complexity metrics, which is covered in `2026-04-30-ai-code-entropy-quality-metrics`

**Constraints:**
- Sources from 2022 onward preferred, while foundational software-design sources and Kent Beck's own publications are accepted regardless of date
- Practitioner evidence is acceptable, but confidence must be lowered when controlled empirical support is missing

## Context

- [fact; source: https://kentbeck.com/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Current GitHub Copilot evidence shows bounded implementation throughput gains, while Kent Beck's current framing of "augmented coding" says the skills that grow in value are vision, strategy, task breakdown, and feedback loops rather than raw code typing.
- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2506.04785; https://www.gitclear.com/ai_assistant_code_quality_2025_research] The unresolved problem is whether teams can review, understand, and integrate AI-generated code with enough discipline to avoid higher downstream maintenance cost.
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] External workflow guidance increasingly treats architecture, context control, investigation, and verification as first-order controls, which implies that the human's highest-value work is strategic and supervisory rather than purely implementational.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html] Adjacent completed repository items already show that clarification-first workflows, stronger architectural boundaries, and fundamentals-first delivery reduce ambiguity and entropy in AI-heavy development.

## Approach

1. **Define the strategic and tactical division**: survey workflow guidance, clarification studies, and collaboration research to separate human-owned decisions from AI-suitable execution work.
2. **Review Kent Beck's design-investment argument**: locate Beck's current public views on tidying, coupling, where changing one element forces changes in another, cohesion, where related change pressure stays concentrated inside one element, and AI-augmented development, then assess whether the compounding-return claim is directly measured or mainly inferential.
3. **Examine the "code is cheap" assumption**: review evidence on review burden, duplicate code, maintenance cost, and human scrutiny in AI-assisted development.
4. **Survey human-AI collaboration models**: gather empirical studies and structured practitioner accounts on clarification, debugging, code review, and context management.
5. **Assess the opportunity cost of human attention**: identify where human time is most leverageable, using evidence rather than assertion.
6. **Synthesise**: produce a structured assessment of the best-supported operating model, the strength of the design-investment case, and whether AI-era economics make bad code more expensive.

## Sources

- [x] [Beck (2023) Tidy First? A Personal Exercise in Empirical Software Design](https://www.oreilly.com/library/view/tidy-first/9781098151232/)
- [x] [Beck (2024) SE Radio 615: Kent Beck on Tidy First?](https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/)
- [x] [Beck (2025) Kent Beck: Software Design Pioneer](https://kentbeck.com/)
- [x] [Ousterhout (2018) Modular Design lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
- [x] [Hunt and Thomas (2019) Tip 5: Don't Live with Broken Windows](https://pragprog.com/tips/)
- [x] [Anthropic (2025) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [GitHub (2025) How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
- [x] [Ziegler et al. (2022) Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537)
- [x] [Peng et al. (2023) The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590)
- [x] [Vaithilingam et al. (2022) Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models](https://ml4code.github.io/publications/vaithilingam2022expectation/)
- [x] [Liang et al. (2023) Practices and Challenges of Using GitHub Copilot: An Empirical Study](https://arxiv.org/abs/2303.08733)
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [GitHub (2023) Research: Quantifying GitHub Copilot's impact on code quality](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/)
- [x] [GitHub (2022) Research: Quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [x] [Wang et al. (2023) ClarifyGPT](https://arxiv.org/abs/2310.10996)
- [x] [Miao et al. (2025) ClariGen](https://openreview.net/forum?id=s566pj5E5M)
- [x] [Addlesee et al. (2024) Clarifying Completions: Evaluating How LLMs Respond to Incomplete Questions](https://aclanthology.org/2024.lrec-main.288/)
- [x] [Microsoft Research (2024) Let's Fix this Together: Conversational Debugging with GitHub Copilot](https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/)
- [x] [Welter et al. (2025) From Developer Pairs to AI Copilots: A Comparative Study on Knowledge Transfer](https://arxiv.org/abs/2506.04785)
- [x] [GitClear (2025) AI Copilot Code Quality: 2025 Look Back at 12 Months of Data](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
- [x] [Barcia (2025) I still care about the code](https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html)
- [x] [Thoughtworks (2024) Legacy Modernization meets GenAI](https://martinfowler.com/articles/legacy-modernization-gen-ai.html)
- [x] [Mitchell (2026) Grill-Me technique: iterative structured interviewing for human and Artificial Intelligence (AI) alignment in code generation](https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html)
- [x] [Mitchell (2026) Artificial Intelligence code entropy and complexity](https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html)
- [x] [Mitchell (2026) Deep modules in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [x] [Mitchell (2026) Fundamentals-first versus specs-to-code](https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
- [x] [Mitchell (2026) The shape of organisations when software is no longer the constraint](https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html)

## Related

- [Grill-Me technique: iterative structured interviewing for human and Artificial Intelligence (AI) alignment in code generation](https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html)
- [Deep modules in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [Artificial Intelligence code entropy and complexity](https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Research question restated: in Artificial Intelligence (AI)-augmented software delivery, which work should remain human-owned at the strategic layer, which work can be safely delegated to AI at the tactical layer, and does repeated investment in design quality improve outcomes enough to justify its daily cost?
- [fact; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/] Scope confirmed: the item covers Beck's design-investment claims, bounded empirical evidence on AI coding, clarification and debugging studies, and maintenance-cost signals, while treating precise return multipliers for daily design work as unproven unless directly measured.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Output format confirmed: structured knowledge note with explicit claims on role division, design investment, human-attention leverage, maintenance economics, and uncertainty.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html] Prior completed repository work already provides adjacent evidence that clarification reduces alignment failures, architecture reduces reasoning surface, repository entropy worsens under weak guardrails, fundamentals-first workflows outperform prompt-only approaches, and cheaper software production shifts organisational value toward judgment and prioritisation.

### §1 Question Decomposition

- **Root question:** what human-AI operating model is best supported for software teams once AI can generate large volumes of code quickly?
- **A. Strategic versus tactical work**
  - A1. Which tasks do current workflow guides and practitioner sources assign to humans rather than to AI?
  - A2. Which tasks do current studies show AI can accelerate safely when the task boundary is clear?
- **B. Design investment**
  - B1. What exactly does Kent Beck claim about tidying, coupling, cohesion, and compounding design effects?
  - B2. Is the compounding-return claim directly measured in AI workflows or mainly inferred from software-change theory?
- **C. Clarification and review**
  - C1. Do clarification-first workflows improve code correctness on ambiguous tasks?
  - C2. Do debugging and review workflows improve when the system investigates before responding?
- **D. Cost of bad code**
  - D1. What evidence shows that AI increases code volume faster than review and maintenance scale?
  - D2. What evidence shows reduced scrutiny or higher downstream understanding cost?
- **E. Human attention leverage**
  - E1. Where is human time most valuable, design, specification, testing, review, or manual code typing?
  - E2. Which claims here are direct facts and which remain synthesis-level inference?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded Substack source was partially access-restricted in this runtime, so Kent Beck's public website and the Software Engineering Radio interview were used as the accessible primary sources for his current AI and design views. Justification: both are first-party or direct Beck interview sources that state the same current positions.
- [assumption] Access note: the seeded Martin Fowler URL for a Cumming article returned 404, so accessible Martin Fowler and Thoughtworks essays on caring about code and modernization economics were substituted. Justification: these are official on-domain sources addressing the same cost and maintenance surface.
- [assumption] Failed primary-study search note: searches including `"daily design investment AI coding randomized study"`, `"Kent Beck augmented coding empirical study"`, and `"strategic tactical division of labour AI software teams controlled trial"` did not surface an accessible head-to-head field experiment on full-team operating models. Justification: the accessible evidence clusters around bounded task experiments, workflow guidance, clarification studies, and longitudinal codebase signals.

#### A. Strategic human work versus tactical AI work

- [fact; source: https://kentbeck.com/] Kent Beck's current public framing of augmented coding says AI deprecates language expertise while amplifying vision, strategy, task breakdown, and feedback loops, and he adds that today's AI assistants "lack taste" and therefore require preserved optionality, meaning preserved future choices, and maintained human judgment.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic's Claude Code guidance says the context window is the most important resource to manage, recommends explore first, then plan, then code, and says the system performs dramatically better when it can verify its own work.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's 2025 context-engineering guidance says complex work needs specification files, modular instructions, validation gates, and session splitting between planning, implementation, and testing.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub Copilot studies show strong tactical gains on bounded tasks, including materially faster task completion and higher success on explicit unit-test tasks.
- [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] The best-supported division of labour is therefore human ownership of architecture, success criteria, context selection, interface design, and verification policy, with AI used as a bounded implementation engine once those constraints are explicit.

#### B. Clarification before code and investigation before advice

- [fact; source: https://arxiv.org/abs/2310.10996] ClarifyGPT introduces a workflow where the model detects ambiguity, asks targeted clarifying questions, refines the requirement, and only then generates code.
- [fact; source: https://arxiv.org/abs/2310.10996] ClarifyGPT raises GPT-4 pass@1 on the Mostly Basic Python Problems (MBPP)-sanitized benchmark from 70.96% to 80.80%, and it also reports multi-benchmark gains for both GPT-4 and ChatGPT.
- [fact; source: https://openreview.net/forum?id=s566pj5E5M] ClariGen reports that a clarifying question-and-answer phase before code generation produces more contextually informed code, improves correctness and reliability, and reduces the need for later revisions.
- [fact; source: https://aclanthology.org/2024.lrec-main.288/] Addlesee et al. show that contextually appropriate clarification behavior only emerges reliably in larger models and when prompted with suitable examples, which means clarification is useful but not automatic.
- [fact; source: https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] Microsoft's investigate-and-respond debugging study inside GitHub Copilot reports that this interaction pattern lowered conversation barriers and produced a 2.5x improvement in bug localization and a 3.5x improvement in bug resolution compared with earlier AI-assisted debugging in Visual Studio.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html] The direct evidence favors a human role that forces clarification, investigation, and boundary setting before or during execution, rather than one that simply approves code after the model has already guessed.

#### C. Kent Beck's design-investment argument

- [fact; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] Beck's public Tidy First? materials frame software design using coupling, where changing one element forces changes in another, cohesion, where related change pressure is concentrated inside one element, and optionality, where design preserves future choices, and they present tidying as a sequence of small structural changes.
- [fact; source: https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] In the 2024 Software Engineering Radio interview, Beck says coupling drives the cost of change, cohesion limits the spread of coupling, and the decision whether or not to design is itself a design decision.
- [fact; source: https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] Beck also says small structural changes can compound, with long runs of small local improvements occasionally unlocking a much larger simplification, and he ties that effect to the observation that most changes happen in a minority of the codebase.
- [fact; source: https://pragprog.com/tips/] Hunt and Thomas's "Don't Live with Broken Windows" tip states that teams should fix bad designs, wrong decisions, and poor code when they see them.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout defines information hiding as keeping design knowledge inside a module so the interface stays much simpler than the implementation, which reduces the amount of cross-module knowledge needed when making changes.
- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Beck's daily-design-investment claim is therefore best understood as an economically framed inference from change-cost theory and high-churn code behavior, not as a precisely measured AI-era multiplier.
- [inference; source: https://kentbeck.com/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://www.anthropic.com/engineering/claude-code-best-practices] In AI-heavy workflows, the plausibility of compounding returns increases because the model repeatedly generates against today's structure, so clearer boundaries and better names should improve tomorrow's generations as well as tomorrow's human changes.

#### D. Bounded-task productivity versus downstream understanding cost

- [fact; source: https://arxiv.org/abs/2302.06590] Peng et al. report that developers with GitHub Copilot access completed a JavaScript Hypertext Transfer Protocol (HTTP) server task 55.8% faster than the control group.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized controlled trial reports that developers using GitHub Copilot had a 53.2% greater likelihood of passing all ten unit tests in the study task and modest statistically significant gains in readability, reliability, maintainability, and concision.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/] GitHub's 2023 study reports that code reviews were more actionable and completed 15% faster with GitHub Copilot Chat, and that 85% of participants felt more confident in code quality with the tool.
- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/] Vaithilingam et al. found that Copilot did not necessarily improve task completion time or success rate in their user study even though participants preferred it, because they still had difficulty understanding, editing, and debugging generated code.
- [fact; source: https://arxiv.org/abs/2303.08733] Liang et al. found useful code generation was the main perceived benefit of GitHub Copilot, while difficulty of integration was the main limitation, and they describe the tool as a double-edged sword.
- [fact; source: https://arxiv.org/abs/2205.06537] Ziegler et al. found that developers' perception of productivity tracked suggestion acceptance rate more strongly than longer-lived persistence metrics in code.
- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2205.06537] The evidence is therefore consistent rather than contradictory: AI produces strong local gains when the task and evaluation criteria are explicit, but ambiguity, integration, and understanding costs can erase part of those gains when human oversight remains weak.

#### E. Why bad code becomes more expensive at AI scale

- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research] GitClear's 2025 analysis of 211 million changed lines reports that code classified as copy-pasted rose from 8.3% of changed lines in 2021 to 12.3% in 2024, while changed lines associated with refactoring fell from 25% to less than 10%.
- [fact; source: https://arxiv.org/abs/2506.04785] Welter et al. found that developers accepted GitHub Copilot's suggestions with less scrutiny than suggestions from human pair-programming partners.
- [fact; source: https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html] Martin Fowler's 2025 essay argues that Large Language Models (LLMs) are inferrers rather than compilers and that AI-assisted software work therefore requires constant risk assessment centered on impact, probability, and detectability.
- [fact; source: https://martinfowler.com/articles/legacy-modernization-gen-ai.html] Thoughtworks' modernization essay says developers spend much more time reading code than writing it and treats understanding existing systems and building better safety nets as the main cost drivers in modernization.
- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733] Academic usability evidence says generated code often imposes later understanding, editing, debugging, and integration burdens even when it feels productive in the moment.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html; https://ml4code.github.io/publications/vaithilingam2022expectation/] Alternative explanations such as changing repository mix or broader delivery pressure may explain part of the cost signal, but the most plausible current explanation is still AI-amplified review and maintenance load because duplication, lighter scrutiny, and debugging burden all move in the same downstream direction across independent sources.

#### F. Opportunity cost of human attention

- [fact; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Current primary workflow guidance repeatedly assigns humans to strategy, scope selection, specification, and judgment, while delegating implementation search to the model.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] The strongest measured workflow improvements come from clarification and investigation phases that reduce guessing before the model commits to an answer.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2302.06590] The main directly measured tactical advantage of AI remains faster completion of repetitive or bounded implementation work.
- [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] Human attention therefore has highest leverage when spent on problem framing, interface design, test and verifier design, code-review standards, and architectural trade-offs, while direct line-by-line implementation is the most defensible delegation target.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/] Positive bounded-task AI results and negative downstream-maintenance signals are compatible because they measure different parts of the workflow.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] The direct empirical support is strongest for "clarify or investigate before acting," not for "let the AI own the whole workflow."
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/abs/2310.10996] A plausible competing hypothesis is that stronger specifications, richer verifiers, and better models could automate much more of the strategic layer, but the current evidence still leaves humans choosing which constraints matter, when clarification is sufficient, and what trade-offs the system should optimize.
- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] The design-investment argument is structurally strong because it rests on change-cost theory, but it remains an inference in AI-heavy workflows because the accessible evidence set argues mechanism and workflow value rather than directly measuring a precise daily-investment percentage and its long-run return.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html] The claim that bad code is more expensive, not cheaper, is better supported than the claim that all AI output is low quality, because the evidence points to scaling of review and maintenance risk rather than universal first-pass failure.

### §4 Consistency Check

- [fact; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/] No contradiction remains between speed gains and design-investment claims once the evidence is separated into bounded implementation tasks versus ambiguous or integration-heavy work.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] No contradiction remains between "AI can help directly" and "humans must stay strategic," because clarification and investigation studies show the best gains when AI operates inside stronger human-guided structure.
- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/] The maintenance-economics claim is kept at inference level because the evidence shows duplication, reduced refactoring, lighter scrutiny, and debugging burden, but it does not yet provide a single unified dollar-cost estimate across teams.

### §5 Depth and Breadth Expansion

- [inference; source: https://kentbeck.com/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html] **Organisational lens:** if AI shifts scarce effort away from code typing and toward judgment, then software teams should increasingly reward architectural clarity, prioritisation, and review quality rather than raw output volume.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] **Economic lens:** lower generation cost increases the return on controls that reduce downstream rework, because every structural flaw can now be reproduced at much higher speed.
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html] **Technical lens:** design investment matters partly because it improves both human comprehension and machine context efficiency, so the same architectural work serves two operators at once.
- [inference; source: https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2205.06537] **Behavioral lens:** developers' willingness to accept useful suggestions quickly can create over-trust, so governance must counteract the psychological appeal of fast local progress.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Even allowing for the competing hypothesis that richer specifications, stronger verifiers, and more capable models could automate more of the strategic layer, the current evidence still favors humans owning architecture, context selection, interface definition, clarification, and verification while AI handles tactical implementation inside those boundaries.
- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Kent Beck's daily design-investment argument is credible and plausibly more valuable under AI-heavy conditions, but the evidence for compounding return remains theory-backed and workflow-backed rather than directly quantified by long-run experiments.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html] The evidence also supports a reversal of "code is cheap" into "bad code is expensive," although that conclusion remains comparative rather than monocausal because some of the downstream cost signal may also reflect changing repository mix or broader delivery pressure.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2302.06590; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] Human attention therefore has its highest leverage in clarifying intent, shaping architecture, and designing verifiers, not in manually typing every line of implementation.

**Key findings:**

1. [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://arxiv.org/abs/2310.10996] Current evidence, even allowing for the competing hypothesis that better specifications and verifiers could shift more strategic work to AI, still supports a strategist-builder split in which humans own architecture, interfaces, context, and verification policy, while AI executes bounded implementation tasks inside those constraints.
2. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html] Clarification and investigation before execution are the most directly evidenced ways to improve human-AI collaboration, because they reduce guessing before code or debugging advice is emitted.
3. [fact; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/] AI coding tools deliver genuine tactical gains on bounded work, including faster completion, better unit-test performance, and quicker code-review cycles when tasks and success criteria are explicit.
4. [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Kent Beck's advice to invest continuously in design quality is best read as a compounding-risk and compounding-optionality argument, and AI plausibly increases its value because future generations inherit today's structure.
5. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html] Bad code is becoming more expensive rather than less expensive at AI scale, because the best-supported current explanation for the observed downstream cost signals is that generation cost is falling faster than scrutiny, understanding, refactoring, and operational risk are falling.
6. [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2205.06537] A dominant failure mode is human over-acceptance of locally useful output that later proves costly to integrate, explain, or revise.
7. [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html] Human attention has highest return when spent on architecture, intent capture, tests, review standards, and prioritisation, while prompt ornamentation and manual boilerplate coding are lower-leverage uses of scarce expert time.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Current evidence still favors humans owning strategic constraints and AI owning bounded implementation, even if future verifier-rich workflows may shift that boundary. | https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://arxiv.org/abs/2310.10996 | medium | Competing hypothesis acknowledged |
| [inference] Clarification and investigation phases improve alignment before execution. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html | medium | Direct empirical support |
| [fact] AI delivers strong tactical gains on explicit tasks. | https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/ | high | Controlled or structured studies |
| [inference] Daily design investment plausibly compounds under AI-heavy workflows because later generations inherit current structure, but the evidence is indirect. | https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | low | Theory-backed and workflow-backed, not directly quantified |
| [inference] The best-supported current explanation is that bad code becomes more expensive at AI scale because review and maintenance do not scale with generation, although other industry shifts may contribute. | https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html | medium | Alternative explanations acknowledged |
| [inference] The main risk is under-scrutinized local usefulness, not universal uselessness. | https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2205.06537 | medium | Usability and perception evidence |
| [inference] Human attention is highest leverage in design, verification, and prioritisation. | https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Guidance plus companion synthesis |

**Assumptions:**

- [assumption] The accessible Beck interview and website represent his current view closely enough to stand in for paywalled or blocked Substack posts. Justification: both are first-party or direct-interview sources from 2024 to 2025 and state concrete positions on augmented coding and design.
- [assumption] The absence of a direct long-run field experiment on team role division means the final operating-model claim must remain synthesis-level rather than elevated to high-confidence fact. Justification: accessible evidence covers adjacent mechanisms rather than the whole team model in one experiment.

**Analysis:**

- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/] The correct synthesis is not "AI is good" or "AI is bad," but that AI is strongest where goals are explicit and weakest where the system must infer hidden intent or integrate into messy contexts.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/] This makes the human's strategic job legible: force clarification, reduce ambiguity, and make the success condition machine-checkable before delegating tactical search.
- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Daily design investment matters because the same naming, interface, and coupling decisions shape both later human changes and later model generations, so design quality becomes a reusable control rather than a one-off aesthetic choice.
- [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html] The economics shift against neglect because high-volume generation magnifies the penalty for weak review and weak architecture, which turns sloppy tactical delegation into a compounding systems-cost problem.

**Risks, gaps, uncertainties:**

- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] The accessible design-investment sources used here argue mechanism and workflow value rather than directly measuring a precise return on a fixed daily design-investment percentage in AI-heavy teams.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Clarification studies are mostly benchmark-based or task-based rather than long-run team ethnographies, so transfer into whole-project economics remains partly inferential.
- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785] Longitudinal evidence on downstream code cost is improving, but it still lacks a single unified model that joins duplication, scrutiny, defect risk, and maintenance spend into one number.

**Open questions:**

- What minimum set of architectural artifacts, types, tests, interface contracts, and repository instructions produces most of the strategist-builder benefit without excessive ceremony?
- At what AI contribution threshold do review capacity and architectural weakness begin to dominate local productivity gains?
- Can future field studies separate the causal contribution of clarification, design investment, and verification policy inside the same team workflow?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-30-strategic-tactical-division-ai-teams.md] This item's synthesis claims are written with either direct source bindings or explicit inference and assumption labels.
- [fact; source: https://kentbeck.com/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2310.10996] Confidence remains medium because the item integrates strong mechanistic and bounded empirical evidence without a single end-to-end randomized study of whole-team role design.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html] Repository cross-references were re-checked before synthesis and sharpen the main control surfaces rather than contradict them.

---

## Findings

### Executive Summary

The best-supported operating model in Artificial Intelligence (AI)-augmented software teams keeps humans responsible for architecture, context, interface definition, clarification, and verification, while delegating bounded implementation work to AI, although stronger specifications, stronger verifiers, and more capable models could shift more strategic work to AI later than current evidence supports. [inference; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M]

Kent Beck's advice to invest continuously in design quality is credible in this setting because coupling, where changing one element forces changes in another, cohesion, where related change pressure stays concentrated inside one element, information hiding, where design knowledge stays inside a module, and optionality, where design preserves future choices, all affect future change cost, and current workflow guidance treats repository structure as part of the context future AI generations consume. [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/]

The compounding-return claim is still indirect, because the accessible design-investment sources used here argue mechanism and workflow value rather than directly measuring a fixed daily design-investment rate against long-run team outcomes under AI-heavy delivery. [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/]

The strongest evidence for the economic side of the question points to "bad code is expensive" rather than "code is cheap," although some of the downstream cost signal may also reflect changing repository mix or broader delivery pressure, because AI can increase duplication, reduce scrutiny, and raise later understanding cost faster than teams can absorb those downstream burdens. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html]

### Key Findings

1. **The strongest available evidence, even allowing for the competing hypothesis that better specifications and verifiers could shift more strategic work to AI, still supports a strategist-builder split in which humans own architecture, interfaces, context, and verification policy, while AI executes bounded implementation tasks inside those constraints.** ([inference]; medium confidence; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://arxiv.org/abs/2310.10996)
2. **Clarification and investigation before execution are the most directly evidenced ways to improve human-AI collaboration, because they reduce guessing before code or debugging advice is emitted and measurably improve correctness or resolution quality.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html)
3. **AI coding tools deliver genuine tactical gains on bounded work, including faster completion, better unit-test performance, and quicker code-review cycles when tasks and success criteria are explicit enough that the model is not forced to infer hidden intent.** ([fact]; high confidence; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/)
4. **Kent Beck's advice to invest continuously in design quality is best read as a compounding-risk and compounding-optionality argument, and AI plausibly increases its value because future generations inherit today's structure rather than starting from a blank slate.** ([inference]; low confidence; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
5. **Bad code is becoming more expensive rather than less expensive at AI scale, because the best-supported current explanation for the observed downstream cost signals is that generation cost is falling faster than scrutiny, understanding, refactoring, and operational risk are falling across real development workflows, even though repository mix and delivery pressure may contribute at the margin.** ([inference]; medium confidence; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html)
6. **A dominant failure mode is human over-acceptance of locally useful output that later proves costly to integrate, explain, debug, or revise inside a larger codebase.** ([inference]; medium confidence; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2205.06537)
7. **Human attention has highest return when spent on architecture, intent capture, tests, review standards, and prioritisation, while prompt ornamentation and manual boilerplate coding are lower-leverage uses of scarce expert time.** ([inference]; medium confidence; source: https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Current evidence still favors humans owning strategic constraints and AI owning bounded implementation, even if future verifier-rich workflows may shift that boundary. | https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://arxiv.org/abs/2310.10996 | medium | Competing hypothesis acknowledged |
| [inference] Clarification and investigation phases improve alignment before execution. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://davidamitchell.github.io/Research/research/2026-04-30-grill-me-ai-alignment-shared-design.html | medium | Direct empirical support |
| [fact] AI delivers strong tactical gains on explicit tasks. | https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/ | high | Controlled or structured studies |
| [inference] Daily design investment likely compounds more strongly under AI-heavy workflows. | https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://pragprog.com/tips/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign | medium | Theory-backed, not directly quantified |
| [inference] The best-supported current explanation is that bad code becomes more expensive at AI scale because review and maintenance do not scale with generation, although other industry shifts may contribute. | https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html; https://martinfowler.com/articles/legacy-modernization-gen-ai.html | medium | Alternative explanations acknowledged |
| [inference] The main risk is under-scrutinized local usefulness, not universal uselessness. | https://ml4code.github.io/publications/vaithilingam2022expectation/; https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2205.06537 | medium | Usability and perception evidence |
| [inference] Human attention is highest leverage in design, verification, and prioritisation. | https://kentbeck.com/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Guidance plus companion synthesis |

### Assumptions

- [assumption; source: https://kentbeck.com/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] The accessible Beck website and interview are adequate stand-ins for blocked or paywalled Substack posts because they state the same core positions on augmented coding, taste, and design judgment.
- [assumption; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.gitclear.com/ai_assistant_code_quality_2025_research] Whole-team role-division conclusions remain inference-level because the available evidence joins mechanism studies and longitudinal signals rather than a single integrated field experiment.

### Analysis

The evidence points to a clean separation between local execution gains and whole-workflow control needs. [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/]

When goals are explicit and tests are available, AI often performs well enough that line-by-line human implementation becomes a lower-value use of expert attention. [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/]

When intent is underspecified, or when the change crosses unclear architectural boundaries, the main determinant of outcome shifts from model fluency to the quality of clarification, context selection, and verification. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.microsoft.com/en-us/research/publication/lets-fix-this-together-conversational-debugging-with-github-copilot/; https://www.anthropic.com/engineering/claude-code-best-practices]

This is why Beck's design-investment claim fits the AI era even without a precise measured multiplier: every improvement to names, boundaries, and tests changes the environment both humans and models operate in next time. [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/]

The long-run economic hazard is that teams may over-index on the visible speed gain and under-invest in the strategic controls that keep output reviewable and reusable. [inference; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html]

### Risks, Gaps, and Uncertainties

- [inference; source: https://www.oreilly.com/library/view/tidy-first/9781098151232/; https://se-radio.net/2024/05/se-radio-615-kent-beck-on-tidy-first/] No accessible source in this evidence set directly measures a universal or recommended daily design-investment percentage for AI-heavy teams.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Clarification studies show mechanism-level gains, but they do not yet provide whole-project maintenance economics.
- [fact; source: https://www.gitclear.com/ai_assistant_code_quality_2025_research; https://arxiv.org/abs/2506.04785] Longitudinal code-quality signals are strong enough to matter, but they still stop short of a unified total-cost-of-ownership model.

### Open Questions

- What is the smallest repeatable package of design artifacts that yields most of the strategist-builder benefit in day-to-day team work?
- How should team staffing, incentives, and review norms change once architectural judgment becomes more valuable than manual implementation volume?
- Which leading indicators best show that an AI-heavy team has crossed from productive delegation into unsustainable review debt?

---

## Output

- Type: knowledge
- Description: Structured synthesis on the strategic versus tactical division of labour in Artificial Intelligence (AI)-augmented software teams, the strength of Kent Beck's daily design-investment argument, and the AI-era economics of bad code.
- Links:
  - https://kentbeck.com/
  - https://arxiv.org/abs/2310.10996
  - https://www.gitclear.com/ai_assistant_code_quality_2025_research
