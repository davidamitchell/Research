---
name: feedback
version: "1.0"
description: Delivers structured, constructive critique of written work, arguments,
  decisions, or plans. Findings are specific, evidence-grounded, and paired with
  actionable recommendations. Use when asked to review, critique, assess, or improve
  any piece of work where quality feedback is the goal.
---

# Skill: Feedback

## When Not to Use

- When the task is to rewrite or produce new content rather than evaluate existing content — produce the new version first, then apply this skill
- When the work is a final legal, compliance, or regulated deliverable requiring professional review — structured feedback is appropriate, but this skill cannot substitute for specialist sign-off
- When unsolicited critique would be inappropriate given the context (e.g., personal creative work shared for enjoyment, not evaluation)

---

## Interaction Protocol

**Before starting**, ask if not already clear:

1. What is the purpose of the work — what is it trying to achieve, and for what audience?
2. Are there specific concerns to prioritise, or should the review be comprehensive?
3. What level of critique is appropriate — high-level structural, line-level, or both?

**Output style**:

- Group findings by category (Structure, Argument/Logic, Clarity, Accuracy, Completeness, Style)
- Assign each finding a priority: `Critical`, `Major`, `Minor`, or `Suggestion`
- For every finding: state the specific problem, identify its location or instance, explain the consequence, and give a concrete recommended change
- End with a summary: total findings by priority, the work's key strengths, and the single highest-leverage improvement
- Do not produce generic encouragement — observations that do not identify a specific problem or produce an actionable recommendation are not findings

---

## Inputs and Outputs

**Input**: The work to be reviewed (text, argument, plan, decision, or document), with optional context: stated purpose, audience, and specific concerns  
**Output**: Structured findings grouped by category, each with priority, location, problem, consequence, and recommendation; overall summary with key strengths  
**Composability**: Use after strategy-author, research, or technical-writer (to evaluate their output); use alongside citation-discipline (to assess sourcing quality); use before remove-ai-slop (to identify structural issues before prose cleaning)

---

## Purpose

Produce specific, evidence-grounded feedback that enables the author to improve their work in concrete ways. Every finding must be tied to an observable problem in the work — not preference, taste, or convention for its own sake.

---

## 1. Review Categories

Apply all relevant categories. Skip a category only if it is entirely inapplicable to the work type.

### 1.1 Structure

- Does the work have a clear beginning, middle, and end appropriate to its type and purpose?
- Is the order of information logical — does earlier content provide what later content requires?
- Are sections proportionate to their importance?
- Is anything present that serves no structural function?

### 1.2 Argument and Logic

- Is the central claim or thesis clear and explicitly stated?
- Do the supporting points actually support the central claim?
- Are there gaps in the reasoning where steps are skipped or assumed?
- Are there contradictions between different parts of the work?
- Are conclusions supported by the evidence presented, or do they exceed it?

### 1.3 Clarity

- Would a reader in the stated audience understand this without additional context?
- Are key terms defined where necessary?
- Are ambiguous pronouns, vague references, or unclear antecedents present?
- Are sentences or paragraphs doing too much — trying to communicate multiple distinct ideas at once?

### 1.4 Accuracy

- Are factual claims correct and appropriately supported?
- Are there statements that overstate or misrepresent the evidence?
- Are assumptions stated explicitly, or are they embedded without acknowledgment?

### 1.5 Completeness

- Does the work address what it sets out to address?
- Are there obvious objections, alternatives, or failure modes not acknowledged?
- Are necessary prerequisites, context, or definitions missing?

### 1.6 Style and Tone

- Is the tone appropriate for the audience and purpose?
- Is the language register consistent throughout?
- Are there patterns that reduce impact: hedging, filler phrases, passive constructions where active would be stronger?

---

## 2. Priority Classification

Assign each finding one of the following:

| Priority | Criteria |
|---|---|
| `Critical` | The work fails its purpose or misleads the reader if this is not addressed |
| `Major` | The work is substantially weakened, confusing, or incomplete without this fix |
| `Minor` | The work would be meaningfully improved, but functions without the change |
| `Suggestion` | An optional improvement that may or may not fit the author's intent |

---

## 3. Finding Format

Each finding must contain:

```
**[PRIORITY] Category — Short title**

Location: <section, paragraph, sentence, or specific quote>
Problem: What is wrong and why it is wrong.
Consequence: What fails or degrades for the reader if this is not addressed.
Recommendation: Specific change to make.
```

---

## 4. Summary Format

End every review with:

```
## Summary

Findings: X Critical, X Major, X Minor, X Suggestions

**Strengths**: [Two or three specific things the work does well — must be observable, not generic praise]

**Highest-leverage improvement**: [The single change that would most improve the work's effectiveness]
```

---

## 5. Consistency Check

Before finalising, verify:

- Every finding has a specific location — no vague "the argument is weak" statements
- Every recommendation is concrete — no "consider improving" without specifying how
- Priority levels are consistent — the same class of problem is not rated `Critical` in one section and `Minor` in another
- Strengths identified are genuine and specific, not formulaic reassurance
- Summary counts match the body

---

## 6. Failure Modes

- Generating generic encouragement that dilutes the signal of genuine findings
- Flagging stylistic preferences as structural failures
- Assigning `Critical` priority without demonstrating a concrete failure for the reader
- Producing findings without a recommended fix
- Omitting the `Strengths` section — honest feedback includes what is working
- Letting the summary contradict the findings (e.g., calling work "strong" when Critical findings exist)
