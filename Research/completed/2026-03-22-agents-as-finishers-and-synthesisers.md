---
review_count: 2
title: "Artificial Intelligence (AI) agents as finishers and synthesisers: optimising AI agents to complement ideation-strong, execution-weak humans"
added: 2026-03-23T08:27:40+00:00
status: completed
priority: high  # low | medium | high
blocks: []
tags: [agents, human-ai-collaboration, productivity, finishing, synthesis, orchestration, cognitive-styles]
started: 2026-03-23T08:27:40+00:00
completed: 2026-03-23T08:27:40+00:00
output: [knowledge, backlog-item]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Artificial Intelligence (AI) agents as finishers and synthesisers: optimising AI agents to complement ideation-strong, execution-weak humans

## Research Question

What agent configurations, prompt strategies, orchestration patterns, and tooling choices allow an AI agent (or agent team) to act as a reliable *finisher* and *synthesiser* - completing work that a human has started but not followed through on - and what are the practical limits of this complementary model?

Supporting questions:
- What cognitive or productivity frameworks describe the "ideas person / weak finisher" profile, and how does that map to AI agent capabilities?
- Which agent roles (planner, executor, reviewer, synthesiser, organiser) are most effective at compensating for execution and organisation weaknesses?
- What prompt patterns and agent instructions produce reliable task completion rather than a new layer of partial ideas?
- How should a human-agent handoff be structured so the agent can pick up unfinished work without losing context?
- What are the failure modes when using agents as finishers (e.g. hallucinated completions, loss of original intent, over-generalisation)?
- Are there published agent frameworks, research papers, or real-world case studies that specifically address human-AI cognitive complementarity?
- What tooling (GitHub Copilot Agent, AutoGen, CrewAI, LangGraph, etc.) is best suited to a "finishing and synthesising" use case in a no-local-Integrated Development Environment (IDE) environment?

## Scope

**In scope:**
- Agent roles explicitly designed to finish, organise, or synthesise: task completion agents, summarisation agents, project management agents, note-to-action agents
- Human-AI cognitive complementarity research - divergent thinking (ideation) vs. convergent thinking (execution, synthesis)
- Prompt engineering patterns for handoff, context preservation, and completion
- Orchestration frameworks available without a local IDE (GitHub Copilot Agent, GitHub Actions-based agents, Application Programming Interface (API)-accessible agents)
- Failure modes and mitigations specific to "finishing" use cases
- Practical patterns already used in this repo (`research-loop` workflow, `copilot-instructions.md`, skills) that could be extended

**Out of scope:**
- General Large Language Model (LLM) capability benchmarks not related to finishing or synthesis
- Visual Studio Code or local IDE extensions (owner has no local IDE)
- Research on pure automation (no human in the loop)
- Credentials or services not listed in the approved credentials table

**Constraints:** GitHub website and iOS app only - no local IDE. Agent work must be triggerable from a browser or mobile.

## Context

The owner has identified a personal superpower (ideation, pattern recognition, abstraction) and a corresponding weakness (finishing, following through, organisation). The question is whether AI agents can be configured and orchestrated to fill exactly those gaps - acting as a persistent, context-aware execution layer on top of a human's ideas.

This is not a generic "how do I use AI" question. It is a specific design challenge: how do you structure a human-agent system where the human provides direction and insight while the agent provides completion and coherence? Getting this wrong leads to more half-finished ideas managed by an agent rather than fewer. Getting it right could dramatically increase throughput.

The question is high-priority because it directly shapes how this Research repo and its workflows should evolve - including whether agent skills, the research-loop workflow, or new tooling should be added.

## Approach

1. **Map the human profile to agent capabilities** - research cognitive frameworks for divergent vs. convergent thinking and identify where agents currently perform well on convergent tasks (summarising, organising, completing, structuring).
2. **Survey agent roles and orchestration patterns** - catalogue "finisher" and "synthesiser" agent roles from existing frameworks (CrewAI, AutoGen, LangGraph, GitHub Copilot Agent). Note which roles are available without a local IDE.
3. **Identify prompt and instruction patterns** - find published or community-documented prompt patterns for task handoff, context preservation, and completion. Evaluate against the failure modes (hallucination, intent drift).
4. **Review failure modes and mitigations** - identify what goes wrong when agents are used as finishers and what structural or prompt-level interventions reduce those failures.
5. **Assess tooling fit** - evaluate which agent frameworks and tools are usable given the no-local-IDE constraint and the approved credentials table.
6. **Produce concrete recommendations** - output: a knowledge summary of what works and why, plus concrete backlog items for changes to this repo's agent configuration, skills, or workflows.

## Sources

