---
name: research
version: "1.1"
description: Performs rigorous, evidence-driven research using recursive decomposition,
  iterative verification loops, and disciplined reasoning. Use when asked to research
  a topic, investigate a question, or gather and synthesize evidence into structured
  findings.
---

# Skill: Detailed Research Behaviour (with Loops & Recursion)

## When Not to Use

- When the task requires creative generation or ideation rather than evidence gathering
- When the question is entirely subjective (matters of preference, value, or opinion) and empirical investigation would be misleading
- When a rapid directional answer is needed and a full research loop is not warranted — in that case, use this skill for a constrained single-pass investigation, then note its limitations explicitly

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What is the research question or goal?
2. What constraints apply (time, scope, source types)?
3. What output format is needed (summary, full report, evidence map, Q&A)?
4. What constraint mode applies — **full**, **bounded**, or **rapid**? (See Constraint Parameter below.)

**Output style**:

- Follow the structured output in Section 6 (Synthesis)
- Label all inferences explicitly; do not embed assumptions in factual prose
- State confidence levels or uncertainty ranges where evidence is incomplete

---

## Inputs and Outputs

**Input**: Research question or topic, with optional scope constraints and source preferences  
**Output**: Structured findings containing executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions  
**Composability**: Use before strategy-author (to ground strategy in evidence); use alongside citation-discipline (to bind every claim to a source) and speculation-control (to label all non-factual content) for full epistemic rigour; both skills apply throughout the investigation and synthesis phases

---

## Constraint Parameter

Select the mode that matches the available time and required rigour.

| Mode | Definition | Evidence Sufficiency |
|---|---|---|
| **full** | Exhaustive investigation with complete decomposition, multi-lens expansion, and consistency check loops | At least two independent credible sources agree, **or** a primary source is definitive; all sub-questions resolved |
| **bounded** | Targeted investigation scoped to the highest-priority sub-questions; one consistency pass | At least two independent credible sources agree on each in-scope claim; out-of-scope claims flagged explicitly |
| **rapid** | Single-pass investigation of the top-level question only; no recursive decomposition | One credible source per claim is acceptable; all findings marked with confidence level; limitations stated upfront |

Default to **full** unless the user specifies otherwise or time constraints make it impractical.

---

## Source Prioritisation Heuristic

When selecting among available sources, apply in order:

1. **Primary sources** — original data, official publications, peer-reviewed research, direct statements from authoritative bodies
2. **Secondary sources** — synthesis, analysis, or reporting directly grounded in primary sources; cite the primary when accessible
3. **Tertiary sources** — encyclopedias, summaries, aggregators; use for orientation only, never as the sole basis for a claim

When primary sources conflict, report both and state which is adopted and why. Do not silently favour one.

---

## Confidence Calibration

Assign a confidence level to each key finding before synthesis.

| Level | Criteria |
|---|---|
| **High** | Multiple independent primary or credible secondary sources agree; no unresolved contradictions; claim is specific and bounded |
| **Medium** | One credible source, or multiple sources with minor conflicts; limited contradictions that are noted; inference is reasonable but not certain |
| **Low** | Single source of uncertain quality, significant gaps, strong inferential leap, or active expert disagreement; claim requires further investigation |

Label every key finding with its confidence level in the synthesis output. Do not aggregate findings into a single confidence rating — label each independently.

---

## Tool Awareness

If MCP tools (web search, file access, database connectors) are available, use them to extend the evidence base. Refer to the project's AGENTS.md § MCP Configuration for the list of configured tools and their scope. When no external tools are available, state this at the start of the output and note that findings are limited to training-data knowledge with a knowledge cutoff.

---

## Output Calibration

Adjust synthesis depth to the constraint mode in use:

- **full**: Complete structured output per Section 6 (all seven components); include full evidence map and open questions
- **bounded**: Abbreviated synthesis covering executive summary, key findings (in-scope only), assumptions, and flagged gaps; omit out-of-scope threads
- **rapid**: Single-section summary with confidence labels on each claim; explicit limitations paragraph; no evidence map required

In all modes: label inferences, state confidence levels, and surface unresolved questions. Do not silently reduce rigour — downgrade explicitly.

---

## 0. Initialise

- Restate the research question.
- Identify scope, constraints, definitions, and required outputs.
- Search completed research items for prior related work. If a completed item is directly relevant, cite it as prior art in the evidence map and note where its findings apply or conflict with the current investigation.

---

## 1. Recursive Problem Decomposition

The agent must recursively break the problem into atomic sub-questions.

### Algorithm

```
function RESEARCH(question):
  subquestions = DECOMPOSE(question)
  for each q in subquestions:
    if q is atomic:
      answer[q] = INVESTIGATE(q)
    else:
      answer[q] = RESEARCH(q)
  return SYNTHESISE(answer)
```

### Rules

- Continue decomposition until each sub-question can be answered with a single evidence-based claim.
- Maintain a decomposition tree for transparency.

---

## 2. Investigation Loop

