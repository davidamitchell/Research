# 2026-05-17 -- Complete research item (aws-bedrock-capabilities)

**Completed:**
- `Research/completed/2026-05-17-aws-bedrock-capabilities.md` — completed the Bedrock capability assessment with official AWS sources, prior-item cross-references, full research-skill output, and review-clean findings.
- `learnings.md` — added this item to the existing transaction-cost and layered-control-plane thread because it sharpens the Bedrock-specific governance boundary.

## Mini-Retro

1. **Did the process work?** Yes. The research loop, manual log inspection, and final completion flow worked once I treated the workflow log rather than the run conclusion as the real pass/fail signal.
2. **What slowed down or went wrong?** The review workflow reported `success` while still carrying `OVERALL: FAIL` in the log, and the remaining violations were narrow wording and first-use-definition issues that required another pass.
3. **What single change would prevent this next time?** Make the review workflow fail the job whenever the generated report contains `OVERALL: FAIL` instead of allowing a success-shaped conclusion.
4. **Is this a pattern?** Yes. This repo already has a known pattern where the research-review workflow conclusion cannot be trusted without reading the log body.
5. **Does any documentation need updating?** No additional documentation change is needed beyond the learning-thread update because the existing repo instructions already call out the workflow-log quirk.
6. **Do the default instructions need updating?** No. The current instructions already warn that the workflow conclusion is not authoritative and that the log must be checked for the real review result.
