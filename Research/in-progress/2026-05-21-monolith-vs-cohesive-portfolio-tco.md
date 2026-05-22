---
title: "Long-term total cost of ownership trade-offs: few tightly coupled monoliths vs many tightly cohesive systems"
added: 2026-05-21T20:43:51+00:00
status: reviewing
priority: high
blocks: []
tags: [software-architecture, coupling, cohesion, maintainability, total-cost-of-ownership, organisational-design, transaction-costs]
started: 2026-05-22T06:38:39+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-03-10-nature-of-the-firm-coase-organisations
  - 2026-05-16-agent-operational-cost-vs-gap-closure-cost
related:
  - 2026-04-30-deep-modules-ai-augmented-codebases
  - 2026-04-02-org-shape-software-cost-zero
  - 2026-03-22-code-architecture-inspection
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Long-term total cost of ownership trade-offs: few tightly coupled monoliths vs many tightly cohesive systems

## Research Question

How do structural differences between portfolios of a few large monolithic systems with tight
coupling, meaning many cross-component dependencies, and portfolios of many smaller tightly
cohesive systems, meaning each system concentrates on one bounded responsibility, correlate
with long-term Total Cost of Ownership (TCO), when balancing direct operational maintenance
costs, infrastructure, patching, and platform governance, against lifecycle mutation costs,
design, development, testing, and deployment?

## Scope

**In scope:**
- Empirical and theoretical evidence linking coupling, cohesion, modularity, and dependency
  propagation to maintainability, change cost, and operating cost
- Cost categories explicitly named in the item: infrastructure, patching, platform governance,
  design, development, testing, and deployment
- Comparative analysis of architecture portfolios, few monoliths versus many smaller cohesive
  systems, over multi-year horizons
- Conditions where one portfolio shape is expected to dominate the other on long-term TCO
- Governance and transaction-cost considerations when many systems multiply coordination
  surfaces

**Out of scope:**
- Vendor-specific tooling or cloud-pricing recommendations
- A prescriptive migration playbook for any single organisation
- Claims of universal superiority independent of team capability, automation depth, and
  governance maturity

**Constraints:**
- Use publicly accessible URLs
- Separate evidence-backed facts from inferences and assumptions
- Prefer decision-grade conclusions with explicit conditions instead of universal claims

## Context

Architecture portfolio shape changes both software mutation cost and internal coordination
cost, so modular design evidence and transaction-cost reasoning both matter when estimating
long-run TCO. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html]

## Approach

1. Define coupling, cohesion, modularity, and hidden-complexity concepts in the software design
   literature.
2. Extract evidence on how these variables affect mutation cost, especially comprehension,
   testing, deployment, and change propagation.
3. Extract evidence on how service proliferation affects operating costs, especially monitoring,
   governance, and organisational coordination.
4. Identify the conditions under which smaller cohesive systems reduce TCO and the conditions
   under which they only shift complexity into the platform layer.
5. Synthesize a falsifiable decision rule that maps boundary quality and governance maturity to
   expected long-run cost outcomes.

## Sources

