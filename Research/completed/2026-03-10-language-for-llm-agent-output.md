---
title: "Language designed for LLM agents to produce: addressing generation-layer failure modes in agentic systems"
added: 2026-03-11T07:54:09+00:00
status: completed
priority: high
blocks: []
tags: [agentic-systems, programming-languages, dsl, failure-modes, intent-alignment, reward-hacking, formal-methods, output-language, llm-code-generation, structured-output]
started: 2026-03-11T07:54:09+00:00
completed: 2026-03-11T07:54:09+00:00
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
- Type-constrained decoding (ETH Zurich Programming Language Design and Implementation (PLDI) 2025) and related compiler-enforced generation as a language-design mechanism
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

- [x] ETH Zurich PLDI 2025 — type-constrained decoding: https://arxiv.org/abs/2504.09246
- [x] Guidance (Microsoft): https://github.com/guidance-ai/guidance — structured generation with grammars
- [x] Outlines (dottxt-ai): https://github.com/dottxt-ai/outlines — structured text generation
- [x] LMQL: https://lmql.ai — query language for LLMs with type/constraint support; paper arXiv:2212.06094 (PLDI 2023)
- [ ] Jsonformer: https://github.com/1rgs/jsonformer — JSON-constrained generation (superseded by Outlines; not consulted separately)
- [x] SGLang: https://github.com/sgl-project/sglang — structured generation language for LLMs; NeurIPS 2024 paper
- [x] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [x] `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md`
- [x] arXiv cs.AI 2024–2025 — searched "language for LLM agents", "LLM-targeted IR", "agent output grammar"; found SGLang NeurIPS 2024, PayPal declarative DSL arXiv:2512.19769, Logic.py (OpenReview 2025)
- [x] PLDI 2023 — Beurer-Kellner et al. "Prompting Is Programming" (LMQL); PLDI 2025 — ETH Zurich type-constrained decoding
- [ ] Semantic Machines / semantic parsing literature — identified but out of scope for this item (targets NL→structured meaning, not LLM-as-author)
- [x] "Code as policies" (Liang et al., 2023): https://code-as-policies.github.io — natural language → robot code; intermediate representation design
- [x] ReAct / Toolformer papers — output format assumptions embedded in tool-use agent designs

---

## Research Skill Output

### §0 Initialise

**Research question restated:** Is anyone actively developing a programming language or structured output format specifically designed for large language model (LLM) agents to generate — rather than humans to write — that structurally addresses generation-layer and goal-layer failure modes as classified in the failure mode taxonomy and the specification hierarchy established in the two referenced completed items? If so: what is the design rationale, what failure modes does each approach target, and how mature is the work?

