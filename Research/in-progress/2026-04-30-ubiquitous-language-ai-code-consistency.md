---
review_count: 1
title: "Ubiquitous Language in Artificial Intelligence (AI)-augmented development: domain glossaries, naming consistency, and long-term codebase coherence"
added: 2026-04-30T20:31:45+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]
tags: [agentic-coding, software-engineering, llm, agentic-ai, workflow]
started: 2026-05-01T07:55:42+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-03-16-intent-driven-development, 2026-03-22-applied-context-engineering-agent-workflows, 2026-04-30-deep-modules-ai-augmented-codebases, 2026-04-30-fundamentals-first-vs-specs-to-code]
related: [2026-04-30-grill-me-ai-alignment-shared-design, 2026-04-30-ai-code-entropy-quality-metrics, 2026-04-30-strategic-tactical-division-ai-teams, 2026-04-30-tdd-feedback-loops-ai-augmented-dev, 2026-04-30-se-fundamentals-ai-code-synthesis]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Ubiquitous Language in Artificial Intelligence (AI)-augmented development: domain glossaries, naming consistency, and long-term codebase coherence

## Research Question

How significantly does maintaining a living Ubiquitous Language (UL), in the Domain-Driven Design (DDD) sense of a shared, precise domain vocabulary used consistently in both code and conversation, improve the precision and consistency of Artificial Intelligence (AI)-generated code, reduce AI verbosity, and prevent naming drift across a growing codebase over time?

## Scope

**In scope:**
- Ubiquitous Language as defined in Evans's *Domain-Driven Design*: a shared vocabulary developed with domain experts and used consistently in code, tests, documentation, and conversation, and its role in reducing ambiguity and translation overhead
- AI verbosity and precision: empirical or practitioner evidence that AI assistants produce more concise, on-target code when given an explicit domain glossary versus when they must infer terminology from context
- Naming consistency and drift: how quickly naming inconsistencies accumulate in AI-generated codebases and the cost of synonym proliferation, for example `user` versus `customer` versus `account_holder` for the same domain concept
- Living glossary maintenance: how to construct, version, and provide a domain glossary to AI assistants as part of system prompt or context injection, and evidence on the impact of glossary quality on output consistency
- The Matt Pocock "Ubiquitous Language" skill: description, mechanics, and practitioner evidence
- Cross-session consistency: whether AI assistants without persistent memory maintain naming conventions across sessions if given an explicit glossary versus if they must infer from file context alone

**Out of scope:**
- Full treatment of Domain-Driven Design (DDD) tactical patterns, such as aggregates, repositories, and bounded contexts, except where they directly affect naming conventions
- AI memory systems and long-term context persistence as a standalone architectural problem
- Grill Me alignment technique, covered in `2026-04-30-grill-me-ai-alignment-shared-design`

**Constraints:**
- Sources from 2022 onwards are preferred for AI-specific evidence, while Evans (2003) and later DDD reference material are acceptable as theoretical anchors
- Practitioner evidence from blog posts, talks, or skills frameworks is acceptable if attributed and traceable

## Context

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/] Ubiquitous Language is a shared, rigorous domain vocabulary used across conversation, code, and documentation so that developers and domain experts stop translating between competing names for the same concept.
- [fact; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] Code-generation models are sensitive to wording and prompt variation, with real-world perturbations degrading performance and user-background differences changing generated code quality.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Current agent workflow guidance treats persistent repository instruction files, memory artifacts, and precise language as first-order controls because agents do not preserve perfect cross-session context on their own.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html] A living domain glossary is therefore plausibly an AI-readiness artifact: it narrows the solution space before generation, stabilizes naming after generation, and does so with far lower context cost than repeatedly restating terminology in free-form prose.

## Approach

1. **Define Ubiquitous Language in the AI context** - Summarize the DDD definition and practical mechanics of Ubiquitous Language, then translate it into an AI-assisted workflow artifact.
2. **Survey AI vocabulary sensitivity** - Review empirical studies and systematic practitioner evidence on how terminology, prompt wording, and clarification affect AI code generation quality.
3. **Examine the Matt Pocock Ubiquitous Language skill** - Locate the canonical public description of the skill, extract its mechanics, and assess the practitioner rationale behind it.
4. **Assess naming drift risk** - Look for direct evidence on naming inconsistency in AI-generated codebases; if direct measures are absent, document the risk as an inference with supporting logic.
5. **Assess cross-session consistency** - Determine whether reusable instruction artifacts and glossary files plausibly improve consistency across stateless or semi-stateless AI sessions.
6. **Synthesize** - Produce a structured assessment of whether living Ubiquitous Language maintenance is a high-return practice in AI-augmented teams, what a minimum viable glossary looks like, and how it should be maintained.

