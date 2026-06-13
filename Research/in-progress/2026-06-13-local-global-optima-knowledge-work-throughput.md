---
review_count: 2
title: "How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput, and which interdependencies determine when local gains become global losses?"
added: 2026-06-13T13:03:37+00:00
status: reviewing
priority: high
blocks: []
themes: [organisational-design, tools-infrastructure, cost-performance, software-engineering, enterprise-adoption]
started: 2026-06-13T19:09:40+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-04-01-backpressure-theory-of-constraints
  - 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate
  - 2026-05-16-do-mode-demand-persistence-and-build-mode-displacement
  - 2026-05-20-banking-agent-sprawl-governance-and-resilience
related:
  - 2026-06-13-local-tooling-fragmentation-threshold-measurement
  - 2026-06-13-shadow-it-custom-tooling-governance-transition
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-06-13-standardization-customization-balance-context-ai
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput, and which interdependencies determine when local gains become global losses?

## Research Question

How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput, and which interdependencies determine when local gains become global losses?

## Scope

**In scope:**
- Application of the Theory of Constraints (TOC) to knowledge work, software delivery, operational review queues, and cross-team handoffs.
- Evidence on how audits, approvals, shared services, and coordination interfaces amplify the downside of individually efficient local tools.
- Interventions such as shared platforms, shared standards, and release-governance patterns that mitigate whole-system degradation.

**Out of scope:**
- Manufacturing-only case studies unless they are explicitly used to translate TOC concepts into knowledge-work settings.
- Advice about personal productivity tools that does not consider organisational interdependence.
- General process-improvement frameworks that do not address local versus global optimisation directly.

**Constraints:** Emphasise knowledge work and software-intensive organisations, and prefer sources that connect throughput, queueing, and organisational interdependence rather than isolated productivity anecdotes.

## Context

This item informs whether apparently successful local tooling should be judged by local efficiency alone or by its effect on end-to-end throughput once shared dependencies, review queues, and coordination costs are included.

## Approach

1. Translate TOC concepts such as the constraint, subordination, and bottleneck migration into knowledge-work tooling contexts.
2. Identify evidence that summing local tooling gains can reduce global performance once teams share data, approvals, or operational dependencies.
3. Examine which kinds of interdependence most strongly amplify the downside of fragmented local optimisation.
4. Identify platform or governance interventions that restore whole-system throughput without eliminating all local autonomy.

## Sources

