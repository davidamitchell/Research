# Theme Report

**Canonical themes in vocabulary:** 22  
**Items scanned:** 446  
**Items with themes:** 444  
**Uncovered items (no themes:):** 2  
**Near-duplicate vocabulary candidates:** 0  
**Stray (non-vocabulary) themes in corpus:** 38  
**Mappable stray themes:** 36  
**Genuine gap themes:** 2  
**Unused canonical themes:** 0

---

## Coverage — uncovered items

> Items without a `themes:` field. These should be enriched via `enrich-items.yml`.
> If count is 0, coverage is complete.

- `2026-05-19-align-strategic-relevance-with-low-effort-knowledge-pathways`
- `2026-06-10-ai-productivity-quality-governance-open-questions`

---

## Near-duplicate vocabulary candidates

> Canonical slugs with Levenshtein distance ≤ 2 or token Jaccard ≥ 0.6.
> Candidates for future vocabulary consolidation (requires ≥3-item policy check).

_None found._

---

## Mappable stray themes

> Stray themes that can be normalised to an existing canonical theme.
> Add high-confidence aliases to `docs/themes-vocabulary.md` or rewrite the item.

| Stray theme | Suggested canonical | Confidence | Basis |
|---|---|---|---|
| `causal-inference` | `llm-reasoning` | high | alias in vocabulary |
| `causal-modeling` | `ai-architecture` | high | alias in vocabulary |
| `causal-reasoning` | `llm-reasoning` | high | alias in vocabulary |
| `causal-representation-learning` | `ai-architecture` | high | alias in vocabulary |
| `computational-theory` | `ai-architecture` | high | alias in vocabulary |
| `decision-making` | `agentic-ai` | high | alias in vocabulary |
| `distributed-complexity` | `multi-agent` | high | alias in vocabulary |
| `distribution-shift` | `security-risk` | high | alias in vocabulary |
| `dynamical-systems-theory` | `ai-architecture` | high | alias in vocabulary |
| `effort-minimisation` | `cost-performance` | high | alias in vocabulary |
| `epistemic-formalism` | `formal-methods` | high | alias in vocabulary |
| `epistemic-foundations` | `formal-methods` | high | alias in vocabulary |
| `epistemology-of-ai` | `formal-methods` | high | alias in vocabulary |
| `explainability-transparency` | `human-ai-interaction` | high | alias in vocabulary |
| `formal-epistemology` | `formal-methods` | high | alias in vocabulary |
| `formal-guarantees` | `formal-methods` | high | alias in vocabulary |
| `formal-learning-theory` | `formal-methods` | high | alias in vocabulary |
| `formal-reliability` | `formal-methods` | high | alias in vocabulary |
| `formal-verification` | `formal-methods` | high | alias in vocabulary |
| `information-asymmetry` | `governance-policy` | high | alias in vocabulary |
| `knowledge-transfer` | `knowledge-management` | high | alias in vocabulary |
| `low-code-development` | `tools-infrastructure` | high | alias in vocabulary |
| `model-interpretability` | `ai-architecture` | high | alias in vocabulary |
| `observability-monitoring` | `mlops-deployment` | high | alias in vocabulary |
| `organisational-behaviour` | `organisational-design` | high | alias in vocabulary |
| `organisational-impact` | `enterprise-adoption` | high | alias in vocabulary |
| `organisational-learning` | `organisational-design` | high | alias in vocabulary |
| `organisational-theory` | `organisational-design` | high | alias in vocabulary |
| `psychological-safety` | `human-ai-interaction` | high | alias in vocabulary |
| `robust-system-design` | `security-risk` | high | alias in vocabulary |
| `system-dynamics` | `ai-architecture` | high | alias in vocabulary |
| `system-interpretability` | `ai-architecture` | high | alias in vocabulary |
| `system-reliability` | `mlops-deployment` | high | alias in vocabulary |
| `theorem-proving` | `formal-methods` | high | alias in vocabulary |
| `vendor-management` | `governance-policy` | high | alias in vocabulary |
| `workflow-automation` | `tools-infrastructure` | high | alias in vocabulary |

---

## Candidate aliases for vocabulary growth

> Canonical themes that would absorb the most currently-unmapped stray themes.
> Only add aliases when the growth-policy threshold (≥3 items) is met.

_No candidate aliases from heuristic matching._

---

## Stray themes (not in canonical vocabulary)

> Theme slugs found in corpus items that are not in `docs/themes-vocabulary.md`
> and could not be mapped to a canonical theme. These may be genuine new themes
> or pre-migration artefacts.

`causal-robustness`, `epistemic-robustness`

---

## Unused canonical themes

> Canonical slugs with zero corpus items. Consider whether they are
> still needed or should be removed from the vocabulary.

_All canonical themes are in use._

---

## Theme frequency

| Theme | Item count |
|---|---|
| `agentic-ai` | 235 |
| `tools-infrastructure` | 215 |
| `governance-policy` | 213 |
| `ai-architecture` | 158 |
| `security-risk` | 118 |
| `knowledge-management` | 104 |
| `benchmarks-eval` | 89 |
| `organisational-design` | 88 |
| `workforce-skills` | 73 |
| `cost-performance` | 58 |
| `llm-reasoning` | 50 |
| `mlops-deployment` | 49 |
| `memory-context` | 46 |
| `rag-retrieval` | 43 |
| `software-engineering` | 43 |
| `knowledge-graphs` | 39 |
| `enterprise-adoption` | 28 |
| `consciousness-cognition` | 25 |
| `formal-methods` | 24 |
| `regulatory-compliance` | 19 |
| `multi-agent` | 12 |
| `human-ai-interaction` | 11 |
| `organisational-learning` | 4 |
| `causal-inference` | 2 |
| `causal-modeling` | 2 |
| `epistemic-foundations` | 2 |
| `epistemology-of-ai` | 2 |
| `formal-verification` | 2 |
| `causal-reasoning` | 1 |
| `causal-representation-learning` | 1 |
| `causal-robustness` | 1 |
| `computational-theory` | 1 |
| `decision-making` | 1 |
| `distributed-complexity` | 1 |
| `distribution-shift` | 1 |
| `dynamical-systems-theory` | 1 |
| `effort-minimisation` | 1 |
| `epistemic-formalism` | 1 |
| `epistemic-robustness` | 1 |
| `explainability-transparency` | 1 |
| `formal-epistemology` | 1 |
| `formal-guarantees` | 1 |
| `formal-learning-theory` | 1 |
| `formal-reliability` | 1 |
| `information-asymmetry` | 1 |
| `knowledge-transfer` | 1 |
| `low-code-development` | 1 |
| `model-interpretability` | 1 |
| `observability-monitoring` | 1 |
| `organisational-behaviour` | 1 |
| `organisational-impact` | 1 |
| `organisational-theory` | 1 |
| `psychological-safety` | 1 |
| `robust-system-design` | 1 |
| `system-dynamics` | 1 |
| `system-interpretability` | 1 |
| `system-reliability` | 1 |
| `theorem-proving` | 1 |
| `vendor-management` | 1 |
| `workflow-automation` | 1 |
