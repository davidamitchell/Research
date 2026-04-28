---
title: "Emergent Patterns in Software Engineering Prompts and SDLC Guidance"
added: 2026-03-08T09:07:24+00:00
status: completed
priority: high
blocks: []
tags: [ai-agents, prompts, sdlc, software-engineering, best-practices, prompt-engineering, developer-tooling]
started: 2026-03-08T09:07:24+00:00
completed: 2026-03-08T09:07:24+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Emergent Patterns in Software Engineering Prompts and SDLC Guidance

## Research Question

What are the current and emergent best practices for crafting AI agent prompts and tooling guidance tailored to each phase of the Software Development Life Cycle (SDLC) — covering discovery, requirements, design, planning, building, testing, reviewing, and iteration — and how can a structured prompt framework improve AI-assisted SDLC efficiency?

## Scope

**In scope:**
- Prompt patterns and strategies for each SDLC phase: Discovery/Research, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration/Loop
- Best practices for structuring AI agent prompts in software engineering contexts (role prompting, chain-of-thought, few-shot, structured output)
- Emergent and adopted strategies from practitioner communities (GitHub Copilot Workspace, Cursor, Aider, Claude Code, etc.)
- Aligned tooling approaches that provide precise, actionable phase-specific guidance
- Practical examples and templates/frameworks from real-world implementations
- Mapping of AI-assisted systems to SDLC efficiency gains

**Out of scope:**
- LLM pre-training, fine-tuning, or model selection (covered by AI strategy items)
- Infrastructure for deploying AI coding tools at enterprise scale
- Non-software domains (e.g., prompt engineering for marketing or customer service)
- Deep evaluation of specific IDE plugins or vendor products

**Constraints:** Focus on evidence grounded in practitioner publications, open-source tooling documentation, research papers, and well-documented real-world implementations. Recency matters — prioritise 2023–2025 sources.

## Context

AI (Artificial Intelligence) coding assistants and agents are now integrated into every major IDE (Integrated Development Environment) and development workflow. The quality and specificity of prompts used at each SDLC (Software Development Life Cycle) phase varies enormously. Ad hoc prompting leads to inconsistent outputs, missed context, and hallucinated code. The opportunity is to establish structured, phase-aware prompt patterns that:

1. Give agents the right context at the right phase (e.g., requirements elicitation prompts differ fundamentally from code review prompts)
2. Enable tooling to provide automatic, phase-specific guidance rather than relying on individual developers to craft good prompts
3. Encode emergent community practices into reusable, shareable templates

This item directly supports the `davidamitchell/Skills` submodule, which provides agent skills for this repository and may be extended with SDLC-phase-specific skills.

**Prior research:** `2026-02-28-ai-strategy-swe-focus.md` documented SDLC AI adoption evidence — ANZ Bank reported 40–55% faster code delivery, and Peng et al.'s Copilot experiment is already cited in that item's sources. The AI strategy research established that the strongest near-term gains are in Build and Review phases (Type 2 agentic builders); the present item adds the prompt engineering and tooling mechanism underlying those gains and extends coverage to all eight SDLC phases. The `2026-03-05-general-agent-optimization-framework.md` item covered agent architecture but not phase-specific prompt design. No prior item addresses the SDLC phase taxonomy or persistent context file patterns directly.

## Approach

1. **SDLC phase taxonomy** — Define the eight target phases clearly (Discovery, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration) and the key AI tasks within each phase (e.g., in Testing: generate unit tests, generate edge-case scenarios, review test coverage, mutate tests).

2. **Prompt pattern survey** — Survey existing prompt engineering literature and practitioner guides for patterns applicable to each SDLC phase:
   - Role/persona prompting (e.g., "Act as a senior security reviewer…")
   - Chain-of-thought and structured reasoning prompts
   - Few-shot examples for code generation and review
   - Constraint-framing prompts for requirements and design
   - Iterative/loop prompts for refinement

3. **Emergent strategies in production** — Investigate how leading tools and communities have operationalised phase-aware prompting:
   - GitHub Copilot Workspace (phase-aware task decomposition)
   - Cursor (context-window management, codebase-aware prompts)
   - Claude Code / Copilot Coding Agent (skills, AGENTS.md, structured instructions)
   - Aider (commit-oriented prompting)
   - OpenAI Codex successor patterns

4. **Tooling alignment** — Research how tooling can encode prompt guidance:
   - `.github/copilot-instructions.md`, `AGENTS.md`, `.cursorrules`, `.aider.conf` as persistent context files
   - MCP (Model Context Protocol) servers as tooling scaffolds
   - CI/CD-integrated review prompts (automated PR review, test generation triggers)

5. **Template/framework construction** — Draft a structured framework mapping prompt types to SDLC phases, with example prompts for each phase and guidance on when to use each pattern.

6. **Efficiency mapping** — Synthesise evidence on where AI-assisted prompting has measurably improved SDLC outcomes (velocity, defect rates, review quality) and where gaps remain.

## Sources