- [x] CrewAI documentation on agent roles and task assignment - https://docs.crewai.com/concepts/agents
- [x] AutoGen documentation on multi-agent conversation patterns - https://microsoft.github.io/autogen/stable/
- [x] LangGraph documentation on agent orchestration - https://docs.langchain.com/oss/python/langgraph/overview
- [x] GitHub Copilot coding agent overview - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [x] GitHub Copilot coding agent how-to index - https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
- [x] GitHub repository custom instructions documentation - https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- [x] GitHub blog: coding agent 101 - https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- [x] Anthropic, "Building effective agents" - https://www.anthropic.com/research/building-effective-agents
- [x] Design Council, "The Double Diamond" - https://www.designcouncil.org.uk/our-resources/the-double-diamond/
- [x] Risko and Gilbert, "Cognitive Offloading" - https://doi.org/10.1016/j.tics.2016.07.002
- [x] Berry et al., "Cognitive Offloading: Structuring the Environment to Improve Children's Working Memory Task Performance" - https://doi.org/10.1111/cogs.12770
- [x] Wigert, Murugavel, and Reiter-Palmon, "The Utility of Divergent and Convergent Thinking in the Problem Construction Processes During Creative Problem-Solving" - https://doi.org/10.1037/aca0000513
- [x] Leidner et al., "Complementarity in human-AI collaboration: concept, sources, and evidence" - https://doi.org/10.1080/0960085X.2025.2475962
- [x] Princeton AI Agent Reliability Tracker - https://hal.cs.princeton.edu/reliability/
- [x] National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management Framework (AI RMF) - https://doi.org/10.6028/NIST.AI.100-1
- [x] Repo context: `.github/copilot-instructions.md`
- [x] Repo context: `.github/workflows/research-loop.yml`
- [x] Prior completed research cross-check: `Research/completed/2026-03-12-superpowers-integration-analysis.md`
- [x] Prior completed research cross-check: `Research/completed/2026-03-18-explore-to-exploit-synthesis-gap.md`
- [x] Prior completed research cross-check: `Research/completed/2026-03-22-coding-ai-agent-skills-survey.md`
- [x] Prior completed research cross-check: `Research/completed/2026-03-22-applied-context-engineering-agent-workflows.md`
- [x] Community-oriented search on Getting Things Done (GTD) and personal knowledge management - searched via Tavily, but excluded from core findings because most results were vendor blogs with weak independent verification.

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. Sections 0-5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- [fact] Research question restated: the task is to determine how an AI finisher can reliably convert a human's partial ideas into completed, structured, reviewable work without adding a new layer of half-finished output.
- [fact] Scope confirmed: the investigation covers cognitive complementarity, agent roles, handoff and prompt patterns, finishing-specific failure modes, and tool fit under a browser-first GitHub workflow.
- [assumption] Constraint confirmed for this item: the recommended pattern should work in a browser-first GitHub workflow without requiring a local Integrated Development Environment (IDE) or unapproved credentials. Justification: the problem statement for this item explicitly scopes the decision to a no-local-IDE environment.
- [fact] Prior-work cross-reference completed before external investigation. The internal review focused on prior items about superpowers adaptation, explore-to-exploit synthesis, coding agent skills, and applied context engineering.
- [fact] Skill-process fallback applied because the research skill file was absent in this checkout, so the mirrored process in `research-prompt.md` was used instead.
- [fact] Output format confirmed: write a full research record in §§0-§7, then seed `## Findings` directly from §6 without introducing new claims.

### §1 Question Decomposition

1. Human profile and complementarity.
   - 1.1 What published frameworks distinguish divergent work from convergent work?
   - 1.2 What evidence shows that external structure can compensate for limited working-memory or executive-load capacity?
   - 1.3 What does "complementarity" mean in a human-AI division of labour?
2. Agent roles and workflow structure.
   - 2.1 Which roles map best to finishing work: planner, executor, synthesiser, reviewer, organiser?
   - 2.2 Is one autonomous agent sufficient, or do finishing tasks benefit from constrained multi-step workflows?
3. Handoff and prompt design.
   - 3.1 What minimum information must a human provide so the agent can resume unfinished work without intent loss?
   - 3.2 Which artifacts make the handoff persistent rather than conversational and fragile?
4. Tooling fit.
   - 4.1 Which tools fit a no-local-IDE environment?
   - 4.2 Which tools assume Python code, custom runtimes, or deeper orchestration than this operating model supports?
5. Failure modes and limits.
   - 5.1 What reliability problems remain even in strong frontier agents?
   - 5.2 What controls reduce hallucinated completion, intent drift, and over-generalisation?
6. Repo-level recommendations.
   - 6.1 What should this repository change first: skills, instructions, workflows, or framework adoption?
   - 6.2 Which backlog items are justified by the evidence gathered here?

### §2 Investigation

#### 2.1 Human profile and complementarity

Sources consulted:
- Primary: Design Council, Double Diamond - https://www.designcouncil.org.uk/our-resources/the-double-diamond/
- Primary: Risko and Gilbert, "Cognitive Offloading" - https://doi.org/10.1016/j.tics.2016.07.002
- Primary: Berry et al. 2019 - https://doi.org/10.1111/cogs.12770
- Primary: Wigert et al. 2024 - https://doi.org/10.1037/aca0000513
- Primary: Leidner et al. 2025 - https://doi.org/10.1080/0960085X.2025.2475962

