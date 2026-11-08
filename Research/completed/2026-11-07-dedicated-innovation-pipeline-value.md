---
review_count: 2
title: "What does a dedicated innovation pipeline buy organisations, and when is its overhead justified?"
added: 2026-11-07T23:40:00+00:00
status: completed
priority: high
blocks: [2026-11-07-cost-of-no-innovation-pipeline]
themes: [organisational-design, governance-policy, benchmarks-eval, enterprise-adoption, tools-infrastructure]
started: 2026-11-08T01:33:17+00:00
completed: 2026-11-08T01:39:53+00:00
output: []
cites: [2026-07-20-regulated-safe-to-fail-probing-operating-models, 2026-06-13-platform-engineering-innersource-hybrid-standardization]
related: [2026-06-13-local-tooling-fragmentation-threshold-measurement, 2026-06-13-standardization-customization-balance-context-ai, 2026-10-02-ideal-internal-platform-product-standard]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What does a dedicated innovation pipeline buy organisations, and when is its overhead justified?

## Research Question

What does a dedicated innovation pipeline, combining budget, a managed backlog, explicit selection, and a promotion path, add to problem-selection quality, experiment throughput, and the ability to scale improvements in medium-to-large organisations, and under what conditions do those benefits justify its overhead compared with emergent problem lodging?

## Scope

**In scope:**
- Benefits and failure modes of formal innovation pipelines, including dedicated budget, backlog ownership, selection, experimentation, promotion, and retirement.
- Evidence about problem-selection quality, learning speed or experiment throughput, and scaling successful improvements.
- Comparison with emergent problem lodging, especially where there is no dedicated pipeline or innovation budget.
- Historical and large-organisation evidence, including Bell Labs, International Business Machines (IBM), Microsoft, and contemporary experimentation platforms.
- Conditions that make formal pipeline investment worthwhile or counterproductive for knowledge work and process improvement.

**Out of scope:**
- Pure statistical design of online controlled experiments.
- Individual ideation techniques.
- Detailed implementation of experiment platforms.

**Constraints:** Prefer primary and independently corroborated evidence where available. Distinguish historical institutional practices from evidence about modern organisations and avoid treating the examples as directly comparable without qualification.

## Context

Organisations may invest in formal innovation structures to improve selection and scaling, but the investment only informs operating-model choices if its additional value can be distinguished from the overhead and compared with emergent alternatives.

## Approach

1. Define the constituent practices of a dedicated innovation pipeline and distinguish them from ad hoc or emergent improvement routes.
2. Examine mechanisms through which formal budgets, portfolio selection, and dedicated ownership may improve the quality and coverage of problems selected.
3. Assess evidence on experiment throughput, learning speed, and promotion or retirement pathways, including failure modes that reduce these benefits.
4. Compare historical evidence from Bell Labs and International Business Machines (IBM), evidence from Microsoft, and contemporary large-scale experimentation-platform practice; verify each case with sources appropriate to its time and claims.
5. Identify contextual conditions, such as scale, coordination costs, risk, available authority, or volume of improvement opportunities, under which pipeline benefits plausibly justify their overhead.
6. Prepare comparison dimensions that can be used by the dependent loss question to assess the emergent-only path.

## Sources

