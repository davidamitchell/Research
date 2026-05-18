# 2026-05-18 -- Research Loop (ai-policy-ambiguity-institutional-knowledge-social-friction-risk)

**Completed:**

Research item:
- `Research/completed/2026-05-17-ai-policy-ambiguity-institutional-knowledge-social-friction-risk.md` -- completed; the item finds that AI-first policy clarification can speed routine access to codified guidance, but it also reduces the peer interactions that carry contextual judgment and mentoring unless organisations keep explicit human escalation paths. The strongest direct evidence supports a mixed conclusion: AI diffuses some expert practice to novices, yet delegation-heavy use weakens deeper skill formation on unfamiliar tasks.

Sources consulted:
- https://www.gsb.stanford.edu/faculty-research/working-papers/generative-ai-work (field evidence on generative AI diffusing expert practice to novices)
- https://arxiv.org/html/2601.20245v1 (direct experiment on AI assistance weakening learning on unfamiliar software tasks)
- https://www.aft.org/ae/winter1991/collins_brown_holum (cognitive apprenticeship source on how mentoring transfers reasoning and context)

## Applied improvements

- Updated `research-prompt.md` with an explicit self-review rule that analogical evidence about apprenticeship, mentoring, or tacit knowledge must stay `[inference]` unless a source directly measures the operational outcome being claimed.

## Mini-Retro

1. **Did the process work?** Mostly yes. The loop surfaced real overclaims, and the second-pass review comments were precise enough to fix quickly.
2. **What slowed down or went wrong?** I let analogical evidence about apprenticeship and coaching drift into factual claims about direct workplace behaviour, which triggered avoidable review failures.
3. **What single change would prevent this next time?** Default peer-consultation, mentoring-path, and institutional-memory displacement claims to `[inference]` unless a source directly measures those behaviours.
4. **Is this a pattern?** Yes. It is a close cousin of the existing evidence-scope and cross-source-synthesis problems already captured in the instructions, so I updated `research-prompt.md` rather than adding a new recurring-pattern row.
