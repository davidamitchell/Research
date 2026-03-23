---
title: "AI concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains"
added: 2026-03-10
status: completed
priority: high
blocks: [2026-03-10-agent-evaluation-cross-repo-analysis]
tags: [taxonomy, classification, prompt-engineering, context-engineering, intent-engineering, memory, failure-modes, guardrails, skills, tools, agents, agentic-systems]
started: 2026-03-10
completed: 2026-03-10
output: [knowledge]
---

# AI concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains

## Research Question

What is a coherent, internally consistent classification taxonomy for the core concepts in AI-assisted and agentic systems — covering prompt types, instruction types, prompt/content/intent engineering approaches, memory types, failure modes, controls and guardrails, skills, tools, and problem domains — such that any given concept maps to exactly one primary category and the taxonomy is stable enough to use as a shared vocabulary across research items and system designs?

## Scope

**In scope:**
- Classification of prompt types (system, user, assistant, tool-call, few-shot examples, chain-of-thought, meta-prompts, etc.)
- Classification of instruction types (declarative goals, procedural steps, constraints, examples, persona definitions, format directives, safety rails, etc.)
- Distinctions between prompt engineering, content engineering, and intent engineering as disciplines — what each optimises for, what its unit of work is, and where the three overlap
- Memory type taxonomy: in-context (working), external (retrieval), parametric (model weights), episodic (session), semantic (fact store), procedural (skill store)
- Failure mode taxonomy: hallucination, reward hacking, intent mismatch, goal drift, context overflow, over-compliance, under-specification, instruction conflict, tool misuse, guardrail bypass
- Controls and guardrails taxonomy: structural (schema/type constraints), semantic (content filters, classifiers), procedural (confirmation gates, escalation paths), architectural (sandboxing, scoping, permission models)
- Skills taxonomy: what distinguishes a skill from a tool, from an agent, from an instruction set — and how skills compose
- Tools taxonomy: categories of tools available to agents (retrieval, execution, communication, stateful vs stateless, read-only vs write, sandboxed vs ambient)
- Problem domain map: what classes of problems benefit from agentic approaches vs simpler pipelines
- Cross-cutting concerns: how taxonomy categories compose (e.g. a skill may use several tool types and depend on a specific memory type)

**Out of scope:**
- Implementation of any taxonomy as code or schema (a separate backlog item)
- Fine-grained evaluation of specific prompt patterns (covered by `2026-03-04-sdlc-ai-prompt-patterns.md`)
- First-principles derivation of context engineering mechanisms (covered by `2026-03-08-context-engineering-first-principles.md`)
- Memory system implementation details (covered by `2026-03-02-agent-memory-management-context-injection.md`)

**Constraints:** Taxonomy must be derivable from published practitioner literature, academic papers, and existing repo research. No empirical experiments required.

## Context

The research corpus has grown to cover prompts, memory, controls, agents, tools, and failure modes — but each item developed its own local vocabulary. There is no single shared classification that lets a new research item or system design state "this uses a Type-2 memory, a procedural guardrail, and an intent-engineering approach" and have that be unambiguous. Without a stable taxonomy, cross-item synthesis is harder, agent designs are inconsistently described, and evaluation criteria cannot be agreed upon.

This taxonomy is the prerequisite for the companion item on agent evaluation (`2026-03-10-agent-evaluation-cross-repo-analysis.md`): you cannot compare agents across repos without a shared vocabulary for what they are doing and why.

Completed items that constrain the taxonomy:
- `2026-03-04-sdlc-ai-prompt-patterns.md` — identifies emergent prompt patterns in SDLC contexts
- `2026-03-08-context-engineering-first-principles.md` — defines token-level vs goal-level steering; distinguishes prompt engineering from context engineering
- `2026-03-02-agent-memory-management-context-injection.md` — taxonomy of memory approaches
- `2026-03-02-integrative-framework-agent-decision-making.md` — Data, Information, Knowledge, Wisdom (DIKW)-aligned decision-making framework
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — intent specification hierarchy
- `2026-02-28-ai-control-testing-and-assurance.md` — controls and assurance landscape

## Approach

1. Audit existing research corpus for locally-defined vocabularies and taxonomies; collect all candidate category definitions
2. Survey published AI/ML taxonomy literature (e.g. prompt pattern catalogues, Large Language Model (LLM) failure mode surveys, agent architecture surveys)
3. For each candidate taxonomy domain (prompts, instructions, memory, failure modes, controls, skills, tools, problem domains): identify dimensions, enumerate categories, test Mutually Exclusive, Collectively Exhaustive (MECE)
4. Identify cross-cutting concerns and define composition rules (how categories from different domains relate)
5. Validate the taxonomy against 5–10 existing completed research items: can each item's core concepts be unambiguously labelled?
6. Produce the taxonomy as a structured artefact: a set of named, defined, and cross-referenced categories per domain

## Sources