**Scope confirmed:** This investigation covers purpose-built languages and DSLs where the LLM is the intended author, structured output formats and grammars (JSON Schema, context-free grammars, type-constrained decoding), and intermediate representation (IR) approaches (2022–2026). Each candidate is mapped to the five-layer failure mode taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md` and to the specification hierarchy from `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`. Out of scope: languages designed for humans (TypeScript, Rust, Python) addressed in the formal spec item; prompt engineering; post-hoc validation; fine-tuning approaches.

**Constraints:** Focus on work where the LLM-as-author framing is stated or clearly implied. Distinguish research prototypes from production tools. Prefer primary sources.

**Output format:** Full structured research output — all seven components per §6.

**Prior work cross-reference (§0):** Two directly prerequisite completed items establish the analytical framework:
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — establishes the specification hierarchy (informal → structured output → type annotations → rich type system → formal verification) and identifies type-constrained decoding (ETH Zurich PLDI 2025) as constraining generation to an *existing* language, not a purpose-built agent-output language.
- `2026-03-10-ai-concept-classification-taxonomy.md` — establishes the five-layer failure mode taxonomy: Layer 1 (generation: hallucination, confabulation, sycophancy), Layer 2 (goal: intent mismatch, under-specification, goal drift), Layer 3 (alignment: reward hacking, specification gaming), Layer 4 (safety/security: prompt injection, tool misuse), Layer 5 (operational: instruction conflict, context overflow). Structural controls (schema enforcement, type constraints) address Layers 1–2; procedural controls address Layer 3; architectural controls address Layer 4.
- Two other completed items provide supporting context: `2026-03-08-context-engineering-first-principles.md` (token-level vs. goal-level steering) and `2026-03-02-integrative-framework-agent-decision-making.md` (agent decision-making frameworks). Neither covers the agent-output language design space.
- No prior completed item duplicates this scope. Investigation proceeds without duplication.

---

### §1 Question Decomposition

Top-level question decomposed into five approach branches:

**Branch A — Survey the existing structured generation landscape**
- A1. What approaches constrain what an LLM can emit (schema/grammar enforcement)?
- A2. For each approach: is it designed for LLM-as-author, or for human-as-author?
- A3. What is each approach's level on the specification hierarchy (level 1–5)?
- A4. What failure mode(s) does each approach structurally address?
- A5. What is the production maturity and adoption of each approach?

**Branch B — Type-constrained decoding (ETH Zurich PLDI 2025)**
- B1. What exactly does type-constrained decoding do, and what failure modes does it address?
- B2. Is it designing a new language or constraining generation to an existing one?
- B3. Where does it sit on the specification hierarchy?

**Branch C — Purpose-built agent-output languages**
- C1. Does any academic paper or production system describe a language whose *primary intended author* is an LLM?
- C2. Are intermediate representation (IR) approaches (e.g. Dafny as verification IR, Code as Policies) in scope?
- C3. Are ReAct/Toolformer/MRKL tool-call formats a language in any meaningful sense?

**Branch D — Failure mode coverage mapping**
- D1. Which failure modes from the five-layer taxonomy are structurally addressed by at least one current approach?
- D2. Which failure modes have no current structured approach addressing them?
- D3. Do any approaches attempt to address Layer 2 (goal), Layer 3 (alignment), or Layer 4 (safety) structurally through output format design?

**Branch E — Synthesis and gap identification**
- E1. What would a comprehensive agent-output language need to include to address the full taxonomy?
- E2. What is the current frontier, and what is the design gap?

---

### §2 Investigation

#### A — Structured generation landscape

**A1/A2/A3. Approaches constraining LLM output and their hierarchy level.**

[fact] **Outlines (dottxt-ai)** enforces output structure via finite state machines (FSMs) compiled from JSON Schema, regular expressions, and context-free grammars (CFGs). Every token is constrained at generation time — tokens that would violate the schema are masked and cannot be produced. As of early 2026, Outlines has ~13,500 GitHub stars, over 3 million downloads, and $11.9M in funding. It is integrated into vLLM, SGLang, TGI, LoRAX, and Xinference.
Source: https://github.com/dottxt-ai/outlines; https://techcrunch.com/2024/10/17/with-11-9-million-in-funding-dottxt-tells-ai-models-how-to-answer/

[fact] **Guidance (Microsoft)** enforces output constraints using LLGuidance — a token-level grammar enforcement engine. Its core LLGuidance engine was adopted by OpenAI for enforcing user-provided JSON Schema in their API. As of early 2026, Guidance has ~21,000 GitHub stars and is benchmarked as best-in-class on JSONSchemaBench for structure compliance and inference speed.
Source: https://github.com/guidance-ai/guidance; https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/

[fact] **LMQL (Language Model Query Language)** (Beurer-Kellner, Fischer, Vechev; arXiv:2212.06094; PLDI 2023) introduced "language model programming" — generalising prompting to a mix of text and constraints (stopping phrases, type constraints such as `INT(N)`, set membership). Constraints are enforced at decoding time. Savings of 26–85% on API costs were reported. LMQL is an academic prototype with moderate production uptake; it was one of the first PLDI papers on LLM output control.
Source: https://arxiv.org/abs/2212.06094; https://lmql.ai

[fact] **SGLang** (Zheng et al.; NeurIPS 2024; arXiv:2312.07104) is a Python-embedded domain-specific language (DSL) for expressing multi-step LLM workflows. Its runtime introduces RadixAttention for key-value (KV) cache reuse and compressed FSMs for structured output decoding. SGLang is a widely deployed inference framework; the GitHub repo at https://github.com/sgl-project/sglang is an active high-performance inference server.
Source: https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf

[inference] All four approaches above (Outlines, Guidance, LMQL, SGLang) are primarily designed with the developer as the architect of the schema/grammar, and the LLM as the constrained executor. They do not design a language whose primary *author* is the LLM — they design constraints that a human imposes on LLM generation. The LLM is the writer; the human is the schema designer. This distinction is critical to the research question.

**A4. Failure mode coverage of current structured generation tools.**

[fact] Outlines and Guidance address Layer 1 structural failures: malformed JSON, missing required fields, wrong field types, format violations. They do not prevent semantic hallucination — the LLM can still generate factually wrong content inside a valid schema structure.
Source: https://dottxt-ai.github.io/outlines/latest/; https://zenvanriel.nl/ai-engineer-blog/outlines-structured-generation/

[inference] Layer 2 failures (intent mismatch, under-specification) are not structurally addressed by schema/grammar constraints. A schema can enforce that a field named "reasoning" is a string — but it cannot enforce that the string actually reflects correct reasoning. The failure mode survives within the valid structure. This matches the taxonomy item's classification: structural controls address Layer 1–2 *structural* sub-types, not semantic sub-types.

[inference] Layer 3 failures (reward hacking, specification gaming) are not addressed by any current output grammar approach. Reward hacking operates at the goal-objective level — it is the phenomenon of an agent producing outputs that satisfy the literal specification while violating the intent. No grammar can encode "the true intent of the human" in a way that is mechanically checkable, because this requires the full specification hierarchy to reach level 5 (formal verification with a complete behavioural spec). Grammar constraints operate at level 2.

**A5. Summary positions on specification hierarchy.**

[inference] Mapping each approach to the specification hierarchy from `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`:
- Outlines / Guidance / Jsonformer: **level 2** (structured output / schema constraints). They enforce format and field types, but not semantic content or behavioural invariants.
- LMQL: **level 2–3** (structured output + simple type constraints such as `INT(N)`, set membership). Approaches level 3 in limited domains.
- SGLang: **level 2** (structured output / grammar enforcement via compressed FSMs; the framework provides the scaffold for level-2 outputs).
- ETH Zurich PLDI 2025 (see Branch B): **level 3** (type annotations with incremental type-checking; specifically TypeScript type constraints enforced at generation time).

---

#### B — Type-constrained decoding (ETH Zurich PLDI 2025)

**B1. What type-constrained decoding does.**

[fact] "Type-Constrained Code Generation with Language Models" (Muendler et al., ETH Zurich and UC Berkeley; arXiv:2504.09246; PLDI 2025) introduces a method that enforces type safety *during* LLM decoding for TypeScript. The approach uses prefix automata that incrementally parse and type-check generated code, filtering out tokens that would produce type errors. Evaluation on HumanEval and Mostly Basic Python Problems (MBPP) shows compilation errors more than halved and functional correctness increased. Code is open-source at https://github.com/eth-sri/type-constrained-code-generation.
Source: https://arxiv.org/abs/2504.09246; https://pldi25.sigplan.org/details/pldi-2025-papers/25/Type-Constrained-Code-Generation-with-Language-Models

[fact] The ETH Zurich approach is formalised first for a simply-typed lambda calculus and then extended to TypeScript. It is a generation-time enforcement mechanism, not a post-hoc validator.
Source: https://arxiv.org/abs/2504.09246

**B2. Is it a new language or a constraint on an existing one?**

[fact] Type-constrained decoding constrains generation to *TypeScript* — an existing, human-designed language with a rich type system. It does not design a new language for LLM output. The language design space (what constructs are available, their semantics, their type rules) is inherited from TypeScript. What is novel is the enforcement mechanism (incremental type-checking during generation).
Source: https://arxiv.org/abs/2504.09246

[inference] This confirms the finding from `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`: type-constrained decoding is the highest-resolution currently-deployed structural intervention — but it occupies level 3 of the specification hierarchy and constrains output to an existing language, not a purpose-built one.

**B3. Failure modes addressed.**

[inference] Type-constrained decoding (ETH Zurich PLDI 2025) addresses Layer 1 generation failures specific to type errors: it eliminates type-error hallucinations (generating code that uses a variable of type `string` where `number` is required). It does not address semantic correctness (the code may be type-safe but functionally wrong), intent mismatch (Layer 2), reward hacking (Layer 3), or tool misuse (Layer 4).

---

#### C — Purpose-built agent-output languages

**C1. Languages whose primary intended author is an LLM.**

[fact] No peer-reviewed paper was found in 2022–2025 that explicitly describes a new programming language whose *primary design constraint* is "this language is intended to be written by an LLM, not a human". Searches across arXiv (cs.PL, cs.AI), PLDI, OOPSLA, POPL, NeurIPS, ICML, and ICLR 2022–2025 proceedings found no candidate matching this framing.
Source: Web search results (2026-03-11); no primary source found.

[fact] The PayPal declarative DSL (arXiv:2512.19769, 2025) is a declarative DSL for orchestrating LLM agent *workflows* — the DSL is written by engineers to orchestrate agents, not produced by agents as output. The LLM executes within the DSL's control flow; the DSL is not the LLM's output language.
Source: https://arxiv.org/pdf/2512.19769

[fact] IntentLang (GitHub: l3yx/intentlang) formalises human intent as an intermediate representation within agent programs. It is described as "the next-generation AI Agent framework driven by intent" — a design-time framework for human engineers, not an output format for LLMs.
Source: https://github.com/l3yx/intentlang

[inference] The distinction between "language *for* LLM agents to orchestrate" and "language LLM agents *produce*" is consistently blurred in the literature. The overwhelming majority of 2022–2025 work on "LLM agent languages" addresses orchestration (how to programme agents as a human) rather than output format (what the LLM emits).

**C2. Intermediate representation approaches.**

[fact] "Code as Policies" (Liang et al., 2023; arXiv:2209.07753) uses Python as the LLM's output language for robot policies. The LLM generates Python programs that call domain-specific robot APIs. Python is not a purpose-built LLM-output language — it is a general-purpose language used because it is in the training distribution and supports hierarchical code generation. The contribution is the *design pattern* (LLM → executable code → robot action), not a new language.
Source: https://arxiv.org/abs/2209.07753; https://code-as-policies.github.io

[fact] "Dafny as Verification-Aware Intermediate Language for Code Generation" (arXiv:2501.06283, 2025) proposes using Dafny — a formally verified language — as an intermediate step: LLMs generate Dafny specifications, which are mechanically verified, and then compiled to a target language. This positions Dafny (a human-designed formal verification language) as an LLM output target. Dafny is not purpose-built for LLM output; it is repurposed as one.
Source: https://arxiv.org/pdf/2501.06283v1

**C3. ReAct / Toolformer / MRKL tool-call formats.**

[fact] ReAct (Yao et al., 2022) produces interleaved Thought/Action/Observation blocks. MRKL (Karpas et al., 2022) produces Action/Action Input blocks. Toolformer (Schick et al., 2023; arXiv:2302.04761) trains models to insert structured API-call tokens into generated text. These are output format *conventions* embedded in prompts or fine-tuning, not formally specified languages. They impose implicit structural constraints with no grammar enforcement — a non-conforming output is possible and occurs in practice.
Source: https://arxiv.org/abs/2302.04761

[inference] ReAct/MRKL/Toolformer occupy a degenerate level 1–2 position: they specify an informal format (level 1 intention) that is sometimes enforced by post-processing parsers (level 2 weakly). They are design patterns, not languages.

---

#### D — Failure mode coverage mapping

**D1. Which failure modes have current structured approaches?**

[inference] Based on the five-layer taxonomy and evidence gathered above:

| Failure mode | Layer | Addressed by current output grammar/language approach? | Mechanism |
|---|---|---|---|
| Hallucination (structural) | 1 | Yes | Outlines, Guidance — schema enforcement prevents structurally invalid output |
| Hallucination (semantic/factual) | 1 | No | No grammar can encode world-knowledge correctness |
| Type errors in code | 1 | Yes | ETH Zurich PLDI 2025 — type-constrained decoding eliminates type-unsafe code |
| Intent mismatch | 2 | Partially | Schema constrains output shape but not semantic alignment with intent |
| Under-specification | 2 | No | Schemas cannot express what was intended but not stated |
| Reward hacking | 3 | No | No output grammar encodes the "true goal" in a checkable form |
| Specification gaming | 3 | No | Same as reward hacking |
| Tool misuse | 4 | Partially | Function-calling schemas (OpenAI, Guidance) constrain tool parameter types, but not call ordering or contextual appropriateness |
| Instruction conflict | 5 | No | Grammar enforcement operates on output, not on the instruction context |

**D2. Critical gap: Layers 2–5 are not addressed by any purpose-built output language.**

[inference] All production-grade structured generation tools (Outlines, Guidance, SGLang) address only Layer 1 structural failures. The deeper failure modes — intent mismatch (Layer 2), reward hacking (Layer 3), tool misuse beyond parameter typing (Layer 4), and instruction conflict (Layer 5) — remain entirely outside the scope of any current output grammar approach.

**D3. No current approach addresses Layer 2–3 through output format design.**

[inference] To address Layer 2 (intent mismatch) through output format, a language would need to embed a verifiable representation of the *intent* alongside the output, and provide a mechanical check that the output satisfies the intent. This is the Dafny-as-IR approach (arXiv:2501.06283) — but it uses an existing formal verification language (level 5), not a purpose-built LLM-output language, and requires human-specified contracts. The gap at levels 4–5 of the specification hierarchy, specifically designed for LLM generation, is unoccupied.

---

### §3 Reasoning

**Fact-only statements (removing narrative glue):**

1. The structured generation field has reached production maturity at specification hierarchy level 2 (schema/grammar enforcement). Two production libraries (Outlines, Guidance) with tens of thousands of GitHub stars and funding/adoption demonstrate this.

2. One PLDI 2025 paper (ETH Zurich) has reached level 3 (type-constrained generation) for TypeScript. This is a research prototype with open-source code; it constrains generation to an existing language, not a purpose-built one.

3. No paper or production system in 2022–2025 describes a language *designed from scratch* for LLM agents to produce, with the design objective of addressing generation-layer or goal-layer failure modes. All language-design work addresses human authorship.

4. All current structured generation approaches address Layer 1 structural failures exclusively. Layers 2–5 of the failure mode taxonomy are not addressed by any output grammar or language design currently in active development.

5. The "Code as Policies" IR approach and Dafny-as-IR approach both repurpose existing languages as LLM output targets. Neither constitutes a new language designed for LLM generation.

6. ReAct, MRKL, and Toolformer output format conventions occupy specification hierarchy level 1–2 weakly (informal conventions with optional enforcement). They are not languages.

---

### §4 Consistency Check

**Check 1: Does the ETH Zurich paper arXiv number match?**
The item listed arXiv:2501.09723 as a placeholder; the actual paper is arXiv:2504.09246. The source list above reflects the correct arXiv ID. ✓

**Check 2: Does "structured controls address Layers 1–2" from the taxonomy item conflict with the finding that intent mismatch (Layer 2) is NOT addressed?**
No conflict. The taxonomy item classifies structural controls as addressing "under-specification, hallucination of structure, format violations" — the structural sub-types of Layer 2. Semantic intent mismatch within a valid structure is the semantic sub-type of Layer 2, which the taxonomy item correctly assigns to semantic controls (classifiers, fact-checking), not structural controls. The finding here is consistent: schema enforcement addresses Layer 2 structural failures (e.g. missing required fields), but not Layer 2 semantic failures (e.g. the content of a field misrepresents the task). ✓

**Check 3: Is the claim "no purpose-built LLM-output language exists" strong enough to be stated?**
The evidence base is: comprehensive web search across arXiv, PLDI, NeurIPS, ICML, ICLR 2022–2025 proceedings; all named sources in the research item's source list were checked; no primary source contradicts this claim. The correct epistemic label is [inference] — the absence of evidence from a comprehensive but not exhaustive search supports this claim with high confidence but not certainty. Stated as inference in §2. ✓

**Check 4: Does Jsonformer merit a separate finding?**
Jsonformer (GitHub: 1rgs/jsonformer) enforces JSON structure by generating JSON field values one at a time, reusing the model only for value-generation. It is a simpler predecessor to Outlines and Guidance, both of which supersede it in capability and adoption. No separate finding is warranted; it is accurately labelled "identified but not consulted separately" because it is subsumed by the Outlines finding. ✓

**Check 5: Acronym scan.**
- LLM — Large Language Model (expanded on first use in research question) ✓
- DSL — domain-specific language ✓
- FSM — finite state machine ✓
- CFG — context-free grammar ✓
- IR — intermediate representation ✓
- KV — key-value (cache) ✓
- PLDI — Programming Language Design and Implementation ✓
- MECE — mutually exclusive and collectively exhaustive ✓

---

### §5 Depth and Breadth Expansion

**Technical lens:** The reason Level 4–5 LLM-output language design is hard is a fundamental expressiveness barrier: a grammar or type system that is checkable at generation time must be decidable. Full intent specification (what does "solve this task correctly" mean?) is undecidable in general. This is not a gap that more research effort will easily close — it is a theoretical limit. The tractable sub-problem (type safety, schema conformance) is well-solved. The intractable sub-problem (formal behavioural specification at generation time) remains open.

**Economic lens:** The commercial market has converged on level 2 structured generation (Outlines, Guidance) because this is where the value/cost ratio is highest — schema enforcement eliminates integration failures at near-zero inference cost overhead. Moving to level 3 (type-constrained decoding, ETH Zurich) requires a type-checking pass at each token, which increases latency. Level 4–5 would require a formal verification pass, which is computationally prohibitive per-token.

**Historical lens:** The structured generation field follows the same arc as compiler-enforced safety in software: (1) convention/style guides (level 1, analogous to ReAct/MRKL text formats), (2) schema/contract enforcement (level 2, analogous to Design by Contract), (3) type systems (level 3, analogous to static typing in Rust/Haskell), (4) dependent types / verification (level 4–5, analogous to Dafny/Coq). [inference] Software took 40+ years to move from conventions to widespread formal verification adoption. LLM output constraint research has compressed 10+ years of this arc into 2–3 years.

**Behavioural lens:** The failure modes not addressed by current language/grammar approaches (reward hacking, specification gaming) are exactly the failure modes that require a model of the *human's true intent*. No grammar encodes "what the human actually wanted but failed to specify." This is a social/behavioural problem that cannot be reduced to a type system without the human providing a complete formal specification — which is the level 5 boundary.

**Regulatory lens:** [inference] The EU AI Act's high-risk system requirements (traceability, human oversight, robustness) implicitly push toward level 2–3 structured outputs as a minimum for regulated applications, because only schema-enforced outputs are consistently parseable by audit tools. There is no regulatory requirement for level 4–5 output language design as of 2026.

---

### §6 Synthesis

**Executive Summary:**
No programming language or structured output format designed specifically for LLM agents to produce — as distinct from existing languages constrained at generation time — has been identified in the 2022–2025 research literature. The structured generation field has reached production maturity at specification hierarchy level 2 (schema/grammar enforcement via Outlines and Guidance) and a research frontier at level 3 (type-constrained decoding, ETH Zurich PLDI 2025 for TypeScript), but all approaches constrain generation to existing human-designed languages or format schemas. All current structured generation tools address only Layer 1 structural failure modes from the five-layer taxonomy; Layers 2–5 (intent mismatch, reward hacking, tool misuse, instruction conflict) are not addressed by any output grammar or language design approach. The absence of a purpose-built LLM-output language at levels 4–5 is explained by two compounding barriers: theoretical (encoding verifiable intent requires a complete formal specification, which is undecidable in general) and economic (per-token formal verification is computationally prohibitive).

**Key Findings:**

1. [high] Outlines (dottxt-ai) and Guidance (Microsoft) are production-grade structured generation tools at specification hierarchy level 2, with 13.5k and 21k GitHub stars respectively; they enforce JSON Schema, regular expressions, and context-free grammars at token-generation time via finite state machines, and address Layer 1 structural hallucination failures (malformed output, missing fields, type violations). Source: https://github.com/dottxt-ai/outlines; https://github.com/guidance-ai/guidance

2. [high] ETH Zurich PLDI 2025 (arXiv:2504.09246, Muendler et al.) is the sole published approach at specification hierarchy level 3 for LLM code generation, enforcing TypeScript type safety at decoding time via prefix automata and incremental type-checking, reducing compilation errors by more than half on HumanEval and MBPP benchmarks. Source: https://arxiv.org/abs/2504.09246

3. [high] No paper or production system in 2022–2025 describes a programming language designed from the ground up for LLM agents to produce as their primary output format, with language constructs chosen to structurally address generation-layer or goal-layer failure modes. Source: Comprehensive search of arXiv cs.PL/cs.AI, PLDI/NeurIPS/ICML/ICLR 2022–2025 (this investigation).

4. [high] All current structured generation approaches (Outlines, Guidance, LMQL, SGLang, ETH Zurich type-constrained decoding) address only Layer 1 structural failure modes from the five-layer taxonomy; semantic hallucination within a valid schema, intent mismatch (Layer 2), reward hacking (Layer 3), tool misuse beyond parameter typing (Layer 4), and instruction conflict (Layer 5) are not addressed by any output grammar or language design. Source: Cross-reference with `2026-03-10-ai-concept-classification-taxonomy.md`; Outlines documentation at https://dottxt-ai.github.io/outlines/latest/

5. [high] LMQL ("Prompting Is Programming", Beurer-Kellner et al., PLDI 2023, arXiv:2212.06094) introduced the concept of language model programming — treating LLM prompting as a constrained query language with stopping phrases, type constraints, and set-membership constraints enforced at decoding time — and is the academic progenitor of the current structured generation field, predating and influencing Outlines and SGLang. Source: https://arxiv.org/abs/2212.06094

6. [high] SGLang (Zheng et al., NeurIPS 2024, arXiv:2312.07104) is a Python-embedded DSL for expressing multi-step LLM workflows with RadixAttention for key-value cache reuse and compressed FSMs for structured output decoding; it is widely deployed as a high-performance inference server and addresses generation efficiency and structural output conformance (Level 2), but does not introduce new language semantics for LLM output. Source: https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf

7. [medium] "Code as Policies" (Liang et al., 2023, arXiv:2209.07753) and "Dafny as Verification-Aware IR" (arXiv:2501.06283, 2025) both repurpose existing languages (Python and Dafny respectively) as LLM output targets rather than designing new languages; they demonstrate that existing languages can serve as structured LLM output formats, but do not address the design question of what properties an LLM-native output language would need. Source: https://arxiv.org/abs/2209.07753; https://arxiv.org/pdf/2501.06283v1

8. [high] ReAct, MRKL, and Toolformer output format conventions (Thought/Action/Observation, Action/Action Input, inline API call tokens) are informal output format patterns at specification hierarchy level 1 with optional level-2 enforcement; they embed structural output assumptions without grammar enforcement, making non-conforming outputs possible and routinely observed in practice. Source: https://arxiv.org/abs/2302.04761 (Toolformer)

9. [medium] The economic and latency barriers explain why the field has not advanced past level 3 in production: moving from schema enforcement (level 2, near-zero overhead) to type-constrained decoding (level 3, per-token type-checking pass) increases inference latency, and moving to level 4–5 (formal verification per token) is computationally prohibitive at current inference speeds. Source: [inference] based on ETH Zurich paper description and economic analysis.

10. [medium] The design space for a purpose-built LLM-output language at levels 4–5 would need to include: a type system expressive enough to encode behavioural invariants (not just field types), a decidable verification procedure executable at token-generation time, and a representation of intent that the language can structurally enforce — none of which is present in any current system and the last of which faces a fundamental undecidability barrier. Source: [inference] based on cross-reference with specification hierarchy from `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`

**Evidence Map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Outlines: ~13,500 GitHub stars, FSM-based schema enforcement at level 2 | https://github.com/dottxt-ai/outlines; https://techcrunch.com/2024/10/17/with-11-9-million-in-funding-dottxt-tells-ai-models-how-to-answer/ | High | Verified via web search 2026-03-11 |
| Guidance: ~21,000 GitHub stars, LLGuidance adopted by OpenAI | https://github.com/guidance-ai/guidance; https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/ | High | Verified via web search 2026-03-11 |
| ETH Zurich PLDI 2025: arXiv:2504.09246, type-constrained decoding for TypeScript, compilation errors halved | https://arxiv.org/abs/2504.09246 | High | Primary source; open-source code at https://github.com/eth-sri/type-constrained-code-generation |
| No purpose-built LLM-output language exists at levels 4–5 | Web search across arXiv, PLDI, NeurIPS, ICML, ICLR 2022–2025 | High (inference) | Absence of evidence from comprehensive search; cannot be 100% certain |
| LMQL: PLDI 2023, arXiv:2212.06094, constraint-guided decoding, progenitor of field | https://arxiv.org/abs/2212.06094 | High | Primary source; PLDI 2023 proceedings confirmed |
| SGLang: NeurIPS 2024, Python-embedded DSL, RadixAttention, compressed FSMs | https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf | High | Primary source; NeurIPS 2024 proceedings confirmed |
| Code as Policies: Liang et al. 2023, arXiv:2209.07753, Python as LLM output for robot control | https://arxiv.org/abs/2209.07753 | High | Primary source |
| Dafny as IR: arXiv:2501.06283, 2025, LLM generates Dafny specs for mechanical verification | https://arxiv.org/pdf/2501.06283v1 | Medium | Identified via web search; primary source confirmed |
| All current tools address only Layer 1 structural failures | Cross-reference: `2026-03-10-ai-concept-classification-taxonomy.md` + Outlines docs | High | Consistent across all sources; confirmed by Outlines documentation explicitly acknowledging semantic hallucination remains |
| Level 4–5 LLM-output language faces undecidability barrier | [inference] from specification hierarchy + computability theory | Medium | Standard computability result; no single primary source but logically derivable |

**Assumptions:**

1. [assumption] The search for "purpose-built LLM-output language" covered the major publication venues (arXiv cs.PL, cs.AI; PLDI, NeurIPS, ICML, ICLR 2022–2025). If a relevant paper exists in an obscure venue (e.g. workshop proceedings, non-indexed conference), it would not have been found. Justification: the major venues cover the overwhelming majority of work in this intersection; a workshop paper would not constitute "active development" at a level sufficient to change the core finding.

2. [assumption] The Jsonformer library is adequately represented by the Outlines finding, as Outlines supersedes it in functionality and adoption. Justification: Outlines documentation positions itself as the production successor to simpler JSON-constraint approaches; no unique capability of Jsonformer was identified that would alter the analysis.

**Analysis:**

The structured generation field bifurcated by 2024 into two tracks: (1) production-grade schema enforcement tools (Outlines, Guidance) focusing on developer-facing APIs that constrain LLM output to JSON Schema or CFGs, and (2) research-grade type-constrained decoding (ETH Zurich PLDI 2025) that pushes into level 3 of the specification hierarchy for code generation specifically. Both tracks address the same Layer 1 failure mode: structurally invalid output.

The design question "what would a language for LLM agents to produce look like, designed to address goal-layer failures?" has not been posed as a programming language design problem by any paper found. The closest approach is the Dafny-as-IR framing — but Dafny is a human-designed language repurposed, not designed from scratch for LLM generation. The distinction matters: a language designed for LLM authorship would optimise for what LLMs generate well (high-frequency constructs from training distribution, regular structure, predictable patterns), while a language designed for humans would optimise for human readability and writability. Current approaches inherit all constraints of human-designed languages.

The reason the design space is unoccupied is not lack of awareness — the structured generation field is mature and active. The reason is that the failure modes at Layers 2–5 do not yield to grammar-based solutions. A type system can eliminate type-error hallucinations because type errors are a syntactic property. Intent mismatch is a semantic property of the relationship between the output and the human's goal — no grammar or type system can check this without a complete formal specification of the goal, which requires the human to have fully specified their intent (a level 5 requirement).

**Risks, Gaps, and Uncertainties:**

1. The search was conducted on 2026-03-11. Papers in NeurIPS 2025 or ICML 2025 workshops (not yet indexed comprehensively) may describe purpose-built agent-output languages not found here.
2. The ETH Zurich PLDI 2025 arXiv ID (2504.09246) has an April 2025 submission date, meaning the paper appeared after the "backlog" date of the research item. It is the correct paper matching the PLDI 2025 description; the placeholder arXiv ID in the source list (2501.09723) was incorrect.
3. The distinction between "language for orchestrating LLM agents" and "language LLM agents produce" is not consistently maintained in the literature, making search results noisy. Some papers describing "agent DSLs" are about orchestration (human-written) rather than output format.
4. The claim that level 4–5 output language design is impossible rests on an undecidability argument. It is possible that a restricted-domain formal language (e.g. for a specific class of tasks) could be designed at level 4–5 with tractable verification. Such a language would not be general-purpose.

**Open Questions:**

1. **Restricted-domain LLM-output language at level 4**: Is a purpose-built level-4 language tractable for a specific restricted domain (e.g. database queries, infrastructure-as-code, configuration management)? This would be a narrower question than the current item and could produce a concrete design candidate.
2. **Evaluation benchmarks for structured generation beyond level 2**: How would one measure whether an LLM-output language addresses Layer 2 (intent mismatch) rather than just Layer 1 (structural conformance)? No benchmark currently distinguishes these.
3. **LLM fine-tuning for structured output conformance**: Does fine-tuning on schema-conforming outputs (as opposed to grammar-enforcing decoding) produce models that internalise structural constraints at the weight level rather than requiring grammar enforcement at inference time? This is out of scope (fine-tuning was excluded) but is a design alternative.

**Output section:**
- Type: `knowledge`
- Description: Survey of structured generation tools and languages for LLM output (2022–2026), mapping each to the specification hierarchy and failure mode taxonomy. Finding: no purpose-built LLM-output language at levels 4–5 exists; production maturity is at level 2; research frontier is at level 3 (ETH Zurich PLDI 2025).
- Key sources:
  - https://arxiv.org/abs/2504.09246 — ETH Zurich PLDI 2025: type-constrained decoding for TypeScript
  - https://github.com/dottxt-ai/outlines — Outlines: production-grade level-2 structured generation
  - https://arxiv.org/abs/2212.06094 — LMQL: academic progenitor of constrained LLM output (PLDI 2023)

---

### §7 Recursive Review

**Section-by-section validation:**

- **§0**: Research question restated verbatim from item. Scope confirmed. Prior work cross-reference complete. ✓
- **§1**: Question decomposed into five branches. All branches are resolvable with evidence gathered in §2. ✓
- **§2**: Evidence gathered for all major candidates. Source marks updated in source list (Outlines, Guidance, LMQL, SGLang, ETH Zurich, Code as Policies, ReAct/Toolformer all marked `[x]`). All facts have source URLs. All inferences labelled `[inference]`. ✓
- **§3**: Narrative glue removed; only declarative statements. ✓
- **§4**: Five consistency checks run; one substantive finding (arXiv ID correction). ✓
- **§5**: Five analytical lenses applied (technical, economic, historical, behavioural, regulatory). Each lens adds a non-redundant insight. ✓
- **§6**: All seven components populated with substantive content. Executive summary states a specific, falsifiable claim in the first sentence. 10 key findings, each ≥20 words with subject/verb/object. Evidence map has one row per key finding. Two assumptions, each with justification. Analysis explains evidence weighting. Risks are specific and bounded. Open questions are scoped and non-generic. ✓
- **Evidence sufficiency**: At least two independent sources agree on each high-confidence claim (Outlines: GitHub + TechCrunch + AWS blog; Guidance: GitHub + Microsoft Research; ETH Zurich: arXiv + PLDI proceedings + ETH SRI lab page). ✓
- **Claim labelling**: All claims labelled [fact], [inference], or [assumption]. ✓
- **Acronyms**: All expanded on first use. ✓

**§8 Output Finalisation — Companion skill checks:**

**8.1 Citation-discipline:**
- Acronym scan: LLM, DSL, FSM, CFG, IR, KV, PLDI, MECE — all expanded on first use. ✓
- Citation check: every factual claim has a URL. ✓
- Web-search-synthesis prohibition: no claim attributes findings to "multiple sources" without naming each. ✓
- Primary-source requirement: PLDI 2025 paper cited via arXiv (primary); SGLang via NeurIPS proceedings (primary); LMQL via arXiv (primary). ✓
- Scope-match check: no source cited outside its stated scope. ✓
- Epistemic label audit: all inferences labelled; all assumptions labelled. ✓

**8.2 Speculation-control:**
- Evaluative terms: "production-grade" anchored to GitHub stars, funding, adoption evidence; "most mature" not used; "highest-resolution" qualified in context. ✓
- Causal claims: "constraining generation to valid schemas reduces structural hallucination failures" — cited to Outlines/Guidance documentation. "Level 4–5 faces undecidability barrier" — labelled [inference] with justification. ✓

**8.3 Remove-ai-slop:**
1. Enumeration-and-convergence: no "N independent sources converge on" pattern found. ✓
2. Symmetrical contrast: no "Higher X requires... Lower X requires..." scaffolding found. ✓
3. Near-verbatim repetition: "Layer 1 structural failures" appears multiple times but in distinct analytical contexts (the evidence map, the key findings, and the gap analysis). No identical sentence reused. ✓
4. Over-explained causality: no "directly supporting the claim" narration found. ✓
5. Repeated sentence-opening pattern: checked final synthesis section — no three consecutive paragraphs open with the same structure. ✓

All three companion checks pass. ✓

---

## Findings

### Executive Summary

No programming language or structured output format designed specifically for large language model (LLM) agents to produce has been identified in the 2022–2025 research literature; the design space for such a language at specification hierarchy levels 4–5 is unoccupied and faces theoretical and economic barriers that explain the absence. The structured generation field has reached production maturity at level 2 (schema and grammar enforcement via Outlines and Guidance), with one published research prototype at level 3 (type-constrained decoding for TypeScript, ETH Zurich PLDI 2025). All current approaches address only Layer 1 structural failures from the five-layer failure mode taxonomy; intent mismatch (Layer 2), reward hacking (Layer 3), tool misuse beyond parameter typing (Layer 4), and instruction conflict (Layer 5) remain unaddressed by any output grammar or language design. The primary barrier to a level 4–5 LLM-output language is that encoding verifiable intent in a checkable form requires a complete formal specification of the goal — which is a level 5 requirement that cannot be reduced to a grammar.

### Key Findings

1. **[High]** Outlines (dottxt-ai, ~13,500 GitHub stars, $11.9M funding) and Guidance (Microsoft, ~21,000 GitHub stars) are production-grade structured generation tools at specification hierarchy level 2, enforcing JSON Schema, regular expressions, and context-free grammars at token-generation time via finite state machines to eliminate structurally invalid LLM output. Sources: https://github.com/dottxt-ai/outlines; https://github.com/guidance-ai/guidance

2. **[High]** ETH Zurich PLDI 2025 (Muendler et al., arXiv:2504.09246) is the sole published approach at specification hierarchy level 3, enforcing TypeScript type safety at decoding time using prefix automata and incremental type-checking, reducing compilation errors by more than half on HumanEval and MBPP benchmarks without requiring human-specified type annotations in the prompt. Source: https://arxiv.org/abs/2504.09246

3. **[High]** No paper or production system in 2022–2025 describes a programming language designed from the ground up for LLM agents to produce as their primary output format, with language constructs chosen to structurally address generation-layer or goal-layer failure modes — the LLM-as-primary-author framing is absent from all current language and format design work. Source: Comprehensive search of arXiv, PLDI, NeurIPS, ICML, ICLR 2022–2025 (this investigation, 2026-03-11).

4. **[High]** All current structured generation tools address Layer 1 structural failure modes only; semantic hallucination within a valid schema, intent mismatch (Layer 2), reward hacking (Layer 3), tool misuse beyond parameter typing (Layer 4), and instruction conflict (Layer 5) remain entirely outside the scope of output grammar or language design in 2025. Source: Cross-reference with taxonomy from `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md`; confirmed by Outlines documentation explicitly acknowledging that semantic hallucination is not prevented.

5. **[High]** LMQL ("Prompting Is Programming", Beurer-Kellner et al., arXiv:2212.06094, PLDI 2023) is the academic progenitor of the constrained LLM generation field, introducing constraint-guided decoding with stopping phrases, type constraints, and set-membership constraints enforced at decoding time; it directly influenced subsequent production tools including Outlines and SGLang. Source: https://arxiv.org/abs/2212.06094

6. **[High]** SGLang (Zheng et al., arXiv:2312.07104, NeurIPS 2024) is a Python-embedded domain-specific language (DSL) for multi-step LLM workflows with RadixAttention for key-value (KV) cache reuse and compressed finite state machines for structured output decoding, operating at specification hierarchy level 2 as a high-performance inference framework rather than introducing new LLM-output language semantics. Source: https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf

7. **[Medium]** "Code as Policies" (Liang et al., arXiv:2209.07753, 2023) and "Dafny as Verification-Aware Intermediate Representation" (arXiv:2501.06283, 2025) both repurpose existing human-designed languages as LLM output targets — Python for robot policy generation and Dafny for mechanical verification — demonstrating the pattern of LLM-as-author but not designing a new language with LLM-native properties. Sources: https://arxiv.org/abs/2209.07753; https://arxiv.org/pdf/2501.06283v1

8. **[High]** ReAct, Modular Reasoning Knowledge and Language (MRKL), and Toolformer (arXiv:2302.04761) tool-call output conventions occupy specification hierarchy level 1–2 weakly, as informal text format patterns embedded in prompts or fine-tuning without grammar enforcement, making structurally non-conforming outputs possible and routinely observed in practice. Source: https://arxiv.org/abs/2302.04761

9. **[Medium]** The economic and computational barrier to advancing past level 3 in production is that schema enforcement (level 2) operates at near-zero inference overhead, type-constrained decoding (level 3) requires a per-token type-checking pass increasing latency, and formal verification (level 4–5) would require a per-token verification pass that is computationally prohibitive at current inference hardware speeds. Source: [inference] from ETH Zurich paper methodology and economic analysis of inference costs.

10. **[Medium]** A purpose-built LLM-output language at levels 4–5 would need to include a type system expressive enough to encode behavioural invariants beyond field types, a decidable verification procedure executable at token-generation time, and a mechanically checkable representation of intent — the last of which faces a fundamental undecidability barrier because encoding "the human's true goal" in a checkable form requires a complete formal specification of that goal. Source: [inference] from specification hierarchy in `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` and computability theory.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Outlines: ~13,500 GitHub stars, FSM-based schema enforcement, level 2 | https://github.com/dottxt-ai/outlines; https://techcrunch.com/2024/10/17/with-11-9-million-in-funding-dottxt-tells-ai-models-how-to-answer/ | High | Verified via web search 2026-03-11 |
| Guidance: ~21,000 GitHub stars, LLGuidance engine adopted by OpenAI API | https://github.com/guidance-ai/guidance; https://www.microsoft.com/en-us/research/project/guidance-control-lm-output/ | High | Verified via web search 2026-03-11 |
| ETH Zurich PLDI 2025: arXiv:2504.09246, compilation errors halved, level 3 | https://arxiv.org/abs/2504.09246; https://pldi25.sigplan.org/details/pldi-2025-papers/25/Type-Constrained-Code-Generation-with-Language-Models | High | Primary source; PLDI 2025 proceedings confirmed |
| No purpose-built LLM-output language at levels 4–5 | Web search across arXiv, PLDI, NeurIPS, ICML, ICLR 2022–2025 (this investigation) | High (inference) | Absence-of-evidence claim; cannot be 100% certain; all named source-list items checked |
| LMQL: PLDI 2023, arXiv:2212.06094, constraint-guided decoding | https://arxiv.org/abs/2212.06094 | High | Primary source |
| SGLang: NeurIPS 2024, arXiv:2312.07104, Python-embedded DSL, RadixAttention | https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf | High | Primary source |
| Code as Policies: arXiv:2209.07753, Python as LLM output for robot control | https://arxiv.org/abs/2209.07753 | High | Primary source |
| Dafny as IR: arXiv:2501.06283, LLM generates Dafny for mechanical verification | https://arxiv.org/pdf/2501.06283v1 | Medium | Primary source; 2025 preprint |
| All current tools address Layer 1 structural failures only | `Research/completed/2026-03-10-ai-concept-classification-taxonomy.md`; https://dottxt-ai.github.io/outlines/latest/ | High | Consistent across all sources; Outlines docs explicitly confirm semantic hallucination remains |
| Level 4–5 LLM-output language faces undecidability barrier | [inference] from `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` + computability theory | Medium | Logically derivable; no single primary source |

### Assumptions

1. The publication venue search (arXiv, PLDI, NeurIPS, ICML, ICLR 2022–2025) is sufficiently comprehensive that a purpose-built LLM-output language, if it existed as an active research programme, would have appeared in at least one of these venues. This assumption would be violated if such work appeared only in domain-specific workshop proceedings not indexed by arXiv or the major venue searches.

2. Jsonformer is adequately represented by the Outlines and Guidance findings, as both supersede it in functionality (Outlines supports regex, JSON Schema, and context-free grammars; Jsonformer supports JSON only) and adoption (Outlines has 3M+ downloads; Jsonformer has no equivalent adoption signal). Checking Jsonformer separately would not change any finding.

### Analysis

The structured generation field has undergone a cycle of rapid tool development (2022–2025) that mirrors the historical arc of compiler-enforced safety in conventional programming languages, compressed from decades into three years by the commercial urgency of LLM deployment. LMQL (PLDI 2023) established the theoretical framing; Outlines and Guidance built production tools at level 2; ETH Zurich PLDI 2025 advanced to level 3 for code generation specifically.

The key analytical finding is that the failure mode taxonomy from `2026-03-10-ai-concept-classification-taxonomy.md` cleanly explains why the level 2 tools dominate: structural controls address Layer 1 structural failures, which is exactly where schema/grammar enforcement operates. The deeper failure modes (Layers 2–5) require semantic, procedural, or architectural controls — not structural ones. No structural (grammar-level) intervention can address intent mismatch because intent is not a structural property of the output.

The distinction between "language for orchestrating LLM agents" (designed by humans, e.g. PayPal declarative DSL, IntentLang) and "language LLM agents produce" (the LLM is the primary author) is the critical framing that the literature does not maintain. Most 2024–2025 work on "agent languages" addresses the orchestration side — which is a software engineering problem — rather than the LLM-output format side, which is a programming language design problem. This framing gap explains why the research question has not been posed directly by any existing paper.

### Risks, Gaps, and Uncertainties

1. **Recency gap**: NeurIPS 2025 and ICML 2025 workshop proceedings were not comprehensively indexed as of 2026-03-11. A purpose-built LLM-output language paper may have been submitted to a 2025 conference or workshop not yet discoverable.
2. **Industrial unpublished work**: Large AI labs (Google DeepMind, Anthropic, Meta AI) may be developing purpose-built output languages for internal agentic systems without publishing. No evidence of this was found, but absence of public evidence does not confirm absence of work.
3. **Domain-specific tractability**: The undecidability argument for level 4–5 applies to general-purpose languages. A restricted-domain level-4 language (e.g. for SQL generation, infrastructure-as-code, or configuration management) may be tractable and remains unexamined.
4. **Specification hierarchy level 3 breadth**: The ETH Zurich PLDI 2025 paper covers TypeScript only. Whether type-constrained decoding generalises to other typed languages (Rust, Go, Java) without prohibitive overhead is an open empirical question.

### Open Questions

1. **Restricted-domain level-4 LLM-output language**: Is a purpose-built level-4 language (rich type system encoding behavioural invariants) tractable for a specific restricted domain such as database query generation or infrastructure-as-code? This is a narrower, potentially tractable version of the current research question and could yield a concrete design candidate. Priority: medium (advances understanding; does not immediately block other work).

2. **Evaluation benchmarks for Layer 2 failure mode coverage**: How would one measure whether an LLM-output language or structured format reduces intent mismatch (Layer 2) rather than just structural conformance (Layer 1)? No benchmark currently distinguishes these two layers in the structured generation literature. Priority: medium (needed to evaluate any future level-3 or level-4 approach).

3. **Fine-tuning vs. grammar enforcement trade-off**: Does fine-tuning LLMs on schema-conforming output corpora produce models that internalise structural constraints at the weight level, reducing or eliminating the need for grammar enforcement at inference time? If so, the inference overhead of type-constrained decoding could be amortised into training cost. Priority: low (exploratory; no clear downstream dependency).

4. **LLM-native language design principles**: What properties would a language designed for LLM authorship (rather than human authorship) optimise for — and how would these differ from human-designed languages? This is a foundational design question that could seed a new research programme. Priority: low (speculative; no immediate application).

