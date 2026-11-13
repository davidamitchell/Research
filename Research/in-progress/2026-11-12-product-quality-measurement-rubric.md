---
review_count: 1
title: "A practical product quality measurement rubric for internal platforms"
added: 2026-11-12T08:07:53+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
themes: [benchmarks-eval, software-engineering, tools-infrastructure, regulatory-compliance, organisational-design]
started: 2026-11-13T07:05:20+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites:
  - 2026-10-02-ideal-internal-platform-product-standard
  - 2026-10-01-thinnest-viable-internal-platform-standard
  - 2026-08-13-llm-consumption-maturity-ladder
  - 2026-05-31-sre-slo-threshold-justification
  - 2026-03-02-research-quality-assurance-methodology
related: []
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# A practical product quality measurement rubric for internal platforms

## Research Question

What is the most practical way to adapt and operationalise the International Organization for Standardization and International Electrotechnical Commission (ISO/IEC) 25010 Product Quality Model as a reusable, evidence-backed measurement and five-level maturity rubric for assessing and improving internal platforms and enterprise systems in knowledge-work and regulated settings?

## Scope

**In scope:**
- Actionable measurements for each of the eight requested product-quality characteristics and key sub-characteristics, using ISO/IEC 25023 formulas where applicable and identifying observable indicators, tools and data sources.
- Characteristic-level scoring criteria, evidence requirements and maturity mapping, including mappings to National Institute of Standards and Technology (NIST) and Center for Internet Security (CIS) controls and verification methods.
- Links to continuous integration and continuous delivery (CI/CD) gates, application performance monitoring (APM), telemetry, DevOps Research and Assessment (DORA) metrics, chaos and disaster recovery (DR) drills, static application security testing (SAST), dynamic application security testing (DAST), accessibility audits and architecture fitness functions.
- How scores and maturity levels inform prioritisation, investment, service level objectives (SLOs), error budgets and continuous improvement.

**Out of scope:**
- Formal certification against the ISO/IEC 25000 series and the quality-in-use model.
- Domain-specific safety-critical certification beyond the product-quality lens and green-field consumer products outside enterprise or internal-platform contexts.

**Constraints:**
- Prefer existing telemetry, delivery and operational data over a new heavy measurement programme; account for federated multi-team ownership, regulatory expectations and auditable evidence trails.
- Draw on standards, published practice and prior local research. The issue refers to a supplied summary but does not include it; recover it if available or explicitly note the gap.
- Verify the applicable editions and characteristic counts before adopting the requested eight-characteristic framing; distinguish an adapted Capability Maturity Model Integration (CMMI)-style rubric from formal appraisal. Standards may require paid access, so distinguish verified formulas from adaptations if the text is unavailable.

## Context

Platform, architecture and quality teams need a concrete way to collect evidence, score product quality and choose improvements, extending prior work on assessable internal-platform standards. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md]

## Approach

Investigate the following through standards and published-practice review, cross-checking the prior local research:

1. Which editions, characteristics and sub-characteristics are relevant, and how should differences from the requested eight-characteristic summary be handled?
2. For each characteristic, which ISO/IEC 25023 measurement functions apply, and what practical indicators, formulas, data sources and tools can supply equivalent evidence where access or telemetry is limited?
3. What five-level criteria and evidence requirements make each characteristic's score repeatable across teams, and how should missing data, ownership and audit trails be handled?
4. How can the measurements map to NIST and CIS controls and to existing tests, delivery gates, monitoring, accessibility audits and resilience drills without implying control compliance?
5. How should teams use the resulting scores, risks and maturity gaps to prioritise investment, set SLOs and error budgets, and track improvement? This depends on the measurement and scoring design in questions 2–3.

Readiness: READY, the question is specific, answerable in principle, scoped, motivated and decomposable; access to standards and the missing summary are constraints to resolve during research.

## Sources

