---
title: "What criteria define tasks where Artificial Intelligence (AI) coding agents reliably add value versus where they introduce systemic risk?"
added: 2026-05-01T08:17:39+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, software-engineering, governance, llm, evaluation]
started: 2026-05-01T20:52:31+00:00
completed: ~
output: [knowledge]
cites: [2026-03-22-agents-as-finishers-and-synthesisers, 2026-04-26-llm-verifiability-asymmetry-code-world-action, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-ai-code-entropy-quality-metrics]
related: [2026-03-22-applied-context-engineering-agent-workflows, 2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-05-01-ai-coding-harness-quality-benchmarks]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What criteria define tasks where Artificial Intelligence (AI) coding agents reliably add value versus where they introduce systemic risk?

## Research Question

What empirically grounded criteria define the characteristics of software development tasks where Artificial Intelligence (AI) coding agents reliably add value, versus tasks where agent autonomy introduces unacceptable systemic risk?

## Scope

**In scope:**
- Characteristics of well-suited agent tasks: bounded scope, verifiable success criteria, non-mission-critical, repetitive or boring, and good isolation where the agent can find everything it needs in context
- Characteristics of poorly suited agent tasks: unbounded scope, no objective success function, mission-critical work, high global interdependency, or work requiring architectural judgment
- Evidence from practitioner accounts and empirical studies on task types where agent performance is reliable versus degraded
- The role of modularity, specifically how codebase structure affects which tasks are safe to delegate
- Specific task categories named in the original motivation for this item: bug reproduction, rubber-duck debugging, boilerplate, non-critical polishing, and reproduction cases
- Hill-climbing and auto-evaluation patterns as enablers of reliable agent use

**Out of scope:**
- Detailed treatment of coding-agent benchmarks as a standalone topic, covered more fully in the benchmark item
- Compound error accumulation as a standalone failure mode, covered more fully in the compounding-error item
- A full governance framework for Artificial Intelligence (AI)-assisted software engineering, covered more fully in synthesis items on sustainable AI software development

**Constraints:**
- Prefer evidence from controlled studies or structured practitioner accounts over anecdote
- Task categorisations should be actionable enough that a developer can apply them to a specific work item before delegation

## Context

