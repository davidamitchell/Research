---
title: "Enterprise AI use-case classification schema"
synthesised: 2026-05-05
status: draft
theme: "ai-use-case-classification"
source_items:
  - 2026-04-22-enterprise-ai-use-case-routing-frameworks
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
  - 2026-04-22-enterprise-ai-capability-model
  - 2026-04-24-business-led-low-code-agent-governance
tags: [agentic-ai, workflow, organisational-design, evaluation]
cites:
  - 2026-04-22-enterprise-ai-use-case-routing-frameworks
  - 2026-04-26-ai-lowcode-risk-tier-classification-controls
  - 2026-04-22-enterprise-ai-capability-model
  - 2026-04-24-business-led-low-code-agent-governance
confidence: medium
versions: []
---

# Enterprise AI use-case classification schema

## Synthesis Question

Across the routing, risk-tier, capability, and low-code governance items, what classification model best explains how an enterprise should sort Artificial Intelligence (AI) use cases so it can choose the right delivery lane, governance intensity, and prerequisite capability investment?

## Source Items

- **2026-04-22-enterprise-ai-use-case-routing-frameworks** — contributes the three-lane routing view: low-code business-led, pro-code custom, and developer productivity.
- **2026-04-26-ai-lowcode-risk-tier-classification-controls** — contributes the four-tier risk model based on action authority, consequence, and reversibility.
- **2026-04-22-enterprise-ai-capability-model** — contributes the dependency-map view that classifies use cases by whether they can reuse shared enterprise capability or first require foundational investment.
- **2026-04-24-business-led-low-code-agent-governance** — contributes the bounded low-code perspective that limits business-led creation to governed, low-risk, process-suitable cases.

## Perspectives Considered

- **Routing perspective** (`2026-04-22-enterprise-ai-use-case-routing-frameworks`) — classifies by delivery lane and governance checkpoint sequence; converges with the other items on proportional governance, but diverges by making platform route more explicit than internal capability readiness.
- **Risk-tier perspective** (`2026-04-26-ai-lowcode-risk-tier-classification-controls`) — classifies by action authority, consequence, human override, and reversibility; converges on risk-proportional control, but diverges from lane-based thinking by treating interface or vendor choice as secondary.
- **Capability-readiness perspective** (`2026-04-22-enterprise-ai-capability-model`) — classifies by whether a use case can safely reuse shared enterprise rails or exposes a missing foundation; converges on central governance as prerequisite, but diverges from pure risk models by centering reuse-versus-build decisions.
- **Bounded low-code operating-model perspective** (`2026-04-24-business-led-low-code-agent-governance`) — classifies business-led use cases by whether governance, environment controls, and support structures already exist; converges with the risk-tier item on bounded, low-risk admissibility and with the capability item on platform quality as a prerequisite.

## Cross-Item Findings

1. **The most useful enterprise classification is multi-axis, not single-axis: each use case should be classified simultaneously by delivery lane, risk tier, and capability readiness, because none of the source items alone covers all three decisions.** [inference; source: 2026-04-22-enterprise-ai-use-case-routing-frameworks, 2026-04-26-ai-lowcode-risk-tier-classification-controls, 2026-04-22-enterprise-ai-capability-model]
2. **Action authority and consequence are the primary boundary tests, while platform or builder persona only becomes relevant after that baseline risk is understood.** [inference; source: 2026-04-26-ai-lowcode-risk-tier-classification-controls, 2026-04-22-enterprise-ai-use-case-routing-frameworks, 2026-04-24-business-led-low-code-agent-governance]
3. **Business-led low-code is not a standalone class of safe AI use case; it is a conditional route that is appropriate only when the use case remains bounded, centrally governed, and cheap to reverse.** [inference; source: 2026-04-24-business-led-low-code-agent-governance, 2026-04-22-enterprise-ai-use-case-routing-frameworks, 2026-04-26-ai-lowcode-risk-tier-classification-controls]
4. **Developer productivity AI should usually start in its own internal-assistance lane, but it must be reclassified upward when it gains write authority, production execution, or other state-changing powers.** [inference; source: 2026-04-22-enterprise-ai-use-case-routing-frameworks, 2026-04-26-ai-lowcode-risk-tier-classification-controls]
5. **Classification is only decision-useful when it also tests whether shared enterprise rails already exist, because the same nominal use case can be acceptable in one organisation and premature in another with weaker governance, context, or platform controls.** [inference; source: 2026-04-22-enterprise-ai-capability-model, 2026-04-24-business-led-low-code-agent-governance, 2026-04-22-enterprise-ai-use-case-routing-frameworks]
6. **The practical purpose of classifying AI use cases is not merely to name them but to decide which control stack must be present before delivery proceeds, which means reclassification is required whenever autonomy, connected systems, data sensitivity, or business criticality changes.** [inference; source: 2026-04-26-ai-lowcode-risk-tier-classification-controls, 2026-04-22-enterprise-ai-capability-model, 2026-04-22-enterprise-ai-use-case-routing-frameworks]

