# 2026-05-18 -- Research Loop (build-mode-failure-vs-do-mode-incident-comparison-denominator)

**Completed:**

Research item:
- `Research/completed/2026-05-17-build-mode-failure-vs-do-mode-incident-comparison-denominator.md` -- completed; the item finds that the least misleading shared denominator for comparing release-stage failures with live-runtime incidents is the count of executions of the same production workflow, not deployments and not calendar time.

Cross-item synthesis:
- `learnings.md` -- updated Thread 14 to add the reliability-measurement asymmetry analogue: unmatched deployment and incident denominators can bias engineering investment just as visible cost-only metrics bias business investment.

Sources consulted:
- https://dora.dev/guides/dora-metrics/
- https://sre.google/sre-book/service-level-objectives/
- https://sre.google/resources/practices-and-processes/measuring-reliability/
- https://sre.google/sre-book/tracking-outages/
- https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf
- https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil4-practices-incident-management-3684

## Mini-Retro

1. **Did the process work?** Yes, after treating the review log as the source of truth instead of the workflow conclusion and iterating until the log showed `OVERALL: PASS`.
2. **What slowed down or went wrong?** Review failures concentrated on first-use jargon, over-strong synthesis wording, and hidden log-level failures that were not obvious from a green workflow badge.
3. **What single change would prevent this next time?** Before the first draft-review trigger, rewrite coined comparison labels into plain language and scan the rendered item for any sentence whose confidence is stronger than the cited source family can support.
4. **Is this a pattern?** Yes. It matches the recurring pattern that research review failures often come from shorthand and synthesis-strength issues rather than from missing sources.
5. **Does any documentation need updating?** No additional repo-process documentation change is needed beyond the `learnings.md` thread update captured in this session.
6. **Do the default instructions need updating?** No. The current instructions already warn about acronym and first-use clarity failures; the fix here was stricter execution, not a missing rule.