- [fact; source: https://pi.dev/; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/] Mario Zechner's published Pi materials emphasize minimal harness complexity, explicit context control, and opt-in workflow extensions rather than assuming that every software task should be delegated to an autonomous coding agent.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Current first-party agent guidance from Anthropic and GitHub treats context scope, verification, and staged workflow structure as first-order reliability constraints rather than as optional refinements.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md] Prior completed work in this repository already suggests that bounded workflow structure, modular code boundaries, external verifiers, and fast feedback loops are recurring control surfaces for safer agent use, so this item focuses on converting those adjacent findings plus external evidence into a practical task-selection rule.

## Approach

1. **Practitioner task taxonomies** - Document the task characteristics from the motivating Pi materials and survey other published practitioner frameworks for overlap and divergence.
2. **Empirical evidence** - Review controlled studies and structured evaluations on the reliability of coding agents across task types, including benchmark difficulty and field data on accepted pull requests (PRs).
3. **Scope and evaluability criteria** - Explain why bounded scope and evaluability matter so much by linking agent-planning guidance, verification guidance, and benchmark evidence.
4. **Modularity as an enabler** - Review evidence that codebase modularity, small well-bounded modules, and explicit interfaces make delegation safer.
5. **Actionable taxonomy** - Synthesize the evidence into a practical decision framework a developer can apply to a specific work item before delegating it.

## Sources

- [x] [Zechner (2025) What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [x] [Pi (2025) Why Pi?](https://pi.dev/)
- [x] [Jimenez et al. (2024) Software Engineering Benchmark (SWE-bench): Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)
- [x] [Pinna et al. (2026) Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance](https://arxiv.org/html/2602.08915v1)
- [x] [Horikawa et al. (2025) Agentic Refactoring: An Empirical Study of AI Coding Agents](https://arxiv.org/abs/2511.04824)
- [x] [Anthropic (2025) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [GitHub (2025) How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [GitHub (2022) Research: quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)
- [x] [Ousterhout (2018) Modular Design lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
- [x] [Parnas (1972) On the Criteria To Be Used in Decomposing Systems into Modules](http://sunnyday.mit.edu/16.355/parnas-criteria.html)
- [x] [Brooks (1987) No Silver Bullet: Essence and Accidents of Software Engineering](https://doi.org/10.1109/MC.1987.1663532)
- [x] [Karpathy (2025) Software Is Changing (Again)](https://www.ycombinator.com/library/MW-andrej-karpathy-software-is-changing-again)

## Related

- [Agents as finishers and synthesisers](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md)
- [Deep modules in AI-augmented development](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md)
- [Large Language Model (LLM) verifiability asymmetry between code and world action](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md)
- [Test-Driven Development (TDD) and fast feedback loops in AI-augmented development](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Research question restated: which characteristics make a software task reliably delegatable to an Artificial Intelligence (AI) coding agent, and which characteristics make delegation unsafe because the agent cannot bound the work, verify success, or contain failure if it is wrong?
- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Scope confirmed: the item covers task-type reliability, verification conditions, modularity and change isolation, and a practical delegation framework, while excluding a full benchmark survey and a full governance program design.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md] Prior completed repository work already established four adjacent claims used here: bounded finisher workflows outperform unconstrained autonomy, deep modules reduce context burden directionally, external verifiers are unusually strong in code domains, and fast feedback loops materially improve agent self-correction.
- [assumption] Workflow constraint: prioritize public evidence that distinguishes task type from raw model strength, keep practitioner claims separate from controlled evidence, and treat reliability as successful completion under explicit checks rather than as plausible output alone. Justification: the goal of this item is a reusable delegation rule, so mixed evidence types need to stay visibly separated.
- [assumption] Output format: use a structured synthesis that states the task-selection rule, maps the supporting evidence, records assumptions and gaps, and turns the result into an actionable screening framework. Justification: the output needs to be reusable as an operational screening tool rather than as a loose narrative summary.

### §1 Question Decomposition

- **Root question:** what properties of a software-development task make current coding agents reliably useful rather than systemically risky?
- **A. Task-type evidence**
  - A1. Which task categories show higher acceptance or completion in real-world or benchmark evidence?
  - A2. Which task categories degrade most sharply as ambiguity, coupling, or novelty increase?
- **B. Scope and evaluability**
  - B1. Why does bounded scope matter for agent performance?
  - B2. Why do explicit tests, repro cases, or other verifiers matter so much?
  - B3. Which tasks lack a strong external success function even if code is produced?
- **C. Modularity and change isolation**
  - C1. What does classic modularity theory say about one-module-at-a-time comprehension?
  - C2. How does that theory translate into agent context burden and change safety?
  - C3. Is there direct head-to-head evidence for modular versus non-modular codebases?
- **D. Systemic-risk boundary**
  - D1. Which task properties raise blast radius or reduce reversibility?
  - D2. Which tasks require architectural, product, or business judgment rather than bounded execution?
  - D3. When does code-verification strength fail to cover the real outcome?
- **E. Practical framework**
  - E1. Which positive criteria should a developer look for before delegation?
  - E2. Which negative criteria should trigger refusal, tighter scoping, or human ownership?
  - E3. What decision questions make the taxonomy operational for everyday work?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded Mario transcript URL resolved to the repository root rather than to a public transcript, so it could not be used as direct evidence for the original conference wording. Justification: the accessible official Pi site and Mario's later blog post document surrounding harness philosophy, but not the exact talk phrasing.
- [assumption] Failed primary-source search note: searches including `"Mario Pi coding agent task selection"`, `"Pi coding agent learn to say no"`, and `"Pi coding agent bug reproduction rubber duck debugging"` did not surface a public transcript or slide deck in this session. Justification: the findings below therefore treat the conference framing as motivating context and rely on independently accessible evidence for the actual task-selection rule.
- [assumption] Access note: the seeded Karpathy URL resolved to a personal homepage rather than to the cited talk page, so the Y Combinator page for *Software Is Changing (Again)* was used as the accessible replacement. Justification: it is the published event page for the referenced talk title.

#### A. Task type is a first-order determinant of observed reliability

- [fact; source: https://arxiv.org/html/2602.08915v1] Pinna et al. analyze 7,156 AI-generated pull requests (PRs) across five agents and report that documentation tasks achieved 82.1% acceptance while new-feature tasks achieved 66.1%, with task-type differences exceeding typical inter-agent variance for most categories.
- [fact; source: https://arxiv.org/html/2602.08915v1] The same study reports that no single agent led every task category: Claude Code led documentation and feature tasks in the retrieved analysis, while Cursor led fix tasks, which means tool choice and task choice interact rather than collapsing to one global ranking.
- [fact; source: https://arxiv.org/abs/2511.04824] Horikawa et al. report that agentic refactoring in open-source Java repositories is dominated by low-level, consistency-oriented edits such as change-variable-type, rename-parameter, and rename-variable operations rather than by sweeping architectural restructures.
- [fact; source: https://arxiv.org/abs/2511.04824] The same refactoring study reports that maintainability and readability account for most explicit motivations behind observed agentic refactors, which indicates that current agents are frequently used for localized quality-improvement work rather than for novel design work.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824] The external evidence therefore supports a task-shape rule: current agents are more reliable on localized, convergent, consistency-oriented tasks than on open-ended or architecturally novel tasks.

#### B. Bounded scope and external evaluability are the core enablers

- [fact; source: https://arxiv.org/abs/2310.06770] Software Engineering Benchmark (SWE-bench) was created precisely because real repository issues require understanding long contexts, coordinating changes across files, and operating in execution environments, and the paper's original evaluation found that the best-performing model in that study solved only 1.96% of the issues.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic's published guidance states that context windows fill quickly, performance degrades as they fill, and the most important resource to manage in an agentic coding session is the context window itself.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] The same guidance states that Claude performs dramatically better when it can verify its own work through tests, comparisons, or other executable checks, and recommends exploring first, then planning, then coding.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's 2025 guidance frames context engineering as ensuring agents focus on the right information rather than more information, and describes specification files and validation gates as tools for making workflows repeatable and reliable.
- [fact; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] GitHub's 2022 controlled study measured a bounded Hypertext Transfer Protocol (HTTP) server task with a test suite and found that developers using GitHub Copilot completed the task 55% faster on average than the control group.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized study also used a bounded web-server task with 10 unit tests and found that code written with Copilot passed more tests and received better review scores on readability, reliability, maintainability, and approval likelihood.
- [inference; source: https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] The common mechanism across benchmark evidence and first-party workflow guidance is not just "small tasks"; it is bounded scope plus an external success function that lets the agent or the human reject bad work quickly.

#### C. Modularity and change isolation determine whether the scope can stay bounded

- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas argues that modularization improves comprehensibility when the system can be studied one module at a time and that the benefits of modularity depend on the criteria used to divide the system into modules.
- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas also lists product flexibility and one-module-at-a-time understanding among the expected benefits of modular programming, which makes change isolation a primary design goal rather than a side effect.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] Ousterhout defines deep modules as modules with a small interface and substantial hidden functionality, and argues that the interface should be much simpler than the implementation so that implementation-only changes do not spill across the rest of the system.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign] The same lecture notes identify information leakage and temporal decomposition as recurrent design problems because they spread knowledge that should stay local across multiple callers and phases.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://www.anthropic.com/engineering/claude-code-best-practices] For a coding agent, deep modules and explicit interfaces matter because they reduce the amount of external knowledge the model must retrieve before making a safe change, which lowers context burden and makes one-module-at-a-time delegation more realistic.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md] The repository's completed deep-modules item reached the same directional conclusion from a larger source set, but explicitly recorded that direct controlled head-to-head evidence comparing deep and shallow codebases for agents was not found.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://arxiv.org/abs/2511.04824] The absence of a direct modularity benchmark does not overturn the modularity argument, but it does keep confidence at medium rather than high because the present case rests on theory plus convergent indirect evidence.

#### D. Feedback loops turn vague work into delegatable work

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md] The repository's completed TDD item found that failing-test-first workflow and fast feedback loops are strong controls because they turn generation into small verifiable increments instead of large unreviewable batches.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] The repository's completed verifiability-asymmetry item found that code domains are unusually strong deployment surfaces for Large Language Models (LLMs) because compilers, type checkers, tests, and similar external verifiers can reject outputs before consequences land.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md] The repository's completed finishers item argued that the strongest practical control set for agent work is bounded scope, explicit definition of done, executable validation steps, reviewable artifacts, escalation rules, and human acceptance at the final gate.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md] Bug reproduction, localized debugging, and small polish tasks become better delegation candidates when they can be reframed as verifier-gated execution tasks instead of as open-ended diagnosis or design tasks.

#### E. Systemic risk begins where local correctness stops being enough

- [fact; source: https://arxiv.org/abs/2310.06770] SWE-bench itself demonstrates that real issue resolution often requires coordinating changes across multiple classes, functions, and files simultaneously, which is exactly where bounded local reasoning begins to fail.
- [fact; source: https://doi.org/10.1109/MC.1987.1663532] Brooks's essential-versus-accidental complexity distinction remains relevant because some software work is about discovering the right problem framing and trade-offs, not merely encoding an already-understood solution.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] The verifiability-asymmetry item also found that code verification does not transfer automatically to higher-level world outcomes, because many consequential decisions lack a domain-complete external verifier even when code compiles and tests pass.
- [inference; source: https://arxiv.org/abs/2310.06770; https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] A task becomes systemically risky when success depends on architecture choice, cross-cutting coordination, ambiguous business intent, or irreversible consequences that are not covered by a strong local verifier.

### §3 Reasoning

- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://arxiv.org/abs/2310.06770] The evidence does not support a binary split between "easy tasks" and "hard tasks." It supports a more precise split between tasks whose relevant context can be bounded and whose outputs can be judged objectively, and tasks whose success depends on diffuse context or open-ended judgment.
- [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices] The positive evidence for coding agents mostly comes from bounded tasks with explicit test suites or review rubrics, which means the apparent productivity gains already presuppose some version of the desired task-selection rule.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://arxiv.org/abs/2511.04824] The modularity argument matters because task suitability is not only a property of the task description; it is also a property of the codebase. The same requested change can be locally bounded in a modular codebase and globally risky in a shallow or tightly coupled one.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md] The practical way to make more tasks safe is therefore not to trust the model more. It is to reshape tasks into smaller, verifier-gated, reviewable units with explicit stop conditions.

### §4 Consistency Check

- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824] The field evidence and refactoring evidence are consistent in one important way: both show better outcomes on localized, well-scoped work than on broad feature or architectural work, even though they measure different surfaces.
- [fact; source: https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Benchmark difficulty, context-management guidance, and verification guidance also point in the same direction, namely that long context and weak success functions are reliability bottlenecks.
- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md] No direct contradiction was found between the modularity theory sources and the AI-specific sources, but the lack of direct modularity experiments means any quantified uplift claim would be unsupported.
- [fact; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://pi.dev/] The retrieved Pi sources support a minimal-harness and explicit-context philosophy, but they do not by themselves prove the exact conference phrasing that motivated this item, so the final conclusions do not depend on the inaccessible transcript wording.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] **Technical lens:** bounded scope is partly a memory-management control, because it preserves context-window budget for the information that actually determines correctness.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824] **Operational lens:** organizations should not evaluate a coding agent only by global averages, because task mix is a confounder. A team can think a tool is "good" or "bad" when the real issue is that it is being assigned the wrong task types.
- [inference; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://arxiv.org/abs/2511.04824] **Economic lens:** boring, repetitive, consistency-oriented work is exactly where even moderate reliability improvements can compound into meaningful throughput gains, because the work volume is high and the novelty burden is low.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md] **Governance lens:** the systemically risky boundary appears before full autonomous world action. It begins as soon as the task exceeds local verification and starts depending on judgment, unobserved downstream effects, or wide cross-system coordination.

### §6 Synthesis

**Executive summary:**

Current Artificial Intelligence (AI) coding agents add value most reliably on tasks that are locally bounded, objectively verifiable, low in blast radius, and structurally isolated from the rest of the codebase. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]

The strongest positive evidence comes from documentation, localized consistency refactors, and bounded coding tasks with explicit test or review rubrics, not from open-ended architectural work or globally coupled repository changes. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://arxiv.org/abs/2310.06770]

Verifier strength is the primary enabling condition, because the task must have a clear done definition that the agent or the human can check with tests, repro cases, linters, review rubrics, or similarly objective gates. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md]

Systemic risk appears when the work is cross-cutting, mission-critical, judgment-heavy, or poorly modularized, because success then depends on diffuse context and consequences that local code correctness cannot fully verify. [inference; source: https://arxiv.org/abs/2310.06770; https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md]

**Key findings:**

1. **Task type appears to influence real-world agent success more strongly than brand-level tool choice, because large-scale field data shows sizeable acceptance-rate gaps between documentation, feature, and fix tasks that exceed typical inter-agent variance for most categories.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1)
2. **Current coding agents are most reliable on localized, convergent work such as documentation, consistency refactors, and tightly scoped bug-fix tasks, because observed agentic refactoring is dominated by low-level edits and the highest field acceptance sits on lower-ambiguity task categories.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824)
3. **Bounded scope by itself is not enough; the task also needs an external success function, because the strongest positive studies for Copilot and the strongest workflow guidance for agents both rely on tests, review rubrics, or other executable checks that can reject bad work quickly.** ([inference]; high confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices)
4. **Repository-scale issue resolution remains a weak delegation surface when the task requires long context, multi-file coordination, and open-ended reasoning, because Software Engineering Benchmark (SWE-bench) was built around exactly those demands and current first-party guidance also identifies long context as a degradation source for coding agents.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices)
5. **Modularity is an enabling condition for safe delegation because deep modules and explicit interfaces reduce the amount of design knowledge that must be loaded outside the change boundary, even though direct controlled comparisons between modular and non-modular codebases for agents remain unavailable.** ([inference]; medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md)
6. **Fast feedback loops such as failing tests, repro cases, and similar verifier gates can convert some debugging and polish work into safe delegation candidates, because they shrink the search space and turn diagnosis into bounded execution against an explicit repair target.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices)
7. **Tasks become systemically risky when success depends on architectural trade-offs, diffuse business intent, cross-cutting repository knowledge, or consequences that local code verifiers do not cover, because in those cases passing tests is no longer a sufficient proxy for a correct outcome.** ([inference]; high confidence; source: https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://arxiv.org/abs/2310.06770)
8. **The most useful practical delegation rule is therefore to give agents convergent execution work with a clear definition of done and to keep humans responsible for divergent judgment, scoping, architecture, and final acceptance, because that is where the evidence base shows the control stack is strongest.** ([inference]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
9. **A developer can operationalize the taxonomy with five screening questions: can the agent find the necessary context, can success be checked objectively, is blast radius low and reversible, is the change isolated, and is the task mostly execution rather than decision-making.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Task type affects field success more than global agent ranking alone. | https://arxiv.org/html/2602.08915v1 | medium | Task-stratified PR evidence |
| [inference] Localized, convergent work is a stronger delegation surface than novel or architectural work. | https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824 | medium | Field data plus refactoring study |
| [inference] Reliable delegation requires bounded scope plus an external success function. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices | high | Tests and review gates |
| [inference] Repository-scale issue resolution remains difficult under long-context, multi-file conditions. | https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Benchmark plus context-limit guidance |
| [inference] Deep modules and explicit interfaces help agents by reducing external knowledge per change. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md | medium | Theory plus prior synthesis |
| [inference] Verifier-gated debugging and polish work can be made safely delegatable. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Feedback-loop mechanism |
| [inference] Systemic risk begins where architecture, judgment, or downstream consequence outrun local verification. | https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://arxiv.org/abs/2310.06770 | high | Essential complexity plus verifier boundary |
| [inference] Human ownership should stay on divergent judgment and acceptance, while agents handle bounded execution. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | high | Convergent workflow guidance |
| [inference] Five screening questions make the taxonomy operational for everyday delegation decisions. | https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md | medium | Synthesized decision rule |

**Assumptions:**

- [assumption; source: https://arxiv.org/html/2602.08915v1] Documentation and low-ambiguity pull-request categories in the field study are treated here as proxies for other low-blast-radius repository tasks, even though they are not identical to every debugging or polish task a team might delegate.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://www.anthropic.com/engineering/claude-code-best-practices] The framework assumes a team can usually create or identify at least one objective verifier for delegatable tasks, such as a failing test, a repro case, a review rubric, or a linter.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] The task-selection rule here is intended for version-controlled software work, not for autonomous agents taking direct consequential world actions outside a strong verifier envelope.

**Analysis:**

The best interpretation of the evidence is that reliable delegation depends on the shape of the task more than on abstract model capability, because the field study, benchmark evidence, and practitioner guidance all separate bounded execution from open-ended judgment in different ways. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices]

Teams should instead ask whether they have shaped the task so the agent can stay inside a legible boundary and know when it is done. [inference; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md]

Modularity matters inside that framing because it changes whether a requested edit is actually local or only appears local on the surface. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md]

The boundary condition is therefore architectural and governance-related at the same time: once local code checks stop being a sufficient proxy for the real outcome, human-led scoping and acceptance have to take over again. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://doi.org/10.1109/MC.1987.1663532]

**Risks, gaps, uncertainties:**

- [fact; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://pi.dev/] The original conference transcript that motivated this research item was not publicly retrievable in this session, so the final criteria do not rely on proving the exact wording of the initial Mario framing.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md] Direct controlled studies comparing agent performance on otherwise similar modular and non-modular codebases were not located, which keeps the modularity-related claims at medium confidence.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824] Acceptance rates and localized refactoring outcomes are useful but incomplete proxies, because they say less about long-term maintainability and cross-release architectural coherence than about immediate task success.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://www.anthropic.com/engineering/claude-code-best-practices] Direct evidence specifically isolating rubber-duck debugging as a high-value task class is still thin, even though the broader verifier-gated debugging mechanism is well supported.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://doi.org/10.1109/MC.1987.1663532] The exact threshold between "mission-critical" and "safe enough" remains organization-specific because the blast radius depends on downstream consequence, not just on code complexity.

**Open questions:**

- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://arxiv.org/html/2602.08915v1] What measurable proxy for change isolation best predicts when a task crosses from a localized fix into an architectural change that current agents handle unreliably?
- [inference; source: https://arxiv.org/abs/2511.04824; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md] How often do high-acceptance low-level agent tasks still contribute to long-run repository entropy when repeated at scale across many pull requests?
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices] Which verifier types, unit tests, repro cases, static analysis, review rubrics, or screenshot diffs, deliver the best reliability gain per minute of setup cost for common software tasks?

**Output:**

- Type: knowledge
- Description: Evidence-backed task-selection framework for deciding when coding agents should be used as bounded execution tools and when the work should remain human-led because verification and change isolation are too weak. [inference; source: https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md]
- Links:
  - https://arxiv.org/html/2602.08915v1
  - https://www.anthropic.com/engineering/claude-code-best-practices
  - https://arxiv.org/abs/2310.06770

### §7 Recursive Review

- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://arxiv.org/abs/2310.06770] Recursive review outcome: the strongest direct evidence retained in the item is task-stratified field performance, localized refactoring behavior, and benchmark difficulty, and all three support the same high-level rule about bounded, verifier-gated work.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/] Remaining uncertainty still comes from two missing surfaces rather than from contradiction: no public transcript for the motivating conference wording and no direct modularity head-to-head experiment for agents.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Confidence remains medium overall because the rule is strongly supported directionally, but some supporting surfaces rely on synthesis across adjacent evidence rather than on a single decisive experiment.
- [fact; source: https://arxiv.org/abs/2310.06770; https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices] Acronym audit completed for the abbreviations used in the Research Skill Output and Findings, including Artificial Intelligence (AI), Large Language Model (LLM), pull request (PR), and Hypertext Transfer Protocol (HTTP), and each is expanded on first use in the audited prose.

---

## Findings

### Executive Summary

Current Artificial Intelligence (AI) coding agents add value most reliably on tasks that are locally bounded, objectively verifiable, low in blast radius, and structurally isolated from the rest of the codebase. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/]

The strongest positive evidence comes from documentation, localized consistency refactors, and bounded coding tasks with explicit test or review rubrics, not from open-ended architectural work or globally coupled repository changes. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824; https://arxiv.org/abs/2310.06770]

Verifier strength is the primary enabling condition, because the task must have a clear done definition that the agent or the human can check with tests, repro cases, linters, review rubrics, or similarly objective gates. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md]

Systemic risk appears when the work is cross-cutting, mission-critical, judgment-heavy, or poorly modularized, because success then depends on diffuse context and consequences that local code correctness cannot fully verify. [inference; source: https://arxiv.org/abs/2310.06770; https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md]

### Key Findings

1. **Task type appears to influence real-world agent success more strongly than brand-level tool choice, because large-scale field data shows sizeable acceptance-rate gaps between documentation, feature, and fix tasks that exceed typical inter-agent variance for most categories.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1)
2. **Current coding agents are most reliable on localized, convergent work such as documentation, consistency refactors, and tightly scoped bug-fix tasks, because observed agentic refactoring is dominated by low-level edits and the highest field acceptance sits on lower-ambiguity task categories.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824)
3. **Bounded scope by itself is not enough; the task also needs an external success function, because the strongest positive studies for Copilot and the strongest workflow guidance for agents both rely on tests, review rubrics, or other executable checks that can reject bad work quickly.** ([inference]; high confidence; source: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices)
4. **Repository-scale issue resolution remains a weak delegation surface when the task requires long context, multi-file coordination, and open-ended reasoning, because Software Engineering Benchmark (SWE-bench) was built around exactly those demands and current first-party guidance also identifies long context as a degradation source for coding agents.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices)
5. **Modularity is an enabling condition for safe delegation because deep modules and explicit interfaces reduce the amount of design knowledge that must be loaded outside the change boundary, even though direct controlled comparisons between modular and non-modular codebases for agents remain unavailable.** ([inference]; medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md)
6. **Fast feedback loops such as failing tests, repro cases, and similar verifier gates can convert some debugging and polish work into safe delegation candidates, because they shrink the search space and turn diagnosis into bounded execution against an explicit repair target.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices)
7. **Tasks become systemically risky when success depends on architectural trade-offs, diffuse business intent, cross-cutting repository knowledge, or consequences that local code verifiers do not cover, because in those cases passing tests is no longer a sufficient proxy for a correct outcome.** ([inference]; high confidence; source: https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://arxiv.org/abs/2310.06770)
8. **The most useful practical delegation rule is therefore to give agents convergent execution work with a clear definition of done and to keep humans responsible for divergent judgment, scoping, architecture, and final acceptance, because that is where the evidence base shows the control stack is strongest.** ([inference]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
9. **A developer can operationalize the taxonomy with five screening questions: can the agent find the necessary context, can success be checked objectively, is blast radius low and reversible, is the change isolated, and is the task mostly execution rather than decision-making.** ([inference]; medium confidence; source: https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Task type affects field success more than global agent ranking alone. | https://arxiv.org/html/2602.08915v1 | medium | Task-stratified PR evidence |
| [inference] Localized, convergent work is a stronger delegation surface than novel or architectural work. | https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824 | medium | Field data plus refactoring study |
| [inference] Reliable delegation requires bounded scope plus an external success function. | https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices | high | Tests and review gates |
| [inference] Repository-scale issue resolution remains difficult under long-context, multi-file conditions. | https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Benchmark plus context-limit guidance |
| [inference] Deep modules and explicit interfaces help agents by reducing external knowledge per change. | http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md | medium | Theory plus prior synthesis |
| [inference] Verifier-gated debugging and polish work can be made safely delegatable. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices | medium | Feedback-loop mechanism |
| [inference] Systemic risk begins where architecture, judgment, or downstream consequence outrun local verification. | https://doi.org/10.1109/MC.1987.1663532; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://arxiv.org/abs/2310.06770 | high | Essential complexity plus verifier boundary |
| [inference] Human ownership should stay on divergent judgment and acceptance, while agents handle bounded execution. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | high | Convergent workflow guidance |
| [inference] Five screening questions make the taxonomy operational for everyday delegation decisions. | https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md | medium | Synthesized decision rule |

### Assumptions

- [assumption; source: https://arxiv.org/html/2602.08915v1] Documentation and low-ambiguity pull-request categories in the field study are treated here as proxies for other low-blast-radius repository tasks, even though they are not identical to every debugging or polish task a team might delegate.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://www.anthropic.com/engineering/claude-code-best-practices] The framework assumes a team can usually create or identify at least one objective verifier for delegatable tasks, such as a failing test, a repro case, a review rubric, or a linter.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md] The task-selection rule here is intended for version-controlled software work, not for autonomous agents taking direct consequential world actions outside a strong verifier envelope.

### Analysis

The best interpretation of the evidence is that reliable delegation depends on the shape of the task more than on abstract model capability, because the field study, benchmark evidence, and practitioner guidance all separate bounded execution from open-ended judgment in different ways. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2310.06770; https://www.anthropic.com/engineering/claude-code-best-practices]

Teams should instead ask whether they have shaped the task so the agent can stay inside a legible boundary and know when it is done. [inference; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md]

Modularity matters inside that framing because it changes whether a requested edit is actually local or only appears local on the surface. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md]

The boundary condition is therefore architectural and governance-related at the same time: once local code checks stop being a sufficient proxy for the real outcome, human-led scoping and acceptance have to take over again. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://doi.org/10.1109/MC.1987.1663532]

### Risks, Gaps, and Uncertainties

- [fact; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://pi.dev/] The original conference transcript that motivated this research item was not publicly retrievable in this session, so the final criteria do not rely on proving the exact wording of the initial Mario framing.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md] Direct controlled studies comparing agent performance on otherwise similar modular and non-modular codebases were not located, which keeps the modularity-related claims at medium confidence.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2511.04824] Acceptance rates and localized refactoring outcomes are useful but incomplete proxies, because they say less about long-term maintainability and cross-release architectural coherence than about immediate task success.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md; https://www.anthropic.com/engineering/claude-code-best-practices] Direct evidence specifically isolating rubber-duck debugging as a high-value task class is still thin, even though the broader verifier-gated debugging mechanism is well supported.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-llm-verifiability-asymmetry-code-world-action.md; https://doi.org/10.1109/MC.1987.1663532] The exact threshold between mission-critical work and safe-enough work remains organization-specific because the blast radius depends on downstream consequence, not just on code complexity.

### Open Questions

- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-deep-modules-ai-augmented-codebases.md; https://arxiv.org/html/2602.08915v1] What measurable proxy for change isolation best predicts when a task crosses from a localized fix into an architectural change that current agents handle unreliably?
- [inference; source: https://arxiv.org/abs/2511.04824; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md] How often do high-acceptance low-level agent tasks still contribute to long-run repository entropy when repeated at scale across many pull requests?
- [inference; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://www.anthropic.com/engineering/claude-code-best-practices] Which verifier types, unit tests, repro cases, static analysis, review rubrics, or screenshot diffs, deliver the best reliability gain per minute of setup cost for common software tasks?

---

## Output

- Type: knowledge
- Description: Evidence-backed task-selection framework for deciding when coding agents should be used as bounded execution tools and when the work should remain human-led because verification and change isolation are too weak. [inference; source: https://arxiv.org/html/2602.08915v1; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-22-agents-as-finishers-and-synthesisers.md]
- Links:
  - https://arxiv.org/html/2602.08915v1
  - https://www.anthropic.com/engineering/claude-code-best-practices
  - https://arxiv.org/abs/2310.06770
