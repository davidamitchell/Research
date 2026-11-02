---
review_count: 2
title: "Substrate-aware enterprise strategic objectives and feasible delivery allocation"
added: 2026-11-01T10:53:33+00:00
status: reviewing
priority: medium
blocks: []
themes: [enterprise-adoption, organisational-design, software-engineering, formal-methods, cost-performance]
started: 2026-11-02T05:23:16+00:00
completed: ~
output: []
cites:
  - 2026-10-01-thinnest-viable-internal-platform-standard
  - 2026-10-23-dependency-properties-coordination-mechanisms
  - 2026-06-13-local-global-optima-knowledge-work-throughput
  - 2026-05-31-gore-strategic-intent-to-delivery-decomposition
related:
  - 2026-10-02-ideal-internal-platform-product-standard
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Substrate-aware enterprise strategic objectives and feasible delivery allocation

## Research Question

What evidence supports or challenges the need for enterprise strategic objectives to explicitly incorporate the existing delivery substrate (multi-year Software as a Service (SaaS) contracts, embedded platform commitments, established team topologies, capacity limits, and architectural dependencies), and which objective-formulation criteria and mechanisms make subsequent allocation between stream-aligned autonomy and centralized architectural coordination feasible without generating technical or capability debt?

## Scope

**In scope:**
- Criteria and decision rules at the enterprise strategic-objective layer that surface delivery-substrate constraints.
- Evidence for and against substrate-aware formulation, including conditions under which substrate-independent objectives remain feasible.
- Mechanisms that connect objective formulation to operating-model choice and the allocation of autonomy and architectural coordination.
- Positive capacity and buffer models that reserve room for coordination, change, maintenance, and capability development rather than leave debt as the residual.
- Contract horizons, embedded platform commitments, team cognitive load, shared bottlenecks, and architectural dependencies.

**Out of scope:**
- Team-level backlog prioritisation, sprint planning, and stand-up practices.
- Purely financial head-count models disconnected from delivery architecture.
- Evaluation of specific tooling.

**Constraints:**
- No industry, enterprise size, or strategic planning horizon is specified; state where any proposed rule depends on these factors.
- Distinguish constraints that are fixed within the objective's horizon from commitments that can be renegotiated or changed through a funded transition; do not assume the current substrate must remain permanent.
- Seek primary research, standards, and documented enterprise cases; distinguish practitioner guidance from empirical evidence and cross-domain analogies from validated enterprise mechanisms.
- Assess the assumptions and transfer limits of mathematical capacity models; do not invent enterprise capacity thresholds or buffer percentages.
- Define technical debt and capability debt separately and specify observable indicators for each.
- Expected eventual output: a knowledge synthesis of evidence, conditional formulation criteria, and allocation mechanisms. No investigation is performed when adding this item.

## Context