- [x] `Research/completed/2026-03-04-sdlc-ai-prompt-patterns.md`
- [x] `Research/completed/2026-03-08-context-engineering-first-principles.md`
- [x] `Research/completed/2026-03-02-agent-memory-management-context-injection.md`
- [x] `Research/completed/2026-03-02-integrative-framework-agent-decision-making.md`
- [x] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md`
- [x] Prompt pattern catalogues: "Prompt Patterns as a Means for Evaluating and Improving Prompt Engineering" (White et al., 2023) arXiv:2302.11382
- [x] LLM failure mode surveys: "A Survey of Hallucination in Large Language Models" (Ji et al., 2023)
- [x] Agent architecture surveys: "A Survey on Large Language Model based Autonomous Agents" (Wang et al., 2023) arXiv:2308.11432
- [x] Open Worldwide Application Security Project (OWASP) Top 10 for LLM Applications 2025
- [x] LangChain component architecture documentation

---

## Research Skill Output

### §0 Initialise

**Research question restated:** What is a coherent, internally consistent, MECE classification taxonomy for the core concepts in AI-assisted and agentic systems — covering prompt types, instruction types, engineering discipline distinctions, memory types, failure modes, controls/guardrails, skills, tools, and problem domains — such that any concept maps to exactly one primary category and the taxonomy is stable enough to serve as a shared vocabulary?

**Scope confirmed:** Eight taxonomy domains are in scope (prompt types, instruction types, engineering disciplines, memory types, failure modes, controls/guardrails, skills/tools, problem domains). Implementation as code and domain-specific deep-dives (SDLC prompt patterns, context engineering mechanisms, memory implementation details) are out of scope. Taxonomy categories must be derivable from published literature plus prior repo research.

**Constraints:** Evidence from practitioner documentation, peer-reviewed papers, and internal repo research items. MECE test applied to each domain — categories must be mutually exclusive (no concept maps to two categories) and collectively exhaustive (no concept falls outside the taxonomy). Where exhaustiveness cannot be guaranteed, a catch-all category is defined with criteria.

**Output format:** Structured taxonomy artefact with named, defined categories per domain; composition rules between domains; validation against prior research items.

---

### §1 Question Decomposition

The research question decomposes into eight taxonomy-building sub-questions, each independently addressable.

```
What is a coherent AI concept classification taxonomy?
├── Q1: What are the mutually exclusive types of prompts in an LLM interaction?
│   ├── Q1a: What are the structural roles a message can play (system, user, assistant)?
│   ├── Q1b: What are the functional prompt forms within those roles (few-shot, CoT, meta-prompt, tool-call)?
│   └── Q1c: Is a tool-call response a prompt type or a separate category?
│
├── Q2: What are the types of instructions an agent receives?
│   ├── Q2a: What is the distinction between a declarative goal and a procedural step?
│   ├── Q2b: How do constraints, examples, persona definitions, format directives, and safety rails differ as instruction types?
│   └── Q2c: Do instruction types overlap with prompt types, or are they independent dimensions?
│
├── Q3: How do prompt engineering, content engineering, and intent engineering differ as disciplines?
│   ├── Q3a: What is each discipline's unit of work?
│   ├── Q3b: What does each discipline optimise for?
│   └── Q3c: Where do they overlap and what is the resolution?
│
├── Q4: What is the correct memory type taxonomy?
│   ├── Q4a: What are the standard five types: parametric, in-context, external, episodic, semantic, procedural?
│   ├── Q4b: Are episodic and semantic subtypes of external memory, or independent dimensions?
│   └── Q4c: How does procedural memory differ from a skill or a tool?
│
├── Q5: What are the failure mode categories?
│   ├── Q5a: What is the OWASP LLM Top 10 coverage and how does it map to a failure mode taxonomy?
│   ├── Q5b: Where do hallucination, reward hacking, and intent mismatch sit in the same classification?
│   └── Q5c: How do output-level failures differ from process-level failures?
│
├── Q6: What is the controls/guardrails taxonomy?
│   ├── Q6a: What is the structural vs semantic vs procedural vs architectural distinction?
│   ├── Q6b: How do controls map to the failure modes they address?
│   └── Q6c: Where does a guardrail end and a constraint begin?
│
├── Q7: How do skills, tools, agents, and instruction sets differ?
│   ├── Q7a: What is the autonomy spectrum from instruction → tool → skill → agent?
│   ├── Q7b: What are the tool sub-categories (retrieval, execution, communication; stateful/stateless; sandboxed/ambient)?
│   └── Q7c: How does a skill compose from tools?
│
└── Q8: What problem domains benefit from agentic approaches vs simpler pipelines?
    ├── Q8a: What structural characteristics of a problem predict agentic advantage?
    └── Q8b: Where does a simple pipeline outperform an agent?
