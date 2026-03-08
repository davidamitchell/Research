# 2026-03-08 — Add context engineering research backlog item

**Added:**

- `Research/backlog/2026-03-08-context-engineering-first-principles.md` — new backlog item: *Context engineering: first principles of steering LLM output without control*

**Summary:**

New research item created from owner input. The hypothesis is that context engineering (prompts, system instructions, agent instructions, RAG, tools, examples, memory injection, etc.) serves two coupled but distinct purposes:

1. **Token-level compliance** — making the next predicted token, and the sequence that follows, more likely to be what we want: compliant, truthful, coherent, cohesive. Context shapes the probability distribution over the vocabulary at each generation step.
2. **Goal-level outcome** — making the overall interaction more likely to achieve its intended purpose, independent of moment-to-moment token quality.

The framing of "steering without control" — structurally analogous to how humans influence other humans through framing, priming, and social context without directly controlling their choices — is the lens through which novel, first-principles approaches are to be sought.

**Cross-references noted in the item (to be updated when this item completes):**
- `2026-02-28-ai-control-testing-and-assurance.md` — compliance and assurance angle
- `2026-03-01-context-mode-llm-context-compression.md` — context compression as downstream application
- `2026-03-04-sdlc-ai-prompt-patterns.md` — empirical prompt patterns to explain at first-principles level
- `2026-03-03-research-loop-quality-prompt-engineering.md` — prompt quality improvement evidence
- `2026-02-28-predictive-processing-active-inference.md` — brain-as-prediction-machine analogy
- `2026-02-28-controlled-hallucination-perception-as-construction.md` — perception as active construction
- `2026-03-05-general-agent-optimization-framework.md` — agent optimisation and context as input
