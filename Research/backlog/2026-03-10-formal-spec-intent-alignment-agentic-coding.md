---
title: "Formal intent specification and language choice for AI alignment in agentic coding systems"
added: 2026-03-10
status: backlog
priority: high
blocks: []
tags: [formal-methods, intent-alignment, reward-hacking, agentic-systems, programming-languages, type-theory, out-of-the-tar-pit]
started: ~
completed: ~
output: [knowledge]
---

# Formal intent specification and language choice for AI alignment in agentic coding systems

## Research Question

Can formal specification of task intent structurally eliminate reward hacking and intent mismatch in agentic coding systems? What is the expressiveness-verifiability tradeoff at each level of the specification hierarchy? Who is currently solving the class of accidental-complexity bugs described in "Out of the Tar Pit"? And which programming languages most effectively aid intent alignment and reduce state and flow bugs — including by making AI-generated code more aligned with human intent?

## Scope

**In scope:**
- Specification hierarchy levels: informal natural language → structured prompts → contracts/pre/postconditions → type-level specs (dependent types) → full formal verification (TLA+, Alloy, Dafny, F*, Coq, Agda, Idris)
- Expressiveness vs. verifiability tradeoff at each level, with evidence of real-world adoption
- "Out of the Tar Pit" (Moseley & Marks, 2006): the thesis that accidental complexity from mutable state and control flow is the root cause of most software bugs — who is applying or extending this work in 2024–2026
- Reward hacking and Goodhart's Law in ML/AI systems: structural causes and proposed specification-theoretic remedies
- Intent mismatch in agentic coding (LLM code generation, Copilot, Devin, SWE-agent): where intent diverges from output and why
- Programming language properties that reduce ambiguity for AI code generation: strong type systems, effect systems, purity, linear types, refinement types
- Evidence on whether AI coding tools produce more aligned code in strongly-typed or formally-specified codebases vs. dynamically-typed or weakly-typed ones

**Out of scope:**
- Full formal verification of entire production systems (impractical at scale; treat as a spectrum upper bound)
- Hardware verification (focus is software and AI systems)
- Non-agentic AI (batch inference, image models)
- Economic cost of formal methods adoption (separate research item if warranted)

**Constraints:** Focus on evidence from 2020–2026 where possible; the "Out of the Tar Pit" paper (2006) is a required anchor. Prefer academic papers, credible engineering blogs, and production case studies over speculative commentary.

## Context

Three converging forces make this question urgent:

1. **Agentic coding systems** (Copilot, Devin, SWE-bench agents, GitHub Copilot Agent) are now executing multi-step tasks autonomously. When intent is specified only informally (natural language), the agent can satisfy the literal specification while violating the intended goal — the classic reward hacking pattern. Understanding whether richer specification can structurally close this gap is directly relevant to the tooling in this repository.

2. **Out of the Tar Pit** diagnosed in 2006 that most software complexity arises from mutable state and control flow — both of which are exactly what LLMs generate most readily and what causes the hardest-to-catch bugs in AI-generated code. Who is applying FRP, relational/declarative programming, and functional purity as remedies in 2025?

3. **Language choice affects AI alignment.** There is an open empirical question: does coding in Haskell, Idris, Rust (with ownership types), or Elm genuinely produce more intent-aligned AI-generated code than Python or JavaScript? Are there empirical benchmarks on this?

The answer informs: (a) how to structure prompts and specifications when tasking agentic coding systems, (b) whether the research tooling in `src/` should adopt stronger type contracts, and (c) what the field's current state-of-the-art is for intent-preserving code generation.

## Approach

1. **Map the specification hierarchy.** Identify the canonical levels (informal → structured → contract → type-level → formal) and locate representative tools/languages at each. Characterise the expressiveness-verifiability tradeoff at each level with concrete evidence.

2. **Investigate reward hacking and intent mismatch.** Review the AI safety and alignment literature on reward hacking (Krakovna et al. 2020 specification gaming compendium, Gao et al. 2022 scaling laws for reward models) and map remedies onto the specification hierarchy.

3. **Trace "Out of the Tar Pit" forward.** What has happened to the FRP, relational, and Functional Core / Imperative Shell approaches since 2006? Who is applying them now, and with what results? Are there new languages, frameworks, or paradigms that directly address the paper's thesis?

4. **Survey language properties for AI alignment.** Collect evidence on which language properties (type strength, purity, effect systems, ownership, linear/affine types) empirically improve alignment between programmer intent and AI-generated code.

5. **Synthesise into a practical framework.** Produce a ranked recommendation: for each level of specification effort available, what does the evidence say is the highest-leverage intervention for reducing intent mismatch in an agentic coding workflow?

## Sources

- [ ] Moseley, B. & Marks, P. (2006). *Out of the Tar Pit*. https://curtclifton.net/papers/MoseleyMarks06a.pdf
- [ ] Krakovna, V. et al. (2020). *Specification Gaming: The Flip Side of AI Ingenuity*. DeepMind blog + compendium. https://www.deepmind.com/blog/specification-gaming-the-flip-side-of-ai-ingenuity
- [ ] Gao, L. et al. (2022). *Scaling Laws for Reward Model Overoptimization*. https://arxiv.org/abs/2210.10760
- [ ] Leino, K.R.M. (2023). *Program Proofs*. MIT Press (Dafny-based formal verification). https://program-proofs.com/
- [ ] Wadler, P. (2015). *Propositions as Types*. CACM. (Curry-Howard correspondence and why types are specs.) https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf
- [ ] Brady, E. (2017). *Type-Driven Development with Idris*. Manning. (Dependent types as executable specifications.)
- [ ] Lamport, L. (2002). *Specifying Systems: The TLA+ Language and Tools*. (Formal behavioural specification.) https://lamport.azurewebsites.net/tla/book.html
- [ ] Hillel Wayne et al. — PlusCal/TLA+ usage at AWS, Microsoft. https://lamport.azurewebsites.net/tla/industrial-use.html
- [ ] Hellerstein, J.M. et al. (2019). *Keeping CALM: When Distributed Consistency Is Easy*. CACM. (CALM conjecture and monotonic logic as a correctness condition.)
- [ ] SWE-bench / SWE-agent papers (Princeton, 2024) — intent alignment in real-world GitHub issue resolution. https://swe-bench.github.io/
- [ ] Research on "functional core, imperative shell" pattern — Gary Bernhardt's Boundaries talk (2012, rewatch for 2025 context). https://www.destroyallsoftware.com/talks/boundaries
- [ ] Effect systems survey — Brachthäuser et al. or similar — which languages have shipped practical effect systems?
- [ ] Rust ownership model as a form of linear type specification — empirical evidence on bug classes eliminated
- [ ] Elm architecture as FRP-based accidental-complexity reduction: https://guide.elm-lang.org/architecture/
- [ ] Agda/Coq/Lean for verified software: what production use cases exist?

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