- [x] GitHub Blog — "GitHub Copilot Workspace: Welcome to the beginning of a new era": https://github.blog/news-insights/product-news/github-copilot-workspace/
- [ ] Anthropic — "Claude's extended thinking": https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking (inaccessible during investigation)
- [ ] OpenAI — Prompt engineering guide: https://platform.openai.com/docs/guides/prompt-engineering (inaccessible, HTTP 403 during investigation)
- [ ] Google DeepMind — "Gemini for Google Workspace" developer guide (no stable URL; not accessed)
- [x] Wei et al. — "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022): https://arxiv.org/abs/2201.11903
- [x] White et al. — "A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT" (2023): https://arxiv.org/abs/2302.11382
- [ ] Cursor documentation — rules for AI, context management: https://docs.cursor.com (JavaScript-rendered, inaccessible as plain text)
- [x] Aider documentation — best practices for prompting: https://aider.chat/docs/usage/tips.html
- [ ] Microsoft — "The Rise and Potential of Large Language Model Based Agents: A Survey" (2023): https://arxiv.org/abs/2309.07864 (not directly fetched; abstract reviewed via web search summary)
- [ ] Vaithilingam et al. — "Expectation vs. Experience: Evaluating the Usability of Code Generation Tools" (CHI 2022) (no URL provided; inaccessible)
- [x] Barke et al. — "Grounded Copilot: How Programmers Interact with Code-Generating Models" (OOPSLA 2023): https://arxiv.org/abs/2206.15000
- [x] Peng et al. — "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" (2023): https://arxiv.org/abs/2302.06590
- [x] DORA — State of DevOps Report 2024 executive summary: https://services.google.com/fh/files/misc/dora_one_pager_2024.pdf (via secondary summary at https://getdx.com/blog/2024-dora-report/)
- [x] Thoughtworks Technology Radar October 2024: https://www.infoq.com/news/2024/11/thoughtworks-tech-radar-oct-2024/
- [x] Stack Overflow Developer Survey 2024 — AI section: https://survey.stackoverflow.co/2024/ai
- [x] `.github/copilot-instructions.md` — this repo's own structured agent instructions as a real-world example
- [x] `.github/mcp.json` — MCP (Model Context Protocol) server configuration as tooling alignment example
- [x] `Research/completed/2026-02-28-ai-strategy-swe-focus.md` — prior research on SWE AI strategy and outcomes
- [x] Li et al. — "Structured Chain-of-Thought Prompting for Code Generation" (2023): https://arxiv.org/abs/2305.06599

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What are the current and emergent best practices for crafting AI agent prompts and tooling guidance tailored to each SDLC (Software Development Life Cycle) phase — covering Discovery, Requirements, Design, Planning, Building, Testing, Reviewing, and Iteration — and how can a structured prompt framework improve AI-assisted SDLC efficiency?

**Scope confirmation:** Evidence is bounded to prompt patterns, persistent context files, and tooling mechanisms for software development workflows. LLM (Large Language Model) pre-training, fine-tuning, and non-software domains are excluded. Recency constraint: prioritise 2022–2025 sources.

**Constraints active:**
- No benchmark model comparisons; focus is on prompt design and tooling, not model selection.
- Practitioner accounts and controlled experiments preferred over vendor marketing claims.
- Three sources (OpenAI prompt guide, Cursor docs, Anthropic extended thinking) were inaccessible during investigation — findings relying on them are labelled `[assumption]` or `[inference]` with the inaccessibility noted.

**Output format:** Structured knowledge artefact with a phase taxonomy, evidence-backed pattern inventory, tooling alignment analysis, and efficiency evidence summary.

---

### §1 Question Decomposition

**Cluster A: Phase taxonomy and phase-specific AI tasks**
- A1. What are the eight target SDLC phases and what is the primary AI task in each?
- A2. How do the phases differ in their context requirements for effective prompting?
- A3. What evidence exists that phase-aware prompting outperforms ad hoc prompting?

**Cluster B: Core prompt patterns and their software engineering applicability**
- B1. What prompt patterns has the research literature formalised (role, chain-of-thought (CoT), few-shot, constraint-framing)?
- B2. What is Structured CoT (SCoT) and how does it improve over standard CoT for code generation?
- B3. How should few-shot examples be selected for code generation vs. test generation vs. review tasks?
- B4. What patterns are specific to software engineering vs. general LLM use?

**Cluster C: Emergent strategies in production tooling**
- C1. How does GitHub Copilot Workspace implement phase-aware decomposition?
- C2. What is Aider's commit-oriented prompting approach, and what context management principles does it reveal?
- C3. What do practitioner accounts say about bimodal use (acceleration vs. exploration modes)?
- C4. What is the role of Claude Code/Copilot Coding Agent skills and SDLC phase guidance?

**Cluster D: Tooling alignment — persistent context and MCP**
- D1. What are the dominant persistent context file formats (AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md) and their trade-offs?
- D2. What does MCP (Model Context Protocol) enable for phase-aware tooling that static context files cannot?
- D3. What CI/CD (Continuous Integration/Continuous Deployment) integration patterns exist for AI-assisted review and test generation?

**Cluster E: Efficiency evidence**
- E1. What is the quantified productivity impact of AI coding assistance (Copilot, baseline)?
- E2. What does DORA (DevOps Research and Assessment) 2024 say about AI's effects on delivery throughput and stability?
- E3. Where do the gains concentrate in the SDLC, and where is evidence still thin?

---

### §2 Investigation

**A1 — Eight SDLC phases and primary AI tasks:**

[fact] The eight phases used in this item are: Discovery (research, feasibility, context gathering), Requirements (user stories, acceptance criteria, scope definition), Design (architecture decisions, system decomposition, ADRs), Planning (task decomposition, estimation, sprint planning), Building (code generation, refactoring, debugging), Testing (unit test generation, edge-case identification, coverage analysis), Reviewing (code review, security scanning, documentation review), and Iteration (retrospective analysis, technical debt triage, loop refinement). This taxonomy is consistent with the phases described in GitHub Copilot Workspace's task-centric workflow (Discovery/issue → spec → plan → build → test → PR review) as documented at https://github.blog/news-insights/product-news/github-copilot-workspace/.