- [x] [Ideal internal platforms as products: an assessable operating standard](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md)
- [x] [Satisfiable internal platforms: a practical standard for platform teams](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-01-thinnest-viable-internal-platform-standard.md)
- [x] [Enterprise artificial intelligence maturity frameworks and the language model consumption ladder](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md)
- [x] [Establishing service level objectives as contractual capability boundaries](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md)
- [x] [Research quality assurance methodology](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-research-quality-assurance-methodology.md)
- [x] [arc42 Quality Model Update on ISO 25010, version 2023](https://quality.arc42.org/articles/iso-25010-update-2023)
- [x] [Spree ISO/IEC 25010 News from the 2nd Edition (2023-11)](https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/)
- [x] [ISO 25000 portal ISO/IEC 25010 product quality model](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010)
- [x] [ISO/IEC 25023:2016 preview sample (iTeh Standards)](https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf)
- [x] [Institute for Standardization of Serbia ISO/IEC DIS 25000-23.2 project record](https://iss.rs/en/project/show/iso:proj:89069)
- [x] [DORA Guides DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- [x] [CIS The 18 CIS Critical Security Controls](https://www.cisecurity.org/controls/cis-controls-list)
- [x] [NIST SP 800-53 Rev. 5 Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [x] [NIST SP 800-218 Secure Software Development Framework Version 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)
- [x] [Principles of Chaos Engineering](https://principlesofchaos.org/)
- [x] [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [x] [Paul and Wang (2019) Fitness function-driven development, Thoughtworks](https://www.thoughtworks.com/insights/articles/fitness-function-driven-development)
- [x] [CMMI Institute CMMI Levels of Capability and Performance](https://cmmiinstitute.com/learning/appraisals/levels)
- [x] [Thurgood (2018) Example Error Budget Policy, Google Site Reliability Engineering (SRE) Workbook](https://sre.google/workbook/error-budget-policy/)

---

## Research Skill Output

### §0 Initialise

```text
question: how to adapt ISO/IEC 25010 into a reusable evidence-backed five-level rubric for internal platforms
scope: eight requested characteristics, 25023 measures, NIST and CIS mapping, delivery and operations evidence, use of scores for prioritisation, SLOs and error budgets
constraints: reuse existing telemetry; federated ownership; auditable evidence; no formal certification
supplied_summary: not present in the issue text available to this session; recorded as a gap
```

Hypothesis H1: the requested eight characteristics correspond to the 2011 edition of ISO/IEC 25010, and the 2023 edition has nine. [assumption; source: https://quality.arc42.org/articles/iso-25010-update-2023]

Hypothesis H2: the rubric thresholds cannot come from the standard and must be set locally. [assumption; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

```text
prior_items_consulted: ideal-internal-platform-product-standard, thinnest-viable-internal-platform-standard, llm-consumption-maturity-ladder, sre-slo-threshold-justification, research-quality-assurance-methodology
```

### §1 Question Decomposition

```text
1 Editions and characteristics
  1a which edition of 25010 is current and how many characteristics does it define
  1b which edition does 25023 align to and what is the revision status
  1c how should the eight-characteristic request be handled
2 Measures per characteristic
  2a what does 25023 provide and not provide (formulas, ranges)
  2b which indicators, data sources and tools supply equivalent evidence
3 Five-level scoring
  3a which level structure to adapt and what it is not
  3b what evidence tiers make a score repeatable
  3c how to treat missing data, ownership and audit trail
4 Control and gate mapping
  4a which CIS controls and NIST publications relate to which characteristics
  4b how to avoid implying compliance
5 Use of scores
  5a how scores drive prioritisation, SLOs, error budgets and tracking
```

### §2 Investigation

#### 1a. Current edition and characteristic count

ISO/IEC 25010:2023 was released in November 2023 and adds Safety as a top-level characteristic, renames Usability to Interaction capability and Portability to Flexibility. [fact; source: https://quality.arc42.org/articles/iso-25010-update-2023; https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/]

The ISO 25000 portal states that the product quality model comprises nine quality characteristics. [fact; source: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010]

At sub-characteristic level, inclusivity and self-descriptiveness were added to interaction capability, resistance to security and scalability to flexibility, user engagement replaced user interface aesthetics, faultlessness replaced maturity, and accessibility was split into inclusivity and user assistance. [fact; source: https://quality.arc42.org/articles/iso-25010-update-2023]

Safety has five sub-characteristics: operational constraint, risk identification, fail safe, hazard warning and safe integration, and is defined as the capability of a product not to endanger human health, property or the environment. [fact; source: https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/]

Access note: the iso.org catalogue pages for ISO/IEC 25010 and 25023 returned HTTP 403; the standards text itself is paywalled, so sub-characteristic lists rely on the secondary sources above and the ISO 25000 portal.

#### 1b. Alignment of 25023 and revision status

The ISO/IEC 25023:2016 table of contents groups measures under eight characteristics: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability and portability, with no safety group. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

The same document uses the 2011 sub-characteristic names, for example maturity, user interface aesthetics and accessibility. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

The standards-body project record lists its successor, the Draft International Standard (DIS) ISO/IEC DIS 25000-23.2, at stage 40.60 (close of voting) and names ISO/IEC 25023:2016 as the previously published edition. [fact; source: https://iss.rs/en/project/show/iso:proj:89069]

The requested eight-characteristic summary therefore corresponds to the 2011 model that 25023:2016 measures, while the current 25010 has nine; this is an inference from matching the two sources. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://quality.arc42.org/articles/iso-25010-update-2023]

#### 1c. Handling the eight-versus-nine difference

A rubric that scores the eight 2011-era characteristics under their 2023 names, with Safety as a conditional ninth characteristic switched on only when the platform can endanger health, property or the environment, keeps the requested framing and current terminology. [inference; source: https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/; https://iso25000.com/index.php/en/iso-25000-standards/iso-25010]

The applicability switch is consistent with the Thinnest Viable Platform (TVP) principle that a platform should carry the smallest set of components that still serves consumers, applied here to the assessment instrument rather than the platform. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-01-thinnest-viable-internal-platform-standard.md]

#### 2a. What 25023 provides

ISO/IEC 25023 defines a basic set of quality measures per characteristic and sub-characteristic and documents each with an identifier, name, description and measurement function. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

Most measures normalise the result to a range from 0.0 to 1.0 where closer to 1.0 is better, and some are relative to a target value set in requirements. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

The standard does not assign value ranges to rated levels or grades of compliance, because those depend on the nature of the system, integrity level and user needs. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

It proposes three ways to interpret a measure that is hard to read in isolation: conformance to a requirement, comparison with a benchmark, and a time series. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

It also allows users to modify the measures or define new ones, provided they state how the new measure relates to the 25010 model. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

Access note: only the preview pages through section 8.1 were retrievable, so the clause 8 measurement functions were not read; searches for the formulas returned unsourced restatements and were not used. Search queries used: "ISO/IEC 25023:2016 measurement formulas availability mean time to recovery fault correction mean response time" (no primary text found).

Because the clause 8 formulas were not read, indicators below are adaptations that name the 25023 sub-characteristic family they stand in for, not verified 25023 functions. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

#### 2b. Indicators, data sources and tools

The table gives candidate indicators per characteristic. Each row is an adaptation and carries its own label and sources.

| Characteristic | Candidate indicators and data sources | Label and sources |
|---|---|---|
| Functional suitability | Requirement-to-acceptance-test coverage, defect escape rate from the issue tracker, task completion in scripted scenarios | [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://iso25000.com/index.php/en/iso-25000-standards/iso-25010] |
| Performance efficiency | Latency percentiles and throughput from application performance monitoring compared with the agreed target, resource utilisation, load-test capacity headroom | [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://principlesofchaos.org/] |
| Compatibility | Contract-test pass rate for exposed and consumed Application Programming Interfaces (APIs), co-existence test results in shared environments | [inference; source: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf] |
| Interaction capability | Pass rate against Web Content Accessibility Guidelines (WCAG) 2.2 success criteria from automated scans plus manual audit, task success rate, user error rate | [inference; source: https://www.w3.org/TR/WCAG22/; https://iso25000.com/index.php/en/iso-25000-standards/iso-25010] |
| Reliability | Availability service level indicator (SLI), incident count, chaos experiment steady-state hypothesis outcomes, failed deployment recovery time, disaster recovery drill result against the agreed recovery target | [inference; source: https://dora.dev/guides/dora-metrics/; https://principlesofchaos.org/; https://www.cisecurity.org/controls/cis-controls-list] |
| Security | SAST and DAST finding age and closure rate, access-review completion, audit-log coverage, secure development practice evidence | [inference; source: https://www.cisecurity.org/controls/cis-controls-list; https://csrc.nist.gov/pubs/sp/800/218/final] |
| Maintainability | Architecture fitness-function pass rate for modularity rules, change lead time, automated test pass and flake rate | [inference; source: https://www.thoughtworks.com/insights/articles/fitness-function-driven-development; https://dora.dev/guides/dora-metrics/] |
| Flexibility (portability in 2011) | Time to provision a new instance, scale-out test result, replacement or migration drill outcome | [inference; source: https://quality.arc42.org/articles/iso-25010-update-2023; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf] |
| Safety (conditional) | Hazard analysis outputs, fail-safe test results, hazard warning verification, only where the platform can endanger health, property or the environment | [inference; source: https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/] |

DORA's current guidance lists five software delivery performance metrics: change lead time, deployment frequency, failed deployment recovery time, change fail rate and deployment rework rate, and records the move from mean time to recovery (MTTR) to failed deployment recovery time. [fact; source: https://dora.dev/guides/dora-metrics/]

DORA also advises that the metrics suit one application or service at a time and that blending them across teams or the whole organisation can be problematic because contexts differ. [fact; source: https://dora.dev/guides/dora-metrics/]

Chaos engineering is defined as experimenting on a system to build confidence in its capability to withstand turbulent conditions, using a four-step process that starts from a measurable steady state and tries to disprove the hypothesis that it persists. [fact; source: https://principlesofchaos.org/]

A chaos experiment that states its steady-state hypothesis and retains the result is usable as a fault-tolerance evidence artefact, while an unrecorded drill is not auditable. [inference; source: https://principlesofchaos.org/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

Fitness functions are tests that describe how close an architecture is to achieving an architectural aim and can be wired into delivery gates, which makes them a repeatable evidence source for maintainability and performance rules. [fact; source: https://www.thoughtworks.com/insights/articles/fitness-function-driven-development]

WCAG 2.2 success criteria are written as testable statements, but the guidelines state they do not address every user need of people with disabilities. [fact; source: https://www.w3.org/TR/WCAG22/]

Accessibility audit results therefore provide partial evidence for interaction capability and should be paired with task-based evidence for inclusivity and user assistance. [inference; source: https://www.w3.org/TR/WCAG22/; https://quality.arc42.org/articles/iso-25010-update-2023]

#### 3a. Level structure

The CMMI Institute describes maturity levels from 0 Incomplete through 1 Initial, 2 Managed, 3 Defined, 4 Quantitatively Managed to 5 Optimizing, each building on the previous one. [fact; source: https://cmmiinstitute.com/learning/appraisals/levels]

A five-level product-quality rubric can reuse levels 1 to 5 as an adapted scale, scoring each characteristic separately, but this is a rubric in CMMI style and not a CMMI appraisal. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels]

Scoring each characteristic separately instead of producing one composite maturity number is supported by the Amazon Web Services (AWS) generative AI maturity model's statement that maturity levels commonly overlap within an organisation rather than progressing linearly. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md]

The same maturity-ladder item reports that maturity-model position correlated with financial performance only in a surveyed sample, which does not show that a higher product-quality level causes better outcomes. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md]

| Level | Adapted name | Criterion for a characteristic | Minimum evidence tier |
|---|---|---|---|
| 1 | Initial | Quality addressed ad hoc; no agreed target; indicators absent or unmeasured | E0 assertion |
| 2 | Managed | Team has an agreed target for the in-scope sub-characteristics and measures at least one indicator manually or on request | E1 dated attestation with artefact link |
| 3 | Defined | Organisation-wide indicator definitions and targets apply across teams; indicators come from tools | E2 reproducible tool output |
| 4 | Quantitatively managed | Indicators are automated in gates or monitoring, targets are justified by data, and misses trigger a defined response such as an error budget policy | E3 automated and retained in an audit trail |
| 5 | Optimizing | Results feed improvement backlogs, drills and fitness functions run continuously, and targets are revised from trend data | E3 plus a retained trend history |

The rows above are adapted criteria. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

#### 3b and 3c. Evidence tiers, missing data, ownership and audit trail

The 25023 interpretation methods of conformance, benchmark and time series map onto levels 2, 3 and 5 respectively: a team target, a cross-team benchmark and a trend. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

Missing data is better scored as level 1 with an explicit unmeasured flag than excluded, because an excluded characteristic would let a team raise its average by not measuring. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

The prior platform-standard item records that Spotify's Soundcheck chains checks into tracks and tracks into certification levels, a deployed pattern for levelled scoring of capability expectations. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md]

The same item recommends combining self-reported data with logs-based delivery data rather than relying on either alone, which supports allowing level 2 attestations while requiring tool output from level 3. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md]

A score record that names the characteristic, scope, level, evidence links, assessor, date and re-assessment due date gives an audit trail without a new measurement programme. [assumption; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

The research-quality-assurance item sequences cheaper structural checks before agent review and human domain review, and the same ordering applies to score validation: automated evidence checks first, peer review of attestations second, domain review of disputed scores last. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-research-quality-assurance-methodology.md]

#### 4a and 4b. Control and gate mapping

The CIS Critical Security Controls v8.1 list 18 controls including Account Management (5), Access Control Management (6), Continuous Vulnerability Management (7), Audit Log Management (8), Data Recovery (11), Application Software Security (16) and Incident Response Management (17). [fact; source: https://www.cisecurity.org/controls/cis-controls-list]

NIST SP 800-218 recommends a core set of high-level secure software development practices that can be integrated into any software development life cycle model. [fact; source: https://csrc.nist.gov/pubs/sp/800/218/final]

Candidate mappings are: Security to CIS 5, 6, 7 and 16 and NIST SP 800-218; Reliability to CIS 11 and 17; Maintainability and Security audit evidence to CIS 8. [inference; source: https://www.cisecurity.org/controls/cis-controls-list; https://csrc.nist.gov/pubs/sp/800/218/final]

NIST states that its mappings and crosswalks give a general indication of control coverage, that equivalency must not be assumed from relationship tables, and that mappings are not always one-to-one. [fact; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

Rubric output should therefore be described as evidence that supports a control, never as control compliance, and the specific SP 800-53 control identifiers should be taken from the catalogue during adoption. [inference; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

Access note: the SP 800-53 catalogue control titles were not retrieved, so this item does not assign individual SP 800-53 controls to characteristics.

#### 5a. Using scores for prioritisation, SLOs and error budgets

Google's example error budget policy halts changes other than priority-zero issues or security fixes when the service exceeds its error budget for the preceding four-week window, and states that the policy is not a punishment but permission to focus on reliability. [fact; source: https://sre.google/workbook/error-budget-policy/]

The prior service-level-objective item concludes that an SLO without an enforced error budget policy becomes a passive reporting metric, which supports requiring both an SLO and a budget response for level 4 of reliability and performance efficiency. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md; https://sre.google/workbook/error-budget-policy/]

Reach, Impact, Confidence and Effort (RICE) scoring, already recommended for internal platform backlogs, can rank improvements that close a characteristic gap by pairing the level gap with consumer reach and confidence in the evidence. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md]

Because SLOs derive from SLIs, only characteristics that produce a user-facing SLI, mainly performance efficiency, reliability and some functional suitability measures, should drive SLOs, while the others should drive backlog priority and gates. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md]

### §3 Reasoning

```text
facts: nine characteristics in 2023; 25023:2016 aligned to eight 2011 characteristics; no rating ranges in 25023; DORA five metrics; CIS control titles; NIST warns against equating mappings; error budget policy halts changes
inferences: eight-plus-conditional-Safety framing; locally set thresholds; five-level adaptation with evidence tiers; unmeasured scored as level 1; mapping as supporting evidence only
assumptions: audit-record fields are sufficient; paid 25023 text would not change the indicator families
```

1. The requested eight characteristics match the 2011 model that 25023:2016 measures. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://quality.arc42.org/articles/iso-25010-update-2023]
2. The standard supplies measure families but no level thresholds, so level criteria must be process and evidence requirements with locally set targets. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]
3. Repeatability across teams comes from shared indicator definitions and evidence tiers rather than from shared numeric thresholds. [inference; source: https://dora.dev/guides/dora-metrics/; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]
4. Control mappings stay at the level of supporting evidence. [inference; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]
5. Investment follows from the level gap weighted by consumer reach, and SLOs follow only where an SLI exists. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md; https://sre.google/workbook/error-budget-policy/]

### §4 Consistency Check

Tension 1: DORA advises against blending metrics across teams, yet a federated organisation wants comparable scores. [fact; source: https://dora.dev/guides/dora-metrics/] The resolution is to compare levels defined by shared criteria and evidence tiers across teams while keeping indicator values per service. [inference; source: https://dora.dev/guides/dora-metrics/; https://cmmiinstitute.com/learning/appraisals/levels]

Tension 2: the iso25000 portal presents nine characteristics while the 25023 measure catalogue covers eight. [fact; source: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf] The resolution is to treat Safety indicators as locally defined until a revised 25023 is published. [inference; source: https://iss.rs/en/project/show/iso:proj:89069]

```text
contradiction_scan: resolved
confidence_adjustment: standards-text claims kept at medium because only secondary sources and a preview were accessible
scope_guardrail: maintained
```

### §5 Depth and Breadth Expansion

Technical lens: indicators that already exist in APM, pipelines and ticketing tools make levels 2 and 3 achievable without new instrumentation, whereas levels 4 and 5 need gates and retained history. [inference; source: https://dora.dev/guides/dora-metrics/; https://www.thoughtworks.com/insights/articles/fitness-function-driven-development]

Regulatory lens: a regulated organisation can retain score records and linked evidence as support for control narratives, but mapping tables are only general indications, so the rubric must not be presented as attestation of compliance. [inference; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final; https://www.cisecurity.org/controls/cis-controls-list]

Economic lens: the TVP principle implies that scoring every sub-characteristic on every platform is waste, so a profile of in-scope sub-characteristics chosen by consumer need keeps measurement cost proportionate. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-01-thinnest-viable-internal-platform-standard.md]

Behavioural lens: scores used as targets may invite gaming, so reading them as diagnostics for improvement conversations rather than team rankings is a design choice. [assumption; source: https://dora.dev/guides/dora-metrics/]

Competing explanation: a single composite maturity score is simpler to communicate, yet overlap between levels within one organisation argues for per-characteristic reporting. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md]

### §6 Synthesis

**Executive summary:** see `## Findings > Executive Summary` below (mirrored).

**Key findings:** see `## Findings > Key Findings` below (mirrored).

**Evidence map:** see `## Findings > Evidence Map` below (mirrored).

**Assumptions:** see `## Findings > Assumptions` below (mirrored).

**Analysis:** see `## Findings > Analysis` below (mirrored).

**Risks, gaps, uncertainties:** see `## Findings > Risks, Gaps, and Uncertainties` below (mirrored).

**Open questions:** see `## Findings > Open Questions` below (mirrored).

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed, Full Name (ABBR) order confirmed at first narrative use
parity_check: Findings mirrors §6 pointers; claims in Findings trace to §2 to §5
label_audit: declarative prose in §2 to §5 carries trailing labels with URL sources
self_citation_check: no section cites this file as a source
gap_record: supplied summary not recovered; 25023 clause 8 formulas not read; SP 800-53 control titles not retrieved
```

---

## Findings

### Executive Summary

The most practical rubric scores the eight 2011-era characteristics that ISO/IEC 25023:2016 measures under their 2023 names, adds Safety as a conditional ninth characteristic, and rates each characteristic separately on an adapted five-level scale tied to evidence tiers rather than to universal numeric thresholds. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://quality.arc42.org/articles/iso-25010-update-2023]

The standard itself cannot supply the thresholds because ISO/IEC 25023 assigns no value ranges to rated levels, so it offers conformance, benchmark or time-series interpretation. [fact; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf] Each team therefore has to agree targets locally. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

Existing delivery metrics, monitoring, fitness functions, chaos drills and accessibility audits supply the indicators, and the resulting evidence supports, but does not demonstrate, compliance with CIS and NIST controls. [inference; source: https://dora.dev/guides/dora-metrics/; https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

Scores guide investment by pairing level gaps with consumer reach and by tying levels 4 and 5 of reliability and performance efficiency to an SLO with an error budget policy, with the main uncertainty being that the ISO/IEC 25023 measurement formulas and the supplied summary were not accessible. [inference; source: https://sre.google/workbook/error-budget-policy/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md]

### Key Findings

1. ISO/IEC 25010:2023 defines nine product quality characteristics, adding Safety and renaming Usability to Interaction capability and Portability to Flexibility. ([fact]; high confidence; source: https://quality.arc42.org/articles/iso-25010-update-2023; https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/) The requested eight-characteristic framing is therefore not the current edition's structure. ([inference]; medium confidence; source: https://quality.arc42.org/articles/iso-25010-update-2023)
2. The ISO/IEC 25023:2016 table of contents organises measures under eight characteristics with 2011-era sub-characteristic names, and the standards-body record places its successor at close of voting. ([fact]; medium confidence; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://iss.rs/en/project/show/iso:proj:89069) No published measure catalogue therefore appears to cover the 2023 characteristics. ([inference]; medium confidence; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://iss.rs/en/project/show/iso:proj:89069)
3. ISO/IEC 25023 normalises most measures to a 0.0 to 1.0 range, assigns no value ranges to rated levels, and offers conformance, benchmark and time-series interpretation. ([fact]; medium confidence; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf) Level thresholds are therefore left to local decision. ([inference]; medium confidence; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf)
4. A rubric that scores the eight characteristics under 2023 names, treats Safety as a conditional ninth, and reports each characteristic separately resolves the edition mismatch while matching the finding that maturity levels overlap rather than progress linearly. ([inference]; medium confidence; source: https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md)
5. The five-level scale can adapt the CMMI maturity levels Initial, Managed, Defined, Quantitatively Managed and Optimizing and pair each level with an evidence tier from attestation to automated retained output, but it remains a rubric in CMMI style rather than a formal appraisal. ([inference]; medium confidence; source: https://cmmiinstitute.com/learning/appraisals/levels; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf)
6. DORA's five delivery metrics, chaos experiments with stated steady-state hypotheses, architecture fitness functions and WCAG 2.2 success-criteria audits can each supply indicators for reliability, maintainability and interaction capability using data that teams already produce. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://principlesofchaos.org/; https://www.thoughtworks.com/insights/articles/fitness-function-driven-development; https://www.w3.org/TR/WCAG22/)
7. DORA recommends measuring one application or service at a time and warns that blending metrics across teams can mislead. ([fact]; medium confidence; source: https://dora.dev/guides/dora-metrics/) Cross-team comparison should therefore use shared level criteria while indicator values stay per service. ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
8. Candidate control mappings link Security to CIS controls 5, 6, 7 and 16 and NIST SP 800-218, and Reliability to CIS controls 11 and 17, with audit-log evidence tied to CIS control 8. ([inference]; medium confidence; source: https://www.cisecurity.org/controls/cis-controls-list; https://csrc.nist.gov/pubs/sp/800/218/final)
9. NIST states that its mappings give only a general indication of coverage and must not be treated as equivalence, so rubric output should be worded as evidence supporting a control and never as control compliance. ([fact]; medium confidence; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
10. WCAG 2.2 criteria are testable statements that do not cover every user need. ([fact]; medium confidence; source: https://www.w3.org/TR/WCAG22/) Accessibility audit pass rates therefore give partial evidence for interaction capability that task-based measures must complement. ([inference]; medium confidence; source: https://www.w3.org/TR/WCAG22/)
11. Google's example error budget policy halts non-priority changes after a four-week budget breach, and the earlier service-level-objective item found that an SLO without such a policy becomes passive reporting, which supports requiring both for level 4 reliability. ([inference]; medium confidence; source: https://sre.google/workbook/error-budget-policy/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md)
12. Reach, Impact, Confidence and Effort scoring from the earlier platform-standard item can rank improvements by pairing a characteristic's level gap with consumer reach, with only characteristics that yield a user-facing indicator driving SLOs. ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md)

The per-characteristic indicator table and the five-level criteria table are held in `§2 Investigation` sections 2b and 3a, and each row there carries its own label and sources.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] ISO/IEC 25010:2023 has nine characteristics with Safety added and two renames | https://quality.arc42.org/articles/iso-25010-update-2023; https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/ | high | Two independent commentators |
| [fact] 25023:2016 covers eight 2011-era characteristics; successor at close of voting | https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://iss.rs/en/project/show/iso:proj:89069 | medium | Preview pages only |
| [fact] 25023 assigns no rating ranges; offers three interpretation methods | https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf | medium | Single source |
| [inference] Eight characteristics under 2023 names plus conditional Safety, reported per characteristic | https://blog.spree.de/2024/01/02/iso-iec-25010-news-from-the-2nd-edition-2023-11/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md | medium | Design choice |
| [inference] Five-level scale adapted from CMMI levels with evidence tiers | https://cmmiinstitute.com/learning/appraisals/levels; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf | medium | Not an appraisal |
| [inference] Existing metrics, drills, fitness functions and audits supply indicators | https://dora.dev/guides/dora-metrics/; https://principlesofchaos.org/; https://www.thoughtworks.com/insights/articles/fitness-function-driven-development; https://www.w3.org/TR/WCAG22/ | medium | Adapted indicators |
| [fact] DORA advises per-service measurement and cautions on blending | https://dora.dev/guides/dora-metrics/ | medium | Single organisation |
| [inference] Candidate CIS and SP 800-218 mappings per characteristic | https://www.cisecurity.org/controls/cis-controls-list; https://csrc.nist.gov/pubs/sp/800/218/final | medium | SP 800-53 titles not retrieved |
| [fact] NIST warns mappings are not equivalence | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final | medium | Single source |
| [fact] WCAG 2.2 criteria are testable but not exhaustive | https://www.w3.org/TR/WCAG22/ | medium | Single source |
| [inference] Error budget policy plus SLO required at level 4 for reliability | https://sre.google/workbook/error-budget-policy/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md | medium | Same evidence family |
| [inference] RICE with level gap ranks improvements; SLOs only where an indicator exists | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-31-sre-slo-threshold-justification.md | medium | Repository items only |

### Assumptions

The audit-record fields of characteristic, scope, level, evidence links, assessor, date and re-assessment due date are assumed sufficient as an audit trail for a regulated setting. [assumption; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final] NIST's own cautions about mappings show that auditors ultimately judge control coverage, so the record needs to be traceable rather than exhaustive. [assumption; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]

The indicator families chosen are assumed to remain valid after the unread ISO/IEC 25023 clause 8 formulas are consulted. [assumption; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf] The preview confirms that users may modify measures if they document the relation to the 25010 model, which limits the cost of an error here. [assumption; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]

Requirements for the 2011 and 2023 editions of the quality model are assumed to differ little for internal platforms outside Safety and the renames. [assumption; source: https://quality.arc42.org/articles/iso-25010-update-2023] The arc42 summary of the official changes is assumed to be complete, so no characteristic was removed beyond those it lists. [assumption; source: https://quality.arc42.org/articles/iso-25010-update-2023]

### Analysis

The main trade-off is between standard fidelity and usability: adopting the 2023 model unchanged would leave no published measure catalogue, while adopting the 2011 measure families unchanged would use retired names. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://iss.rs/en/project/show/iso:proj:89069] Scoring the 2011 families under 2023 names, with documented modifications as 25023 permits, balances both. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://quality.arc42.org/articles/iso-25010-update-2023]

Universal numeric thresholds were considered and rejected as the basis of levels because the standard leaves ranges to the nature of the system and DORA warns that context differs between teams. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://dora.dev/guides/dora-metrics/] Defining levels by evidence tier and process rigour keeps scores comparable without forcing identical targets. [inference; source: https://cmmiinstitute.com/learning/appraisals/levels; https://dora.dev/guides/dora-metrics/]

A single composite score is the rival design, and it was set aside because maturity levels are reported to overlap within one organisation and a composite hides which characteristic limits the platform. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md]

Rival remedies for weak evidence, such as relying on self-attestation alone or buying a new measurement platform, were weighed against reusing tool output the teams already produce, which fits the constraint of avoiding a heavy programme and the finding that self-reported and logs-based data complement each other. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-10-02-ideal-internal-platform-product-standard.md; https://dora.dev/guides/dora-metrics/]

Score validation can follow the cheaper-checks-first ordering from the research-quality-assurance item, with automated evidence checks before peer review of attestations. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-research-quality-assurance-methodology.md]

### Risks, Gaps, and Uncertainties

- The supplied summary referred to in the issue was not part of the issue text available for this item, so the requested eight-characteristic list is inferred from the 2011 model. [inference; source: https://quality.arc42.org/articles/iso-25010-update-2023]
- The clause 8 measurement functions of ISO/IEC 25023:2016 sit beyond the freely available preview pages, so formulas for availability, response time or fault-correction measures are not verified and every indicator is an adaptation. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf]
- The revised ISO/IEC 25023 is at close of voting and may change measure names and families before publication. [fact; source: https://iss.rs/en/project/show/iso:proj:89069]
- The 2023 sub-characteristic structure is drawn from commentary and the ISO 25000 portal rather than the standard text. [inference; source: https://iso25000.com/index.php/en/iso-25000-standards/iso-25010; https://quality.arc42.org/articles/iso-25010-update-2023]
- Specific SP 800-53 control identifiers were not mapped because the catalogue titles were not retrieved. [inference; source: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final]
- No empirical study was found that tests whether a higher rubric level predicts better platform outcomes, so the rubric is a design proposal. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-08-13-llm-consumption-maturity-ladder.md]

### Open Questions

- Which ISO/IEC 25023 clause 8 formulas should be licensed and verified, and do they change the proposed indicator families once the revised edition is published?
- How should a Safety characteristic be scored for internal platforms that touch clinical or physical processes?
- Does pilot scoring across several teams show stable inter-assessor agreement at each level?

---

## Output

- Type: knowledge
- Description: A five-level, evidence-tiered product quality measurement rubric adapting ISO/IEC 25010 for internal platforms, with indicator families, control-mapping cautions and prioritisation guidance. [inference; source: https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://cmmiinstitute.com/learning/appraisals/levels]
- Links: https://quality.arc42.org/articles/iso-25010-update-2023; https://cdn.standards.iteh.ai/samples/35747/34b91bc957f647ce8bbb2093907d7bc0/ISO-IEC-25023-2016.pdf; https://dora.dev/guides/dora-metrics/
