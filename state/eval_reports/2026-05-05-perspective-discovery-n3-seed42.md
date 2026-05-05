# Process Evaluation Report — perspective-discovery

**Process:** §0.5b Perspective Discovery — four-slot STORM-grounded template (basic facts / mechanism / stakeholder / failure-mode) generates seed questions before §1 decomposition.
**Sampled:** 3 of 3 requested
**Seed:** 42
**Generated:** 2026-05-05T10:20:52.930386+00:00
**Scored:** yes

## Summary Scores

| Metric | Mean |
| --- | --- |
| Structural completeness | 1.0 |
| Coverage overlap (Jaccard) | 0.079 |
| Perspective slots filled | 0.5 |

## Items

### 1. 2026-03-07-run-build-it-allocation-implementation-how

**Title:** How organisations practically implement IT RUN vs BUILD cost allocation

**Research Question:**

How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: how did they agree on what counts as an "application", how did they get consistent work-item tagging across teams, how did they establish a shared team taxonomy, who drove the change, and how did they make the business case for the investment required?

**Process Prompt:**

```
You are conducting research. Your task is to complete §0.5b Perspective Discovery
before beginning investigation on the following research question.

Research Question:
How have organisations actually implemented a working RUN vs BUILD IT cost allocation — specifically: how did they agree on what counts as an "application", how did they get consistent work-item tagging across teams, how did they establish a shared team taxonomy, who drove the change, and how did they make the business case for the investment required?

Tags (topic area): it-finance, run-build, cost-allocation, application-portfolio, change-management, organisational-design, tbm

---

### §0.5b Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research
perspectives for the question above. Use these four slots:

1. **Basic facts lens** — what a broad factual writer must cover first.
2. **Mechanism or implementation lens** — how the thing works, is built, or fails operationally.
3. **Stakeholder or decision-impact lens** — who is affected, who decides, and what trade-offs matter.
4. **Failure-mode or critic lens** — what could be missing, misleading, risky, or overstated.

For each perspective, output exactly:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer …
```

**Scores:**

- `structural_completeness`: 1.0
- `coverage_overlap`: 0.107
- `perspective_slots`: 0.0

**LLM Response (first 800 chars):**

```
1. Perspective: Enterprise taxonomy mapper  
Distinct coverage added: This lens defines the factual baseline of how organisations drew the boundary around "application", "team", and "work type" so later implementation details are comparable.  
Seed question: In organisations that implemented RUN vs BUILD IT allocation, what formal definition and inclusion rules did they use to decide whether a cost belonged to an application versus shared platform, infrastructure, or project work?  
Evidence to seek: Operating model documents, TBM case studies, finance or portfolio governance artefacts, and published allocation policy manuals.

2. Perspective: Delivery instrumentation architect  
Distinct coverage added: This lens focuses on the operational mechanics of getting consistent tagging and taxon…
```

### 2. 2026-02-28-ai-strategy-business-efficiency-examples

**Title:** AI Strategy Examples: Business Efficiency Focus

**Research Question:**

Which published AI strategies — corporate, national, or sector-specific — are explicitly designed around business efficiency as the primary objective, what measurable outcomes have they produced, and what design choices distinguish effective efficiency-focused AI programmes from those that underperform?

**Process Prompt:**

```
You are conducting research. Your task is to complete §0.5b Perspective Discovery
before beginning investigation on the following research question.

Research Question:
Which published AI strategies — corporate, national, or sector-specific — are explicitly designed around business efficiency as the primary objective, what measurable outcomes have they produced, and what design choices distinguish effective efficiency-focused AI programmes from those that underperform?

Tags (topic area): ai-strategy, business-efficiency, productivity, operations, case-studies, financial-services

---

### §0.5b Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research
perspectives for the question above. Use these four slots:

1. **Basic facts lens** — what a broad factual writer must cover first.
2. **Mechanism or implementation lens** — how the thing works, is built, or fails operationally.
3. **Stakeholder or decision-impact lens** — who is affected, who decides, and what trade-offs matter.
4. **Failure-mode or critic lens** — what could be missing, misleading, risky, or overstated.

For each perspective, output exactly:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer that question>

Constraints:
- Prefer non-overlap over stylistic v…
```

**Scores:**

- `structural_completeness`: 1.0
- `coverage_overlap`: 0.067
- `perspective_slots`: 0.5

**LLM Response (first 800 chars):**

```
Perspective: Strategy cataloguer  
Distinct coverage added: This lens establishes the baseline map of which published AI strategies explicitly prioritize efficiency first and what outcomes they publicly claim.  
Seed question: Which corporate, national, and sector-specific AI strategies explicitly define productivity, cost reduction, or operational efficiency as their primary objective, and what measurable results do they report?  
Evidence to seek: Official strategy documents, policy papers, annual reports, and programme launch materials with stated objectives and KPIs.

Perspective: Operating-model analyst  
Distinct coverage added: This lens explains how efficiency-focused AI programmes are actually designed and run, including the implementation choices that enable or block results.  
S…
```

### 3. 2026-04-01-backpressure-theory-of-constraints

**Title:** Backpressure Infrastructure and the Theory of Constraints

**Research Question:**

What is backpressure infrastructure, specifically as it pertains to the Theory of Constraints (TOC), and what does academic research and real-world white papers say about its practical application?

**Process Prompt:**

```
You are conducting research. Your task is to complete §0.5b Perspective Discovery
before beginning investigation on the following research question.

Research Question:
What is backpressure infrastructure, specifically as it pertains to the Theory of Constraints (TOC), and what does academic research and real-world white papers say about its practical application?

Tags (topic area): theory-of-constraints, backpressure, systems-thinking, operations, lean

---

### §0.5b Perspective Discovery

Before §1 Question Decomposition, generate exactly four non-overlapping research
perspectives for the question above. Use these four slots:

1. **Basic facts lens** — what a broad factual writer must cover first.
2. **Mechanism or implementation lens** — how the thing works, is built, or fails operationally.
3. **Stakeholder or decision-impact lens** — who is affected, who decides, and what trade-offs matter.
4. **Failure-mode or critic lens** — what could be missing, misleading, risky, or overstated.

For each perspective, output exactly:
- Perspective: <short role label>
- Distinct coverage added: <one sentence on what this lens sees that the others may miss>
- Seed question: <one concrete research question this lens would ask first>
- Evidence to seek: <the kind of source most likely to answer that question>

Constraints:
- Prefer non-overlap over stylistic variety — if two perspectives collapse into the
  same question class, rewrite one.
- Keep every seed question specific enough th…
```

**Scores:**

- `structural_completeness`: 1.0
- `coverage_overlap`: 0.064
- `perspective_slots`: 1.0

**LLM Response (first 800 chars):**

```
I’m checking the repo’s research workflow wording so the perspective set matches the expected format exactly.

● Search (grep)
  │ "0\.5b Perspective Discovery|Perspective Discovery" in *.{md,py,yml,yaml}
  └ 21 lines found

● Search (grep)
  │ "Basic facts lens|Mechanism or implementation lens|Stakeholder or
  │ decision-impact lens|Failure-mode or critic lens" in *.{md,py,yml,yaml}
  └ 28 lines found

I found the exact template and I’m sampling prior perspective outputs to keep the lenses non-overlapping and specific.

● Read 2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md
  │ Research/completed/2026-05-02-storm-perspective-discovery-multi-perspective-
  │ question-generation.md
  └ L266:330 (65 lines read)

● Read 2026-05-05-perspective-discovery-n3-seed4…
```
