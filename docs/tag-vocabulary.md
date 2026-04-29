# Tag Vocabulary

This file defines the canonical tag vocabulary for the research corpus. It is
the evidence-based result of running `scripts/tag_report.py` (W-0053) and
reviewing the co-occurrence report in `state/tag_report.md`.

When writing or completing a research item, consult this vocabulary and use
only canonical tag forms. Do not invent new tags that are near-synonyms of
existing canonical tags.

## How to read this file

Each cluster below lists one **canonical** tag and zero or more **aliases**
that should be rewritten to it. The YAML block at the end of this file is the
machine-readable version loaded by `scripts/canonicalise_tags.py`.

## Clusters

| Canonical | Aliases | Rationale |
|---|---|---|
| `agentic-ai` | `ai`, `agent`, `ai-agents`, `agents`, `agentic-systems` | Highest-frequency cluster (25 items). `agentic-ai` is the most precise and most common form. |
| `llm` | `large-language-model`, `llm-agent` | `llm` is the established abbreviation; expanded forms are rare singletons. |
| `hallucinations` | `hallucination` | Plural form is more common (5 vs 3 items); matches standard AI research usage. |
| `memory-system` | `memory-systems` | Singular form is 4× more common (8 vs 2 items). |
| `workflow` | `workflows` | Singular canonical; 4× more common (8 vs 2 items). |
| `ai-platform` | `ai-platforms` | Singular canonical; equal frequency; hyphenated form preferred. |
| `knowledge-graph` | `knowledge-graphs` | Singular canonical; equal frequency. |
| `organisation` | `organisations` | Singular canonical; equal frequency; UK/NZ spelling retained. |
| `analytics` | `advanced-analytics` | `analytics` is broader and more common; `advanced-analytics` always co-occurs with `analytics` (100%). |
| `organisational-learning` | `organizational-learning` | UK/NZ spelling is canonical; both are singletons in the corpus but clearly the same concept. |
| `organisational-theory` | `organizational-theory` | UK/NZ spelling is canonical; same rationale as above. |
| `organisational-design` | `organisation-design`, `org-design` | Most common form (6 items); `org-design` (2) and `organisation-design` (1) are variants. |
| `agentic-coding` | `ai-coding`, `ai-assisted-development` | `agentic-coding` is more common (3 vs 1 each); covers AI-driven code generation. |
| `ricardian-contracts` | `ricardian-contract` | Plural canonical; both are singletons but clearly the same concept. |
| `lecun` | `yann-lecun` | `lecun` appears in 2 items; `yann-lecun` is a singleton near-duplicate. |
| `now-assist` | `nowassist` | ServiceNow Now Assist product; hyphenated form is consistent with tagging conventions. |
| `agent-tooling` | `agent-harnesses` | Both refer to infrastructure scaffolding around LLM agents; `agent-tooling` is more common (2 vs 1). |
| `evaluation` | `evals` | `evaluation` is more common (6 items); `evals` is a singleton abbreviation. |
| `invariants` | `invariant` | Plural canonical; both are singletons; plural aligns with technical usage. |
| `tdd` | `test-driven-development` | Both are singletons; `tdd` is the established abbreviation used in BACKLOG and instructions. |

---

## Machine-readable map

The YAML block below is parsed by `scripts/canonicalise_tags.py`.
Each key is the canonical tag. The list value contains aliases that map to it.

```yaml
agentic-ai:
  - ai
  - agent
  - ai-agents
  - agents
  - agentic-systems
llm:
  - large-language-model
  - llm-agent
hallucinations:
  - hallucination
memory-system:
  - memory-systems
workflow:
  - workflows
ai-platform:
  - ai-platforms
knowledge-graph:
  - knowledge-graphs
organisation:
  - organisations
analytics:
  - advanced-analytics
organisational-learning:
  - organizational-learning
organisational-theory:
  - organizational-theory
organisational-design:
  - organisation-design
  - org-design
agentic-coding:
  - ai-coding
  - ai-assisted-development
ricardian-contracts:
  - ricardian-contract
lecun:
  - yann-lecun
now-assist:
  - nowassist
agent-tooling:
  - agent-harnesses
evaluation:
  - evals
invariants:
  - invariant
tdd:
  - test-driven-development
```