Claims:
- [fact] The Double Diamond formalises a repeated expansion-and-narrowing pattern: teams diverge to explore options and converge to define, develop, and deliver a selected direction. Source: Design Council, "The Double Diamond" - https://www.designcouncil.org.uk/our-resources/the-double-diamond/
- [fact] Risko and Gilbert define cognitive offloading as using physical action or environmental structure to reduce the information-processing demands of a task, and they frame it as a common response to cognitive demand. Source: https://doi.org/10.1016/j.tics.2016.07.002
- [fact] Berry et al. found that ordered external structure improved performance for children with lower working-memory ability in a working-memory task, showing that task-relevant environmental arrangement can improve execution on load-sensitive tasks. Source: https://doi.org/10.1111/cogs.12770
- [fact] Wigert et al. report that combining divergent and convergent thinking yields more creative problem construction than using only one mode, supporting a division between idea generation and later selection/refinement. Source: https://doi.org/10.1037/aca0000513
- [fact] Leidner et al. define human-AI complementarity as performance gains that arise from asymmetries in information, capabilities, or processing strengths between humans and AI systems. Source: https://doi.org/10.1080/0960085X.2025.2475962
- [inference] The owner's stated pattern - strong ideation, weak follow-through - maps cleanly onto a divergent/convergent split in which the human contributes direction, pattern recognition, and prioritisation while the agent supplies external structure, persistent memory, and completion discipline. Basis: Double Diamond; cognitive offloading review; Berry et al.; complementarity paper.
- [inference] The strongest theoretical justification for an AI finisher is not that the agent is generally smarter, but that it can externalise sequencing, formatting, cross-checking, and persistence in ways that reduce executive burden on the human. Basis: cognitive offloading sources and complementarity framing.

#### 2.2 Agent roles and workflow patterns

Sources consulted:
- Primary: Anthropic, "Building effective agents" - https://www.anthropic.com/research/building-effective-agents
- Primary: CrewAI docs - https://docs.crewai.com/concepts/agents
- Primary: AutoGen docs - https://microsoft.github.io/autogen/stable/
- Primary: LangGraph docs - https://docs.langchain.com/oss/python/langgraph/overview
- Primary: GitHub Copilot coding agent docs - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

Claims:
- [fact] Anthropic distinguishes workflows from agents: workflows use predefined code paths, while agents dynamically decide how to proceed; Anthropic explicitly recommends starting with the simplest pattern that works and adding complexity only when needed. Source: https://www.anthropic.com/research/building-effective-agents
- [fact] Anthropic identifies prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer as practical workflow patterns for production agentic systems. Source: https://www.anthropic.com/research/building-effective-agents
- [fact] CrewAI presents agents as configurable autonomous units with roles, goals, tools, retries, reasoning flags, and optional delegation; its documentation recommends YAML or code configuration and exposes execution-control parameters such as max iterations and code execution. Source: https://docs.crewai.com/concepts/agents
- [fact] AutoGen describes itself as a framework for building AI agents and applications, with Python packages such as `autogen-agentchat`, `autogen-core`, and a web-based prototyping user interface started from the command line. Source: https://microsoft.github.io/autogen/stable/
- [fact] LangGraph describes itself as a low-level orchestration framework for long-running, stateful agents and explicitly recommends higher-level abstractions when users are just getting started. Source: https://docs.langchain.com/oss/python/langgraph/overview
- [fact] GitHub Copilot coding agent can fix bugs, implement incremental features, improve test coverage, update documentation, and address technical debt in its own ephemeral GitHub Actions-powered development environment. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [inference] A reliable finisher pattern should decompose into at least four roles even when implemented by one underlying agent: planner, executor, synthesiser, and reviewer. Basis: Anthropic workflow taxonomy plus Copilot coding agent's documented ability to run tasks asynchronously and iterate through review.
- [inference] For this use case, evaluator-optimizer and orchestrator-worker patterns are more relevant than open-ended autonomous multi-agent swarms, because finishing depends on iterative refinement against a known goal more than on unconstrained exploration. Basis: Anthropic workflow guidance.
- [inference] Framework-native multi-agent roles are most valuable when a team can write orchestration code, own runtime state, and debug toolchains; that is a weaker fit for a browser-only owner than a GitHub-native agent plus explicit workflow artifacts. Basis: CrewAI, AutoGen, LangGraph, and GitHub docs.

#### 2.3 Handoff and prompt design

Sources consulted:
- Primary: GitHub repository custom instructions docs - https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- Primary: GitHub coding agent overview - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- Primary: GitHub blog, coding agent 101 - https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- Primary: Anthropic, "Building effective agents" - https://www.anthropic.com/research/building-effective-agents
- Primary: Risko and Gilbert 2016 - https://doi.org/10.1016/j.tics.2016.07.002
- Repository sources: `.github/copilot-instructions.md`; `.github/workflows/research-loop.yml`

Claims:
- [fact] GitHub repository custom instructions support repository-wide instructions in `.github/copilot-instructions.md`, path-specific instruction files, and agent instruction files such as `AGENTS.md`. Source: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- [fact] GitHub says Copilot coding agent becomes more effective when the repository contains custom instructions, specialized custom agents, hooks, and skills describing how to build, test, and validate work. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [fact] The GitHub blog describes coding agent as an asynchronous teammate that starts from issues, the agents panel, or chat, then works through a draft pull request (PR) in an ephemeral GitHub Actions environment. Source: https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- [fact] Anthropic recommends transparent planning steps, clear tool documentation, and explicit stopping conditions when building reliable agents. Source: https://www.anthropic.com/research/building-effective-agents
- [fact] GitHub's documented control surfaces already support persistent instruction artifacts and pull-request-centered workflow state machines through custom instructions, skills, custom agents, and review-driven task execution. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [inference] A robust finisher handoff should be treated as a persistent artifact rather than a chat message. The minimum contract is: objective, constraints, definition of done, source materials, allowed tools, validation steps, escalation triggers, and output location. Basis: GitHub custom instructions docs, Anthropic workflow guidance, and the repo's existing durable-instruction pattern.
- [inference] The handoff artifact acts as cognitive offloading for the human and intent anchoring for the agent, because it moves fragile task state out of working memory and into a stable environment the agent can revisit. Basis: Risko and Gilbert 2016; Berry et al. 2019; GitHub instruction model.
- [inference] The highest-value prompt pattern for finishers is not "be more proactive" but "work through these checkpoints and stop if any checkpoint fails," because completion reliability depends on explicit gates rather than motivational tone. Basis: Anthropic evaluator-optimizer pattern; repo workflow controls.