- [Garvin and Levesque (2004) Emerging Business Opportunities at IBM (A), Harvard Business School case 304-075](https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
- [Fabijan et al. (2017) The Evolution of Continuous Experimentation in Software Product Development, International Conference on Software Engineering (ICSE) 2017](https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf)
- [Microsoft Bing (2013) Large Scale Experimentation at Bing](https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/)
- [Chesbrough (2003) The governance and performance of Xerox's technology spin-off companies, Research Policy](https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies)
- [Burgelman (1991) Intraorganizational Ecology of Strategy Making and Organizational Adaptation, Organization Science](https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation)
- [Computer History Museum (2007) 1952: Bell Labs Licenses Transistor Technology](https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/)
- [Governance and operating models for safe-to-fail experimentation in regulated industries](https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
- [Platform engineering, InnerSource, and standard-core plus local-extension operating models](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [Local tooling fragmentation threshold measurement](https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html)
- [Standardization and customization balance across context and Artificial Intelligence (AI) adoption](https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html)
- [Ideal internal platforms as products: an assessable operating standard](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html)

---

## Research Skill Output

*(Full output from running the research skill - retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
question: what a dedicated innovation pipeline (budget, managed backlog, explicit selection, promotion path) adds over emergent problem lodging, and when overhead is justified
scope: formal pipelines, selection quality, experiment throughput, scaling; IBM, Bell Labs, Microsoft, Xerox, Intel; excludes statistical experiment design and ideation techniques
constraints: historical cases (Bell Labs, IBM 2000s) kept separate from contemporary evidence; no source located that measures pipeline versus emergent outcomes head to head
output: knowledge
```

Prior completed items checked in `Research/completed/` before investigation. The regulated safe-to-fail item reports that the Food and Drug Administration (FDA) Digital Health Software Precertification (Pre-Cert) pilot generated learning but could not scale because authority sat above the pilot's design, which bears on the promotion-path question. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html] The platform engineering and InnerSource item argues that opinionated default paths with permitted deviation preserve local agility, which bears on how much a pipeline should centralise. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]

Working hypothesis: a pipeline's main contribution is protected funding plus a promotion path rather than better ex ante selection. [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

### §1 Question Decomposition

```text
Q1 constituent practices
  Q1a what practices did IBM's formal Emerging Business Opportunity (EBO) system contain
  Q1b what did IBM lack before it
Q2 selection quality
  Q2a how reliably do ideas deliver value when tested
Q3 throughput, promotion, retirement
  Q3a how does experiment volume scale at Microsoft
  Q3b what happens at the promotion boundary (Xerox spin-offs, Bell Labs transfer)
  Q3c what failure modes appear
Q4 rival: emergent lodging
  Q4a what does Intel's autonomous strategic process show
Q5 conditions for justification
Q6 comparison dimensions for the dependent loss question
```

### §2 Investigation

**Q1: constituent practices and the pre-pipeline baseline.**

The IBM case describes a pre-pipeline baseline in which new businesses needed cooperation from many parts of a matrix of seven groups and 39 business units. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] A promising optical-laser components business from the Zurich research lab was sold because the Microelectronics Division would not support scaling it. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] A senior IBM executive observed that an idea had a chance to scale only if it became the passion of a senior person. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] IBM executives listed among their diagnosed problems the absence of established disciplines for selecting, experimenting, funding, and terminating new growth businesses, and noted that new ideas lacked sponsorship and were often the first programmes cut when budgets tightened. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

An earlier corporate venture fund failed in a specific way: managers from the groups tried to fund ideas with loose, back-of-the-envelope business plans, which a senior executive called "bowling for dollars". [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] A dedicated budget without selection discipline therefore did not by itself produce a working pipeline in this case. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

The EBO system that followed protected funding once a business was selected, held monthly reviews of each corporate EBO, and kept a separate corporate pool of funds (initially $100 million) used as a last resort with matching funds required from divisions. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Funding meetings could be brief (one general manager recalled a 30-minute discussion for tens of millions of dollars) because rigorous financial analysis was judged meaningless for embryonic markets. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

**Q1/Q3c: what the IBM system produced.**

By the case date, 18 EBOs had been identified, funded, and shepherded. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] In early 2003 the corporate team rated 12 of 18 corporate EBOs green on developing a clear strategy, but only four green on an executable model and two green on winning in the marketplace. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] The ratings pattern suggests that the pipeline was better at getting businesses started and funded than at converting them into market wins at that date. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

The leaders spent substantial executive time on the system: one senior executive devoted about one-third of his time to the effort, and the case records the chief executive's concern about whether results could be sustained as EBOs multiplied. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Senior attention is therefore a cost that scales with portfolio size. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

**Q2: selection quality.**

Microsoft's Bing experimentation team reported that when ideas are evaluated in a controlled experiment, less than a third move the metrics they were designed to improve, and in an optimised domain the share is lower. [fact; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/]

If most ideas do not deliver, ex ante selection by committee has limited power and the value of a pipeline lies in cheap, fast testing and in retiring losers. [inference; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/] This is a Microsoft web-product result and does not transfer directly to process-improvement ideas in other knowledge work. [assumption; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

**Q3a: throughput at Microsoft.**

Fabijan et al. describe a growth model with four phases, crawl, walk, run, and fly, and report that teams at Bing conduct over 10,000 experiments per year and set up, execute, and analyse them autonomously without help from the central Analysis and Experimentation data scientists. [fact; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] The same paper states that scaling beyond 100 data-driven experiments per year needs the experimentation platform to be extended beyond the power analysis and pre-experiment checks comparing identical variants of the walk phase. [fact; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] In the fly phase the overall evaluation criterion (OEC, the quantitative measure of success for an experiment) changes only periodically, for example once per year, under a standardised process, giving independent teams a stable target. [fact; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

High throughput at Microsoft therefore came from a shared platform and a stable evaluation criterion with federated experiment ownership, rather than from a central team approving each idea. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] The Bing blog and the conference paper both originate from Microsoft's experimentation group, so they are one evidence family. [fact; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

**Q3b: the promotion boundary.**

Chesbrough analysed 35 spin-off organisations from Xerox and reported that Xerox's initial equity position correlated negatively with spin-off performance, that spin-offs with a higher share of venture capital investors on their boards performed better, and that spin-offs with a Xerox insider as chief executive officer performed worse. [fact; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies] Qualitative interviews in the same study suggest that Xerox's practices pushed spin-offs to search locally near Xerox's own business. [fact; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies] The promotion path can therefore reduce value when the parent's governance constrains what a promoted idea may become. [inference; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies]

For Bell Labs, the Computer History Museum records that in April 1952 over 100 representatives from 40 companies that had paid a $25,000 patent-licensing fee attended a nine-day transistor symposium, and that the proceedings became a reference for the emerging semiconductor industry. [fact; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/] This documents a deliberate technology-transfer route for a research output, but it does not document pipeline overhead, selection quality, or the funding conditions of Bell Labs, and it describes a mid-twentieth-century research laboratory rather than a modern process-improvement pipeline. [inference; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/]

The FDA Pre-Cert pilot, summarised in a prior completed item, generated useful learning but concluded that scaling its oversight model would exceed existing statutory authority, which shows a promotion path blocked by authority above the pipeline. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]

**Q4: the emergent rival.**

Burgelman's field study of Intel distinguishes induced strategic processes, aligned with current strategy, from autonomous processes originating outside it. [fact; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation] The paper proposes that successful reorientations are likely to have been preceded by internal experimentation and selection through the autonomous process, and that successful organisations exercise both processes at once. [fact; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation] Emergent lodging is therefore a credible route to strategic novelty at Intel, so a formal pipeline adds value mainly where emergent routes fail to secure sponsorship, as the IBM case documents. [inference; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation; https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

**Q5/Q6: conditions and adjacent items.**

The platform engineering item argues that an opinionated default path with permitted, unsupported deviation preserves local agility, and the Microsoft federated-ownership pattern is consistent with that design. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

The fragmentation-threshold item identifies shared dependency density and administrative absorption capacity as drivers of coordination cost, which are the same conditions under which IBM's matrix blocked cross-unit scaling. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html; https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

The standardisation-balance item separates governance-infrastructure standardisation from task-execution standardisation, and a pipeline's shared selection and promotion rules fall on the governance-infrastructure side while idea generation stays local. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html]

The platform-as-product standard item uses a check-track-level mechanism and an eligible-team denominator for adoption measurement, which suggests pipeline reach could be measured against an eligible-team denominator as well. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html]

```text
Failed search: query "empirical comparison formal corporate innovation pipeline versus bottom-up emergent employee ideas outcomes study large firms" returned candidate studies whose abstracts could not be verified from the publisher pages in this session; none used as evidence
Failed search: no source located that measures process-improvement outcomes of a dedicated pipeline against emergent lodging in the same organisation
Access note: Nature 2022 Bell Labs article and ScienceDirect Chesbrough abstract not retrievable (status codes 406 and 403); not used
```

### §3 Reasoning

1. IBM executives diagnosed missing sponsorship and missing funding, selection, and termination disciplines before the EBO system. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]
2. The earlier venture fund shows that budget alone, without selection discipline, produced weak proposals. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]
3. Fewer than a third of ideas move their target metrics in controlled tests at Bing, so the testing and retirement function carries value that ex ante selection cannot. [inference; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/]
4. Microsoft throughput scaled through a shared platform and federated ownership. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]
5. Xerox shows that the promotion path can destroy value when parent governance constrains it. [inference; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies]
6. Intel shows emergent routes can drive reorientation, so the pipeline's marginal value is conditional on emergent routes failing. [inference; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation]

### §4 Consistency Check

The Microsoft evidence (high throughput without central approval) appears to conflict with the IBM evidence (central funding and monthly review). The conflict resolves because the two address different layers: Microsoft's cheap, reversible web experiments need a shared platform, while IBM's new-business ventures needed cross-unit authority and funding. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf; https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

```text
contradiction_scan: resolved
confidence_adjustment: no Key Finding above medium; sources are single-case or one evidence family
scope_guardrail: Bell Labs limited to transfer practice; no head-to-head claim made
```

### §5 Depth and Breadth Expansion

Economic lens: the IBM case shows overhead as senior executive time and a protected funding pool, and the case records the chief executive questioning whether support could be sustained across more EBOs. [fact; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Overhead therefore grows with the number of ventures needing senior sponsorship. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Microsoft's model shows overhead can be amortised into a platform when experiments are cheap. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

Historical lens: IBM's case dates from the early 2000s and Bell Labs' transfer example from 1952, so neither describes a modern knowledge-work improvement pipeline, and comparability is limited. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/]

Regulatory lens: the Pre-Cert outcome shows that where authority to scale sits outside the pipeline, the promotion path is the binding constraint. [inference; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]

Behavioural lens: the IBM "bowling for dollars" account shows that open budgets invite weakly specified proposals from managers, so explicit selection criteria shape proposer behaviour. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

### §6 Synthesis

**Executive summary:**

A dedicated pipeline buys protected funding and a defined sponsor, while the route from experiment to scale was the weakest part of the cases examined, and the available evidence supports the pipeline mainly where cross-unit coordination blocks emergent ideas, as in IBM's matrix. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Evidence that it improves ex ante selection is weak, because fewer than a third of ideas move their target metrics when tested at Bing. [fact; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/] High experiment throughput at Microsoft came from a shared platform with federated ownership rather than central approval. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] No source located measures a pipeline against emergent lodging head to head, so the conditions for justifying overhead are inferred from case evidence. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation]

**Key findings:**

1. Before its Emerging Business Opportunity system, IBM lacked disciplines for selecting, funding, and terminating new businesses, and ideas lacking a senior sponsor were often the first cut when budgets tightened. ([fact]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
2. IBM's earlier corporate venture fund produced loosely specified proposals, so budget without explicit selection criteria did not create a working pipeline. ([inference]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
3. After 18 EBOs were funded, only two were rated green on winning in the marketplace in early 2003, so the pipeline's early yield was stronger at funding than at scaling. ([inference]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
4. Microsoft's Bing team reported that fewer than a third of ideas move their target metrics in controlled tests, which limits what ex ante selection can add relative to cheap testing and retirement. ([inference]; medium confidence; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/)
5. Bing teams run over 10,000 experiments per year autonomously on a shared platform with a periodically changed evaluation criterion, so throughput came from platform and federation rather than central approval. ([inference]; medium confidence; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf)
6. Across 35 Xerox spin-offs, a Xerox insider as chief executive correlated with lower performance and venture capital board share with higher performance. ([fact]; medium confidence; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies) Parent governance of the promotion path can therefore reduce the value of promoted ideas. ([inference]; medium confidence; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies)
7. Burgelman's Intel study proposes that successful reorientations were preceded by internal experimentation through an autonomous process. ([fact]; medium confidence; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation) Emergent lodging can therefore deliver strategic novelty where sponsors exist. ([inference]; medium confidence; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation)
8. The Bell Labs 1952 transistor symposium documents a deliberate paid transfer route for research output but says nothing about overhead or selection, so it is weak evidence for the cost-benefit question. ([inference]; medium confidence; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/)
9. The FDA Pre-Cert pilot generated learning but could not scale because authority sat above the pilot, so a promotion path needs authority to scale, not only a budget. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
10. Pipeline overhead is most plausibly justified where ideas cross unit boundaries, sponsorship is scarce, and experiment volume is high enough to amortise shared tooling, and least justified for cheap single-team changes. ([inference]; low confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] IBM lacked selection, funding, termination disciplines; ideas lacked sponsorship | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | single case |
| [inference] Budget without selection criteria did not work at IBM | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | single case |
| [inference] EBO yield stronger at funding than scaling | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | 2003 ratings |
| [inference] Under a third of ideas move metrics, limiting ex ante selection | https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/ | medium | web product |
| [inference] Throughput from platform and federation | https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf | medium | same vendor family |
| [fact] Xerox insider chief executive and venture capital board share correlate with spin-off performance | https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies | medium | 35 spin-offs |
| [fact] Autonomous process precedes reorientation at Intel | https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation | medium | single firm |
| [inference] Bell Labs transfer is weak cost-benefit evidence | https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/ | medium | historical |
| [inference] Promotion needs authority to scale | https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html | medium | prior item |
| [inference] Conditions that justify overhead | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf | low | synthesis |

**Assumptions:**

The Microsoft web-product results are assumed to inform other knowledge-work contexts only as a pattern, not as transferable rates. [assumption; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] That assumption is reasonable because the sources report Microsoft's own products and no study located reports rates for process-improvement ideas. [assumption; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/]

The IBM case is assumed to be representative of large matrix organisations. [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] That assumption rests on the case describing a general pattern of missing sponsorship, but it remains one firm. [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

**Analysis:**

The evidence supports a narrow claim: a pipeline substitutes protected funding and a defined sponsor for the ad hoc senior-executive sponsorship that, in the IBM case, determined whether an idea had a chance to scale. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Emergent lodging remains a credible rival because Intel's strategic reorientation emerged through an autonomous process. [inference; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation] A rival remedy, investing in shared tooling instead of adding a selection layer, is consistent with the Microsoft pattern, where platform investment rather than approval layers drove throughput. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] The IBM case outweighs the other evidence on the funding and sponsorship question because it is the only source here that directly describes both the baseline and the formal system. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Adjacent completed work on golden paths, fragmentation thresholds, and adoption measurement suggests that the pipeline's shared rules should sit at the governance layer while ideas stay local. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html; https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html]

Comparison dimensions for the dependent loss question: sponsorship availability for cross-unit ideas, protection of funding under budget pressure, existence of a termination mechanism, experiment cost and volume, authority to scale, and executive time per venture. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

**Risks, gaps, uncertainties:**

No located source measures a dedicated pipeline against emergent lodging within the same organisation. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] The Bell Labs evidence covers only a technology-transfer episode and not funding or selection. [inference; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/] The Microsoft sources share an origin, and the IBM and Xerox evidence is single-case or correlational. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf; https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies]

**Open questions:**

What does the loss from lacking a pipeline look like in observable terms for process-improvement ideas? [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] What lightweight pipeline subset, for example only protected funding and a sponsor, captures most of the benefit? [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
```

---

## Findings

### Executive Summary

A dedicated pipeline buys protected funding and a defined sponsor, while the route from experiment to scale was the weakest part of the cases examined, and the available evidence supports the pipeline mainly where cross-unit coordination blocks emergent ideas, as in IBM's matrix. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Evidence that it improves ex ante selection is weak, because fewer than a third of ideas move their target metrics when tested at Bing. [fact; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/] High experiment throughput at Microsoft came from a shared platform with federated ownership rather than central approval. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] No source located measures a pipeline against emergent lodging head to head, so the conditions for justifying overhead are inferred from case evidence. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation]

### Key Findings

1. Before its Emerging Business Opportunity system, IBM lacked disciplines for selecting, funding, and terminating new businesses, and ideas lacking a senior sponsor were often the first cut when budgets tightened. ([fact]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
2. IBM's earlier corporate venture fund produced loosely specified proposals, so budget without explicit selection criteria did not create a working pipeline. ([inference]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
3. After 18 EBOs were funded, only two were rated green on winning in the marketplace in early 2003, so the pipeline's early yield was stronger at funding than at scaling. ([inference]; medium confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf)
4. Microsoft's Bing team reported that fewer than a third of ideas move their target metrics in controlled tests, which limits what ex ante selection can add relative to cheap testing and retirement. ([inference]; medium confidence; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/)
5. Bing teams run over 10,000 experiments per year autonomously on a shared platform with a periodically changed evaluation criterion, so throughput came from platform and federation rather than central approval. ([inference]; medium confidence; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf)
6. Across 35 Xerox spin-offs, a Xerox insider as chief executive correlated with lower performance and venture capital board share with higher performance. ([fact]; medium confidence; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies) Parent governance of the promotion path can therefore reduce the value of promoted ideas. ([inference]; medium confidence; source: https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies)
7. Burgelman's Intel study proposes that successful reorientations were preceded by internal experimentation through an autonomous process. ([fact]; medium confidence; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation) Emergent lodging can therefore deliver strategic novelty where sponsors exist. ([inference]; medium confidence; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation)
8. The Bell Labs 1952 transistor symposium documents a deliberate paid transfer route for research output but says nothing about overhead or selection, so it is weak evidence for the cost-benefit question. ([inference]; medium confidence; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/)
9. The FDA Pre-Cert pilot generated learning but could not scale because authority sat above the pilot, so a promotion path needs authority to scale, not only a budget. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
10. Pipeline overhead is most plausibly justified where ideas cross unit boundaries, sponsorship is scarce, and experiment volume is high enough to amortise shared tooling, and least justified for cheap single-team changes. ([inference]; low confidence; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] IBM lacked selection, funding, termination disciplines; ideas lacked sponsorship | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | single case |
| [inference] Budget without selection criteria did not work at IBM | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | single case |
| [inference] EBO yield stronger at funding than scaling | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf | medium | 2003 ratings |
| [inference] Under a third of ideas move metrics, limiting ex ante selection | https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/ | medium | web product |
| [inference] Throughput from platform and federation | https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf | medium | same vendor family |
| [fact] Xerox insider chief executive and venture capital board share correlate with spin-off performance | https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies | medium | 35 spin-offs |
| [fact] Autonomous process precedes reorientation at Intel | https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation | medium | single firm |
| [inference] Bell Labs transfer is weak cost-benefit evidence | https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/ | medium | historical |
| [inference] Promotion needs authority to scale | https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html | medium | prior item |
| [inference] Conditions that justify overhead | https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf | low | synthesis |

### Assumptions

The Microsoft web-product results are assumed to inform other knowledge-work contexts only as a pattern, not as transferable rates. [assumption; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] That assumption is reasonable because the sources report Microsoft's own products and no study located reports rates for process-improvement ideas. [assumption; source: https://blogs.bing.com/search-quality-insights/2013/8/Large-Scale-Experimentation-at-Bing/]

The IBM case is assumed to be representative of large matrix organisations. [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] That assumption rests on the case describing a general pattern of missing sponsorship, but it remains one firm. [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

### Analysis

The evidence supports a narrow claim: a pipeline substitutes protected funding and a defined sponsor for the ad hoc senior-executive sponsorship that, in the IBM case, determined whether an idea had a chance to scale. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Emergent lodging remains a credible rival because Intel's strategic reorientation emerged through an autonomous process. [inference; source: https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation] A rival remedy, investing in shared tooling instead of adding a selection layer, is consistent with the Microsoft pattern, where platform investment rather than approval layers drove throughput. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf] The IBM case outweighs the other evidence on the funding and sponsorship question because it is the only source here that directly describes both the baseline and the formal system. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf] Adjacent completed work on golden paths, fragmentation thresholds, and adoption measurement suggests that the pipeline's shared rules should sit at the governance layer while ideas stay local. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html; https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html; https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html]

Comparison dimensions for the dependent loss question: sponsorship availability for cross-unit ideas, protection of funding under budget pressure, existence of a termination mechanism, experiment cost and volume, authority to scale, and executive time per venture. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf]

### Risks, Gaps, and Uncertainties

- No located source measures a dedicated pipeline against emergent lodging within the same organisation. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]
- The Bell Labs evidence covers only a technology-transfer episode and not funding or selection. [inference; source: https://www.computerhistory.org/siliconengine/bell-labs-licenses-transistor-technology/]
- The Microsoft sources share an origin, and the IBM and Xerox evidence is single-case or correlational. [inference; source: https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf; https://www.academia.edu/120648458/The_governance_and_performance_of_Xerox_s_technology_spin_off_companies]

### Open Questions

- What does the loss from lacking a pipeline look like in observable terms for process-improvement ideas? [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]
- What lightweight pipeline subset, for example only protected funding and a sponsor, captures most of the benefit? [assumption; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]

---

## Output

- Type: knowledge
- Description: Evidence synthesis on the value and overhead conditions of a dedicated innovation pipeline, with comparison dimensions for the dependent loss question. [inference; source: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf]
- Links: https://www.elkarbide.com/sites/default/files/ibm_ebo_1.pdf; https://exp-platform.com/Documents/2017-05%20ICSE2017_EvolutionOfExP.pdf; https://www.gsb.stanford.edu/faculty-research/publications/intraorganizational-ecology-strategy-making-organizational-adaptation

## Related

- [Governance and operating models for safe-to-fail experimentation in regulated industries](https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
- [At what scale or under what operating conditions do the aggregate costs of fragmented local tooling exceed the productivity gains from customization, and which metrics let organisations detect that crossover early?](https://davidamitchell.github.io/Research/research/2026-06-13-local-tooling-fragmentation-threshold-measurement.html)
- [How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation, and which patterns most reliably preserve local agility without creating fragmentation?](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)
- [How should the balance between standardized and customized internal tooling shift across industries, organisation sizes, maturity levels, and Artificial Intelligence (AI) agent adoption patterns, and what evidence exists for effects on productivity, innovation, and employee experience?](https://davidamitchell.github.io/Research/research/2026-06-13-standardization-customization-balance-context-ai.html)
- [Ideal internal platforms as products: an assessable operating standard](https://davidamitchell.github.io/Research/research/2026-10-02-ideal-internal-platform-product-standard.html)
