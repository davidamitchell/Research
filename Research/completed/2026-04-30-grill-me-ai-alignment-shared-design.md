---
review_count: 2
title: "Grill-Me technique: iterative structured interviewing for human and Artificial Intelligence (AI) alignment in code generation"
added: 2026-04-30T20:31:45+00:00
status: completed
priority: high  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, evaluation, workflow, agentic-ai]
started: 2026-04-30T22:07:42+00:00
completed: 2026-04-30T22:26:16+00:00
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-30-fundamentals-first-vs-specs-to-code, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-03-16-intent-driven-development]
related: [2026-04-30-ai-code-entropy-quality-metrics, 2026-03-14-reliable-software-llm-era]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 02e771d6cbd0a627737ba93a82f578cffeb57dcf
    changed: 2026-04-30
    progress: progress/2026-04-30-grill-me-ai-alignment-shared-design.md
    summary: "Initial completion"
---

# Grill-Me technique: iterative structured interviewing for human and Artificial Intelligence (AI) alignment in code generation

## Research Question

How effectively does the "Grill Me" technique, relentless iterative structured interviewing of the human developer by the AI assistant to build a shared design concept before generating any code, reduce misalignment between human intent and AI-generated output, and what are the measurable outcome differences compared to jumping directly into plan or code generation?

## Scope

**In scope:**
- Definition and mechanics of the "Grill Me" interaction pattern: the AI asks clarifying questions before producing any design or code, the human answers, and the AI iterates until it can restate the requirements without ambiguity
- Measurement of alignment quality: how precisely the resulting code matches the original human intent, defect rates, and the number of post-generation correction rounds required
- Measurable outcome differences between grill-first sessions and prompt-to-code sessions: correctness of first output, revision cycles, and time-to-working-feature
- Iteration dynamics: how many questions or rounds are typically required to reach a stable shared design concept, and which question types surface the most critical hidden assumptions or unspecified dependencies
- Connection to adjacent software engineering practices: specification quality, requirements gathering, user story refinement, and whether "Grill Me" is a natural-language analogue for these activities in AI-augmented workflows
- Empirical evidence from practitioner reports, academic studies, or controlled experiments where available

**Out of scope:**
- Full analysis of Test-Driven Development (TDD) integration with AI, covered in `2026-04-30-tdd-feedback-loops-ai-augmented-dev`
- Deep module and architectural design decisions, covered in `2026-04-30-deep-modules-ai-augmented-codebases`
- Ubiquitous Language (UL) and domain glossary effects, covered in `2026-04-30-ubiquitous-language-ai-code-consistency`

**Constraints:**
- Evidence must be traceable to named practitioners, studies, or published frameworks; anecdote without source is flagged as `[assumption]`
- Sources from 2022 onwards preferred; older foundational software engineering sources accepted for the requirements-gathering analogy

## Context

- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Current code-generation evidence shows a recurring alignment problem: developers often like AI output as a fast starting point, but still struggle with code that misses unstated intent or becomes expensive to understand, debug, and review.
- [fact; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral] Matt Pocock's "Grill Me" technique responds to that problem by forcing a clarifying interview before planning or coding, with one question at a time and an explicit goal of reaching shared understanding.
- [inference; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2310.10996] The likely mechanism is not magical prompting but explicit requirements discovery: hidden assumptions are surfaced before the model is allowed to guess, which should improve first-pass correctness on underspecified tasks and reduce downstream rework.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] This item sits inside a broader repository thread arguing that better alignment artifacts, clearer architecture, and stronger verification loops are the main way to turn AI coding speed into durable engineering value.

## Approach

