# 2026-05-31 -- Research Loop (split-authority-q6-instability-leading-indicators)

**Completed:**

Research item:
- `Research/completed/2026-05-29-split-authority-q6-instability-leading-indicators.md` -- completed; five metric families tiered by causal distance from the approval constraint (queue age, blocked-work ratio, exception volume, lead time trend, rework and unplanned capacity share) plus a shadow-work proxy provide minimum viable early-warning telemetry for split-authority delivery systems. The four warning tiers map directly to Q3 circuit-breaker triggers and Q5 control-regime shift conditions. Threshold values are calibration heuristics grounded in SRE burn-rate alerting design and Reinertsen's product development flow, not empirically validated universal values.

Sources consulted:
- https://dora.dev/guides/dora-metrics-four-keys/ (DORA four key metrics definitions)
- https://dora.dev/research/2024/dora-report/ (DORA 2024 State of DevOps Report)
- https://sre.google/workbook/alerting-on-slos/ (SRE workbook multi-window alerting design)
- https://sre.google/workbook/eliminating-toil/ (SRE workbook toil capacity guidance)
- https://econpapers.repec.org/RePEc:inm/oropre:v:9:y:1961:i:3:p:383-387 (Little's Law queueing theory)
- https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009 (Reinertsen product development flow)
- https://www.tocinstitute.org/five-focusing-steps.html (Theory of Constraints five focusing steps)

## Mini-Retro

1. **Did the process work?** Yes. The item entered Step 8 with review_count: 1 and OVERALL: FAIL. Violations were concrete and fixable. After fixing four violations (compound [fact] label, unlabeled closing sentences in §5 and Findings Analysis, em-dash), a second review ran and returned OVERALL: FAIL again with a new set of violations (unlabeled closing sentences in §2.A2/A3/A4, unlabeled §2.C preamble and Tier descriptions, unlabeled §5 behavioural opening, and repeated paragraph-opening structure in Findings Analysis). With review_count reaching 2, the item auto-passed. All violations were fixed before completion for quality.

2. **What slowed down or went wrong?** The review found new violations in the second pass that were not present in the first pass's violation list. This is the known pattern where the first review catches some missing labels and the second review catches others that were obscured by the first batch. The "closing sentence must carry its own label" rule keeps surfacing in multiple locations per review cycle.

3. **What single change would prevent this next time?** Before triggering any review, run a dedicated closing-sentence scan on every paragraph in §2, §5, and Findings Analysis: if the final sentence of a paragraph does not end with `[inference; source: ...]` or `[fact; source: ...]`, add the label. Also scan every Tier description and structural preamble sentence in §2.C for missing labels before the first review pass.

4. **Is this a pattern?** Yes. This matches the known recurring pattern "Unlabeled closing/summary sentences and §6 Synthesis / Findings Executive Summary opening sentences." The §2 Tier-description and preamble violations are a specific instance of the same class: structured list entries and introductory framing sentences that precede labelled content are repeatedly missed because they look like metadata or scaffolding but are treated as claim-bearing prose by the reviewer.