#### 2.4 Tooling fit under a browser-first GitHub operating model

Sources consulted:
- Primary: GitHub Copilot coding agent docs - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- Primary: GitHub coding agent how-to index - https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
- Primary: GitHub blog, coding agent 101 - https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- Primary: CrewAI docs - https://docs.crewai.com/concepts/agents
- Primary: AutoGen docs - https://microsoft.github.io/autogen/stable/
- Primary: LangGraph docs - https://docs.langchain.com/oss/python/langgraph/overview

Claims:
- [fact] GitHub Copilot coding agent works directly on GitHub, opens pull requests, iterates via review comments, and runs in GitHub Actions-backed ephemeral environments. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [fact] GitHub's how-to documentation says tasks can be initiated from GitHub issues, the agents panel, GitHub Mobile, chat surfaces, the Command Line Interface (CLI), and integrations, which matches the owner's no-local-IDE operating model better than IDE-tethered approaches. Source: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- [fact] CrewAI, AutoGen, and LangGraph all assume programmable orchestration, package installation, and owned runtime surfaces rather than a pure GitHub-web operating model. Sources: https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [fact] LangGraph explicitly positions itself as low-level infrastructure for stateful agents, and AutoGen exposes Python packages and command-line setup even for its web-based prototyping surface. Sources: https://docs.langchain.com/oss/python/langgraph/overview; https://microsoft.github.io/autogen/stable/
- [inference] GitHub Copilot coding agent is the best default finisher tool for this repository because it matches the delivery surface, authentication model, review process, and artifact flow the owner already uses. Basis: GitHub docs plus repo operating constraints.
- [inference] CrewAI, AutoGen, and LangGraph are better understood here as reference architectures for future deeper automation, not as first-line tools for immediate owner-facing finishing work. Basis: framework docs and the repository's browser-only constraint.
- [assumption] If the owner later wants richer multi-agent orchestration beyond GitHub-native flows, that work would require additional runtime ownership and possibly capability confirmations that are outside the currently documented credential set. Justification: richer orchestration would require runtime ownership and capability confirmations that are outside the currently stated operating model for this item.

#### 2.5 Failure modes, controls, and practical limits

Sources consulted:
- Primary: Princeton AI Agent Reliability Tracker - https://hal.cs.princeton.edu/reliability/
- Primary: NIST AI RMF - https://doi.org/10.6028/NIST.AI.100-1
- Primary: Anthropic, "Building effective agents" - https://www.anthropic.com/research/building-effective-agents
- Primary: GitHub Copilot coding agent docs - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

Claims:
- [fact] The Princeton AI Agent Reliability Tracker finds that reliability has improved only modestly relative to capability gains, and that consistency, predictability, and prompt robustness remain distinct problems even for strong frontier agents. Source: https://hal.cs.princeton.edu/reliability/
- [fact] The Princeton AI Agent Reliability Tracker specifically recommends multi-run evaluation, multi-condition perturbation, and deployment governance that distinguishes augmentation use cases from automation use cases. Source: https://hal.cs.princeton.edu/reliability/
- [fact] NIST describes the Artificial Intelligence Risk Management Framework (AI RMF) as a voluntary framework for incorporating trustworthiness into the design, development, use, and evaluation of AI systems. Source: https://doi.org/10.6028/NIST.AI.100-1
- [fact] Anthropic states that agents trade latency and cost for performance, and that autonomous agents are best reserved for open-ended problems where operators have enough trust in model decision-making plus appropriate guardrails. Source: https://www.anthropic.com/research/building-effective-agents
- [fact] GitHub's coding agent keeps human review in the loop by opening pull requests for review rather than shipping directly to production. Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [inference] The main failure modes for an AI finisher are not only fabrication and factual hallucination, but also premature closure, loss of original intent, and confidence without consistency. Basis: the Princeton AI Agent Reliability Tracker findings, Anthropic guardrail guidance, and the reviewed GitHub operating pattern.
- [inference] The strongest mitigations are bounded tasks, explicit done criteria, validation commands, durable handoff artifacts, reviewer loops, and escalation rules that force the agent to stop instead of inventing certainty. Basis: the Princeton AI Agent Reliability Tracker recommendations, NIST trustworthiness framing, Anthropic workflow guidance, and GitHub pull-request-based review.
- [inference] Full autonomy is a poor fit for ambiguous personal synthesis tasks where success is difficult to verify mechanically; the complementary model works best when the human still owns intent, prioritisation, and final acceptance. Basis: the Princeton AI Agent Reliability Tracker augmentation-vs-automation guidance; Anthropic on verifiable coding tasks.

#### 2.6 Repo-level implications and candidate backlog items

Sources consulted:
- Repository sources: `.github/copilot-instructions.md`; `.github/workflows/research-loop.yml`
- External support: GitHub custom instructions docs; Anthropic workflow patterns; GitHub coding agent docs

