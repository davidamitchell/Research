---
review_count: 2
title: "Matched denominator for comparing post-pipeline release-based failures with production live-runtime incidents"
added: 2026-05-17T20:40:49+00:00
status: completed
priority: high
blocks: []
tags: [organisation, workflow, analytics]
started: 2026-05-18T11:09:21+00:00
completed: 2026-05-18T11:39:12+00:00
output: []
cites: [2026-05-16-variance-control-comparison-across-delivery-modes]
related: [2026-05-07-ai-production-incidents-deep-dive, 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: 8dc7a01be2910f82b0b1e5581924fb64ed711846
    changed: 2026-05-18
    progress: progress/2026-05-18-build-mode-failure-vs-do-mode-incident-comparison-denominator.md
    summary: "Initial completion"
---

# Matched denominator for comparing post-pipeline release-based failures with production live-runtime incidents

## Research Question

What common denominator enables direct matched comparison between post-pipeline release-based failure rates and production live-runtime incident rates for the same production workflow?

## Scope

**In scope:**
- Candidate denominator definitions for build and run reliability comparison (for example workflow execution unit, deployment unit, and business-process transaction unit)
- Matching strategies for the same production workflow across delivery and production operations
- Bias and observability limitations in cross-phase failure and incident comparison

**Out of scope:**
- Platform-specific implementation details of any single continuous integration or service-management product
- Reliability economics models that do not provide measurable denominator mappings

**Constraints:** Prioritise denominator choices that can be computed from standard engineering and incident-management telemetry without proprietary data models.

## Context

Teams cannot make defensible control or investment decisions when build failures and production incidents are tracked on incompatible units. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

## Approach

1. Identify denominator options used in software delivery performance and operational reliability literature.
2. Evaluate which denominator can be computed consistently for both post-pipeline failures and production incidents.
3. Define a matched comparison protocol and known distortion risks for comparing the same production workflow across modes.

## Sources

- [x] [DevOps Research and Assessment (DORA) (2026) DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) - official release-based metric definitions and comparison cautions; substituted for the cloud.google.com overview page that did not expose the needed metric content in this runtime
- [x] [Google (2016) Site Reliability Engineering (SRE) Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) - request, yield, throughput, and end-to-end latency denominators used for live-service reliability
- [x] [Google (2016) Site Reliability Engineering (SRE) Book: Tracking Outages](https://sre.google/sre-book/tracking-outages/) - incident counts over time and alerts-per-incident analysis used for operational review
- [x] [Google (2016) Site Reliability Engineering (SRE) Book: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) - post-release recovery framing and pre-release blocking through system tests
- [x] [Google (2016) Site Reliability Engineering (SRE) Book: Release Engineering](https://sre.google/sre-book/release-engineering/) - repeatable release gates and deployment discipline for release-based changes
- [x] [Google (2022) Measuring Reliability](https://sre.google/resources/practices-and-processes/measuring-reliability/) - service level indicator (SLI) ratio examples, grouping cautions, and question-fit guidance
- [x] [PeopleCert (2026) Information Technology Infrastructure Library (ITIL) 4 Practitioner: Incident Management](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684) - official incident-management purpose and practice-metric framing; substituted for the Axelos page that did not expose the needed practice content in this runtime
- [x] [Swanson et al. (2008) National Institute of Standards and Technology (NIST) Special Publication (SP) 800-55 Revision 1 Performance Measurement Guide for Information Security](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf) - quantifiable, repeatable, comparable, and decision-useful measurement criteria
- [x] [Mitchell (2026) Variance control comparison across delivery modes](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-variance-control-comparison-across-delivery-modes.md) - prior completed repository item that framed the asymmetry between release-gate controls and live-runtime controls

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0-5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

- Question: What common denominator enables direct matched comparison between post-pipeline release-based failure rates and production live-runtime incident rates for the same production workflow?
- Scope: denominator choice, matching the same production workflow, and distortion risks for cross-phase comparison
- Constraints: prefer metrics that can be computed from standard release, logging, tracing, queue, and incident telemetry without proprietary vendor schemas
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions
- Mode: full
- [fact] Prior completed repository work already established that release-based delivery is usually observed through escaped-release proxies while live runtime execution is observed through live task-execution proxies; this item narrows the question to the denominator that can compare the same production workflow directly. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-variance-control-comparison-across-delivery-modes.md]
- [assumption] In this item, the comparison is restricted to a bounded family of production executions with the same task objective, trigger, success condition, and user-visible consequence, because SRE guidance says reliability measures must answer a specific operational question and warns that mixed request groups can hide meaningful differences. [assumption; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://sre.google/sre-book/service-level-objectives/]

### §1 Question Decomposition

- Q1. What denominators do the source literatures use natively?
  - Q1.1. What denominator does DORA use for post-deployment release-based instability?
  - Q1.2. What denominators does SRE use for live-service reliability?
  - Q1.3. What denominator framing does official incident-management practice use?
  - Q1.4. What measurement-design constraints does NIST impose on denominator choice?
- Q2. Which candidate denominator can be computed consistently for both post-pipeline build failures and production incidents?
  - Q2.1. Can deployment count serve as the shared denominator?
  - Q2.2. Can calendar time or raw incident count serve as the shared denominator?
  - Q2.3. Can production workflow execution or business transaction count serve as the shared denominator?
- Q3. What protocol is needed to compare the same production workflow rather than incomparable systems?
  - Q3.1. How should the same production workflow be matched?
  - Q3.2. How should release-based and live-runtime numerators be mapped onto the same denominator?
  - Q3.3. What fallback is least misleading when incident systems do not record affected executions directly?
- Q4. What bias and observability risks remain after the denominator is chosen?
  - Q4.1. What happens when requests or transactions are not equally consequential?
  - Q4.2. What happens when incidents span multiple production workflows?
  - Q4.3. What happens when low-volume workflows lack enough executions for stable rates?

### §2 Investigation

- **Q1.1 Build-mode instability denominator**
  - [fact] DORA defines change fail rate as the ratio of deployments that require immediate intervention after deployment to total deployments. [fact; source: https://dora.dev/guides/dora-metrics/]
  - [fact] DORA also defines deployment rework rate as the ratio of unplanned deployments caused by an incident in production to total deployments. [fact; source: https://dora.dev/guides/dora-metrics/]
  - [fact] DORA says its software-delivery metrics are best suited to one application or service at a time and warns that comparing metrics across vastly different applications can be misleading. [fact; source: https://dora.dev/guides/dora-metrics/]
  - [fact] Google's release-engineering guidance treats reliable release processes as repeatable, automated, and gated through tests, approvals, canarying, and rollback practices. [fact; source: https://sre.google/sre-book/release-engineering/]
  - [fact] Google's testing guidance says a system-level test can detect a bug before production and produce zero mean time to repair, because the push is blocked before users experience the failure. [fact; source: https://sre.google/sre-book/testing-reliability/]
  - [inference] Deployment count is the native denominator for release-based delivery instability, but it measures change attempts rather than live production demand. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/release-engineering/]

- **Q1.2 Live-service reliability denominators**
  - [fact] SRE guidance defines an SLI as a quantitative measure of service level and lists error rate as the fraction of all requests received, request latency, throughput, and yield, meaning the fraction of well-formed requests that succeed, as common live-service measures. [fact; source: https://sre.google/sre-book/service-level-objectives/]
  - [fact] The same SRE chapter says big-data systems care about throughput and end-to-end latency, meaning how much data is processed and how long it takes data to progress from ingestion to completion. [fact; source: https://sre.google/sre-book/service-level-objectives/]
  - [fact] Google's outage-tracking chapter uses incidents per week, month, or quarter and alerts per incident for operational review, trend detection, and team comparison. [fact; source: https://sre.google/sre-book/tracking-outages/]
  - [fact] Google's measuring-reliability talk gives SLI examples as ratios such as Hypertext Transfer Protocol (HTTP) 500 responses over all HTTP responses, and responses under 200 milliseconds over all responses. [fact; source: https://sre.google/resources/practices-and-processes/measuring-reliability/]
  - [fact] The same talk warns that SLIs assume all requests are equal and recommends human-curated grouping, for example by application programming interface call or location, when request classes differ materially. [fact; source: https://sre.google/resources/practices-and-processes/measuring-reliability/]
  - [inference] Live-service reliability literature therefore normalises failure against executed demand units, such as requests, transactions, or completed pipeline runs, while time-based incident counts remain secondary management views. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

- **Q1.3 Incident-management practice framing**
  - [fact] PeopleCert's official Incident Management practice page says the practice focuses on restoring normal service operations swiftly after disruptions and includes key practice metrics for evaluating effectiveness and ensuring timely resolution of incidents. [fact; source: https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684]
  - [inference] Official incident-management practice is therefore concerned with incident handling effectiveness and restoration speed, but it does not by itself supply a direct cross-phase denominator for comparing released-change failure with live-execution failure. [inference; source: https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684; https://sre.google/sre-book/tracking-outages/]

- **Q1.4 NIST denominator-choice constraints**
  - [fact] NIST SP 800-55 Rev.1 says measures must yield quantifiable information, be repeatable, and be useful for tracking performance and pointing to corrective actions. [fact; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
  - [fact] The same NIST guide says measures should help management decide where to invest additional resources, identify nonproductive controls, and justify investments. [fact; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
  - [fact] NIST also says information-security measures must yield quantifiable information for comparison purposes and track changes using the same points of reference. [fact; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
  - [inference] A defensible common denominator must therefore be quantifiable from normal telemetry, repeatable over time, comparable across the two modes, and useful for choosing controls or investment. [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

- **Q2.1 Candidate denominator: deployments**
  - [inference] Deployment count cannot serve as the shared denominator because live-runtime incidents can recur many times without any new deployment, while DORA explicitly scopes deployment-based instability to software-delivery performance for a single application or service. [inference; source: https://dora.dev/guides/dora-metrics/]

- **Q2.2 Candidate denominator: calendar time or incident count**
  - [inference] Calendar-time denominators such as incidents per month are useful for operational trend review, but they cannot support matched comparison across production workflows because the same incident count can arise from very different execution volumes. [inference; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

- **Q2.3 Candidate denominator: production workflow execution**
  - [inference] Production workflow execution is the strongest shared denominator because both release-based escaped failures and live-runtime incidents are only realised when an actual production execution attempt is degraded, fails, or produces the wrong outcome. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
  - [inference] For user-facing services, this denominator should be instantiated as requests, application programming interface calls, or completed business transactions; for batch and pipeline systems, it should be instantiated as job runs, dataset loads, or stage completions, because SRE maps reliability measures to those service types already. [inference; source: https://sre.google/sre-book/service-level-objectives/]

- **Q3.1 Workflow-class matching**
  - [inference] Workflow classes should be matched by task objective, trigger, dependency surface, success condition, and external consequence, because both DORA and SRE warn that blended metrics hide meaningful contextual differences. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

- **Q3.2 Numerator mapping**
  - [inference] For release-based delivery, the numerator should be the count of failed or materially degraded executions attributable to a released change after it passed pipeline gates, not all failed builds and not all deployments. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/testing-reliability/; https://sre.google/sre-book/release-engineering/]
  - [inference] For live runtime execution, the numerator should be the count of failed or materially degraded live executions in the same production workflow, or the subset of executions affected during an incident window when the system cannot tag each failed execution directly. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/]

- **Q3.3 Fallback when affected executions are not recorded directly**
  - [assumption] When incident systems capture only start time, end time, and the affected production workflow, multiplying the affected window by baseline workflow throughput is the least misleading fallback estimate of affected executions, because it preserves the execution denominator instead of reverting to deployments or calendar time. [assumption; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

- **Q4 Distortion and observability risks**
  - [fact] Google's measuring-reliability guidance says SLIs assume all requests are equal and that aggregation can hide severe problems experienced by a subset of users or request types. [fact; source: https://sre.google/resources/practices-and-processes/measuring-reliability/]
  - [inference] Severity mix, shared incidents that span multiple production workflows, poor workflow tagging, and low-volume workflows can all distort execution-based comparison unless the workflow definition and consequence threshold are explicit. [inference; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
  - [inference] Latent build defects with no production exposure will be invisible to an execution denominator until traffic reaches the affected path, but this is acceptable for this item because the question is about post-pipeline failures actually realised in production. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/testing-reliability/]

### §3 Reasoning

- [inference] The core problem is not that delivery and operations use the wrong metrics inside their own domains; it is that their native denominators answer different questions. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]
- [inference] DORA's deployment denominator answers "how often do our releases escape and require intervention," while SRE's request and completion denominators answer "how often does a production execution fail or degrade," so only the latter can absorb both build escapes and live-runtime incidents into one matched frame. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]
- [inference] The shared denominator should therefore be all production workflow executions in a matched class, with release-based events translated forward from deployments to affected executions rather than translating live-runtime incidents backward to deployments. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- [inference] This denominator is more decision-useful than deployments or incident counts because leaders choosing controls care about failure per business outcome attempt, not failure per internal process step or per reporting period. [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- [assumption] Where execution-level tagging is incomplete, throughput-based estimation is preferable to switching denominators mid-analysis, but the resulting rate should be marked lower confidence. [assumption; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/]

### §4 Consistency Check

- [fact] DORA and SRE use different native denominators because they are designed for different reliability questions: change-process stability versus live-service behavior. [fact; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]
- [inference] That difference is not a contradiction. It is the reason deployments cannot be the shared denominator for direct build-versus-do comparison. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]
- [fact] SRE warns that not all requests are equal and DORA warns against disparate comparisons, so both literatures reject blind aggregation across materially different work types. [fact; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- [inference] These warnings are jointly resolved by workflow-specific execution denominators, not by service-wide or organisation-wide incident counts. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- [inference] NIST's quantifiable, repeatable, comparable, and decision-useful measurement criteria fit execution counts from logs and tracing data better than subjective severity-only incident labels. [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: execution-denominator comparison fits the telemetry most teams already have, because request logs, queue records, trace spans, and job-completion events are closer to production effects than deployment ledgers are. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/; https://sre.google/sre-book/release-engineering/]
- [inference] Service-management lens: transaction- or execution-based rates align better with service degradation and restoration management than deployment counts do, because users experience failed service attempts rather than internal release events. [inference; source: https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684; https://sre.google/sre-book/service-level-objectives/]
- [inference] Economic lens: execution-based comparison prevents high-volume classes from hiding behind low incident counts and low-volume classes from looking worse than they are through raw incident totals, which makes investment triage more defensible. [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- [inference] Measurement-behaviour lens: DORA warns that teams can game metrics when metrics become goals, so a denominator tied to production executions is harder to detach from user impact than a denominator tied only to deployments or reporting periods. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

### §6 Synthesis

#### Executive summary

The most defensible common denominator is the count of executions of the same production workflow, not deployments and not calendar time. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

DORA's deployment denominator is valid for delivery-process instability, but it cannot support direct comparison with live-runtime incidents because live-runtime failures can recur many times without a new deployment and DORA itself warns against disparate comparisons across unlike systems. [inference; source: https://dora.dev/guides/dora-metrics/]

SRE reliability practice already measures live behavior on executed demand units such as requests, yield, throughput, and end-to-end pipeline completions, which means release-based escapes and live-runtime incidents can be translated onto the same execution unit once the same production workflow is matched. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

The practical comparison protocol is to attribute both post-pipeline build defects and live-runtime incidents to failed or materially degraded executions in the same production workflow, using incident-window duration multiplied by workflow throughput only as a lower-confidence fallback when direct per-execution tagging is absent. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

#### Key findings

1. **DORA defines post-deployment build instability on a deployment denominator, because change fail rate and deployment rework rate are both expressed as ratios of problematic deployments to total deployments.** ([fact]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
2. **SRE defines live-service reliability on executed demand units, because the core service measures are request error fraction, request latency, yield over well-formed requests, throughput, and end-to-end completion for pipeline-like systems.** ([fact]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/)
3. **Deployment count cannot be the shared denominator for direct build-versus-do comparison, because live-runtime incidents can accumulate without new releases and DORA explicitly warns that cross-context comparisons between unlike applications are misleading.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
4. **Calendar-time incident counts, such as incidents per month or alerts per incident, are useful for operational review but cannot support matched reliability comparison when the same production workflow has very different execution volumes over time.** ([inference]; medium confidence; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/)
5. **The strongest common denominator is therefore the count of executions of the same production workflow, instantiated as requests, business transactions, application programming interface calls, job runs, or stage completions depending on the service type.** ([inference]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf)
6. **A matched comparison should count post-pipeline build failures as degraded or failed executions caused by a released change, and should count live-runtime incidents as degraded or failed live executions in the same production workflow, so that both numerators sit on the same exposure base.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/testing-reliability/; https://sre.google/sre-book/service-level-objectives/)
7. **When execution-level incident tagging is missing, estimating affected executions from incident duration multiplied by baseline workflow throughput is a defensible fallback, but the confidence should be downgraded because the estimate assumes stable demand during the impact window.** ([assumption]; low confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/)
8. **The denominator choice is only decision-useful when the same production workflow is explicitly matched by objective, trigger, success condition, and consequence threshold, because otherwise severity mix and blended traffic will distort the apparent reliability difference between release-based delivery and live runtime execution.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf)

#### Evidence map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] DORA defines build instability on deployment-based ratios. | https://dora.dev/guides/dora-metrics/ | medium | Native build denominator |
| [fact] SRE defines live reliability on executed demand units such as requests, yield, throughput, and end-to-end completions. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ | medium | Native live denominator |
| [inference] Deployment count cannot be the shared denominator for build-versus-do comparison. | https://dora.dev/guides/dora-metrics/ | medium | Asymmetric change cadence |
| [inference] Calendar-time incident counts are secondary views, not matched exposure denominators. | https://sre.google/sre-book/tracking-outages/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ | medium | Volume-distortion risk |
| [inference] Execution count for the same production workflow is the strongest common denominator across both modes. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ ; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf | medium | Core synthesis claim |
| [inference] Both numerators should be mapped to failed or degraded executions in the same production workflow. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/sre-book/testing-reliability/ ; https://sre.google/sre-book/service-level-objectives/ | medium | Numerator-alignment rule |
| [assumption] Incident duration multiplied by workflow throughput is the least misleading fallback when affected executions are not logged directly. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/sre-book/tracking-outages/ | low | Estimation fallback |
| [inference] Explicit matching of the same production workflow is required to keep the denominator decision-useful. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ ; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf | medium | Scope-control rule |

#### Assumptions

- [assumption] The same production workflow can be bounded operationally by objective, trigger, success condition, and consequence threshold strongly enough to support rate comparison, even when the underlying implementation differs between build and live runtime execution. [assumption; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://sre.google/sre-book/service-level-objectives/]
- [assumption] Incident duration multiplied by baseline workflow throughput is an acceptable fallback only when the service does not expose direct affected-execution counts and demand is not highly bursty within the incident window. [assumption; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/]

#### Analysis

The evidence is strongest on native denominator choice, not on a pre-existing published bridge metric, because the delivery literature and the operations literature optimise for different control questions. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]

DORA's deployment denominator is the right unit for judging release-process stability, but it is the wrong shared unit for build-versus-do comparison because it measures how often releases escape rather than how often production executions fail. [inference; source: https://dora.dev/guides/dora-metrics/]

SRE reliability practice supplies the bridge because it already treats production reliability as a property of executed requests, transactions, or pipeline completions, and that same unit can absorb failures from either a released defect or a live live-runtime execution. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

This produces a clearer investment question than either native denominator alone: for a given production workflow, which delivery mode causes more failed or degraded production executions per execution opportunity? [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]

Plausible rival denominator choices exist. Deployment count preserves delivery-process accountability, and monthly incident count preserves operations review simplicity, but neither survives translation across both control surfaces without conflating exposure with process cadence. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/tracking-outages/]

This conclusion extends the earlier repository item on variance control across delivery modes by replacing its asymmetric proxy observation with a single matched execution denominator that can be used for direct comparison. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-variance-control-comparison-across-delivery-modes.md; https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]

#### Risks, gaps, uncertainties

- Among the sources reviewed for this item, no located public source publishes a ready-made, shared denominator for direct comparison of post-pipeline build escapes and live-runtime incidents, so the final answer is a synthesis across DORA, SRE, ITIL practice framing, and NIST measurement criteria rather than a single quoted formula. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- Some organisations do not tag incidents to a single production workflow or record affected execution counts, which forces throughput-based estimation and lowers precision. [inference; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- Execution-denominator rates can still hide severity differences unless the workflow definition includes a consequence threshold or separate severity slices. [inference; source: https://sre.google/resources/practices-and-processes/measuring-reliability/]
- Low-volume workflows may require longer observation windows or statistical smoothing before the rates are stable enough for investment decisions. [assumption; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]

#### Open questions

- What minimum incident-logging fields are needed to compute affected-execution counts directly for low-volume or highly bursty production workflows? [assumption; source: https://sre.google/sre-book/tracking-outages/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- How should severity weighting be added without destroying the denominator's comparability across production workflows? [assumption; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- When a single incident spans multiple production workflows, what attribution rule best prevents double counting while preserving decision usefulness? [assumption; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

### §7 Recursive Review

- Review result: pass
- Confidence: medium
- Parity: aligned
- Retained gaps: no single-source formula for the shared denominator; fallback estimation remains assumption-shaped where direct execution tagging is missing

---

## Findings

### Executive Summary

DORA's deployment denominator is not the right shared unit for this question, because the most defensible common denominator is the count of executions of the same production workflow. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

Deployment-based change-failure rates remain useful for judging release-process stability, but they do not compare directly with live-runtime incidents because live-runtime failures can recur many times without a new release and DORA explicitly warns against disparate cross-context comparisons. [inference; source: https://dora.dev/guides/dora-metrics/]

SRE reliability guidance already measures live quality on executed demand units such as requests, yield, throughput, and end-to-end completions, so release-based escapes and live-runtime incidents can be translated onto the same execution unit once the same production workflow is matched. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

The practical rule is to count both post-pipeline build defects and live-runtime incidents as failed or materially degraded executions in the same production workflow, and to use incident-window duration multiplied by workflow throughput only as a lower-confidence fallback when direct execution tagging is unavailable. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]

### Key Findings

1. **DORA defines post-deployment build instability on a deployment denominator, because change fail rate and deployment rework rate are ratios of problematic deployments to total deployments rather than ratios of failed live transactions to all live transactions.** ([fact]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
2. **SRE defines live-service reliability on executed demand units, because the core measures are request error fraction, yield over well-formed requests, throughput, and end-to-end completion for pipeline-like systems, all of which normalise failure against actual production execution.** ([fact]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/)
3. **Deployment count cannot be the shared denominator for direct build-versus-do comparison, because live-runtime incidents can accumulate without new deployments and DORA explicitly warns that metrics become misleading when contexts or applications are not matched.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/)
4. **Calendar-time incident counts, such as incidents per month or alerts per incident, are useful for operational review but cannot support matched reliability comparison when the same production workflow has materially different execution volumes or burst patterns.** ([inference]; medium confidence; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/)
5. **The strongest common denominator is the count of executions of the same production workflow, instantiated as requests, business transactions, application programming interface calls, job runs, or stage completions depending on the service type.** ([inference]; medium confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf)
6. **A matched comparison should count post-pipeline build failures as degraded or failed executions caused by a released change, and should count live-runtime incidents as degraded or failed live executions in the same production workflow, so that both numerators sit on the same exposure base.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/testing-reliability/; https://sre.google/sre-book/service-level-objectives/)
7. **When execution-level incident tagging is missing, estimating affected executions from incident duration multiplied by baseline workflow throughput is a defensible fallback, but the confidence should be downgraded because the estimate assumes stable demand during the impact window.** ([assumption]; low confidence; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/)
8. **The denominator choice is only decision-useful when the same production workflow is explicitly matched by objective, trigger, success condition, and consequence threshold, because otherwise severity mix and blended traffic will distort the apparent reliability difference between release-based delivery and live runtime execution.** ([inference]; medium confidence; source: https://dora.dev/guides/dora-metrics/; https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] DORA defines build instability on deployment-based ratios. | https://dora.dev/guides/dora-metrics/ | medium | Native build denominator |
| [fact] SRE defines live reliability on executed demand units such as requests, yield, throughput, and end-to-end completions. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ | medium | Native live denominator |
| [inference] Deployment count cannot be the shared denominator for build-versus-do comparison. | https://dora.dev/guides/dora-metrics/ | medium | Asymmetric change cadence |
| [inference] Calendar-time incident counts are secondary views, not matched exposure denominators. | https://sre.google/sre-book/tracking-outages/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ | medium | Volume-distortion risk |
| [inference] Execution count for the same production workflow is the strongest common denominator across both modes. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ ; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf | medium | Core synthesis claim |
| [inference] Both numerators should be mapped to failed or degraded executions in the same production workflow. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/sre-book/testing-reliability/ ; https://sre.google/sre-book/service-level-objectives/ | medium | Numerator-alignment rule |
| [assumption] Incident duration multiplied by workflow throughput is the least misleading fallback when affected executions are not logged directly. | https://sre.google/sre-book/service-level-objectives/ ; https://sre.google/sre-book/tracking-outages/ | low | Estimation fallback |
| [inference] Explicit matching of the same production workflow is required to keep the denominator decision-useful. | https://dora.dev/guides/dora-metrics/ ; https://sre.google/resources/practices-and-processes/measuring-reliability/ ; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf | medium | Scope-control rule |

### Assumptions

- The same production workflow can be bounded operationally by objective, trigger, success condition, and consequence threshold strongly enough to support rate comparison, even when the underlying implementation differs between build and live runtime execution. [assumption; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://sre.google/sre-book/service-level-objectives/]
- Incident duration multiplied by baseline workflow throughput is an acceptable fallback only when the service does not expose direct affected-execution counts and demand is not highly bursty within the incident window. [assumption; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/sre-book/tracking-outages/]

### Analysis

The evidence is strongest on native denominator choice, not on a pre-existing published bridge metric, because the delivery literature and the operations literature optimise for different control questions. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]

DORA's deployment denominator is the right unit for judging release-process stability, but it is the wrong shared unit for build-versus-do comparison because it measures how often releases escape rather than how often production executions fail. [inference; source: https://dora.dev/guides/dora-metrics/]

SRE reliability practice supplies the bridge because it already treats production reliability as a property of executed requests, transactions, or pipeline completions, and that same unit can absorb failures from either a released defect or a live live-runtime execution. [inference; source: https://sre.google/sre-book/service-level-objectives/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

This produces a clearer investment question than either native denominator alone: for a given production workflow, which delivery mode causes more failed or degraded production executions per execution opportunity? [inference; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]

Plausible rival denominator choices exist. Deployment count preserves delivery-process accountability, and monthly incident count preserves operations review simplicity, but neither survives translation across both control surfaces without conflating exposure with process cadence. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/tracking-outages/]

This conclusion extends the earlier repository item on variance control across delivery modes by replacing its asymmetric proxy observation with a single matched execution denominator that can be used for direct comparison. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-16-variance-control-comparison-across-delivery-modes.md; https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/]

### Risks, Gaps, and Uncertainties

- Among the sources reviewed for this item, no located public source publishes a ready-made, shared denominator for direct comparison of post-pipeline build escapes and live-runtime incidents, so the final answer is a synthesis across DORA, SRE, ITIL practice framing, and NIST measurement criteria rather than a single quoted formula. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- Some organisations do not tag incidents to a single production workflow or record affected execution counts, which forces throughput-based estimation and lowers precision. [inference; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]
- Execution-denominator rates can still hide severity differences unless the workflow definition includes a consequence threshold or separate severity slices. [inference; source: https://sre.google/resources/practices-and-processes/measuring-reliability/]
- Low-volume workflows may require longer observation windows or statistical smoothing before the rates are stable enough for investment decisions. [assumption; source: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf; https://sre.google/resources/practices-and-processes/measuring-reliability/]

### Open Questions

- What minimum incident-logging fields are needed to compute affected-execution counts directly for low-volume or highly bursty production workflows? [assumption; source: https://sre.google/sre-book/tracking-outages/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- How should severity weighting be added without destroying the denominator's comparability across production workflows? [assumption; source: https://sre.google/resources/practices-and-processes/measuring-reliability/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- When a single incident spans multiple production workflows, what attribution rule best prevents double counting while preserving decision usefulness? [assumption; source: https://sre.google/sre-book/tracking-outages/; https://sre.google/resources/practices-and-processes/measuring-reliability/]

---

## Output

- Type: knowledge
- Description: This item produces a denominator-selection rule for direct build-versus-do reliability comparison: measure both modes as failed or degraded executions of the same production workflow, and keep deployments and calendar-time incident counts as secondary diagnostic views rather than the shared denominator. [inference; source: https://dora.dev/guides/dora-metrics/; https://sre.google/sre-book/service-level-objectives/; https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf]
- Links:
  - https://dora.dev/guides/dora-metrics/
  - https://sre.google/sre-book/service-level-objectives/
  - https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf
