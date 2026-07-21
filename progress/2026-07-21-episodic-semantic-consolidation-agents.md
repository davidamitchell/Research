# 2026-07-21 -- Research Loop (episodic-semantic-consolidation-agents)

**Completed:**

Research item:
- `Research/completed/2026-07-20-episodic-semantic-consolidation-agents.md` -- completed; the item distinguishes generalization techniques from the companion architecture study and finds that current systems can generate semantic abstractions through summaries, triplets, graphs, and cross-episode reflections, but usually rely on heuristic promotion triggers rather than calibrated evidence thresholds. It also finds that current benchmarks such as LoCoMo and LongMemEval test downstream memory competence and updates, but do not directly score whether a semantic abstraction was the right one to promote at write time.

Sources consulted:
- https://arxiv.org/abs/2410.10813 (LongMemEval benchmark and memory-design analysis)
- https://arxiv.org/abs/2407.04363 (AriGraph episodic-plus-semantic memory graph architecture)
- https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/ (AgentCore episode extraction, reflection, and confidence scoring)

## Mini-Retro

1. **Did the process work?** Yes. The research, review, fix, and complete loop worked end to end, and the second review pass incremented `review_count` as expected.
2. **What slowed down or went wrong?** The first draft used the workflow's requested plain-prose Findings Executive Summary, but the review workflow still enforced inline epistemic labels there. A later review also caught missing expansion of TBox and ABox in cross-item boundary text.
3. **What single change would prevent this next time?** Extend the research prompt's terminology sweep examples to include TBox and ABox so description-logic terms are caught before the first review pass.
4. **Is this a pattern?** Partly. First-use terminology misses remain a recurring class in this repo, although TBox and ABox are a new instance rather than a long-running exact repeat.
