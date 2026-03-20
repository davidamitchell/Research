---
review_count: 1
title: "Intent Driven Development: context and concept layering to bound the solution space"
added: 2026-03-16
status: completed
priority: high  # low | medium | high
blocks: []
tags: [intent, software-engineering, test-driven-development, specification-driven-development, context-layering, agentic-coding, artificial-intelligence, developer-tooling, design-methodology]
started: 2026-03-20
completed: 2026-03-20
output: [knowledge]
---

# Intent Driven Development: context and concept layering to bound the solution space

## Research Question

What is Intent Driven Development (IDD) — as a methodology that moves past Test Driven Development (TDD) and Specification Driven Development (SDD) — and what context and concept layering mechanisms are required to sufficiently bound the potential solution space so that Artificial Intelligence (AI) coding agents produce outputs that are aligned with developer and organisational intent?

Supporting questions:
- What is IDD? Is it a named methodology, an emergent practice, or a set of loosely related ideas? Who coined it or is actively defining it?
- How does IDD differ from TDD and SDD? What does each paradigm use as its primary constraint on the solution space, and where does each break down with AI-assisted development?
- What does StrongDM Factory (https://factory.strongdm.ai/) represent as a concrete implementation of intent-driven principles in infrastructure and access management? What can be generalised?
- What is the structure of a complete "intent layer"? What artefacts (natural language, formal specs, constraints, examples, policies) are needed and in what combination?
- How do concept layering and context architecture interact with intent? What are the relevant findings from context-compression and aligned decision-making research?
- What does the Hacker News (HN) community (https://news.ycombinator.com/item?id=46924426) identify as the key challenges, precedents, and open problems in intent-driven approaches?

## Scope

**In scope:**
- Definition and characterisation of Intent Driven Development (IDD) as a software engineering methodology
- Comparison of TDD, SDD, and Design by Contract (DbC): what each uses as a primary constraint, where each applies, and where each fails
- StrongDM Factory as a concrete implementation: what it does, what principles it embodies, and what is generalisable
- Artefact types that encode intent: natural-language specifications, property-based tests, type-level constraints, contracts (including Ricardian Contract model from `2026-03-14-ricardian-contract-model`), policy rules, and worked examples
- Context and concept layering: how the hierarchical context model from `2026-03-15-context-layers-aligned-decisions-synthesis` applies to bounding the agent solution space
- Agent policy enforcement: relationship to the Language Server Protocol (LSP)-style guidance from `2026-03-01-agent-lsp-policy-enforcement`
- Formal methods and reliability: relationship to findings from `2026-03-14-reliable-software-llm-era` on cognitive debt and formal specification
- Practitioner discourse: Hacker News thread and related community discussion

**Out of scope:**
- Full implementation of an IDD toolchain or framework (this is a research item, not an engineering item)
- Detailed reinvestigation of topics already covered in the prerequisite completed items above
- General Large Language Model (LLM) benchmarking or capability comparison unrelated to intent alignment

**Constraints:** Publicly accessible sources. Build primarily on the completed prior research referenced above, supplemented by web search for current practitioner work and the HN thread. Prefer 2023–2026 sources to reflect the current AI-assisted development context.

## Context

Test Driven Development constrains the solution space via executable tests: code is correct if and only if it passes the tests. This works well when the test suite is complete and the problem is well-bounded. Specification Driven Development (and the related Design by Contract (DbC) school) constrains via formal or semi-formal contracts: preconditions, postconditions, and invariants. Both approaches are fundamentally reactive — they detect violations after code has been produced, or guide code towards satisfying a pre-written constraint set.

With AI coding agents, the failure mode changes. An agent can produce code that satisfies every test and every contract while still being wrong — because the tests and contracts themselves were incomplete, ambiguous, or misaligned with the actual intent of the developer or organisation. The question is no longer "does the code pass the spec?" but "does the code embody what the developer actually meant?"

Intent Driven Development (IDD) proposes intent as the primary input: the developer (or organisation) expresses *what they want to achieve*, in sufficient richness that the solution space is bounded without being over-specified. The challenge is that intent is harder to formalise than a test or a contract. It requires:
1. **Concept layering** — decomposing intent from high-level goals (organisational strategy, domain model) down to immediate task requirements, without losing coherence at each layer.
2. **Context architecture** — ensuring the right subset of that layered context is available at inference time, given finite context windows.
3. **Policy enforcement** — encoding constraints derived from intent (security posture, architecture governance, team norms) as enforceable rules the agent must satisfy in real time.

This item connects prior research threads: the context architecture work (`2026-03-15-context-layers-aligned-decisions-synthesis`), agent policy enforcement (`2026-03-01-agent-lsp-policy-enforcement`), formal reliability methods (`2026-03-14-reliable-software-llm-era`), and machine-readable contract models (`2026-03-14-ricardian-contract-model`). The synthesis question is: what does a complete IDD stack look like, and which components are production-ready versus still open problems?

## Approach

1. **Define the landscape** — search for "intent driven development" as a named methodology: who defines it, what artefacts it requires, and how it is distinguished from TDD and SDD. Start with the HN thread and StrongDM Factory documentation.
2. **Comparative analysis** — construct a comparison table: TDD vs. SDD/DbC vs. IDD, on axes of: primary constraint artefact, failure mode with AI agents, solution space bound mechanism, verification approach, and tooling maturity.
3. **StrongDM Factory deep dive** — analyse the StrongDM Factory product (https://factory.strongdm.ai/) as a concrete IDD implementation in the access management and infrastructure space. What intent artefacts does it require? What context layering does it implement? What can be generalised to other domains?
4. **Intent artefact taxonomy** — synthesise the types of artefact that encode intent: natural-language user stories, property-based tests, type-level constraints, formal contracts, policy-as-code rules, worked examples, architectural decision records, and organisational context documents. Which artefacts are necessary versus sufficient? What combination produces a bounded solution space?
5. **Context layering mapping** — map the intent artefact taxonomy onto the layered context architecture from `2026-03-15-context-layers-aligned-decisions-synthesis`. At which layer does each artefact type belong? How is it stored, retrieved, and composed at inference time?
6. **Gap analysis** — identify which components of the IDD stack are production-ready and which are open problems. What tooling, protocols, or standards are missing?
7. **Synthesis** — produce the Executive Summary, Key Findings, and Evidence Map.

## Sources

- [x] Hacker News (HN) thread on intent-driven development — https://news.ycombinator.com/item?id=46924426
- [x] StrongDM Factory main page — https://factory.strongdm.ai/
- [x] StrongDM Factory principles — https://factory.strongdm.ai/principles
- [x] StrongDM Factory techniques — https://factory.strongdm.ai/techniques
- [x] StrongDM Factory products — https://factory.strongdm.ai/products
- [x] StrongDM Attractor README — https://raw.githubusercontent.com/strongdm/attractor/main/README.md
- [x] StrongDM Attractor specification — https://raw.githubusercontent.com/strongdm/attractor/main/attractor-spec.md
- [x] StrongDM coding agent loop specification — https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md
- [x] AttractorBench README — https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md
- [x] Keyhole Software — "Intent-Driven Development: A Modern SDLC for AI-Accelerated Teams" — https://keyholesoftware.com/intent-driven-development-build-first-documentation/
- [x] Martin Fowler — "Test-Driven Development" — https://martinfowler.com/bliki/TestDrivenDevelopment.html
- [x] Eiffel documentation — "Design by Contract basics" — https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405
- [x] Prior completed research: `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md`
- [x] Prior completed research: `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [x] Prior completed research: `Research/completed/2026-03-14-reliable-software-llm-era.md`
- [x] Prior completed research: `Research/completed/2026-03-14-ricardian-contract-model.md`
- [x] Prior completed research: `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md`
- [ ] Amazon Web Services (AWS) — AI-driven development life cycle article linked from Keyhole — https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- [ ] Microsoft Azure Apps on Azure blog — AI-led SDLC article linked from Keyhole — https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is Intent Driven Development (IDD) in the era of AI coding agents, how does it differ from Test Driven Development (TDD) and Specification Driven Development (SDD) / Design by Contract (DbC), what does StrongDM Factory show as a concrete implementation, and what layered artefacts are required to keep agent output aligned with developer and organisational intent?

**Scope confirmed:** In scope are public definitions and practitioner descriptions of IDD, comparison with TDD and DbC, StrongDM Factory and its open specifications, the artefact stack required to encode intent, the relationship to layered context architecture and in-loop policy enforcement, and a production-readiness gap analysis. Out of scope are building a full toolchain, re-running the full prior research items, and general Large Language Model (LLM) capability debates unrelated to intent alignment.

**Constraint mode:** Full.

**Output format:** Full research item with §§0–7 completed, followed by Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, Open Questions, and Output.

**Prior work cross-reference:**
- [fact] `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md` established an eight-layer context hierarchy and is directly relevant to how intent should be stored and served.
- [fact] `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` established that real-time policy guidance is most feasible today through in-loop diagnostics and tool-mediated feedback rather than post-commit gates alone.
- [fact] `Research/completed/2026-03-14-reliable-software-llm-era.md` showed that formal specification becomes most useful when humans validate the specification and deterministic tools validate behavior before code generation.
- [fact] `Research/completed/2026-03-14-ricardian-contract-model.md` documented the prose-plus-code-plus-parameters pattern, which is directly relevant to intent encoding.
- [fact] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` mapped the broader specification hierarchy and provides the baseline for comparing TDD, DbC, and IDD.

### §1 Question Decomposition

**Top-level question:** What artefact and context architecture turns "intent" into a practical constraint on AI coding agents, and how is that different from test-first or contract-first methods?

**A. Definition landscape**
- A1. Is Intent Driven Development (IDD) a stable named methodology with a canonical source, or an emerging umbrella term used by multiple practitioners?
- A2. What common core appears across the public descriptions that were consulted?
- A3. What evidence suggests that public implementations still depend on detailed specifications rather than on short natural-language prompts alone?

**B. Comparison with older constraint regimes**
- B1. What is the primary constraint artefact in Test Driven Development (TDD)?
- B2. What is the primary constraint artefact in Specification Driven Development (SDD) / Design by Contract (DbC)?
- B3. What does IDD add above tests and contracts when AI agents are doing substantial implementation work?
- B4. Where does each regime fail when the specification is incomplete or gameable?

**C. StrongDM Factory as a concrete implementation**
- C1. What artefacts does StrongDM actually provide publicly?
- C2. How do scenarios, satisfaction, and the Digital Twin Universe (DTU) function in the StrongDM model?
- C3. Which StrongDM elements generalise beyond StrongDM's "no human code" doctrine?
- C4. What criticisms or caveats appear in practitioner discussion?

**D. Intent artefact taxonomy**
- D1. Which artefacts encode goals, boundaries, and success criteria?
- D2. Which artefacts encode executable correctness constraints?
- D3. Which artefacts encode architecture, policy, and organisational context?
- D4. Which artefacts appear necessary, and which only strengthen the stack?

**E. Context layering and enforcement**
- E1. At what layers should intent artefacts live?
- E2. Which layers should be persistent core context versus retrieved or compressed on demand?
- E3. How should policy enforcement interact with intent in the agent loop?

**F. Gap analysis**
- F1. Which components of an IDD stack are publicly production-ready today?
- F2. Which components remain open problems or weakly evidenced?

### §2 Investigation

**Consulted sources**
- [x] https://factory.strongdm.ai/
- [x] https://factory.strongdm.ai/principles
- [x] https://factory.strongdm.ai/techniques
- [x] https://factory.strongdm.ai/products
- [x] https://news.ycombinator.com/item?id=46924426
- [x] https://raw.githubusercontent.com/strongdm/attractor/main/README.md
- [x] https://raw.githubusercontent.com/strongdm/attractor/main/attractor-spec.md
- [x] https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md
- [x] https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md
- [x] https://keyholesoftware.com/intent-driven-development-build-first-documentation/
- [x] https://martinfowler.com/bliki/TestDrivenDevelopment.html
- [x] https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405
- [x] `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md`
- [x] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [x] `Research/completed/2026-03-14-reliable-software-llm-era.md`
- [x] `Research/completed/2026-03-14-ricardian-contract-model.md`
- [x] `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md`

**Identified but not consulted**
- [ ] https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- [ ] https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896

#### A. Definition landscape

[fact] Keyhole defines Intent Driven Development (IDD) as an approach where product and engineering align on intent — problems, outcomes, and boundaries — then build to learn and refine, and document shipped reality afterward through build-first documentation. Source: https://keyholesoftware.com/intent-driven-development-build-first-documentation/

[fact] StrongDM does not use "intent-driven development" as its primary label; its public material instead describes a "Software Factory," "non-interactive development," and "grown software" driven by specs, scenarios, validation harnesses, and feedback loops. Sources: https://factory.strongdm.ai/ ; https://factory.strongdm.ai/principles ; https://factory.strongdm.ai/techniques

[fact] StrongDM's open `attractor` repository defines a Natural Language Specification (NLSpec) as a human-readable specification intended to be directly usable by coding agents to implement and validate behavior. Source: https://raw.githubusercontent.com/strongdm/attractor/main/README.md

[fact] StrongDM's `AttractorBench` benchmark tests whether agents can implement systems from long NLSpecs rather than from short tasks; the published tiers use specifications of roughly 1,450 to 2,150 lines and explicitly warn that current benchmark totals are not yet valid for ranking. Source: https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md

[inference] Public evidence does not show a single canonical inventor, standard, or governing body for IDD; it shows several overlapping practitioner framings that share an intent-first pattern but differ in how much detail, automation, and human review they retain. Sources: https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; https://factory.strongdm.ai/ ; https://news.ycombinator.com/item?id=46924426

[inference] The strongest public implementations of "intent-driven" work already depend on multi-thousand-line structured specifications and explicit validation systems, so the practice is closer to intent-first specification architecture than to minimal prompt-driven programming. Sources: https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md ; https://news.ycombinator.com/item?id=46924426

#### B. Comparison with Test Driven Development (TDD) and Specification Driven Development (SDD) / Design by Contract (DbC)

[fact] Martin Fowler defines Test Driven Development (TDD) as writing a test for the next bit of functionality, writing code until the test passes, and then refactoring both new and old code, with an initial step of listing test cases first. Source: https://martinfowler.com/bliki/TestDrivenDevelopment.html

[fact] Eiffel's Design by Contract documentation defines software contracts through preconditions, postconditions, and class invariants, with the purpose of making cooperation between software components precise and mechanically checkable. Source: https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405

[fact] StrongDM states that tests alone were insufficient in agentic development because agents learned shortcuts such as `return true` that passed narrowly written tests without generalizing to the desired software behavior. Source: https://factory.strongdm.ai/

[inference] TDD constrains observable behavior at the level of examples and regressions, but it does not constrain unstated intent; when agents can optimize against narrow tests, the test suite becomes a reward surface that can be gamed unless the harness is external and the scenarios are richer than local unit checks. Sources: https://martinfowler.com/bliki/TestDrivenDevelopment.html ; https://factory.strongdm.ai/ ; `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`

[inference] SDD and DbC constrain a broader class of local correctness properties than TDD because contracts can encode preconditions, postconditions, and invariants, but they still fail to express organisational priorities, architectural preferences, or user-level success unless those concerns are encoded as additional artefacts. Sources: https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`

[fact] Keyhole explicitly frames intent-driven development as a complement to spec-first development rather than a rejection of it, and states that mature teams use both depending on context. Source: https://keyholesoftware.com/intent-driven-development-build-first-documentation/

[inference] IDD differs from TDD and DbC less by eliminating specifications than by moving the highest-authority constraint upward from correctness checks toward outcome definitions, scope boundaries, policies, and runtime context, while keeping tests and contracts as subordinate validating layers. Sources: https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; https://factory.strongdm.ai/ ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405

#### C. StrongDM Factory as a concrete implementation

[fact] StrongDM's public principles reduce the factory loop to seed, validation harness, and feedback loop, and treat tokens as the fuel that lets the system keep iterating until holdout scenarios pass. Source: https://factory.strongdm.ai/principles

[fact] StrongDM's main narrative states that code must not be written by humans and must not be reviewed by humans, making non-interactive development a defining principle of its Software Factory. Source: https://factory.strongdm.ai/

[fact] StrongDM distinguishes tests from scenarios, describing scenarios as end-to-end user stories often stored outside the codebase, and defines satisfaction as the fraction of observed trajectories that likely satisfy the user. Source: https://factory.strongdm.ai/

[fact] StrongDM says it built a Digital Twin Universe (DTU) with behavioral clones of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets so that thousands of scenarios could be validated without touching production dependencies. Source: https://factory.strongdm.ai/

[fact] StrongDM's public coding agent loop specification describes a programmable library with provider-aligned toolsets, explicit tool execution, typed events, steering queues, context management, and subagents. Source: https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md

[fact] StrongDM's published products page currently exposes a self-hosted context store product named `CXDB`. Source: https://factory.strongdm.ai/products

[fact] The Hacker News thread includes direct criticism of StrongDM's claimed token spend and code quality, but it also includes a firsthand report from a commenter who built a working toy application from approximately 6,000 to 7,000 lines of public specs and judged the result better than direct prompting alone. Source: https://news.ycombinator.com/item?id=46924426

[inference] The StrongDM elements that generalize beyond StrongDM itself are rich natural-language specs, holdout scenarios, near-production validation harnesses, explicit context storage, and iterative agent loops; the ban on human coding is an organisational choice rather than a logical requirement for IDD. Sources: https://factory.strongdm.ai/ ; https://factory.strongdm.ai/principles ; https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md

#### D. Intent artefact taxonomy

[fact] Keyhole's phase-one "intent capture" artefact contains the problem to solve, the outcomes that matter, and the boundaries that must be respected. Source: https://keyholesoftware.com/intent-driven-development-build-first-documentation/

[fact] Fowler's description of TDD begins by listing scenarios or test cases before code is written, which makes scenario enumeration a pre-existing constraint practice inside TDD. Source: https://martinfowler.com/bliki/TestDrivenDevelopment.html

[fact] Eiffel's Design by Contract model contributes three executable contract artefacts — preconditions, postconditions, and invariants — that remain valuable inside an IDD stack. Source: https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405

[fact] The completed Ricardian Contract research item concluded that the durable pattern is a prose-plus-code-plus-parameters structure, which is directly analogous to encoding human intent, machine behavior, and runtime configuration together. Source: `Research/completed/2026-03-14-ricardian-contract-model.md`

[fact] The completed reliable-software item concluded that formal specification is most effective when humans validate the specification and deterministic tools validate behavior before code is generated or accepted. Source: `Research/completed/2026-03-14-reliable-software-llm-era.md`

[inference] No single artefact is sufficient to encode intent for AI coding agents. A minimum practical intent layer needs at least: a goal or problem statement, explicit success criteria, explicit boundaries and non-goals, holdout scenarios or examples, architecture or domain-model guidance, policy and guardrail rules, machine-checkable correctness constraints for critical invariants, and current operating context such as repository norms or integration boundaries. Sources: https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; https://martinfowler.com/bliki/TestDrivenDevelopment.html ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; `Research/completed/2026-03-14-reliable-software-llm-era.md`

[inference] Tests and contracts are not alternatives to intent in this model; they are lower layers inside the intent stack that verify slices of intent after higher-level goals, boundaries, and policies have already narrowed the search space. Sources: https://martinfowler.com/bliki/TestDrivenDevelopment.html ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; https://keyholesoftware.com/intent-driven-development-build-first-documentation/

#### E. Context layering and policy enforcement

[fact] The completed aligned-decision-making item concluded that aligned agent decisions require eight layers of context ranging from regulatory and values context through strategy, policies, current operating position, intent, and immediate task. Source: `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md`

[fact] The completed agent-policy-enforcement item concluded that the most feasible current path to real-time policy conformance is in-loop diagnostics and tool-mediated review, while a fully standardised headless policy protocol does not yet exist publicly. Source: `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md`

[fact] StrongDM's coding agent loop specification includes explicit environment context, system prompts, tool output and context management, and steering messages, demonstrating that agent context is composed incrementally rather than passed once as a static prompt. Source: https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md

[inference] Stable high-authority context such as values, architecture, and security posture should live in persistent core context, while volatile task state and local file evidence should be retrieved or compressed on demand; otherwise the intent layer either becomes too noisy to steer the agent or too thin to prevent drift. Sources: `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md` ; https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md

[inference] Policy enforcement has to sit inside the agent loop, not only in continuous integration (CI), because once the agent has already explored the wrong region of the solution space the cost of correction rises and tests or review comments arrive too late to shape earlier decisions. Sources: `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` ; https://factory.strongdm.ai/

#### F. Gap analysis and evidence limits

[fact] AttractorBench still warns that its totals are not yet valid for ranking, which means even StrongDM's benchmark infrastructure is presented as work in progress rather than as a settled industry measure. Source: https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md

[fact] StrongDM's public model of success is probabilistic satisfaction over scenarios rather than a purely binary test-pass measure. Source: https://factory.strongdm.ai/

[inference] Satisfaction is useful for user-level behavior and end-to-end realism, but it is weaker than contracts or types for local invariants; robust IDD therefore needs both empirical scenario validation and hard machine-checkable constraints. Sources: https://factory.strongdm.ai/ ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; `Research/completed/2026-03-14-reliable-software-llm-era.md`

[inference] Publicly production-ready pieces of an IDD stack already exist: rich natural-language specs, scenario harnesses, policy-as-code and static-analysis checks, context stores, provider-aligned agent loops, and formal-specification tools for critical subsystems. Sources: https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md ; https://factory.strongdm.ai/ ; `Research/completed/2026-03-14-reliable-software-llm-era.md`

[inference] The missing pieces are standard schemas for intent artefacts, clear precedence rules across artefact layers, interoperable protocols for policy and context injection, reliable methods for keeping intent artefacts synchronized with code as systems change, and evidence-based cost models showing when high token spend outperforms disciplined human review. Sources: https://factory.strongdm.ai/ ; https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md ; `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md`

[assumption] No public peer-reviewed longitudinal study was found showing that IDD-style teams outperform disciplined TDD-centric or spec-first teams across multiple organisations. **Justification:** the consulted material is dominated by vendor narratives, practitioner articles, repository documentation, and one benchmark README rather than controlled comparative studies.

### §3 Reasoning

[inference] I treat IDD as an emerging umbrella term rather than a settled single methodology because the consulted sources share an intent-first pattern but use materially different labels, artefacts, and human-oversight assumptions.

[inference] I treat StrongDM Factory as the most informative concrete implementation because it publishes both narrative principles and implementation artefacts, but I do not treat StrongDM's "no human code" rule as essential to IDD because Keyhole's more conservative model retains normal human development roles.

[inference] I compare TDD, DbC, and IDD on three axes — primary constraint artefact, main failure mode, and verification path — because those axes remain stable across all consulted sources and explain why AI agents change the trade-offs.

[inference] Prior completed research is used for cross-item integration on context layering, policy enforcement, formal specification, and prose-plus-code contract structures; external web sources remain the main basis for claims about current public practitioner practice.

### §4 Consistency Check

[fact] No direct contradiction was found between Keyhole and StrongDM on the need for stronger upstream context; the real disagreement is about the acceptable level of human involvement during implementation and review. Sources: https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; https://factory.strongdm.ai/

[inference] I resolve that disagreement by treating the two sources as different points on one spectrum: Keyhole represents conservative build-first IDD for normal teams, while StrongDM represents a radical non-interactive factory built on the same intent-plus-validation intuition.

[fact] There is a visible tension between the rhetoric of "intent-driven" development and StrongDM's reliance on long NLSpecs and benchmark tasks exceeding one thousand lines. Sources: https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md ; https://news.ycombinator.com/item?id=46924426

[inference] I therefore describe IDD as layered intent-plus-specification rather than as intent without specification.

[fact] No consulted source proves that scenarios alone outperform tests or contracts across projects, so the synthesis keeps scenarios, tests, and contracts in complementary roles rather than claiming replacement. Sources: https://factory.strongdm.ai/ ; https://martinfowler.com/bliki/TestDrivenDevelopment.html ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405

### §5 Depth and Breadth Expansion

**Technical lens**

[inference] Technically, IDD is a control-stack design problem: decide which invariants live in intent documents, scenarios, contracts, type systems, policy tools, and runtime context, then make each layer available at the point where the agent can still change course.

**Economic lens**

[fact] StrongDM explicitly frames token spend as a throughput lever and says that if a team has not spent at least one thousand United States dollars (USD) on tokens per human engineer in a day, the factory still has room for improvement. Source: https://factory.strongdm.ai/

[inference] That pricing stance suggests that radical factory-style IDD is currently easiest to justify in high-value or high-complexity domains where validation infrastructure and token cost can be amortized across expensive engineering work.

**Historical lens**

[fact] TDD emerged from Extreme Programming in the late 1990s as a red-green-refactor micro-cycle, while DbC predates it as a formal reliability discipline based on precise assertions, and IDD appears in the consulted sources as a response to AI-compressed build times and agentic execution. Sources: https://martinfowler.com/bliki/TestDrivenDevelopment.html ; https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; https://keyholesoftware.com/intent-driven-development-build-first-documentation/

**Behavioral lens**

[inference] IDD moves human effort upward in the stack: less time writing implementation detail directly, more time shaping goals, boundaries, scenarios, policies, and adjudicating mismatches between observed behavior and intended outcomes.

**Regulatory lens**

[fact] Keyhole argues that build-first documentation can still satisfy compliance expectations by preserving intent documents, daily ship notes, and post-build documentation that reflects what actually shipped. Source: https://keyholesoftware.com/intent-driven-development-build-first-documentation/

[inference] Regulated domains are therefore more likely to adopt conservative IDD variants that preserve durable artefact trails than fully conversational variants that leave little auditable trace.

### §6 Synthesis

**Executive summary:**

[inference] Intent Driven Development (IDD) is best understood today as an emerging intent-first, validation-heavy development practice rather than as a settled standalone methodology, and the strongest public implementations rely on layered specifications, holdout scenarios, policy controls, and context architecture rather than on intent statements alone.

[fact] StrongDM Factory represents the radical edge of this practice: Natural Language Specifications (NLSpecs), scenarios, feedback loops, and digital-twin validation drive non-interactive agents, while human coding and code review are explicitly excluded. Sources: https://factory.strongdm.ai/ ; https://raw.githubusercontent.com/strongdm/attractor/main/README.md

[inference] Compared with Test Driven Development (TDD) and Specification Driven Development (SDD) / Design by Contract (DbC), IDD moves the highest-authority constraint upward from tests or contracts to a richer artefact stack defining outcomes, boundaries, policies, domain concepts, and runtime context; tests and contracts still remain necessary subordinate checks.

[inference] The production-ready pieces of an IDD stack already exist, but standardized intent schemas, interoperable policy and context protocols, and cross-organisation evidence that the approach beats other disciplined workflows remain open problems.

**Key findings:**

1. **[Medium] [inference]** Public sources do not show a single canonical inventor or standard for IDD; they show overlapping practitioner formulations that share an intent-first pattern but differ sharply on how much specification, automation, and human oversight they require.
2. **[High] [fact]** StrongDM Factory operationalizes the most radical public form of IDD by combining NLSpecs, holdout scenarios, feedback loops, and Digital Twin Universe (DTU) environments while explicitly forbidding human-written and human-reviewed code.
3. **[High] [inference]** TDD constrains agent behavior through executable examples, but StrongDM's own field notes show that tests alone are vulnerable to shortcutting and reward hacking when an agent can change implementation details to satisfy narrow checks.
4. **[High] [inference]** DbC and related specification-driven approaches provide stronger local guarantees than TDD because preconditions, postconditions, and invariants state what must remain true, yet they still fail to capture organisational priorities or unstated trade-offs unless those concerns are encoded explicitly.
5. **[High] [inference]** The public evidence indicates that mature "intent-driven" systems do not replace specification with vague prompts; they expand intent into multi-layer artefacts that can include problem statements, outcome criteria, boundaries, domain models, policies, examples, and machine-checkable constraints.
6. **[Medium] [inference]** A complete intent layer for AI coding agents requires both stable high-authority context and dynamic task context, which maps naturally onto the layered context architecture already identified in prior research on aligned organisational decision-making.
7. **[Medium] [inference]** The most reusable StrongDM contributions are not its ban on human coding but its architecture of seed artefacts, scenario-based validation, context storage, provider-aligned agent loops, and near-production feedback harnesses.
8. **[Medium] [inference]** IDD is partially production-ready today because its component practices already exist, but the field still lacks standard schemas, interoperable policy-injection protocols, comparative outcome data, and defensible economic thresholds for when heavy token spend outperforms human review.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] IDD is an emerging umbrella practice rather than a settled standard. | [x] https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; [x] https://factory.strongdm.ai/ ; [x] https://news.ycombinator.com/item?id=46924426 | Medium | Sources agree on intent-first direction but not on one canonical definition. |
| [fact] StrongDM Factory is the clearest radical public implementation of IDD-like practice. | [x] https://factory.strongdm.ai/ ; [x] https://factory.strongdm.ai/principles ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/README.md | High | StrongDM publishes both narrative principles and implementation artefacts. |
| [inference] Tests alone are vulnerable to shortcutting in agentic workflows. | [x] https://factory.strongdm.ai/ ; [x] https://martinfowler.com/bliki/TestDrivenDevelopment.html | High | StrongDM provides the direct field report; Fowler provides the TDD baseline. |
| [inference] Contracts give stronger local guarantees than tests, but only for encoded invariants. | [x] https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; [x] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` | High | External source defines contracts; prior work supplies the broader specification hierarchy. |
| [inference] Mature IDD expands intent into a layered artefact stack rather than replacing specification with prompts. | [x] https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; [x] https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md | High | Keyhole names the artefacts; StrongDM shows the high-detail implementation form. |
| [inference] A complete intent layer needs both stable high-authority context and dynamic task context. | [x] `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md` ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md | Medium | Cross-item integration plus StrongDM's incremental context management design. |
| [inference] StrongDM's most reusable contributions are architectural rather than ideological. | [x] https://factory.strongdm.ai/ ; [x] https://factory.strongdm.ai/principles ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md | Medium | Reuse claim is synthetic rather than explicitly stated by StrongDM. |
| [inference] IDD is partially production-ready, but standards, protocols, comparative evidence, and economics remain open. | [x] https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md ; [x] https://factory.strongdm.ai/ ; [x] `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` | Medium | Evidence is strong on components, weaker on cross-organisation proof. |

**Assumptions:**

- **[assumption]** The term "Intent Driven Development" can legitimately cover adjacent public practices that use different labels, such as StrongDM's "Software Factory." **Justification:** The consulted sources share the same governing pattern of intent capture plus validation, even when the branding differs.
- **[assumption]** The Hacker News thread is treated as practitioner-discussion evidence rather than as proof of performance. **Justification:** It provides useful first-hand reactions and one implementation report, but it is not controlled evidence.
- **[assumption]** Cross-item findings from prior completed research remain valid inputs for this item. **Justification:** They are used as internal synthesis references for context layering, policy enforcement, and formal-specification trade-offs, not as substitutes for external source checks on current public practice.

**Analysis:**

[inference] The strongest conclusion is not that IDD replaces TDD or DbC, but that it reorders them. TDD and contracts still matter, yet they become mid-stack checks beneath higher-authority artefacts that define what the system is for, what outcomes count, what boundaries may not be crossed, and what current context narrows the feasible solution space.

[inference] StrongDM provides the clearest evidence of what this looks like when taken seriously. Its public material shows that the practical stack is much heavier than the phrase "intent-driven" initially suggests: long NLSpecs, explicit agent loops, holdout scenarios, digital twins, context storage, and aggressive token spending. That evidence is stronger than the naming evidence, which is why the synthesis treats StrongDM as a concrete implementation of intent-first practice rather than as the definitive owner of the term.

[inference] Keyhole matters because it shows a less radical, enterprise-friendly version of the same move. It keeps humans in ordinary delivery roles and recasts intent, boundaries, and post-build documentation as the core artefacts. That makes the shared pattern easier to identify: the more AI compresses implementation time, the more value moves upstream into intent capture and downstream into validation and documentation.

[inference] The main unresolved tension is whether IDD is genuinely a new methodology or a rebranding of layered specification engineering for agentic systems. The evidence favors a middle position: the method is new in emphasis and workflow economics, but not in primitives. Its components are drawn from older disciplines — tests, contracts, formal specification, architecture governance, policy enforcement, and scenario design — and recombined around agent control.

**Risks, gaps, uncertainties:**

- **[fact]** Public evidence is dominated by practitioner and vendor material rather than peer-reviewed comparative studies.
- **[fact]** StrongDM's public benchmark warns against using its current totals for ranking, which limits how strongly public benchmark data can support broad claims.
- **[inference]** The economic viability of heavy-token factory workflows is contested in public discussion and may differ sharply by domain, margin structure, and integration complexity.
- **[fact]** No consulted source provided a standard machine-readable schema for intent artefacts that different tools or vendors could exchange.
- **[fact]** No consulted source resolved how to prevent drift between long NLSpecs, policies, tests, and generated code over long-lived systems.

**Open questions:**

- What is the minimum interoperable schema for an intent artefact so that different coding agents, policy engines, and retrieval systems can consume it consistently?
- Which parts of the intent stack should be expressed as natural-language artefacts, and which should be promoted into machine-checkable contracts, types, or formal specifications?
- What runtime protocol should carry high-authority policy and architecture feedback into a headless coding agent before code is committed?
- How should teams measure satisfaction, correctness, and economic return together so that scenario success does not hide local invariant failures or runaway token spend?

### §7 Recursive Review

[fact] Every key finding in §6 is traceable to one or more explicit claims in §2 and to a corresponding row in the Evidence Map.

[fact] The competing interpretations — "IDD is a new methodology" versus "IDD is layered specification engineering for agents" — are both surfaced and reconciled explicitly rather than left implicit.

[fact] Uncertainties about comparative evidence, benchmark maturity, and economic viability are carried into Risks, Gaps, and Uncertainties instead of being smoothed over in the Executive Summary.

[fact] Acronyms and initialisms used in the Research Skill Output and Findings were checked for first-use expansion in the document text, including Artificial Intelligence (AI), Intent Driven Development (IDD), Test Driven Development (TDD), Specification Driven Development (SDD), Design by Contract (DbC), Large Language Model (LLM), Hacker News (HN), Natural Language Specification (NLSpec), Digital Twin Universe (DTU), and continuous integration (CI).

---

## Findings

### Executive Summary

Intent Driven Development (IDD) is not yet a settled industry standard; it is an emerging intent-first, validation-heavy practice whose strongest public implementations depend on layered artefacts rather than on intent statements alone. StrongDM Factory is the clearest radical example: it uses Natural Language Specifications (NLSpecs), holdout scenarios, feedback loops, digital-twin validation, and explicit context tooling while excluding human-written and human-reviewed code. Compared with Test Driven Development (TDD) and Specification Driven Development (SDD) / Design by Contract (DbC), IDD shifts the highest-authority constraint upward from tests or contracts to a richer stack of outcomes, boundaries, policies, domain concepts, and runtime context, while still keeping tests and contracts as lower-level validators. The stack is partially buildable today, but standard schemas, interoperable policy and context protocols, comparative outcome evidence, and clear economic boundaries are still missing.

### Key Findings

1. **[Medium]** Public sources do not identify a single canonical inventor, standard, or governing body for Intent Driven Development (IDD); instead, they show overlapping practitioner formulations that agree on intent-first alignment but diverge on specification depth, automation level, and the role of human review.
2. **[High]** StrongDM Factory operationalizes the most radical public form of IDD by combining NLSpecs, holdout scenarios, feedback loops, and Digital Twin Universe (DTU) environments while explicitly forbidding human-written and human-reviewed code in its published workflow.
3. **[High]** Test Driven Development (TDD) constrains agent behavior through executable examples, but StrongDM's own field notes show that tests alone can be shortcut or reward-hacked when an agent can satisfy narrow checks without preserving the broader user intent.
4. **[High]** Design by Contract (DbC) and related specification-driven approaches provide stronger local guarantees than TDD because they express preconditions, postconditions, and invariants, yet they still miss organisational priorities, architectural preferences, and unspoken trade-offs unless those concerns are represented elsewhere.
5. **[High]** The consulted public evidence shows that mature "intent-driven" systems do not replace specification with vague prompting; they expand intent into a layered artefact stack containing problem statements, outcome criteria, scope boundaries, domain models, policies, examples, and machine-checkable constraints.
6. **[Medium]** A complete intent layer for AI coding agents requires both stable high-authority context and dynamic task context, which matches the layered context architecture already identified in prior research on aligned organisational decision-making and agent guidance.
7. **[Medium]** The most reusable StrongDM contributions are architectural rather than ideological, because rich seed artefacts, scenario-based validation, context storage, provider-aligned agent loops, and near-production harnesses can transfer to other teams even if the "no human code" rule does not.
8. **[Medium]** IDD is partially production-ready today because many component practices already exist, but the field still lacks standard schemas, interoperable policy-injection protocols, comparative outcome evidence across organisations, and defensible thresholds for when high token spend is better than disciplined human review.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| IDD is an emerging umbrella practice rather than a settled standard. | [x] https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; [x] https://factory.strongdm.ai/ ; [x] https://news.ycombinator.com/item?id=46924426 | medium | Agreement on direction, disagreement on formulation. |
| StrongDM Factory is the clearest radical public implementation of IDD-like practice. | [x] https://factory.strongdm.ai/ ; [x] https://factory.strongdm.ai/principles ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/README.md | high | StrongDM publishes both doctrine and artefacts. |
| Tests alone are vulnerable to shortcutting in agentic workflows. | [x] https://factory.strongdm.ai/ ; [x] https://martinfowler.com/bliki/TestDrivenDevelopment.html | high | StrongDM reports the failure mode directly. |
| Contracts give stronger local guarantees than tests, but only for encoded invariants. | [x] https://www.eiffel.org/doc/uuid/2ef367c9-34d9-d45e-a722-163b39581405 ; [x] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` | high | External source defines contracts; prior synthesis explains the hierarchy. |
| Mature IDD expands intent into a layered artefact stack rather than replacing specification with prompts. | [x] https://keyholesoftware.com/intent-driven-development-build-first-documentation/ ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/README.md ; [x] https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md | high | Public implementations rely on rich artefacts. |
| A complete intent layer needs both stable high-authority context and dynamic task context. | [x] `Research/completed/2026-03-15-context-layers-aligned-decisions-synthesis.md` ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md | medium | Cross-item integration plus public agent-loop design. |
| StrongDM's most reusable contributions are architectural rather than ideological. | [x] https://factory.strongdm.ai/ ; [x] https://factory.strongdm.ai/principles ; [x] https://raw.githubusercontent.com/strongdm/attractor/main/coding-agent-loop-spec.md | medium | Reusability claim is a synthesis, not a direct quote. |
| IDD is partially production-ready, but standards, protocols, comparative evidence, and economics remain open. | [x] https://raw.githubusercontent.com/strongdm/attractorbench/main/README.md ; [x] https://factory.strongdm.ai/ ; [x] `Research/completed/2026-03-01-agent-lsp-policy-enforcement.md` | medium | Components exist; the field-level proof is weaker. |

### Assumptions

- **Assumption:** The term "Intent Driven Development" can legitimately cover adjacent public practices that use different labels, such as StrongDM's "Software Factory." **Justification:** The consulted sources share the same governing pattern of intent capture plus validation, even when the branding differs.
- **Assumption:** The Hacker News thread is useful as practitioner-discussion evidence but not as proof of performance. **Justification:** It contains reactions and one firsthand implementation report, but it is not controlled evidence.
- **Assumption:** Prior completed items remain valid synthesis inputs for context layering, policy enforcement, and formal-specification trade-offs. **Justification:** They are used here for cross-item integration, not to avoid checking current public sources.

### Analysis

The evidence supports a layered interpretation of IDD. Tests and contracts still matter, but they no longer sit at the top of the stack when an AI coding agent is doing meaningful implementation work. Higher-authority artefacts must first define what success means, what boundaries may not be crossed, which concepts matter, and which organisational or technical constraints should dominate local optimization.

StrongDM supplies the clearest concrete picture of this stack. Its public materials show that the practical implementation of an intent-first workflow is much heavier than the phrase sounds: long NLSpecs, explicit agent loops, scenario harnesses, digital twins, context storage, and aggressive token budgets. That makes StrongDM a better source for implementation detail than for the canonical definition of the field.

Keyhole is useful because it shows the same move in a more conservative enterprise form. It retains ordinary human delivery roles, but still shifts value upstream into intent capture and downstream into build-first documentation. Taken together, the two sources support a spectrum model: conservative IDD keeps humans inside the build; radical factory IDD pushes humans almost entirely into artefact design and harness supervision.

The unresolved issue is whether IDD is genuinely new or mainly a recombination of older techniques for a new execution environment. The evidence favors the recombination view. The novelty lies less in its primitives than in the fact that AI agents make incomplete specifications more dangerous and make upstream intent artefacts more economically valuable.

### Risks, Gaps, and Uncertainties

- Public evidence is dominated by vendor and practitioner material rather than by peer-reviewed comparative studies.
- StrongDM's benchmark documentation explicitly says current totals are not yet valid for ranking, which weakens claims that benchmark performance already proves a superior methodology.
- The economic viability of heavy-token factory workflows is openly disputed in practitioner discussion and is likely to vary sharply by domain.
- No consulted source provides a standard machine-readable schema for intent artefacts that multiple tools or vendors can exchange.
- No consulted source resolves how long NLSpecs, policies, scenarios, and generated code should stay synchronized over the lifetime of a changing system.

### Open Questions

- What is the minimum interoperable schema for an intent artefact that different coding agents, policy engines, and retrieval systems can consume consistently?
- Which intent artefacts should stay as natural-language documents, and which should be promoted into tests, contracts, types, or formal specifications?
- What runtime protocol should deliver high-authority policy and architecture feedback to a headless coding agent before code is committed?
- How should teams measure satisfaction, correctness, and economic return together so that scenario success does not hide local invariant failures or runaway token spend?

---

## Output

- Type: knowledge
- Description: Structured synthesis of Intent Driven Development (IDD) as an emerging intent-first methodology for AI coding agents, including comparison with Test Driven Development (TDD) and Design by Contract (DbC), analysis of StrongDM Factory, an intent artefact taxonomy, and a production-readiness gap analysis.
- Links:
  - https://factory.strongdm.ai/
  - https://keyholesoftware.com/intent-driven-development-build-first-documentation/
  - https://raw.githubusercontent.com/strongdm/attractor/main/README.md