- [x] [Parnas (1972) On the Criteria To Be Used in Decomposing Systems into Modules](http://sunnyday.mit.edu/16.355/parnas-criteria.html)
- [x] [Ousterhout (2018) Modular Design lecture notes](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign)
- [x] [Chidamber and Kemerer (1994) A Metrics Suite for Object Oriented Design](https://ieeexplore.ieee.org/document/295895/)
- [x] [Briand et al. (1999) A Unified Framework for Coupling Measurement in Object-Oriented Systems](https://ieeexplore.ieee.org/document/748920/)
- [x] [MacCormack et al. (2005) Exploring the Structure of Complex Software Designs working paper](https://www.hbs.edu/ris/Publication%20Files/05-016.pdf)
- [x] [Villamizar et al. (2015) Evaluating the monolithic and the microservice architecture pattern to deploy web applications in the cloud](https://doi.org/10.1109/ColumbianCC.2015.7333476)
- [x] [Kalske et al. (2018) Challenges When Moving from Monolith to Microservice Architecture](https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content)
- [x] [Auer et al. (2021) From Monolithic Systems to Microservices: An Assessment Framework](https://arxiv.org/abs/1909.08933)
- [x] [Mitchell (2026) The Nature of the Firm: why organisations exist, their fitness functions, and invariants](https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html)
- [x] [Mitchell (2026) Agent Operational Cost vs Gap Closure Cost](https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html)
- [ ] [Taube-Schock et al. (2011) Can We Avoid High Coupling?](https://researchcommons.waikato.ac.nz/handle/10289/5307)
- [ ] [Bogner et al. (2019) Assuring the Evolvability of Microservices: Insights into Industry Practices and Challenges](https://ieeexplore.ieee.org/document/8813066)

## Related

- [The Nature of the Firm: why organisations exist, their fitness functions, and invariants](https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html)
- [Deep modules in AI-augmented development: interface design, contract-first delegation, and architectural rescue of AI-generated codebases](https://davidamitchell.github.io/Research/research/2026-04-30-deep-modules-ai-augmented-codebases.html)
- [Agent Operational Cost vs Gap Closure Cost](https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html)

---

## Research Skill Output

### §0 Initialise

- question: compare the long-run Total Cost of Ownership (TCO) effects of a few tightly coupled
  monoliths against many smaller tightly cohesive systems.
- scope: weigh mutation-cost mechanisms, operating-cost mechanisms, and coordination-cost
  mechanisms over multi-year horizons.
- constraints: public URLs only, explicit fact and inference separation, no universal claims.
- output: full structured knowledge note with evidence map and conditional decision rule.
- mode: full.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html;
  https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]
  Prior completed repository work matters in two ways: the transaction-cost item frames
  architecture boundaries as coordination-cost choices, and the gap-closure item shows that
  recurring operational complexity can outweigh build-time savings when a stable capability could
  instead be encoded deterministically.

### §1 Question Decomposition

```text
Root question: when does portfolio shape lower or raise long-run TCO?
|
|-- A. Structural mechanism
|   |-- A1. What do coupling, cohesion, and modular depth mean in the consulted literature?
|   `-- A2. Why should these variables affect change propagation and comprehension cost?
|
|-- B. Mutation cost
|   |-- B1. What evidence shows that more modular structure improves evolvability?
|   `-- B2. Can deliberate redesign materially change future mutation cost?
|
|-- C. Operating cost
|   |-- C1. What benefits do smaller independently deployable services provide?
|   `-- C2. What new monitoring, testing, and governance burdens appear?
|
|-- D. Boundary conditions
|   |-- D1. When do smaller cohesive systems outperform monoliths?
|   `-- D2. When does fragmentation only shift complexity into the platform layer?
|
`-- E. Synthesis
    |-- E1. Which variables dominate the decision?
    `-- E2. What falsifiable decision rule follows from the evidence?
```

### §2 Investigation

#### Source-access and search notes

- source_correction: the seeded Villamizar source link pointed to the wrong IEEE record and was replaced
  with `https://doi.org/10.1109/ColumbianCC.2015.7333476`.
- source_correction: the seeded Kalske source link pointed to the wrong Springer chapter and was
  replaced with the Helsinki repository copy of `10.1007/978-3-319-74433-9_3`.
- search_note: no accessible study in this session provided a direct multi-year, audited TCO
  benchmark comparing few large monoliths against many cohesive systems as whole portfolios, so
  the answer must be synthesized from mutation-cost, operating-cost, and coordination-cost
  evidence.
- search_note: the Taube-Schock and Bogner items were identified but not needed for the final
  decision rule once stronger directly consulted sources covered the same trade-off surface.

#### A. Foundational structural theory

- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas states that
  modularization should improve flexibility and comprehensibility, and that those benefits depend
  on how the system is divided into modules.
- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html] Parnas names shorter
  development time, product flexibility, and one-module-at-a-time understanding as expected
  benefits of good modular decomposition.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]
  Ousterhout defines a deep module as one with a simple interface and substantial hidden
  functionality, and a shallow module as one whose interface complexity is large relative to the
  functionality it hides.
- [fact; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]
  Ousterhout argues that interfaces should be much simpler than implementations so that changes
  inside a module do not force changes in other modules.
- [fact; source: https://ieeexplore.ieee.org/document/295895/] Chidamber and Kemerer argue that
  managers need theoretically grounded design metrics when they adopt new software-development
  approaches, because process improvement depends on having measures that describe structural
  properties rather than intuition alone.
- [fact; source: https://ieeexplore.ieee.org/document/748920/] Briand and coauthors report that
  coupling measurement in object-oriented systems had become rich but difficult to compare, so they
  created a unified terminology and framework to classify measures consistently.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://ieeexplore.ieee.org/document/295895/; https://ieeexplore.ieee.org/document/748920/]
  Taken together, the foundational literature implies that TCO is shaped by how much dependency
  knowledge leaks across boundaries, because leaked knowledge increases the amount of system
  context required for each local change.

#### B. Mutation-cost evidence

- [fact; source: https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] MacCormack, Rusnak, and
  Baldwin report that Linux initially had a more modular architecture than Mozilla, but a
  purposeful Mozilla redesign produced an architecture that was significantly more modular than
  both its predecessor and Linux.
- [fact; source: https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] The same working paper
  states that purposeful managerial actions can materially adapt a design's structure rather than
  leaving modularity as a fixed by-product of language or development mode.
- [inference; source: https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign]
  Mutation cost is not locked in once a system becomes complex, but redesign requires explicit
  effort to concentrate responsibility and reduce dependency exposure, which is why delayed
  modularization is possible but not free.

#### C. Operating-cost and deployment evidence

- [fact; source: https://doi.org/10.1109/ColumbianCC.2015.7333476] Villamizar and coauthors
  describe microservice architectures as sets of small services that can be developed, tested,
  deployed, scaled, operated, and upgraded independently, and they present a case study that
  reports both benefits and challenges relative to a monolithic approach.
- [fact; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content]
  Kalske, Makitalo, and Mikkonen find that typical reasons for moving from a monolith toward
  microservices are complexity, scalability, and code ownership, while the resulting challenges
  divide into architectural and organisational challenges.
- [fact; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content]
  Kalske and coauthors conclude that microservices become attractive when a company grows large
  enough for codebase size and monolithic complexity to become dominant problems, not as a
  context-free default.
- [fact; source: https://arxiv.org/abs/1909.08933] Auer and coauthors argue that migration from
  monoliths to microservices should be based on collected evidence rather than instinct, and they
  propose an assessment framework that tells companies which information and metrics to gather
  before re-architecting.
- [fact; source: https://arxiv.org/abs/1909.08933] The Auer preprint describes microservices as
  autonomous services with a single clearly defined purpose that can be developed, deployed, and
  tested independently by different teams and technology stacks.
- [fact; source: https://arxiv.org/abs/1909.08933] The same preprint says microservices can make
  maintenance easier and improve fault isolation, but testing can become more complex, multiple
  languages can increase overall complexity, and central monitoring and logging become explicit
  architectural needs.
- [inference; source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] Smaller cohesive systems reduce local deployment and mutation
  coupling only if they preserve real service autonomy, because otherwise they add service count
  without removing the underlying dependency tangle.

#### D. Coordination-cost and governance evidence

- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html]
  The prior transaction-cost item concludes that organisational boundaries exist where internal
  coordination is cheaper than external contracting, which makes boundary multiplication a cost
  question rather than a stylistic one.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]
  The prior gap-closure item finds that recurring operational work remains expensive when stable
  capability could instead be encoded into deterministic software and governance structures.
- [inference; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933;
  https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html;
  https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]
  A portfolio of many systems expands the coordination surface for monitoring, ownership, testing,
  and release governance, so its run-cost advantage depends on whether those coordination tasks are
  largely automated or mostly manual.

#### E. Working assumptions

- [assumption; source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] For this item, "many tightly cohesive systems" is treated as
  a portfolio in which services are independently deployable and each service has a bounded
  responsibility, because the consulted migration literature uses those properties as the practical
  mechanism behind the architecture pattern.
- [assumption; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] For this item, mutation cost is used as
  a proxy for a large share of long-run TCO because the accessible literature offers stronger
  evidence about comprehension, dependency propagation, and redesign effort than about audited
  multi-firm cost ledgers.

### §3 Reasoning

- [fact; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] The strongest direct evidence in this
  item concerns the mutation-cost side of the trade-off, because the consulted structural studies
  directly discuss modularity, hidden complexity, and redesign.
- [fact; source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] The strongest direct evidence on operating cost concerns the
  conditions and side effects of microservice migration, not audited portfolio-wide ledger data.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
  https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] The answer must therefore be conditional: modular and service
  decomposition lowers long-run cost when it reduces dependency propagation faster than it expands
  monitoring, testing, and governance overhead.

### §4 Consistency Check

- [fact; source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] None of the consulted monolith-to-microservices sources claims
  universal superiority for microservices; all describe benefits together with explicit conditions
  and challenges.
- [inference; source: https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://arxiv.org/abs/1909.08933] The apparent tension between "reduced complexity" and
  "increased complexity" resolves once local module simplicity is separated from portfolio-level
  operating complexity: a service can be simpler in isolation while the total estate becomes harder
  to govern.
- [inference; source: https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content]
  The consulted sources are consistent with a staged interpretation: modular redesign is valuable,
  but it pays off only when the redesign creates boundaries the organisation can actually own and
  operate.

### §5 Depth and Breadth Expansion

- [inference; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] Technical lens: deployment independence and fault isolation
  are real engineering advantages, but they create parallel needs for observability, integration
  testing, and platform standards.
- [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] Economic lens: the cost driver is not
  module or service count by itself, but the number of dependencies and the amount of leaked
  knowledge that must be paid for on each change.
- [inference; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html]
  Organisational lens: service proliferation increases coordination points for ownership,
  interfaces, and incident response, so governance maturity becomes part of architecture cost, not
  a separate management issue.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html;
  https://arxiv.org/abs/1909.08933] Operational lens: recurring manual governance and workaround
  effort behaves like durable run cost, so fragmented architectures are cheapest only when they
  convert coordination into repeatable platform capability instead of ongoing human effort.

### §6 Synthesis

**Executive summary:**

Over multi-year horizons, portfolios of many smaller cohesive systems usually beat a few tightly
coupled monoliths on Total Cost of Ownership (TCO) only when boundary quality is high and
platform governance is mature; otherwise the extra coordination surface can make them more
expensive than a well-structured monolith. [inference; source:
http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://doi.org/10.1109/ColumbianCC.2015.7333476;
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933]

The mutation-cost side of the trade-off is strong: foundational modularity theory and the Mozilla
redesign study both support the claim that reducing dependency exposure lowers future change
burden and can be achieved deliberately rather than accidentally. [inference; source:
http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]

The operating-cost side is equally real: the migration literature says smaller services help when
monolithic size, scalability, and ownership become dominant pain points, but they also demand
more explicit monitoring, testing, ownership, and organisational coordination. [fact; source:
https://doi.org/10.1109/ColumbianCC.2015.7333476;
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933]

The practical decision rule is therefore not "monolith or microservices" but "are our boundaries
good enough, and our governance automated enough, that extra system count reduces dependency
propagation faster than it increases run-cost overhead?" [inference; source:
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933;
https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html;
https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

**Key findings:**

1. **High coupling and weak cohesion raise long-run mutation cost because every local change
   requires developers to understand, coordinate, and retest a wider dependency surface than the
   business change itself would otherwise require.** ([inference]; high confidence; source:
   http://sunnyday.mit.edu/16.355/parnas-criteria.html;
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://ieeexplore.ieee.org/document/295895/;
   https://ieeexplore.ieee.org/document/748920/)
2. **Purposeful redesign can materially improve evolvability, because the Mozilla case shows that
   managerial effort can produce a design that is significantly more modular than both an earlier
   version and an already more modular comparator.** ([fact]; medium confidence; source:
   https://www.hbs.edu/ris/Publication%20Files/05-016.pdf)
3. **Many smaller cohesive systems reduce change and deployment coupling only when they really are
   independently deployable, independently testable, and owned as bounded responsibilities rather
   than as thin wrappers around a still-shared dependency tangle.** ([inference]; high confidence;
   source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933)
4. **The same decomposition that lowers local change cost can raise portfolio run cost, because
   service counts expand the need for monitoring, logging, integration testing, ownership
   alignment, and organisational coordination.** ([fact]; high confidence; source:
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933)
5. **Smaller cohesive systems are most likely to lower long-run TCO when monolithic scale,
   scalability pressure, and code ownership friction have already become dominant costs, because
   that is the regime where deployment independence starts to offset governance overhead.**
   ([inference]; medium confidence; source:
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://doi.org/10.1109/ColumbianCC.2015.7333476;
   https://arxiv.org/abs/1909.08933)
6. **A well-structured monolith or a small number of deep modules can remain cheaper than a large
   service portfolio when the organisation lacks strong platform standards, because fragmentation
   then shifts complexity into operations and governance instead of actually removing it.**
   ([inference]; medium confidence; source:
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933;
   https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html)
7. **The dominant decision variable is therefore boundary quality plus governance maturity, not
   service count alone, which makes "few versus many" a weaker predictor of TCO than dependency
   exposure and the amount of manual coordination left in the operating model.** ([inference];
   medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933;
   https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] High coupling and weak cohesion raise long-run mutation cost by expanding change-propagation and retest surfaces. | http://sunnyday.mit.edu/16.355/parnas-criteria.html ; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://ieeexplore.ieee.org/document/295895/ ; https://ieeexplore.ieee.org/document/748920/ | high | Structural mechanism |
| [fact] Purposeful redesign can materially improve modularity and evolvability. | https://www.hbs.edu/ris/Publication%20Files/05-016.pdf | medium | Mozilla redesign |
| [inference] Smaller cohesive systems lower deployment and change coupling only when independence is real. | https://doi.org/10.1109/ColumbianCC.2015.7333476 ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 | high | Boundary quality matters |
| [fact] Service proliferation raises monitoring, logging, integration, ownership, and coordination overhead. | https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 | high | Run-cost surface |
| [inference] Smaller cohesive systems lower TCO chiefly after monolithic size and ownership pain dominate. | https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://doi.org/10.1109/ColumbianCC.2015.7333476 ; https://arxiv.org/abs/1909.08933 | medium | Conditional regime |
| [inference] A well-structured monolith can stay cheaper than fragmentation when governance is weak. | https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 ; https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html | medium | Fragmentation penalty |
| [inference] Boundary quality and governance maturity predict TCO better than system count alone. | http://sunnyday.mit.edu/16.355/parnas-criteria.html ; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 ; https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html | medium | Final decision rule |

**Assumptions:**

- [assumption; source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933] "Many tightly cohesive systems" is treated as a portfolio of
  truly independent bounded services, because the consulted literature uses that operational
  independence as the mechanism behind the architecture's benefits.
- [assumption; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf] Mutation cost is treated as a major
  proxy for long-run TCO because the accessible evidence base is much stronger on dependency
  propagation and redesign effort than on audited cross-firm cost ledgers.

**Analysis:**

The evidence weighs more heavily toward structural mechanism than toward direct accounting
measurement, so the most defensible answer is about cost drivers rather than universal percentage
deltas. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]

An important rival explanation is that microservices look cheaper simply because the studied
firms were already under exceptional growth pressure, which would have forced re-architecture
under almost any naming scheme. That challenge matters, but the consulted sources still point to a
bounded mechanism, independent deployment and bounded ownership, rather than to naming alone.
[inference; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933; https://doi.org/10.1109/ColumbianCC.2015.7333476]

Another rival remedy is to keep the monolith but deepen its internal modules. The evidence does
not reject that option; in fact, it suggests it is often the cheaper first move when service-level
governance would still be manual. [inference; source:
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

The practical trade-off is therefore triangular rather than binary: reduce dependency exposure,
preserve real deployment autonomy, and automate enough governance that extra system count does not
become a standing tax. [inference; source:
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933;
https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html]

**Risks, gaps, uncertainties:**

- Direct audited portfolio-wide TCO datasets remain absent in the consulted evidence base, so the
  final answer is a conditional synthesis rather than a universal numeric benchmark. [fact; source:
  https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- The empirical microservice literature in this item concentrates on migration contexts, which may
  overrepresent organisations already experiencing scale or complexity pain. [inference; source:
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- The unconsulted Taube-Schock and Bogner items could sharpen the coupling-unavoidability and
  service-evolvability sides of the argument, but they are unlikely to reverse the main conditional
  conclusion already supported by the consulted sources. [inference; source:
  https://researchcommons.waikato.ac.nz/handle/10289/5307;
  https://ieeexplore.ieee.org/document/8813066]

**Open questions:**

- Which public datasets measure how much observability and platform-engineering headcount rises as
  service counts increase? [inference; source:
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- Under what conditions does a modular monolith capture most mutation-cost benefits without paying
  the governance cost of many independently deployed systems? [inference; source:
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]
- Which observable governance metrics best predict when a service portfolio has crossed from
  productive decomposition into fragmentation debt? [inference; source:
  https://arxiv.org/abs/1909.08933;
  https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

### §7 Recursive Review

- review_result: pass after full-document logic, acronym, citation, and parity checks.
- acronym_audit: passed, with Total Cost of Ownership (TCO) expanded on first use and no other
  unexplained initialisms retained in prose.
- claim_audit: Research Skill Output claims are labeled and Findings claims use suffix epistemic
  labels with URL-backed sources; workflow notes remain pure metadata fragments.
- parity_check: §6 Synthesis and Findings are substantively aligned.

---

## Findings

### Executive Summary

Over multi-year horizons, portfolios of many smaller cohesive systems usually beat a few tightly
coupled monoliths on Total Cost of Ownership (TCO) only when boundary quality is high and
platform governance is mature; otherwise the extra coordination surface can make them more
expensive than a well-structured monolith. [inference; source:
http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://doi.org/10.1109/ColumbianCC.2015.7333476;
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933]

The mutation-cost side of the trade-off is strong: foundational modularity theory and the Mozilla
redesign study both support the claim that reducing dependency exposure lowers future change
burden and can be achieved deliberately rather than accidentally. [inference; source:
http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]

The operating-cost side is equally real: the migration literature says smaller services help when
monolithic size, scalability, and ownership become dominant pain points, but they also demand
more explicit monitoring, testing, ownership, and organisational coordination. [fact; source:
https://doi.org/10.1109/ColumbianCC.2015.7333476;
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933]

The practical decision rule is therefore not "monolith or microservices" but "are our boundaries
good enough, and our governance automated enough, that extra system count reduces dependency
propagation faster than it increases run-cost overhead?" [inference; source:
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933;
https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html;
https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

### Key Findings

1. **High coupling and weak cohesion raise long-run mutation cost because every local change
   requires developers to understand, coordinate, and retest a wider dependency surface than the
   business change itself would otherwise require.** ([inference]; high confidence; source:
   http://sunnyday.mit.edu/16.355/parnas-criteria.html;
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://ieeexplore.ieee.org/document/295895/;
   https://ieeexplore.ieee.org/document/748920/)
2. **Purposeful redesign can materially improve evolvability, because the Mozilla case shows that
   managerial effort can produce a design that is significantly more modular than both an earlier
   version and an already more modular comparator.** ([fact]; medium confidence; source:
   https://www.hbs.edu/ris/Publication%20Files/05-016.pdf)
3. **Many smaller cohesive systems reduce change and deployment coupling only when they really are
   independently deployable, independently testable, and owned as bounded responsibilities rather
   than as thin wrappers around a still-shared dependency tangle.** ([inference]; high confidence;
   source: https://doi.org/10.1109/ColumbianCC.2015.7333476;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933)
4. **The same decomposition that lowers local change cost can raise portfolio run cost, because
   service counts expand the need for monitoring, logging, integration testing, ownership
   alignment, and organisational coordination.** ([fact]; high confidence; source:
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933)
5. **Smaller cohesive systems are most likely to lower long-run TCO when monolithic scale,
   scalability pressure, and code ownership friction have already become dominant costs, because
   that is the regime where deployment independence starts to offset governance overhead.**
   ([inference]; medium confidence; source:
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://doi.org/10.1109/ColumbianCC.2015.7333476;
   https://arxiv.org/abs/1909.08933)
6. **A well-structured monolith or a small number of deep modules can remain cheaper than a large
   service portfolio when the organisation lacks strong platform standards, because fragmentation
   then shifts complexity into operations and governance instead of actually removing it.**
   ([inference]; medium confidence; source:
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933;
   https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html)
7. **The dominant decision variable is therefore boundary quality plus governance maturity, not
   service count alone, which makes "few versus many" a weaker predictor of TCO than dependency
   exposure and the amount of manual coordination left in the operating model.** ([inference];
   medium confidence; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
   https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
   https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
   https://arxiv.org/abs/1909.08933;
   https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] High coupling and weak cohesion raise long-run mutation cost by expanding change-propagation and retest surfaces. | http://sunnyday.mit.edu/16.355/parnas-criteria.html ; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://ieeexplore.ieee.org/document/295895/ ; https://ieeexplore.ieee.org/document/748920/ | high | Structural mechanism |
| [fact] Purposeful redesign can materially improve modularity and evolvability. | https://www.hbs.edu/ris/Publication%20Files/05-016.pdf | medium | Mozilla redesign |
| [inference] Smaller cohesive systems lower deployment and change coupling only when independence is real. | https://doi.org/10.1109/ColumbianCC.2015.7333476 ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 | high | Boundary quality matters |
| [fact] Service proliferation raises monitoring, logging, integration, ownership, and coordination overhead. | https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 | high | Run-cost surface |
| [inference] Smaller cohesive systems lower TCO chiefly after monolithic size and ownership pain dominate. | https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://doi.org/10.1109/ColumbianCC.2015.7333476 ; https://arxiv.org/abs/1909.08933 | medium | Conditional regime |
| [inference] A well-structured monolith can stay cheaper than fragmentation when governance is weak. | https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 ; https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html | medium | Fragmentation penalty |
| [inference] Boundary quality and governance maturity predict TCO better than system count alone. | http://sunnyday.mit.edu/16.355/parnas-criteria.html ; https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign ; https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content ; https://arxiv.org/abs/1909.08933 ; https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html | medium | Final decision rule |

### Assumptions

- "Many tightly cohesive systems" means truly bounded services with real deployment independence,
  because the consulted migration literature treats that property as the mechanism behind the
  pattern's benefits; without real independence, system count rises without removing the
  underlying dependency tangle. [assumption; source:
  https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- Mutation cost is a major proxy for long-run TCO in this item, because the accessible evidence
  base is much stronger on dependency propagation and redesign effort than on audited cross-firm
  cost ledgers, so the synthesis must reason from the best-supported cost mechanism. [assumption;
  source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]

### Analysis

The evidence weighs more heavily toward structural mechanism than toward direct accounting
measurement, so the most defensible answer is about cost drivers rather than universal percentage
deltas. [inference; source: http://sunnyday.mit.edu/16.355/parnas-criteria.html;
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]

An important rival explanation is that microservices look cheaper simply because the studied
firms were already under exceptional growth pressure, which would have forced re-architecture
under almost any naming scheme. That challenge matters, but the consulted sources still point to a
bounded mechanism, independent deployment and bounded ownership, rather than to naming alone.
[inference; source: https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933; https://doi.org/10.1109/ColumbianCC.2015.7333476]

Another rival remedy is to keep the monolith but deepen its internal modules. The evidence does
not reject that option; in fact, it suggests it is often the cheaper first move when service-level
governance would still be manual. [inference; source:
https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
https://www.hbs.edu/ris/Publication%20Files/05-016.pdf;
https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

The practical trade-off is therefore triangular rather than binary: reduce dependency exposure,
preserve real deployment autonomy, and automate enough governance that extra system count does not
become a standing tax. [inference; source:
https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
https://arxiv.org/abs/1909.08933;
https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html]

### Risks, Gaps, and Uncertainties

- Direct audited portfolio-wide TCO datasets remain absent in the consulted evidence base, so the
  final answer is a conditional synthesis rather than a universal numeric benchmark. [fact; source:
  https://doi.org/10.1109/ColumbianCC.2015.7333476;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- The empirical microservice literature in this item concentrates on migration contexts, which may
  overrepresent organisations already experiencing scale or complexity pain. [inference; source:
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- The unconsulted Taube-Schock and Bogner items could sharpen the coupling-unavoidability and
  service-evolvability sides of the argument, but they are unlikely to reverse the main conditional
  conclusion already supported by the consulted sources. [inference; source:
  https://researchcommons.waikato.ac.nz/handle/10289/5307;
  https://ieeexplore.ieee.org/document/8813066]

### Open Questions

- Which public datasets measure how much observability and platform-engineering headcount rises as
  service counts increase? [inference; source:
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- Under what conditions does a modular monolith capture most mutation-cost benefits without paying
  the governance cost of many independently deployed systems? [inference; source:
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://www.hbs.edu/ris/Publication%20Files/05-016.pdf]
- Which observable governance metrics best predict when a service portfolio has crossed from
  productive decomposition into fragmentation debt? [inference; source:
  https://arxiv.org/abs/1909.08933;
  https://davidamitchell.github.io/Research/research/2026-05-16-agent-operational-cost-vs-gap-closure-cost.html]

---

## Output

- Type: knowledge
- Description: This item produces a conditional decision rule for when service proliferation lowers
  long-run TCO and when a better-structured monolith remains cheaper. [inference; source:
  http://sunnyday.mit.edu/16.355/parnas-criteria.html;
  https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=modularDesign;
  https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content;
  https://arxiv.org/abs/1909.08933]
- Links:
  - https://www.hbs.edu/ris/Publication%20Files/05-016.pdf
  - https://helda.helsinki.fi/server/api/core/bitstreams/b3f9ded3-9db4-4e91-b683-f3ebadd2ede9/content
  - https://arxiv.org/abs/1909.08933