1. **Define the technique** - Identify the canonical public description of "Grill Me" from Matt Pocock's published skills and blog posts. Extract the mechanism, question cadence, and stopping criterion. Compare the pattern to Three Amigos refinement and related requirements-discovery practices.
2. **Survey empirical evidence** - Search for controlled experiments, practitioner case studies, or interactive code-generation research that measures output quality when sessions begin with structured clarification instead of immediate code generation.
3. **Measure iteration dynamics** - Review published or practitioner data on how many clarifying rounds are needed before output stabilises, and which question types surface the highest-impact hidden assumptions.
4. **Compare outcome metrics** - Examine defect rates, revision cycles, time-to-working-feature, and developer experience. If no direct controlled comparison exists, state the gap explicitly and keep any synthesis claim at inference level.
5. **Assess transferability** - Check whether the clarification-first mechanism appears across multiple models, stacks, or public agent workflows, and identify where evidence remains thin.
6. **Synthesise** - Produce a structured assessment of whether "Grill Me" is a high-Return on Investment (ROI) practice, where it is most useful, and what evidence is still missing.

## Sources

- [x] [Pocock (2025) grill-me skill](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md)
- [x] [Pocock (2025) My Grill Me Skill Has Gone Viral](https://www.aihero.dev/my-grill-me-skill-has-gone-viral)
- [x] [Pocock (2025) 5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)
- [x] [Mu et al. (2023) ClarifyGPT: Empowering LLM-based Code Generation with Intention Clarification](https://arxiv.org/abs/2310.10996)
- [x] [Miao et al. (2025) ClariGen: Bridging Instruction Gaps via Interactive Clarification in Code Generation](https://openreview.net/forum?id=s566pj5E5M)
- [x] [Addlesee et al. (2024) Clarifying Completions: Evaluating How LLMs Respond to Incomplete Questions](https://aclanthology.org/2024.lrec-main.288/)
- [x] [Vaithilingam et al. (2022) Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models](https://ml4code.github.io/publications/vaithilingam2022expectation/)
- [x] [Nguyen and Nadi (2022) An Empirical Evaluation of GitHub Copilot's Code Suggestions](https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf)
- [x] [Peng et al. (2023) The Impact of AI on Developer Productivity: Evidence from GitHub Copilot](https://arxiv.org/abs/2302.06590)
- [x] [GitHub (2024) Does GitHub Copilot improve code quality? Here's what the data says](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/)
- [x] [Liang et al. (2023) Practices and Challenges of Using GitHub Copilot: An Empirical Study](https://arxiv.org/abs/2303.08733)
- [x] [Anthropic (2025) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [GitHub (2025) How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
- [x] [Smart (2017) One to request, one to suggest and one to protest: the anatomy of a Three Amigos Requirements Discovery workshop](https://johnfergusonsmart.com/three-amigos-requirements-discovery/)
- [x] [Mitchell (2026) Fundamentals-first versus specs-to-code](https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
- [x] [Mitchell (2026) Deep modules in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [x] [Mitchell (2026) Intent Driven Development](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)

## Related

- [Fundamentals-first versus specs-to-code](https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
- [Deep modules in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [Intent Driven Development](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Research question restated: does a clarification-first "Grill Me" workflow materially reduce misalignment between human intent and generated code, and how much stronger is that outcome than going directly from prompt to plan or code?
- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf; https://arxiv.org/abs/2302.06590] Scope confirmed: this item covers the public Pocock technique, direct clarification-before-code studies, baseline code-generation studies that show why ambiguity matters, and requirements-discovery analogues, while treating long-run project-level head-to-head evidence as sparse.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://johnfergusonsmart.com/three-amigos-requirements-discovery/] Output format confirmed: structured knowledge note with explicit claims on technique mechanics, correctness effects, revision-cycle effects, iteration dynamics, transferability, and uncertainty.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] Prior completed repository work already sharpens this item in three ways: fundamentals-first workflows outperform pure prompt-to-code mainly by reducing ambiguity and strengthening feedback loops, deep modules reduce the reasoning surface agents must search, and intent-driven development treats richer intent artifacts as the real bound on the solution space.

### §1 Question Decomposition

- **Root question:** How much alignment benefit comes from forcing clarification before code generation, and what evidence supports that benefit?
- **A. Technique definition**
  - A1. What exactly does Matt Pocock instruct the agent to do in a grilling session?
  - A2. What is the stopping rule, and what makes the interaction different from ordinary planning?
- **B. Direct code-generation evidence**
  - B1. Do clarification-before-code systems improve first-pass correctness on underspecified tasks?
  - B2. Are those gains visible across more than one model or benchmark?
- **C. Baseline misalignment evidence**
  - C1. What do Copilot usability and correctness studies show about ambiguity, over-reliance, and debugging burden when developers skip clarification?
  - C2. What bounded-task benefits does direct prompt-to-code still provide?
- **D. Software engineering analogue**
  - D1. Which established requirements-discovery practices most closely match Grill Me?
  - D2. What question types do those practices use to surface hidden assumptions?
- **E. Synthesis**
  - E1. Which outcome differences are directly measured, and which remain inferred?
  - E2. What is known about question counts, session length, and transferability?
  - E3. Is Grill Me best understood as a prompting trick or as a requirements-elicitation workflow?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded Total TypeScript page `https://www.totaltypescript.com/ai-coding-assistants` returned 404 in this session, so official Matt Pocock sources were substituted with the raw `grill-me` skill file and two AI Hero posts. Justification: those replacement sources are current first-party Pocock publications that describe the same technique.
- [assumption] Failed primary-study search note: searches including `"grill me prompt-to-code randomized study"`, `"clarifying questions code generation field study revision rounds"`, and `"Matt Pocock grill me empirical evaluation"` did not surface an accessible long-run head-to-head field study of grill-first versus prompt-to-code workflows. Justification: the accessible evidence clusters around controlled benchmark studies, public workflow guidance, and usability studies rather than project-length randomized comparisons.

#### A. Technique mechanics

- [fact; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md] The raw `grill-me` skill tells the agent to interview the user relentlessly about every aspect of the plan until shared understanding is reached, walk down each branch of the design tree, provide a recommended answer for each question, ask one question at a time, and answer questions from codebase exploration when possible.
- [fact; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral] Pocock's AI Hero explanation says the technique is for the early phase of coding, where requirements must be discovered by talking through the change before implementation starts.
- [fact; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock reports that grilling sessions often last about 45 minutes, and that one feature discussion took 16 questions while complex features can take 30, 40, or even 50 questions.
- [fact; source: https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock explicitly frames the goal as reaching shared understanding with the Large Language Model (LLM) before Claude Code or another agent starts emitting a plan too early.
- [inference; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral] The operational stopping criterion is not "enough questions were asked" but "the design tree has been walked far enough that the agent can restate the change without obvious unresolved branches."

#### B. Direct evidence that clarifying questions improve code generation

- [fact; source: https://arxiv.org/abs/2310.10996] ClarifyGPT introduces a code-generation workflow where the model first detects ambiguity, asks targeted clarifying questions, refines the requirement, and only then generates code.
- [fact; source: https://arxiv.org/abs/2310.10996] ClarifyGPT reports that clarifying questions increased GPT-4 first-attempt benchmark correctness on the Mostly Basic Python Problems (MBPP)-sanitized benchmark from 70.96% to 80.80%.
- [fact; source: https://arxiv.org/abs/2310.10996] ClarifyGPT also reports multi-benchmark gains, improving average performance across four benchmarks from 68.02% to 75.75% for GPT-4 and from 58.55% to 67.22% for ChatGPT.
- [fact; source: https://openreview.net/forum?id=s566pj5E5M] ClariGen states that adding an explicit clarifying question-and-answer phase before code generation produces more contextually informed code and that high-quality clarifications substantially improve both correctness and reliability while reducing the need for subsequent revisions.
- [fact; source: https://aclanthology.org/2024.lrec-main.288/] Addlesee et al. show that contextually appropriate clarifying-completion behavior only emerges reliably in larger LLMs and when models are prompted with suitable examples, which means clarification is useful but not automatic.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://aclanthology.org/2024.lrec-main.288/] The strongest direct evidence for Grill Me's mechanism is therefore not the Pocock workflow alone but the broader result that structured clarification on ambiguous tasks measurably raises first-pass code correctness and reliability.

#### C. Baseline evidence on why prompt-to-code misaligns

- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/] Vaithilingam et al. report that Copilot did not necessarily improve task completion time or success rate in their user study, even though most participants preferred it because it provided a useful starting point and reduced online searching.
- [fact; source: https://ml4code.github.io/publications/vaithilingam2022expectation/] The same study reports that participants had significant difficulty understanding, editing, and debugging generated code, and that those difficulties hindered task-solving effectiveness.
- [fact; source: https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf] Nguyen and Nadi's evaluation found that correctness varied by language and prompt context, with some incorrect suggestions relying on undefined helper methods, which is a concrete example of the model guessing beyond the user's actual requirement.
- [fact; source: https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] GitHub's 2024 randomized controlled trial found that developers with Copilot access had a 53.2% greater likelihood of passing all ten unit tests in the study task, which confirms that direct prompt-to-code can work well when the task is bounded and evaluation criteria are clear.
- [fact; source: https://arxiv.org/abs/2302.06590] Peng et al. found that developers with Copilot access completed a JavaScript Hypertext Transfer Protocol (HTTP) server task 55.8% faster than the control group, which confirms a real speed benefit for direct generation under controlled conditions.
- [fact; source: https://arxiv.org/abs/2303.08733] Liang et al. describe Copilot as a double-edged sword and report that practitioners' main limitation was difficulty of integration, which is consistent with a workflow where local snippet help does not automatically resolve broader design intent.
- [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] The baseline pattern is therefore mixed rather than uniformly bad: prompt-to-code is fast and often locally correct, but the moment requirements are incomplete or the code must be adapted, understanding and revision costs rise sharply.

#### D. Requirements-discovery analogue from software engineering

- [fact; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/] John Ferguson Smart describes Three Amigos as a collaborative requirements-discovery workshop whose main goal is shared understanding, specifically to avoid misunderstandings, incorrect assumptions, and overlooked details before implementation.
- [fact; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/] Smart says effective sessions use concrete examples to discover business rules, and that developers and testers contribute technical constraints, edge cases, and testability concerns.
- [fact; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/] Smart recommends short sessions shortly before work starts, and says they are commonly time-boxed to 30 to 45 minutes.
- [fact; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock independently describes Grill Me as an early-phase conversation for discovering requirements and explicitly compares it to rubber ducking, where talking through the idea surfaces hidden permutations before code exists.
- [inference; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/5-agent-skills-i-use-every-day] Grill Me is best understood as a one-human, one-agent natural-language version of requirements elicitation, not as a standalone generation trick, because both workflows spend upfront time surfacing examples, constraints, edge cases, and design dependencies before execution starts.

#### E. Iteration dynamics, transferability, and public workflow guidance

- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic advises users not to let Claude jump straight to coding, recommends explore first, then plan, then code, and states that vague tasks without clear success criteria often produce solutions to the wrong problem.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's 2025 context-engineering guidance argues that ad hoc prompting works for simple fixes but complex work needs reusable structure, specification artifacts, and context that keeps the agent focused on the right information rather than just more information.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The direct clarification-before-code studies span more than one model and more than one benchmark family, which is evidence that the mechanism is not specific to a single vendor model.
- [inference; source: https://www.aihero.dev/5-agent-skills-i-use-every-day; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Transferability looks plausible across coding agents because the common mechanism is ambiguity reduction plus scoped context management, both of which are model-agnostic workflow properties rather than TypeScript-only prompt wording.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590] The outcome difference most directly supported today is better first-pass correctness under ambiguous requirements, while evidence for full lifecycle benefits such as lower long-run defect rate or shorter total time-to-working-feature remains indirect.

### §3 Reasoning

- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://johnfergusonsmart.com/three-amigos-requirements-discovery/] The cleanest causal chain is: ambiguous requirement leads to clarifying questions, clarifying questions refine the requirement, and refined requirements improve first-pass correctness and reduce later revision pressure.
- [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf] The strongest negative case against prompt-to-code is not that models always fail, but that users often accept plausible starting points that are harder to understand and correct than they initially appear.
- [inference; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock's reported question counts and session lengths are useful practitioner evidence for iteration dynamics, but they do not establish a universal optimal number of questions.
- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] Any claim that Grill Me is always faster than direct generation would be unsupported, because direct generation still has strong bounded-task speed and quality results when the problem is already well specified.

### §4 Consistency Check

- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] No contradiction appears between the direct clarification studies: both report correctness or reliability gains when an interactive clarification phase is added before code generation.
- [fact; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/; https://ml4code.github.io/publications/vaithilingam2022expectation/] No contradiction appears between positive Copilot productivity results and the usability warnings, because those studies measure different things: bounded-task speed and test outcomes on one hand, versus comprehension, debugging, and workflow fit on the other.
- [inference; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://www.aihero.dev/5-agent-skills-i-use-every-day] The human requirements-discovery analogue is directionally consistent with Pocock's technique, but the mapping remains an inference because Three Amigos is a team workshop rather than a one-user, one-agent workflow.

### §5 Depth and Breadth Expansion

- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] **Technical lens:** clarification shifts work from post hoc debugging into pre-generation requirement refinement, which is cheaper when ambiguity is the root cause and not just a symptom.
- [inference; source: https://arxiv.org/abs/2302.06590; https://ml4code.github.io/publications/vaithilingam2022expectation/; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] **Economic lens:** Grill Me likely pays back most on multi-step or high-ambiguity changes, while trivial or fully specified tasks may still be better served by direct generation because the questioning overhead would dominate.
- [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://www.aihero.dev/my-grill-me-skill-has-gone-viral] **Behavioural lens:** the technique counters premature closure by forcing the human and the model to notice gaps before plausible code creates false confidence.
- [inference; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] **Historical lens:** Grill Me fits a long software-engineering pattern where better outcomes come from better requirement articulation and richer intent artifacts, not from hoping implementation will discover the missing constraints by itself.

### §6 Synthesis

**Executive summary:**

Grill Me is an effective alignment technique when the task is ambiguous because it turns more of the user's hidden intent into explicit pre-code constraints before generation begins. [inference; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The strongest direct evidence comes from clarification-before-code research, which shows measurable gains in first-pass correctness and reliability when models ask targeted questions before writing code. [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Baseline Copilot studies explain why that helps in practice: direct generation is often fast and locally useful, but developers still lose time when they must understand, edit, and debug code generated from incomplete requirements. [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf; https://arxiv.org/abs/2302.06590] The remaining uncertainty is which ingredient matters most, because current studies do not cleanly separate ambiguity reduction from extra interaction time, richer examples, or longer context accumulation, and they do not yet show the full-project wall-clock effect in production. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices]

**Key findings:**

1. **Matt Pocock's Grill Me technique is a concrete clarification-first workflow in which the agent asks one question at a time, walks the design tree branch by branch, recommends answers, and stops only when shared understanding has been reached.** ([fact]; medium confidence; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral)
2. **Direct code-generation research shows that adding a targeted clarifying-question phase before code generation materially improves first-pass correctness on underspecified tasks, including a GPT-4 benchmark correctness increase from 70.96% to 80.80% in ClarifyGPT.** ([fact]; medium confidence; source: https://arxiv.org/abs/2310.10996)
3. **A second clarification-before-code study, ClariGen, reports that high-quality clarifications improve code correctness and reliability while reducing later revision needs, which supports the same mechanism through a separate research program but currently with thinner evidence than ClarifyGPT.** ([fact]; low confidence; source: https://openreview.net/forum?id=s566pj5E5M)
4. **Baseline Copilot usability evidence shows why Grill Me matters: users often prefer generated code as a starting point, but still lose effectiveness when they must understand, edit, and debug output produced from incomplete or mismatched requirements.** ([fact]; high confidence; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf)
5. **The strongest software-engineering analogue for Grill Me is requirements discovery rather than prompt optimization, because Three Amigos workshops use concrete examples, edge cases, technical constraints, and testability questions to surface hidden assumptions before implementation begins.** ([inference]; medium confidence; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)
6. **Pocock's public examples report Grill Me sessions ranging from 16 questions on a smaller feature to roughly 30 to 50 questions on more complex changes, and he says these conversations often last about 45 minutes, which suggests the practice is a real discovery phase rather than a one-line prompt enhancement.** ([inference]; medium confidence; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day)
7. **Compared with jumping directly to code, Grill Me is best supported as a way to improve first-output correctness and reduce correction rounds under ambiguity, but direct evidence that it always shortens total time-to-working-feature is still missing.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
8. **The available evidence suggests Grill Me is likely transferable across models and stacks because clarification gains appear in multi-model studies and the same explore-then-plan guidance appears in both Anthropic and GitHub workflow recommendations, but industrial cross-language head-to-head data remains thin.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Grill Me is a one-question-at-a-time design interview that resolves dependencies until shared understanding. | https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral | medium | Direct Pocock mechanism |
| [fact] ClarifyGPT raises first-pass correctness by adding clarifying questions before code generation. | https://arxiv.org/abs/2310.10996 | medium | Measured benchmark gain |
| [fact] ClariGen reports correctness, reliability, and revision benefits from interactive clarification. | https://openreview.net/forum?id=s566pj5E5M | low | Abstract-level evidence |
| [fact] Prompt-to-code remains attractive but creates comprehension and debugging burden when intent is incomplete. | https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf | high | Baseline misalignment evidence |
| [inference] Grill Me maps most closely to requirements-discovery practices such as Three Amigos. | https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html | medium | Mechanism match |
| [inference] Pocock's public examples suggest 16 to 50 questions and sessions that often last about 45 minutes on non-trivial work. | https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day | medium | Pocock-reported examples |
| [inference] The clearest proven advantage is better first-output correctness, not guaranteed lower total cycle time. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Lifecycle gap remains |
| [inference] Transferability is plausible across models because ambiguity reduction and context scoping are model-agnostic mechanisms. | https://arxiv.org/abs/2310.10996; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | medium | Multi-model plus workflow guidance |

**Assumptions:**

- [assumption] The current Pocock first-party sources are an acceptable substitute for the dead Total TypeScript seed URL because they describe the same technique in current public form.
- [assumption] The absence of an accessible long-run randomized field study means project-length benefits must be inferred from benchmark studies, usability studies, and requirements-discovery analogues rather than asserted directly.

**Analysis:**

The evidence supports Grill Me most strongly as an ambiguity-management workflow rather than as a universal speed hack. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590] Direct clarification studies carry the core causal weight because they measure code-generation outcomes before and after an explicit questioning phase. [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Ambiguity reduction is the best-supported explanation for the gains, but it is not the only plausible explanation, because clarification sessions also add more interaction time, more user-provided examples, and more context tokens before generation starts. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices] The practical trade-off is therefore front-loaded questioning cost versus downstream debugging cost, which means Grill Me should have its highest Return on Investment on ambiguous, multi-step, or high-consequence changes rather than on tiny, already-explicit tasks. [inference; source: https://www.aihero.dev/5-agent-skills-i-use-every-day; https://arxiv.org/abs/2302.06590; https://www.anthropic.com/engineering/claude-code-best-practices]

**Risks, gaps, uncertainties:**

- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The direct clarification studies are controlled or benchmark-oriented, not longitudinal production studies.
- [fact; source: https://openreview.net/forum?id=s566pj5E5M] ClariGen evidence is currently accessible as an abstract and project summary rather than a fully reviewed camera-ready paper in this session.
- [inference; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock's question-count examples are informative but may reflect his teaching style and chosen examples rather than a stable industry median.
- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] No accessible study isolates total wall-clock feature delivery for grill-first versus prompt-to-code across a full project lifecycle.

**Open questions:**

- What is the smallest set of question categories that captures most of Grill Me's alignment benefit without making the session feel slow?
- Can automated instrumentation measure whether grill-first sessions reduce later code review comments, bug-fix churn, or failed test iterations in real repositories?
- Does the benefit curve flatten after a certain number of questions, or does value depend mainly on surfacing a small number of high-impact hidden constraints?
- Which parts of Grill Me can be automated from repository context without losing the human alignment benefit?

### §7 Recursive Review

- [fact; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://ml4code.github.io/publications/vaithilingam2022expectation/] Every substantive claim in this item is either bound to a public URL or labelled as an inference or assumption.
- [fact; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://www.aihero.dev/5-agent-skills-i-use-every-day] The synthesis keeps the analogy to requirements discovery at inference level and does not overstate it as a direct controlled equivalence.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590] Confidence remains medium overall because the key mechanism is directly supported, but full lifecycle and field-transfer evidence remains incomplete.

---

## Findings

### Executive Summary

Grill Me is an effective alignment technique when the task is ambiguous because it turns more of the user's hidden intent into explicit pre-code constraints before generation begins. [inference; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The strongest direct evidence comes from clarification-before-code research, which shows measurable gains in first-pass correctness and reliability when models ask targeted questions before writing code. [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Baseline Copilot studies explain why that helps in practice: direct generation is often fast and locally useful, but developers still lose time when they must understand, edit, and debug code generated from incomplete requirements. [inference; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf; https://arxiv.org/abs/2302.06590] The remaining uncertainty is which ingredient matters most, because current studies do not cleanly separate ambiguity reduction from extra interaction time, richer examples, or longer context accumulation, and they do not yet show the full-project wall-clock effect in production. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices]

### Key Findings

1. **Matt Pocock's Grill Me technique is a concrete clarification-first workflow in which the agent asks one question at a time, walks the design tree branch by branch, recommends answers, and stops only when shared understanding has been reached.** ([fact]; medium confidence; source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral)
2. **Direct code-generation research shows that adding a targeted clarifying-question phase before code generation materially improves first-pass correctness on underspecified tasks, including a GPT-4 benchmark correctness increase from 70.96% to 80.80% in ClarifyGPT.** ([fact]; medium confidence; source: https://arxiv.org/abs/2310.10996)
3. **A second clarification-before-code study, ClariGen, reports that high-quality clarifications improve code correctness and reliability while reducing later revision needs, which supports the same mechanism through a separate research program but currently with thinner evidence than ClarifyGPT.** ([fact]; low confidence; source: https://openreview.net/forum?id=s566pj5E5M)
4. **Baseline Copilot usability evidence shows why Grill Me matters: users often prefer generated code as a starting point, but still lose effectiveness when they must understand, edit, and debug output produced from incomplete or mismatched requirements.** ([fact]; high confidence; source: https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf)
5. **The strongest software-engineering analogue for Grill Me is requirements discovery rather than prompt optimization, because Three Amigos workshops use concrete examples, edge cases, technical constraints, and testability questions to surface hidden assumptions before implementation begins.** ([inference]; medium confidence; source: https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)
6. **Pocock's public examples report Grill Me sessions ranging from 16 questions on a smaller feature to roughly 30 to 50 questions on more complex changes, and he says these conversations often last about 45 minutes, which suggests the practice is a real discovery phase rather than a one-line prompt enhancement.** ([inference]; medium confidence; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day)
7. **Compared with jumping directly to code, Grill Me is best supported as a way to improve first-output correctness and reduce correction rounds under ambiguity, but direct evidence that it always shortens total time-to-working-feature is still missing.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
8. **The available evidence suggests Grill Me is likely transferable across models and stacks because clarification gains appear in multi-model studies and the same explore-then-plan guidance appears in both Anthropic and GitHub workflow recommendations, but industrial cross-language head-to-head data remains thin.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Grill Me is a one-question-at-a-time design interview that resolves dependencies until shared understanding. | https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://www.aihero.dev/my-grill-me-skill-has-gone-viral | medium | Direct Pocock mechanism |
| [fact] ClarifyGPT raises first-pass correctness by adding clarifying questions before code generation. | https://arxiv.org/abs/2310.10996 | medium | Measured benchmark gain |
| [fact] ClariGen reports correctness, reliability, and revision benefits from interactive clarification. | https://openreview.net/forum?id=s566pj5E5M | low | Abstract-level evidence |
| [fact] Prompt-to-code remains attractive but creates comprehension and debugging burden when intent is incomplete. | https://ml4code.github.io/publications/vaithilingam2022expectation/; https://sarahnadi.org/assets/pdf/pubs/NguyenMSR22.pdf | high | Baseline misalignment evidence |
| [inference] Grill Me maps most closely to requirements-discovery practices such as Three Amigos. | https://johnfergusonsmart.com/three-amigos-requirements-discovery/; https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html | medium | Mechanism match |
| [inference] Pocock's public examples suggest 16 to 50 questions and sessions that often last about 45 minutes on non-trivial work. | https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day | medium | Pocock-reported examples |
| [inference] The clearest proven advantage is better first-output correctness, not guaranteed lower total cycle time. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Lifecycle gap remains |
| [inference] Transferability is plausible across models because ambiguity reduction and context scoping are model-agnostic mechanisms. | https://arxiv.org/abs/2310.10996; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/ | medium | Multi-model plus workflow guidance |

### Assumptions

- [assumption] The current Pocock first-party sources are an acceptable substitute for the dead Total TypeScript seed URL because they describe the same technique in current public form.
- [assumption] The absence of an accessible long-run randomized field study means project-length benefits must be inferred from benchmark studies, usability studies, and requirements-discovery analogues rather than asserted directly.

### Analysis

The evidence supports Grill Me most strongly as an ambiguity-management workflow rather than as a universal speed hack. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://arxiv.org/abs/2302.06590] Direct clarification studies carry the core causal weight because they measure code-generation outcomes before and after an explicit questioning phase. [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Ambiguity reduction is the best-supported explanation for the gains, but it is not the only plausible explanation, because clarification sessions also add more interaction time, more user-provided examples, and more context tokens before generation starts. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices] The practical trade-off is therefore front-loaded questioning cost versus downstream debugging cost, which means Grill Me should have its highest Return on Investment on ambiguous, multi-step, or high-consequence changes rather than on tiny, already-explicit tasks. [inference; source: https://www.aihero.dev/5-agent-skills-i-use-every-day; https://arxiv.org/abs/2302.06590; https://www.anthropic.com/engineering/claude-code-best-practices]

### Risks, Gaps, and Uncertainties

- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The direct clarification studies are controlled or benchmark-oriented, not longitudinal production studies.
- [fact; source: https://openreview.net/forum?id=s566pj5E5M] ClariGen evidence is currently accessible as an abstract and project summary rather than a fully reviewed camera-ready paper in this session.
- [inference; source: https://www.aihero.dev/my-grill-me-skill-has-gone-viral; https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock's question-count examples are informative but may reflect his teaching style and chosen examples rather than a stable industry median.
- [inference; source: https://arxiv.org/abs/2302.06590; https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/] No accessible study isolates total wall-clock feature delivery for grill-first versus prompt-to-code across a full project lifecycle.

### Open Questions

- What is the smallest set of question categories that captures most of Grill Me's alignment benefit without making the session feel slow?
- Can automated instrumentation measure whether grill-first sessions reduce later code review comments, bug-fix churn, or failed test iterations in real repositories?
- Does the benefit curve flatten after a certain number of questions, or does value depend mainly on surfacing a small number of high-impact hidden constraints?
- Which parts of Grill Me can be automated from repository context without losing the human alignment benefit?

---

## Output

- Type: knowledge
- Description: Evidence-backed synthesis showing that clarification-first interviewing improves alignment mainly by converting ambiguous intent into explicit pre-code constraints, with strongest support on first-pass correctness and revision reduction rather than proven end-to-end speed gains.
- Links:
  - https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md
  - https://arxiv.org/abs/2310.10996
  - https://openreview.net/forum?id=s566pj5E5M