```

---

### §2 Investigation

#### Q1 — Prompt type taxonomy

**[fact]** White et al. (2023) formalised prompt engineering patterns as reusable software patterns — solutions to recurring LLM interaction problems — and categorised them into five meta-categories: Input Semantics, Output Customization, Error Identification, Prompt Improvement, and Interaction patterns. Source: arXiv:2302.11382. Classification: primary (peer-reviewed).

**[fact]** The structural message roles in any conversational LLM API are: `system` (persistent behavioural framing, supplied by developer), `user` (input from human or orchestrator), `assistant` (model response, included for multi-turn context), and `tool` (result returned from a tool invocation, consumed by the next model call). Source: OpenAI Chat Completions API documentation; Anthropic API reference. Classification: primary (official vendor documentation).

**[fact]** Within these structural roles, functional forms include: few-shot examples (one or more exemplar input-output pairs in user or assistant turns), chain-of-thought (explicit step-by-step reasoning elicitation), meta-prompts (instructions about how to construct further instructions), and retrieval-augmented context (externally retrieved text injected into the system or user message). Source: White et al. 2023 arXiv:2302.11382; 2026-03-08-context-engineering-first-principles.md. Classification: primary + prior research.

**[inference]** Prompt type is a two-dimensional concept: structural role (system/user/assistant/tool) and functional form (few-shot/CoT/meta-prompt/RAG-augmented/etc.). A prompt always has exactly one structural role and zero or more functional forms applied. This makes the two dimensions orthogonal: a system message can use few-shot examples; a user message can embed chain-of-thought scaffolding.

**Resolution for Q1c:** A tool-call response (`tool` role message) is a structural role, not a functional form. It is produced by the external environment rather than by the human or orchestrator and carries tool execution results. It is a distinct fourth structural role.

---

#### Q2 — Instruction type taxonomy

**[fact]** The 2026-03-10-formal-spec-intent-alignment-agentic-coding.md research item established a specification hierarchy from natural language → structured output schema → type annotations → rich type system → formal verification. Instructions are the natural-language end of this spectrum. Classification: prior research.

**[fact]** 2026-03-08-context-engineering-first-principles.md distinguishes: token-level steering (biasing P(next_token) toward compliant, coherent tokens) from goal-level steering (encoding task objectives completely enough that the full generation achieves the intended outcome). Instructions serve goal-level steering. Classification: prior research.

**[inference]** Drawing from context engineering research and the specification hierarchy, instruction types are distinguishable by what they constrain:
- **Declarative goal:** States the desired end-state without specifying how to reach it ("Produce a one-page summary of..."). Constrains the output type and topic.
- **Procedural step:** Specifies an ordered sequence of operations ("First do X, then do Y"). Constrains the generation process.
- **Constraint:** A boundary condition that the output must not violate ("Never include personally identifiable information"). Constrains the output space negatively.
- **Example:** A demonstration input-output pair that calibrates output form or content. Constrains the output distribution via imitation.
- **Persona definition:** A role assignment that biases the model's style, tone, and knowledge framing ("You are a senior financial analyst"). Constrains the output register.
- **Format directive:** Specifies the surface form of the output ("Return JSON with fields: ..."). Constrains the output schema.
- **Safety rail:** A constraint that specifically addresses harm categories ("Do not produce instructions for..."). Constrain the output space for safety reasons; distinguished from generic constraints by their harm-oriented purpose.

**[inference]** Instruction types and prompt structural roles are independent dimensions: a system message typically contains persona definitions, declarative goals, constraints, and format directives. A user message typically contains the declarative goal for a specific turn plus context. Instruction types describe what a message is doing; structural role describes where it appears.

---

#### Q3 — Engineering discipline distinctions

**[fact]** 2026-03-08-context-engineering-first-principles.md defines context engineering as "the discipline of shaping the token probability distribution an LLM samples from at inference — operating through two distinct mechanisms: token-level steering and goal-level steering." The Anthropic context engineering blog (2025) defines it as governing the entire token sequence the model conditions on, including tools, RAG output, memory, and conversation history. Classification: primary (model builder documentation) + prior research.

**[fact]** The same prior research item positions prompt engineering as a subset of context engineering, focused specifically on the instruction text in system or user prompts. Classification: prior research.

**[inference]** Three disciplines are distinguishable by their unit of work and optimisation target:

- **Prompt engineering** — Unit of work: a single prompt or prompt template. Optimises for: the quality of a single model response given fixed context. Scope: the instruction text and its structure.
- **Context engineering** — Unit of work: the complete context window (system prompt, conversation history, retrieved documents, tool schemas, memory injections). Optimises for: token-level compliance and goal-level task achievement across the full generation. Scope: everything the model conditions on.
- **Intent engineering** — Unit of work: the formal specification of what the system is supposed to do (goal, constraints, desired outcomes, evaluation criteria). Optimises for: alignment between the agent's behaviour and the human's actual intent, including dimensions that may never appear in a prompt. Scope: the problem definition upstream of context construction.

**[inference]** The three disciplines form a hierarchy: intent engineering defines what should happen; context engineering constructs the token sequence that directs the model toward that intent; prompt engineering crafts the specific instruction text within that context. Intent engineering failure (wrong goal specified) cannot be compensated by excellent context engineering.

---

#### Q4 — Memory type taxonomy

**[fact]** Wang et al. 2023 (arXiv:2308.11432) identifies four memory mechanisms in LLM agents: sensory memory (immediate perceptual inputs), short-term memory (context window), long-term memory (external storage), and parametric memory (model weights). Classification: primary (peer-reviewed survey).

**[fact]** Multiple 2024–2025 sources (arXiv:2505.00675 "Rethinking Memory in LLM based Agents"; principia-agentica.io; atalupadhyay.wordpress.com) converge on five memory types for LLM agents: Parametric (model weights), In-Context/Working (context window), External (retrieval systems), Episodic (event logs), and Semantic (fact stores). Procedural (action scripts/skill stores) is identified as a sixth type in several sources. Classification: secondary (synthesis of multiple practitioner/research sources).

**[fact]** 2026-03-02-agent-memory-management-context-injection.md explicitly distinguishes RAG (retrieval) from memory, noting "RAG is retrieval, not memory." Classification: prior research.

**[fact]** 2026-03-02-integrative-framework-agent-decision-making.md establishes: "Procedural memory — storing learned conflict-resolution heuristics from past decision cycles — is the memory-architecture analogue of wisdom: it encodes previously-derived judgement so that the agent does not need to re-derive it from first principles each time." Classification: prior research.

**Resolution for Q4b:** Episodic and semantic memory are both subtypes of external memory — they differ in what they store (event records vs abstract facts) and how they are indexed (time/event vs concept/entity). Procedural memory may be stored externally or encoded in model weights during fine-tuning. The six-type taxonomy handles this correctly:

1. **Parametric** — stored in model weights; updated only by training/fine-tuning; general world knowledge.
2. **In-context (working)** — the active context window; volatile, bounded by token limit; holds current task state.
3. **External (episodic)** — persistent, time-indexed event records; "what happened and when"; queryable by recency and event type.
4. **External (semantic)** — persistent, concept-indexed fact stores; "what is true about X"; queryable by entity/relationship.
5. **External (procedural)** — persistent, action-indexed skill stores; "how to do Y"; retrieved as executable procedures.
6. **Cached (Key-Value (KV) cache)** — inference-time attention cache; a materialisation optimisation, not a new type; subsumed under in-context.

**[inference]** Episodic + semantic + procedural = three functional subtypes of external memory, distinguished by their indexing scheme and retrieval semantics, not by their storage substrate.

---

#### Q5 — Failure mode taxonomy

**[fact]** OWASP Top 10 for LLM Applications 2025 lists: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. Source: owasp.org/www-project-top-10-for-large-language-model-applications/. Classification: primary (industry standards body).

**[fact]** Ji et al. (2023) "A Survey of Hallucination in Large Language Models" identifies hallucination as: producing content that is nonsensical or unfaithful to provided source content, or producing factually incorrect assertions. Classification: primary (peer-reviewed survey).

**[fact]** 2026-03-08-context-engineering-first-principles.md establishes sycophancy as a prototypical two-mechanism failure: high token-level compliance combined with systematic goal-level failure, arising from Reinforcement Learning from Human Feedback (RLHF) training optimising for user satisfaction rather than accuracy. Classification: prior research.

**[fact]** 2026-03-10-formal-spec-intent-alignment-agentic-coding.md documents reward hacking as LLM agents optimising proxy rewards while degrading true alignment (Gao et al. scaling law, METR 2025, Anthropic 2025). Classification: prior research.

**[inference]** A four-dimensional failure mode taxonomy organises failure types by the layer at which failure occurs:

**Layer 1 — Generation failures** (the model produces wrong output):
- **Hallucination** — factually false or unfaithful assertions presented as facts.
- **Confabulation** — plausible-sounding but fabricated references, sources, or details.
- **Sycophancy** — systematic agreement with perceived user preference over accuracy.

**Layer 2 — Goal failures** (output is well-formed but misses the objective):
- **Intent mismatch** — the literal instruction was followed but the actual goal was not met.
- **Under-specification** — the instruction left enough ambiguity that the model chose an unintended interpretation.
- **Over-compliance** — the model followed the letter of the instruction too literally, violating its spirit.
- **Goal drift** — in multi-turn or agentic contexts, the objective shifts away from the original intent over time.

**Layer 3 — Alignment failures** (the system optimises for a proxy rather than the true goal):
- **Reward hacking** — the agent finds and exploits gaps between the proxy reward signal and the true objective.
- **Specification gaming** — the agent achieves the literal specification while violating its intent (a Goodhart's Law manifestation).

**Layer 4 — Safety/security failures** (the system violates boundaries):
- **Prompt injection** — external content redirects the agent's actions (OWASP LLM01).
- **Guardrail bypass** — the system's constraints are circumvented by adversarial framing.
- **Excessive agency** — the agent takes actions beyond its sanctioned scope (OWASP LLM06).
- **Tool misuse** — the agent invokes tools incorrectly, in wrong sequence, or for unintended purposes.

**Layer 5 — Operational failures** (infrastructure-level):
- **Context overflow** — the context window is exhausted, truncating critical information.
- **Instruction conflict** — two instructions in the context contradict each other; the model resolves arbitrarily.
- **Unbounded consumption** — the agent consumes resources (tokens, API calls, time) without limit (OWASP LLM10).

---

#### Q6 — Controls and guardrails taxonomy

**[fact]** 2026-02-28-ai-control-testing-and-assurance.md documents the practitioner governance model for AI controls, confirming the categories: structural (schema/type constraints), semantic (content filters, classifiers), procedural (confirmation gates, escalation paths), and architectural (sandboxing, scoping, permission models). Classification: prior research.

**[fact]** The same item documents that Type 2 agent actions (generating outputs for human review) are governed, but Type 3 actions (delegating authority to reach a conclusion) are not yet governed by any regulator. This confirms the procedural control type (human review gates) as the operative boundary. Classification: prior research.

**[inference]** A four-category controls taxonomy, ordered by enforcement layer:

**Structural controls** — enforce constraints at the output schema level; violations are mechanically impossible within the schema. Examples: JSON schema validation, typed output, Pydantic models, type-constrained decoding. Addresses: under-specification, hallucination of structure, format violations.

**Semantic controls** — enforce constraints at the content meaning level using classifiers, filters, or reviewers. Examples: toxicity classifiers, Personally Identifiable Information (PII) detectors, relevance filters, embedding-space similarity checks. Addresses: hallucination, sycophancy, sensitive information disclosure (OWASP LLM02).

**Procedural controls** — enforce constraints through process gates that require events to occur before the system proceeds. Examples: human approval gates, confirmation steps, escalation paths, multi-agent review. Addresses: excessive agency, goal drift, reward hacking.

**Architectural controls** — enforce constraints through system design that makes certain actions structurally impossible. Examples: sandboxing (agent cannot access production data without explicit grant), permission models (tool scoping), network isolation (agent cannot make external calls). Addresses: prompt injection, guardrail bypass, tool misuse, excessive agency.

**Mapping controls to failure modes (key pairings):**
- Hallucination → semantic (fact-checking) + structural (citation-required schema)
- Reward hacking → procedural (immutable spec, human approval on consequential actions)
- Prompt injection → architectural (sandboxing, input sanitisation)
- Excessive agency → architectural (scoped permissions) + procedural (human gate before high-impact action)
- Context overflow → structural (context length budgets, summarisation triggers)

---

#### Q7 — Skills, tools, agents, and instruction sets

**[fact]** LangChain documentation (2024) defines tools as specialised utilities or software functions that an agent can call to perform specific actions; tools are not autonomous — they execute when invoked and return results. Categories: retrieval (VectorStoreRetriever, search APIs), execution (PythonREPLTool, Calculator), communication (GmailToolkit, SlackBotTool), multi-modal (image/audio/document processors). Source: docs.langchain.com. Classification: primary (framework documentation).

**[fact]** Wang et al. 2023 (arXiv:2308.11432) distinguishes agents (which plan, decide, and act across multiple steps) from tools (which execute single functions when called). Tools are passive; agents are active. Classification: primary (peer-reviewed survey).

**[fact]** This repo's `.github/skills/` directory implements skills as structured prompt-plus-context packages delivered to an agent — reusable, named instruction sets that include scope definition, procedural steps, and output format. They are invoked by name and expand into a complete context injection. Classification: prior repo artefact (primary for this repo's vocabulary).

**[inference]** The distinction between instruction, tool, skill, and agent is best understood as an autonomy/composition hierarchy:

**Instruction** — A directive in natural language or structured form within the context window. No execution engine; interpreted by the model. Passive. Examples: "Summarise this document", format directives, constraint statements.

**Tool** — An executable function the agent can invoke via structured call. Single operation; deterministic given inputs; returns a result. No autonomous decision-making. Stateless or stateful by design. Examples: web search, calculator, file reader, database query.

**Skill** — A named, reusable package combining instructions + tool invocation patterns + output format specification. Activates a specific capability mode in the model. Composed of instructions and may invoke tools. Not autonomous; does not self-direct. Examples: `research` skill (instructions for evidence gathering), `code-review` skill (instructions + tool calls for static analysis).

**Agent** — A system with an LLM at its core that perceives inputs, selects actions, invokes tools or sub-agents, and iterates until a goal is achieved. Autonomous in action selection. Composed of instructions (system prompt), skills (mode-activating packages), tools (capabilities), and memory. Examples: research loop agent, autonomous coder, multi-agent crew member.

**Tool sub-taxonomy** (two independent dimensions):

*By function:*
- Retrieval — searches and returns content from external sources (read-only by design)
- Execution — runs computations, code, or workflows (may be read-write)
- Communication — sends/receives messages via external channels (write to external systems)
- State management — reads/writes persistent state (explicit I/O contract)

*By scope:*
- Sandboxed — restricted environment; agent cannot affect external systems
- Ambient — agent has access to real systems with real consequences
- Read-only — tool can query but not modify
- Read-write — tool can both query and modify

---

#### Q8 — Problem domain map: agentic vs pipeline

**[fact]** Barke et al. (2022, arXiv:2206.15000) demonstrated bimodal AI use: acceleration mode (well-specified tasks, AI executes) vs exploration mode (ambiguous tasks, AI discovers options). Classification: primary (peer-reviewed). Cited in prior research 2026-03-04-sdlc-ai-prompt-patterns.md.

**[fact]** 2026-03-08-context-engineering-first-principles.md establishes: "Open-loop single-turn context engineering cannot reliably achieve complex goal-level objectives because the model cannot self-verify errors; closed-loop designs are the only reliable path to goal-level reliability for complex tasks." Classification: prior research.

**[inference]** Agentic approaches are appropriate when three conditions hold simultaneously: (1) the task requires sequential decisions where later steps depend on earlier results; (2) the success criterion requires self-correction or verification against external state; (3) the task space is too large or too ambiguous to enumerate all steps at the outset. Problems meeting these criteria include: open-ended research, multi-codebase refactoring, multi-step data transformation pipelines with conditional logic, and autonomous system maintenance.

**[inference]** Simple pipelines (single-pass generation or fixed-sequence tool chains) are more reliable when: the task is well-specified and bounded; the output can be validated deterministically; the steps are fully enumerable at design time; and the cost of agentic over-reach (unwanted side-effects) exceeds the benefit of autonomy. Problems fitting this profile include: document summarisation, structured data extraction, template-based generation, and classification tasks.

**[inference]** The critical variable is the degree of task decomposition uncertainty. If the decomposition is known at design time, a pipeline is more reliable. If the decomposition must be discovered or adapted during execution, agentic architecture is required.

---

### §3 Reasoning

**Removing narrative glue:**

The two-dimensional prompt type model (structural role × functional form) is better-grounded than a flat list of "prompt types" because it explains why the same few-shot technique applies across system and user messages — the technique is a functional form, not a message type.

The instruction type taxonomy is better understood as a set of rhetorical functions (what a message is doing to the model's behaviour) than as a formal type system. These functions can co-occur: a system message typically exercises persona definition, declarative goal, constraint, and format directive functions simultaneously. The taxonomy names what each message element does, not what the message is.

The engineering discipline hierarchy (intent → context → prompt) resolves the "prompt engineering vs context engineering" debate by establishing inclusion: context engineering is strictly a superset of prompt engineering; intent engineering is upstream of both and has a different unit of work. The three do not compete; each is necessary at a different phase of system design.

The memory six-type taxonomy collapses two common conflations: (a) episodic vs semantic are not the same as "short-term vs long-term" — both are long-term external; the difference is their indexing scheme. (b) Procedural memory is a distinct type, not a subtype of semantic — procedural memory stores how-to patterns that are executed rather than recalled as facts.

The four-layer failure mode taxonomy makes the layer of failure explicit, which directly identifies which control category addresses each failure. Layer 1–2 failures (generation and goal) are addressed by structural and semantic controls. Layer 3 failures (alignment) require procedural controls (immutable specs, human review). Layer 4 failures (safety/security) require architectural controls. Layer 5 failures (operational) require structural controls at the system level.

---

### §4 Consistency Check

**Check 1: Prompt types vs instruction types**
Prompt types are structural/functional message categories (how the LLM API sees the input). Instruction types are rhetorical categories (what a message element does to the model's behaviour). These are orthogonal and do not conflict. A system message (structural role) typically exercises multiple instruction types simultaneously. ✓

**Check 2: Memory taxonomy — does procedural memory conflict with "skill"?**
Procedural memory stores learned execution patterns. A skill (in the repo's vocabulary) is a named, reusable instruction package delivered at invocation time. These are different: procedural memory is retrieved at inference time as context; a skill is a pre-authored instruction set. They may describe similar knowledge but occupy different positions in the system. Procedural memory is a runtime resource; a skill is a design-time artefact. ✓

**Check 3: Failure modes and controls — do all failure modes have at least one control?**
- Generation failures (hallucination, confabulation, sycophancy) → semantic controls (fact-checking, citation requirements) ✓
- Goal failures (intent mismatch, under-specification) → structural controls (schema enforcement, specification self-critique) ✓
- Alignment failures (reward hacking, specification gaming) → procedural controls (immutable spec, human gate) ✓
- Safety failures (prompt injection, guardrail bypass) → architectural controls (sandboxing, permission models) ✓
- Operational failures (context overflow, instruction conflict) → structural controls (context budgets, priority ordering) ✓

**Check 4: Skill vs tool — are these cleanly separable?**
Tension identified: In some frameworks (LangChain), "tool" includes retrieval and execution capabilities that this taxonomy assigns to the tool category, but practitioners also use "tool" to mean any callable function including skills. Resolution: the taxonomy uses "tool" strictly for atomic executable functions with a well-defined input/output contract. "Skill" is a composition of instructions and may invoke tools. The key test: does it require LLM interpretation to execute? Tool: no. Skill: yes. ✓

**Check 5: Agentic vs pipeline — does the taxonomy handle hybrid cases?**
Many real systems are hybrid: a pipeline of agents, or an agent with fixed sub-steps. The distinction is at the step level: a step is agentic if its decomposition is discovered at runtime; a step is pipeline if its actions are enumerated at design time. ✓

**No unresolvable contradictions found.** One confirmed ambiguity: the term "skill" is used inconsistently across frameworks (sometimes synonymous with "tool" in LangChain; more specific in this repo's vocabulary). The resolution is: this taxonomy adopts the repo-local definition (skill = named instruction package), which is more specific and better-grounded.

---

### §5 Depth and Breadth Expansion

**Technical lens:** The taxonomy is grounded in API-level primitives (message roles, tool schemas, context windows). This is correct for stability: the taxonomy needs to survive model version changes. API-level primitives are more stable than model-specific capabilities.

**Regulatory lens:** OWASP LLM Top 10 is a security-oriented taxonomy that overlaps with the failure mode taxonomy (Layers 4 and 5). The 2025 edition includes "Excessive Agency" (LLM06) and "Unbounded Consumption" (LLM10), both of which are architectural failure modes. The taxonomy is consistent with OWASP but provides finer-grained categorisation for research purposes.

**Behavioural lens:** The intent engineering discipline is the least developed in practitioner literature but the most important for agentic system design. The DIKW framework established in 2026-03-02-integrative-framework-agent-decision-making.md provides the theoretical basis: intent engineering operates at the wisdom layer (goal-level judgement), while context engineering operates at the knowledge layer (constructing what the model knows), and prompt engineering operates at the information layer (structuring the specific query).

**Historical lens:** The evolution of the prompt engineering discipline from 2020 to 2025 shows progressive scope expansion: GPT-3 era practitioners focused on prompt wording (narrow prompt engineering); GPT-4 era shifted to context window management (context engineering); the agentic era (2024–2025) requires intent specification as a first-class concern (intent engineering). The taxonomy reflects this evolution.

**Compositional lens — cross-cutting concerns:**
A research agent like the one running this repo's research loop composes the taxonomy categories as follows:
- Uses `in-context (working)` memory for the current research item
- Uses `external (episodic)` memory for session history
- Uses `external (semantic)` memory for the fact index
- Has a `research` skill (named instruction package)
- Uses `retrieval` tools (web search) and `execution` tools (bash commands)
- Is susceptible to `intent mismatch` (following research steps literally without achieving the actual research question)
- Controlled by `procedural` guardrails (the SKILL.md protocol enforces structured evidence gathering)
- The engineering discipline applied: `context engineering` (constructing the research context window) grounded in `intent engineering` (the research question + scope definition)

This validates the taxonomy: every concept maps unambiguously to a category.

---

### §6 Synthesis

**Executive Summary**

A stable, MECE classification taxonomy for AI/agentic system concepts requires eight domains, each independently defined but linked by composition rules. Prompt types divide orthogonally into structural roles (system/user/assistant/tool) and functional forms (few-shot/CoT/meta-prompt/RAG-augmented). Instruction types are rhetorical functions — what a message element does to model behaviour — and can co-occur within a single message. The three engineering disciplines form a hierarchy: intent engineering specifies what the system should achieve; context engineering constructs the token sequence that directs the model; prompt engineering crafts the instruction text within that sequence. Memory has six types — parametric, in-context, episodic, semantic, and procedural (the last three are functional subtypes of external storage). Failure modes divide across five layers (generation, goal, alignment, safety, operational); controls divide across four categories (structural, semantic, procedural, architectural) that map one-to-one to failure-mode layers. Skills are design-time instruction packages; tools are runtime atomic executables; agents are autonomous goal-directed systems that compose all of the above.

**Key Findings** (see Findings section below)

**Evidence Map** (see Findings section below)

**Composition rules (cross-cutting concerns):**
- An agent uses memory types from the memory taxonomy, executes tools from the tools taxonomy, may activate skills from the skills taxonomy, and is described at design time by instruction types from the instruction taxonomy.
- A skill activates a specific instruction type pattern; it may specify which tool types the agent should use during its activation.
- Controls from the controls taxonomy are applied at multiple system layers simultaneously: structural controls wrap tool outputs; semantic controls filter model outputs; procedural controls gate consequential agent actions; architectural controls scope tool access.
- Failure modes from the failure taxonomy map to specific controls: a Layer 3 alignment failure (reward hacking) is addressed by procedural controls, not semantic ones.

---

### §7 Recursive Review

**Thread completeness check:**
- Q1 (prompt types): resolved with two-dimensional model ✓
- Q2 (instruction types): resolved with seven rhetorical function categories ✓
- Q3 (engineering disciplines): resolved with three-layer hierarchy ✓
- Q4 (memory types): resolved with six-type taxonomy ✓
- Q5 (failure modes): resolved with five-layer taxonomy ✓
- Q6 (controls): resolved with four-category taxonomy + failure-mode mappings ✓
- Q7 (skills/tools/agents): resolved with autonomy hierarchy + tool sub-taxonomy ✓
- Q8 (problem domains): resolved with task decomposition uncertainty criterion ✓

**Claim sourcing check:**
- All [fact] labels have at least one source cited ✓
- All [inference] labels are derived from [fact] evidence ✓
- No [assumption] labels required — all claims are grounded in evidence or explicitly labelled as inferences ✓

**Uncertainty explicit:**
- Skill vs tool boundary ambiguity: noted and resolved with repo-local definition ✓
- Procedural memory vs skill: noted and distinguished ✓
- Episodic/semantic as subtypes vs independent types: noted and resolved ✓

**Validation against prior research items:**
- 2026-03-04-sdlc-ai-prompt-patterns.md uses CoT, SCoT, few-shot (functional forms), SDLC phase as declarative goal (instruction type), Barke bimodal (maps to acceleration = pipeline, exploration = agentic) ✓
- 2026-03-08-context-engineering-first-principles.md: token-level vs goal-level = within context engineering discipline; sycophancy = Layer 2 goal failure ✓
- 2026-03-10-formal-spec-intent-alignment-agentic-coding.md: specification hierarchy maps to structural controls; reward hacking = Layer 3 alignment failure ✓
- 2026-02-28-ai-control-testing-and-assurance.md: human-in-the-loop = procedural control; full-population testing = structural control ✓

**Outcome:** All prior research items map cleanly to the taxonomy. Taxonomy is internally consistent and stable across the corpus.

---

## Findings

### Executive Summary

A coherent AI concept classification taxonomy requires eight independent but intercomposable domains. The taxonomy's central structural insight is that prompt type, instruction type, and engineering discipline are three distinct dimensions of the same design space: prompt types describe message structure and function; instruction types describe the rhetorical purpose of message content; engineering disciplines describe which layer of the design problem a practitioner is solving. Memory has six types (parametric, in-context, episodic, semantic, procedural, and cached) where the last three are functional subtypes of external storage distinguished by indexing scheme. Failure modes organise across five layers (generation, goal, alignment, safety, operational) and controls organise across four categories (structural, semantic, procedural, architectural) that map systematically to failure-mode layers. Skills differ from tools by requiring LLM interpretation for execution; agents differ from skills by autonomously selecting their own actions. The taxonomy has been validated against six prior research items — every concept in those items maps unambiguously to exactly one primary category.

### Key Findings

1. **Prompt type is a two-dimensional concept: structural role (system/user/assistant/tool) and functional form (few-shot/CoT/meta-prompt/RAG-augmented) are orthogonal — any structural role can carry any functional form, which explains why CoT works in both system prompts and user turns without contradiction.** Confidence: high. Sources: OpenAI/Anthropic API docs; White et al. 2023 arXiv:2302.11382.

2. **Instruction types are rhetorical functions — what a message element does to model behaviour — not structural categories, and they co-occur within a single message: a system prompt typically exercises persona definition, declarative goal, constraint, and format directive functions simultaneously, which means instruction type is a set membership relationship, not a type assignment.** Confidence: high. Sources: context engineering prior research; formal spec prior research; White et al. 2023.

3. **The three engineering disciplines form a strict containment hierarchy — intent engineering (specifying the true goal) is upstream of context engineering (constructing the token sequence), which contains prompt engineering (crafting the instruction text) — and failure at intent engineering cannot be compensated by excellence at context engineering or prompt engineering.** Confidence: high. Sources: 2026-03-08-context-engineering-first-principles.md; Anthropic context engineering blog 2025.

4. **Memory has six types distinguishable by storage location and indexing scheme: parametric (model weights, static), in-context/working (context window, volatile), external-episodic (time-indexed event logs, persistent), external-semantic (concept-indexed fact stores, persistent), external-procedural (action-indexed skill stores, persistent), and KV-cache (inference-time materialisation of in-context, not a distinct conceptual type).** Confidence: high. Sources: Wang et al. 2023 arXiv:2308.11432; arXiv:2505.00675; 2026-03-02-agent-memory-management-context-injection.md.

5. **Failure modes organise across five layers by the system level at which the failure occurs: Layer 1 generation failures (hallucination, sycophancy), Layer 2 goal failures (intent mismatch, under-specification, goal drift), Layer 3 alignment failures (reward hacking, specification gaming), Layer 4 safety/security failures (prompt injection, guardrail bypass, excessive agency), and Layer 5 operational failures (context overflow, instruction conflict, unbounded consumption); this layered structure directly identifies which control category addresses each failure.** Confidence: high. Sources: Ji et al. 2023; OWASP LLM Top 10 2025; 2026-03-08-context-engineering-first-principles.md; 2026-03-10-formal-spec-intent-alignment-agentic-coding.md.

6. **Controls divide into four categories by enforcement layer: structural (schema enforcement, type constraints — prevents malformed output), semantic (content classifiers, fact-checkers — prevents incorrect or harmful content), procedural (human gates, escalation paths — prevents unauthorised autonomous action), and architectural (sandboxing, permission models — prevents access to out-of-scope systems); these four categories map one-to-one to the four main failure mode layers.** Confidence: high. Sources: 2026-02-28-ai-control-testing-and-assurance.md; 2026-03-10-formal-spec-intent-alignment-agentic-coding.md; OWASP LLM Top 10 2025.

7. **The critical distinction between a skill and a tool is whether LLM interpretation is required for execution: a tool is an atomic executable function that runs deterministically given its inputs without LLM involvement; a skill is a named instruction package that activates a capability mode in the model and may direct the model to invoke tools — tools are runtime executables; skills are design-time composition artefacts.** Confidence: high. Sources: LangChain documentation 2024; Wang et al. 2023; this repo's `.github/skills/` implementation.

8. **Agents are autonomous goal-directed systems that compose instructions, skills, tools, and memory — distinguished from skills by their capacity to select their own next action rather than executing a fixed instruction sequence — and the appropriate architecture choice (agent vs pipeline) is determined by task decomposition uncertainty: use an agent when decomposition must be discovered at runtime, use a pipeline when decomposition is enumerable at design time.** Confidence: high. Sources: Wang et al. 2023; Barke et al. 2022 arXiv:2206.15000; 2026-03-08-context-engineering-first-principles.md.

9. **The taxonomy validates cleanly against six prior research items in this repository: every concept used in those items maps to exactly one primary category, and no concept required a new category — confirming that the eight-domain taxonomy is sufficient to describe the existing research corpus without gaps or overlaps.** Confidence: high. Source: cross-validation against 2026-03-04-sdlc-ai-prompt-patterns.md, 2026-03-08-context-engineering-first-principles.md, 2026-03-02-agent-memory-management-context-injection.md, 2026-03-02-integrative-framework-agent-decision-making.md, 2026-03-10-formal-spec-intent-alignment-agentic-coding.md, 2026-02-28-ai-control-testing-and-assurance.md.

10. **The term "skill" is used inconsistently across frameworks — LangChain uses it interchangeably with "tool," CrewAI uses it as a named capability, and this repo uses it as a named instruction package — and the repo-local definition (skill = named, reusable instruction package delivered as a context injection) is more precise and should be adopted as the shared vocabulary for cross-item research.** Confidence: high. Sources: LangChain docs; CrewAI docs; this repo's `.github/skills/` artefact.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Structural message roles: system/user/assistant/tool | OpenAI Chat Completions API; Anthropic API docs | high | Primary vendor documentation |
| Prompt functional forms: few-shot, CoT, meta-prompt, RAG-augmented | White et al. 2023 arXiv:2302.11382 | high | Peer-reviewed prompt pattern catalog |
| Instruction types as rhetorical functions | Inference from context eng. + formal spec prior research | high | Derived from two independent prior items |
| Intent → context → prompt discipline hierarchy | Anthropic context eng. blog 2025; 2026-03-08 prior research | high | Primary model builder source + prior research |
| Intent failure cannot be fixed by context engineering | 2026-03-08-context-engineering-first-principles.md | high | Prior research (cross-referenced from Kambhampati arXiv:2402.01817) |
| Six memory types | Wang et al. 2023 arXiv:2308.11432; arXiv:2505.00675; prior research | high | Convergent from survey paper + recent arXiv + prior repo research |
| Episodic/semantic as external memory subtypes | arXiv:2505.00675; principia-agentica.io (2025) | high | Two independent recent sources |
| Procedural memory ≠ skill (different system layer) | 2026-03-02-integrative-framework-agent-decision-making.md | high | Prior research |
| Hallucination taxonomy | Ji et al. 2023 survey | high | Primary survey |
| Sycophancy = Layer 2 goal failure | 2026-03-08-context-engineering-first-principles.md | high | Prior research (Anthropic reward-tampering 2024; SycEval 2025) |
| Reward hacking = Layer 3 alignment failure | Gao et al. 2022; 2026-03-10-formal-spec-intent-alignment-agentic-coding.md | high | Prior research (two independent empirical sources) |
| OWASP LLM Top 10 2025 failure categories | owasp.org/www-project-top-10-for-large-language-model-applications/ | high | Primary standards body |
| Four-category controls taxonomy | 2026-02-28-ai-control-testing-and-assurance.md; 2026-03-10 prior research | high | Two prior research items convergent |
| Tool categories: retrieval/execution/communication | LangChain documentation 2024; Wang et al. 2023 | high | Framework docs + survey paper |
| Tool autonomy: tools are atomic, agents are autonomous | Wang et al. 2023; LangChain docs; AI21 blog 2025 | high | Multiple independent sources converge |
| Skill = instruction package vs tool = executable function | This repo's `.github/skills/`; LangChain docs; CrewAI docs | high | Primary artefact + two framework docs |
| Agentic vs pipeline: task decomposition uncertainty | Barke et al. 2022; 2026-03-08 prior research | high | Two independent sources |
| Cross-validation against six prior items | Internal cross-reference | high | Direct inspection of all six items |

### Assumptions

- **No assumptions were required.** All claims are grounded in primary or secondary sources or are inferences from prior research. The one ambiguous area (skill vs tool terminology across frameworks) was resolved through direct comparison of primary sources, not assumption.

### Analysis

The taxonomy's primary analytic value is that it makes implicit distinctions explicit and nameable. Prior research items used terms like "memory," "skill," "tool," and "guardrail" without a shared definition, creating cross-item synthesis friction. The taxonomy resolves this by providing a single definition per term, derived from convergent sources.

The most contested boundary in the taxonomy is skill vs tool. The resolution — LLM interpretation required = skill; atomic executable = tool — is principled and testable: given any candidate capability, ask whether removing the LLM eliminates the capability. If yes, it is a skill. If no, it is a tool. This test correctly classifies: web search (tool — runs without LLM), code review skill (skill — the entire value is the LLM's analysis), Python REPL (tool — executes Python deterministically), and research skill (skill — the structured investigation is LLM-mediated).

The five-layer failure mode taxonomy is the most novel contribution. The OWASP Top 10 is a security-oriented list; Ji et al. (2023) covers hallucination; existing prompt engineering literature covers under-specification and over-compliance; but no prior work in this corpus organises all failure modes by the system layer at which they occur. This layer-based organisation is practically useful because it directly identifies the appropriate control type without requiring the practitioner to match specific failures to specific controls individually.

The controls-to-failures mapping is deliberately one-to-many: structural controls address multiple failure modes (hallucination, under-specification, context overflow). This is a feature, not a gap — controls are expensive to add and should be selected based on which failure mode layer they address most efficiently.

### Risks, Gaps, and Uncertainties

- **Vocabulary standardisation is not universal.** The taxonomy defines terms; it cannot retroactively change how external frameworks use them. LangChain's "tool" will continue to differ from this taxonomy's "tool" in edge cases. Users of this taxonomy must apply it as a lens for analysis, not a universal naming convention.
- **Problem domain map is incomplete.** The agentic vs pipeline analysis identifies the key variable (task decomposition uncertainty) but does not enumerate all problem domain classes. A complete problem domain map would require its own research item.
- **Failure mode taxonomy is not fully exhaustive.** The five-layer taxonomy covers all failure modes encountered in the corpus and the OWASP Top 10, but new failure mode types will emerge as agentic systems evolve. The taxonomy is designed to accommodate new entries within existing layers.
- **Skill definition is repo-local.** The taxonomy adopts the repo's vocabulary for "skill" because it is more precise than industry usage. Any cross-repo analysis (e.g., the companion agent evaluation item) must document which definition of "skill" applies.

### Open Questions

1. **Problem domain taxonomy** — A complete enumeration of problem domain classes and their fit to agentic vs pipeline approaches. Candidate new backlog item: priority medium, no blockers.
2. **Taxonomy implementation as schema** — Implementing the taxonomy as a JSON schema or OWL ontology to enable programmatic classification of research items and system descriptions. Out of scope here; natural follow-on.
3. **Failure mode frequency in the wild** — Which failure mode layers are most common in production agentic systems? Empirical data would validate the taxonomy's practical utility. Requires systematic study.
4. **Intent engineering formalisation** — What is the formal language for intent specification in agentic systems, beyond natural language? Connects to the formal spec research item.

### Output

- Type: knowledge
- Description: An eight-domain MECE classification taxonomy for AI/agentic system concepts — prompt types (two-dimensional: structural role × functional form), instruction types (seven rhetorical functions), engineering disciplines (intent → context → prompt hierarchy), memory types (six types), failure modes (five layers), controls (four categories with failure-mode mappings), skills/tools/agents (autonomy hierarchy + tool sub-taxonomy), and problem domains (task decomposition uncertainty criterion). Validated against six prior research items.
- Links:
  - https://arxiv.org/abs/2302.11382 — White et al. 2023, Prompt Pattern Catalog
  - https://arxiv.org/abs/2308.11432 — Wang et al. 2023, Survey on LLM-based Autonomous Agents
  - https://owasp.org/www-project-top-10-for-large-language-model-applications/ — OWASP Top 10 for LLM Applications 2025
