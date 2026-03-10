---
title: "Adversarial agents with shared goals: multi-perspective coverage across competencies and time horizons"
added: 2026-03-10
status: backlog
priority: high
blocks: []
tags: [multi-agent, adversarial-collaboration, competency-coverage, time-horizons, fitness-functions, organisational-design, red-team, quality-assurance, values-alignment]
started: ~
completed: ~
output: [knowledge]
---

# Adversarial agents with shared goals: multi-perspective coverage across competencies and time horizons

## Research Question

What is the design pattern for a system of agents — human or AI — that share a common goal but deliberately occupy different competency domains and time horizons? How does "adversarial collaboration" (each agent challenging from a distinct perspective) produce better outcomes than a single generalist? What are the required agent roles, the interaction protocol between them, and the conditions under which disagreement is productive rather than blocking?

## Scope

**In scope:**
- The principle of adversarial collaboration: agents with a shared goal but deliberately different perspectives, each challenging the others' blind spots
- Competency-domain coverage: the specific agent types that provide non-overlapping coverage (see candidate list below)
- Time-horizon coverage: the different temporal scopes across which agents reason (immediate, sprint, quarterly, annual, multi-year, permanent)
- Interaction protocols: how agents with different competencies surface disagreements without deadlock; how shared-goal alignment is maintained under local optima pressure
- Mapping to organisational structures: how traditional review boards, design councils, and cross-functional teams instantiate this pattern
- Mapping to AI multi-agent systems: how multiple LLM agents with different system prompts (personas/roles) can provide multi-perspective coverage for a single task
- The relationship to the BBC Five Case Model: each case (strategic, economic, commercial, financial, management) as a distinct adversarial perspective
- How values alignment and strategic alignment agents function as "wisdom-layer" reviewers — the K→W gatekeepers in the DIKW framing
- Conditions for productive disagreement: when does a vetoing perspective improve quality vs. create gridlock?

**Out of scope:**
- Competitive multi-agent systems where agents have genuinely opposed goals (game theory, zero-sum)
- Full formal treatment of mechanism design or social choice theory
- Specific AI model comparison for multi-agent tasks

