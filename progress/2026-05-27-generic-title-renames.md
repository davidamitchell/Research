# 2026-05-27 — Generic title renames (second pass)

## Objective

A second pass over the research corpus to rename titles identified as too generic — titles
that use vague category labels ("Examples", "Framework", "Methodology", "Survey") or
omit the specific finding, key statistic, or design decision the item actually contains.

## Files changed

13 completed items — `title:` frontmatter and `# Title` H1 heading updated in each.

| File | Old title | New title |
|---|---|---|
| `2026-02-28-ai-strategy-risk-reduction-focus.md` | AI Strategy Examples: Risk Reduction Focus | Artificial Intelligence (AI) risk-reduction deployments in financial services: fraud and Anti-Money Laundering (AML) outcome evidence, regulatory framework mapping, and model bias as dominant failure mode |
| `2026-02-28-ai-strategy-swe-focus.md` | AI Strategy Examples: Software Engineering Focus | Artificial Intelligence (AI) coding assistant deployment outcomes: individual productivity evidence, Google's 25% code disclosure, DORA stability degradation, and the Type 2 to Type 3 governance boundary |
| `2026-02-28-ai-strategy-business-efficiency-examples.md` | AI Strategy Examples: Business Efficiency Focus | Enterprise Artificial Intelligence (AI) efficiency programme outcomes: why 74% fail to scale, three success conditions, and evidence from ANZ Bank's $1.9 billion productivity programme |
| `2026-02-28-ai-strategy-security-focus.md` | AI Strategy Examples: Security Focus | Artificial Intelligence (AI) security strategy: 1,265% AI-enhanced phishing growth, prompt injection as highest-severity agentic vulnerability, and the New Zealand (NZ) regulatory guidance gap |
| `2026-02-28-ai-line-1-line-2-risk-agents.md` | AI Line 1 and Line 2 Risk Agents: Who Is Building Them? | Artificial Intelligence (AI) agents in financial services line 1 and line 2 functions: vendor platform dominance, existing regulatory framework application, and the unresolved nominal-review accountability problem |
| `2026-02-28-exploit-explore-ai-portfolio-framework.md` | Exploit vs Explore: A Decision Framework for AI Portfolio Planning | Exploit versus explore Artificial Intelligence (AI) investment classification: five-dimension scoring diagnostic, March's competency trap, and 70/20/10 horizon-differentiated portfolio governance |
| `2026-03-02-research-quality-assurance-methodology.md` | Research Quality Assurance and Knowledge Integration Methodology | Coverage gaps in automated research review skills, peer review patterns for Artificial Intelligence (AI) agents, and cross-item integration methodology using the Data, Information, Knowledge, Wisdom (DIKW) hierarchy |
| `2026-03-03-ml-techniques-and-algorithms.md` | ML techniques, algorithms, and advanced analytics — a systematic reference for analytics teams | Machine Learning (ML) technique taxonomy and selection criteria for analytics teams: supervised, unsupervised, and advanced methods with maturity benchmarks distinguishing routine from advanced practice |
| `2026-03-05-general-agent-optimization-framework.md` | General Agent Optimization Framework | Self-improving Artificial Intelligence (AI) agent evaluation loop architecture: DSPy and MIPRO for inner-loop prompt optimisation, adversarial outer-loop variation, and benchmark harness selection |
| `2026-03-15-neurological-context-management.md` | Neurological Basis of Contextual Reasoning and Relevance Filtering | Working memory architecture, prefrontal cortex contextual gating, and predictive processing as neurological design principles for Artificial Intelligence (AI) context management |
| `2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md` | IT Throughput Constraint Magnitude and Debt Accumulation Rate | Information Technology (IT) throughput capacity as a constraint on unmet operational capability demand accumulation: empirical evidence and Artificial Intelligence (AI)-assisted delivery absorption modelling |
| `2026-05-16-decommission-trigger-design-for-do-mode-agents.md` | Decommission Trigger Design for Temporary Bridge Agents | Automated decommission of temporary bridge Artificial Intelligence (AI) agents: expiring exception registration, machine-observed supersession signals, and enforcement without manual intervention |
| `2026-05-17-aws-bedrock-capabilities.md` | AWS Bedrock: full feature and capability survey | Amazon Web Services (AWS) Bedrock platform capabilities: model access, agents, knowledge bases, guardrails, evaluation, and enterprise governance primitives for regulated environments |

## Validation

- `make check`: all checks passed
- `python -m pytest tests/ -q`: 612 passed, 1 expected env-gated failure (`test_tavily_api_key_is_configured`)
