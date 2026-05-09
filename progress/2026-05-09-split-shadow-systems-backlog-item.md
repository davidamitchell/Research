# 2026-05-09 -- Split shadow-systems backlog item

**Completed:**
- Removed `Research/backlog/2026-05-09-enterprise-risk-workforce-shadow-systems.md`.
- Added 8 individually scoped backlog items in `Research/backlog/`:
  - `2026-05-09-basel-iso-nist-shadow-workforce-risk-classification.md`
  - `2026-05-09-system-of-record-bypass-control-deficiencies.md`
  - `2026-05-09-process-inefficiency-vs-latent-risk-taxonomy.md`
  - `2026-05-09-cobit-cmmi-defined-process-risk-mitigation.md`
  - `2026-05-09-nist-800-53-provenance-gaps-in-shadow-artifacts.md`
  - `2026-05-09-prc-risk-scoring-unstandardized-workforce-processes.md`
  - `2026-05-09-policy-lsp-capability-debt-detection.md`
  - `2026-05-09-key-person-dependency-basel-risk-linkage.md`

## Mini-Retro

1. **Did the process work?** Yes. The umbrella question split cleanly into independent research tracks.
2. **What slowed down or went wrong?** Initial lint/test commands failed before dependencies were installed.
3. **What single change would prevent this next time?** Start by installing dev dependencies (`pip install -e ".[dev]"`) before running checks in fresh environments.
4. **Is this a pattern?** Yes. Fresh runner sessions frequently miss local tooling until bootstrap is run.
5. **Does any documentation need updating?** No additional user-facing docs were changed; this was backlog restructuring only.
6. **Do the default instructions need updating?** No new convention emerged beyond existing setup guidance.
