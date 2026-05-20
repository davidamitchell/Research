# 2026-05-20 -- Add backlog item (information-density-filtering-financial-rag)

**Completed:**
- `Research/backlog/2026-05-20-information-density-filtering-financial-rag.md` — added from issue "Research question"; scoped a validated question on pre-retrieval information-density filtering and deduplication controls for financial Retrieval-Augmented Generation (RAG) risk workflows.

## Related

- `Research/_template.md`
- `Research/README.md`
- `.github/copilot-instructions.md`

## Mini-Retro

1. **Did the process work?** Yes. The issue content was specific enough to derive a motivated and scoped research question without interactive clarification.
2. **What slowed down or went wrong?** The skills submodule was not initialized in this fresh clone, so the research-question skill file was initially unavailable.
3. **What single change would prevent this next time?** Initialize `.github/skills` at session start in fresh clones before applying repository skills.
4. **Is this a pattern?** Yes. Fresh clone sessions commonly require explicit submodule initialization before skill-based workflows.
5. **Does any documentation need updating?** No; existing instructions already document both the new-research-item workflow and skills setup requirement.
6. **Do the default instructions need updating?** No additional instruction changes are needed for this issue type.

---

# 2026-05-20 -- Complete research item (information-density-filtering-financial-rag)

**Completed:**
- `Research/completed/2026-05-20-information-density-filtering-financial-rag.md` — completed the research item with a reviewed synthesis on pre-retrieval corpus hygiene, duplicate-family control, low-information suppression, and governance requirements for financial Retrieval-Augmented Generation (RAG) workflows.
- `learnings.md` — updated Thread 19 with the new corpus-hygiene corollary for authoritative knowledge supply chains.

## Related

- `Research/completed/2026-05-20-information-density-filtering-financial-rag.md`
- `learnings.md`
- `.github/copilot-instructions.md`

## Mini-Retro

1. **Did the process work?** Yes, but only after iterating through multiple review cycles that surfaced real citation-discipline and cross-item-synthesis gaps.
2. **What slowed down or went wrong?** The review workflow can finish with a successful GitHub Actions conclusion while the embedded report still says `OVERALL: FAIL`, so the log had to be treated as the real gate.
3. **What single change would prevent this next time?** Make the review workflow fail the job whenever the generated report contains `OVERALL: FAIL`, not just when the action step itself exits non-zero.
4. **Is this a pattern?** Yes. Workflow-level success masking report-level failure is the same class of false-green signal as prior automated-review drift.
5. **Does any documentation need updating?** No user-facing documentation needed changes beyond the mandatory learnings update tied to this completed item.
6. **Do the default instructions need updating?** No additional instruction change is needed in this session because the task prompt already warned against trusting the workflow conclusion alone.
