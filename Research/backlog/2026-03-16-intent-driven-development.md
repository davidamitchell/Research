---
title: "Intent Driven Development: context and concept layering to bound the solution space"
added: 2026-03-16
status: backlog  # backlog | in-progress | reviewing | completed
priority: high  # low | medium | high
blocks: []
tags: [intent, software-engineering, tdd, specification, context-layering, agentic-coding, ai, developer-tooling, design-methodology]
started: ~
completed: ~
output: [knowledge]
---

# Intent Driven Development: context and concept layering to bound the solution space

## Research Question

What is Intent Driven Development (IDD) — as a methodology that moves past Test Driven Development (TDD) and Specification Driven Development (SDD) — and what context and concept layering mechanisms are required to sufficiently bound the potential solution space so that AI coding agents produce outputs that are aligned with developer and organisational intent?

Supporting questions:
- What is IDD? Is it a named methodology, an emergent practice, or a set of loosely related ideas? Who coined it or is actively defining it?
- How does IDD differ from TDD and SDD? What does each paradigm use as its primary constraint on the solution space, and where does each break down with AI-assisted development?
- What does StrongDM Factory (https://factory.strongdm.ai/) represent as a concrete implementation of intent-driven principles in infrastructure and access management? What can be generalised?
- What is the structure of a complete "intent layer"? What artefacts (natural language, formal specs, constraints, examples, policies) are needed and in what combination?
- How do concept layering and context architecture interact with intent? What are the relevant findings from context-compression and aligned decision-making research?
- What does the HN community (https://news.ycombinator.com/item?id=46924426) identify as the key challenges, precedents, and open problems in intent-driven approaches?

## Scope

**In scope:**
- Definition and characterisation of Intent Driven Development (IDD) as a software engineering methodology
- Comparison of TDD, Specification Driven Development (SDD)/Design by Contract (DbC), and IDD: what each uses as a primary constraint, where each applies, and where each fails
- StrongDM Factory as a concrete implementation: what it does, what principles it embodies, and what is generalisable
- Artefact types that encode intent: natural-language specifications, property-based tests, type-level constraints, contracts (including Ricardian Contract model from `2026-03-14-ricardian-contract-model`), policy rules, and worked examples
- Context and concept layering: how the hierarchical context model from `2026-03-15-context-layers-aligned-decisions-synthesis` applies to bounding the agent solution space
- Agent policy enforcement: relationship to the Language Server Protocol (LSP)-style guidance from `2026-03-01-agent-lsp-policy-enforcement`
- Formal methods and reliability: relationship to findings from `2026-03-14-reliable-software-llm-era` on cognitive debt and formal specification
- Practitioner discourse: Hacker News thread and related community discussion

**Out of scope:**
- Full implementation of an IDD toolchain or framework (this is a research item, not an engineering item)
- Detailed reinvestigation of topics already covered in the prerequisite completed items above
- General LLM benchmarking or capability comparison unrelated to intent alignment

**Constraints:** Publicly accessible sources. Build primarily on the completed prior research referenced above, supplemented by web search for current practitioner work and the HN thread. Prefer 2023–2026 sources to reflect the current AI-assisted development context.

## Context

Test Driven Development constrains the solution space via executable tests: code is correct if and only if it passes the tests. This works well when the test suite is complete and the problem is well-bounded. Specification Driven Development (and the related Design by Contract (DbC) school) constrains via formal or semi-formal contracts: pre-conditions, post-conditions, and invariants. Both approaches are fundamentally reactive — they detect violations after code has been produced, or guide code towards satisfying a pre-written constraint set.

With AI coding agents, the failure mode changes. An agent can produce code that satisfies every test and every contract while still being wrong — because the tests and contracts themselves were incomplete, ambiguous, or misaligned with the actual intent of the developer or organisation. The question is no longer "does the code pass the spec?" but "does the code embody what the developer actually meant?"

Intent Driven Development (IDD) proposes intent as the primary input: the developer (or organisation) expresses *what they want to achieve*, in sufficient richness that the solution space is bounded without being over-specified. The challenge is that intent is harder to formalise than a test or a contract. It requires:
1. **Concept layering** — decomposing intent from high-level goals (organisational strategy, domain model) down to immediate task requirements, without losing coherence at each layer.
2. **Context architecture** — ensuring the right subset of that layered context is available at inference time, given finite context windows.
3. **Policy enforcement** — encoding constraints derived from intent (security posture, architecture governance, team norms) as enforceable rules the agent must satisfy in real time.

This item connects prior research threads: the context architecture work (`2026-03-15-context-layers-aligned-decisions-synthesis`), agent policy enforcement (`2026-03-01-agent-lsp-policy-enforcement`), formal reliability methods (`2026-03-14-reliable-software-llm-era`), and machine-readable contract models (`2026-03-14-ricardian-contract-model`). The synthesis question is: what does a complete IDD stack look like, and which components are production-ready vs. still open problems?

## Approach

1. **Define the landscape** — search for "intent driven development" as a named methodology: who defines it, what artefacts it requires, and how it is distinguished from TDD and SDD. Start with the HN thread and StrongDM Factory documentation.
2. **Comparative analysis** — construct a comparison table: TDD vs. SDD/DbC vs. IDD, on axes of: primary constraint artefact, failure mode with AI agents, solution space bound mechanism, verification approach, and tooling maturity.
3. **StrongDM Factory deep dive** — analyse the StrongDM Factory product (https://factory.strongdm.ai/) as a concrete IDD implementation in the access management and infrastructure space. What intent artefacts does it require? What context layering does it implement? What can be generalised to other domains?
4. **Intent artefact taxonomy** — synthesise the types of artefact that encode intent: natural-language user stories, property-based tests, type-level constraints, formal contracts, policy-as-code rules, worked examples, architectural decision records, and organisational context documents. Which artefacts are necessary vs. sufficient? What combination produces a bounded solution space?
5. **Context layering mapping** — map the intent artefact taxonomy onto the layered context architecture from `2026-03-15-context-layers-aligned-decisions-synthesis`. At which layer does each artefact type belong? How is it stored, retrieved, and composed at inference time?
6. **Gap analysis** — identify which components of the IDD stack are production-ready and which are open problems. What tooling, protocols, or standards are missing?
7. **Synthesis** — produce the Executive Summary, Key Findings, and Evidence Map.

## Sources

- [ ] HN thread on intent-driven development — https://news.ycombinator.com/item?id=46924426
- [ ] StrongDM Factory — https://factory.strongdm.ai/ — intent-driven infrastructure access management
- [ ] Prior completed research: `2026-03-01-agent-lsp-policy-enforcement` — LSP-like real-time policy enforcement for agents
- [ ] Prior completed research: `2026-03-14-reliable-software-llm-era` — formal methods, cognitive debt, and reliability in the LLM era
- [ ] Prior completed research: `2026-03-14-ricardian-contract-model` — machine-readable contract model as an intent encoding mechanism
- [ ] Prior backlog item: `2026-03-15-context-layers-aligned-decisions-synthesis` — layered context architecture for aligned AI decisions
- [ ] Web search for "intent driven development" methodology definitions (2024–2026)
- [ ] Property-based testing literature (Hypothesis, QuickCheck, fast-check) as a bridge between TDD and intent specification
- [ ] Design by Contract literature: Bertrand Meyer's Eiffel work and modern implementations (contracts in TypeScript, Python beartype/typeguard, Racket contracts)

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
