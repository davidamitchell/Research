# Process Evaluation Report — question-decomposition

**Process:** §1 Question Decomposition — recursively break Approach sub-questions into atomic questions, each answerable with a single evidence-based claim.
**Sampled:** 3 of 3 requested
**Seed:** 42
**Generated:** 2026-05-05T10:37:48.056750+00:00
**Scored:** yes

## Summary Scores

| Metric | Mean |
| --- | --- |
| Structural completeness | 0.667 |
| Coverage overlap (Jaccard) | 0.065 |

## Items

### 1. 2026-03-07-run-build-it-allocation-implementation-how

**Title:** How organisations practically implement IT RUN vs BUILD cost allocation

**Research Question:**

How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: how did they agree on what counts as an "application", how did they get consistent work-item tagging across teams, how did they establish a shared team taxonomy, who drove the change, and how did they make the business case for the investment required?

**Process Prompt:**

```
You are conducting research. Your task is to complete §1 Question Decomposition
for the following research question.

Research Question:
How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: how did they agree on what counts as an "application", how did they get consistent work-item tagging across teams, how did they establish a shared team taxonomy, who drove the change, and how did they make the business case for the investment required?

Approach sub-questions from the item:
1. **Application definition governance:** How do organisations draw the boundary around an "application"? What criteria are used (business capability, deployment unit, support contract, cost centre)? Who owns the definition, and what is the process for resolving disputes? How is the application register kept current as systems evolve?
2. **Team and contract alignment:** How is the internal team model aligned with vendor contracts and finance cost centres? What data model sits underneath, and what is the operational process for keeping it current? How are shared services and platform teams handled?
3. **Work-item tagging in practice:** What tooling and process are used to tag tickets as RUN or BUILD? How is compliance enforced or incentivised? What does the degradation pattern look like, and how is it detected and corrected? Are there automated classification approaches, and what are their limits?
4. **Sponsorship and investment case:** Who typically spons…
```

**Scores:**

- `structural_completeness`: 0.5
- `coverage_overlap`: 0.101

**LLM Response (first 800 chars):**

```
I’m aligning the decomposition to the repo’s research workflow so the output matches the expected §1 structure rather than inventing a format.

● Search (glob)
  │ ".github/skills/research/SKILL.md"
  └ No matches found

● Search (glob)
  │ "research-prompt.md"
  └ 1 file found

● Read copilot-instructions.md
  │ .github/copilot-instructions.md
  └ L1:220 (219 lines read)

I found the repo prompt, so I’m pulling the exact §1 framing to mirror its decomposition style and avoid mismatching the expected research artifact.

● Search (glob)
  │ "Research/in-progress/*.md"
  └ 1 file found

● Search (grep)
  │ "§1|Question Decomposition|atomic question" (research-prompt.md)
  └ 24 lines found

● Search (glob)
  │ "Research/completed/*.md"
  └ 9 files found

I’ve got the formal requirement; now I…
```

### 2. 2026-02-28-ai-strategy-business-efficiency-examples

**Title:** AI Strategy Examples: Business Efficiency Focus

**Research Question:**

Which published AI strategies — corporate, national, or sector-specific — are explicitly designed around business efficiency as the primary objective, what measurable outcomes have they produced, and what design choices distinguish effective efficiency-focused AI programmes from those that underperform?

**Process Prompt:**