Claims:
- [fact] A GitHub-native finisher pattern can be built from durable instructions, GitHub-native automation, explicit state transitions, and review workflows. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
- [inference] The next increment should be to formalise the handoff contract rather than introduce a new orchestration framework, because the repo's bottleneck is disciplined completion, not raw agent capability. Basis: sections 2.1-2.5 above.
- [inference] Three justified backlog directions emerge: a reusable finisher-handoff template, a reviewer/evaluator skill that focuses on completion criteria and intent preservation, and a GitHub-native issue-to-finish workflow for bounded repo-maintenance tasks. Basis: repository context plus the evidence above.

### §3 Reasoning

- [inference] The evidence supports a complementarity model built on asymmetry of strengths, not a replacement model. Humans contribute goals, taste, and strategic judgment; agents contribute persistence, formatting discipline, iterative execution, and cross-checking. Basis: Leidner et al.; cognitive offloading literature; GitHub and Anthropic workflow evidence.
- [inference] Because finishing is convergent work, reliability matters more than novelty. Therefore the best architecture is one that narrows agent freedom with checkpoints, artifacts, and evaluation rather than maximizing autonomous exploration. Basis: divergent/convergent sources; Anthropic workflow guidance; the Princeton AI Agent Reliability Tracker findings.
- [inference] GitHub-native agents dominate custom orchestration frameworks for the owner's current operating model because they minimize setup burden and maximize compatibility with how work is already reviewed and accepted. Basis: GitHub docs versus CrewAI/AutoGen/LangGraph docs.
- [inference] The correct human-agent handoff is closer to a lightweight operating procedure than a conversational prompt, because persistence and validation are what convert ideation into completion. Basis: repository patterns and cognitive offloading evidence.
- [assumption] The owner's main unmet need is disciplined finish-through rather than high-scale autonomous delegation across many systems. Justification: item context and repository operating model.

### §4 Consistency Check

- [fact] No source-level contradiction was found on the central tooling question. GitHub sources consistently describe an asynchronous, pull-request-based agent model, while CrewAI, AutoGen, and LangGraph consistently describe programmable orchestration frameworks rather than GitHub-native delegation surfaces. Sources: GitHub, CrewAI, AutoGen, and LangGraph docs.
- [fact] No contradiction was found between the cognition literature and the tooling literature. The cognition sources recommend external structure to reduce executive load, and the tooling sources identify durable instructions, workflow gates, and explicit artifacts as the mechanisms that provide that structure. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://www.anthropic.com/research/building-effective-agents.
- [inference] The only meaningful tension is between agent flexibility and reliability: richer autonomy can cover more cases, but the available reliability evidence shows that consistency and predictability still lag raw capability. Basis: Anthropic guidance and the Princeton AI Agent Reliability Tracker results.
- [inference] That tension is resolved for this item by prioritising bounded completion over maximum autonomy, which matches both the owner context and the stronger evidence base. Basis: sections 2.2-2.5.

### §5 Depth and Breadth Expansion

- [inference] From a technical lens, the finisher role is best implemented as a state machine with explicit transitions such as intake -> plan -> execute -> validate -> synthesize -> review, because stateful checkpoints reduce ambiguity and make failures observable. Basis: Anthropic workflow patterns and the repo's state-machine practice.
- [inference] From a behavioural lens, the finisher agent's value is partly motivational: it converts intention into visible progress artifacts, which reduces the psychic cost of returning to unfinished work. Basis: cognitive offloading framing and durable-instruction practice.
- [inference] From an economic lens, GitHub-native finishing has lower coordination cost than introducing a bespoke orchestration stack, because it reuses existing authentication, review, branch, and automation infrastructure. Basis: GitHub docs and framework setup assumptions.
- [fact] GitHub's documented instruction, skills, hooks, and custom-agent surfaces provide durable operating artifacts that support repeatable finisher behaviour better than ad hoc prompting alone. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
- [inference] From a governance lens, the complementary model stays credible only while the human continues to own intent, acceptance, and exception handling. If those are delegated too early, the failure modes shift from incomplete work to confidently wrong work. Basis: the Princeton AI Agent Reliability Tracker guidance; NIST AI RMF; GitHub review workflow.

### §6 Synthesis

**Executive summary:**

- [inference] The best-supported way to use an AI finisher for an ideation-strong, execution-weak human is a constrained GitHub-native workflow in which the human sets intent and acceptance criteria, while the agent plans, executes, validates, and synthesises bounded tasks inside reviewable pull requests. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://www.anthropic.com/research/building-effective-agents; https://hal.cs.princeton.edu/reliability/
- [inference] The complementary advantage comes from externalising executive-load work - sequencing, remembering constraints, checking completion, and packaging outputs - rather than from giving the agent unconstrained autonomy. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://doi.org/10.1080/0960085X.2025.2475962
- [inference] For this repository's browser-only operating model, GitHub Copilot coding agent and GitHub-native workflow artifacts are a substantially better fit than CrewAI, AutoGen, or LangGraph as first-line finishing tools, because those frameworks assume programmable orchestration and runtime ownership that the owner does not currently use. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [inference] The practical limit is reliability: current agents still vary too much in consistency and prompt robustness to be trusted as fully autonomous finishers for ambiguous work, so human review and explicit stop conditions remain mandatory. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1

**Key findings:**

