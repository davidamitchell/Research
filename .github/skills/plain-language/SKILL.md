---
name: plain-language
version: "1.0"
description: Rewrites complex, technical, or dense text so that a non-expert reader
  can understand it without losing accuracy or completeness. Use when asked to simplify
  content, make text more accessible, or adapt specialist material for a general
  audience.
---

# Skill: Plain Language

## When Not to Use

- When the audience is already expert and technical precision is more important than accessibility — use technical-writer instead
- When the goal is to remove words for concision without changing register — plain language changes vocabulary and structure, not just length
- When legal, regulatory, or contractual language must be preserved verbatim — note the constraints and flag sections that cannot be simplified

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. Who is the target audience — what is their background, and what can they be assumed to know?
2. Are there terms that must be preserved (product names, legal terms, required technical vocabulary)?
3. Is the goal a complete rewrite, or an audit with targeted changes?

**Output style**:

- Produce the simplified version directly
- For audit mode: annotate each change with a one-line rationale (jargon replaced, sentence split, structure clarified)
- Do not sacrifice accuracy for simplicity — if a simplification loses meaning, flag it and offer an alternative
- Preserve all factual content; do not omit details to make simplification easier

---

## Inputs and Outputs

**Input**: Source text (any length or domain), target audience description, and optional list of terms to preserve  
**Output**: Simplified version retaining full meaning; or annotated audit identifying changes and their rationale  
**Composability**: Use after technical-writer (to adapt technical docs for broader audiences); use after research or strategy-author (to make expert output accessible); use alongside remove-ai-slop (to eliminate formulaic patterns after simplification)

---

## Purpose

Make complex content understandable to a reader who lacks specialist knowledge, without losing accuracy, completeness, or the author's intended meaning.

---

## 1. Audience Calibration

Before rewriting, establish the reader's profile:

- **Prior knowledge**: What domain concepts can be assumed? What must be explained?
- **Reading context**: Is this a one-time read, a reference document, or instructional material?
- **Action required**: Does the reader need to do something after reading, decide something, or simply understand?

Every simplification decision must serve this reader — not an imagined generic audience.

---

## 2. Plain Language Principles

Apply the following in sequence:

### 2.1 Vocabulary

- Replace specialist terms with common equivalents where no meaning is lost.
- When a specialist term must be kept, define it on first use in one plain sentence.
- Replace Latin, legal, or bureaucratic phrases with plain equivalents: "prior to" → "before"; "utilise" → "use"; "in the event that" → "if".
- Do not replace precise technical terms with vague alternatives — accuracy is not negotiable.

### 2.2 Sentence Structure

- Break sentences longer than 25 words into shorter ones where the logic allows it.
- Move the main clause to the front: "If the server is unavailable, the request fails" not "In cases where server availability cannot be confirmed, the request will fail to complete".
- Eliminate embedded clauses that interrupt the main point.
- Use active voice: "The system validates the token" not "The token is validated by the system".

### 2.3 Paragraph Structure

- One idea per paragraph.
- Lead with the most important sentence — readers who stop early should still get the core point.
- Remove transition filler ("Furthermore", "It is worth noting that") and go directly to the next point.

### 2.4 Document Structure

- Use headings to orient the reader to what each section contains.
- Use numbered lists for sequences; bullet lists for non-ordered items.
- Put the conclusion or key message before the supporting detail, not after.

---

## 3. Accuracy Safeguards

Simplification must not:

- Remove conditions, exceptions, or qualifications that affect how the content applies
- Convert approximate or uncertain statements into definite ones
- Conflate distinct concepts by using the same term for both
- Omit steps, requirements, or facts to reduce word count

When a section cannot be simplified without losing material accuracy:

- Keep the original text
- Annotate it: `[Preserved: simplification would lose accuracy — original term required]`
- Offer an explanatory gloss in plain language alongside it

---

## 4. Review Protocol

After rewriting, check each paragraph against:

1. **Readability**: Would the target audience understand this on first read without re-reading?
2. **Completeness**: Is everything from the source present, even if expressed differently?
3. **Accuracy**: Has any meaning shifted, narrowed, or expanded relative to the original?
4. **Consistency**: Are the same concepts referred to by the same plain-language term throughout?

---

## 5. Failure Modes

- Oversimplifying by removing necessary qualifications or conditions
- Replacing precise technical terms with vague everyday words that lose accuracy
- Producing shorter text that is no clearer because sentence structure was not addressed
- Defining jargon in more jargon
- Applying plain language mechanics (short sentences, active voice) without considering whether the result serves the reader's actual task