- [x] [Forte Labs (2019) Theory of Constraints 102: Local Optima](https://fortelabs.com/blog/theory-of-constraints-102-local-optima/) - practitioner explanation of local versus global optimisation in knowledge work.
- [x] [Forte Labs (2019) Theory of Constraints 101: Applying the Principles of Flow to Knowledge Work](https://fortelabs.com/blog/theory-of-constraints-101/) - foundational TOC principles applied to knowledge-work settings.
- [x] [Forte Labs (2019) Theory of Constraints 103: The Four Fundamental Principles of Flow](https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/) - flow principles including Work in Progress (WIP) limits and constraint exploitation.
- [x] [Wikipedia: Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) - overview of TOC five focusing steps, throughput accounting, and Drum-Buffer-Rope (DBR).
- [x] [DORA (2025) State of AI-assisted Software Development - dora.dev summary](https://dora.dev/research/2025/dora-report/) - official summary: AI acts as amplifier of existing org conditions, not universal productivity booster.
- [x] [InfoQ (2026) AI Is Amplifying Software Engineering Performance, Says the 2025 DORA Report](https://www.infoq.com/news/2026/03/ai-dora-report/) - detailed analysis of DORA 2025 findings on fragmented tooling, platform maturity, and system-level throughput.
- [x] [Faros AI (2025/2026) Key Takeaways from the DORA Report 2025 and AI Engineering Report 2026](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025) - telemetry-backed analysis: "Acceleration Whiplash" showing individual gains with system-level quality deterioration.
- [x] [DORA Capabilities: Loosely Coupled Teams](https://dora.dev/capabilities/loosely-coupled-teams/) - DORA capability definition linking architectural decoupling to high software delivery performance.
- [x] [Mitchell (2026) Backpressure Infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html) - prior repository synthesis on backpressure and the Theory of Constraints.
- [x] [Mitchell (2026) How large can the Information Technology (IT) throughput constraint become before debt accumulation becomes discontinuous?](https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html) - prior repository work on throughput constraints and debt accumulation.
- [x] [Mitchell (2026) Why does do-mode demand keep displacing build-mode work in Information Technology (IT), and what operating model changes stop that displacement?](https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html) - prior repository work on queue displacement and capacity trade-offs.
- [x] [Mitchell (2026) How should banks govern department-level agent sprawl and bottleneck shifts across divisions?](https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html) - domain case linking local automation to shifted organisational bottlenecks across shared review queues.

## Related

- [Backpressure Infrastructure and the Theory of Constraints](https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html)
- [How large can the Information Technology (IT) throughput constraint become before debt accumulation becomes discontinuous?](https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html)
- [Why does do-mode demand keep displacing build-mode work in Information Technology (IT), and what operating model changes stop that displacement?](https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

Question: How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput, and which interdependencies determine when local gains become global losses?

Scope: Application of the Theory of Constraints (TOC) to knowledge work, software delivery, operational review queues, and cross-team handoffs. Evidence on how audits, approvals, shared services, and coordination interfaces amplify the downside of individually efficient local tools. Interventions such as shared platforms, standards, and release-governance patterns that mitigate whole-system degradation.

Out of scope: Manufacturing-only case studies unless explicitly used to translate TOC concepts to knowledge-work settings. Personal productivity advice that ignores organisational interdependence. General process-improvement frameworks that do not address local versus global optimisation directly.

Constraints: Emphasise knowledge work and software-intensive organisations; prefer sources connecting throughput, queueing, and organisational interdependence rather than isolated productivity anecdotes.

Output format: Research Skill Output §§0–7 followed by structured Findings.

Working hypotheses:
[assumption; source: https://fortelabs.com/blog/theory-of-constraints-101/; https://en.wikipedia.org/wiki/Theory_of_constraints] Local optimisation of non-constraint resources in a knowledge-work pipeline does not improve global throughput and typically degrades it by flooding the constraint with more Work in Progress (WIP) than it can process.
[assumption; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/] The degree of harm from local tooling gains is proportional to the density of shared dependencies: approval queues, shared services, data handoffs, and integration points where individual acceleration concentrates demand.

### §1 Question Decomposition

Decomposition tree derived from the Approach sub-questions:

**A. TOC mechanics in knowledge-work settings**
A1. What does TOC assert about throughput, constraints, and the effect of improving non-constraint resources?
A2. How does the "stay busy" norm translate local efficiency into queue flooding at the constraint?
A3. How does subordination (step 3 of the TOC five focusing steps) differ from local optimisation?

**B. Empirical evidence for local-to-global throughput loss**
B1. Does Artificial Intelligence (AI)-assisted coding provide a controlled test of local tooling gain without system-wide adaptation?
B2. What does the DevOps Research and Assessment (DORA) 2025 survey say about whether individual productivity gains translate to organisation-level delivery?
B3. What does telemetry from Faros AI across 10,000–22,000 developers show about the gap between individual and organisational metrics?

**C. Which interdependencies most amplify the downside**
C1. What shared dependencies convert an upstream speed increase into a downstream queue?
C2. How does architectural coupling (tightly-coupled versus loosely-coupled systems) modulate the harm from local tooling?
C3. What role do approval queues, code review gates, change advisory boards, and shared test environments play as bottleneck surfaces?

**D. Interventions that restore whole-system throughput**
D1. What does platform engineering do to convert local gains into global gains?
D2. What architectural patterns (loosely-coupled teams, WIP limits, small batches) limit harm from local speed?
D3. What governance and standards patterns reduce coordination overhead without eliminating local autonomy?

### §2 Investigation

**A1. TOC assertion about throughput and non-constraint improvement**

[inference] The Theory of Constraints (TOC), introduced by Eliyahu M. Goldratt in his 1984 book "The Goal", holds that any system's throughput is limited by at most a small number of constraints, and that only increasing flow through the constraint increases overall throughput. Source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/

[inference] TOC defines five focusing steps: (1) identify the system's constraint, (2) exploit the constraint, (3) subordinate everything else to the above decision, (4) elevate the constraint, (5) if the constraint is broken, go back to step 1. Source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/

[inference] TOC holds that improving a non-constraint resource does not improve total throughput; it only increases the Work in Progress (WIP) queue in front of the constraint. Source: https://fortelabs.com/blog/theory-of-constraints-101/

[inference] In knowledge work, the constraint is often not visible as a physical bottleneck but manifests as a shared approval queue, a specialised reviewer, an integration gate, or a shared services team. Source: https://fortelabs.com/blog/theory-of-constraints-101/; https://en.wikipedia.org/wiki/Theory_of_constraints

**A2. How "stay busy" norms flood the constraint**

[fact] Forte Labs' practitioner analysis of TOC in knowledge work describes a pipe model where departments feed work downstream. When the constraint fills, non-constraint upstream and downstream departments continue starting new work because they cannot tolerate being "underutilised," which continuously sends more demand to the constraint. Source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/

[inference] The result is a reinforcing loop: more WIP in front of the constraint reduces the constraint's effective capacity (via context switching, email, coordination overhead), which further slows output, which causes more upstream departments to start new work to avoid appearing idle, which generates more WIP. Source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/

[fact] Forte Labs identifies that downstream departments waiting on the constraint also start new work, generating additional coordination requests ("decisions requiring input from Engineering") that further reduce the constraint's productive capacity. Source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/

[inference] Ford's original flow principles, described in the Forte Labs TOC 103 article, identify four principles: optimise flow (not local utilisation), establish mechanisms for when not to produce, abolish local optima, and use a focusing process. The anti-pattern of maximising local utilisation explicitly violates principles 2 and 3. Source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/

**A3. Subordination versus local optimisation**

[inference] TOC's step 3 (subordinate everything else to the constraint decision) directly opposes local optimisation: non-constraint resources are explicitly instructed to slow down or idle to avoid overloading the constraint. This is structurally incompatible with "stay busy" management norms. Source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/

[inference] In software delivery, subordination means upstream teams (such as product, design, or feature delivery) limiting their WIP to match what a shared review, deployment, or compliance gate can absorb, rather than maximising their own delivery cadence. Source: https://fortelabs.com/blog/theory-of-constraints-101/; https://dora.dev/capabilities/loosely-coupled-teams/

**B1. AI-assisted coding as a controlled test of local tooling gain**

[fact] The DORA 2025 State of AI-assisted Software Development report, based on nearly 5,000 technology professionals and more than 100 hours of qualitative interviews, concludes that AI acts primarily as an amplifier of existing organisational conditions rather than a universal productivity booster. Source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/

[fact] The DORA 2025 report finds that high-performing teams with mature DevOps practices, well-defined workflows, and strong platform capabilities convert AI-driven gains into measurable improvements in delivery performance, while teams with fragmented tooling and unclear processes can experience the opposite. Source: https://www.infoq.com/news/2026/03/ai-dora-report/

[inference] AI-assisted coding is a natural experiment in local tooling optimisation: it raises individual developer speed (a local gain) without automatically changing the downstream review, integration, and deployment infrastructure through which that output must flow. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/

**B2. DORA 2025 on individual gains versus organisation-level delivery**

[fact] The DORA 2025 report identifies seven capabilities required for AI gains to translate to organisational performance: clear AI stance, healthy data ecosystems, AI-accessible internal knowledge, strong version control, working in small batches, user-centric focus, and quality internal platforms. Source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] The requirement for all seven capabilities implies that the absence of any single capability, particularly platform quality or small-batch discipline, can prevent individual productivity gains from improving system-level outcomes. Source: https://www.infoq.com/news/2026/03/ai-dora-report/

[fact] The DORA 2025 report states that organisations with fragmented tooling, unclear processes, or inconsistent development practices may see AI accelerate technical debt creation, increase code review complexity, and introduce instability into already fragile systems. Source: https://www.infoq.com/news/2026/03/ai-dora-report/

**B3. Faros AI telemetry on the individual-to-organisational gap**

[fact] Faros AI telemetry across 10,000+ developers in 2025 found AI coding assistants produced 21% more tasks completed and 98% more pull requests (PRs) merged per developer, but organisational delivery metrics remained flat. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[fact] Faros AI telemetry updated to 22,000+ developers in 2026 found: tasks completed per developer +33.7%, epics per developer +66.2%, but median time in PR review +441%, bugs per developer +54%, and incidents per PR +242.7%. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] Faros AI names this pattern "Acceleration Whiplash": individual throughput rises, but the shared infrastructure through which work flows, specifically code review, quality assurance, and production stabilisation, absorbs and amplifies the volume increase as queue depth, defect rate, and incident frequency. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[fact] Faros AI 2026 telemetry found developers using AI interact with 67.4% more PR contexts and 17.7% more task contexts daily, with 26% more in-progress tasks showing no PR or activity for seven or more days (stalled WIP). Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

**C1. Which shared dependencies convert upstream speed into downstream queues**

[inference] The pattern from Faros telemetry and DORA 2025 follows TOC mechanics: PR review queues, bug triage, and production incident response are the shared constraint surfaces. When developers submit work faster, review queues lengthen, review quality drops (31% more PRs merging with no review), and production instability follows. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/

[inference] The prior completed repository item on banking agent sprawl documents the same pattern in regulated environments: local department automation raises technical throughput, but validation, exception handling, compliance review, and incident response remain constrained at the shared queue level. Source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html

[inference] The prior completed repository item on do-mode demand and build-mode displacement shows that when workaround automation demand is met locally (by teams building their own tools), the shared delivery pipeline is not relieved; instead, each local automation adds ongoing operational cost and fragments the queue of work competing for shared governance attention. Source: https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html

[inference] The prior completed repository item on IT throughput constraints shows that central delivery throughput functions as the dominant rate-limiter for organisational capability: when local tools fill the gap left by insufficient central delivery, they generate shadow IT demand that further fragments governance and approval queues rather than reducing them. Source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html

**C2. Architectural coupling as an amplifier of local-optimisation harm**

[fact] DORA's loosely-coupled-teams capability page states that when system architecture enables teams to test, deploy, and change systems without dependencies on other teams, teams require little communication to get work done and both architecture and teams are loosely coupled. Source: https://dora.dev/capabilities/loosely-coupled-teams/

[fact] DORA's loosely-coupled-teams page states that with a tightly coupled architecture, small changes can result in large-scale cascading failures, requiring anyone working in one part of the system to constantly coordinate with anyone else working in another part. Source: https://dora.dev/capabilities/loosely-coupled-teams/

[inference] Tightly-coupled systems convert local speed gains into coordination overhead: a team that delivers faster must still negotiate integration, cascading test dependencies, and change management with adjacent teams, which creates queue pressure at shared integration and approval points. Source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/

[fact] Team Topologies' key-concepts page identifies "eliminating team dependencies" as the primary lever for flow: organisations obsess over making individual teams more efficient while ignoring the massive delays between teams, and hiring more people can decrease throughput when teams are still waiting for each other. Source: https://teamtopologies.com/key-concepts

**C3. Approval queues, code review gates, and shared test environments as bottleneck surfaces**

[inference] PR review time increasing 441% in Faros's 2026 dataset, while PR volume continues rising, demonstrates the structure of a TOC queue overflow: the review resource was not expanded when the upstream delivery rate increased, so the queue depth grew and review quality degraded. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] Change Advisory Boards (CABs), shared compliance review panels, and shared testing environments function as the same structural constraint: local teams improve delivery velocity but the constraint capacity (number of reviewers, test environment slots, compliance analyst hours) does not increase, so the bottleneck shifts visibly to the shared gate. Source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://dora.dev/capabilities/loosely-coupled-teams/

**D1. What platform engineering does to convert local gains into global gains**

[inference] DORA 2025 found 90% of surveyed organisations now have platform engineering capabilities, with a direct correlation between platform quality and AI's amplification of organisational performance. Source: https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] Platform engineering converts local gains into global gains by providing a shared, standardised substrate that includes integrated test pipelines, deployment automation, and monitoring, so that the increased volume of work produced by locally-faster teams flows through a common gate with known, governed capacity rather than accumulating in ad hoc queues. Source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] Without this platform foundation, AI adoption creates new forms of complexity: developers generate larger PRs, introduce inconsistent coding patterns, or rely on AI suggestions that do not align with established architectural standards, all of which slow delivery and increase operational risk at shared review points. Source: https://www.infoq.com/news/2026/03/ai-dora-report/

**D2. Architectural and batch-size patterns that limit harm**

[fact] DORA's loosely-coupled-teams capability states that teams able to make large-scale design changes without permission from outside the team or depending on other teams are a key predictor of high software delivery performance. Source: https://dora.dev/capabilities/loosely-coupled-teams/

[inference] Working in small batches limits the queue-flooding effect of local tooling gains: smaller changes clear review gates faster, produce less review overload, and generate smaller blast radius on production incidents, so the constraint (review or deployment gate) stays closer to being subordinated to the delivery pipeline rather than becoming an unmanaged queue. Source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] The WIP-limiting principle from TOC and flow theory, described in the Forte Labs TOC 103 article, states that unchecked WIP is one of the greatest enemies of flow. Limiting WIP enforces subordination of non-constraint resources to the constraint's capacity, which is the structural opposite of maximising individual utilisation. Source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/

**D3. Governance and standards patterns**

[inference] The prior completed repository item on the TOC and backpressure shows that Drum-Buffer-Rope (DBR) scheduling enforces throughput discipline by tying upstream release rates to the drumbeat of the constraint; analogous mechanisms in software delivery include WIP limits on kanban boards, PR size limits, and deployment frequency controls. Source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html

[inference] Shared platform standards reduce the coordination cost that accumulates when each team runs its own tools, security posture, and integration pattern: each non-standard surface generates incremental coordination demand at every handoff, shared review, and incident response event. Source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://dora.dev/capabilities/loosely-coupled-teams/

[inference] The backpressure-TOC prior item identifies buffer management as the mechanism that absorbs variability in front of the constraint, preventing starvation downstream while limiting queue overflow. The equivalent in knowledge work is an explicit review-capacity management process that treats the shared review queue as a managed service with known capacity, rather than an elastic resource. Source: https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html

### §3 Reasoning

Causal chain (each item bears its own label and source):

1. In a knowledge-work pipeline with shared dependencies, total throughput is bounded by the shared constraint's capacity, not by the sum of individual resource capacities. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/]

2. Local tooling optimisation raises the output rate of non-constraint resources, increasing the rate at which work arrives at the constraint. [inference; source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/]

3. Because the constraint's capacity is not raised, the queue in front of it grows, increasing cycle time and reducing effective constraint throughput via context switching and coordination overhead. [inference; source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

4. The Faros AI 2025 and 2026 telemetry data provides empirical confirmation: individual developer output rose (21–34% more tasks, 98% more PRs), but PR review time rose 441% and production incidents per PR rose 242.7%, matching the predicted queue-overflow pattern. [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

5. The severity of harm scales with the density of shared dependencies: tightly-coupled architectures, shared approval queues, and shared test environments amplify the downside, while loosely-coupled architectures, small batches, and WIP limits reduce it. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

6. Interventions that restore whole-system throughput operate by either (a) raising constraint capacity (platform engineering, review automation, shared infrastructure), (b) reducing WIP entering the constraint (small-batch discipline, WIP limits, architectural decoupling), or (c) both. [inference; source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://dora.dev/capabilities/loosely-coupled-teams/]

Narrative glue removed: claims of necessity, universality, and hedged attribution from §2 have been reduced to the above causal chain with explicit labels.

Unsupported generalisation check: The claim that "everyone is always hurt by local optimisation" is not supported; the evidence shows harm scales with coupling density and is mitigated by architectural and WIP controls.

### §4 Consistency Check

```text
contradiction_scan: resolved
  - No internal contradiction found between TOC mechanics (A1-A3) and empirical data (B1-B3).
  - DORA 2025 reports AI as amplifier of existing conditions, consistent with TOC
    subordination logic: strong foundations (loose coupling, platform) act as
    pre-existing constraint-management; weak foundations (fragmented tooling) mean
    the constraint is already overwhelmed before AI further floods it.
  - Faros 2026 finding that even high-maturity organisations experience
    Acceleration Whiplash is consistent with the claim that without WIP limits
    and batch-size controls, any upstream speed increase eventually floods review.
  - No reversal between §2 and §3.
confidence_adjustment:
  - Claims backed only by practitioner synthesis (Forte Labs) without peer-reviewed
    corroboration are kept at [inference] rather than [fact].
  - Empirical claims from Faros telemetry are marked [fact] because they report
    observed metrics from a defined developer population.
scope_guardrail: maintained
  - Manufacturing-only case studies were not used.
  - Personal productivity advice without organisational interdependence framing
    was not used.
```

### §5 Depth and Breadth Expansion

**Technical lens**

[inference] WIP limits are the primary technical mechanism translating TOC subordination into software delivery: by capping the number of items in a pipeline stage, they prevent upstream speed from overloading downstream gates. This is the core design principle of kanban columns, PR size limits, and deployment throttles. Source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://dora.dev/capabilities/loosely-coupled-teams/

[inference] Architectural decoupling (microservices, well-defined interfaces, independent deployment) reduces the coupling density that converts local speed into coordination overhead. Organisations that invest in decoupling before scaling AI tooling are structurally positioned to absorb local gains without queue overflow. Source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/

**Economic lens**

[inference] The Faros Acceleration Whiplash data implies a negative return on local tooling investment beyond a certain coupling-density threshold: each additional unit of individual throughput increase generates more than one unit of review, defect, and incident cost when shared review capacity is not expanded commensurately. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

[inference] The prior completed repository item on Information Technology (IT) throughput constraints shows that shadow IT accumulation has the same economic structure: each local workaround reduces the friction on one team while adding governance and maintenance cost to the shared constraint, making the global cost of local efficiency greater than the local saving. Source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html

**Behavioural lens**

[inference] The "stay busy" norm identified by Forte Labs is a behavioural amplifier: managers and employees who equate individual utilisation with value creation will resist the TOC prescription to idle non-constraint resources, making the cultural change required for subordination harder than the technical change. Source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/

[inference] DORA 2025 reports no correlation between AI adoption and increased burnout or friction (survey data), even as Faros telemetry simultaneously documents rising stalled WIP, restart rates, and parallel task contexts. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/research/2025/dora-report/

[inference] The gap between survey sentiment and telemetry outcomes suggests that developers do not experience the constraint-queue overflow as personal overload in the short term; instead, system-level degradation (incidents, defects, PR review latency) accumulates in shared infrastructure without registering as individual burnout until the cascade is severe. Source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

**Regulatory lens**

[inference] In regulated environments (banking, healthcare, critical infrastructure), shared approval queues include compliance and model-risk review panels that cannot be auto-approved or removed; local tooling gains in those industries are more likely to create visible compliance bottlenecks because the constraint is legally protected from being eliminated rather than just being under-resourced. Source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html

**Historical lens**

[inference] The TOC observation that local optima systematically reduce global performance pre-dates AI tooling by four decades; Goldratt formalised it in 1984. The Faros and DORA 2025 data provide a new, large-scale empirical test of the same principle in a context (AI-assisted coding) where the local gain is abrupt and the shared constraint (PR review) is structurally unscaled. Source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025

### §6 Synthesis

**Executive summary:**

In knowledge-work pipelines with shared dependencies, local tooling optimisation reliably degrades whole-system throughput when the shared constraint's capacity is not increased commensurately, a mechanism that TOC has described since 1984 and that DORA 2025 and Faros AI 2026 telemetry now confirm at scale in AI-assisted software delivery. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI telemetry across 22,000 developers in 2026 documents the failure mode directly: individual task completion rose 33.7%, but PR review time rose 441% and production incidents per PR rose 242.7%, confirming that individual acceleration floods shared review infrastructure when review capacity is not scaled. [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The interdependencies that most amplify the gap between local and global outcomes are shared approval and review queues, tightly-coupled architectures that force coordination at every change, and change-management gates that cannot be bypassed without regulatory or architectural redesign. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Interventions that restore whole-system throughput operate on two levers simultaneously: raising shared constraint capacity (platform engineering, review automation, architectural decoupling) and limiting the rate at which local speed floods that constraint (WIP limits, small-batch discipline, PR size controls). [inference; source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://dora.dev/capabilities/loosely-coupled-teams/]

**Key findings:**

1. Local tooling optimisation in a knowledge-work pipeline does not improve total throughput unless the shared constraint's capacity is increased, because throughput is bounded by the constraint, not by the sum of individual resource outputs, as TOC established in 1984. ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/)

2. Faros AI telemetry across 22,000 developers in 2026 measured individual task completion up 33.7% and epics completed up 66.2%, while PR review time rose 441%, bugs per developer rose 54%, and production incidents per PR rose 242.7%, providing large-scale empirical confirmation of queue overflow caused by local tooling gains. ([fact]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

3. The DORA 2025 report, based on nearly 5,000 technology professionals, found that AI acts as an amplifier of existing organisational conditions rather than a universal productivity booster: teams with mature platform engineering and loose coupling convert AI gains into system-level improvement, while teams with fragmented tooling experience increased instability. ([fact]; medium confidence; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/)

4. Shared approval and review queues are the primary interdependency surface that converts local speed gains into global throughput losses, because they represent a constraint whose capacity is fixed by personnel, policy, or regulatory mandate rather than by technical infrastructure alone. ([inference]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/capabilities/loosely-coupled-teams/)

5. Tightly-coupled architectures amplify local-to-global throughput losses by forcing coordination at every dependency boundary: a speed increase in one team generates cascading coordination demand from adjacent teams, compressing the constraint's capacity for productive work. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/)

6. Platform engineering is the single most evidence-backed intervention for converting local gains into global gains, by providing shared, standardised infrastructure through which increased local output can flow without accumulating in ad hoc queues; DORA 2025 found 90% of organisations now have platform engineering capabilities but quality varies. ([inference]; medium confidence; source: https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/)

7. WIP limits and small-batch discipline are the structural mechanism by which non-constraint resources are subordinated to the constraint, preventing the queue-flooding dynamic; DORA 2025 identifies working in small batches as one of seven capabilities required for AI gains to translate to organisational performance. ([inference]; medium confidence; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

8. In regulated environments such as banking, local department automation that raises technical throughput predictably shifts the visible bottleneck to compliance, validation, and incident-response queues that cannot be removed without regulatory redesign, making the local-to-global throughput loss more durable than in unregulated contexts. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html; https://dora.dev/capabilities/loosely-coupled-teams/)

9. The "stay busy" norm identified by Forte Labs acts as a cultural amplifier of the local-optima failure mode: when managers equate individual utilisation with value creation, they structurally resist the TOC subordination prescription that non-constraint resources should idle rather than flood the constraint with new WIP. ([inference]; medium confidence; source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/)

10. Shadow IT and local workaround automation exhibit the same structural failure as local tooling optimisation in software delivery: each local workaround reduces friction for one team while adding governance, maintenance, and approval cost to shared constraint surfaces, producing a global cost exceeding the local saving. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] TOC bounds throughput at the constraint; non-constraint improvements do not raise total throughput | https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/ | medium | Established theory (1984); cited sources are tertiary (Wikipedia) and secondary-practitioner (Forte Labs); no peer-reviewed primary citation |
| [fact] Faros 2026: individual tasks +33.7%, PR review time +441%, bugs +54%, incidents/PR +242.7% | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Telemetry from 22,000 developers; single commercial vendor source; direction consistent with DORA survey |
| [fact] DORA 2025: AI amplifies existing conditions; fragmented tooling leads to increased instability | https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/ | high | Based on nearly 5,000 respondents; consistent with prior DORA findings |
| [inference] Shared approval queues are the primary interdependency surface for local-to-global loss | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Inferred from queue-overflow data; no direct experiment isolating approval-queue capacity |
| [inference] Tight architectural coupling amplifies the loss | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | DORA finds strong correlation between coupling and delivery performance; direction consistent with TOC |
| [inference] Platform engineering converts local gains into global gains | https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | DORA 2025 identifies platform quality as required capability; causal direction inferred |
| [inference] WIP limits and small-batch discipline subordinate non-constraint resources | https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | TOC prescription plus DORA empirical finding; not a controlled experiment |
| [inference] Regulated-environment bottleneck migration to compliance queues | https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html | medium | Prior repository item; mechanism consistent with TOC but no direct cross-sector empirical study |
| [inference] "Stay busy" norm is cultural amplifier of local-optima failure | https://fortelabs.com/blog/theory-of-constraints-102-local-optima/ | medium | Practitioner synthesis; no independent peer-reviewed study of this specific norm |
| [inference] Shadow IT exhibits same structural failure as local tooling optimisation | https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html | medium | Prior repository synthesis; consistent with DORA and TOC findings |

**Assumptions:**

- [assumption; source: https://fortelabs.com/blog/theory-of-constraints-101/; https://en.wikipedia.org/wiki/Theory_of_constraints] Knowledge-work pipelines with shared downstream dependencies follow the same constraint-throughput logic as manufacturing pipelines in TOC, because both involve discrete work items flowing through sequential stages with a rate-limiting shared resource. Justification: TOC has been applied to software delivery, project management, and healthcare in peer-reviewed literature cited in the prior backpressure-TOC repository item; the Forte Labs series explicitly extends the analysis to knowledge work.

- [assumption; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI's developer telemetry represents a sufficient cross-section of knowledge-work organisations to support a directional inference about the local-to-global gap, even though the population is not random and over-represents GitHub-hosted engineering teams. Justification: Faros reports the population size (22,000 developers, 4,000+ teams) and methodology, and the direction of the finding is consistent with DORA survey data and TOC theory.

- [assumption; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/] AI-assisted coding is a valid proxy for local tooling optimisation in the knowledge-work sense: it raises an individual contributor's delivery rate without automatically raising the capacity of shared downstream stages. Justification: DORA 2025 and Faros both use AI adoption as the test case and find the amplifier pattern consistent with this assumption.

**Analysis:**

The evidence converges on a single structural pattern: local tooling gains become global losses at the shared constraint. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

TOC provides the theoretical frame: throughput is bounded by the constraint, so non-constraint gains cannot raise global throughput; they can only accumulate as WIP in front of the constraint, reducing its effective capacity via coordination overhead. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/]

The Faros telemetry provides the most direct empirical test in this body of evidence, comparing individual output against shared-infrastructure outcomes simultaneously. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] A simultaneous measurement of individual output (rising) and shared-infrastructure outcomes (PR review time, bugs, incidents) shows the queue-overflow signature. The 441% increase in PR review time against a 33.7% increase in task completion is inconsistent with a scenario where local gains are translating into global gains; instead, the shared review gate is absorbing the throughput increase as queue depth rather than producing faster delivery. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

DORA 2025 contextualises this: the seven capabilities required for AI gains to translate to organisational performance are all concerned with reducing the coupling density that amplifies the gap. [inference; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/] Platform quality reduces queue accumulation. [inference; source: https://www.infoq.com/news/2026/03/ai-dora-report/] Small-batch discipline limits WIP at the constraint. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Loose coupling reduces coordination-overhead tax on the constraint's capacity. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/] Organisations with these capabilities in place experience AI as an amplifier of existing strengths; organisations without them experience AI as an amplifier of existing fragmentation. [inference; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

The interdependencies that most amplify the failure are: (1) shared approval and review queues with fixed or slowly-scalable human capacity, (2) tightly-coupled architectures that convert every local change into a coordination demand on adjacent teams, and (3) change-management gates (Change Advisory Boards, compliance panels) whose throughput is governed by policy or regulation rather than resource investment. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html]

The dominant rival explanation is that the Faros data reflects a transition period: quality and stability will improve once organisations adapt their review processes to the new throughput level. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] This is consistent with TOC step 4 (elevate the constraint), but requires active intervention, not passive adaptation. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints] The DORA 2025 finding that even organisations with strong engineering foundations see downstream quality pressure from AI adoption (per Faros 2026) suggests that passive adaptation is insufficient, and that explicit constraint-elevation investment is required regardless of baseline maturity. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

**Risks, gaps, uncertainties:**

- No peer-reviewed controlled experiment directly tests the local-tooling-to-global-loss hypothesis in knowledge work with a randomised design. The evidence is correlational (Faros telemetry, DORA survey) and theoretical (TOC). The direction is consistent across multiple independent sources, which supports the medium-confidence assignment.
- The Faros developer population over-represents GitHub-hosted engineering teams and may not generalise to non-software knowledge work (legal, financial analysis, strategic planning). No equivalent telemetry study for those knowledge-work types was found in this search.
- The relative weight of the three amplifying interdependencies (approval queues, architectural coupling, change-management gates) is not directly measurable from the available evidence. The ranking is an inference from the pattern in Faros and DORA data, not from a direct comparison experiment.
- The TOC five-step model assumes a stable, identifiable constraint; in software delivery, the constraint migrates after each improvement cycle (the bottleneck shifts from coding to review, from review to deployment, from deployment to incident response). This migration is well-described in TOC step 5 but is not directly measured in the DORA or Faros data.

**Open questions:**

- What is the measurable coupling-density threshold below which local tooling gains stop reducing global throughput? This is a candidate for a new backlog item in quantitative form.
- How does the local-global throughput gap behave in non-engineering knowledge work (legal review, financial modelling, regulatory analysis) where AI tooling adoption is accelerating but shared constraint surfaces differ?
- Does architectural decoupling actually eliminate the local-global gap, or does it displace the constraint to a different shared surface (Application Programming Interface (API) governance, integration testing, data contract management)?

### §7 Recursive Review

```text
review_result: pass

acronym_audit:
  - TOC: expanded "Theory of Constraints (TOC)" at first prose use in §0
  - WIP: expanded "Work in Progress (WIP)" at first prose use in §0
  - AI: expanded "Artificial Intelligence (AI)" at first prose use in §1 B1
  - DORA: expanded "DevOps Research and Assessment (DORA)" at first prose use in §1 B2
  - PR: expanded "pull request (PR)" context checked; first use is in B3 where "pull
    requests (PRs)" is used; confirmed expanded
  - IT: expanded "Information Technology (IT)" in §5 economic lens and in prior item
    citations where it first appears in this item's prose
  - DBR: expanded "Drum-Buffer-Rope (DBR)" in §2 D3 at first use
  - CAB: expanded "Change Advisory Boards (CABs)" at first prose use in §2 C3
  - WIP: confirmed expanded first use in §0 working hypotheses

claim_audit:
  - All §2 claims carry [fact], [inference], or [assumption] labels
  - §3 causal chain items each carry own label and source
  - §6 Synthesis key findings each carry confidence and URL-backed source
  - Executive summary sentences each carry trailing inference labels

findings_parity: §6 Synthesis and ## Findings are seeded from the same content

source_audit:
  - All cited URLs are accessible public pages
  - Forte Labs URL updated from fortelabs.co to fortelabs.com (redirect resolved)
  - DORA 2025 cited via accessible summary page at dora.dev/research/2025/dora-report/
    and InfoQ analysis at infoq.com/news/2026/03/ai-dora-report/

scope_guardrail: maintained; no manufacturing-only case studies used without
  knowledge-work translation; no personal productivity advice without
  organisational interdependence framing used

confidence: medium; key findings are supported by multiple independent secondary
  sources (DORA, Faros, TOC theory) but no peer-reviewed randomised experiment
  directly tests the hypothesis in knowledge work
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

In knowledge-work pipelines with shared dependencies, local tooling optimisation reliably degrades whole-system throughput when the shared constraint's capacity is not increased commensurately, a mechanism that the Theory of Constraints (TOC) has described since 1984 and that DevOps Research and Assessment (DORA) 2025 and Faros AI 2026 telemetry now confirm at scale in AI-assisted software delivery. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Faros AI telemetry across 22,000 developers in 2026 documents the failure mode directly: individual task completion rose 33.7%, but pull request (PR) review time rose 441% and production incidents per PR rose 242.7%, confirming that individual acceleration floods shared review infrastructure when review capacity is not scaled. [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The interdependencies that most amplify the gap between local and global outcomes are shared approval and review queues, tightly-coupled architectures that force coordination at every change, and change-management gates that cannot be bypassed without regulatory or architectural redesign. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Interventions that restore whole-system throughput operate on two levers simultaneously: raising shared constraint capacity (platform engineering, review automation, architectural decoupling) and limiting the rate at which local speed floods that constraint (Work in Progress (WIP) limits, small-batch discipline, PR size controls). [inference; source: https://www.infoq.com/news/2026/03/ai-dora-report/; https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://dora.dev/capabilities/loosely-coupled-teams/]

### Key Findings

1. Local tooling optimisation in a knowledge-work pipeline does not improve total throughput unless the shared constraint's capacity is increased, because throughput is bounded by the constraint and not by the sum of individual resource outputs, as TOC established in 1984. ([inference]; medium confidence; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/)

2. Faros AI telemetry across 22,000 developers in 2026 measured individual task completion up 33.7% and epics completed up 66.2%, while PR review time rose 441%, bugs per developer rose 54%, and production incidents per PR rose 242.7%, providing large-scale empirical confirmation of queue overflow caused by local tooling gains. ([fact]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

3. The DORA 2025 report, based on nearly 5,000 technology professionals, found that Artificial Intelligence (AI) acts as an amplifier of existing organisational conditions rather than a universal productivity booster: teams with mature platform engineering and loose coupling convert AI gains into system-level improvement, while teams with fragmented tooling experience increased instability. ([fact]; medium confidence; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/)

4. Shared approval and review queues are the primary interdependency surface that converts local speed gains into global throughput losses, because they represent a constraint whose capacity is fixed by personnel, policy, or regulatory mandate rather than by technical infrastructure alone. ([inference]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/capabilities/loosely-coupled-teams/)

5. Tightly-coupled architectures amplify local-to-global throughput losses by forcing coordination at every dependency boundary: a speed increase in one team generates cascading coordination demand from adjacent teams, compressing the constraint's capacity for productive work. ([inference]; medium confidence; source: https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/)

6. Platform engineering is the single most evidence-backed intervention for converting local gains into global gains, by providing shared, standardised infrastructure through which increased local output can flow without accumulating in ad hoc queues; DORA 2025 found 90% of organisations now have platform engineering capabilities but quality varies. ([inference]; medium confidence; source: https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/)

7. WIP limits and small-batch discipline are the structural mechanism by which non-constraint resources are subordinated to the constraint, preventing the queue-flooding dynamic, and DORA 2025 identifies working in small batches as one of seven capabilities required for AI gains to translate to organisational performance. ([inference]; medium confidence; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

8. In regulated environments such as banking, local department automation that raises technical throughput predictably shifts the visible bottleneck to compliance, validation, and incident-response queues that cannot be removed without regulatory redesign, making the local-to-global throughput loss more durable than in unregulated contexts. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html; https://dora.dev/capabilities/loosely-coupled-teams/)

9. The "stay busy" norm identified by Forte Labs acts as a cultural amplifier of the local-optima failure mode: when managers equate individual utilisation with value creation, they structurally resist the TOC subordination prescription that non-constraint resources should idle rather than flood the constraint with new WIP. ([inference]; medium confidence; source: https://fortelabs.com/blog/theory-of-constraints-102-local-optima/)

10. Shadow Information Technology (IT) and local workaround automation exhibit the same structural failure as local tooling optimisation in software delivery: each local workaround reduces friction for one team while adding governance, maintenance, and approval cost to shared constraint surfaces, producing a global cost that exceeds the local saving. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] TOC bounds throughput at the constraint; non-constraint improvements do not raise total throughput | https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/ | medium | Established theory (1984); cited sources are tertiary (Wikipedia) and secondary-practitioner (Forte Labs); no peer-reviewed primary citation |
| [fact] Faros 2026: individual tasks +33.7%, PR review time +441%, bugs +54%, incidents/PR +242.7% | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | Telemetry from 22,000 developers; single commercial vendor source; direction consistent with DORA survey |
| [fact] DORA 2025: AI amplifies existing conditions; fragmented tooling leads to increased instability | https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | Primary report and secondary coverage of same study; same DORA 2025 study, not independent sources |
| [inference] Shared approval queues are the primary interdependency surface for local-to-global loss | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/capabilities/loosely-coupled-teams/ | medium | Inferred from queue-overflow data; no direct experiment isolating approval-queue capacity |
| [inference] Tight architectural coupling amplifies the loss by forcing coordination at every boundary | https://dora.dev/capabilities/loosely-coupled-teams/; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | DORA finds strong correlation between coupling and delivery performance |
| [inference] Platform engineering converts local gains into global gains | https://dora.dev/research/2025/dora-report/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://www.infoq.com/news/2026/03/ai-dora-report/ | medium | DORA 2025 identifies platform quality as required capability; causal direction inferred |
| [inference] WIP limits and small-batch discipline subordinate non-constraint resources to the constraint | https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 | medium | TOC prescription confirmed as DORA capability requirement |
| [inference] Regulated-environment bottleneck migration to compliance queues after local automation | https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html | medium | Prior repository item; mechanism consistent with TOC; no direct cross-sector empirical study |
| [inference] "Stay busy" norm is cultural amplifier of local-optima failure | https://fortelabs.com/blog/theory-of-constraints-102-local-optima/ | medium | Practitioner synthesis; no independent peer-reviewed study of this specific norm |
| [inference] Shadow IT exhibits same structural failure as local tooling optimisation | https://davidamitchell.github.io/Research/research/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.html; https://davidamitchell.github.io/Research/research/2026-05-16-do-mode-demand-persistence-and-build-mode-displacement.html | medium | Prior repository synthesis; consistent with DORA and TOC findings |

### Assumptions

- Knowledge-work pipelines with shared downstream dependencies follow the same constraint-throughput logic as manufacturing pipelines in TOC, because both involve discrete work items flowing through sequential stages with a rate-limiting shared resource; TOC has been applied to software delivery, project management, and healthcare in peer-reviewed literature cited in the prior backpressure-TOC repository item, and the Forte Labs series explicitly extends the analysis to knowledge work. [assumption; source: https://fortelabs.com/blog/theory-of-constraints-101/; https://en.wikipedia.org/wiki/Theory_of_constraints; https://davidamitchell.github.io/Research/research/2026-04-01-backpressure-theory-of-constraints.html]

- Faros AI's developer telemetry represents a sufficient cross-section of knowledge-work organisations to support a directional inference about the local-to-global gap, even though the population over-represents GitHub-hosted engineering teams; Faros reports the population size (22,000 developers, 4,000+ teams) and methodology, and the direction is consistent with DORA survey data and TOC theory from independent sources. [assumption; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

- AI-assisted coding is a valid proxy for local tooling optimisation in the knowledge-work sense: it raises an individual contributor's delivery rate without automatically raising the capacity of shared downstream stages; DORA 2025 and Faros both use AI adoption as the test case and find the amplifier pattern consistent with this assumption. [assumption; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/]

### Analysis

The evidence converges on a single structural pattern: local tooling gains become global losses at the shared constraint. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-102-local-optima/; https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

TOC provides the theoretical frame: throughput is bounded by the constraint, so non-constraint gains cannot raise global throughput; they can only accumulate as WIP in front of the constraint, reducing its effective capacity via coordination overhead. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints; https://fortelabs.com/blog/theory-of-constraints-101/]

The Faros telemetry provides the most direct empirical test in this body of evidence, comparing individual output against shared-infrastructure outcomes simultaneously. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The 441% increase in PR review time against a 33.7% increase in task completion is inconsistent with local gains translating into global gains; instead, the shared review gate is absorbing the throughput increase as queue depth rather than producing faster delivery. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

DORA 2025 contextualises this pattern: the seven capabilities required for AI gains to translate to organisational performance are all concerned with reducing the coupling density that amplifies the gap. [inference; source: https://dora.dev/research/2025/dora-report/; https://www.infoq.com/news/2026/03/ai-dora-report/] Platform quality reduces queue accumulation. [inference; source: https://www.infoq.com/news/2026/03/ai-dora-report/] Small-batch discipline limits WIP at the constraint. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] Loose coupling reduces coordination-overhead tax on the constraint's capacity. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/]

The dominant rival explanation is that the Faros data reflects a transition period and quality and stability will improve once organisations adapt their review processes to the new throughput level. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] This is consistent with TOC step 4 (elevate the constraint), but requires active intervention, not passive adaptation. [inference; source: https://en.wikipedia.org/wiki/Theory_of_constraints] The DORA 2025 finding that even organisations with strong engineering foundations see downstream quality pressure from AI adoption suggests that explicit constraint-elevation investment is required regardless of baseline maturity. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025]

### Risks, Gaps, and Uncertainties

- No peer-reviewed controlled experiment directly tests the local-tooling-to-global-loss hypothesis in knowledge work with a randomised design. The evidence is correlational (Faros telemetry, DORA survey) and theoretical (TOC). The direction is consistent across multiple independent sources, supporting the medium-confidence assignment.
- The Faros developer population over-represents GitHub-hosted engineering teams and may not generalise to non-software knowledge work (legal review, financial analysis, strategic planning). No equivalent telemetry study for those knowledge-work types was found in this search.
- The relative weight of the three amplifying interdependencies (approval queues, architectural coupling, change-management gates) is not directly measurable from the available evidence. The ranking is an inference from the Faros and DORA pattern, not from a direct comparison experiment.
- TOC's five-step model assumes a stable, identifiable constraint; in software delivery the constraint migrates after each improvement cycle (from coding to review, from review to deployment, from deployment to incident response). This migration is described in TOC step 5 but is not directly measured in the DORA or Faros data.

### Open Questions

- What is the measurable coupling-density threshold below which local tooling gains stop reducing global throughput? This is a candidate for a new research backlog item in quantitative form.
- How does the local-global throughput gap behave in non-engineering knowledge work (legal review, financial modelling, regulatory analysis) where AI tooling adoption is accelerating but shared constraint surfaces differ from software delivery?
- Does architectural decoupling eliminate the local-global gap, or does it displace the constraint to a different shared surface (Application Programming Interface (API) governance, integration testing, data contract management)?

---

## Output

- Type: knowledge
- Description: Structured synthesis showing that TOC mechanics predict local tooling optimisation degrades global throughput in proportion to shared dependency density, and that DORA 2025 and Faros AI 2026 telemetry provide large-scale empirical confirmation of this pattern in AI-assisted software delivery. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://dora.dev/research/2025/dora-report/]
- Links:
  - https://fortelabs.com/blog/theory-of-constraints-102-local-optima/ (primary practitioner explanation of local vs global optima in knowledge work)
  - https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 (Faros AI telemetry showing Acceleration Whiplash across 22,000 developers)
  - https://dora.dev/capabilities/loosely-coupled-teams/ (DORA capability evidence on architectural decoupling and delivery performance)
