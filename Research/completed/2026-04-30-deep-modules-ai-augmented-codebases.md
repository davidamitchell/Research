---
review_count: 2
title: "Deep modules in AI-augmented development: interface design, contract-first delegation, and architectural rescue of AI-generated codebases"
added: 2026-04-30T20:31:45+00:00
status: completed
priority: high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, evaluation, agentic-ai]
started: 2026-04-30T21:18:01+00:00
completed: 2026-04-30T21:41:16+00:00
output: [knowledge]
cites: [2026-04-30-ai-code-entropy-quality-metrics, 2026-03-16-intent-driven-development, 2026-03-14-reliable-software-llm-era, 2026-04-26-llm-verifiability-asymmetry-code-world-action]
related: [2026-04-26-software-engineering-investment-case-llm, 2026-03-22-coding-ai-agent-skills-survey, 2026-04-02-org-shape-software-cost-zero]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: d71b0b3b5a093554dd975d8128ba033deaa6fd7e
    changed: 2026-04-30
    progress: progress/2026-04-30-deep-modules-ai-augmented-codebases.md
    summary: "Initial completion"
---

# Deep modules in AI-augmented development: interface design, contract-first delegation, and architectural rescue of AI-generated codebases

## Research Question

How much more effective is Artificial Intelligence (AI) at understanding, navigating, and correctly modifying a codebase composed of deep modules with simple interfaces versus one filled with many shallow modules, and can iterative architectural improvement rescue an AI-generated "ball of mud" codebase, and if so what is the typical effort-versus-benefit ratio?

## Scope

**In scope:**
- Deep modules definition from John Ousterhout's *A Philosophy of Software Design*: modules with powerful functionality behind a small, simple interface, contrasted with shallow modules that expose as much complexity as they hide
- AI code navigation and comprehension: empirical or practitioner evidence that deep modules reduce the cognitive load and context-window pressure on AI assistants when modifying or extending existing code
- Contract-first delegation, meaning a human developer defines the contract, examples, tests, and type boundaries while delegating most implementation detail to an AI assistant
- Iterative architectural improvement: refactoring-first approaches for AI-generated codebases and any evidence on effort and benefit
- Connection to information hiding and module decomposition: David Parnas's information-hiding principle as the theoretical parent, and its relevance to AI-assisted development
- The cost of rescue: how much effort is required to recover a densely coupled, weakly named, shallow-module codebase after it has been AI-generated without architectural guidance

**Out of scope:**
- Code entropy metrics and measurement methodology, covered in `2026-04-30-ai-code-entropy-quality-metrics`
- Test-Driven Development (TDD) as an interface-design tool, covered in `2026-04-30-tdd-feedback-loops-ai-augmented-dev`
- Ubiquitous Language (UL) and domain naming, covered in `2026-04-30-ubiquitous-language-ai-code-consistency`
- Microservices architecture at system-of-systems level, unless directly relevant to code-level module decomposition

**Constraints:**
- Sources from 2020 onwards preferred for AI-specific evidence; foundational Software Engineering (SE) texts accepted regardless of date
- Practitioner case studies accepted if sufficiently detailed; anecdote without a traceable source remains labelled `[assumption]`
- Direct controlled comparisons between deep and shallow module structures for AI agents may not exist; if absent, the gap must be stated explicitly rather than filled with confident extrapolation

## Context

- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; http://sunnyday.mit.edu/16.355/parnas-criteria.html] Ousterhout argues that a deep module hides substantial implementation complexity behind a simple interface, and Parnas argues that modularization works best when modules hide design decisions likely to change.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Current agentic coding guidance treats context-window management, specification artifacts, and explicit verification criteria as operational necessities rather than stylistic preferences.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] This makes module depth, interface clarity, and verifier-gated delegation plausible control surfaces for AI coding outcomes even when direct deep-versus-shallow experiments are missing.

## Approach

1. **Define deep versus shallow modules in the AI context** - Summarize Ousterhout's framework and Parnas's information-hiding principle, then map them to AI-assisted development.
2. **Survey AI comprehension and modification evidence** - Search for studies or practitioner reports that link architecture, context management, or interface quality to AI coding performance.
3. **Examine contract-first delegation** - Search for interface-first, type-first, test-first, and specification-first guidance for AI coding, and assess whether the pattern is directly evidenced or mainly inferential.
4. **Review rescue approaches for ball-of-mud codebases** - Survey incremental refactoring guidance, hotspot prioritization, change-coupling analysis, and AI-assisted large-scale cleanup case studies.
5. **Analyse effort versus benefit** - Estimate what can be said credibly about rescue cost and payoff without inventing an unsupported universal multiplier.
6. **Synthesize** - Produce a structured assessment: whether deep modules are an AI-readiness investment, what minimal architecture enables safer delegation, and what realistic rescue looks like for already-messy codebases.