## Contradictions and Tensions

| Tension | Items | Resolution |
|---|---|---|
| Three routing lanes versus four positive risk tiers appear inconsistent if treated as rival taxonomies. | `2026-04-22-enterprise-ai-use-case-routing-frameworks`; `2026-04-26-ai-lowcode-risk-tier-classification-controls` | **resolved** — they classify different things: routing chooses the delivery path, while tiers choose governance intensity within or across those paths. |
| A maturity or capability dependency map seems to compete with risk-tiering as the intake model. | `2026-04-22-enterprise-ai-capability-model`; `2026-04-26-ai-lowcode-risk-tier-classification-controls` | **resolved** — capability readiness is a prerequisite gate, not a substitute for risk classification. |
| The developer productivity lane can look like a low-risk exemption, while the risk-tier item says interface and vendor are secondary to action authority. | `2026-04-22-enterprise-ai-use-case-routing-frameworks`; `2026-04-26-ai-lowcode-risk-tier-classification-controls` | **open** — the sources agree that action-capable developer tooling should escalate, but they do not yet specify the exact boundary for hybrid coding agents that both assist and execute. |

## Confidence Map

| Finding | Confidence | Limiting factors |
|---|---|---|
| 1 | medium | Supported by three source items, but each source item is itself overall medium confidence and uses a different classification lens. |
| 2 | medium | Strong convergence on action and consequence, but the synthesis elevates this above route and persona through cross-item reasoning. |
| 3 | medium | Well supported by the low-code governance and routing items, but much of the low-code evidence rests on Microsoft and Robotic Process Automation (RPA) analogues rather than broad multi-vendor empirical studies. |
| 4 | medium | Supported by two items, but the exact escalation boundary for hybrid developer tools remains unresolved. |
| 5 | medium | Strongly implied by the capability and low-code items, but the proposition depends on organisation-relative readiness rather than a single external benchmark threshold. |
| 6 | medium | The reclassification logic is explicit in the risk-tier item and consistent with the other items, but trigger thresholds still require local policy design. |

## Open Questions

- What intake form is most usable for applying all three axes, route, risk tier, and capability readiness, without forcing business teams to learn a specialist governance vocabulary?
- At what exact point should a developer productivity assistant be reclassified as a bounded-action or autonomous-action system once it can edit, deploy, or trigger production workflows?
- Which minimum evidence set should prove that a use case can reuse shared enterprise rails rather than demanding new foundational investment first?

## Related

- [Enterprise AI platform operating models: organisational structure and ownership](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-enterprise-ai-platform-operating-models.md)
- [What control-plane architecture is required to manage Artificial Intelligence (AI) agents and low-code systems as distributed, semi-autonomous actors within enterprise environments?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-ai-agent-control-plane-architecture-enterprise.md)
- [AI governance assurance: change control, verification, and review loops](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-22-ai-governance-assurance-change-control-verification.md)
