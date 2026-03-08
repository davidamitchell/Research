---
name: remove-ai-slop
version: "1.0"
description: Removes generic, formulaic patterns from AI-generated text to produce
  more natural, authentic prose. Targets structural uniformity, predictable transitions,
  alignment artifacts, and lexical monotony. Use when AI-drafted content feels
  flat, over-structured, or stilted and needs to read more like thoughtful human
  writing.
---

# Skill: Remove AI Slop

## Purpose

Identify and remove the generic, formulaic patterns that make AI-generated text feel
impersonal, over-structured, or low-quality. The goal is authentic, high-quality prose —
not the removal of all AI involvement, but the elimination of the specific habits that
make AI writing feel like a template output.

This skill operates post-generation and focuses on **structural variety**,
**lexical authenticity**, and **voice coherence**.  
Stylistic voice shaping is handled by a separate skill.

---

## When Not to Use

- When the text must meet a formal template or structured format (e.g., legal filings, standardised reports) — structural uniformity may be required
- When the text is already high-quality and natural — unnecessary passes introduce risk of degradation
- When the goal is to misrepresent AI-generated work as human-written in contexts where disclosure is required (academic submissions, regulated content, etc.) — this skill is for quality improvement, not deception

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What is the intended audience and register?
2. Are there structural constraints that must be preserved (e.g., headers, lists)?
3. Is the priority naturalness, concision, or both?

**Output**: Return the revised text with a brief note identifying the main pattern categories addressed. Do not produce a word-by-word annotation unless asked.

---

## Inputs and Outputs

**Input**: AI-generated or AI-assisted text (any length)  
**Output**: Revised text with generic AI patterns removed; brief summary of changes made  
**Composability**: Apply after drafting; apply before style shaping or final editorial review

---

## 0. Quality Indicators

AI-generated text commonly exhibits these patterns that reduce authenticity:

1. **Predictable token sequences**
   - Low entropy phrase patterns
   - Formulaic transitions repeated at scale
2. **Over-structured layout**
   - Symmetrical paragraphs of equal length
   - Compulsive use of headers and bullets where prose would serve better
3. **Alignment artifacts**
   - Over-clarity that removes productive ambiguity
   - Unnecessary framing and meta-commentary
   - Safe, hedged phrasing that dilutes voice
4. **Stylometric uniformity**
   - Consistent sentence length
   - Predictable transition markers
   - Hedging density higher than natural writing
5. **Register flatness**
   - No micro-disruptions or human noise
   - Polished coherence with no personality

Goal: Introduce natural variation and eliminate formulaic habits without degrading meaning.

---

# 1. Signal Decomposition

## 1.1 Core AI Slop Features

Break text into atomic detectable features:

- Repetitive clause structure
- Predictable paragraph architecture
- Excessive explicit transitions
- Overly balanced sentence length
- Uniform syntactic rhythm
- Hedging density
- Safety disclaimers
- Explicit meta-structure ("In conclusion", "This means that")
- High semantic density without human noise
- Polished coherence with no micro-disruptions

---

# 2. Recursive Slop Removal Algorithm

function ELIMINATE_SLOP(text):

features = IDENTIFY_FEATURES(text)

for each feature in features:
    text = DISRUPT(feature, text)

if FEATURES_REMAIN(text):
    return ELIMINATE_SLOP(text)
else:
    return text

Stop only when quality-degrading patterns are eliminated.

---

# 3. Disruption Strategies

## 3.1 Entropy Injection

Increase local unpredictability without degrading clarity.

Methods:
- Replace common token pairs with less frequent equivalents
- Insert occasional human-like compression
- Introduce subtle asymmetry in phrasing
- Break predictable transition chains

Constraint:
Do not introduce semantic drift.

---

## 3.2 Structural Irregularization

AI outputs often exhibit:

- Symmetrical paragraphs
- Even sentence lengths
- Topic sentence → explanation → summary pattern

Countermeasures:

- Vary paragraph density
- Remove explicit summarization lines
- Occasionally omit logical signposting
- Mix fragment + long-form sentences

---

## 3.3 Alignment Artifact Removal

Remove:

- Safety-prefacing language
- Artificial neutrality padding
- Over-explained causal links
- Redundant context framing

Rewrite to:

- Assume reader competence
- Compress obvious reasoning
- Remove explicit justification loops

---

## 3.4 Stylometric Noise Injection

Humans exhibit:

- Minor asymmetries
- Micro-ambiguities
- Occasional compression
- Implicit references

Techniques:

- Replace over-formal constructions
- Introduce mild syntactic variance
- Avoid rhetorical symmetry
- Remove checklist-like formatting unless required