## Sources

- [x] [Ousterhout (2021) A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php)
- [x] [Ousterhout (2018) Modular Design lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
- [x] [Parnas (1972) On the Criteria To Be Used in Decomposing Systems into Modules](http://sunnyday.mit.edu/16.355/parnas-criteria.html)
- [x] [Fowler (2018) Refactoring: Improving the Design of Existing Code](https://martinfowler.com/books/refactoring.html)
- [x] [Gamma et al. (1994) Design Patterns: Elements of Reusable Object-Oriented Software](https://www.oreilly.com/library/view/design-patterns-elements/0201633612/)
- [x] [Tornhill (2018) Software Design X-Rays](https://pragprog.com/titles/atevol/software-design-x-rays/)
- [x] [Pocock (2025) Cursor Rules for Better AI Development](https://www.totaltypescript.com/cursor-rules-for-better-ai-development)
- [x] [Pocock (2025) Should You Declare Return Types?](https://www.totaltypescript.com/should-you-declare-return-types)
- [x] [Pocock (2025) The Case for TypeScript in the AI Coding Era](https://www.totaltypescript.com/the-case-for-typescript-in-the-ai-coding-era)
- [x] [Anthropic (2025) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [GitHub (2025) How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
- [x] [Santos et al. (2025) Decoding the Configuration of AI Coding Agents: Insights from Claude Code Projects](https://arxiv.org/html/2511.09268v1)
- [x] [Ziegler et al. (2022) Productivity Assessment of Neural Code Completion](https://arxiv.org/abs/2205.06537)
- [x] [Dakhel et al. (2023) GitHub Copilot AI Pair Programmer: Asset or Liability?](https://arxiv.org/abs/2206.15331)
- [x] [Welter et al. (2025) From Developer Pairs to AI Copilots: A Comparative Study on Knowledge Transfer](https://arxiv.org/abs/2506.04785)
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [GitHub (2023) Research: Quantifying GitHub Copilot's impact on code quality](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/)
- [x] [Atlassian (2025) How to effectively utilise AI to enhance large-scale refactoring](https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring)
- [x] [CodeScene (2021) Change coupling: visualize the cost of change](https://codescene.com/blog/change-coupling-visualize-the-cost-of-change)
- [x] [CodeScene (2021) Measure code health of your codebase](https://codescene.com/blog/measure-code-health-of-your-codebase)
- [x] [Mitchell (2026) Artificial Intelligence code entropy and complexity](https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html)
- [x] [Mitchell (2026) Intent Driven Development](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)
- [x] [Mitchell (2026) Reliable Software in the LLM Era](https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html)
- [x] [Mitchell (2026) LLM verifiability asymmetry between code and world action](https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html)

## Related

- [Artificial Intelligence code entropy and complexity](https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html)
- [Intent Driven Development](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)
- [Reliable Software in the LLM Era](https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html)
- [LLM verifiability asymmetry between code and world action](https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Research question restated: do deep modules with simple interfaces make AI coding agents materially better at understanding and modifying codebases than shallow, densely coupled structures, and if a codebase is already a ball of mud, can iterative architectural improvement recover enough structure to make AI delegation safer and more productive?
- [fact; source: https://www.totaltypescript.com/should-you-declare-return-types; https://arxiv.org/html/2511.09268v1; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Scope confirmed: the item covers foundational module theory, AI-specific context and verification guidance, interface-first delegation patterns, and rescue case evidence, while treating any exact uplift multiplier as unproven unless directly measured.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase] Output format confirmed: structured knowledge note with explicit findings on architecture benefit, delegation pattern maturity, rescue feasibility, and effort-versus-benefit limits.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] Prior completed repository work already establishes four adjacent claims used here: local AI coding quality can improve while repository entropy worsens over time, layered intent artifacts outperform vague prompting, deterministic verification matters more than generation fluency, and verifier-gated software engineering is a stronger Large Language Model (LLM) deployment surface than open-world consequential action.

### §1 Question Decomposition

- **Root question:** what codebase structure and workflow boundaries make AI coding agents more reliable, and how recoverable is a poorly structured AI-generated codebase?
- **A. Theory**
  - A1. What do Parnas and Ousterhout mean by information hiding, deep modules, and shallow modules?
  - A2. Why would deep modules reduce the amount of knowledge an AI agent must load to make a safe change?
- **B. Architecture and context evidence**
  - B1. Do current agent guidance sources treat architecture and context boundaries as first-order concerns?
  - B2. Is there any direct empirical comparison between deep and shallow architectures for AI agents?
- **C. Gray-box delegation**
  - C1. What evidence exists for interface-first, type-first, or test-first delegation to AI?
  - C2. Is contract-first delegation a named, evidenced pattern or mainly a synthesis from adjacent practices?
- **D. Rescue of ball-of-mud codebases**
  - D1. What does classic refactoring literature say about recovering structure safely?
  - D2. What do hotspot and change-coupling methods contribute to rescue prioritization?
  - D3. What AI-assisted large-scale refactoring cases reveal about feasible workflows?
- **E. Effort versus benefit**
  - E1. What effort-benefit claims are directly evidenced?
  - E2. Which claims remain inferential or unquantified?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded Total TypeScript page `https://www.totaltypescript.com/ai-coding-assistants` was not a live public page during this session, so the official Total TypeScript article index and the accessible articles on Cursor rules, return types, and TypeScript in the AI era were used instead. Justification: those replacement pages are official, on-domain sources that address the same control surface.
- [assumption] Access note: the seeded Parnas DOI landing page was access-restricted in this runtime, so an accessible MIT-hosted reprint was used for the abstract and quoted text. Justification: the mirror identifies the original publication and reproduces the text needed for this investigation.
- [assumption] Failed-study-search note: searches for a direct controlled comparison between deep-module and shallow-module codebases for AI agents, using queries including `"deep modules AI coding assistant controlled study"` and `"well-defined interfaces modular codebase Copilot experiment"`, did not surface a directly relevant head-to-head benchmark in the accessible literature. Justification: available results clustered around theory, configuration studies, and practitioner guidance rather than architecture A/B experiments.

#### A. Foundational theory: information hiding and module depth

- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas's abstract states that modularization improves flexibility and comprehensibility, and that the effectiveness of modularization depends on the criteria used to divide the system into modules.
- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas's first expected benefits of modular programming are shorter development time, product flexibility, and the ability to understand the system one module at a time.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout defines a deep class as a module with a small interface and lots of hidden functionality, and defines a shallow class as one whose interface complexity is large relative to the functionality it hides.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout states that the design goal is for the interface to be much simpler than the implementation, because a change that affects only the implementation should not affect other modules.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout explicitly says that size matters less than depth, and that classes in the 200 to 2000 line range can be acceptable if the abstraction is powerful and the interface remains simple.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout identifies information leakage and temporal decomposition as recurring causes of poor modular design, because they spread implementation knowledge across multiple call sites or stages.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] In AI-assisted development, the same theory predicts that deep modules should reduce the amount of code and hidden dependency knowledge an agent must retrieve before it can make a bounded change, because more of the relevant reasoning is concentrated behind the interface rather than spread across consumers.

#### B. AI context, architecture, and verification evidence

- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic's Claude Code guidance states that context windows fill quickly, performance degrades as context fills, and context is the most important resource to manage in agentic coding sessions.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] The same Anthropic guidance says Claude performs dramatically better when it can verify its work through tests, comparisons, or executable checks, and recommends explore first, then plan, then code.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's 2025 context-engineering guidance defines specification files as implementation-ready blueprints, describes context engineering as ensuring agents focus on the right information rather than simply more information, and recommends modular instructions and phase separation to preserve focus.
- [fact; source: https://arxiv.org/html/2511.09268v1] Santos et al. analyze 328 Claude Code configuration files and report that publicly shared agent configurations emphasize a broad range of software engineering concerns, with particular emphasis on architecture.
- [fact; source: https://arxiv.org/html/2511.09268v1] The same paper describes configuration files as sources of architecture constraints, coding practices, and tool-use policies that guide autonomous software engineering work.
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/html/2511.09268v1] These sources jointly support a directional claim that architecture quality affects AI effectiveness, because they treat context scope, architectural constraints, and verification boundaries as core determinants of agent reliability rather than optional optimizations.

#### C. Interface-first and contract-first delegation evidence

- [fact; source: https://www.totaltypescript.com/cursor-rules-for-better-ai-development] Matt Pocock's public Cursor rules article argues that community rule sets are often low quality, and says his own rules focus on language features, documentation, and structure that are widely applicable.
- [fact; source: https://www.totaltypescript.com/should-you-declare-return-types] Pocock's return-types article states that top-level functions should declare return types because doing so helps future AI assistants understand the function's purpose.
- [fact; source: https://www.totaltypescript.com/the-case-for-typescript-in-the-ai-coding-era] Pocock's broader AI-era argument for TypeScript begins from the premise that type information, while carrying some upfront cost, becomes more valuable when AI tools must infer and preserve program intent.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic recommends providing example tests, explicit validation criteria, and concrete file references before asking the agent to implement a change.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's context-engineering article recommends specification files, reusable prompts, and agentic workflows with built-in validation rather than ad hoc prompting alone.
- [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] The public evidence supports a contract-first delegation pattern in practice: the human defines the contract surface, validation criteria, and architecture constraints, and the AI fills in implementation detail inside that envelope.
- [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices] This pattern is stronger than "ask the model to do everything" because explicit return types, tests, and file-scoped constraints reduce ambiguity before the agent starts generating code.
- [assumption] Public guidance from TypeScript-heavy sources is relevant to other typed or test-driven ecosystems to the extent that the control surface is the same, namely explicit interfaces plus executable verification. Justification: the core mechanism is interface clarity rather than TypeScript syntax itself.

#### D. What current AI quality evidence does and does not show

- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized controlled study found that developers with GitHub Copilot access had a 53.2 percent greater likelihood of passing all 10 unit tests in the task, and small statistically significant gains in readability, reliability, maintainability, and conciseness.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-code-quality/] GitHub's 2023 Copilot Chat study reported that code reviews were completed 15 percent faster, and framed maintainability in terms of minimizing dependencies and keeping code understandable and reusable.
- [fact; source: https://arxiv.org/abs/2206.15331] Dakhel et al. report that Copilot can solve many bounded programming problems, but also that some solutions are buggy, non-reproducible, and weak at combining multiple methods into a correct whole.
- [fact; source: https://arxiv.org/abs/2205.06537] Ziegler et al. report that developers' perception of productivity is driven by suggestion acceptance rate more than by persistence of completions in the code over time.
- [fact; source: https://arxiv.org/abs/2506.04785] Welter et al. report that developers accept GitHub Copilot suggestions with less scrutiny than they accept suggestions from human pair-programming partners.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2205.06537; https://arxiv.org/abs/2506.04785] This evidence supports bounded-task usefulness, but it does not directly show how AI performs on deep versus shallow architectures, so any architecture claim must be inferred from theory, context evidence, and repository-scale maintainability evidence rather than presented as a measured multiplier.

#### E. Repository-scale and rescue evidence

- [fact; source: https://martinfowler.com/books/refactoring.html] Fowler defines refactoring as a controlled technique for improving the design of an existing code base through small, behavior-preserving transformations whose cumulative effect can be significant.
- [fact; source: https://pragprog.com/titles/atevol/software-design-x-rays/] Tornhill's *Software Design X-Rays* description says behavioral code analysis uses version-control data to identify hotspots, prioritize technical debt, measure refactoring effects, and uncover dependencies that code inspection alone misses.
- [fact; source: https://codescene.com/blog/change-coupling-visualize-the-cost-of-change] CodeScene's change-coupling article defines change coupling as files or modules that continuously co-evolve in the same commit sets, and argues that unexplained tight coupling is often a signal of severe maintenance issues such as God Classes.
- [fact; source: https://codescene.com/blog/measure-code-health-of-your-codebase] CodeScene's code-health article argues that hotspot trends matter more than absolute static numbers, and that early detection is valuable because declining hotspot health tends to persist once feature pressure displaces cleanup.
- [fact; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Atlassian's 2025 large-scale refactoring report describes removing feature gates and mocks across roughly 1,400 files by using persistent AI context, discovery prompts, package-level cleanup methods, small batches, and repeated validation.
- [fact; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] The same Atlassian report states that an initial "AI to scripts to cleanup" approach increased workload because generated code still required heavy review and manual refactoring, but that the refined context-rich, iterative workflow produced a safe large-scale cleanup process and approximately 2x productivity.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] The companion repository item on AI code entropy concludes that the best early warning signals are clone ratio, short-term churn, hotspot code-health decline, and unexpected change coupling rather than defect counts alone.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] Architectural rescue is feasible, but the credible path is iterative and hotspot-first rather than one-shot, because hidden coupling and declining code health are precisely the signals that make a full blind rewrite unsafe and uneconomic.

#### F. Cross-item integration

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html] The repository's formal-methods companion item concludes that validation, not generation, is the central reliability problem in LLM-assisted software development.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] The repository's intent-driven-development item concludes that the strongest public implementations depend on layered artifacts rather than intent statements alone.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] The repository's verifiability item concludes that software engineering is strongest when outputs pass through external verifier gates rather than model confidence.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] Deep modules fit this broader stack because they localize implementation complexity, make contract surfaces clearer, and give verifiers and humans a more bounded unit to inspect.

### §3 Reasoning

- [fact; source: https://arxiv.org/abs/2205.06537; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] The available direct AI studies primarily measure bounded tasks, review outcomes, or suggestion acceptance, not architecture-level comprehension differences across whole codebases.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1] The strongest defensible claim is therefore directional rather than numerical: deep modules should help AI agents because they minimize the externally visible knowledge surface, and current agent guidance repeatedly treats constrained context and architecture as critical.
- [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Gray-box delegation is best treated as a synthesized practice pattern rather than a directly benchmarked method, because the evidence comes from convergent guidance on interfaces, specs, and verification rather than from a named controlled trial.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change] Rescue claims should also stay bounded: there is good evidence for iterative cleanup and hotspot-prioritized gains, but not for a universal rescue ratio that would apply across all AI-generated codebases.

### §4 Consistency Check

- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] There is no contradiction between positive bounded-task Copilot results and caution about long-run entropy, because the underlying evidence speaks to different timescales and different units of analysis.
- [fact; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://www.anthropic.com/engineering/claude-code-best-practices] There is no contradiction between using AI for rescue and arguing that AI-generated ball-of-mud code is risky, because the successful rescue evidence depends on strong context, batching, verification, and human review rather than on unconstrained generation.
- [inference; source: https://arxiv.org/html/2511.09268v1; https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices] Architecture-sensitive guidance, explicit interfaces, and verification criteria point in the same direction, so the synthesis can claim practical convergence without overstating it as a settled quantitative law.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://pragprog.com/titles/atevol/software-design-x-rays/; https://codescene.com/blog/measure-code-health-of-your-codebase] Effort-versus-benefit remains medium-confidence because the rescue literature supports prioritization logic and iterative transformation, but does not provide a single cross-project cost curve.

### §5 Depth and Breadth Expansion

- [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices] **Technical lens:** deep modules matter to AI for the same reason they matter to humans, namely that the required reasoning boundary becomes smaller and more stable per change.
- [inference; source: https://arxiv.org/abs/2506.04785; https://www.totaltypescript.com/should-you-declare-return-types] **Behavioral lens:** because developers scrutinize AI suggestions less than human suggestions, upstream interface clarity and explicit contracts become more important, not less.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://codescene.com/blog/measure-code-health-of-your-codebase] **Economic lens:** rescue economics favor small, validated refactorings on active hotspots because the cumulative benefit of repeated cleanups is more credible than a speculative full rewrite payoff.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-14-reliable-software-llm-era.html; https://davidamitchell.github.io/Research/research/2026-04-26-llm-verifiability-asymmetry-code-world-action.html] **Governance lens:** deep modules strengthen verifier-gated development because smaller, cleaner interfaces make it easier to attach tests, type checks, model-based checks, and review boundaries to the right unit of change.

### §6 Synthesis

**Executive summary:**

- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1] Indirect evidence suggests Artificial Intelligence (AI) coding agents should be more reliable in codebases built from deep modules with explicit interfaces than in shallow, densely coupled codebases, but the gain appears to come from a bundle of controls that also includes verifier strength, type information, tests, and repository instruction artifacts rather than from module depth alone.
- [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] The best-supported delegation pattern keeps humans responsible for contract design and verification while letting the AI search within that boundary for a working implementation.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] A densely coupled codebase with weak boundaries can be rescued incrementally, but the credible path is hotspot-first and batch-validated rather than a one-shot rewrite.
- [inference; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] The effort-versus-benefit ratio is therefore highly uneven: targeted architectural work on high-churn boundaries can produce meaningful gains, while whole-repository rescue becomes more expensive as hidden coupling, duplication, and code-health decline accumulate.

**Key findings:**

1. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1] The available evidence for architecture benefit is indirect rather than head-to-head: foundational module theory, modern context-management guidance, and configuration studies converge on the same mechanism, but none of them quantifies a universal uplift multiplier.
2. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices] Deep modules should improve AI codebase navigation and modification because they minimize the amount of design knowledge exposed across call sites, which lowers the context each change requires.
3. [fact; source: https://arxiv.org/html/2511.09268v1; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://www.anthropic.com/engineering/claude-code-best-practices] Current agent guidance and configuration practice repeatedly elevate architecture, context scope, and verification rules as operational concerns rather than as afterthoughts.
4. [fact; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.totaltypescript.com/cursor-rules-for-better-ai-development] Public practitioner evidence directly shows that explicit interface cues such as return types and durable rule files are treated as aids to future AI assistants' understanding of code intent.
5. [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] Contract-first delegation is the most defensible workflow pattern because it combines architecture, explicit types, tests, and repository instruction artifacts while preserving human ownership of contracts and verification.
6. [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2506.04785] Bounded-task AI coding can be genuinely useful, but weaker human scrutiny and fragile multi-step reasoning make architecture and verifier boundaries more important than raw suggestion quality alone.
7. [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Rescue of a densely coupled codebase with weak boundaries is feasible through iterative refactoring, hotspot prioritization, persistent context, and small validated batches, and the available evidence favors that path over blind whole-repository rewrites.
8. [inference; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://codescene.com/blog/measure-code-health-of-your-codebase] The payoff from rescue is front-loaded on active hotspots and interface seams, while the cost rises as hidden coupling and declining code health accumulate, so no single effort-benefit ratio is portable across codebases.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The architecture-benefit case is indirect: theory, context guidance, and configuration evidence align, but no universal uplift multiplier is measured. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1 | medium | Indirect convergence |
| [inference] Deep modules should reduce AI context burden per change. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Theory plus agent guidance |
| [fact] Architecture and context rules are prominent operational concerns in agent configuration practice. | https://arxiv.org/html/2511.09268v1; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | medium | Public config ecosystem |
| [fact] Explicit return types and durable rule files are used to help AI understand code intent. | https://www.totaltypescript.com/should-you-declare-return-types; https://www.totaltypescript.com/cursor-rules-for-better-ai-development | medium | Practitioner guidance |
| [inference] Contract-first delegation is best supported when architecture is paired with types, tests, and repository instructions. | https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html | medium | Convergent, not direct trial |
| [inference] Bounded-task quality gains do not eliminate the need for stronger architecture and verification. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2506.04785 | medium | Local gains, review limits |
| [inference] Available rescue evidence favors iterative, hotspot-first cleanup over blind whole-repository rewrites. | https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring | medium | Classic plus modern case |
| [inference] Rescue return on investment (ROI) concentrates on high-churn hotspots and interface seams. | https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://codescene.com/blog/measure-code-health-of-your-codebase | medium | No universal ratio |

**Assumptions:**

- [assumption; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices] Interface-first guidance from TypeScript-centric sources is treated as relevant to broader software engineering because the claimed mechanism is explicit contract surface rather than language choice alone.
- [assumption; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Atlassian's feature-gate cleanup case is treated as relevant to AI-generated-code rescue even though the target code was not described as wholly AI-generated, because the case still shows what large-scale, context-rich architectural cleanup requires in practice.
- [assumption; source: https://arxiv.org/html/2511.09268v1] The absence of a direct benchmark in the accessible search is treated as an evidence gap rather than as proof that architecture does not matter.

**Analysis:**

- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices] The core analytic move is to combine a strong theoretical mechanism with modern agent constraints: information hiding reduces externally required knowledge, and context limits make externally required knowledge the scarce resource for AI agents.
- [inference; source: https://arxiv.org/html/2511.09268v1; https://www.totaltypescript.com/should-you-declare-return-types; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] The public AI-era evidence is stronger on design and workflow convergence than on causal measurement, which is why the item can recommend deep modules and contract-first delegation directionally without pretending the uplift is already numerically pinned down.
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2506.04785] Bounded-task quality gains and reduced scrutiny can coexist, which explains why teams can feel faster locally while still accumulating architectural debt globally.
- [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Rescue economics favor a modular-monolith style of cleanup, namely identifying active seams, restoring boundaries, and iterating with tests and history-based metrics, because that is where current evidence ties effort to observable benefit.

**Risks, gaps, uncertainties:**

- [inference; source: https://arxiv.org/html/2511.09268v1; https://www.anthropic.com/engineering/claude-code-best-practices] The sources reviewed here do not provide a direct controlled study that compares otherwise similar deep-module and shallow-module codebases under the same AI task.
- [fact; source: https://www.totaltypescript.com/cursor-rules-for-better-ai-development; https://www.totaltypescript.com/should-you-declare-return-types] The strongest public evidence for contract-first delegation is practitioner guidance rather than controlled experimentation.
- [fact; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] The best rescue case in this item is a single detailed practitioner report rather than a multi-organization benchmark.
- [inference; source: https://codescene.com/blog/measure-code-health-of-your-codebase; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html] Any whole-repository effort curve remains uncertain because rescue cost depends heavily on hidden coupling, hotspot distribution, and how much executable verification already exists.

**Open questions:**

- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] What measurable proxy for module depth best predicts agent success on multi-file maintenance tasks?
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1] Can a controlled study randomize the same repository into deep-boundary and shallow-boundary variants to estimate the architecture effect on agent accuracy and context consumption directly?
- [inference; source: https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] Which hotspot-first rescue sequence gives the best return in real AI-heavy codebases: interface extraction, dependency inversion, module consolidation, or test-harness reinforcement?

### §7 Recursive Review

- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1] Every architecture-benefit claim retained in this item is either grounded directly in foundational module theory or explicitly marked as an inference from modern agent-context evidence.
- [fact; source: https://www.totaltypescript.com/should-you-declare-return-types; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://www.anthropic.com/engineering/claude-code-best-practices] The contract-first delegation section has been kept at medium confidence because the pattern is supported by convergent guidance rather than by a direct comparative experiment.
- [fact; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring] The rescue section claims only incremental, hotspot-first feasibility and avoids an unsupported universal multiplier.
- [fact; source: https://arxiv.org/html/2511.09268v1] Confidence remains medium overall because the central conclusion is plausible and well-supported directionally, but direct architecture A/B evidence is still missing.

---

## Findings

### Executive Summary

Indirect evidence suggests Artificial Intelligence (AI) coding agents should be more reliable in codebases organized around deep modules with explicit interfaces than in shallow, densely coupled codebases, but the gain appears to come from a bundle of controls that also includes verifier strength, type information, tests, and repository instruction artifacts rather than from module depth alone. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1]

The best-supported delegation pattern keeps humans responsible for contract design and verification while letting the AI search within that boundary for a working implementation, which makes module depth one enabling condition among several rather than the sole cause of safer outcomes. [inference; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html]

A densely coupled codebase with weak boundaries can be rescued incrementally, but the credible path is hotspot-first and batch-validated rather than a one-shot rewrite. [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring]

The effort-versus-benefit ratio is therefore highly uneven: targeted architectural work on high-churn boundaries can produce meaningful gains, while whole-repository rescue becomes more expensive as hidden coupling, duplication, and code-health decline accumulate. [inference; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://codescene.com/blog/measure-code-health-of-your-codebase]

### Key Findings

1. **The available evidence for architecture benefit is indirect rather than head-to-head: foundational module theory, modern context-management guidance, and configuration studies converge on the same mechanism, but none of them quantifies a universal uplift multiplier.** ([inference]; medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1)
2. **Deep modules should improve AI codebase navigation and modification because they minimize the amount of design knowledge exposed across call sites, which lowers the context each change requires and keeps more reasoning inside a bounded implementation surface.** ([inference]; medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices)
3. **Current agent guidance and configuration practice repeatedly elevate architecture, context scope, and verification rules as operational concerns rather than as afterthoughts, which shows that these surfaces are treated as first-class configuration targets in real agent workflows.** ([fact]; medium confidence; source: https://arxiv.org/html/2511.09268v1; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://www.anthropic.com/engineering/claude-code-best-practices)
4. **Public practitioner evidence directly shows that explicit interface cues such as return types and durable rule files are treated as aids to future AI assistants' understanding of code intent, which gives a concrete small-scale example of the broader deep-module argument.** ([fact]; medium confidence; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.totaltypescript.com/cursor-rules-for-better-ai-development)
5. **Contract-first delegation is the most defensible workflow pattern because it combines architecture, explicit types, tests, and repository instruction artifacts while preserving human ownership of contracts and verification, even though the pattern is better supported as a synthesis than as a named experimental method.** ([inference]; medium confidence; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)
6. **Bounded-task AI coding can be genuinely useful, but weaker human scrutiny and fragile multi-step reasoning make architecture and verifier boundaries more important than raw suggestion quality alone when changes must remain coherent across a codebase.** ([inference]; medium confidence; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2506.04785)
7. **Rescue of a densely coupled codebase with weak boundaries is feasible through iterative refactoring, hotspot prioritization, persistent context, and small validated batches, and the available evidence favors that path over blind whole-repository rewrites.** ([inference]; medium confidence; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring)
8. **The payoff from rescue is front-loaded on active hotspots and interface seams, while the cost rises as hidden coupling and declining code health accumulate, so no single effort-benefit ratio is portable across codebases.** ([inference]; medium confidence; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://codescene.com/blog/measure-code-health-of-your-codebase)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] The architecture-benefit case is indirect: theory, context guidance, and configuration evidence align, but no universal uplift multiplier is measured. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1 | medium | Indirect convergence |
| [inference] Deep modules should reduce AI context burden per change. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Theory plus agent guidance |
| [fact] Architecture and context rules are prominent operational concerns in agent configuration practice. | https://arxiv.org/html/2511.09268v1; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | medium | Config ecosystem |
| [fact] Explicit return types and durable rule files are used to help AI understand code intent. | https://www.totaltypescript.com/should-you-declare-return-types; https://www.totaltypescript.com/cursor-rules-for-better-ai-development | medium | Small-scale direct evidence |
| [inference] Contract-first delegation is best supported when architecture is paired with types, tests, and repository instructions. | https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html | medium | Convergent guidance |
| [inference] Local AI quality gains do not remove the need for stronger architecture and verification. | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://arxiv.org/abs/2206.15331; https://arxiv.org/abs/2506.04785 | medium | Local gains, scrutiny limits |
| [inference] Available rescue evidence favors iterative, hotspot-first cleanup over blind whole-repository rewrites. | https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring | medium | Classic plus modern case |
| [inference] Rescue return on investment (ROI) concentrates on high-churn hotspots and interface seams. | https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html; https://codescene.com/blog/measure-code-health-of-your-codebase | medium | No universal ratio |

### Assumptions

- Interface-first guidance from TypeScript-centric sources is relevant to broader software engineering because the claimed mechanism is explicit contract surface rather than language choice alone. [assumption; source: https://www.totaltypescript.com/should-you-declare-return-types; https://www.anthropic.com/engineering/claude-code-best-practices]
- Atlassian's feature-gate cleanup case is relevant to AI-generated-code rescue even though the target code was not described as wholly AI-generated, because the case still shows what large-scale, context-rich architectural cleanup requires in practice. [assumption; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring]
- The absence of a direct benchmark in the accessible search is an evidence gap rather than proof that architecture does not matter. [assumption; source: https://arxiv.org/html/2511.09268v1]

### Analysis

The core analytic move is to combine a strong theoretical mechanism with modern agent constraints: information hiding reduces externally required knowledge, and context limits make externally required knowledge the scarce resource for AI agents. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices]

The public AI-era evidence is stronger on design and workflow convergence than on causal measurement, which is why this item can recommend deep modules and contract-first delegation directionally without pretending the uplift is already numerically pinned down. [inference; source: https://arxiv.org/html/2511.09268v1; https://www.totaltypescript.com/should-you-declare-return-types; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/]

A rival explanation is that verifier strength, test coverage, type information, naming and specification artifacts, and repository instructions drive most of the observed gain regardless of module depth. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://arxiv.org/html/2511.09268v1; https://www.totaltypescript.com/should-you-declare-return-types]

The evidence partly supports that rival explanation, which is why the strongest conclusion here is not that architecture dominates those controls, but that deep modules make them more local, legible, and enforceable inside real maintenance tasks. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/]

Rescue economics favor modular cleanup, namely identifying active seams, restoring boundaries, and iterating with tests and history-based metrics, because that is where current evidence ties effort to observable benefit. [inference; source: https://martinfowler.com/books/refactoring.html; https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://codescene.com/blog/measure-code-health-of-your-codebase; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring]

### Risks, Gaps, and Uncertainties

- The sources reviewed here do not provide a direct controlled study that compares otherwise similar deep-module and shallow-module codebases under the same AI task. [inference; source: https://arxiv.org/html/2511.09268v1; https://www.anthropic.com/engineering/claude-code-best-practices]
- The strongest public evidence for contract-first delegation is practitioner guidance rather than controlled experimentation. [fact; source: https://www.totaltypescript.com/cursor-rules-for-better-ai-development; https://www.totaltypescript.com/should-you-declare-return-types]
- The best rescue case in this item is a single detailed practitioner report rather than a multi-organization benchmark. [fact; source: https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring]
- Any whole-repository effort curve remains uncertain because rescue cost depends heavily on hidden coupling, hotspot distribution, and how much executable verification already exists. [inference; source: https://codescene.com/blog/measure-code-health-of-your-codebase; https://davidamitchell.github.io/Research/research/2026-04-30-ai-code-entropy-quality-metrics.html]

### Open Questions

- What measurable proxy for module depth best predicts agent success on multi-file maintenance tasks? [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]
- Can a controlled study randomize the same repository into deep-boundary and shallow-boundary variants to estimate the architecture effect on agent accuracy and context consumption directly? [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/html/2511.09268v1]
- Which hotspot-first rescue sequence gives the best return in real AI-heavy codebases: interface extraction, dependency inversion, module consolidation, or test-harness reinforcement? [inference; source: https://codescene.com/blog/change-coupling-visualize-the-cost-of-change; https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring]

---

## Output

- Type: knowledge
- Description: A research note concluding that deep modules and contract-first delegation are directionally beneficial for AI coding, while architectural rescue is feasible only through iterative hotspot-first refactoring rather than one-shot rewrites.
- Links:
  - https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign
  - https://www.anthropic.com/engineering/claude-code-best-practices
  - https://www.atlassian.com/blog/development/how-to-effectively-utilise-ai-to-enhance-large-scale-refactoring
