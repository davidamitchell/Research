---
title: "Language designed for LLM agents to produce: addressing generation-layer failure modes in agentic systems"
added: 2026-03-10
status: backlog
priority: high
blocks: []
tags: [agentic-systems, programming-languages, dsl, failure-modes, intent-alignment, reward-hacking, formal-methods, output-language, llm-code-generation, structured-output]
started: ~
completed: ~
output: []
---

# Language designed for LLM agents to produce: addressing generation-layer failure modes in agentic systems

## Research Question

Is anyone actively developing a programming language or structured output format specifically designed for LLM agents to generate — rather than humans to write — that structurally addresses generation-layer and goal-layer failure modes (hallucination, intent mismatch, reward hacking, under-specification, instruction conflict, tool misuse) as classified in the failure mode taxonomy and the specification hierarchy established in the two referenced completed items? If so: what is the design rationale, what failure modes does each approach target, and how mature is the work?

## Scope

**In scope:**
- Purpose-built languages or DSLs whose primary intended author is an LLM agent, not a human programmer
- Structured output formats (JSON schemas, constraint grammars, typed intermediate representations) designed specifically to constrain what LLMs can emit and thereby reduce failure modes
- Research prototypes, academic papers, and production systems (2022–2026) describing languages or grammars designed with LLM generation in mind
- How each candidate approach maps to the five-layer failure mode taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md`: which layers (generation, goal, alignment, safety/security, operational) each language targets
- How each candidate maps to the specification hierarchy from `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`: where on the informal → structured output → type annotations → rich type system → formal verification continuum each approach sits
- Type-constrained decoding (ETH Zurich PLDI 2025) and related compiler-enforced generation as a language-design mechanism
- The "Out of the Tar Pit" thesis applied to agent-generated code: do any of these languages reduce mutable state and control flow complexity in LLM-produced output?
- Intermediate representation (IR) approaches where agents emit to a typed IR rather than a surface language

**Out of scope:**
- Languages designed for humans to write that happen to be used with LLMs (TypeScript, Rust, Python with type annotations) — these are covered in `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- Prompt engineering techniques that constrain model behaviour through instruction rather than grammar/type enforcement
- Post-hoc validation pipelines (e.g. schema validators, linters applied after generation) unless they are architecturally inseparable from the language design
- LLM fine-tuning approaches that target failure modes by adjusting weights rather than output grammar

**Constraints:** Focus on work where the language/format design is explicit and the LLM-as-author framing is stated or clearly implied. Distinguish research prototypes from production-grade tools. Prefer primary sources (papers, repo READMEs, design documents).

## Context

The two completed research items establish a clear gap:

1. **`2026-03-10-formal-spec-intent-alignment-agentic-coding.md`** shows that natural language specifications (level 1 of the specification hierarchy) have zero verifiability, and that the highest-leverage structural intervention is moving up the specification hierarchy. It identifies type-constrained decoding (ETH Zurich PLDI 2025) as a mechanistic approach — but that paper constrains generation to an existing language (e.g. Python), not to a purpose-built agent-output language. The open question it leaves: "Does writing specifications in Dafny (level 5) and using LLM-assisted spec generation produce more aligned agentic code outputs than natural language task descriptions alone?"

2. **`2026-03-10-ai-concept-classification-taxonomy.md`** produces a five-layer failure mode taxonomy and an explicit open question: "Intent engineering formalisation — What is the formal language for intent specification in agentic systems, beyond natural language? Connects to the formal spec research item." It also identifies that structural controls (schema enforcement, type constraints) are the category that addresses generation-layer and goal-layer failures — the lowest and most tractable layer.

Together these items make the research question tractable: a language specifically designed for LLM agent output would sit at the intersection of structural controls and the level 3–4 specification hierarchy. The question is whether this design space has active occupants.

Related prior research:
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — specification hierarchy, type-constrained decoding, reward hacking
- `2026-03-10-ai-concept-classification-taxonomy.md` — failure mode taxonomy, structural controls
- `2026-03-08-context-engineering-first-principles.md` — goal-level vs token-level steering
- `2026-03-02-integrative-framework-agent-decision-making.md` — decision-making frameworks for agents

## Approach

1. **Survey type-constrained and grammar-constrained generation literature.** Start with ETH Zurich PLDI 2025 (type-constrained decoding), Guidance (Microsoft), Outlines (dottxt-ai), LMQL, and related structured generation libraries. For each: what failure modes does it address, what is the level on the specification hierarchy, and is the output grammar a "language" in a meaningful sense?

2. **Search for purpose-built agent output languages.** Look for academic papers, blog posts, and repos explicitly describing a language whose primary intended author is an LLM agent. Search terms: "language for LLM agents", "agent output language", "DSL for LLM code generation", "LLM-targeted intermediate representation", "agent-native language". Check arXiv (cs.PL, cs.AI, cs.SE), GitHub topics, and NeurIPS/ICML/ICLR/PLDI/OOPSLA 2023–2025 proceedings.

3. **Map candidates to the failure mode taxonomy.** For each identified approach, use the five-layer taxonomy from the taxonomy item to label which failure modes it structurally addresses and which it does not. Identify gaps: are there layers that no current approach covers?

4. **Map candidates to the specification hierarchy.** Place each approach on the informal → structured output → type annotations → rich type system → formal verification continuum. Assess whether any approach occupies the "designed for LLM generation at level 4–5" position, or whether the field has only reached level 2–3.

5. **Assess maturity and adoption.** For each candidate: is it a research prototype, an open-source library, or a production tool? What is the evidence of adoption (GitHub stars, citations, integration into agentic frameworks)?

6. **Synthesise.** Produce a structured assessment: which failure modes are currently addressed by purpose-built approaches, which are not, and what would a comprehensive agent-output language need to include to address the full taxonomy.

## Sources

- [ ] ETH Zurich PLDI 2025 — type-constrained decoding: https://arxiv.org/abs/2501.09723 (or closest match)
- [ ] Guidance (Microsoft): https://github.com/guidance-ai/guidance — structured generation with grammars
- [ ] Outlines (dottxt-ai): https://github.com/dottxt-ai/outlines — structured text generation
- [ ] LMQL: https://lmql.ai — query language for LLMs with type/constraint support
- [ ] Jsonformer: https://github.com/1rgs/jsonformer — JSON-constrained generation
- [ ] SGLang: https://github.com/sgl-project/sglang — structured generation language for LLMs
- [ ] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [ ] `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md`
- [ ] arXiv cs.PL and cs.AI 2023–2025 — search "language for LLM agents", "LLM-targeted IR", "agent output grammar"
- [ ] PLDI/OOPSLA/POPL 2023–2025 proceedings — programming language design for LLM generation
- [ ] Semantic Machines / "semantic parsing for agents" literature — structured meaning representations as agent output targets
- [ ] "Code as policies" (Liang et al., 2023): https://code-as-policies.github.io — natural language → robot code; intermediate representation design
- [ ] MRKL / ReAct / Toolformer papers — what output format assumptions are embedded in tool-use agent designs