1. [inference][high] The most reliable finisher pattern is not a single free-form autonomous helper, but a bounded workflow in which one agent or one agentic surface plays planner, executor, synthesiser, and reviewer roles against explicit acceptance criteria. Sources: https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
2. [inference][high] Human-AI complementarity is strongest when the human retains divergent work such as goal selection and judgment, while the agent absorbs convergent work such as structuring, sequencing, packaging, and completeness checking. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://doi.org/10.1037/aca0000513
3. [inference][high] Persistent handoff artifacts outperform conversational prompts for unfinished work because they offload memory demands, preserve intent across time, and give the agent an auditable contract for what completion means. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
4. [fact][high] GitHub Copilot coding agent is purpose-built for asynchronous GitHub-based completion work, whereas CrewAI, AutoGen, and LangGraph are programmable frameworks that assume code-level orchestration and runtime ownership. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
5. [inference][medium] For the owner's no-local-IDE workflow, adopting GitHub-native instructions, review loops, and workflow gates will yield more immediate finishing value than introducing a bespoke multi-agent framework. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/; https://www.anthropic.com/research/building-effective-agents
6. [fact][high] Current frontier agents still exhibit meaningful gaps between accuracy and reliability, especially on consistency, predictability, and prompt robustness, which makes unchecked autonomous finishing unsafe for ambiguous tasks. Sources: https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents
7. [inference][high] The best practical control set is: bounded scope, explicit done definition, validation commands, reviewable output artifacts, escalation triggers, and human acceptance at the final gate. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
8. [fact][medium] GitHub exposes several repository-level control surfaces - including custom instructions, agent instruction files, skills, hooks, and custom agents - so finisher behaviour can be tuned incrementally without first migrating to a different platform. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Bounded planner-executor-synthesiser-reviewer workflow beats unconstrained autonomy for finishing tasks. | https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | high | Supported by first-party workflow guidance and GitHub review model. |
| [inference] Complementarity is strongest when humans stay on divergent work and agents take convergent work. | https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://doi.org/10.1037/aca0000513 | high | Convergent/divergent split plus formal complementarity framing. |
| [inference] Persistent handoff artifacts reduce intent loss and executive burden. | https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions | high | Cognitive offloading plus durable repository instructions. |
| [inference] GitHub Copilot coding agent fits browser-only finishing better than CrewAI, AutoGen, or LangGraph. | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview | high | Direct capability and operating-model comparison. |
| [inference] Repository instructions, handoff contracts, and reviewer gates should be improved before bespoke multi-agent orchestration is introduced. | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/; https://www.anthropic.com/research/building-effective-agents | medium | [inference] First-party workflow guidance supports this rollout order. |
| [inference] Reliability limits still block full autonomy for ambiguous work. | https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents | high | Reliability dimensions lag raw capability. |
| [inference] Completion control should rely on explicit done criteria, validation, review, and escalation. | https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | high | Governance and deployment controls align across sources. |
| [fact] Finisher behaviour can be improved through additive repository artifacts such as instructions, skills, hooks, and custom agents. | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | medium | [fact] GitHub documents several repository-level control surfaces for behaviour shaping. |

**Assumptions:**

- [assumption] The initial deployment target is bounded repository or document work that can be expressed as an issue, task brief, or section-level deliverable rather than as open-ended personal decision-making. **Justification:** GitHub coding agent and the Princeton AI Agent Reliability Tracker are both strongest for bounded, reviewable tasks. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://hal.cs.princeton.edu/reliability/
- [assumption] The operator is willing to keep human review at the final acceptance gate instead of delegating irreversible decisions to the agent. **Justification:** GitHub coding agent and the NIST framework both assume meaningful human oversight for trustworthy deployment. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://doi.org/10.6028/NIST.AI.100-1
- [assumption] A good outcome means higher completion throughput with bounded risk, not maximum agent autonomy. **Justification:** Anthropic and the Princeton AI Agent Reliability Tracker both treat reliability and controllability as first-order deployment criteria, not optional extras. Sources: https://www.anthropic.com/research/building-effective-agents; https://hal.cs.princeton.edu/reliability/

**Analysis:**

- [inference] The evidence converges on a simple rule: use the agent to finish what is already conceptually shaped, not to decide what should matter. The human should still choose goals, judge trade-offs, and accept outcomes. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents
- [inference] The useful architecture is therefore an augmentation architecture, not an automation architecture. GitHub's pull-request-based agent loop is a concrete implementation of augmentation because it keeps changes reviewable and visible. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://hal.cs.princeton.edu/reliability/
- [inference] Frameworks such as CrewAI, AutoGen, and LangGraph are not wrong for finishing work, but they are second-step tools in this pattern. They become attractive only after a team proves that its handoff contract, completion rubric, and reviewer loop work consistently in the simpler GitHub-native form. Sources: https://www.anthropic.com/research/building-effective-agents; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [inference] The cognitive literature matters because it explains why this division of labour is useful. The agent is not merely faster; it is functioning as an externalised execution scaffold. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770

**Risks, gaps, uncertainties:**

- [fact] The reliability evidence is still benchmark-heavy and does not provide a single universal threshold for when a finisher can be trusted without review. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1
- [inference] The published evidence reviewed here is stronger on coding and structured completion than on general personal productivity finishing, so the recommendations are best grounded for repository work rather than all life-admin tasks. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://www.anthropic.com/research/building-effective-agents; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [inference] The complementarity literature in this review is newer and thinner than the workflow/tooling literature, so the psychological framing should be treated as supportive rather than exhaustive. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://www.anthropic.com/research/building-effective-agents

