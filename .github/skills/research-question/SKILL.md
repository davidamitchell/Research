---
name: research-question
version: "1.0"
description: Validates and scopes a research question before investigation begins. Use when formulating a new research item, reviewing a drafted question for quality, or checking whether a question is ready to hand to the research skill.
---

# Skill: Research Question Formulation

## When Not to Use

- When a research question already exists and has been validated — proceed directly to the `research` skill
- When the task is to investigate rather than to scope (this skill prepares the question; `research` executes it)
- When the question is a creative brief, design prompt, or opinion request — those are not research questions

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What decision or problem does the answer need to inform?
2. Are there known constraints (time, source types, access, domain)?
3. What output type is expected (knowledge, decision, recommendation, artefact)?

**Output style**: Return a validated research question with scope, constraints, approach, and a readiness verdict. Flag every gap that would prevent investigation from starting.

---

## Inputs and Outputs

**Input**: A candidate research question or topic statement, with optional context  
**Output**: A validated research question with scope boundaries, constraints, decomposed approach sub-questions, and a readiness verdict (ready / needs revision)  
**Composability**: Use before `research` (gates the start of investigation); the output feeds directly into `research` §0 Initialise

---

## 1. Question Quality Test

A research question is ready when it passes all five tests:

| Test | Pass condition | Fail signal |
|---|---|---|
| **Specific** | Names the subject, the comparison or evaluation, and the context | "Investigate X", "What about Y", vague topic statements |
| **Answerable** | Can be resolved with evidence available in principle | Requires future events, unobtainable data, or pure opinion |
| **Scoped** | Has explicit in-scope and out-of-scope boundaries | No scope defined; would expand infinitely |
| **Motivated** | States what decision or problem the answer informs | No stated purpose; investigating for its own sake |
| **Decomposable** | Can be broken into at least two atomic sub-questions | Monolithic; cannot be subdivided |

If any test fails, the question needs revision before investigation begins.

---

## 2. Question Rewriting

If the question fails the Specific test, rewrite it using this pattern:

> "What is the [best / most appropriate / correct] [X] for [purpose] given [constraints]?"

Examples:
- Weak: "Investigate memory management for agents"
- Strong: "What is the most operationally practical memory architecture for a single-owner research agent running in GitHub Actions, given a constraint of no persistent server and a corpus under 500 items?"

If the question fails the Scoped test, add explicit boundaries:
- **In scope**: list the specific aspects, technologies, or contexts that are in scope
- **Out of scope**: list the aspects explicitly excluded and why
- **Constraints**: time horizon, source types, access limitations, budget

---

## 3. Approach Decomposition

Decompose the validated question into sub-questions before investigation begins.

Rules:
- Each sub-question must be answerable with a single evidence-based claim
- Sub-questions must be independent where possible (parallel, not sequential)
- Number each sub-question; use letter suffixes for nested decomposition (1a, 1b)
- If a sub-question cannot be answered without first answering another, make the dependency explicit

Stopping condition: decomposition is complete when every leaf sub-question passes the Specific and Answerable tests independently.

---

## 4. Readiness Verdict

After applying tests, rewriting, and decomposing, issue one of two verdicts:

**READY**: The question is specific, answerable, scoped, motivated, and decomposed. Hand to the `research` skill.

**NEEDS REVISION**: List each failing test with a concrete fix instruction. Do not proceed to investigation until all tests pass.

---

## 5. Output Format

```
Research Question: [final validated question]

Scope:
  In scope: [list]
  Out of scope: [list]
  Constraints: [list]

Context: [one sentence: what decision or problem this informs]

Approach:
  1. [sub-question]
     1a. [atomic]
     1b. [atomic]
  2. [sub-question]

Readiness: READY | NEEDS REVISION
[If NEEDS REVISION: list each failing test and fix instruction]
```
