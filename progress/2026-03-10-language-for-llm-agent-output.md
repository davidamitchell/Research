# Session: Language designed for LLM agents to produce — new backlog item

**Date:** 2026-03-10
**Slug:** language-for-llm-agent-output

## What was done

Added a new research backlog item in response to the issue asking whether anyone is developing a language specifically for LLM agents to produce that addresses failure modes described in two completed research items.

### Item created

**`Research/backlog/2026-03-10-language-for-llm-agent-output.md`**
- Priority: high
- Tags: agentic-systems, programming-languages, dsl, failure-modes, intent-alignment, reward-hacking, formal-methods, output-language, llm-code-generation, structured-output
- Research question: Is anyone actively developing a language or structured output format specifically designed for LLM agents to generate — not humans to write — that structurally addresses generation-layer and goal-layer failure modes?

### Motivating context from completed items

**From `2026-03-10-formal-spec-intent-alignment-agentic-coding.md`:**
- The specification hierarchy shows natural language (level 1) has zero verifiability; moving up the hierarchy mechanically closes failure gaps
- Type-constrained decoding (ETH Zurich PLDI 2025) constrains LLM generation to an existing language — but not a purpose-built agent-output language
- Open question left by that item: does spec-level 5 generation (Dafny-style) produce more aligned agent output than natural language?

**From `2026-03-10-ai-concept-classification-taxonomy.md`:**
- The five-layer failure mode taxonomy identifies structural controls (schema/type enforcement) as the category addressing generation-layer and goal-layer failures
- Explicit open question in that item: "What is the formal language for intent specification in agentic systems, beyond natural language? Connects to the formal spec research item."

The new backlog item directly addresses that open question and the gap it points to.

### Scope decisions

- **In scope:** Purpose-built languages/DSLs for LLM agent output; structured output grammars; type-constrained generation libraries (Guidance, Outlines, LMQL, SGLang); mapping to failure mode taxonomy and specification hierarchy
- **Out of scope:** Languages designed for humans (TypeScript, Rust, Python) already covered in the formal spec item; prompt engineering; post-hoc validators; fine-tuning approaches

## Notes

The item is positioned as a direct follow-on from both completed items. It bridges the "structural controls" category from the taxonomy item and the "level 3–4 specification hierarchy" from the formal spec item. The synthesis goal is to identify which failure mode layers current purpose-built approaches cover and what gaps remain.