```
You are conducting research. Your task is to complete §1 Question Decomposition
for the following research question.

Research Question:
Which published AI strategies — corporate, national, or sector-specific — are explicitly designed around business efficiency as the primary objective, what measurable outcomes have they produced, and what design choices distinguish effective efficiency-focused AI programmes from those that underperform?

Approach sub-questions from the item:
1. **Survey published cases** — identify 8–12 corporate or government programmes where efficiency was the explicit primary objective and outcomes were published or independently reported.
2. **Extract design variables** — for each case: industry, AI type (Type 1–4 in the four-type typology), deployment model (build/buy/partner), data readiness approach, change management method, time to value, and outcome metric.
3. **Pattern analysis** — identify common success factors and failure modes across cases.
4. **NZ relevance filter** — assess which patterns are applicable to NZ-scale organisations (typically smaller, less data-rich than the global cases).
5. **Efficiency ceiling analysis** — what are the known limits of efficiency-focused AI deployment? When does efficiency-mode AI investment face diminishing returns?

Tags (topic area): ai-strategy, business-efficiency, productivity, operations, case-studies, financial-services

---

### §1 Question Decomposition

Recursively break the Approach sub-questions …
```

**Scores:**

- `structural_completeness`: 1.0
- `coverage_overlap`: 0.095

**LLM Response (first 800 chars):**

```
I’m checking the repo’s research format so the decomposition matches the expected house style, then I’ll lay out the full tree without answering any of the questions.

✗ Read SKILL.md
  │ .github/skills/research/SKILL.md
  └ Path does not exist

● Read research-prompt.md
  └ L1:220 (220 lines read)

● Search (grep)
  │ "§1|Question Decomposition|Atomic questions" in Research/**/*.md
  └ 10 files found

I found the workflow prompt but not the submodule skill file in this checkout, so I’m using the repo’s own prompt and a completed item to mirror the expected decomposition structure.

● Read 2026-04-29-knowledge-scaffolding-context-engineering.md
  │ Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md
  └ L60:180 (113 lines read)

● Read _template.md
  │ Research/_temp…
```

### 3. 2026-04-01-backpressure-theory-of-constraints

**Title:** Backpressure Infrastructure and the Theory of Constraints

**Research Question:**

What is backpressure infrastructure, specifically as it pertains to the Theory of Constraints (TOC), and what does academic research and real-world white papers say about its practical application?

**Process Prompt:**

```
You are conducting research. Your task is to complete §1 Question Decomposition
for the following research question.

Research Question:
What is backpressure infrastructure, specifically as it pertains to the Theory of Constraints (TOC), and what does academic research and real-world white papers say about its practical application?

Approach sub-questions from the item:
1. Define backpressure as used in TOC and operations management contexts
2. Trace academic and primary-source evidence for backpressure as a TOC implementation mechanism
3. Survey real-world case studies or white papers applying backpressure in TOC implementations
4. Connect backpressure to key TOC constructs: drum-buffer-rope, throughput accounting, Work in Progress (WIP) limits

Tags (topic area): theory-of-constraints, backpressure, systems-thinking, operations, lean

---

### §1 Question Decomposition

Recursively break the Approach sub-questions into atomic questions — each
answerable with a single evidence-based claim. For each atomic question, note:
- The parent Approach sub-question it belongs to
- Whether it is a factual, definitional, comparative, or evaluative question

Output the full decomposition tree. Do not answer the questions yet.

```

**Scores:**

- `structural_completeness`: 0.5
- `coverage_overlap`: 0.0

**LLM Response (first 800 chars):**

```
I’m pulling the repo’s research guidance first so the decomposition matches the house format instead of freelancing it.

● Search (glob)
  │ "**/{research-prompt.md,.github/skills/research/SKILL.md}"
  └ 1 file found

● Search (grep)
  │ "§1|Question Decomposition|decompose|atomic questions" in research-prompt.md
  └ 18 lines found

● Read research-prompt.md
  └ L100:140 (40 lines read)

● Search (grep)
  │ "factual|definitional|comparative|evaluative" in **/*
  └ 5 lines found

I found the repo guidance. I’m checking one completed item for the expected tree shape, then I’ll write the full atomic breakdown.

● Search (grep)
  │ "### §1 Question Decomposition" in completed/**/*.md (Research)
  └ No matches found

● Search (grep)
  │ "### §1 Question Decomposition" in in-progress/**/*.md (Re…
```
