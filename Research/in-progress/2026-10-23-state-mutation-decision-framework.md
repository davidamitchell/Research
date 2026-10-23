---
review_count: 1
title: "State mutation decision framework: mapping delivery delay, ownership, and change costs"
added: 2026-10-23T21:41:54+00:00
status: reviewing
priority: high  # low | medium | high
blocks: []
themes: [software-engineering, cost-performance, benchmarks-eval]
started: 2026-10-23T23:31:01+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-04-30-ai-code-entropy-quality-metrics, 2026-05-21-monolith-vs-cohesive-portfolio-tco, 2026-05-29-commit-trends-repo-velocity-rework-abandonment, 2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate]
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# State mutation decision framework: mapping delivery delay, ownership, and change costs

## Research Question

Which published empirical software-engineering metrics can operationalise Cost of Delay (CoD),
Future Cost of Ownership (FCO), and Future Cost of Change (FCC), and what evidence shows whether
shortcut-related quality degradation compounds over time or affects ownership and change costs
differently across software architecture styles?

## Scope

**In scope:**
- Map established software quality, delivery, and cost measures to CoD, FCO, and FCC; test whether
  each measure is a direct outcome, a proxy, or an indicator of more than one construct.
- Assess candidate FCO indicators such as defect density, mean time to resolution (MTTR), incident
  frequency, and patch overhead, and candidate FCC indicators such as code churn, change
  propagation, cyclomatic complexity, and modification blast radius.
- Assess candidate CoD indicators such as change lead time, release latency, and service-level
  agreement (SLA) non-compliance costs, distinguishing elapsed delivery time from monetised delay.
- Review evidence linking technical shortcuts or technical debt to later maintenance burden and
  change friction, separating longitudinal or causal findings from cross-sectional correlations.
- Compare evidence across architecture styles, including monolithic, modular-monolith, and
  microservice systems, without assuming that operating cost and change friction move together.
- Consider relevant measurement frameworks and cost models, including the International
  Organization for Standardization and International Electrotechnical Commission (ISO/IEC) 25010
  quality model, Consortium for Information & Software Quality (CISQ) automated measures, and
  Constructive Cost Model II (COCOMO II) drivers.

**Out of scope:**
- Prescribing a universally superior architecture or a single metric score for all organisations.
- Vendor-specific tooling, pricing, or recommendations for a particular enterprise.
- Treating shortcut exposure as a comparable numeric variable unless a study defines and measures
  it explicitly.

**Constraints:**
- Search the Association for Computing Machinery (ACM) Digital Library, Institute of Electrical
  and Electronics Engineers (IEEE) Xplore, Google Scholar, and Software Engineering Institute
  (SEI) technical reports; record search strings, dates, screening criteria, and exclusions.
- Prefer peer-reviewed empirical studies, repository-mining datasets, official standards, and
  primary technical reports; use secondary sources for discovery and context.
- Report effect sizes and study limitations where available; do not infer a universal compounding
  rate from heterogeneous measures or observational associations.
- Treat CoD, FCO, and FCC as constructs to operationalise and validate, not as interchangeable
  labels for existing metrics.

## Context

The existing corpus asks which quality-metric bundle best predicts remediation cost
([code entropy and quality metrics](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md)),
leaves open when modular monoliths capture change benefits without service-governance costs
([architecture portfolio total cost of ownership](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md)),
tracks repository velocity and rework while leaving longitudinal outcomes unresolved
([repository commit trends](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md)),
and asks which measures distinguish unmet demand and debt accumulation
([throughput and debt accumulation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md)).
This review connects those strands to determine whether their metrics measure distinct cost
constructs or overlapping proxies, informing decisions about where short-term delivery choices
create later operating or modification costs.

## Approach

1. Define CoD, FCO, and FCC as decision constructs and identify how published studies operationalise
   delivery delay, recurring ownership cost, and change effort.
   1a. Map candidate measures to the construct and outcome they directly observe.
   1b. Check construct validity, overlap, measurement windows, and whether measures capture cost
   rather than only technical condition or elapsed time.
2. Review repository-mining and software-economics evidence on shortcuts and technical debt.
   2a. Extract longitudinal and causal estimates separately from cross-sectional associations.
   2b. Record how studies define shortcuts, debt, maintenance overhead, and change friction; identify
   whether any measured exposure supports a compounding claim.