[Issue #686](https://github.com/davidamitchell/Research/issues/686) asks how enterprise architecture and operating-model choices can inform strategic objectives before allocation decisions, testing the hypothesis that discovering entrenched delivery constraints only during execution turns delivery pressure into local workarounds and accumulated debt.

## Approach

1. What evidence shows that acknowledging substrate constraints during objective formulation improves enterprise delivery feasibility? Review enterprise cases and studies, distinguishing observed outcomes from proposed explanations.
2. Under what conditions can substrate-independent strategic objectives remain feasible? Seek counterexamples and compare explicit constraint incorporation with later decomposition, funded substrate change, and staged commitment.
3. Which objective-level criterion reveals a binding contract or embedded platform commitment within the planning horizon? Examine constraint registers and objective specifications for treatment of exit costs, renewal dates, and transition lead times.
4. Which objective-level criterion exposes capacity or architectural-dependency infeasibility before allocation? Examine demand, shared bottleneck, dependency, and cognitive-load representations.
5. Which dependency property indicates that a delivery decision requires centralized architectural coordination rather than stream-aligned autonomy? Compare decision-rights and interaction-mode mechanisms using the constraint categories identified in questions 3 and 4.
6. Which traceability mechanism preserves feasibility when strategic intent is decomposed into scoped delivery objectives? Examine goal refinement and constraint propagation, drawing on questions 3 and 4.
7. Under what assumptions does each seeded cross-domain capacity model apply to enterprise delivery? Assess Erlang's queueing work, Little's law, Amdahl's law, Gunther's Universal Scalability Law, railway block signalling, and International Union of Railways (UIC) Code 406 separately; identify where an analogy lacks empirical validation.
8. Which positive capacity or buffer rule prevents technical debt from absorbing excess demand? Examine maintenance and coordination reservations, testing applicability against question 7.
9. Which positive capacity or buffer rule prevents capability debt from absorbing excess demand? Examine protected learning, capability development, and transition capacity, testing applicability against question 7.

Readiness: **READY**. Specific, answerable in principle, scoped, motivated, and decomposed; investigate both necessity and counterexamples rather than assume the motivating hypothesis is true.

## Related

- [Satisfiable internal platforms](https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html): starting point for Thinnest Viable Platform (TVP), cognitive-load, and fixed-capacity questions.
- [Ideal internal platforms as products](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html): starting point for assessing platform commitments as operating-model choices.
- [Dependency properties and coordination mechanisms](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html): starting point for question 5's allocation criteria.
- [Local and global optima in knowledge-work throughput](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html): starting point for shared bottlenecks and the difference between team and enterprise feasibility.
- [Platform engineering, InnerSource, and hybrid standardisation](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html): adjacent operating-model research in the issue's local-versus-global cluster.
- [Goal-Oriented Requirements Engineering (GORE): translating strategic intent to scoped delivery objectives](https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html): starting point for question 6's objective-refinement mechanisms.

## Sources

Starting points consulted, followed by sources added during research. Issue-linked entries preserve bibliographic leads supplied by the requester; locate and verify the original publications during research rather than cite the issue as evidence for the theories.

- [x] [Issue #686: Erlang (1909) and Little (1961)](https://github.com/davidamitchell/Research/issues/686): queueing and flow foundations to locate.
- [x] [Issue #686: Amdahl (1967) and Gunther's Universal Scalability Law](https://github.com/davidamitchell/Research/issues/686): serial work, contention, and coordination foundations to locate.
- [x] [Issue #686: railway block signalling and UIC Code 406](https://github.com/davidamitchell/Research/issues/686): capacity and buffer foundations to locate; verify the relevant edition and transfer assumptions.
- [x] [Issue #686: Conway (1968), Skelton and Pais (2019) Team Topologies, and Wardley Mapping](https://github.com/davidamitchell/Research/issues/686): organisational structure and strategy-mapping foundations to locate.
- [x] [Issue #686: Cunningham (1992) technical debt and Goldratt's Theory of Constraints](https://github.com/davidamitchell/Research/issues/686): debt and bottleneck foundations to locate.
- [x] [Satisfiable internal platforms](https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html)
- [x] [Ideal internal platforms as products](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html)
- [x] [Dependency properties and coordination mechanisms](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html)
- [x] [Local and global optima in knowledge-work throughput](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
- [x] [Platform engineering, InnerSource, and hybrid standardisation](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [x] [Goal-Oriented Requirements Engineering: translating strategic intent to scoped delivery objectives](https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html)
- [x] [Conway (1968) How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html)
- [x] [Cunningham (1992) The WyCash Portfolio Management System](http://c2.com/doc/oopsla92.html)
- [x] [Gunther (2008) A General Theory of Computational Scalability Based on Rational Functions](https://arxiv.org/abs/0808.1431)
- [x] [MacCormack, Rusnak and Baldwin (2012) Exploring the duality between product and organizational architectures](https://doi.org/10.1016/j.respol.2012.10.007)
- [x] [Kruchten, Nord and Ozkaya (2012) Technical Debt: From Metaphor to Theory and Practice](https://doi.org/10.1109/MS.2012.130)
- [x] [Ernst et al. (2015) Measure It? Manage It? Ignore It? Software Practitioners and Technical Debt](https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/)
- [x] [Cataldo and Herbsleb (2013) Coordination Breakdowns and Their Impact on Development Productivity and Software Failures](https://doi.org/10.1109/TSE.2012.32)
- [x] [Ross, Weill and Robertson (2006) Enterprise Architecture as Strategy](https://cisr.mit.edu/publication/enterprise-architecture-as-strategy)
- [x] [Mintzberg and Waters (1985) Of strategies, deliberate and emergent](https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html)
- [x] [Skelton and Pais Team Topologies Key Concepts](https://teamtopologies.com/key-concepts)
- [x] [Oricchio (2026) UIC 406 Rail Line Capacity: Compression and Mixed Traffic](https://www.ibano.com/insights/uic-406-rail-line-capacity-compression)
- [x] [Plus Maths (2026) Agner Krarup Erlang (1878 - 1929)](https://plus.maths.org/agner-krarup-erlang-1878-1929)
- [x] [Little (1961) A Proof for the Queuing Formula L = lambda W](https://doi.org/10.1287/opre.9.3.383)
- [x] [Amdahl (1967) Validity of the single processor approach to achieving large scale computing capabilities](https://doi.org/10.1145/1465482.1465560)
- [x] [Agile Laws Kingman's Formula](https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html)
- [x] [DORA Loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/)
- [x] [Forte Labs Theory of Constraints 103: The Four Fundamental Principles of Flow](https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/)
- [x] [Infopro Learning Learning Debt: The Hidden Cost of Deferring L&D Capacity Decisions](https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/)
- [x] [Connecting Experts The Real Transformation Bottleneck: Capability Debt](https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation)
- [x] [VendorBenchmark SaaS Renewal Negotiation Playbook 2026](https://vendorbenchmark.com/guides/renewal-negotiation-playbook)
- [x] [Faros AI (2025/2026) Key Takeaways from the DORA Report 2025 and AI Engineering Report 2026](https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025)

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
question: do enterprise strategic objectives need to carry the existing delivery substrate explicitly, and which formulation criteria make later allocation feasible without technical or capability debt
substrate_definition: the existing delivery base of multi-year contracts, platform commitments, team structures, capacity limits, and architectural dependencies
scope: objective-formulation criteria, counterexamples, allocation mechanisms, capacity and buffer models
constraints: no assumed industry or horizon; fixed versus renegotiable commitments kept distinct; no invented thresholds
output: knowledge synthesis
```

Prior-work check against completed repository items (all cited later with URLs):

- Satisfiable internal platforms, which treats cognitive load as a fixed capacity: https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html
- Dependency properties and coordination mechanisms, which supplies question 5's inputs: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html
- Local and global optima in knowledge-work throughput, which supplies the shared-bottleneck mechanism: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html
- Goal-Oriented Requirements Engineering (GORE) decomposition, which supplies question 6's refinement rules: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html
- Ideal internal platforms as products: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html
- Platform engineering, InnerSource, and hybrid standardisation: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html

Working hypothesis under test: [assumption] objectives that ignore substrate constraints convert delivery pressure into local workarounds, and the issue's motivating hypothesis is treated as a claim to test rather than a premise (source: https://github.com/davidamitchell/Research/issues/686). Justification: the issue frames the hypothesis as the question to investigate, and the item's own Approach requires counterexamples (source: https://github.com/davidamitchell/Research/issues/686).

### §1 Question Decomposition

Approach sub-questions broken into atomic questions, one evidence-based claim each.

```text
Q1 evidence that substrate-aware formulation improves feasibility
  Q1a what do organisation-structure and architecture studies show about structure constraining design
  Q1b what do coordination studies show about dependency-coordination mismatch
  Q1c does any study test objective-level substrate acknowledgement directly
Q2 conditions where substrate-independent objectives stay feasible
  Q2a emergent and staged strategy
  Q2b funded substrate change
Q3 objective-level criterion for binding contracts and platform commitments
Q4 objective-level criterion for capacity and architectural-dependency infeasibility
Q5 dependency property that indicates a need for central architectural coordination
Q6 traceability mechanism that preserves feasibility under decomposition
Q7 transfer assumptions of each seeded capacity model
  Q7a Erlang, Q7b Little, Q7c Amdahl and Universal Scalability Law (USL), Q7d railway blocks and UIC 406
Q8 positive buffer rule against technical debt
Q9 positive buffer rule against capability debt
```

### §2 Investigation

Evidence gathered per atomic question. Source classes: primary (original paper or standard), secondary (peer-reviewed summary or practitioner synthesis), tertiary or vendor (flagged).

**Q1a, structure constrains design.** Conway states that any given design team organisation rules out a class of design alternatives because the necessary communication paths do not exist. [fact; source: https://www.melconway.com/Home/Committees_Paper.html] The same paper states that voluntarily abandoning a creation is painful and expensive. [fact; source: https://www.melconway.com/Home/Committees_Paper.html] A test of the mirroring hypothesis, the claim that product architecture copies organisational structure, compared products from tightly coupled commercial firms with products from loosely coupled open-source communities and reports that the loosely coupled organisations produced more modular products. [inference; source: https://doi.org/10.1016/j.respol.2012.10.007] Access note: the publisher page for MacCormack et al. was read only through an abstract-level summary, so no effect sizes are carried into this item.

**Q1b, coordination mismatch.** Cataldo and Herbsleb examined two large projects from different companies and report that gaps between coordination requirements and actual coordination increase software failures, and that higher socio-technical congruence, meaning a match between technical dependencies and the communication that handles them, is associated with higher productivity. [fact; source: https://doi.org/10.1109/TSE.2012.32] The dependency-properties item finds that no property set prescribes a coordination mechanism without organisational context. [fact; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html] That finding limits how far Cataldo and Herbsleb's result can be turned into an objective-level rule. [inference; source: https://doi.org/10.1109/TSE.2012.32; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

**Q1c, direct tests of objective-level substrate acknowledgement.** Ross, Weill and Robertson define an operating model as the level of business-process integration and standardisation an enterprise needs, and argue it should be chosen before architecture decisions. [inference; source: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy] That source is a practitioner-research book built on case studies, so it is guidance and not a controlled test of feasibility outcomes. [inference; source: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy] Search record: queries for empirical studies linking objective formulation, constraint registers, and contract horizons to delivery feasibility returned vendor and analyst renewal playbooks and no peer-reviewed study; outcome "not found". Vendor playbooks advise starting renewal preparation well before expiry, but they are produced by firms that sell negotiation services. [inference; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook] Direct causal evidence for the motivating hypothesis is therefore absent from the sources located. [inference; source: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy; https://doi.org/10.1109/TSE.2012.32]

**Q2, substrate-independent objectives.** Mintzberg and Waters distinguish intended strategy from realised strategy, defining strategy as a pattern in a stream of decisions, and describe emergent strategies that form without or despite intentions. [fact; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html] Cunningham contrasts waterfall-style up-front design, which he compares to payment in advance and in full, with incremental growth followed by consolidation. [fact; source: http://c2.com/doc/oopsla92.html] Exhaustive up-front modelling of the substrate therefore competes with staged commitment as a route to feasibility. [inference; source: http://c2.com/doc/oopsla92.html; https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html] Ross, Weill and Robertson describe building the architecture one project at a time, which is consistent with funded substrate change inside the horizon. [inference; source: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy]

**Q3, contract and platform-commitment criterion.** No source located specifies an objective-level test for binding commitments; the search record under Q1c covers this gap. [inference; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook] The satisfiable-platform item treats a platform as justified only while it removes a verified shared burden at lower cost than the burden removed, which turns a platform commitment into a reversible inequality that needs re-testing. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html] The ideal-platform item lists a platform team becoming the organisation's central blocking dependency as a recurring anti-pattern, which shows that a platform commitment can itself become a constraint on objectives. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html]

**Q4 and Q5, capacity and dependency criteria.** The throughput item reports that individual task completion rose 33.7% while pull-request review time rose 441% in 22,000-developer telemetry, a case of local acceleration flooding a shared review queue. [fact; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025] The same item attributes the mechanism to the Theory of Constraints (TOC), in which system throughput is limited by its scarcest shared resource. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/] DevOps Research and Assessment (DORA) lists loosely coupled teams as a capability, which ties autonomy to architectural decoupling. [inference; source: https://dora.dev/capabilities/loosely-coupled-teams/] Team Topologies names three interaction modes, collaboration, X-as-a-Service, and facilitating, and defines a stream-aligned team as a team aligned to a single flow of work from a business domain. [fact; source: https://teamtopologies.com/key-concepts] The satisfiable-platform item records that no validated software-engineering instrument measures cognitive load, the limit on what a team can hold in mind, directly. [fact; source: https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html] High recurrence with reversible, bounded-impact work favours delegation or self-service, and high required certainty or regulatory exposure favours synchronisation. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

**Q6, traceability.** The GORE item finds that refinement rules give no criterion for when a goal is refined enough to act on and treat temporal constraints as informal annotations. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html] It also finds that the Knowledge Acquisition in autOmated Specification (KAOS) framework's obstacle analysis checks failure modes of individual goals and does not check end-to-end coverage from strategic intent to leaf requirements. [fact; source: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html] A substrate constraint attached to a strategic objective therefore has no standard propagation mechanism in the refinement frameworks reviewed, and a supplementary mechanism is needed. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html]

**Q7, transfer of capacity models.** Erlang's 1909 work on Copenhagen telephone traffic modelled call arrivals as a Poisson process. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929] The Erlang B blocking formula assumes Poisson arrivals, exponentially distributed holding times, a fixed number of servers, and blocked calls cleared, none of which describe enterprise work items that queue, vary widely in size, and share staff. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929] Search record: the primary 1909 paper in Nyt Tidsskrift for Matematik was not located in accessible form; outcome "not found", and the assumptions above rest on a secondary biography. Little's law relates average work in the system to arrival rate and average time in the system for a stable system, and it needs no arrival or service distribution assumption. [inference; source: https://doi.org/10.1287/opre.9.3.383; https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html] Gunther proves that the Universal Scalability Law (USL) is equivalent to a machine-repairman queueing bound, with Amdahl's law as a corollary. [fact; source: https://arxiv.org/abs/0808.1431] Amdahl's law bounds speedup by the serial fraction of a task, and applying it to organisations requires an assumption that serial coordination work can be identified and that its share stays fixed as teams are added. [inference; source: https://doi.org/10.1145/1465482.1465560; https://arxiv.org/abs/0808.1431] Search record: no study located that fits the USL to measured enterprise team-scaling data; outcome "not found". Kingman's formula, as summarised by a practitioner source, makes queueing delay grow in proportion to utilisation divided by one minus utilisation, so delay rises steeply as shared resources approach full load. [inference; source: https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html] The UIC 406 method compresses a real timetable and measures the share of a period that trains occupy, and it gives no fixed trains-per-hour capacity. [fact; source: https://www.ibano.com/insights/uic-406-rail-line-capacity-compression] A secondary summary of the leaflet lists peak-hour occupancy rates of 85% for dedicated suburban lines and 75% for high-speed and mixed-traffic lines. [fact; source: https://www.ibano.com/insights/uic-406-rail-line-capacity-compression] Those rates depend on fixed track geometry, signalling headways, and a published timetable, so they do not transfer to enterprise delivery, where demand and service times are not fixed by physical block lengths. [inference; source: https://www.ibano.com/insights/uic-406-rail-line-capacity-compression] Search record: the primary UIC 406 leaflet was not located in accessible form; outcome "not found", so the thresholds above are secondary-source values.

**Q8, technical debt.** Cunningham states that shipping first-time code is like going into debt, that a little debt speeds development when promptly repaid, and that every minute spent on not-quite-right code counts as interest. [fact; source: http://c2.com/doc/oopsla92.html] Kruchten, Nord and Ozkaya describe technical debt as extending to anything that adds friction to deploying or evolving software, including architectural and test debt, and argue for explicit management such as a backlog of debt items. [inference; source: https://doi.org/10.1109/MS.2012.130] Ernst and colleagues surveyed 1,831 software engineers and architects to identify the most important sources of technical debt. [fact; source: https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/] No source located gives an enterprise-wide maintenance reservation percentage. [inference; source: https://doi.org/10.1109/MS.2012.130; https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/]

**Q9, capability debt.** Definition needed: no authoritative or peer-reviewed definition of capability debt was located. [inference; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/] Practitioner sources describe the term as the gap between the skills an organisation has and the skills its commitments require, accumulated when learning and hiring investment is deferred. [inference; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation] Both are consultancy or training-vendor publications, so they establish usage and not measured effect. [inference; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/] The Team Topologies facilitating interaction mode, in which one team helps another build capability, is the nearest documented mechanism for protected capability transfer. [inference; source: https://teamtopologies.com/key-concepts]

**Platform operating-model adjacency.** The InnerSource and platform-engineering item finds that mandatory centralisation without extension points produces bypass behaviour that recreates fragmentation outside governance. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html] The same item reports a DORA 2024 finding that platform engineering can decrease change stability, which marks a central platform as a risk concentration. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]

### §3 Reasoning

Causal chain from the evidence to the design criteria, each step labelled and sourced.

1. Organisation structure rules out classes of design alternatives, and abandoning a built design is costly. [fact; source: https://www.melconway.com/Home/Committees_Paper.html]
2. Loosely coupled organisations produced more modular products in a comparative study, which supports treating structure as a real constraint on what objectives can deliver. [inference; source: https://doi.org/10.1016/j.respol.2012.10.007]
3. Mismatch between coordination requirements and actual coordination raises failures in two large projects, which supports checking dependency-coordination fit when objectives are formulated. [inference; source: https://doi.org/10.1109/TSE.2012.32]
4. Local acceleration was followed by a large rise in shared review time in the cited telemetry, which shows shared queues limiting system throughput. [inference; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
5. Queueing delay rises steeply as utilisation approaches full load in the cited practitioner summary, which supports reserving slack on shared bottlenecks instead of planning them at full load. [inference; source: https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html]
6. No source located supplies a validated enterprise buffer percentage, so any buffer rule must be derived from observed local data. [inference; source: https://doi.org/10.1109/MS.2012.130; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression]
7. Direct evidence that substrate-aware objective formulation improves feasibility is absent from the sources located, so the criteria below are design syntheses and carry low to medium confidence. [inference; source: https://cisr.mit.edu/publication/enterprise-architecture-as-strategy; https://doi.org/10.1109/TSE.2012.32]

### §4 Consistency Check

Apparent tension between emergent strategy and up-front substrate acknowledgement resolved as a conditional rule: staged commitment is adequate when the substrate is renegotiable inside the horizon, and explicit acknowledgement matters when commitments bind. [inference; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://doi.org/10.1109/MS.2012.130]

```text
contradiction_scan: resolved
unresolved_contradictions: none
confidence_adjustment: criteria findings kept at medium or low because direct tests are absent
scope_guardrail: maintained
threshold_guardrail: rail occupancy rates not carried into enterprise buffers
```

### §5 Depth and Breadth Expansion

**Economic lens.** Cunningham's interest metaphor frames debt as a recurring cost that grows until consolidation, so a buffer sized from observed interest follows the metaphor's own logic. [inference; source: http://c2.com/doc/oopsla92.html] Renewal and exit terms on Software as a Service (SaaS) contracts are economic constraints that objectives cannot override, although evidence about their typical lead times comes only from vendor playbooks. [inference; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook]

**Behavioural lens.** Mandatory centralisation without extension points produced bypass behaviour in the platform item, so a constraint register imposed without a route for exceptions invites workarounds. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html] A platform team that becomes the only route for change can turn into the blocking dependency the register was meant to expose. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html]

**Historical lens.** Conway's 1968 observation and the later mirroring tests are consistent over decades, although the studies concern software products and may not extend to non-software strategic objectives. [inference; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1016/j.respol.2012.10.007]

**Technical lens.** The Universal Scalability Law (USL) adds a coordination term to Amdahl's serial fraction and is proved equivalent to a queueing bound, which suggests that adding teams to a shared substrate can reduce throughput past a point. [inference; source: https://arxiv.org/abs/0808.1431] The parameters would need fitting to local data, and no enterprise fit was located. [inference; source: https://arxiv.org/abs/0808.1431]

**Regulatory lens.** No source located addresses regulatory obligations as substrate constraints, so that lens remains a gap. [assumption; source: https://doi.org/10.1109/MS.2012.130]

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

Substrate-aware objective formulation, meaning formulation that records the existing delivery base of contracts, platforms, team structures, and capacity limits, is warranted when commitments bind inside the objective's horizon and is less critical when the base is renegotiable through funded or staged change, and no direct empirical test of the hypothesis was located. [inference; source: https://doi.org/10.1109/TSE.2012.32; https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html]
The best-supported formulation criteria are a contract test (a commitment binds an objective when its earliest exit date plus transition lead time falls after the date the objective needs the change), a per-bottleneck demand-and-capacity record, and a coordination rule that centralises decisions touching shared, hard-to-reverse elements. [inference; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1109/TSE.2012.32; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
Capacity models from telephony, queueing, and railways supply structural questions and bounds and supply no transferable utilisation thresholds, and debt buffers are best sized from locally observed rework and onboarding cost. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression; https://doi.org/10.1109/MS.2012.130]

**Key findings:**

1. Direct empirical evidence that explicit substrate acknowledgement at objective formulation improves delivery feasibility was not found, and the case for it rests on adjacent studies of organisational structure, coordination, and architecture. ([inference]; medium confidence; source: https://doi.org/10.1109/TSE.2012.32; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy)
2. Organisation structure constrains which designs can be built, and a comparison of loosely and tightly coupled organisations found that loosely coupled ones produced more modular products, which supports treating structure as a real constraint on objectives. ([inference]; medium confidence; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1016/j.respol.2012.10.007)
3. Gaps between coordination requirements and actual coordination were associated with more software failures in two large projects, which supports checking dependency-coordination fit when objectives are set. ([inference]; medium confidence; source: https://doi.org/10.1109/TSE.2012.32)
4. Substrate acknowledgement is less critical when strategy is emergent, when the substrate can be changed through funded projects inside the horizon, or when demand sits well below capacity, so the criterion is conditional on binding commitments. ([inference]; medium confidence; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy)
5. A proposed contract criterion treats a commitment as binding an objective when its earliest exit date plus transition lead time falls after the date the objective needs the change, and no located study validates this test, so it remains a design inference. ([inference]; low confidence; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook; https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html)
6. Local speed gains flooded a shared review queue in cited telemetry, and queueing theory summaries show delay rising steeply near full utilisation, which supports a per-bottleneck demand-and-capacity record with slack instead of planning shared resources at full load. ([inference]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. Centralised coordination is indicated for decisions that touch shared, hard-to-reverse elements with many consumers, while reversible bounded decisions suit delegation or self-service, although no dependency property set prescribes a mechanism without organisational context. ([inference]; medium confidence; source: https://teamtopologies.com/key-concepts; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
8. Goal-Oriented Requirements Engineering (GORE) refinement frameworks offer no sufficiency criterion and no standard propagation of constraints, so substrate constraints need an external register whose entries each refined goal inherits by reference. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html)
9. The Erlang, Little, Amdahl, Universal Scalability Law, and railway occupancy models each rest on assumptions that enterprise work violates in places, and the railway occupancy rates are track-specific values that should not become enterprise buffer percentages. ([inference]; medium confidence; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://arxiv.org/abs/0808.1431; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression)
10. Technical debt buffers are best sized from observed interest such as rework and incident time, because the located literature offers a debt metaphor and practitioner survey but no validated enterprise reservation percentage. ([inference]; medium confidence; source: http://c2.com/doc/oopsla92.html; https://doi.org/10.1109/MS.2012.130; https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/)
11. Capability debt lacks an authoritative definition in the located sources, which are consultancy and training-vendor publications, so buffers for it should rest on observable indicators such as single-person dependencies and onboarding time. ([inference]; low confidence; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation)

**Cross-domain model table:**

| Model | Transferable idea | Where the assumption breaks | Validation status |
|---|---|---|---|
| [inference] Erlang B | Finite servers produce blocking | Work waits and retries, sizes vary | Secondary summary only; source: https://plus.maths.org/agner-krarup-erlang-1878-1929 |
| [inference] Little's law | Work in system equals arrival rate times time in system for stable systems | Unstable or unmeasured flow | Primary DOI not read; source: https://doi.org/10.1287/opre.9.3.383 |
| [inference] Amdahl and Universal Scalability Law | Serial and coordination fractions cap scaling | Fractions are hard to identify and change over time | Equivalence proved; no enterprise fit located; source: https://arxiv.org/abs/0808.1431 |
| [inference] Kingman's formula | Delay rises steeply near full load | Single-queue idealisation | Practitioner summary; source: https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html |
| [inference] UIC 406 | Capacity is measured by compressing a real plan | Occupancy rates are track-specific | Secondary summary; source: https://www.ibano.com/insights/uic-406-rail-line-capacity-compression |

**Evidence map:** see Findings, which carries the full table.

**Assumptions:**

Objectives are assumed to be set over a horizon of years for an enterprise with shared platforms and multi-year contracts. [assumption; source: https://github.com/davidamitchell/Research/issues/686]
The issue's hypothesis that late discovery of entrenched constraints leads to local workarounds and debt is assumed plausible enough to test and is not assumed true. [assumption; source: https://github.com/davidamitchell/Research/issues/686]
Practitioner and vendor sources are assumed to establish common usage of terms such as capability debt without establishing measured effect. [assumption; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/]

**Analysis:**

Evidence weight is highest for the structural-constraint claims, which rest on a foundational paper and two empirical studies of different design. [inference; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1109/TSE.2012.32]
The criteria are weighted lower because they combine those studies with prior repository findings and practitioner sources and have not been tested as objective-level rules. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html; https://doi.org/10.1109/MS.2012.130]
One rival remedy is to pre-plan everything against a complete substrate model, which Cunningham's incremental-growth argument and Mintzberg and Waters' emergent strategy both count against when requirements are unclear. [inference; source: http://c2.com/doc/oopsla92.html; https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html]
A second rival remedy is to pool the shared bottleneck through a central platform team, which the platform items show can itself become the blocking dependency. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]
The two remedies are resolved as complements: staged commitment handles renegotiable substrate, and register-based acknowledgement handles binding substrate. [inference; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy]
Definition needed: a "demand-and-capacity record" here means a list of demand lines against each shared bottleneck, such as a platform team, a review queue, or an architecture authority, with the nearest evidence-backed equivalent being the Theory of Constraints (TOC) practice of identifying the constraining resource. [inference; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/]
Debt reservations enter that record as demand lines sized from observed rework, incident time, onboarding time, and contractor reliance. [inference; source: http://c2.com/doc/oopsla92.html; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation]

**Risks, gaps, uncertainties:**

No peer-reviewed study of objective-level constraint registers or contract-horizon tests was found in the searches recorded in §2. [inference; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook]
Primary sources for Erlang's 1909 paper, the UIC 406 leaflet, and the Little and Amdahl papers were not read, so transfer-assumption claims rest on secondary summaries. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression]
Wardley Mapping and Goldratt's primary text on the Theory of Constraints were not examined, which leaves two named seed topics only partly covered. [inference; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/]
Regulatory obligations as substrate constraints are not covered by the located sources. [assumption; source: https://doi.org/10.1109/MS.2012.130]

**Open questions:**

- Can a contract-horizon test be validated against recorded cases of objectives that failed on contract or platform constraints? [assumption; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook]
- Can the Universal Scalability Law be fitted to measured enterprise team data? [assumption; source: https://arxiv.org/abs/0808.1431]
- What measurable definition of capability debt would survive peer review? [assumption; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/]

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
labels_and_sources_audit: passed
confidence: medium
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Substrate-aware objective formulation, meaning formulation that records the existing delivery base of contracts, platforms, team structures, and capacity limits, is warranted when commitments bind inside the objective's horizon and is less critical when the base is renegotiable through funded or staged change, and no direct empirical test of the hypothesis was located. [inference; source: https://doi.org/10.1109/TSE.2012.32; https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html]
The best-supported formulation criteria are a contract test (a commitment binds an objective when its earliest exit date plus transition lead time falls after the date the objective needs the change), a per-bottleneck demand-and-capacity record, and a coordination rule that centralises decisions touching shared, hard-to-reverse elements. [inference; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1109/TSE.2012.32; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
Capacity models from telephony, queueing, and railways supply structural questions and bounds and supply no transferable utilisation thresholds, and debt buffers are best sized from locally observed rework and onboarding cost. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression; https://doi.org/10.1109/MS.2012.130]

### Key Findings

1. Direct empirical evidence that explicit substrate acknowledgement at objective formulation improves delivery feasibility was not found, and the case for it rests on adjacent studies of organisational structure, coordination, and architecture. ([inference]; medium confidence; source: https://doi.org/10.1109/TSE.2012.32; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy)
2. Organisation structure constrains which designs can be built, and a comparison of loosely and tightly coupled organisations found that loosely coupled ones produced more modular products, which supports treating structure as a real constraint on objectives. ([inference]; medium confidence; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1016/j.respol.2012.10.007)
3. Gaps between coordination requirements and actual coordination were associated with more software failures in two large projects, which supports checking dependency-coordination fit when objectives are set. ([inference]; medium confidence; source: https://doi.org/10.1109/TSE.2012.32)
4. Substrate acknowledgement is less critical when strategy is emergent, when the substrate can be changed through funded projects inside the horizon, or when demand sits well below capacity, so the criterion is conditional on binding commitments. ([inference]; medium confidence; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy)
5. A proposed contract criterion treats a commitment as binding an objective when its earliest exit date plus transition lead time falls after the date the objective needs the change, and no located study validates this test, so it remains a design inference. ([inference]; low confidence; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook; https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html)
6. Local speed gains flooded a shared review queue in cited telemetry, and queueing theory summaries show delay rising steeply near full utilisation, which supports a per-bottleneck demand-and-capacity record with slack instead of planning shared resources at full load. ([inference]; medium confidence; source: https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. Centralised coordination is indicated for decisions that touch shared, hard-to-reverse elements with many consumers, while reversible bounded decisions suit delegation or self-service, although no dependency property set prescribes a mechanism without organisational context. ([inference]; medium confidence; source: https://teamtopologies.com/key-concepts; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
8. Goal-Oriented Requirements Engineering (GORE) refinement frameworks offer no sufficiency criterion and no standard propagation of constraints, so substrate constraints need an external register whose entries each refined goal inherits by reference. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html)
9. The Erlang, Little, Amdahl, Universal Scalability Law, and railway occupancy models each rest on assumptions that enterprise work violates in places, and the railway occupancy rates are track-specific values that should not become enterprise buffer percentages. ([inference]; medium confidence; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://arxiv.org/abs/0808.1431; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression)
10. Technical debt buffers are best sized from observed interest such as rework and incident time, because the located literature offers a debt metaphor and practitioner survey but no validated enterprise reservation percentage. ([inference]; medium confidence; source: http://c2.com/doc/oopsla92.html; https://doi.org/10.1109/MS.2012.130; https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/)
11. Capability debt lacks an authoritative definition in the located sources, which are consultancy and training-vendor publications, so buffers for it should rest on observable indicators such as single-person dependencies and onboarding time. ([inference]; low confidence; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation)

### Cross-domain Model Table

| Model | Transferable idea | Where the assumption breaks | Validation status |
|---|---|---|---|
| [inference] Erlang B | Finite servers produce blocking | Work waits and retries, sizes vary | Secondary summary only; source: https://plus.maths.org/agner-krarup-erlang-1878-1929 |
| [inference] Little's law | Work in system equals arrival rate times time in system for stable systems | Unstable or unmeasured flow | Primary DOI not read; source: https://doi.org/10.1287/opre.9.3.383 |
| [inference] Amdahl and Universal Scalability Law | Serial and coordination fractions cap scaling | Fractions are hard to identify and change over time | Equivalence proved; no enterprise fit located; source: https://arxiv.org/abs/0808.1431 |
| [inference] Kingman's formula | Delay rises steeply near full load | Single-queue idealisation | Practitioner summary; source: https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html |
| [inference] UIC 406 | Capacity is measured by compressing a real plan | Occupancy rates are track-specific | Secondary summary; source: https://www.ibano.com/insights/uic-406-rail-line-capacity-compression |

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Direct empirical evidence that explicit substrate acknowledgement at objective formulation improves delivery feasibility was not found, and the case for it rests on adjacent studies of organisational structure, coordination, and architecture. | https://doi.org/10.1109/TSE.2012.32; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy | medium | design synthesis |
| [inference] Organisation structure constrains which designs can be built, and a comparison of loosely and tightly coupled organisations found that loosely coupled ones produced more modular products, which supports treating structure as a real constraint on objectives. | https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1016/j.respol.2012.10.007 | medium | design synthesis |
| [inference] Gaps between coordination requirements and actual coordination were associated with more software failures in two large projects, which supports checking dependency-coordination fit when objectives are set. | https://doi.org/10.1109/TSE.2012.32 | medium | design synthesis |
| [inference] Substrate acknowledgement is less critical when strategy is emergent, when the substrate can be changed through funded projects inside the horizon, or when demand sits well below capacity, so the criterion is conditional on binding commitments. | https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy | medium | design synthesis |
| [inference] A proposed contract criterion treats a commitment as binding an objective when its earliest exit date plus transition lead time falls after the date the objective needs the change, and no located study validates this test, so it remains a design inference. | https://vendorbenchmark.com/guides/renewal-negotiation-playbook; https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html | low | design synthesis |
| [inference] Local speed gains flooded a shared review queue in cited telemetry, and queueing theory summaries show delay rising steeply near full utilisation, which supports a per-bottleneck demand-and-capacity record with slack instead of planning shared resources at full load. | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025; https://agilelaws.com/iterative-delivery-and-flow/kingmans-formula.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html | medium | design synthesis |
| [inference] Centralised coordination is indicated for decisions that touch shared, hard-to-reverse elements with many consumers, while reversible bounded decisions suit delegation or self-service, although no dependency property set prescribes a mechanism without organisational context. | https://teamtopologies.com/key-concepts; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html | medium | design synthesis |
| [inference] Goal-Oriented Requirements Engineering (GORE) refinement frameworks offer no sufficiency criterion and no standard propagation of constraints, so substrate constraints need an external register whose entries each refined goal inherits by reference. | https://davidamitchell.github.io/Research/research/2026-05-31-gore-strategic-intent-to-delivery-decomposition.html | medium | design synthesis |
| [inference] The Erlang, Little, Amdahl, Universal Scalability Law, and railway occupancy models each rest on assumptions that enterprise work violates in places, and the railway occupancy rates are track-specific values that should not become enterprise buffer percentages. | https://plus.maths.org/agner-krarup-erlang-1878-1929; https://arxiv.org/abs/0808.1431; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression | medium | design synthesis |
| [inference] Technical debt buffers are best sized from observed interest such as rework and incident time, because the located literature offers a debt metaphor and practitioner survey but no validated enterprise reservation percentage. | http://c2.com/doc/oopsla92.html; https://doi.org/10.1109/MS.2012.130; https://www.sei.cmu.edu/library/measure-it-manage-it-ignore-it-software-practitioners-and-technical-debt/ | medium | design synthesis |
| [inference] Capability debt lacks an authoritative definition in the located sources, which are consultancy and training-vendor publications, so buffers for it should rest on observable indicators such as single-person dependencies and onboarding time. | https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation | low | design synthesis |

### Assumptions

Objectives are assumed to be set over a horizon of years for an enterprise with shared platforms and multi-year contracts. [assumption; source: https://github.com/davidamitchell/Research/issues/686]
The issue's hypothesis that late discovery of entrenched constraints leads to local workarounds and debt is assumed plausible enough to test and is not assumed true. [assumption; source: https://github.com/davidamitchell/Research/issues/686]
Practitioner and vendor sources are assumed to establish common usage of terms such as capability debt without establishing measured effect. [assumption; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/]

### Analysis

Evidence weight is highest for the structural-constraint claims, which rest on a foundational paper and two empirical studies of different design. [inference; source: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1109/TSE.2012.32]
The criteria are weighted lower because they combine those studies with prior repository findings and practitioner sources and have not been tested as objective-level rules. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-01-thinnest-viable-internal-platform-standard.html; https://doi.org/10.1109/MS.2012.130]
One rival remedy is to pre-plan everything against a complete substrate model, which Cunningham's incremental-growth argument and Mintzberg and Waters' emergent strategy both count against when requirements are unclear. [inference; source: http://c2.com/doc/oopsla92.html; https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html]
A second rival remedy is to pool the shared bottleneck through a central platform team, which the platform items show can itself become the blocking dependency. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html; https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]
The two remedies are resolved as complements: staged commitment handles renegotiable substrate, and register-based acknowledgement handles binding substrate. [inference; source: https://ideas.repec.org/a/bla/stratm/v6y1985i3p257-272.html; https://cisr.mit.edu/publication/enterprise-architecture-as-strategy]
Definition needed: a "demand-and-capacity record" here means a list of demand lines against each shared bottleneck, such as a platform team, a review queue, or an architecture authority, with the nearest evidence-backed equivalent being the Theory of Constraints (TOC) practice of identifying the constraining resource. [inference; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/]
Debt reservations enter that record as demand lines sized from observed rework, incident time, onboarding time, and contractor reliance. [inference; source: http://c2.com/doc/oopsla92.html; https://www.connectingexperts.com/the-real-transformation-bottleneck-capability-debt-and-why-strategic-hiring-fixes-it-faster-than-reorganisation]

### Risks, Gaps, and Uncertainties

No peer-reviewed study of objective-level constraint registers or contract-horizon tests was found in the searches recorded in §2. [inference; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook]
Primary sources for Erlang's 1909 paper, the UIC 406 leaflet, and the Little and Amdahl papers were not read, so transfer-assumption claims rest on secondary summaries. [inference; source: https://plus.maths.org/agner-krarup-erlang-1878-1929; https://www.ibano.com/insights/uic-406-rail-line-capacity-compression]
Wardley Mapping and Goldratt's primary text on the Theory of Constraints were not examined, which leaves two named seed topics only partly covered. [inference; source: https://fortelabs.com/blog/theory-of-constraints-103-the-four-fundamental-principles-of-flow/]
Regulatory obligations as substrate constraints are not covered by the located sources. [assumption; source: https://doi.org/10.1109/MS.2012.130]

### Open Questions

- Can a contract-horizon test be validated against recorded cases of objectives that failed on contract or platform constraints? [assumption; source: https://vendorbenchmark.com/guides/renewal-negotiation-playbook]
- Can the Universal Scalability Law be fitted to measured enterprise team data? [assumption; source: https://arxiv.org/abs/0808.1431]
- What measurable definition of capability debt would survive peer review? [assumption; source: https://www.infoprolearning.com/blog/learning-debt-the-hidden-cost-of-deferring-ld-capacity-decisions/]

---

## Output

- Type: knowledge
- Description: Conditional case for substrate-aware strategic objectives with contract, capacity, coordination, and traceability criteria and debt-buffer rules, labelled as design inference because direct tests were not found. [inference; source: https://doi.org/10.1109/TSE.2012.32]
- Links: https://www.melconway.com/Home/Committees_Paper.html; https://doi.org/10.1109/TSE.2012.32; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html