## Sources

- [x] [Evans (2015) Domain-Driven Design Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- [x] [Fowler (2006) Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)
- [x] [Open Practice Library Ubiquitous Language](https://openpracticelibrary.com/practice/ubiquitous-language/)
- [x] [Pocock (2025) Ubiquitous Language skill](https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md)
- [x] [Pocock (2025) Deprecated skills README](https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md)
- [x] [Pocock (2025) 5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day)
- [x] [White et al. (2023) Prompt Pattern Catalog](https://arxiv.org/abs/2302.11382)
- [x] [Liang et al. (2023) Practices and Challenges of Using GitHub Copilot: An Empirical Study](https://arxiv.org/abs/2303.08733)
- [x] [Wang et al. (2023) Clarification-before-code framework](https://arxiv.org/abs/2310.10996)
- [x] [Chen et al. (2024) NLPerturbator prompt-robustness study](https://arxiv.org/abs/2406.19783)
- [x] [Paleyes et al. (2025) Code Roulette prompt-variability study](https://arxiv.org/abs/2506.10204)
- [x] [Miao et al. (2025) ClariGen: Bridging Instruction Gaps via Interactive Clarification in Code Generation](https://openreview.net/forum?id=s566pj5E5M)
- [x] [Anthropic (2025) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [GitHub Blog (2025) How to build reliable AI workflows with agentic primitives and context engineering](https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)

## Related

- [Deep modules in AI-augmented development](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [Fundamentals-first versus specs-to-code](https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html)
- [Applied context engineering: skills, workflows, and best practices for agent development](https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html)
- [Intent Driven Development: context and concept layering to bound the solution space](https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://arxiv.org/abs/2406.19783] Research question restated: does maintaining a living Ubiquitous Language (UL) artifact materially improve the precision and consistency of Artificial Intelligence (AI)-generated code, and is the benefit large enough to justify glossary maintenance overhead?
- [fact; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices] Scope confirmed: this item covers DDD naming discipline, AI prompt sensitivity, Matt Pocock's public UL mechanics, cross-session glossary injection, and the risk of naming drift, while treating direct longitudinal naming-drift measurements as likely sparse.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://www.anthropic.com/engineering/claude-code-best-practices; https://arxiv.org/abs/2302.11382] Output format confirmed: structured knowledge note with explicit findings on glossary mechanics, prompt sensitivity, cross-session consistency, evidence quality, and uncertainty.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] Prior completed repository work already sharpens this item in four ways: explicit interfaces and bounded context improve AI navigation, structured workflows outperform prompt-only execution on maintained projects, context artifacts must stay short and reusable, and layered intent artifacts are more reliable than asking agents to infer meaning from vague requests.

### §1 Question Decomposition

- **Root question:** Does a maintained domain glossary make AI-generated code more precise and consistent over time, and what evidence supports that claim?
- **A. DDD foundation**
  - A1. What does Ubiquitous Language mean in DDD?
  - A2. What makes it a living glossary rather than a one-off naming exercise?
  - A3. What minimum fields must the artifact contain to be useful?
- **B. AI prompt sensitivity**
  - B1. How sensitive is code generation quality to wording and prompt variation?
  - B2. What evidence shows that clarifying or enriching requirements improves correctness?
  - B3. What parts of that evidence transfer to domain glossary use?
- **C. Pocock workflow**
  - C1. What exactly does Matt Pocock's Ubiquitous Language skill instruct the agent to do?
  - C2. Is the skill evidence of a reusable AI workflow artifact or only a naming idea?
- **D. Cross-session consistency and drift**
  - D1. What current agent guidance says reusable instruction artifacts matter across sessions?
  - D2. Is there direct evidence measuring naming drift in AI-generated repositories?
  - D3. If direct drift evidence is absent, what is the strongest defensible inference?
- **E. Synthesis**
  - E1. What benefits are directly evidenced?
  - E2. Which claims remain inferred, especially around verbosity reduction and long-run drift prevention?
  - E3. What is the minimum viable glossary and where is its likely return highest?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded O'Reilly landing pages for Evans and Vernon were not useful for inspectable content in this session, so the accessible Evans reference PDF, Martin Fowler summary, and Open Practice Library guide were used instead. Justification: those replacement sources expose the relevant Ubiquitous Language definitions and maintenance mechanics in readable form.
- [assumption] Access note: the seeded Total TypeScript page `https://www.totaltypescript.com/ai-coding-assistants` no longer resolves, so current first-party Matt Pocock sources were substituted with the public GitHub skill file, the deprecated-skills README, and the AI Hero workflow article. Justification: those sources are first-party and directly describe the glossary mechanic or the surrounding rationale for strict reusable skills.
- [assumption] Access note: the seeded arXiv identifier `https://arxiv.org/abs/2112.00114` resolves to a scratchpad reasoning paper rather than the claimed Zhao et al. code-generation prompting study, so it was treated as a mismatched seed and replaced with directly relevant prompt-robustness studies on code generation. Justification: the replacement sources measure wording sensitivity on code-generation tasks rather than unrelated reasoning behavior.
- [assumption] Access note: the seeded arXiv identifier `https://arxiv.org/abs/2307.10680` resolves to a recommender-system knowledge-graph paper rather than the claimed code-generation consistency study, so it was replaced with accessible prompt-variability and workflow-consistency sources. Justification: the replacement sources are on-topic for code-generation consistency and session-level guidance.
- [assumption] Failed primary-source search note: searches including `"Trebing consistency code generation"`, `"naming drift llm code generation repository study"`, and `"synonym proliferation AI-generated codebase"` did not surface an accessible longitudinal study that directly measures naming-drift rates in AI-generated repositories. Justification: the accessible literature clusters around prompt robustness, clarification, and workflow guidance rather than repository-level glossary experiments.

#### A. DDD foundation and living glossary mechanics

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html] Fowler defines Ubiquitous Language as a common, rigorous language between developers and users, based on the domain model used in the software, because software does not cope well with ambiguity.
- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html] Fowler's Evans-backed summary also says the language should be exercised in conversations with domain experts and should evolve as the team's understanding of the domain grows.
- [fact; source: https://openpracticelibrary.com/practice/ubiquitous-language/] Open Practice Library describes Ubiquitous Language as a canonical, rigorous, and unambiguous language shared by everyone involved in software development, not only developers.
- [fact; source: https://openpracticelibrary.com/practice/ubiquitous-language/] Open Practice Library recommends that the output of the practice be a glossary of terms, concepts, and definitions that is visible to everyone and versionable in a git repository so changes can be tracked and reviewed.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Pocock's public Ubiquitous Language skill tells the agent to scan the current conversation for domain-relevant nouns, verbs, and concepts, identify ambiguity and synonym conflicts, propose canonical terms, and write a glossary file with definitions, aliases to avoid, relationships, example dialogue, and flagged ambiguities.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md] The same skills repository labels the artifact as a DDD-style ubiquitous language glossary extracted from the current conversation, which makes the DDD lineage explicit rather than implied.
- [inference; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] A minimum viable AI glossary therefore needs four things at minimum: one canonical term per domain concept, a tight definition, aliases to avoid, and a small set of relationship notes that prevent near-synonyms from collapsing into each other.

#### B. AI vocabulary sensitivity and prompt precision

- [fact; source: https://arxiv.org/abs/2302.11382] White et al. describe prompt patterns as reusable solutions to common prompting problems and explicitly argue that multiple prompt patterns can be combined to improve the outputs of Large Language Model (LLM) conversations.
- [fact; source: https://arxiv.org/abs/2406.19783] Chen et al. study 18 categories of real-world natural-language perturbations for code generation and report that perturbed prompts can reduce performance by as much as 21.2%, with average drops between 4.8% and 6.1% across evaluated models.
- [fact; source: https://arxiv.org/abs/2506.10204] Paleyes et al. state that functionality and quality of generated code can be sensitive to user background and familiarity with software development, and propose an evaluation pipeline specifically to measure sensitivity to prompt augmentations.
- [fact; source: https://arxiv.org/abs/2310.10996] Wang et al.'s clarification-before-code framework reports that adding a clarifying-question phase before code generation raised Generative Pre-trained Transformer 4 (GPT-4) Pass@1 on Mostly Basic Python Problems (MBPP)-sanitized from 70.96% to 80.80% and improved average benchmark performance across four benchmarks from 68.02% to 75.75%.
- [fact; source: https://openreview.net/forum?id=s566pj5E5M] ClariGen reports that a clarifying question-and-answer phase before code generation improves contextual accuracy and reliability while reducing the need for later revisions.
- [fact; source: https://arxiv.org/abs/2303.08733] Liang et al. report that Copilot is a double-edged sword and identify difficulty of integration as the main practitioner limitation in their dataset.
- [inference; source: https://arxiv.org/abs/2303.08733; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] That integration finding is directionally consistent with terminology risk, but Liang et al. do not isolate inconsistent naming as the specific causal mechanism behind the reported integration burden.
- [inference; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The best-supported AI mechanism is therefore ambiguity sensitivity: if small changes in wording and requirement clarification change code correctness, then domain vocabulary is likely to matter whenever domain terms carry part of the task specification.

#### C. Matt Pocock's Ubiquitous Language skill as an AI workflow artifact

- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Pocock's skill is not just a naming checklist; it prescribes a concrete output file, `UBIQUITOUS_LANGUAGE.md`, with grouped glossary tables, relationships, example dialogue, and explicit ambiguity flags.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] The skill is opinionated, because it instructs the agent to choose the best canonical term when multiple words exist for the same concept and to mark the alternatives as aliases to avoid.
- [fact; source: https://www.aihero.dev/5-agent-skills-i-use-every-day] Pocock's general workflow guidance says agents have no memory and therefore need extremely strict, well-defined processes encoded as reusable skills, which is the surrounding rationale for externalizing important context instead of trusting session memory.
- [inference; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://www.aihero.dev/5-agent-skills-i-use-every-day] In AI-assisted development, the UL skill functions as a memory-compensation artifact: it moves fragile conversational terminology into a stable file that future sessions can load instead of rediscovering term boundaries from scratch.
- [inference; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://openpracticelibrary.com/practice/ubiquitous-language/] The skill's emphasis on aliases to avoid is especially relevant to AI because synonym collisions, such as `customer`, `user`, and `account`, are exactly the kind of lexical ambiguity that prompt-sensitive models can interpret as materially different tasks.

#### D. Cross-session consistency, naming drift, and context artifacts

- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices] Anthropic says the context window fills quickly, performance degrades as it fills, and CLAUDE.md is read at the start of every conversation to provide persistent workflow and architecture guidance that the model cannot reliably infer from code alone.
- [fact; source: https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] GitHub's context-engineering guidance recommends instructions files, specification files, memory files, and context helper files so agents get the right information rather than simply more information, and frames precise language as a way to eliminate ambiguity.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html] The repository's applied context-engineering synthesis argues that reliable agent work depends on compact, reusable context artifacts because effective context capacity is materially below the advertised token window.
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html] These workflow sources jointly imply that a short glossary file is a plausible cross-session control surface for naming consistency, because it is compact enough to load repeatedly and specific enough to override noisy local file context.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html] Naming drift is best understood as an upstream alignment problem rather than a downstream formatting problem, because changing the names of concepts changes the boundaries of the solution space that agents and humans think they are working inside.
- [assumption] No accessible longitudinal study directly measures synonym proliferation or naming-drift rate in AI-generated codebases over months of repository growth. Justification: the accessible evidence base contains prompt-variation studies, clarification studies, and workflow guidance, but no repository-scale glossary intervention study.

### §3 Reasoning

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/] DDD sources directly support the claim that Ubiquitous Language reduces ambiguity by creating a shared evolving vocabulary and a visible glossary.
- [fact; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] AI-specific studies directly support the claim that wording quality, prompt perturbation, and clarification affect code-generation correctness and reliability.
- [fact; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Current workflow guidance directly supports the claim that persistent, reusable context artifacts are part of reliable cross-session agent work.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] A competing explanation remains live: some observed gains may come from any structured clarification phase or persistent context artifact rather than from glossary-specific vocabulary control.
- [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices] The synthesis claim is therefore mechanism-level rather than experiment-level: a living glossary should help because it reduces lexical ambiguity before generation and gives later sessions a stable naming reference.
- [inference; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices] Claims about reduced verbosity and direct long-run drift prevention remain weaker than claims about improved precision, because those effects are inferred from prompt sensitivity and context-budget logic rather than directly measured.

### §4 Consistency Check

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] The DDD and Pocock sources are internally consistent on the core mechanic: choose canonical terms, surface ambiguity, and use the vocabulary everywhere.
- [fact; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] The AI studies are internally consistent on ambiguity sensitivity, but they do not directly test glossary files, so any claim stronger than mechanism transfer would be unsupported.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Pocock's UL skill sits in the repository's deprecated section, so it is evidence of a real published mechanic, not proof that it remains his flagship recommendation today.
- [fact; source: https://arxiv.org/abs/2112.00114; https://arxiv.org/abs/2307.10680; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] The mismatched seeded academic URLs were replaced with on-topic prompt-variation papers, which removes a source-identity contradiction from the evidence base.

### §5 Depth and Breadth Expansion

- [inference; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Technical lens: a glossary converts hidden lexical assumptions into an explicit artifact, which should reduce alias collisions before they spread into class names, test names, and prompt phrasing.
- [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Economic lens: a short glossary has low token cost and low maintenance cost relative to repeated renaming, reviewer confusion, and repeated re-explanation across sessions.
- [inference; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html] Behavioral lens: the practice should help humans as much as models because explicit aliases-to-avoid make wrong term choices easy to spot in review rather than silently accepted as "close enough."
- [inference; source: https://davidamitchell.github.io/Research/research/2026-03-16-intent-driven-development.html; https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html] Organizational lens: glossary discipline becomes more valuable as projects become multi-session, multi-contributor, and multi-artifact, because the same term boundaries must survive across plans, code, tests, and architectural seams.

### §6 Synthesis

**Executive summary:**

Living Ubiquitous Language (UL) maintenance is very likely to improve the precision and naming consistency of Artificial Intelligence (AI)-generated code, but current public evidence supports that conclusion mainly through mechanism-level studies on ambiguity sensitivity rather than through glossary-only trials. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] The strongest direct evidence is that code-generation quality changes materially when wording changes or when models ask clarifying questions before writing code, which means terminology is part of the causal input rather than incidental phrasing. [fact; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Matt Pocock's public UL skill shows one concrete way to operationalize that insight: externalize canonical terms, aliases to avoid, and domain relationships into a reusable glossary file that future sessions can reload. [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md] The remaining uncertainty is about magnitude, because direct measures of reduced verbosity, reduced rename churn, or slower naming drift over long repository lifecycles are not yet accessible in the public literature reviewed here. [inference; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices]

**Key findings:**

1. **Domain-Driven Design sources define Ubiquitous Language as a shared, rigorous vocabulary used in conversations, code, and evolving domain models, so the practice is fundamentally about ambiguity reduction rather than stylistic naming preference.** ([fact]; high confidence; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/)
2. **Open Practice Library and Matt Pocock's public skill both operationalize Ubiquitous Language as a maintained glossary artifact with canonical terms, definitions, aliases to avoid, and visible review, which provides a concrete artifact model rather than only an abstract naming principle.** ([fact]; medium confidence; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md)
3. **Code-generation studies show that modest changes to natural-language problem statements can materially change correctness, with NLPerturbator reporting up to a 21.2% performance drop under real-world prompt variations and Code Roulette showing sensitivity to user background and prompt augmentations.** ([fact]; high confidence; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204)
4. **Clarification-before-code studies show that making requirements linguistically richer before generation improves output quality, including Wang et al.'s reported increase from 70.96% to 80.80% Pass@1 on Mostly Basic Python Problems (MBPP)-sanitized tasks, which supports the same ambiguity-reduction mechanism that a domain glossary is meant to provide.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M)
5. **Current agent workflow guidance from Anthropic and GitHub recommends persistent repository instruction files, specification files, memory files, and precise language, which means a short glossary file fits the dominant cross-session control pattern for keeping agents focused on the right terms.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html)
6. **Matt Pocock's deprecated but still public Ubiquitous Language skill makes the AI-specific mechanics explicit: scan conversations for domain nouns and verbs, flag synonyms and overloaded terms, choose canonical vocabulary, and externalize the result into a reusable glossary file.** ([fact]; medium confidence; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md)
7. **The glossary-specific benefit is most defensible when the failure mode is domain-term ambiguity, because current evidence does not show that glossary files outperform any other persistent structured context artifact on tasks whose terminology is already settled.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
8. **The accessible evidence base supports living Ubiquitous Language as a medium-to-high-return practice for long-lived, domain-heavy codebases, but it does not yet justify a universal multiplier because direct glossary-versus-no-glossary longitudinal repository experiments remain missing and some benefit may come from structured context more generally.** ([inference]; medium confidence; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://arxiv.org/abs/2310.10996)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Ubiquitous Language is a shared rigorous vocabulary used across conversation, code, and evolving domain models. | https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/ | high | DDD foundation |
| [fact] Ubiquitous Language can be operationalized as a maintained glossary artifact with canonical terms and aliases to avoid. | https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md | medium | Concrete mechanics |
| [fact] Code generation quality is sensitive to real-world prompt wording changes and user-background variation. | https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204 | high | Direct sensitivity evidence |
| [inference] Clarification studies support the same ambiguity-reduction mechanism that a glossary is meant to provide. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M | medium | Mechanism transfer |
| [inference] A short glossary file fits the dominant cross-session context-control pattern in current agent workflows. | https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html | medium | Persistent artifact fit |
| [fact] Pocock's public UL skill explicitly tells the agent to extract canonical terms, flag ambiguities, and write a reusable glossary file. | https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md | medium | Practitioner artifact |
| [inference] Precision and naming consistency are better supported outcomes than quantified verbosity reduction. | https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html | medium | Outcome asymmetry |
| [inference] Living Ubiquitous Language appears highest-return on long-lived domain-heavy projects, but no universal multiplier is currently justified. | https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Return bounded by evidence gap |

**Assumptions:**

- [assumption] The current public Pocock GitHub skill is an acceptable substitute for the dead Total TypeScript seed URL because it exposes the same underlying glossary mechanic in first-party form. Justification: the skill file and repository README are first-party sources describing the glossary output directly.
- [assumption] The absence of a direct glossary intervention study means long-run naming-drift and verbosity claims must be inferred from prompt-sensitivity, clarification, and workflow-guidance evidence rather than asserted as measured facts. Justification: the accessible literature reviewed here measures wording sensitivity and clarification benefit, not glossary-specific repository outcomes.
- [assumption] Open Practice Library's recommendation to store the glossary in git generalizes to AI instruction ecosystems where glossary files are loaded as durable project context. Justification: current Anthropic and GitHub workflow guidance already treat small repository files as the normal way to preserve reusable agent context.

**Analysis:**

The evidence base is asymmetric: DDD sources directly justify why shared vocabulary matters, while AI-specific studies directly show that wording and clarification materially change code outcomes. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] A live competing explanation is that much of the observed gain may come from any structured clarification phase or persistent context artifact, not from glossary-specific vocabulary control by itself. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] The reason glossary discipline still looks valuable is that it is the smallest artifact in this evidence set that targets lexical ambiguity directly by fixing canonical terms, aliases to avoid, and relationships before those distinctions spread through code and conversation. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Anthropic and GitHub guidance also explain why the artifact must stay short and versioned, because persistent instruction files only work when they fit scarce context budget and remain easy to reload across sessions. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html] The likely economic pattern is therefore high leverage on long-lived domains with repeated feature work and lower leverage on disposable or one-off tasks, where glossary maintenance would not have time to amortize. [inference; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html]

**Risks, gaps, uncertainties:**

- [assumption] The accessible literature clusters around prompt robustness, clarification, and workflow guidance rather than glossary-only experiments, so the direct empirical base for naming-drift prevention remains thin. Justification: the consulted accessible sources on code generation focus on prompt perturbation, clarifying questions, and persistent context artifacts.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Pocock's UL skill is published in the deprecated section of his repository, so it is evidence of a real mechanic but not proof that it remains a current flagship workflow component.
- [fact; source: https://arxiv.org/abs/2112.00114; https://arxiv.org/abs/2307.10680] Two seeded academic URLs resolved to unrelated papers rather than the claimed code-generation studies, which reduced the amount of directly reusable seed evidence and required source substitution.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Clarification studies measure better-specified task prompts, not long-running repository naming governance, so their support for glossary maintenance is mechanistic rather than direct.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Some of the observed benefit may come from generic structured context and clarification rather than from vocabulary control specifically, so the glossary-specific uplift should be treated as incremental rather than isolated.

**Open questions:**

- What is the smallest glossary structure that captures most of the precision benefit without adding enough maintenance burden to be ignored?
- Can repository instrumentation measure naming drift directly, for example by tracking synonym introduction, rename churn, or reviewer comments on domain terminology?
- Should glossary enforcement happen only through context loading, or should linters, code review templates, and architecture checks also reject aliases-to-avoid?
- Can an agent safely propose glossary updates from repository changes without creating circular drift in the glossary itself?

### §7 Recursive Review

- [fact; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices] Every substantive external claim retained in this item is bound to a public URL or explicitly labelled as an inference or assumption.
- [fact; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Confidence remains medium overall because the mechanism is well-supported, but direct glossary-only and longitudinal naming-drift evidence remains incomplete.
- [fact; source: https://arxiv.org/abs/2112.00114; https://arxiv.org/abs/2307.10680; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] Seed-source mismatch checks, acronym expansion checks, and synthesis-to-findings parity checks were completed with only accessible, on-topic sources left in the retained evidence chain.

---

## Findings

### Executive Summary

Living Ubiquitous Language (UL) maintenance is very likely to improve the precision and naming consistency of Artificial Intelligence (AI)-generated code, but current public evidence supports that conclusion mainly through mechanism-level studies on ambiguity sensitivity rather than through glossary-only trials. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204] The strongest direct evidence is that code-generation quality changes materially when wording changes or when models ask clarifying questions before writing code, which means terminology is part of the causal input rather than incidental phrasing. [fact; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Matt Pocock's public UL skill shows one concrete way to operationalize that insight: externalize canonical terms, aliases to avoid, and domain relationships into a reusable glossary file that future sessions can reload. [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md] The remaining uncertainty is about magnitude, because direct measures of reduced verbosity, reduced rename churn, or slower naming drift over long repository lifecycles are not yet accessible in the public literature reviewed here. [inference; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices]

### Key Findings

1. **Domain-Driven Design sources define Ubiquitous Language as a shared, rigorous vocabulary used in conversations, code, and evolving domain models, so the practice is fundamentally about ambiguity reduction rather than stylistic naming preference.** ([fact]; high confidence; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/)
2. **Open Practice Library and Matt Pocock's public skill both operationalize Ubiquitous Language as a maintained glossary artifact with canonical terms, definitions, aliases to avoid, and visible review, which provides a concrete artifact model rather than only an abstract naming principle.** ([fact]; medium confidence; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md)
3. **Code-generation studies show that modest changes to natural-language problem statements can materially change correctness, with NLPerturbator reporting up to a 21.2% performance drop under real-world prompt variations and Code Roulette showing sensitivity to user background and prompt augmentations.** ([fact]; high confidence; source: https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204)
4. **Clarification-before-code studies show that making requirements linguistically richer before generation improves output quality, including Wang et al.'s reported increase from 70.96% to 80.80% Pass@1 on Mostly Basic Python Problems (MBPP)-sanitized tasks, which supports the same ambiguity-reduction mechanism that a domain glossary is meant to provide.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M)
5. **Current agent workflow guidance from Anthropic and GitHub recommends persistent repository instruction files, specification files, memory files, and precise language, which means a short glossary file fits the dominant cross-session control pattern for keeping agents focused on the right terms.** ([inference]; medium confidence; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html)
6. **Matt Pocock's deprecated but still public Ubiquitous Language skill makes the AI-specific mechanics explicit: scan conversations for domain nouns and verbs, flag synonyms and overloaded terms, choose canonical vocabulary, and externalize the result into a reusable glossary file.** ([fact]; medium confidence; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md)
7. **The glossary-specific benefit is most defensible when the failure mode is domain-term ambiguity, because current evidence does not show that glossary files outperform any other persistent structured context artifact on tasks whose terminology is already settled.** ([inference]; medium confidence; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/)
8. **The accessible evidence base supports living Ubiquitous Language as a medium-to-high-return practice for long-lived, domain-heavy codebases, but it does not yet justify a universal multiplier because direct glossary-versus-no-glossary longitudinal repository experiments remain missing and some benefit may come from structured context more generally.** ([inference]; medium confidence; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html; https://arxiv.org/abs/2310.10996)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Ubiquitous Language is a shared rigorous vocabulary used across conversation, code, and evolving domain models. | https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/ | high | DDD foundation |
| [fact] Ubiquitous Language can be operationalized as a maintained glossary artifact with canonical terms and aliases to avoid. | https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md | medium | Concrete mechanics |
| [fact] Code generation quality is sensitive to real-world prompt wording changes and user-background variation. | https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204 | high | Direct sensitivity evidence |
| [inference] Clarification studies support the same ambiguity-reduction mechanism that a glossary is meant to provide. | https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M | medium | Mechanism transfer |
| [inference] A short glossary file fits the dominant cross-session context-control pattern in current agent workflows. | https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html | medium | Persistent artifact fit |
| [fact] Pocock's public UL skill explicitly tells the agent to extract canonical terms, flag ambiguities, and write a reusable glossary file. | https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md | medium | Practitioner artifact |
| [inference] Precision and naming consistency are better supported outcomes than quantified verbosity reduction. | https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://www.anthropic.com/engineering/claude-code-best-practices; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html | medium | Outcome asymmetry |
| [inference] Living Ubiquitous Language appears highest-return on long-lived domain-heavy projects, but no universal multiplier is currently justified. | https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html | medium | Return bounded by evidence gap |

### Assumptions

- [assumption] The current public Pocock GitHub skill is an acceptable substitute for the dead Total TypeScript seed URL because it exposes the same underlying glossary mechanic in first-party form. Justification: the skill file and repository README are first-party sources describing the glossary output directly.
- [assumption] The absence of a direct glossary intervention study means long-run naming-drift and verbosity claims must be inferred from prompt-sensitivity, clarification, and workflow-guidance evidence rather than asserted as measured facts. Justification: the accessible literature reviewed here measures wording sensitivity and clarification benefit, not glossary-specific repository outcomes.
- [assumption] Open Practice Library's recommendation to store the glossary in git generalizes to AI instruction ecosystems where glossary files are loaded as durable project context. Justification: current Anthropic and GitHub workflow guidance already treat small repository files as the normal way to preserve reusable agent context.

### Analysis

The evidence base is asymmetric: DDD sources directly justify why shared vocabulary matters, while AI-specific studies directly show that wording and clarification materially change code outcomes. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://arxiv.org/abs/2406.19783; https://arxiv.org/abs/2506.10204; https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] A live competing explanation is that much of the observed gain may come from any structured clarification phase or persistent context artifact, not from glossary-specific vocabulary control by itself. [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] The reason glossary discipline still looks valuable is that it is the smallest artifact in this evidence set that targets lexical ambiguity directly by fixing canonical terms, aliases to avoid, and relationships before those distinctions spread through code and conversation. [inference; source: https://martinfowler.com/bliki/UbiquitousLanguage.html; https://openpracticelibrary.com/practice/ubiquitous-language/; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Anthropic and GitHub guidance also explain why the artifact must stay short and versioned, because persistent instruction files only work when they fit scarce context budget and remain easy to reload across sessions. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-03-22-applied-context-engineering-agent-workflows.html] The likely economic pattern is therefore high leverage on long-lived domains with repeated feature work and lower leverage on disposable or one-off tasks, where glossary maintenance would not have time to amortize. [inference; source: https://openpracticelibrary.com/practice/ubiquitous-language/; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/; https://davidamitchell.github.io/Research/research/2026-04-30-fundamentals-first-vs-specs-to-code.html]

### Risks, Gaps, and Uncertainties

- [assumption] The accessible literature clusters around prompt robustness, clarification, and workflow guidance rather than glossary-only experiments, so the direct empirical base for naming-drift prevention remains thin. Justification: the consulted accessible sources on code generation focus on prompt perturbation, clarifying questions, and persistent context artifacts.
- [fact; source: https://github.com/mattpocock/skills/blob/main/skills/deprecated/README.md; https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md] Pocock's UL skill is published in the deprecated section of his repository, so it is evidence of a real mechanic but not proof that it remains a current flagship workflow component.
- [fact; source: https://arxiv.org/abs/2112.00114; https://arxiv.org/abs/2307.10680] Two seeded academic URLs resolved to unrelated papers rather than the claimed code-generation studies, which reduced the amount of directly reusable seed evidence and required source substitution.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M] Clarification studies measure better-specified task prompts, not long-running repository naming governance, so their support for glossary maintenance is mechanistic rather than direct.
- [inference; source: https://arxiv.org/abs/2310.10996; https://openreview.net/forum?id=s566pj5E5M; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.blog/ai-and-ml/github-copilot/how-to-build-reliable-ai-workflows-with-agentic-primitives-and-context-engineering/] Some of the observed benefit may come from generic structured context and clarification rather than from vocabulary control specifically, so the glossary-specific uplift should be treated as incremental rather than isolated.

### Open Questions

- What is the smallest glossary structure that captures most of the precision benefit without adding enough maintenance burden to be ignored?
- Can repository instrumentation measure naming drift directly, for example by tracking synonym introduction, rename churn, or reviewer comments on domain terminology?
- Should glossary enforcement happen only through context loading, or should linters, code review templates, and architecture checks also reject aliases-to-avoid?
- Can an agent safely propose glossary updates from repository changes without creating circular drift in the glossary itself?

---

## Output

- Type: knowledge
- Description: Evidence-backed synthesis showing that living Ubiquitous Language is a plausible high-leverage alignment artifact for AI-assisted software work, with strongest support for better precision and naming consistency rather than directly measured verbosity reduction or long-run drift prevention.
- Links:
  - https://martinfowler.com/bliki/UbiquitousLanguage.html
  - https://github.com/mattpocock/skills/blob/main/skills/deprecated/ubiquitous-language/SKILL.md
  - https://arxiv.org/abs/2406.19783
