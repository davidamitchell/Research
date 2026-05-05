# Process Evaluation Report — question-decomposition

**Process:** §1 Question Decomposition — recursively break Approach sub-questions into atomic questions, each answerable with a single evidence-based claim.
**Sampled:** 3 of 3 requested
**Seed:** 42
**Generated:** 2026-05-05T10:31:09.387239+00:00
**Scored:** yes

## Summary Scores

| Metric | Mean |
| --- | --- |
| Structural completeness | 0.5 |
| Coverage overlap (Jaccard) | 0.09 |

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

- `structural_completeness`: 1.0
- `coverage_overlap`: 0.104

**LLM Response (first 800 chars):**

```
## §1 Question Decomposition

**Root question:** How have organisations implemented a working RUN vs BUILD IT cost allocation model?

### 1. Application definition governance
**Parent Approach sub-question:** 1  
**Branch:** Defining the application boundary
- **Atomic Q1.1** *(definitional)* — What explicit criteria do organisations use to define an “application” in RUN/BUILD allocation models?
- **Atomic Q1.2** *(comparative)* — Do organisations define an application primarily as a business capability, a technical system, a deployment unit, or a supportable service?
- **Atomic Q1.3** *(comparative)* — Is the application boundary tied to ownership, support accountability, or financial accountability more often than to architecture?
- **Atomic Q1.4** *(factual)* — Do organisations maintain…
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

- `structural_completeness`: 0.0
- `coverage_overlap`: 0.084

**LLM Response (first 800 chars):**

```
## §1 Question Decomposition

### 0. Framing and inclusion logic
These framing questions support the full investigation but do **not** answer the research question.

- **0.1** What counts as a **published Artificial Intelligence (AI) strategy or programme** for this study: formal strategy document, annual report disclosure, ministerial strategy, regulator-backed sector plan, or independently reported transformation programme?  
  **Type:** definitional
- **0.2** What evidence is sufficient to classify **business efficiency** as the **primary objective** rather than a secondary benefit?  
  **Type:** definitional
- **0.3** What counts as a **measurable outcome**: cost reduction, time reduction, throughput increase, error reduction, productivity uplift, service-level improvement, or return o…
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
- `coverage_overlap`: 0.083

**LLM Response (first 800 chars):**

```
## §1 Question Decomposition

**Root question:** *What is backpressure infrastructure, specifically as it pertains to the Theory of Constraints (TOC), and what does academic research and real-world white papers say about its practical application?*

### 1. Define backpressure as used in Theory of Constraints (TOC) and operations management contexts
1.1 **Terminology and scope**
- **AQ1.1** What definition of **backpressure** is used in operations management literature?  
  - Parent: **1**
  - Type: **definitional**
- **AQ1.2** Is backpressure described as a control mechanism, a flow-regulation mechanism, or a scheduling rule in operations contexts?  
  - Parent: **1**
  - Type: **comparative**
- **AQ1.3** Does TOC literature explicitly use the term **backpressure**, or does it rely on adja…
```
