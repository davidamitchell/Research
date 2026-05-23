# Themes Vocabulary

This file defines the canonical `themes` field vocabulary for the research corpus. It
supersedes and unifies the legacy `tags:` field and the `ai_themes:` field — both of which
are retired by W-0077.

The vocabulary was designed using the findings of W-0076 (similarity algorithms and growth
policy for controlled vocabulary management) and the empirical `ai_themes` 16-item set
enriched across the corpus by W-0069.

When writing or completing a research item, consult this vocabulary and assign **only
canonical theme slugs** from the table below. Do not invent new slugs that are
near-synonyms of existing canonical themes — use the alias map to find the correct
canonical form. If a genuine concept is missing, record it in `gaps:` frontmatter and
raise it for review against the ≥3-item growth-policy threshold.

## How to read this file

Each row below lists one **canonical** theme slug and zero or more **aliases** that the
migration script (`scripts/canonicalise_themes.py`) rewrites to it automatically. The YAML
block at the end is the machine-readable map loaded by the script.

## Growth policy

A new canonical slug may be added to this vocabulary **only when**:

1. ≥3 research items require a concept not covered by any existing canonical slug or alias.
2. The candidate slug passes a near-duplicate check: Levenshtein edit distance > 2 **and**
   token Jaccard similarity < 0.6 against every existing canonical slug.
3. A human reviewer confirms the addition during a `theme-review.yml` workflow run (W-0080).

Do not add new themes during research sessions. Record the gap in `gaps:` frontmatter
instead. The monthly review workflow surfaces candidates automatically.

## Canonical themes

| Canonical slug | Aliases | Scope |
|---|---|---|
| `agentic-ai` | `ai`, `agent`, `ai-agents`, `agents`, `agentic-systems` | AI agents, tool use, autonomous decision-making systems |
| `llm-reasoning` | `prompt-engineering`, `chain-of-thought` | LLM (Large Language Model) reasoning, chain-of-thought prompting, structured output, prompt engineering |
| `memory-context` | `context-window`, `context-compression` | Memory management, context windows, compression, retrieval within a session |
| `multi-agent` | `multi-agent-systems`, `agent-coordination` | Multi-agent orchestration, coordination patterns, swarm architectures |
| `rag-retrieval` | `retrieval-augmented-generation`, `vector-search` | Retrieval-augmented generation (RAG), vector search, semantic retrieval |
| `governance-policy` | `ai-governance`, `ethics`, `low-code-governance` | AI governance, regulation, ethics, risk frameworks, policy |
| `benchmarks-eval` | `evaluation`, `evals`, `metrics`, `research-methodology` | Evaluation, benchmarks, metrics, measurement methodology |
| `security-risk` | `operational-risk`, `supply-chain-security`, `adversarial` | Adversarial attacks, security vulnerabilities, operational and supply-chain risk |
| `knowledge-graphs` | `ontologies`, `taxonomies` | Knowledge graphs, ontologies, taxonomies, structured knowledge representation |
| `consciousness-cognition` | `neuro-inspired-ai`, `cognitive-science`, `neuroscience` | Consciousness, cognitive science, neuroscience, neuro-inspired AI |
| `ai-architecture` | `mechanistic-interpretability`, `model-architecture`, `fine-tuning` | Model architecture, training, fine-tuning, mechanistic interpretability |
| `tools-infrastructure` | `workflow`, `workflow-automation`, `developer-experience`, `citizen-development`, `developer-tools` | MCP (Model Context Protocol), tooling, developer infrastructure, pipelines, workflow automation, low-code |
| `mlops-deployment` | `deployment`, `production-systems` | Deployment, MLOps (Machine Learning Operations), production system management |
| `workforce-skills` | `skills-gap`, `capability-building` | Workforce impact, skills gaps, capability building, talent development |
| `cost-performance` | `efficiency`, `performance-tradeoffs` | Cost optimisation, efficiency, performance trade-offs |
| `knowledge-management` | `pkm`, `information-architecture`, `personal-knowledge-management` | Personal knowledge management (PKM), information architecture, synthesis, research tooling |
| `organisational-design` | `organisation`, `org-design`, `organisation-design` | Organisational design, structure, reporting, change management |
| `regulatory-compliance` | `compliance-automation`, `legal-requirements` | Regulatory compliance, legal requirements, compliance automation |
| `human-ai-interaction` | `human-ai-collaboration`, `ux`, `human-computer-interaction` | Human-AI interaction, collaboration UX (User Experience), human-computer interaction |
| `formal-methods` | `formal-verification`, `program-synthesis` | Formal methods, formal verification, provable correctness, program synthesis |
| `software-engineering` | `software-engineering-practices`, `engineering-practices` | Software engineering practices, code quality, architecture, developer experience |
| `enterprise-adoption` | `enterprise-strategy`, `digital-transformation` | Enterprise adoption, digital transformation strategy, organisational change |

---

## Machine-readable map

The YAML block below is parsed by `scripts/canonicalise_themes.py`.
Each key is the canonical theme slug. The list value contains aliases that map to it.
An empty list means the slug has no known aliases.

```yaml
agentic-ai:
  - ai
  - agent
  - ai-agents
  - agents
  - agentic-systems
llm-reasoning:
  - prompt-engineering
  - chain-of-thought
memory-context:
  - context-window
  - context-compression
multi-agent:
  - multi-agent-systems
  - agent-coordination
rag-retrieval:
  - retrieval-augmented-generation
  - vector-search
governance-policy:
  - ai-governance
  - ethics
  - low-code-governance
benchmarks-eval:
  - evaluation
  - evals
  - metrics
  - research-methodology
security-risk:
  - operational-risk
  - supply-chain-security
  - adversarial
knowledge-graphs:
  - ontologies
  - taxonomies
consciousness-cognition:
  - neuro-inspired-ai
  - cognitive-science
  - neuroscience
ai-architecture:
  - mechanistic-interpretability
  - model-architecture
  - fine-tuning
tools-infrastructure:
  - workflow
  - workflow-automation
  - developer-experience
  - citizen-development
  - developer-tools
mlops-deployment:
  - deployment
  - production-systems
workforce-skills:
  - skills-gap
  - capability-building
cost-performance:
  - efficiency
  - performance-tradeoffs
knowledge-management:
  - pkm
  - information-architecture
  - personal-knowledge-management
organisational-design:
  - organisation
  - org-design
  - organisation-design
regulatory-compliance:
  - compliance-automation
  - legal-requirements
human-ai-interaction:
  - human-ai-collaboration
  - ux
  - human-computer-interaction
formal-methods:
  - formal-verification
  - program-synthesis
software-engineering:
  - software-engineering-practices
  - engineering-practices
enterprise-adoption:
  - enterprise-strategy
  - digital-transformation
```