**Open questions:**

- [inference] What is the smallest reusable handoff template that reliably preserves intent across repo tasks such as research, backlog grooming, and workflow maintenance?
- [inference] Should the reviewer role be encoded as a dedicated repository skill focused on completion criteria, or as a path-specific instruction file for GitHub-native agents?
- [inference] At what point does this repository have enough repeated finishing demand to justify a deeper custom-agent or multi-agent orchestration layer?
- [inference] How should non-code finishing work - such as synthesis across multiple completed research items - be validated when automated tests are unavailable?

### §7 Recursive Review

- [inference] The recursive review did not overturn the core conclusion: bounded GitHub-native finishing, durable handoff artifacts, and mandatory human review remain the best-supported pattern across the cognition, tooling, and reliability evidence. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://hal.cs.princeton.edu/reliability/
- [inference] The remaining uncertainty is about rollout sequence and scope, not about whether the complementary model is directionally correct, because the source base is stronger on control mechanisms than on any case for unchecked autonomy. Sources: https://www.anthropic.com/research/building-effective-agents; https://doi.org/10.6028/NIST.AI.100-1; https://hal.cs.princeton.edu/reliability/
- [fact] Acronym expansion audit completed for the terms introduced in the Research Skill Output and Findings, including Artificial Intelligence (AI), Application Programming Interface (API), Large Language Model (LLM), Integrated Development Environment (IDE), Command Line Interface (CLI), pull request (PR), and Artificial Intelligence Risk Management Framework (AI RMF).

---

## Findings

### Executive Summary

- [inference] Artificial Intelligence (AI) finishers are most dependable when they operate inside bounded GitHub-native tasks, because the agent can handle planning, execution, validation, and packaging while the human keeps scoping authority and final sign-off. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://www.anthropic.com/research/building-effective-agents; https://hal.cs.princeton.edu/reliability/
- [inference] The key mechanism is cognitive complementarity: the human provides divergent thinking, judgment, and prioritisation, while the agent externalises convergent work such as sequencing, formatting, cross-checking, and synthesis into durable artifacts. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://doi.org/10.1016/j.tics.2016.07.002
- [inference] In a browser-first repository workflow, the GitHub-native agent surface fits sooner than CrewAI, AutoGen, or LangGraph, because it reuses existing issues, pull requests, instructions, and review gates instead of requiring a separate programmable runtime. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [inference] The main practical limit is reliability rather than raw capability, so the model remains complementary rather than autonomous: bounded scope, explicit done criteria, validation, and human review are mandatory controls rather than optional extras. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1

### Key Findings

1. [inference][high] A reliable finisher architecture uses an explicit planner-executor-synthesiser-reviewer loop, because completion quality improves when planning, doing, packaging, and checking are treated as distinct responsibilities rather than collapsed into one unconstrained conversational turn. Sources: https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
2. [inference][high] Human-AI complementarity is strongest when the human keeps ownership of divergent tasks such as choosing goals and making trade-offs, while the agent takes convergent tasks such as structuring, sequencing, packaging, and verifying completeness against stated criteria. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://doi.org/10.1037/aca0000513
3. [inference][high] Persistent handoff artifacts are more dependable than conversational memory for unfinished work because they offload executive burden, preserve intent over time, and give the agent a stable contract describing constraints, sources, validation, and stop conditions. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
4. [inference][high] GitHub Copilot coding agent is directly aligned with browser-first GitHub workflows, while CrewAI, AutoGen, and LangGraph are primarily frameworks for teams that can install packages, write orchestration code, and operate custom runtime state. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
5. [inference][medium] The fastest practical path in a browser-first GitHub workflow is to strengthen repository instructions, handoff contracts, and reviewer gates before experimenting with bespoke multi-agent frameworks, because the largest immediate gains come from clearer completion discipline rather than from deeper orchestration. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/; https://www.anthropic.com/research/building-effective-agents
6. [inference][high] Frontier agents still show meaningful reliability gaps on consistency, predictability, and prompt robustness, so fully autonomous finishing remains inappropriate for ambiguous tasks where success cannot be checked by tests, review, or hard acceptance criteria. Sources: https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents
7. [inference][high] The most effective control stack for a finisher agent is bounded scope, explicit definition of done, executable validation steps, reviewable output artifacts, escalation rules, and human acceptance at the final gate, because each control targets a different failure mode in the completion loop. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
8. [fact][medium] GitHub exposes several repository-level control surfaces - including custom instructions, agent instruction files, skills, hooks, and custom agents - so finisher behaviour can be tuned incrementally without first migrating to a different platform. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Explicit planner-executor-synthesiser-reviewer loops improve finishing reliability. | https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | high | [fact] Supported by first-party workflow patterns and the GitHub review surface. |
| [inference] Complementarity works best when humans stay on divergent work and agents take convergent work. | https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://doi.org/10.1037/aca0000513 | high | [inference] Theory and process evidence align. |
| [inference] Durable handoff artifacts reduce intent loss and executive burden. | https://doi.org/10.1016/j.tics.2016.07.002; https://doi.org/10.1111/cogs.12770; https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions | high | [inference] Cognitive offloading and repository-instruction mechanisms point in the same direction. |
| [inference] GitHub Copilot coding agent fits browser-only finishing better than CrewAI, AutoGen, or LangGraph. | https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview | high | [fact] Tooling capabilities and operating assumptions differ clearly. |
| [inference] Repository instructions, handoff contracts, and reviewer gates should be improved before bespoke multi-agent orchestration is introduced. | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/; https://www.anthropic.com/research/building-effective-agents | medium | [inference] First-party workflow guidance supports this rollout order. |
| [inference] Reliability gaps still prevent unchecked autonomous finishing for ambiguous work. | https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents | high | [fact] Consistency and prompt robustness remain unresolved. |
| [inference] Bounded scope, validation, review, and escalation are the right completion controls. | https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | high | [inference] Governance and workflow controls converge on the same safeguards. |
| [fact] Finisher behaviour can be improved through additive repository artifacts such as instructions, skills, hooks, and custom agents. | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent | medium | [fact] GitHub documents several repository-level control surfaces for behaviour shaping. |