For each atomic question, run an iterative evidence-gathering loop:

```
loop until evidence_sufficient or limits_reached:
  gather sources
  classify sources (primary, secondary, tertiary)
  evaluate credibility, incentives, and bias
  extract claims
  cross-verify claims across independent sources
  identify contradictions
  update evidence map
```

### Evidence sufficiency criteria

Apply the criteria for the active constraint mode (see Constraint Parameter table). In **full** mode:

- At least two independent credible sources agree, **or**
- A primary source is definitive.

### Source Marking

Every source in the evidence map must carry one of two marks:

- `[x]` — consulted: the source was accessed, read, and a specific claim was extracted from it
- `[ ]` — identified but not consulted: the source was found but not accessed

Never mark a source `[x]` unless it was actually read and its claim explicitly extracted. List all `[ ]` sources in a separate "Identified but not consulted" section in the evidence map. Do not cite an unconsulted source as evidence for any claim.

---

## 3. Reasoning Discipline

For every claim:

- Separate **facts**, **inferences**, and **assumptions**.
- Make assumptions explicit and justified.
- Quantify uncertainty using ranges or confidence levels.
- Avoid narrative glue, causal leaps, or unsupported generalisations.

---

## 4. Consistency Check Loop

After drafting findings, run a self-consistency cycle:

```
loop until no contradictions remain:
  scan for internal inconsistencies
  scan for unsupported leaps
  scan for ambiguous terms
  scan for unexpanded acronyms or initialisms on first use
  scan for non-self-evident terms lacking an authoritative definition link
  if contradiction found:
    trace back to source
    revise or flag uncertainty
```

If contradictions cannot be resolved, present competing interpretations.

---

## 5. Depth & Breadth Expansion Loop

Re-evaluate findings through multiple analytical lenses:

```
for lens in [technical, economic, regulatory, historical, behavioural]:
  re-evaluate findings through lens
  add new insights or constraints
```

---

## 6. Synthesis

Produce a structured output containing:

- Executive summary
- Key findings
- Evidence map
- Assumptions
- Analysis
- Risks, gaps, uncertainties
- Open questions

### Output Quality

Every section in the synthesis output must contain substantive content. Apply these constraints without exception:

- No placeholder headings with empty or deferred content
- No "not applicable" entries unless the absence is itself a finding requiring explanation
- The executive summary must state the core finding — not describe the structure of the report
- Every key finding must include its confidence level label (High / Medium / Low) per the Confidence Calibration table
- Risks and open questions must be specific and bounded; generic uncertainty statements are not acceptable

---

## 7. Recursive Review

Perform a final recursive pass:

```
function REVIEW(section):
  if section is atomic:
    validate clarity, evidence, and logic
  else:
    for each subsection:
      REVIEW(subsection)
```

Stop only when:

- Every section is justified
- All threads have been synthesised
- The structure is clear and integrated
- Every claim is sourced, or if inferred, labelled as inference
- All uncertainties are explicit
- No unlabelled assumptions
- Every acronym and initialism is expanded on first use
- Every non-self-evident domain term is linked to an authoritative definition

## 8. Output Finalisation

Before marking output complete, run all three companion skill pre-output checks in order. Do not output until all three pass.

### 8.1 Citation-discipline pre-output checklist

Apply the full pre-output checklist from `citation-discipline/SKILL.md`:

- **Acronym scan** — every acronym and initialism expanded on first use
- **Citation check** — every factual claim has a URL or DOI; no bare assertions
- **Web-search-synthesis prohibition** — no claim attributed to "multiple sources" without naming each source explicitly
- **Primary-source requirement** — secondary sources traced to their primary source where accessible
- **Scope-match check** — no source cited for a claim outside its stated scope
- **Epistemic label audit** — every inference labelled as inference; every assumption labelled as assumption

### 8.2 Speculation-control pre-output scan

Apply the full pre-output scan from `speculation-control/SKILL.md`:

- **Evaluative/comparative terms scan** — terms such as "better", "worse", "significant", "major", "leading", "important" must be anchored to a stated criterion or removed
- **Causal claims scan** — every "X causes Y" or "X leads to Y" statement must cite a source or be explicitly labelled as inference

### 8.3 Remove-ai-slop pre-commit scan

Apply the mandatory pre-commit scan from `remove-ai-slop/SKILL.md`. All five checks must pass:

1. **Enumeration-and-convergence** — no sentence matching "N independent [sources/fields] — X, Y, Z — converge on..." (or close variants); rewrite to state the point directly
2. **Symmetrical contrast** — no "Higher X requires... Lower X requires... The design sits at..." scaffolding; state the design choice directly
3. **Near-verbatim repetition** — no claim restated in substance across multiple sections with only surface word substitution
4. **Over-explained causality** — no narration of the obvious ("directly supporting the claim", "which demonstrates the point"); let evidence speak
5. **Repeated sentence-opening pattern** — no three or more consecutive paragraphs opening with the same syntactic structure
