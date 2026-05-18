# 2026-05-18 -- Research Loop (ai-policy-ambiguity-epistemic-risk)

**Completed:**

Research item:
- `Research/completed/2026-05-17-ai-policy-ambiguity-epistemic-risk.md` -- completed; the item finds that fluent and confident policy-assistant answers can suppress user verification even when the underlying interpretation remains uncertain. It also finds that uncertainty wording, visible source text, and escalation prompts are governance controls, while model self-reported confidence is still too weakly matched to correctness to replace external verification.

Sources consulted:
- https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/ (uncertainty wording and over-reliance experiment)
- https://arxiv.org/abs/2006.14779 (explanations increasing acceptance without improving complementary performance)
- https://arxiv.org/html/2401.01301v1 (legal-task hallucinations and weak error self-awareness)

## Mini-Retro

1. **Did the process work?** Yes, but only after two review-fix loops clarified where synthesis language was too strong for the cited evidence.
2. **What slowed down or went wrong?** Review failures concentrated on subtle epistemic-label issues, vague comparative phrasing, and domain terms that looked clear in context but still needed simpler wording.
3. **What single change would prevent this next time?** Before the first draft-review trigger, rewrite every synthesis sentence as if it had to survive hostile parsing: remove comparative phrasing, avoid specialist shorthand in Findings, and downgrade synthesis claims to inference unless a source states them directly.
4. **Is this a pattern?** Yes. It matches the existing recurring pattern that review failures often come from shorthand, over-strong synthesis wording, and first-use clarity gaps rather than missing evidence.
