# 2026-05-02 -- Research Loop (sustainable-ai-software-development-synthesis)

**Completed:**

Research item:
- `Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md` -- completed; the synthesis finds that sustainable AI coding-agent use currently depends on bounded automation, explicit context and harness control, verifier-rich task routing, and protected human review capacity rather than broad autonomous delivery. It also concludes that the field is in an intermediate maturity stage: governance and workflow patterns are recurring, but the strongest direct evidence still concentrates on bounded work rather than self-modifying or extension-first architectures.

Sources consulted:
- https://www.tbench.ai/leaderboard/terminal-bench/2.0 (TerminalBench leaderboard evidence on harness performance and minimal vs richer agent setups)
- https://www.anthropic.com/engineering/claude-code-best-practices (Practitioner guidance on bounded delegation, verification, and task selection)
- https://www.gitclear.com/ai_assistant_code_quality_2025_research (Repository-scale evidence on AI-assisted throughput and code quality degradation patterns)

## Mini-Retro

1. **Did the process work?** Yes. The research-loop structure plus the automated review workflow caught both substantive wording issues and epistemic-label mistakes before completion.
2. **What slowed down or went wrong?** The review workflow's success state masked failing log output on the second-pass auto-pass path, so I had to inspect the logs directly instead of trusting the workflow conclusion alone.
3. **What single change would prevent this next time?** Add an explicit reminder to treat a successful second-pass review run as "inspect logs anyway" rather than "assume clean"; this belongs in the research-loop prompt.
4. **Is this a pattern?** Yes. It matches the broader recurring pattern that surface evaluation is insufficient and real workflow behavior has to be checked directly.

## Pending skill improvements

- None. The improvement identified here belongs in `research-prompt.md`, not in the read-only skill submodule.
