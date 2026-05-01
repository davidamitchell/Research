# 2026-05-01 -- Research Loop (appropriate-task-selection-coding-agents)

**Completed:**

Research item:
- `Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md` -- completed; the item argues that current coding agents are most reliable on bounded, verifier-gated, low-blast-radius work with clear change isolation, and become systemically risky on cross-cutting, judgment-heavy, or weakly verifiable tasks. It turns that evidence into a five-question delegation screen and ties the rule back to task-stratified field data, benchmark difficulty, modularity theory, and prior repository work on verifiability and feedback loops.

Sources consulted:
- https://arxiv.org/html/2602.08915v1 (task-stratified pull-request acceptance study across coding agents)
- https://arxiv.org/abs/2310.06770 (Software Engineering Benchmark, SWE-bench, repository-scale issue-resolution difficulty)
- https://www.anthropic.com/engineering/claude-code-best-practices (first-party guidance on context limits and verifier-gated workflows)

## Mini-Retro

1. **Did the process work?** Yes, after one review-fix loop; the evidence stack was strong enough, and the review workflow surfaced the exact places where the draft was making stronger claims than the sources justified.
2. **What slowed down or went wrong?** The first review pass caught two preventable issues: `§0` workflow metadata had been written as externally sourced facts, and the task-shape claim initially read as more causal than the observational evidence supported.
3. **What single change would prevent this next time?** Add an explicit self-review rule that `§0` workflow-constraint and output-format notes must be written as metadata or justified assumptions, not as externally sourced facts.
4. **Is this a pattern?** Yes, it is adjacent to the existing self-referential citation pattern: internal process notes tend to drift into externally cited prose unless the prompt blocks that move explicitly.

## Applied improvements

- Updated `research-prompt.md` to add a `§0 workflow-metadata claims` self-review check so future items do not cite outside sources for internal handling notes such as output format or evidence-discipline constraints.