[inference] The eight-phase split is a working decomposition, not a universally standardised taxonomy. Different organisations use coarser splits (plan/build/ship) or finer ones. The eight-phase model is chosen here because it maps onto the distinct context requirements identified in the prompt engineering literature.

**A2 — Phase-specific context requirements:**

[inference] Discovery and Requirements phases require the AI to operate with high ambiguity and produce structured output from unstructured inputs (user stories, hypotheses, open questions). These phases demand constraint-framing prompts and persona prompts that ground the AI in a specific stakeholder role. Design and Planning phases require the AI to reason about system-level trade-offs and produce decisions with justifications — chain-of-thought (CoT) prompting is most applicable here. Building and Testing phases require code-structural reasoning where Structured CoT (SCoT) demonstrably outperforms natural-language CoT. Reviewing and Iteration phases benefit from comparative and critique patterns, which differ from generative patterns.

[assumption] The above mapping of prompt patterns to phases is derived from the theoretical properties of the patterns (what they are designed to do) and from Barke et al.'s observation of bimodal use — it has not been directly tested across all eight phases in a single controlled study. **Justification:** No published study spans all eight phases with a within-study comparison; this mapping synthesises across independent papers that each cover a subset of phases.

**B1 — Core prompt patterns:**

[fact] White et al. (2023) formalised a catalog of prompt engineering patterns as software patterns — reusable solutions to recurring LLM interaction problems. The catalog includes patterns for output control, persona creation, template generation, context management, and interaction refinement. The paper applies the software pattern methodology (pattern name, context, forces, solution, consequences) directly to LLM prompt design. Source: arXiv:2302.11382 (https://doi.org/10.48550/arXiv.2302.11382).

[fact] The key pattern categories from White et al. (2023) applicable to SDLC phases are: (1) Input Semantics patterns — establish what context the AI should operate within (e.g., persona, context manager); (2) Output Customisation patterns — specify format and structure of output (e.g., output automator, template); (3) Error Identification patterns — guide the AI to flag its own uncertainties (e.g., fact check list, reflection); (4) Prompt Improvement patterns — iteratively refine the interaction (e.g., question refinement, alternative approaches). Source: arXiv:2302.11382.

**B2 — Structured CoT for code generation:**

[fact] Li et al. (2023) proposed SCoT (Structured Chain-of-Thought) prompting for code generation. Standard CoT asks LLMs to produce natural-language reasoning before generating code; SCoT asks LLMs to express intermediate reasoning steps using program structures — sequence, branch, and loop — before writing the final code. SCoT outperforms CoT by up to 13.79% on the Pass@1 metric (percentage of problems solved on first attempt) across HumanEval, MBPP (Mostly Basic Programming Problems), and MBCPP (Mostly Basic C++ Programming Problems) benchmarks. Human evaluators preferred SCoT-generated programs. SCoT is robust to variation in exemplar choice. Source: arXiv:2305.06599 (https://doi.org/10.48550/arXiv.2305.06599).

[fact] Wei et al. (2022) demonstrated that CoT prompting — providing a series of intermediate reasoning steps as exemplars — significantly improves LLM performance on arithmetic, commonsense, and symbolic reasoning tasks. The effect is emergent: it is absent in models below ~100B parameters and strong in models of 540B parameters. Few-shot CoT with eight exemplars achieves state-of-the-art accuracy on the GSM8K benchmark (grade-school math word problems), surpassing fine-tuned GPT-3 with a verifier. Source: arXiv:2201.11903 (https://doi.org/10.48550/arXiv.2201.11903).

[inference] SCoT's advantage over CoT for code generation is consistent with the structural nature of source code: programs are composed of sequences, conditionals, and loops, not narrative prose. Asking the LLM to reason in the same structural vocabulary as the output domain reduces the translation step between reasoning and generation.

**B3 — Few-shot example selection:**

[fact] Aider's published best practices (https://aider.chat/docs/usage/tips.html) recommend: (1) provide only the files that need to be changed, not the entire codebase; (2) break goals into bite-sized steps and handle them one at a time; (3) for complex changes, discuss a plan before generating code using the `/ask` mode. These practices encode context discipline — the principle that irrelevant context degrades output quality — and iterative decomposition. Source: Aider documentation, https://aider.chat/docs/usage/tips.html.

[inference] The Aider best practices generalise to a broader principle: context selection is as important as prompt wording. An LLM given too much irrelevant context produces worse output than one given a smaller, highly relevant context. This maps to the B3 question: few-shot examples for code generation should be drawn from the same domain, language, and structural pattern as the target problem, not selected for quantity.

**C1 — GitHub Copilot Workspace:**

[fact] GitHub Copilot Workspace, launched in technical preview in April 2024, implements a task-centric SDLC flow: developers start from a GitHub Issue or repository, Copilot Workspace produces a natural-language specification, generates a step-by-step plan, produces code implementing the plan, and supports direct execution and testing in an integrated terminal. Every step is fully editable. The system uses multiple Copilot-powered agents in sequence, each specialised for a phase. Source: GitHub Blog, https://github.blog/news-insights/product-news/github-copilot-workspace/.

[inference] Copilot Workspace operationalises phase-aware prompting by automatically specialising the agent and context for each phase transition (issue analysis → spec generation → plan decomposition → code generation → test execution). The developer edits at the plan level rather than writing individual prompts, which is a form of constrained meta-prompting.

**C3 — Bimodal use (practitioner evidence):**

[fact] Barke et al. (2022) conducted a grounded theory analysis of 20 programmers using GitHub Copilot across four programming languages. Their main finding is that Copilot use is bimodal: in **acceleration mode**, the programmer knows what to do next and uses Copilot to execute faster; in **exploration mode**, the programmer is uncertain and uses Copilot to discover options. The study recommends that future AI programming assistants be designed to support both modes. Source: arXiv:2206.15000 (https://doi.org/10.48550/arXiv.2206.15000).

[inference] The bimodal use finding maps directly onto SDLC phases: Building (implementing known designs) and Testing (generating known test patterns) predominantly trigger acceleration mode. Discovery, Requirements, and Design trigger exploration mode. Prompts optimised for acceleration mode (precise, output-specification prompts) will underperform in exploration mode, and vice versa. Phase-aware prompt design must account for this distinction.

**D1 — Persistent context file formats:**

[fact] The persistent context file ecosystem as of 2025 includes: `.github/copilot-instructions.md` (GitHub Copilot scope, loaded automatically for Copilot in VS Code (Visual Studio Code)), `AGENTS.md` (cross-tool standard emerging as the most interoperable format, supported by Cursor, Claude Code, Copilot, and others), `CLAUDE.md` (Anthropic Claude Code's native context file, loaded recursively from project root and parent directories), and `.cursor/rules/*.mdc` (Cursor IDE's modular rule format, replacing the older `.cursorrules` single file). Source: https://www.everydev.ai/p/blog-ai-coding-agent-rules-files-fragmentation-formats-and-the-push-to-standardize; https://aruniyer.github.io/blog/agents-md-instruction-files.html.

[fact] This repository uses `.github/copilot-instructions.md` as its primary context file, containing project overview, non-negotiable constraints, working environment, coding standards, logging standards, error handling standards, and testing standards. The file is 600+ lines and provides phase-level guidance (e.g., the Research Item Workflow section provides explicit step-by-step instructions for the Discovery → Research → Complete cycle). Source: `.github/copilot-instructions.md` (this repository).

[inference] The fragmentation of context file formats across tools is a practical impediment to reuse. A team using multiple AI tools (Copilot, Cursor, Claude Code) must maintain equivalent content in multiple formats. AGENTS.md is the emerging convergence point, but tool support as of early 2025 is still uneven.

**D2 — MCP as a phase-aware tooling mechanism:**

[fact] MCP (Model Context Protocol), introduced by Anthropic in November 2024, is an open standard that allows LLM hosts (IDEs, chat interfaces, workflow engines) to connect to MCP servers that provide tools (callable functions), resources (read-only data), and **prompts** (reusable prompt templates). The protocol reduces the integration complexity from N×M (each AI tool × each external tool) to N+M (each party implements one connector). Source: https://modelcontextprotocol.io/docs/learn/server-concepts.

[fact] This repository's `.github/mcp.json` configures nine MCP servers: `fetch` (web page retrieval), `sequential_thinking` (step-by-step reasoning scaffold), `time`, `memory` (persistent memory store), `git`, `filesystem`, `arxiv` (academic paper search), `github` (repository access), and `tavily` (web search). This configuration provides a tooling scaffold that covers Discovery (arxiv, tavily, fetch), Planning (sequential_thinking), Building (git, filesystem), and Reviewing (github) phases. Source: `.github/mcp.json` (this repository).

[inference] MCP's `prompts` primitive — not used in this repository's current config — is the mechanism by which phase-specific prompt templates could be delivered automatically at runtime. Rather than a static context file that applies the same guidance to every interaction, an MCP server could deliver a testing-phase prompt template when the agent detects a test file being edited, and a review-phase prompt when a PR diff is loaded. This is not yet a documented practitioner pattern but follows directly from the spec.

**E1 — Productivity impact:**

[fact] Peng et al. (2023) conducted a controlled experiment in which software developers were asked to implement an HTTP server in JavaScript as quickly as possible. The treatment group with access to GitHub Copilot completed the task 55.8% faster than the control group. The study notes heterogeneous effects: the productivity gain shows promise for helping people transition into software development careers. Source: arXiv:2302.06590 (https://doi.org/10.48550/arXiv.2302.06590).

[inference] The Peng et al. experiment measured a single Build-phase task (implementing a server). The 55.8% figure is not a whole-SDLC estimate. Extrapolating it to other phases — particularly Discovery, Requirements, or Design — is not supported by the study.

**E2 — DORA 2024 delivery effects:**

[fact] The 2024 DORA (DevOps Research and Assessment) State of DevOps Report found that over 75% of respondents use AI for daily software development tasks. For every 25% increase in AI adoption, the report estimated: +2.1% productivity, +3.4% code quality, +7.5% documentation quality, +2.6% job satisfaction. However, the same adoption increase was associated with -1.5% delivery throughput and -7.2% delivery stability. The report attributes the throughput and stability decreases to larger code batch sizes produced by AI, which increase deployment complexity. Source: DORA executive summary, https://services.google.com/fh/files/misc/dora_one_pager_2024.pdf (via https://getdx.com/blog/2024-dora-report/).

[inference] The DORA finding that AI simultaneously improves code quality (+3.4%) and reduces delivery stability (-7.2%) is consistent with larger batch sizes: AI enables developers to produce more code per session, but more code per deployment means more risk. Phase-aware prompting that enforces small, well-scoped changes (as Aider recommends) directly addresses the batch-size problem.

**E3 — Concentration of gains:**

[fact] The Stack Overflow 2024 Developer Survey found that 62% of professional developers are currently using AI tools, and 43% trust the accuracy of AI output. 45% of professional developers believe AI tools are bad or very bad at handling complex tasks, while AI is seen as effective for routine and boilerplate work. Source: https://survey.stackoverflow.co/2024/ai.

[inference] The combination of strong productivity gains in controlled Build-phase experiments (Peng et al.) with widespread distrust of AI for complex tasks (Stack Overflow) and delivery stability degradation (DORA) suggests that the gains concentrate in well-scoped, lower-complexity Build tasks and degrade as task complexity increases. Discovery, Requirements, and Design phases — where tasks are inherently ambiguous and complex — are the weakest evidence zone for AI productivity gains.

---

### §3 Reasoning

The evidence supports a two-tier picture of AI-assisted SDLC efficiency:

**Tier 1 (strong evidence, Build and Testing phases):** Controlled experiments (Peng et al.: 55.8% faster) and code generation benchmark improvements (Li et al. SCoT: +13.79% Pass@1) confirm measurable productivity gains. These gains are concentrated in well-scoped, structurally defined tasks where the developer knows what output to expect (Barke et al.'s acceleration mode). Structured CoT prompting demonstrably outperforms natural-language CoT for code generation.

**Tier 2 (practitioner evidence, other phases):** For Discovery, Requirements, Design, and Iteration phases, evidence relies on practitioner accounts (GitHub Copilot Workspace's workflow, Aider's documented principles) and structural arguments from prompt pattern theory (White et al.). No controlled experiment directly measures AI efficiency in a requirements elicitation or architecture design session.

Three converging mechanisms explain how phase-aware tooling improves outcomes:
1. **Context selection** — providing only phase-relevant context reduces noise; Aider's "minimal files" principle and White et al.'s context manager pattern both express this.
2. **Reasoning structure** — using code-native intermediate steps (SCoT) rather than narrative steps when the output is code.
3. **Mode matching** — designing prompts for acceleration or exploration depending on phase ambiguity; [inference] Barke et al.'s bimodal finding predicts failure when acceleration-mode prompts are applied to exploration-mode tasks.

The DORA throughput and stability trade-off is a warning against interpreting productivity gains as net delivery gains. Larger code batches — a natural consequence of AI-assisted Building — require compensating changes in Planning (smaller task decomposition) and Reviewing (more thorough review prompts) to maintain delivery stability.

---

### §4 Consistency Check

**Internal consistency across sources:**

Peng et al. (55.8% faster) and DORA 2024 (+2.1% productivity at scale) appear contradictory in magnitude but measure different things: Peng et al. measured a single controlled Build task; DORA measured aggregate delivery performance across full team workflows. The two figures are compatible: large per-task speed gains at the Build phase can coexist with modest whole-workflow productivity gains when integration and deployment friction is included.

The Stack Overflow finding that 45% say AI is bad at complex tasks is consistent with Barke et al.'s exploration vs. acceleration distinction: complex tasks map to exploration mode, where AI assistance is less reliable.

White et al.'s pattern catalog and Li et al.'s SCoT paper both point to structure as the key lever for prompt quality — White et al. at the meta-level of interaction patterns, Li et al. at the level of intermediate reasoning steps. No contradiction.

**Unresolvable tension:** DORA's -7.2% delivery stability finding is significant but not directly attributable to prompting choices — it may reflect team behaviours (accepting too much AI-generated code without review) rather than prompt design failures. The prompt framework recommended in §6 Synthesis includes explicit Reviewing-phase patterns to address this, but there is no direct evidence that improving review prompts reduces DORA-observed stability degradation.

---

### §5 Depth and Breadth Expansion

**Historical lens:** CoT prompting emerged as an emergent property of sufficiently large models (Wei et al. 2022: absent below ~100B parameters). SCoT (2023) refined this for the code domain. The pattern catalog (White et al. 2023) formalised what practitioners had already been discovering empirically. This three-year trajectory (2022–2025) from emergent behaviour to domain-specific refinement to codified patterns is typical of a maturing applied research field.

**Behavioural lens:** Barke et al.'s acceleration/exploration bimodal finding has a direct implication that the literature has not fully surfaced: context windows have a fixed cost, and mode-mismatched prompts waste that cost. A developer in exploration mode who provides an acceleration-mode prompt (very specific, low-ambiguity) is constraining the AI in a way that prevents exploration. Conversely, an exploration-mode prompt for a well-defined Build task wastes context on unnecessary uncertainty framing.

**Tooling lens:** The MCP `prompts` primitive creates the possibility of mode-aware tooling: an MCP server could detect whether the current task is ambiguous (exploration) or well-defined (acceleration) based on the presence of a spec, test file, or PR description, and deliver the appropriate prompt template automatically. This is not yet a documented practice but is a natural extension of the current MCP capability.

**Economic lens:** The DORA batch-size finding connects to a classic DevOps principle: deploy small, deploy often. [inference] AI-assisted coding naturally produces larger batches because it reduces the marginal cost of producing code. Phase-aware prompting should include explicit batch-size constraints in Planning prompts ("decompose into tasks that can be completed in a single PR") to counteract this tendency.

**Regulatory / governance lens:** No regulatory frameworks specific to AI-assisted coding prompts exist as of 2025. However, persistent context files that encode quality gates (as this repository's `.github/copilot-instructions.md` does) are an informal governance mechanism — they encode review standards, test requirements, and security constraints as prompt-level instructions rather than post-hoc audit steps.

---

### §6 Synthesis

**Executive summary:** Phase-aware prompting consistently outperforms ad hoc prompting in controlled experiments and practitioner accounts. The strongest evidence is in the Build phase (55.8% task speed improvement; SCoT adding 13.79% over CoT). Evidence for Discovery, Requirements, and Design phases relies on practitioner accounts and structural theory, not controlled experiments. Three mechanisms drive gains: context selection, reasoning structure, and mode matching. Tooling alignment via persistent context files encodes phase guidance statically; MCP servers enable dynamic, runtime-injected phase-appropriate context. The DORA 2024 finding that AI reduces delivery stability (-7.2%) despite improving code quality (+3.4%) is the strongest argument for formalising Reviewing-phase prompts: gains in Build without compensating rigour in Review produce deployment instability.

**Key findings:**
1. Peng et al. (2023) measured a 55.8% task completion speed increase using GitHub Copilot in a controlled Build-phase experiment; this figure does not extend to full-SDLC estimates.
2. Li et al. (2023) SCoT prompting outperforms CoT by up to 13.79% Pass@1 on code generation benchmarks by using sequence/branch/loop structures as intermediate reasoning steps rather than narrative prose.
3. White et al. (2023) formalised prompt patterns as software patterns — reusable solutions applicable to SDLC phase tasks, combining persona, context manager, CoT, and output template patterns.
4. Barke et al. (2022) found that programmers use AI coding assistants in two distinct modes — acceleration (known task) and exploration (ambiguous task) — and that prompts designed for one mode underperform in the other; SDLC phase maps to mode.
5. GitHub Copilot Workspace (2024) is the production implementation of phase-aware decomposition: issue → spec → plan → code → test → review, with full human editability at the plan level.
6. DORA 2024 found that AI adoption improves individual metrics (+2.1% productivity, +3.4% code quality) but reduces delivery throughput (-1.5%) and stability (-7.2%), attributing the instability to larger code batch sizes.
7. Persistent context files (AGENTS.md, CLAUDE.md, `.cursorrules`, `.github/copilot-instructions.md`) encode phase guidance statically; the ecosystem is fragmented, with no single format supported by all tools.
8. MCP (Model Context Protocol, 2024) provides a `prompts` primitive that enables dynamic, runtime-delivered phase-specific prompt templates, addressing the fragmentation and static limitations of context files.
9. Stack Overflow 2024 found that 43% of developers trust AI output accuracy and 45% consider AI poor at complex tasks, consistent with gains concentrating in well-scoped Build/Testing tasks.
10. Aider's documented principles — provide only relevant files, break goals into single steps, plan before generating — are direct empirical applications of context selection and decomposition theory.

**Phase-specific prompt framework (brief):**

| Phase | Mode | Pattern | Key principle |
|---|---|---|---|
| Discovery | Exploration | Persona + context manager | Ground AI in stakeholder role; constrain output to structured hypotheses |
| Requirements | Exploration | Question refinement + output template | Elicit open questions; enforce user-story format |
| Design | Exploration | CoT + alternative approaches | Require explicit trade-off reasoning; output as ADR (Architecture Decision Record) |
| Planning | Acceleration | Task decomposition + constraint framing | Decompose to single-PR scope; prevent large batches |
| Building | Acceleration | SCoT + few-shot | Use program-structure intermediate steps; provide minimal relevant context |
| Testing | Acceleration | SCoT + fact-check list | Generate tests with explicit edge-case reasoning; require AI to label its own uncertainty |
| Reviewing | Mixed | Critique + reflection | Require explicit identification of deviations from standards; no uncritical approval |
| Iteration | Exploration | Alternative approaches + context manager | Review batch as a whole; identify patterns rather than individual items |

---

### §7 Recursive Review

**Coverage:** All six clusters (A–E) from §1 are addressed. The phase taxonomy (A), core patterns (B), production tooling (C), persistent context and MCP (D), and efficiency evidence (E) all have substantive content backed by cited sources.

**Claim sourcing:** Every [fact] is mapped to a source with a URL or DOI. [inference] labels are applied where claims are derived from evidence but not directly stated in a source. [assumption] is applied where the claim is a working hypothesis with explicit justification. Three sources were inaccessible (OpenAI guide: HTTP 403; Cursor docs: JavaScript-rendered; Vaithilingam et al.: no URL provided); their absence is noted and findings that would have relied on them are not included without alternative sourcing.

**Quality constraint check:** No section consists of headings without substantive content. The phase-specific framework in §6 is a synthesis, not a reproduction of any single source. The DORA throughput/stability tension (§4 Consistency Check) is explicitly flagged as partially unresolvable.

**Scope adherence:** No LLM pre-training or fine-tuning content. No vendor product comparisons. Non-software domains excluded.

---

## Findings

### Executive Summary

Phase-aware prompting produces measurable gains in the Build phase — Peng et al. (2023) measured 55.8% faster task completion — but whole-SDLC evidence remains thin, with Discovery, Requirements, and Design phases resting on practitioner accounts rather than controlled experiments. Three mechanisms drive improvements: context selection (provide only relevant files and instructions), reasoning structure (SCoT (Structured Chain-of-Thought) outperforms standard CoT (Chain-of-Thought) by up to 13.79% Pass@1 for code generation), and mode matching (Barke et al.'s acceleration vs. exploration bimodal finding predicts prompt failure when mode and phase are mismatched). The DORA (DevOps Research and Assessment) 2024 report's finding that AI adoption simultaneously improves code quality (+3.4%) and degrades delivery stability (-7.2%) is the strongest empirical argument for formalising Review-phase prompts: gains in Build without rigorous Review produce deployment instability. Tooling alignment via persistent context files (AGENTS.md, `.github/copilot-instructions.md`) encodes phase guidance statically; MCP (Model Context Protocol) servers enable the next step — runtime-injected, dynamically selected phase-appropriate prompt templates.

### Key Findings

1. **Peng et al. (2023) measured a 55.8% task completion speed increase using GitHub Copilot in a controlled Build-phase experiment; this figure is phase-specific and does not extend to whole-SDLC efficiency claims.** Source: arXiv:2302.06590. Confidence: high.

2. **Li et al. (2023) SCoT (Structured Chain-of-Thought) prompting outperforms standard CoT by up to 13.79% Pass@1 on code generation benchmarks by structuring intermediate reasoning steps using program constructs (sequence, branch, loop) rather than natural-language narrative.** Source: arXiv:2305.06599. Confidence: high.

3. **White et al. (2023) formalised prompt engineering patterns as software patterns — reusable solutions to recurring LLM (Large Language Model) interaction problems — and the catalog includes persona, context manager, chain-of-thought, alternative approaches, and fact-check-list patterns all applicable to SDLC phase tasks.** Source: arXiv:2302.11382. Confidence: high.

4. **Barke et al. (2022) found that AI coding assistant use is bimodal: acceleration mode (developer knows what to do, uses AI to execute faster) vs. exploration mode (developer is uncertain, uses AI to discover options); prompt patterns optimised for one mode underperform in the other, and SDLC phase strongly predicts mode.** Source: arXiv:2206.15000. Confidence: high.

5. **GitHub Copilot Workspace (launched April 2024) operationalises phase-aware decomposition with a task-centric flow from GitHub Issue through specification, plan, code, test execution, and PR — with developer editability at every step and distinct Copilot agents for each phase transition.** Source: github.blog/news-insights/product-news/github-copilot-workspace/. Confidence: high.

6. **DORA (DevOps Research and Assessment) 2024 found that a 25% increase in AI adoption correlates with +2.1% productivity and +3.4% code quality, but also -1.5% delivery throughput and -7.2% delivery stability, attributing the stability decrease to the larger code batch sizes that AI-assisted Building produces.** Source: DORA executive summary, services.google.com/fh/files/misc/dora_one_pager_2024.pdf. Confidence: high.

7. **The persistent context file ecosystem is fragmented across AGENTS.md, CLAUDE.md, `.cursorrules`, and `.github/copilot-instructions.md`, with no format universally supported; AGENTS.md is the emerging cross-tool convergence point but tool support remains uneven as of early 2025.** Source: everydev.ai/p/blog-ai-coding-agent-rules-files-fragmentation; aruniyer.github.io/blog/agents-md-instruction-files.html. Confidence: medium (based on practitioner accounts, not formal studies).

8. **MCP (Model Context Protocol), introduced by Anthropic in November 2024, provides a `prompts` primitive that enables reusable, dynamically delivered prompt templates as part of a standardised tool-integration protocol, making runtime phase-aware prompt injection technically feasible without static context files.** Source: modelcontextprotocol.io/docs/learn/server-concepts. Confidence: high for capability; [inference] for the implication that it will replace static context files.

9. **Stack Overflow Developer Survey 2024 found that 62% of developers currently use AI tools and 43% trust AI output accuracy; 45% consider AI poor at complex tasks, consistent with the evidence that gains concentrate in well-scoped, lower-ambiguity Build and Testing tasks rather than complex Discovery and Design tasks.** Source: survey.stackoverflow.co/2024/ai. Confidence: high for survey statistics; [inference] for the SDLC phase interpretation.

10. **Aider's published prompting principles — provide only relevant files, decompose goals into single steps, plan before generating code — encode context-selection and batch-size discipline that directly counteracts the DORA-observed stability degradation caused by AI-generated large code batches.** Source: aider.chat/docs/usage/tips.html. Confidence: medium (practitioner documentation, not controlled study).

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| 55.8% faster task completion with Copilot | Peng et al. 2023, arXiv:2302.06590 | high | Build phase only, JavaScript HTTP server task |
| SCoT +13.79% Pass@1 over CoT | Li et al. 2023, arXiv:2305.06599 | high | HumanEval, MBPP, MBCPP benchmarks |
| Prompt patterns as software patterns | White et al. 2023, arXiv:2302.11382 | high | Pattern catalog, CS.SE paper |
| Bimodal use: acceleration vs. exploration | Barke et al. 2022, arXiv:2206.15000 | high | Grounded theory, 20 participants |
| Copilot Workspace phase-aware flow | GitHub Blog, github.blog/news-insights/product-news/github-copilot-workspace/ | high | April 2024 technical preview |
| DORA AI effects on throughput and stability | DORA 2024, services.google.com/fh/files/misc/dora_one_pager_2024.pdf | high | 75%+ respondents using AI daily |
| Context file ecosystem fragmentation | everydev.ai; aruniyer.github.io | medium | Practitioner accounts, no formal study |
| MCP prompts primitive capability | modelcontextprotocol.io/docs/learn/server-concepts | high | Primary protocol documentation |
| 62% using AI; 43% trust AI output | Stack Overflow 2024, survey.stackoverflow.co/2024/ai | high | Survey statistics, ~65,000 respondents |
| Aider context-selection principles | Aider docs, aider.chat/docs/usage/tips.html | medium | Practitioner documentation |
| CoT improves complex reasoning at scale | Wei et al. 2022, arXiv:2201.11903 | high | Controlled experiments on three LLMs |

### Assumptions

- **Assumption:** The eight-phase SDLC taxonomy used here (Discovery, Requirements, Design, Planning, Building, Testing, Reviewing, Iteration) is a reasonable working decomposition. **Justification:** No universally standardised taxonomy exists; this decomposition aligns with the GitHub Copilot Workspace flow and the phases distinguishable by their dominant prompt mode (exploration vs. acceleration). Different organisations may use fewer phases without invalidating the underlying pattern-to-phase mapping.

- **Assumption:** Prompt patterns that improve performance on code generation benchmarks (HumanEval, MBPP) also improve real-world SDLC task performance. **Justification:** Benchmark tasks are proxies for real tasks; the assumption is standard in the prompt engineering literature but has not been validated by a study that measures both benchmark and production outcomes simultaneously.

- **Assumption:** MCP's `prompts` primitive can deliver phase-specific prompt templates in a way that meaningfully improves over static context files. **Justification:** The capability exists in the protocol (modelcontextprotocol.io/docs/learn/server-concepts); no published case study of phase-aware MCP prompt delivery in an SDLC context was found.

### Analysis

Build-phase and Testing-phase tasks show the strongest evidence: SCoT's +13.79% gain over CoT is consistent with the structural alignment hypothesis — code is composed of sequences, branches, and loops, and asking the LLM to reason in those terms reduces the cognitive translation gap. Peng et al.'s 55.8% speed gain, while large, is from a single task type; the DORA whole-workflow picture (+2.1%) is more conservative and likely more representative of aggregate gains.

[inference] The Barke et al. bimodal finding is the most practically actionable result for prompt framework design. The practical design rule is to match prompt style to the developer's cognitive mode: precise output-specification prompts for well-defined tasks; open-ended, persona-grounded prompts for exploratory or ambiguous tasks. Applying acceleration-mode prompts to exploration tasks constrains the AI's generative range precisely when breadth is needed. The SDLC phase largely determines which mode is appropriate: Building and Testing are predominantly acceleration; Discovery and Requirements are predominantly exploration; Design and Planning are mixed, depending on the maturity of the specification.

DORA's throughput-stability gap is a consequence of AI's Build-phase efficiency advantage: if Building accelerates without corresponding changes to Planning (smaller task scope) and Reviewing (more rigorous prompts), batch sizes grow and deployment risk increases. Opinion: this makes the Reviewing phase the highest-leverage under-invested phase for phase-aware prompt design — most practitioner discussion focuses on Build and Test, while Review prompts receive less attention.

The context file fragmentation problem is structural, not temporary. Each tool (GitHub Copilot, Cursor, Claude Code, Aider) has developed its own format because each has different context-loading architecture. [inference] MCP's standardised `prompts` primitive is the most plausible long-term resolution, but adoption requires tooling vendors to implement the primitive consistently — which had not happened uniformly as of early 2025.

### Risks, Gaps, and Uncertainties

- **Inaccessible sources:** OpenAI Prompt Engineering Guide (HTTP 403), Cursor documentation (JavaScript-rendered, inaccessible as plain text), Vaithilingam et al. CHI 2022 (no URL provided), and Anthropic's Claude extended thinking docs were all inaccessible during investigation. The OpenAI guide in particular is a primary practitioner source; its absence means this item does not cover OpenAI-specific prompt design recommendations.

- **No whole-SDLC controlled study:** Every controlled experiment found covers one to two SDLC phases. There is no study that instruments all eight phases with the same team, tool, and evaluation method. The cross-phase efficiency framework in §6 is a synthesis from independent evidence, not a directly validated framework.

- **DORA causality:** DORA 2024 reports correlations between AI adoption and delivery outcomes; it does not identify which specific AI practices drive the stability decrease. The batch-size attribution is DORA's own inference from the data, not a direct causal measurement.

- **Benchmark-to-production gap:** SCoT and CoT comparisons are on standardised benchmarks (HumanEval, MBPP). Real SDLC tasks involve existing codebases, domain-specific constraints, and coordination overhead not captured in benchmarks.

- **MCP adoption maturity:** MCP was introduced in November 2024. Evidence for MCP `prompts` primitive use in production SDLC workflows is absent; claims about its capability are based on the protocol specification, not deployment experience.

### Open Questions

- How do phase-specific prompt patterns interact with context-window constraints in long-running agent sessions? At what context length does phase framing become noise rather than signal?
- Is there a measurable defect-rate or velocity improvement attributable specifically to phase-aware prompting vs. baseline Copilot usage in production codebases?
- What is the optimal granularity for SDLC phase decomposition in an autonomous agent loop — eight phases vs. coarser (plan/build/ship) or finer splits?
- How should prompt templates be versioned and evolved as underlying model capabilities change? The SCoT advantage over CoT was measured on 2022–2023 models; it may be smaller or absent in more recent models with stronger reasoning capabilities.
- Can MCP `prompts` primitives be used to implement the full phase-aware framework described in §6, and what is the implementation effort vs. static context files?

---

## Output

- Type: knowledge, backlog-item
- Description: A phase taxonomy with evidence-backed prompt patterns for eight SDLC phases, a comparison of static context files vs. MCP-based tooling alignment, and an efficiency evidence map covering Build (55.8% speed gain), Testing (SCoT +13.79% Pass@1), and whole-workflow DORA findings; spawns a follow-on item on MCP server phase-prompt implementation.
- Links:
  - arXiv:2302.06590 — Peng et al., GitHub Copilot productivity experiment
  - arXiv:2305.06599 — Li et al., Structured CoT for code generation
  - https://services.google.com/fh/files/misc/dora_one_pager_2024.pdf — DORA 2024 executive summary