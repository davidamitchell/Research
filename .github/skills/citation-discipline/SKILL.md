---
name: citation-discipline
version: "1.0"
description: Ensures all factual statements are bound to verifiable sources, cited
  precisely at the point of claim, and integrated without disrupting prose flow.
  Use when producing research, reports, or any writing where every assertion must
  be independently traceable.
---

# Substantiated Claims & Citation Discipline

## When Not to Use

- When the task is explicitly creative or fictional writing, where factual citation is inappropriate
- When rapid ideation or early-stage drafting is in progress and precise sourcing would slow the flow — apply this skill in a dedicated review pass instead
- When the content is an acknowledged personal opinion or editorial commentary with no factual claims

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What citation style is required (inline, footnote, endnote, or none specified)?
2. Are primary sources accessible, or must secondary sources be relied upon?
3. What is the intended audience's level of familiarity with the subject?

**Output style**:

- Citations placed per the operational rules below
- Flag any claim that cannot be sourced with `[SOURCE NEEDED]`
- Do not silently omit citations for hard-to-source claims — always surface them

---

## Inputs and Outputs

**Input**: Draft text with factual claims, plus any source materials provided  
**Output**: Revised text with inline citations; list of flagged unsourced claims  
**Composability**: Apply after research or strategy-author; use alongside speculation-control for epistemic rigour

---

## Purpose

Ensure all factual statements are supported by verifiable sources, cited
consistently, and integrated into prose without disrupting clarity or flow.

---

## Core Principles

1. No factual assertion is made without a verifiable source.
2. Every citation must correspond to a specific claim, not a general paragraph.
3. Citations must be sufficient for a reader to independently verify the claim.
4. Claims must be stated precisely — without exaggeration, inflation, or implication beyond what the source supports.
5. When multiple interpretations exist, specify which is being used and why.

---

## Operational Rules

### Claim–Source Binding

- Each factual claim must be paired with a source at the moment it is introduced.
- The source must directly support the claim as written.
- If the source is indirect, secondary, or interpretive, state this explicitly.

### Citation Placement

- Place citations at the end of the sentence containing the claim.
- If a sentence contains multiple claims, support each individually or split the sentence.

### Flow

- Integrate citations without interrupting argument structure.
- Use footnotes for source commentary, methodological notes, or alternative interpretations only.
- Use appendices for extended evidence, data, or derivations.

### Source Quality

- Prefer primary sources.
- Secondary sources are permitted only when primary sources are inaccessible, or when the secondary source provides necessary synthesis.
- Tertiary sources (summaries, encyclopedias) may be used for orientation only — not for claims.

### Precision

- Avoid vague quantifiers ("many", "most", "significant") unless the source uses them explicitly.
- Avoid causal language unless the source demonstrates causality.
- Avoid generalizing from single examples.

### Terminology and Acronyms

- On first use, expand every acronym and initialism: write the full term followed by the abbreviation in parentheses — e.g., "Large Language Model (LLM)". Use only the abbreviation thereafter.
- Link every non-self-evident domain term to its authoritative definition on first use — an official specification, standards body publication, or recognised authoritative glossary. Do not use summaries, encyclopedias, or tertiary sources for this purpose.
- If no authoritative definition source is available, flag the term with `[DEFINITION NEEDED]` rather than silently omitting the link.

### Verification

- Before finalizing, re-check each claim–source pair for accuracy, scope, and fidelity to the source.

### Epistemic Label Boundary

- A claim is `[fact]` only when: (a) it is directly supported by the cited source, **and** (b) the source is independently verifiable by the reader. If either condition fails, the label must be `[inference]` — regardless of how confident the source sounds or how indirect the wording is. A source that says "inferred from context" or "based on analysis" does not meet condition (a).

---

## Mandatory Pre-Output Checklist

Run these steps in order before outputting any document. Do not mark output as complete until all steps pass.

1. **Acronym scan**: Read the full document and list every initialism and acronym found. Verify each is expanded at first use in the format "Full Name (ACRONYM)". If any are not expanded, expand them before proceeding.
2. **Citation URL/DOI check**: For every citation in the document, verify it includes a URL or DOI sufficient for independent verification by the reader. A citation that lists only a name, title, or descriptive phrase without a URL or DOI must be either completed or replaced with `[SOURCE NEEDED]`.
3. **"Web search synthesis" prohibition**: Search the document for any citation that uses the phrase "web search synthesis" or equivalent. If found, it must be replaced with a specific, independently verifiable source or removed and replaced with `[SOURCE NEEDED]`.
4. **Primary-source requirement for external claims**: For every claim about an external system, product, or organisation, verify the citation is the primary external source (official documentation, canonical publication, or direct statement from the authoritative body) — not a secondary article, blog post, or internal document. If not, either locate the primary source or label the claim `[inference]` with the secondary source noted.
5. **Scope match check**: For every citation, verify that the scope of the cited source matches the scope of the claim. A source scoped to a specific product variant, edition, or environment (e.g. Enterprise Server, a particular API version, a regional deployment) must not be used to support a claim about a different scope (e.g. the cloud-hosted version, the general product, or a different region).
6. **Epistemic label audit**: For every claim labeled `[fact]`, apply the epistemic label boundary rule above. Downgrade to `[inference]` if either condition fails.

---

## Failure Modes

- Claims without citations
- Citations that do not support the claim as written
- Overgeneralizing from limited evidence
- Using citations as decoration rather than justification
- Introducing in footnotes facts that belong in the main text
- Using an acronym or initialism without expanding it on first use
- Using non-self-evident domain terms without linking to an authoritative definition
- Citing a scoped or secondary source for a claim about a different scope (e.g. Enterprise Server documentation cited for a claim about github.com behaviour, or a secondary article cited for a claim about an external product's native capability).
- Listing a citation by name or description only, without a URL or DOI sufficient for independent verification.