**Constraints:** Ground the framework in real-world implementations (design review panels, Site Reliability Engineering's "error budget" negotiation with product teams, security review gates, investment committee structures) before extending to AI multi-agent systems.

## Context

### The core insight

A single capable agent — human or AI — optimises for what it knows and can see. A designer optimises for usability; an SRE optimises for reliability; a security reviewer optimises for threat surface reduction. Each is locally rational but globally suboptimal in isolation. The adversarial collaboration pattern places these agents in deliberate tension: they share the goal of shipping something good but challenge each other's assumptions from non-overlapping vantage points.

This is not committee design by accident — it is a structural mechanism for covering the blind spots that any single perspective necessarily has.

### Candidate agent types and their time horizons

| Agent | Primary concern | Time horizon | DIKW layer |
|---|---|---|---|
| **Designer** | User experience, systemic coherence, aesthetic fit | Sprint → quarter | Information → Knowledge |
| **SRE** | Reliability, availability, observability, incident response | Operational (hours–weeks) | Data → Information |
| **Tester** | Correctness, edge cases, coverage, regression | Sprint | Data → Information |
| **Security** | Threat surface, vulnerabilities, compliance posture | Immediate + architectural (long) | Knowledge |
| **Performance — speed/resource** | Latency, throughput, resource cost | Sprint → quarter | Data → Information |
| **Performance — ROI** | Return on investment, cost/benefit, opportunity cost | Quarterly → annual | Information → Knowledge |
| **Performance — goal achievement** | OKR delivery, outcomes vs. outputs, impact | Quarterly → annual | Knowledge → Wisdom |
| **Strategic alignment** | Are we building the right thing? Is this consistent with direction? | Multi-year | Wisdom |
| **Insight capture** | What have we learned? Is learning being retained? | Continuous / retrospective | Knowledge |
| **Researcher** | What do we not know? Where are the unknown unknowns? | Long / pre-competitive | Knowledge → Wisdom |
| **Architecture** | Technical structure, constraints, coupling, evolution | Medium → long | Knowledge |
| **Architecture alignment** | Is the technical structure consistent with the strategic direction? | Long | Knowledge → Wisdom |
| **Values alignment** | Is this consistent with our stated values and principles? | Permanent | Wisdom |
| **Change impact assessment** | What breaks? What changes for users, systems, teams? | Immediate | Data → Information |
| **Risk assessment** | What could go wrong? What is the probability and severity? | Variable (sprint → long) | Knowledge |

### Why time horizons matter

Agents reasoning at different time horizons will make different decisions about the same trade-off. An SRE and a strategic alignment reviewer looking at the same architectural change will disagree — not because one is wrong, but because the trade-off is genuinely different at different time scales. The adversarial collaboration pattern *requires* this disagreement to surface and be resolved explicitly rather than letting the fastest or loudest perspective dominate.

### Connection to organisational theory

This pattern is the operational instantiation of the Coase/North framework:
- Each agent type is an internal coordination function whose cost of externalisation (market contracting) is high due to asset specificity (Williamson)
- The interaction protocol between agents is the informal institution (North) that reduces coordination costs
- When an agent type is absent, the organisation bears a hidden coordination cost — the cost of discovering (usually late, usually expensively) the perspective that was missing

The BBC Five Case Model (`Research/completed/2026-03-08-bbc-five-case-model.md`) is a formalised instance of this pattern for investment decisions: five mandated perspectives (strategic, economic, commercial, financial, management), each required before a case can proceed.

### Connection to DIKW

Different agent types operate at different DIKW levels. Testers and SREs work primarily at Data → Information (instrumentation, observation, signal extraction). Architects and researchers work at Information → Knowledge (pattern recognition, abstraction, causal modelling). Values alignment and strategic alignment agents work at Knowledge → Wisdom (purpose calibration, long-horizon consequence modelling). A system that only has agents at one layer will fail at the transformations it does not cover.

### Connection to intent alignment

The values alignment and strategic alignment agents are the explicit K→W gatekeepers. Their role is not to block but to ensure that the collective K (what we know how to build) is aligned with W (what we genuinely should build). This is the organisational equivalent of the formal intent specification problem (`2026-03-10-formal-spec-intent-alignment-agentic-coding.md`): the adversarial agents provide the informal institution (North) mechanism that formal specification cannot supply.

**Prior research in this corpus:**
- `2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal K→W specification; adversarial agents provide the informal complement
- `2026-03-10-dikw-transformation-functions.md` — transformation functions; different agent types cover different transformations
- `2026-03-10-nature-of-the-firm-coase-organisations.md` — why each agent type exists as an internal function (transaction cost logic)
- `2026-03-08-bbc-five-case-model.md` — the BBC Five Case Model as a formalised adversarial-perspectives framework
- `2026-03-08-ai-coding-harnesses-agent-philosophy.md` — multi-agent coordination patterns in AI systems

## Approach

1. **Survey adversarial collaboration in research.** Kahneman's concept of adversarial collaboration (two researchers with opposing views running a joint study) is the most formal academic treatment. Extract its core conditions: shared goal, different priors, agreed methodology for resolving disagreement.

2. **Map real-world institutional implementations.** How do design review boards, Security Review Committees, Change Advisory Boards (CAB), Investment Committees, and Architecture Review Boards instantiate the pattern? What makes them productive vs. bureaucratic? Look for the conditions (quorum rules, veto rights, escalation paths) that distinguish good from bad implementations.

3. **Characterise each agent type.** For each of the 15 agent types above: what is the core concern, the canonical question it asks, the artefact it produces, and the time horizon it operates at? This produces a reference taxonomy.

4. **Map agent types to DIKW layers.** Which agents are primarily Data→Information agents (instrumenting, observing, measuring)? Which are Information→Knowledge (synthesising, abstracting, pattern-matching)? Which are Knowledge→Wisdom (purpose-calibrating, values-checking, consequence-modelling)?

5. **Design the interaction protocol.** What is the minimal protocol for productive adversarial collaboration? How are disagreements surfaced, scoped, and resolved? What is the role of the shared goal in preventing deadlock? Reference the BBC Five Case Model as a working example.

6. **Apply to AI multi-agent systems.** How would you implement this as a set of LLM agents with different system prompt personas? What are the practical constraints (context sharing, output format, aggregation)? What evidence exists from published multi-agent AI research on role-differentiated agents?

7. **Synthesise.** Produce a design pattern: agent taxonomy + interaction protocol + resolution mechanism + conditions for productive vs. blocking disagreement.

## Sources

- [ ] **Kahneman, D. & Klein, G. (2009).** "Conditions for intuitive expertise: a failure to disagree." *American Psychologist*, 64(6), 515–526. — adversarial collaboration methodology; when expert disagreement is productive
- [ ] **Reason, J. (1990).** *Human Error.* Cambridge University Press. — Swiss cheese model; how multiple independent defensive layers (each covering different failure modes) outperform single-layer defence — the safety-engineering analogue of adversarial agents
- [ ] **UK HM Treasury (2018).** *The Green Book: Central Government Guidance on Appraisal and Evaluation.* — the BBC Five Case Model as a formal multi-perspective review framework
- [ ] `Research/completed/2026-03-08-bbc-five-case-model.md` — completed research on the BBC Five Case Model
- [ ] **Park, J.S. et al. (2023).** "Generative Agents: Interactive Simulacra of Human Behavior." UIST 2023. — role-differentiated AI agents with persistent identity and coordination
- [ ] **Wang, L. et al. (2024).** "A Survey on Large Language Model based Autonomous Agents." *Frontiers of Computer Science*. — multi-agent architectures and role differentiation
- [ ] **Liang, T. et al. (2023).** "Encouraging Divergent Thinking in Large Language Models through Debate." — AI agents with deliberately different views producing better outputs
- [ ] `Research/backlog/2026-03-10-nature-of-the-firm-coase-organisations.md` — transaction cost logic for why each agent type exists inside the boundary
- [ ] `Research/backlog/2026-03-10-dikw-transformation-functions.md` — each agent type as a specialist at one or more DIKW transformations
- [ ] `Research/completed/2026-03-10-formal-spec-intent-alignment-agentic-coding.md` — formal specification as the K layer; adversarial agents supply the informal W layer

---

## Research Skill Output

*(Full output from running the research skill — retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Restate the research question. Confirm scope, constraints, and output format.

-

### §1 Question Decomposition

Approach sub-questions broken into atomic questions — each answerable with a single evidence-based claim.

-

### §2 Investigation

Evidence gathered per atomic question. Label each claim: **[fact]**, **[inference]**, or **[assumption]** with source.

-

### §3 Reasoning

Facts, inferences, and assumptions explicitly separated. No unsupported generalisations or narrative leaps.

-

### §4 Consistency Check

Internal contradictions identified and resolved (or explicitly flagged where unresolvable).

-

### §5 Depth and Breadth Expansion

Findings re-examined through relevant lenses (technical, regulatory, economic, historical, behavioural).

-

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

**Key findings:**

**Evidence map:**

**Assumptions:**

**Analysis:**

**Risks, gaps, uncertainties:**

**Open questions:**

### §7 Recursive Review

Final pass: every section justified, all threads synthesised, every claim sourced or labelled, all uncertainties explicit.

-

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

3–5 sentences. What is the answer to the research question? State the key conclusion directly.

### Key Findings

Ordered list. Each finding is a specific, evidence-backed claim.

1.
2.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| | | high / medium / low | |

### Assumptions

Explicit assumptions made during the investigation and the justification for each.

- **Assumption:** ... **Justification:** ...

### Analysis

How the evidence was weighed, what trade-offs were identified, and how competing interpretations were resolved.

### Risks, Gaps, and Uncertainties

What is still unknown? Where does the evidence fall short? What could change the conclusion?

-

### Open Questions

Questions that surfaced during research but are out of scope for this item. Each may become a new backlog item.

-

---

## Output

*(Fill in when completing — what was produced as a result of this research?)*

- Type: knowledge
- Description:
- Links:
