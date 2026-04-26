# 2026-04-26 — Multiple AI/low-code governance research questions backlog intake

**Completed:**
- `Research/backlog/2026-04-26-ai-lowcode-risk-tier-classification-controls.md` — Q5: validated research question on risk tier classification for AI and low-code use cases, including how governance controls, oversight intensity, and approval thresholds vary across tiers; foundational item that blocks Q1, Q9, Q8
- `Research/backlog/2026-04-26-ai-agent-identity-access-management-enterprise.md` — Q2: validated research question on identity and access management (IAM) for non-human actors (AI agents, low-code artefacts) — machine identity standards, delegation models, credential management, attribution; prerequisite for Q3, Q4, Q16
- `Research/backlog/2026-04-26-ai-lowcode-regulatory-compliance-alignment.md` — Q15: validated research question on mapping enterprise AI/low-code governance mechanisms to external regulatory obligations (EU AI Act, GDPR, APRA CPS 230, DORA, FCA/PRA); blocks Q1, Q16, Q13
- `Research/backlog/2026-04-26-ai-lowcode-failure-modes-governance-mitigation.md` — Q12: validated research question on primary failure modes in AI and low-code deployments (data leakage, conflicting automations, prompt injection, loss of auditability) and governance preventative/corrective controls; blocks Q3, Q16
- `Research/backlog/2026-04-26-ai-governance-culture-incentives-behaviour.md` — Q14: validated research question on how organisational incentives, culture, and behaviour drive governance circumvention (shadow IT, workarounds) and what design conditions produce durable compliance; blocks Q13
- `Research/backlog/2026-04-26-ai-lowcode-decision-rights-accountability-liability.md` — Q1: validated research question on RACI structures, approval models, production ownership, separation of duties, escalation paths, and liability allocation for AI/low-code systems; requires Q5, Q15; blocks Q9, Q16, Q13
- `Research/backlog/2026-04-26-ai-lowcode-governance-enforcement-architecture.md` — Q3: validated research question on governance enforcement point placement across enterprise architecture layers (API gateways, data access, orchestration, model runtime) and control type mapping; requires Q2; blocks Q4, Q10, Q16
- `Research/backlog/2026-04-26-data-governance-ai-lowcode-enterprise-enforcement.md` — Q6: validated research question on enforcing data classification, lineage, access controls, and sensitive data restrictions consistently within AI and low-code runtime environments; blocks Q4, Q7, Q16
- `Research/backlog/2026-04-26-ai-lowcode-lifecycle-management.md` — Q7: validated research question on comprehensive lifecycle management for AI models, prompts, and low-code artefacts (versioning, deployment gates, rollback, ownership, decommissioning); requires Q6; blocks Q10, Q16
- `Research/backlog/2026-04-26-ai-lowcode-observability-telemetry-governance.md` — Q4: validated research question on what must be logged for AI/low-code governance (prompts, decisions, actions, attribution), at what granularity, with what retention and correlation model; requires Q2, Q3, Q6; blocks Q8, Q16
- `Research/backlog/2026-04-26-human-in-the-loop-ai-automated-workflows.md` — Q9: validated research question on trigger conditions, thresholds, escalation procedures, override mechanisms, and automation bias mitigation for human oversight of AI-driven workflows; requires Q1, Q5; blocks Q16, Q8
- `Research/backlog/2026-04-26-vendor-platform-governance-constraints-compensating-controls.md` — Q11: validated research question on vendor platform governance capability gaps and compensating control design across major AI and low-code platforms (Power Platform, Azure AI Foundry, Salesforce, AWS Bedrock); blocks Q16
- `Research/backlog/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.md` — Q10: validated research question on integrating AI/low-code governance into CI/CD pipelines, infrastructure-as-code, testing frameworks, release management, and internal developer platforms; requires Q3, Q7; blocks Q8, Q16
- `Research/backlog/2026-04-26-ai-governance-cost-performance-delivery-impact.md` — Q8: validated research question on the economic model for AI/low-code governance trade-offs (implementation cost, operational overhead, developer friction, centralised vs federated governance); requires Q3, Q4, Q7, Q10; blocks Q13
- `Research/backlog/2026-04-26-ai-agent-control-plane-architecture-enterprise.md` — Q16: validated research question on the control-plane architecture for managing AI agents and low-code as distributed semi-autonomous actors (policy creation/propagation/enforcement, control-observability-feedback loop); requires Q1–Q12, Q15; blocks Q13
- `Research/backlog/2026-04-26-ai-lowcode-governance-maturity-model.md` — Q13: validated research question on the maturity model for AI/low-code governance capability evolution (stage definitions, capability benchmarks, progression pathways, assessment instrument); requires all other items; final synthesis item

## Dependency ordering

The 16 items form four tiers of dependency:

**Tier 1 — Foundational (no prerequisites among the 16):**
- Q5 (risk tiers) — most broadly foundational; blocks Q1, Q8, Q9
- Q2 (IAM) — prerequisite for enforcement and observability; blocks Q3, Q4, Q16
- Q12 (failure modes) — adversarial analysis independent of governance design; blocks Q3, Q16
- Q14 (culture/incentives) — behavioural analysis independent of structural design; blocks Q13
- Q15 (regulatory) — regulatory landscape independent of internal governance design; blocks Q1, Q16, Q13

**Tier 2 — Structurally dependent on Tier 1:**
- Q1 (decision rights) — requires Q5, Q15; blocks Q9, Q16, Q13
- Q3 (enforcement) — requires Q2; blocks Q4, Q10, Q16
- Q6 (data governance) — parallel with Q3; blocks Q4, Q7, Q16

**Tier 3 — Operationally dependent on Tier 2:**
- Q4 (observability) — requires Q2, Q3, Q6; blocks Q8, Q16
- Q7 (lifecycle) — requires Q6; blocks Q10, Q16
- Q9 (human-in-loop) — requires Q1, Q5; blocks Q16, Q8
- Q11 (vendor constraints) — parallel investigation; blocks Q16

**Tier 4 — Integration dependent on Tier 3:**
- Q10 (SDLC integration) — requires Q3, Q7; blocks Q8, Q16
- Q8 (cost/impact) — requires Q3, Q4, Q7, Q9, Q10; blocks Q13
- Q16 (control-plane) — requires Q1–Q12, Q15; blocks Q13

**Tier 5 — Synthesis:**
- Q13 (maturity model) — requires Q1–Q12, Q14–Q16; no blocks

## Mini-Retro

1. **Did the process work?** Yes. The 16 questions in the issue were well-articulated but needed structuring — they were listed independently without explicit cross-references or dependency ordering. The primary work was mapping the dependency graph and ensuring each backlog item's scope was bounded correctly relative to its companion items.

2. **What slowed down or went wrong?** The question numbering in the issue did not correspond to a natural dependency ordering, requiring explicit dependency analysis before writing scope statements. The Q1 file initially contained a duplicate `## Research Question` section (caught and corrected before commit). The volume of items (16) made it important to be disciplined about scope boundaries to avoid overlap — particularly between Q3 (enforcement architecture) and Q16 (control-plane architecture), and between Q7 (lifecycle) and Q10 (SDLC integration).

3. **What single change would prevent this next time?** For multi-question issues, explicitly map the dependency graph before creating any files — it is faster to reason about dependencies in the abstract than to discover inconsistencies after writing scope sections.

4. **Is this a pattern?** Second occurrence of a multi-question issue in this repo (the first was also in a 2026-04-26 session). The pattern is now established. The instructions note that "distinct PRs" in a multi-question issue means the agent creates all items in one PR.

5. **Does any documentation need updating?** No — the conventions followed are consistent with existing `copilot-instructions.md` requirements. The dependency ordering information is recorded in this session log and in the `## Context` and `blocks:` fields of each backlog item.

6. **Do the default instructions need updating?** No new conventions emerged. The existing multi-question issue handling note in the progress log for `2026-04-26-multiple-research-questions-backlog-intake.md` remains applicable.