---

## 3.5 Transition Suppression

Common AI markers:

- Furthermore
- Additionally
- In conclusion
- It is important to note
- This highlights that

Remove or collapse into implicit flow.

---

# 4. Quality Improvement by Pattern Category

## 4.1 Lexical Monotony

Improve:
- Increase lexical diversity
- Replace high-frequency phrase templates with more precise alternatives
- Avoid structural repetition across paragraphs
- Vary sentence openings

---

## 4.2 Tone and Register Flatness

Improve:
- Break overly neutral, impersonal tone where voice is appropriate
- Reduce politeness scaffolding ("I hope this helps", "Happy to elaborate")
- Remove instructional cadence where it is not needed
- Vary explanation depth to match argument weight

---

## 4.3 Over-Polished Flow

Improve:
- Vary sentence construction to reflect natural thought
- Remove overly optimized, frictionless transitions
- Reintroduce productive specificity in places where over-smoothing removed it

---

# 5. Multi-Pass Refinement Loop

loop until quality_threshold met:

run structural audit
run lexical diversity audit
run alignment artifact audit
run repetition scan

revise

Threshold defined by:

- Structural variety achieved
- No repeated syntactic openings
- No visible rhetorical scaffolding
- No checklist-like cadence where prose is more appropriate

---

# 6. Tooling Layer

Optional automation stack:

1. N-gram frequency scanner
2. Sentence length variance analyzer
3. Transition phrase blacklist filter
4. Hedging density counter
5. Perplexity estimator (local LLM proxy)
6. Classifier probe (if available)

Pipeline:

Generate → Audit → Disrupt → Audit → Final Review

---

# 7. Human Noise Calibration

After revision:

- Ensure coherence preserved
- Ensure no artificial awkwardness
- Ensure semantic integrity

Quality requires:
Natural variance without visible manipulation.

---

# 8. Consistency Check

function CONSISTENCY_CHECK(text):

assert no logical contradictions
assert no semantic drift
assert tone stable
assert argument intact

If failed:
Trace modification step and correct.

---

# 9. Stopping Conditions

Stop when:

- No formulaic transitions remain
- Sentence length varies naturally
- Paragraph structures vary
- No alignment padding present
- Text does not read like a structured exposition template

---

## Mandatory Pre-Commit Scan

Run these checks in order before finalising any document. Do not mark output complete until all five pass.

1. **Enumeration-and-convergence**: Search for any sentence matching the pattern "N independent [sources/literatures/fields] — X, Y, and Z — converge on..." (or close variants). If found, rewrite to state the point directly or delete the framing.
2. **Symmetrical contrast**: Search for any sequence of sentences forming a "Higher X requires... Lower X requires... The design sits at..." pattern or equivalent symmetrical bracketing. If found, rewrite to state the design choice directly without the scaffold.
3. **Near-verbatim repetition**: For each section, check whether any sentence appears in substance in more than one section (with only word substitution). If found, retain the instance where it has the most analytical weight and remove or compress the repeat.
4. **Over-explained causality**: Search for any phrase of the form "directly supporting the [claim]", "which demonstrates [already-evident point]", or "thereby confirming [conclusion]". If found, delete the narration — let the evidence speak.
5. **Repeated sentence-opening pattern**: Check whether three or more consecutive paragraphs open with the same syntactic structure (e.g. all beginning with "This", all beginning with a gerund, all beginning with "The [noun]"). If found, vary the structure of at least two openings.

---

# 10. Failure Modes

- Over-randomization
- Meaning drift
- Artificial awkwardness
- Stylistic degradation
- Loss of clarity
- Enumeration-and-convergence framing: "N independent [sources/literatures/fields] — X, Y, and Z — converge on..." used to open or close a section.
- Symmetrical contrast scaffold: "Higher X requires... Lower X requires... The design sits at..." or equivalent symmetrical framing used in place of a direct statement.
- Near-verbatim repetition between sections: the same claim restated in substance across multiple sections with only surface word substitution.
- Over-explained causality: narration of the obvious ("directly supporting the claim", "which demonstrates the point") appended to evidence that already speaks for itself.
- Repeated sentence-opening pattern: three or more consecutive paragraphs opening with the same syntactic structure.

If detected:
Rollback last disruption layer.

---

# 11. Integration

Works in sequence with:

1. Research skill (for factual grounding)
2. Style authenticity skill (for human voice)
3. This skill (for quality improvement)

Order of execution:

Research → Draft → Slop Removal → Style Layer → Final Audit

---

End of File