---
name: research-reviewer
version: "1.0"
description: Audits a completed research item for citation discipline, speculation control, and writing quality. Use after research investigation is complete and before the item is marked done. Audit-only — never edits the item.
---

# Skill: Research Item Review

## When Not to Use

- When the research item is still in progress — complete the investigation first
- When a quick sanity check is needed rather than a full audit — use `citation-discipline`, `speculation-control`, or `remove-ai-slop` individually
- When the goal is to improve the writing — this skill audits; it does not rewrite

---

## Interaction Protocol

**Operating mode**: Audit-only. Read the item. Report violations. Do not edit, rewrite, or commit anything.

**Before starting**, confirm:
1. Is the item complete? (Findings, Evidence Map, and Executive Summary are populated — not stubs or "TBD")
2. Which sections require full audit? (Research Skill Output and Findings sections require full checks; Context section has lighter standards — see scope notes below)

**Output**: A structured violation report. See Output Format.

---

## Inputs and Outputs

**Input**: A completed research item in structured Markdown format with Research Skill Output and Findings sections  
**Output**: A structured audit report with per-skill PASS/FAIL verdicts and specific violations  
**Composability**: Use after `research` §8 Output Finalisation; referenced in `research` skill as the final gate before marking an item complete. Applies `citation-discipline`, `speculation-control`, and `remove-ai-slop` in sequence.

---

## Scope Notes

Apply these standards consistently across all items:

**Research Skill Output and Findings sections**: Full audit. All three skills apply at maximum rigour.

**Context section**: Lighter standard.
- `citation-discipline`: flag only hard factual claims (specific statistics, named studies, precise dates) that lack a source. Do not flag framing prose, motivating rationale, or working hypotheses.
- `speculation-control`: flag overconfident assertions presented as settled fact. Allow unlabelled framing assumptions and working hypotheses — the Context section is intentionally a pre-investigation framing device.
- `remove-ai-slop`: apply normally.

**Template structure**: Do not flag required structural elements (section headers, numbered sections, Evidence Map table) as AI slop. These are required by the format.

---

## Step 1 — Citation Discipline

Check the Research Skill Output and Findings sections for:

- Factual claims that lack a `[fact]`, `[inference]`, or `[assumption]` label and a corresponding source
- Sourced claims where the citation does not directly support what is asserted
- Vague quantifiers ("many", "most", "significant") used without sourcing
- Acronyms or initialisms used without expansion on first occurrence
- Domain terms used without a link to an authoritative definition

Do not flag stubs or "TBD" sections — an incomplete section is not a citation violation.

The labels `[inference]` and `[assumption]` are the accepted convention for epistemic labelling in research items — treat them as compliant with citation discipline for the purpose of distinguishing verified facts from inferences.

---

## Step 2 — Speculation Control

Check the Research Skill Output and Findings sections for:

- Speculative statements that are not prefixed with `Speculation:` or `Hypothesis:`, or not labelled `[inference]` or `[assumption]`
- Opinions or subjective judgments that are not labelled `Opinion:`
- Overconfident language ("clearly", "obviously", "undeniably") unsupported by evidence
- Evidentiary gaps filled with invented or assumed detail presented as fact

The labels `[inference]` and `[assumption]` in Research Skill Output sections are the accepted convention — treat them as compliant.

---

## Step 3 — Remove AI Slop

Check the Findings section (Executive Summary, Key Findings, Analysis, etc.) for:

- Formulaic AI writing patterns: predictable transitions ("Furthermore", "Additionally", "It is important to note"), symmetrical paragraphs, explicit meta-structure ("In conclusion")
- Alignment artifacts: safety-prefacing language, over-explained causal links, unnecessary framing sentences
- Lexical monotony: repeated sentence openings, uniform sentence length, excessive hedging density

Apply `remove-ai-slop/SKILL.md` checks in full.

---

## Output Format

Produce the report in this exact format:

```
REVIEW_TARGET: <item identifier or title>
citation-discipline: PASS | FAIL
  VIOLATION: <specific violation with section reference or quote>
speculation-control: PASS | FAIL
  VIOLATION: <specific violation with section reference or quote>
remove-ai-slop: PASS | FAIL
  VIOLATION: <specific violation with section reference or quote>
OVERALL: PASS | FAIL
```

Rules:
- Use `PASS` if no violations are found for a skill; use `FAIL` if any violations are found
- Each violation on its own line, indented two spaces, prefixed `VIOLATION: `
- `OVERALL: PASS` only if all three skills passed; otherwise `OVERALL: FAIL`
- If a required companion skill file is missing, write `SKILL_FILE_MISSING` as the result and treat it as `PASS` for the overall calculation
- If the item is a stub (Findings not yet populated), write `ITEM_INCOMPLETE` and do not audit