### Assumptions

- [assumption] The initial deployment target is bounded repository or document work that can be expressed as an issue, task brief, or section-level deliverable rather than as open-ended personal decision-making. **Justification:** GitHub coding agent and the Princeton AI Agent Reliability Tracker are both strongest for bounded, reviewable tasks. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://hal.cs.princeton.edu/reliability/
- [assumption] The operator is willing to keep human review at the final acceptance gate instead of delegating irreversible decisions to the agent. **Justification:** GitHub coding agent and the NIST framework both assume meaningful human oversight for trustworthy deployment. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://doi.org/10.6028/NIST.AI.100-1
- [assumption] A good outcome means higher completion throughput with bounded risk, not maximum agent autonomy. **Justification:** Anthropic and the Princeton AI Agent Reliability Tracker both treat reliability and controllability as first-order deployment criteria, not optional extras. Sources: https://www.anthropic.com/research/building-effective-agents; https://hal.cs.princeton.edu/reliability/

### Analysis

[inference] The evidence does not support the naive idea that an ideation-heavy human simply needs "a stronger agent." It supports a more specific design: the human keeps problem framing and acceptance, while the agent becomes an execution scaffold that turns intent into artifacts, checks, and structured outputs. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://doi.org/10.1016/j.tics.2016.07.002; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

[inference] That is why GitHub-native finishing is the best present fit. It packages work as issues, pull requests, comments, instructions, and workflow states - exactly the kinds of durable objects that both humans and agents can revisit without relying on conversational memory. Sources: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions; https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

[inference] The larger orchestration frameworks still matter, but as second-order options. They become attractive only after the repository has proven a stable handoff contract and completion rubric, because otherwise they would automate ambiguity rather than reduce it. Sources: https://www.anthropic.com/research/building-effective-agents; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview

[inference] The main architectural principle is therefore: maximise external structure before maximising autonomy. In this domain, better completion comes from clearer contracts and reviews before it comes from more elaborate agent topologies. Sources: https://doi.org/10.1016/j.tics.2016.07.002; https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1

### Risks, Gaps, and Uncertainties

- [fact] Reliability evidence is still evolving and does not supply a universal threshold at which an agent can be trusted to finish ambiguous tasks without review. Sources: https://hal.cs.princeton.edu/reliability/; https://doi.org/10.6028/NIST.AI.100-1
- [inference] The public evidence base is stronger for coding and structured completion than for personal productivity or personal knowledge management finishing, so these conclusions are strongest for repository workflows. Sources: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent; https://www.anthropic.com/research/building-effective-agents; https://docs.crewai.com/concepts/agents; https://microsoft.github.io/autogen/stable/; https://docs.langchain.com/oss/python/langgraph/overview
- [inference] The complementarity literature is newer and less extensive than the tooling literature, so the psychological explanation should be treated as supportive framing rather than closed theory. Sources: https://doi.org/10.1080/0960085X.2025.2475962; https://www.designcouncil.org.uk/our-resources/the-double-diamond/; https://www.anthropic.com/research/building-effective-agents
- [inference] The exact threshold at which this repo should graduate from GitHub-native finishing to custom multi-agent orchestration remains uncertain and should be decided empirically after a simpler finisher contract is piloted. Sources: https://hal.cs.princeton.edu/reliability/; https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent

### Open Questions

- [inference] What is the smallest reusable handoff template that reliably preserves intent across research, repo-maintenance, and backlog-management tasks in this repository?
- [inference] Should completion review be implemented as a dedicated repository skill, as path-specific GitHub instructions, or as a workflow-enforced checklist?
- [inference] How should non-code finishing work be validated when there are no automated tests and the main risks are synthesis drift and premature closure?
- [inference] When, if ever, would it become worthwhile to add a deeper CrewAI, AutoGen, or LangGraph orchestration layer on top of the current GitHub-native workflow?

---

## Output

- Type: knowledge, backlog-item
- Description: Completed a research synthesis showing that the highest-fit "AI finisher" model for this repository is a bounded GitHub-native workflow with explicit handoff contracts, planner/executor/synthesiser/reviewer responsibilities, and mandatory human review; identified three justified follow-on backlog directions: a reusable finisher-handoff template, a completion-review skill or instruction set, and a GitHub-native issue-to-finish workflow for bounded tasks.
- Links:
  - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
  - https://www.anthropic.com/research/building-effective-agents
  - https://hal.cs.princeton.edu/reliability/