3. Compare operational ownership costs and change-friction outcomes across architecture styles.
   3a. Separate recurring run-state outcomes from the effort and risk of making modifications.
   3b. Identify architecture, system size, team, and governance factors that may confound or moderate
   the comparison.
4. Synthesize a decision-oriented metric map, stating which measures are supported, ambiguous, or
   unsupported for each construct, and identify evidence gaps that prevent causal or general claims.

## Sources

Starting points from the completed research corpus and references already catalogued there:

- [ ] [McCabe (1976) A Complexity Measure](https://doi.org/10.1109/TSE.1976.233837) — cyclomatic complexity measure used in the quality-metrics review.
- [ ] [Chidamber and Kemerer (1994) A Metrics Suite for Object Oriented Design](https://ieeexplore.ieee.org/document/295895/) — object-oriented design metrics cited in the architecture cost review.
- [ ] [DevOps Research and Assessment (DORA) 2024 State of DevOps Report](https://dora.dev/research/2024/dora-report/) — delivery-performance and stability outcomes.
- [ ] [GitClear (2025) AI Copilot Code Quality: 2025 Look Back at 12 Months of Data](https://www.gitclear.com/ai_assistant_code_quality_2025_research) — repository-mining indicators of churn and rework.
- [ ] [Mitchell (2026) Artificial Intelligence code entropy and complexity](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md) — prior work on code-quality indicators and remediation-cost metric gaps.
- [ ] [Mitchell (2026) Long-term total cost of ownership trade-offs](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md) — prior architecture comparison and open questions on modular-monolith and governance costs.
- [ ] [Mitchell (2026) Software-development commit trends](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md) — repository velocity, rework, and open longitudinal questions.
- [ ] [Mitchell (2026) Information Technology throughput and debt accumulation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md) — prior work on delivery constraints and the need for debt-accumulation indicators.
- [ ] [Tornhill and Borg (2022) Code Red](https://arxiv.org/abs/2203.04374) — code quality, defects, and cycle time in 39 codebases.
- [ ] [Besker et al. (2018) Technical Debt Cripples Software Developer Productivity](https://research.chalmers.se/en/publication/507477) — wasted development time due to technical debt.
- [ ] [Lenarduzzi et al. (2019) Does Migrating a Monolithic System to Microservices Decrease the Technical Debt?](https://arxiv.org/abs/1902.06282) — debt growth before and after microservice extraction.
- [ ] [MacCormack and Sturtevant (2016) Technical Debt and System Architecture](https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf) — coupling and defect-related activity.
- [ ] [Jaspan and Green (2018) Defining, Measuring, and Managing Technical Debt](https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf) — metrics versus engineer-reported debt (mirror copy).
- [ ] [Sjøberg et al. (2013) Quantifying the Effect of Code Smells on Maintenance Effort](https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf) — controlled maintenance experiment.
- [ ] [Nagappan and Ball (2005) Use of Relative Code Churn Measures to Predict System Defect Density](https://ieeexplore.ieee.org/document/1553571) — churn and defect density.
- [ ] [Villamizar et al. (2017) Cost Comparison of Running Web Applications in the Cloud](https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/) — infrastructure cost by architecture style.
- [ ] [DORA Software Delivery Performance Metrics](https://dora.dev/guides/dora-metrics/) — definitions of change lead time and recovery time.
- [ ] [Wikipedia Cost of Delay](https://en.wikipedia.org/wiki/Cost_of_delay) — orientation definition only.
- [ ] [arc42 ISO/IEC 25010 Quality Model](https://quality.arc42.org/standards/iso-25010) — maintainability sub-characteristics.
- [ ] [arc42 ISO/IEC 5055 Automated Source Code Quality Measures](https://quality.arc42.org/standards/iso-5055) — CISQ weakness measures.
- [ ] [MSDBOK COCOMO II Drivers](https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html) — scale factors and effort multipliers.

---

## Research Skill Output

*(Full output from running the research skill; retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: Which published empirical software-engineering metrics can operationalise Cost of Delay (CoD), Future Cost of Ownership (FCO), and Future Cost of Change (FCC), and does shortcut-related quality degradation compound over time or differ across architecture styles?

Scope: map measures to constructs; separate longitudinal from cross-sectional evidence; compare monolithic, modular-monolith, and microservice evidence without assuming run cost and change friction move together.

Constraints: no universal compounding rate; no single score; CoD, FCO, and FCC are constructs to validate, not synonyms for existing metrics.

Prior work check: four completed items bear on this question. The code entropy review identifies clone ratio, short-term churn, and change coupling as early-warning signals. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md] The architecture portfolio review concludes that smaller cohesive systems lower Total Cost of Ownership (TCO) only when boundary quality and platform governance are mature. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md] The commit-trends review reports rising short-cycle churn alongside persistently low project-to-production conversion. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md] The throughput review finds no universal coefficient linking lost delivery throughput to accumulated unmet demand. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md]

Working hypothesis: elapsed-time and defect measures are inputs to CoD and FCO rather than the constructs themselves. [assumption; source: https://dora.dev/guides/dora-metrics/] The assumption is reasonable because the DevOps Research and Assessment (DORA) metrics are defined in time units and ratios, not in money. [assumption; source: https://dora.dev/guides/dora-metrics/]

### §1 Question Decomposition

```text
Q1 Construct definition
  Q1a Is CoD defined in money per unit time, and do delivery-time metrics measure that?
  Q1b Which measures observe recurring ownership cost (FCO) versus change effort (FCC)?
Q2 Shortcut and debt evidence
  Q2a What cross-sectional associations link code quality to defects and cycle time?
  Q2b Do controlled or longitudinal studies show maintenance effort rising with debt indicators?
  Q2c Does any study measure shortcut exposure and a compounding rate?
Q3 Architecture styles
  Q3a What evidence addresses run-state (operating) cost by architecture style?
  Q3b What evidence addresses change friction by architecture style or coupling structure?
Q4 Decision map
  Q4a Which measures are supported, ambiguous, or unsupported per construct?
```

### §2 Investigation

Search record: date 2026-10-23; engine = general web search plus publisher, author, and repository pages; queries = "technical debt cripples developer productivity wasted time", "migrating monolith to microservices technical debt", "coupling defect-related activity technical debt architecture", "code smells maintenance effort", "relative code churn defect density", "cost comparison monolithic microservice AWS Lambda", "ISO/IEC 25010 maintainability", "ISO/IEC 5055 CISQ", "COCOMO II scale factors cost drivers". Direct queries to ACM Digital Library, IEEE Xplore, Google Scholar, and SEI reports were not run; screening = peer-reviewed or primary technical report, empirical measurement of cost, effort, defects, or cycle time; exclusions = vendor pricing and opinion posts.

**Q1a. CoD and delivery time.**

CoD is defined as the partial derivative of total expected value with respect to time, expressed in currency per unit time. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay] The source is an encyclopedia summary of Reinertsen's product-development work, so the definition serves as orientation and carries an inference label. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay]

DORA defines change lead time as the time from commit to deployment in production, and failed deployment recovery time as the time to recover from a failed deployment needing immediate intervention. [fact; source: https://dora.dev/guides/dora-metrics/] Both are measured in time, not currency. [fact; source: https://dora.dev/guides/dora-metrics/]

Elapsed-time metrics therefore feed a CoD calculation only after a value-decay rate is supplied from outside the delivery data. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay; https://dora.dev/guides/dora-metrics/] Service-level agreement (SLA) non-compliance cost is a contractual monetised delay candidate, but none of the studies examined measures it. [assumption; source: https://en.wikipedia.org/wiki/Cost_of_delay]

DORA describes its five metrics as best suited to measuring one application or service at a time. [fact; source: https://dora.dev/guides/dora-metrics/] This limits their use for comparing architecture styles across portfolios. [inference; source: https://dora.dev/guides/dora-metrics/]

**Q1b. FCO and FCC candidates and standards.**

ISO/IEC 25010 lists maintainability sub-characteristics including modularity, analysability, modifiability, and testability, as summarised by the arc42 quality model. [inference; source: https://quality.arc42.org/standards/iso-25010] ISO/IEC 5055, the Consortium for Information & Software Quality (CISQ) automated source code measures, counts code weaknesses under reliability, security, performance efficiency, and maintainability, as summarised by arc42. [inference; source: https://quality.arc42.org/standards/iso-5055] Both describe structural condition, not realised cost. [inference; source: https://quality.arc42.org/standards/iso-25010; https://quality.arc42.org/standards/iso-5055]

Constructive Cost Model II (COCOMO II) uses scale factors and effort multipliers such as product complexity, platform volatility, and personnel continuity as ex-ante estimation drivers, as summarised by a practitioner body of knowledge. [inference; source: https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html] These drivers predict effort rather than observe it. [inference; source: https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html]

**Q2a. Cross-sectional quality and cost.**

Tornhill and Borg analysed 39 proprietary codebases and 30,737 files and report that low-quality code contains 15 times more defects, takes 124% more development time per issue, and shows 9 times longer maximum cycle times than high-quality code. [fact; source: https://arxiv.org/abs/2203.04374] The design is cross-sectional, uses a single commercial tool (CodeScene) for code-health scoring. [inference; source: https://arxiv.org/abs/2203.04374]

MacCormack and Sturtevant measured coupling for more than 20,000 components in each of two systems and report that tightly coupled core components cost significantly more defect-related activity than loosely coupled peripheral components, so a small number of components generate a large share of cost. [fact; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf] They also report major differences in refactoring benefit between a hierarchical design and a core-periphery design. [fact; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

Nagappan and Ball report on Windows Server 2003 that relative code churn measures predict defect density and discriminate fault-prone from non-fault-prone binaries with 89% accuracy, whereas absolute churn predicts poorly. [fact; source: https://ieeexplore.ieee.org/document/1553571] The outcome predicted is defect density, so churn is an indicator of defect-related cost rather than a direct measure of change effort. [inference; source: https://ieeexplore.ieee.org/document/1553571]

Access note: Nagappan and Ball abstract-level content only; full text not read.

**Q2b. Controlled and survey evidence.**

Sjøberg and colleagues had six professional developers perform maintenance tasks on four functionally equivalent Java systems and modify 298 files; none of 12 code smells was significantly associated with increased effort after adjusting for file size and number of changes, and file size and number of changes explained almost all modelled variation. [fact; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] A code smell is a surface code pattern assumed to indicate poor design. [fact; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf]

Tornhill and Borg's code-health association and Sjøberg's null smell result use different quality constructs, so they do not directly contradict each other. [inference; source: https://arxiv.org/abs/2203.04374; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf]

Jaspan and Green explored 117 candidate metrics against engineer-reported technical debt at Google and report that no single metric predicted reports, linear regression predicted under 1% of variance, and random forest models had above 80% precision with 10% to 25% recall. [fact; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf]

**Q2c. Compounding.**

Besker, Martini, and Bosch surveyed 43 developers longitudinally with follow-up interviews of 16 practitioners and report that developers waste on average 23% of development time due to technical debt and are frequently forced to introduce new debt because of existing debt. [fact; source: https://research.chalmers.se/en/publication/507477] The wasted-time figure is self-reported, so it measures perceived cost. [inference; source: https://research.chalmers.se/en/publication/507477]

Lenarduzzi and colleagues followed a 280,000-line project over more than four years and report that, after an initial spike, debt measured with SonarQube grew more slowly in extracted microservices than in the monolith. [fact; source: https://arxiv.org/abs/1902.06282]

The repository trend item reports 84% relative growth in short-cycle churn in one dataset between 2020 and 2024, which is a velocity-and-quality trend, not an exposure-response estimate for shortcuts. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md]

Search outcome: query "shortcut technical debt interest compounding rate longitudinal measured exposure" found no study that defines shortcut exposure numerically and estimates a compounding rate; result = not found within the sources examined.

Taken together, the self-reported feedback mechanism and one slower-growth case support a qualitative compounding mechanism but not a rate. [inference; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282]

**Q3. Architecture styles.**

Villamizar and colleagues compared one web application deployed as a monolith, as customer-operated microservices, and as provider-operated services (Amazon Web Services (AWS) Lambda) and report lower infrastructure cost for microservices, with reductions of 70% or more for the provider-operated variant. [fact; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/] The measure is infrastructure cost, so it speaks to run-state cost and not to change friction. [inference; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/]

Lenarduzzi and colleagues measure code-level debt in one company's migration and not infrastructure cost. [inference; source: https://arxiv.org/abs/1902.06282]

No examined study measures both infrastructure cost and change effort on the same systems across architecture styles. [inference; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282]

MacCormack and Sturtevant find that coupling structure within a system explains where maintenance cost falls, which shifts the explanatory weight from deployment style toward dependency structure. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

The architecture portfolio item concludes that smaller cohesive systems reduce mutation cost only when boundaries are well drawn and governance is mature, and that a modular monolith (a single deployable system with enforced internal module boundaries) remains an open comparison. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md]

The throughput item finds no universal coefficient for how fast unmet demand accumulates, which parallels the absence of a compounding rate here. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md]

The code entropy item lists change coupling and short-term churn among early-warning signals, consistent with the coupling findings above. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

### §3 Reasoning

1. Delivery-time metrics are measured in time, and CoD is defined in currency per time. [fact; source: https://dora.dev/guides/dora-metrics/]
2. A CoD estimate therefore needs an external value-decay input that no examined delivery dataset supplies. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay; https://dora.dev/guides/dora-metrics/]
3. Defect-related activity is both a recurring ownership cost and a modification effort, so it overlaps FCO and FCC. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]
4. Structural-condition standards describe state, whereas FCO and FCC describe future cost, so each standard-based measure needs an empirical link to cost. [inference; source: https://quality.arc42.org/standards/iso-5055; https://arxiv.org/abs/2203.04374]
5. The compounding claim lacks a measured exposure variable and a longitudinal rate in the examined set. [inference; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282]
6. The architecture comparison mixes infrastructure cost and code-debt outcomes from different systems, so no style-level ranking follows. [inference; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282]

### §4 Consistency Check

Smells versus code health: Sjøberg's null result for 12 smells and Tornhill's strong association for code-health scores concern different constructs, studies, and designs. [inference; source: https://arxiv.org/abs/2203.04374; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf]

```text
contradiction_scan: resolved (different constructs; both retained at medium confidence)
confidence_adjustment: single-study claims kept at medium; no two sources from one organisation counted as independent
scope_guardrail: no universal compounding rate or architecture ranking claimed
```

### §5 Depth and Breadth Expansion

Technical lens: file size and change count explained most effort variance in the one controlled experiment, so any FCC indicator should be tested against these baselines before it is credited. [inference; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] Coupling-based indicators add information about where cost concentrates. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

Economic lens: CoD, FCO, and FCC have different cash-flow shapes, since CoD accrues while a change waits and FCO and FCC accrue after release. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf] A shortcut that cuts delay can therefore raise later cost, and the trade is decidable only when all three are on one currency scale. [inference; source: https://en.wikipedia.org/wiki/Cost_of_delay; https://arxiv.org/abs/2203.04374]

Behavioural lens: engineer-perceived debt is weakly predicted by existing metrics, so perception data and metric data capture different things. [inference; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf] Self-reported wasted time is therefore a separate indicator, not a validated proxy for FCC. [inference; source: https://research.chalmers.se/en/publication/507477; https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf]

Historical lens: the debt idea describes expedient design decisions that raise future maintenance and adaptation cost. [fact; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf] That definition makes FCO and FCC the natural cost-side constructs of debt. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

### §6 Synthesis

**Executive summary:**

No examined study validates a measure of CoD, FCO, or FCC as a cost construct, and the best-supported measures are proxies: elapsed-time metrics for delay, defect-related activity for ownership cost, and file size, change count, and coupling for change effort. [inference; source: https://dora.dev/guides/dora-metrics/; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The evidence supports a qualitative claim that debt feeds back into more debt, based on self-reported data and one slower-growth case, but no study estimates a compounding rate. [inference; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282] Architecture-style evidence mixes infrastructure cost and code-debt outcomes from different systems, so run cost and change friction cannot be shown to move together or apart. [inference; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282]

**Key findings:**

1. Elapsed-time metrics such as DORA change lead time and failed deployment recovery time measure duration, while Cost of Delay is currency per unit time, so these metrics are inputs to a delay-cost calculation and not CoD itself. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://en.wikipedia.org/wiki/Cost_of_delay)
2. Across 39 proprietary codebases, low-quality code showed 15 times more defects, 124% more development time per issue, and 9 times longer maximum cycle times, but the design is cross-sectional and relies on one commercial code-health tool. ([fact]; medium confidence; source: https://arxiv.org/abs/2203.04374)
3. In a controlled maintenance experiment with six developers, none of 12 code smells was significantly associated with higher effort after adjusting for file size and number of changes, which together explained almost all modelled variation. ([fact]; medium confidence; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf)
4. Tightly coupled core components generated significantly more defect-related activity than peripheral components in two systems of more than 20,000 components each, and refactoring benefits differed between hierarchical and core-periphery designs. ([fact]; medium confidence; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf)
5. Among 117 candidate metrics tested against engineer-reported technical debt at Google, no single metric predicted reports and linear models explained under 1% of variance, so metric bundles are unvalidated as stand-ins for perceived cost. ([fact]; medium confidence; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf)
6. Developers reported wasting 23% of development time on technical debt and being forced to add new debt because of existing debt, and one four-year case showed slower debt growth after microservice extraction, yet neither study estimates a compounding rate. ([inference]; medium confidence; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282)
7. The one cost comparison across architecture styles reports infrastructure savings of 70% or more for provider-operated services, while the one debt study measures code-level debt, so neither addresses both run-state cost and change friction on the same system. ([inference]; medium confidence; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282)
8. Relative code churn predicted defect density in Windows Server 2003 with 89% discrimination accuracy while absolute churn did not, so churn indicates defect risk and not directly the effort of a change. ([fact]; medium confidence; source: https://ieeexplore.ieee.org/document/1553571)
9. ISO/IEC 25010 maintainability sub-characteristics, ISO/IEC 5055 weakness counts, and COCOMO II cost drivers describe structural condition or estimation inputs rather than realised cost, so each needs an empirical link to FCO or FCC before use. ([inference]; low confidence; source: https://quality.arc42.org/standards/iso-25010; https://quality.arc42.org/standards/iso-5055; https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html)

**Metric map:**

| Construct | Measure | Status | Basis |
|---|---|---|---|
| CoD | Change lead time, recovery time | [inference] Supported as elapsed-delay input; unsupported as monetised CoD | https://dora.dev/guides/dora-metrics/; https://en.wikipedia.org/wiki/Cost_of_delay |
| CoD | SLA non-compliance cost | [assumption] Ambiguous; not measured in examined studies | https://en.wikipedia.org/wiki/Cost_of_delay |
| FCO | Defect density, defect-related activity | [inference] Supported proxy; cross-sectional evidence only | https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf |
| FCO | Failed-deployment rate, recovery time | [inference] Ambiguous; delivery instability, link to ownership cost not tested | https://dora.dev/guides/dora-metrics/ |
| FCO | Self-reported wasted time | [inference] Ambiguous; perceived cost | https://research.chalmers.se/en/publication/507477 |
| FCC | File size, number of changes | [inference] Supported in one controlled experiment | https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf |
| FCC | Coupling, change propagation | [inference] Supported for defect-related maintenance in two systems | https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf |
| FCC | Relative code churn | [inference] Ambiguous; predicts defects, not change effort | https://ieeexplore.ieee.org/document/1553571 |
| FCC | Code smells | [inference] Unsupported by the controlled evidence examined | https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf |
| FCC | Cyclomatic complexity, modification blast radius | [assumption] Untested in the examined set | https://quality.arc42.org/standards/iso-5055 |

**Evidence map:** see Findings.

**Assumptions:**

Delivery-time and defect measures are treated as inputs to monetised constructs rather than as the constructs. [assumption; source: https://dora.dev/guides/dora-metrics/] The treatment follows from DORA defining its metrics in time units and ratios. [assumption; source: https://dora.dev/guides/dora-metrics/]

The examined sources approximate the published evidence base because the search used a general web engine and not the four named databases. [assumption; source: https://arxiv.org/abs/2203.04374] The approximation is reasonable because the sources are peer-reviewed or primary reports, but coverage is unmeasured. [assumption; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

**Analysis:**

Cross-sectional associations (Tornhill and Borg, MacCormack and Sturtevant) and the controlled experiment (Sjøberg and colleagues) answer different questions, and the item keeps all three at medium confidence. [inference; source: https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] A rival reading holds that all debt indicators track size, since size and change count explained most effort variance. [inference; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The coupling result partly answers that rival because it identifies where cost concentrates within systems of similar size. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf] A modular monolith is a plausible rival to microservices for change friction, but no examined study measures it. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md]

**Risks, gaps, uncertainties:**

The named databases were not queried directly, so coverage of the literature is unmeasured. [assumption; source: https://arxiv.org/abs/2203.04374] McCabe (1976) and Chidamber and Kemerer (1994) are listed as starting points but no effect size from them is used. [assumption; source: https://doi.org/10.1109/TSE.1976.233837] Effect sizes come from heterogeneous designs and are not pooled. [inference; source: https://arxiv.org/abs/2203.04374; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The Jaspan and Green text was read from a mirror of the article. [assumption; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf]

**Open questions:**

Which monetised value-decay data can be paired with change lead time to estimate CoD? Does any longitudinal repository study estimate change-effort growth against a measured shortcut exposure? How do modular monoliths compare with microservices on both run-state cost and change effort in the same organisation?

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
```

---

## Findings

### Executive Summary

No examined study validates a measure of Cost of Delay (CoD), Future Cost of Ownership (FCO), or Future Cost of Change (FCC) as a cost construct, and the best-supported measures are proxies: elapsed-time metrics for delay, defect-related activity for ownership cost, and file size, change count, and coupling for change effort. [inference; source: https://dora.dev/guides/dora-metrics/; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The evidence supports a qualitative claim that debt feeds back into more debt, based on self-reported data and one slower-growth case, but no study estimates a compounding rate. [inference; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282] Architecture-style evidence mixes infrastructure cost and code-debt outcomes from different systems, so run cost and change friction cannot be shown to move together or apart. [inference; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282]

### Key Findings

1. Elapsed-time metrics such as DORA change lead time and failed deployment recovery time measure duration, while Cost of Delay is currency per unit time, so these metrics are inputs to a delay-cost calculation and not CoD itself. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://en.wikipedia.org/wiki/Cost_of_delay)
2. Across 39 proprietary codebases, low-quality code showed 15 times more defects, 124% more development time per issue, and 9 times longer maximum cycle times, but the design is cross-sectional and relies on one commercial code-health tool. ([fact]; medium confidence; source: https://arxiv.org/abs/2203.04374)
3. In a controlled maintenance experiment with six developers, none of 12 code smells was significantly associated with higher effort after adjusting for file size and number of changes, which together explained almost all modelled variation. ([fact]; medium confidence; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf)
4. Tightly coupled core components generated significantly more defect-related activity than peripheral components in two systems of more than 20,000 components each, and refactoring benefits differed between hierarchical and core-periphery designs. ([fact]; medium confidence; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf)
5. Among 117 candidate metrics tested against engineer-reported technical debt at Google, no single metric predicted reports and linear models explained under 1% of variance, so metric bundles are unvalidated as stand-ins for perceived cost. ([fact]; medium confidence; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf)
6. Developers reported wasting 23% of development time on technical debt and being forced to add new debt because of existing debt, and one four-year case showed slower debt growth after microservice extraction, yet neither study estimates a compounding rate. ([inference]; medium confidence; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282)
7. The one cost comparison across architecture styles reports infrastructure savings of 70% or more for provider-operated services, while the one debt study measures code-level debt, so neither addresses both run-state cost and change friction on the same system. ([inference]; medium confidence; source: https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282)
8. Relative code churn predicted defect density in Windows Server 2003 with 89% discrimination accuracy while absolute churn did not, so churn indicates defect risk and not directly the effort of a change. ([fact]; medium confidence; source: https://ieeexplore.ieee.org/document/1553571)
9. ISO/IEC 25010 maintainability sub-characteristics, ISO/IEC 5055 weakness counts, and COCOMO II cost drivers describe structural condition or estimation inputs rather than realised cost, so each needs an empirical link to FCO or FCC before use. ([inference]; low confidence; source: https://quality.arc42.org/standards/iso-25010; https://quality.arc42.org/standards/iso-5055; https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html)

### Metric Map

| Construct | Measure | Status | Basis |
|---|---|---|---|
| CoD | Change lead time, recovery time | [inference] Supported as elapsed-delay input; unsupported as monetised CoD | https://dora.dev/guides/dora-metrics/; https://en.wikipedia.org/wiki/Cost_of_delay |
| CoD | SLA non-compliance cost | [assumption] Ambiguous; not measured in examined studies | https://en.wikipedia.org/wiki/Cost_of_delay |
| FCO | Defect density, defect-related activity | [inference] Supported proxy; cross-sectional evidence only | https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf |
| FCO | Failed-deployment rate, recovery time | [inference] Ambiguous; delivery instability, link to ownership cost not tested | https://dora.dev/guides/dora-metrics/ |
| FCO | Self-reported wasted time | [inference] Ambiguous; perceived cost | https://research.chalmers.se/en/publication/507477 |
| FCC | File size, number of changes | [inference] Supported in one controlled experiment | https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf |
| FCC | Coupling, change propagation | [inference] Supported for defect-related maintenance in two systems | https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf |
| FCC | Relative code churn | [inference] Ambiguous; predicts defects, not change effort | https://ieeexplore.ieee.org/document/1553571 |
| FCC | Code smells | [inference] Unsupported by the controlled evidence examined | https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf |
| FCC | Cyclomatic complexity, modification blast radius | [assumption] Untested in the examined set | https://quality.arc42.org/standards/iso-5055 |

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Elapsed-time metrics are inputs to CoD, not CoD | https://dora.dev/guides/dora-metrics/; https://en.wikipedia.org/wiki/Cost_of_delay | medium | definition from tertiary source |
| [fact] Low-quality code: 15x defects, 124% more time, 9x max cycle time | https://arxiv.org/abs/2203.04374 | medium | cross-sectional; single tool |
| [fact] 12 smells not associated with effort after size and changes | https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf | medium | six developers, four systems |
| [fact] Coupled core components cost more defect-related activity | https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf | medium | two systems |
| [fact] No single metric predicted perceived debt | https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf | medium | 117 metrics; mirror copy |
| [inference] Compounding mechanism supported, rate not | https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282 | medium | self-report; one case |
| [inference] Run cost and change friction not measured together | https://research.tue.nl/en/publications/cost-comparison-of-running-web-applications-in-the-cloud-using-mo/; https://arxiv.org/abs/1902.06282 | medium | absence within examined set |
| [fact] Relative churn predicts defect density | https://ieeexplore.ieee.org/document/1553571 | medium | abstract-level read |
| [inference] Standards describe condition or estimates, not realised cost | https://quality.arc42.org/standards/iso-25010; https://quality.arc42.org/standards/iso-5055; https://msdbok.github.io/content/scope/estimates/cocomo_ii_drivers.html | low | secondary summaries |

### Assumptions

Delivery-time and defect measures are treated as inputs to monetised constructs rather than as the constructs. [assumption; source: https://dora.dev/guides/dora-metrics/] The treatment follows from DORA defining its metrics in time units and ratios. [assumption; source: https://dora.dev/guides/dora-metrics/]

The examined sources approximate the published evidence base because the search used a general web engine and not the four named databases. [assumption; source: https://arxiv.org/abs/2203.04374] The approximation is reasonable because the sources are peer-reviewed or primary reports, but coverage is unmeasured. [assumption; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf]

### Analysis

Cross-sectional associations (Tornhill and Borg, MacCormack and Sturtevant) and the controlled experiment (Sjøberg and colleagues) answer different questions, and the item keeps all three at medium confidence. [inference; source: https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] A rival reading holds that all debt indicators track size, since size and change count explained most effort variance. [inference; source: https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The coupling result partly answers that rival because it identifies where cost concentrates within systems of similar size. [inference; source: https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf] A modular monolith is a plausible rival to microservices for change friction, but no examined study measures it. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-21-monolith-vs-cohesive-portfolio-tco.md] Prior repository work on code entropy, repository velocity, and throughput supplies churn and coupling signals and a parallel absence of universal coefficients, which this item neither overturns nor extends with new rates. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-ai-code-entropy-quality-metrics.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-29-commit-trends-repo-velocity-rework-abandonment.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-it-throughput-constraint-magnitude-and-debt-accumulation-rate.md]

### Risks, Gaps, and Uncertainties

The named databases were not queried directly, so coverage of the literature is unmeasured. [assumption; source: https://arxiv.org/abs/2203.04374] McCabe (1976) and Chidamber and Kemerer (1994) are listed as starting points but no effect size from them is used. [assumption; source: https://doi.org/10.1109/TSE.1976.233837] Effect sizes come from heterogeneous designs and are not pooled. [inference; source: https://arxiv.org/abs/2203.04374; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf] The Jaspan and Green text was read from a mirror of the article. [assumption; source: https://static.isthisit.nz/artifacts/blog/Defining_Measuring_and_Managing_Technical_Debt.pdf] A failed search for a measured shortcut-exposure compounding rate leaves that claim unsupported. [inference; source: https://research.chalmers.se/en/publication/507477; https://arxiv.org/abs/1902.06282]

### Open Questions

- Which monetised value-decay data can be paired with change lead time to estimate CoD?
- Does any longitudinal repository study estimate change-effort growth against a measured shortcut exposure?
- How do modular monoliths compare with microservices on both run-state cost and change effort in the same organisation?

---

## Output

- Type: knowledge
- Description: A construct-by-construct metric map for CoD, FCO, and FCC with supported, ambiguous, and unsupported ratings, and a statement that compounding rates and architecture-style rankings are not established by the examined evidence. [inference; source: https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://research.chalmers.se/en/publication/507477]
- Links: https://arxiv.org/abs/2203.04374; https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf; https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf
