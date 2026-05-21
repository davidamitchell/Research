# 2026-05-21 -- Complete research item (agentic-km-5-pillar-capability-model)

**Completed:**
- `Research/completed/2026-05-20-agentic-km-5-pillar-capability-model.md` — completed the research item with a reviewed synthesis arguing for a five-pillar enterprise Knowledge Management capability model built from separate knowledge, context, memory, governance, and operations control surfaces.
- `learnings.md` — updated Thread 12 and Thread 19 with the new control-surface and governed-knowledge-spine corollaries from this item.

## Related

- `Research/completed/2026-05-20-agentic-km-5-pillar-capability-model.md`
- `learnings.md`
- `.github/workflows/research-review.yml`

## Sources consulted

- [Anthropic Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Microsoft Multi-Agent Reference Architecture](https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
- [AWS Prescriptive Guidance: Best practices for an enterprise-ready generative AI platform](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/best-practices.html)

## Mini-Retro

1. **Did the process work?** Yes, after treating the review report itself rather than the GitHub Actions conclusion as the real quality gate and iterating until the claim labels matched the evidence strength.
2. **What slowed down or went wrong?** The review workflow can end in a superficially successful state even when the embedded report still contains `OVERALL: FAIL`, and remote pushes to `main` required repeated rebases during the research-review loop.
3. **What single change would prevent this next time?** Make `research-review.yml` fail the job whenever the generated report contains `OVERALL: FAIL`, regardless of whether the wrapper step itself exits successfully.
4. **Is this a pattern?** Yes. False-green workflow conclusions and fast-moving `main` rebases are both recurring friction points in autonomous research completion.
5. **Does any documentation need updating?** No user-facing documentation needed updating beyond the mandatory learnings refresh that captured the new synthesis.
6. **Do the default instructions need updating?** No immediate instruction change is needed because the task prompt already required reading the embedded review report rather than trusting the workflow status alone.
