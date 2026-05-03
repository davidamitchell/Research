# 2026-05-03 — Add backlog item (hbr-ai-positional-bias-backlog-intake)

**Completed:**
- `Research/backlog/2026-05-03-hbr-ai-positional-bias-strategic-advice-reliability.md` — added from issue "New study and follow up research questions"; validated question asks what the 2025 HBR positional bias study and related empirical research on LLM sycophancy, opinion-suppression effects, and chain-of-thought reliability reveal about the reliability of AI strategic recommendations and what countermeasures practitioners can apply

## Research Question Skill Process (applied manually — submodule not initialised)

**Three questions extracted from issue:**
1. *Decision/problem:* Whether Large Language Model (LLM) advice tools can be trusted for high-stakes decisions (health, business strategy), and how to use them effectively given known failure modes demonstrated by the Harvard Business Review (HBR) study.
2. *Constraints:* Find and review the specific HBR study, related studies (arXiv 2025, Nature Digital Medicine, Anthropic chain-of-thought reliability), and connect findings to existing research in this repository.
3. *Output type:* Knowledge (structured synthesis connecting the studies and providing practitioner countermeasures).

**Five-test quality check:**
- Specific ✓ — names the specific HBR study, specific phenomena (positional bias, sycophancy, chain-of-thought fabrication)
- Answerable ✓ — the HBR paper can be located and reviewed; related papers are findable via arXiv and Nature
- Scoped ✓ — focus on trust calibration for strategic/advisory decision contexts; out-of-scope items explicit
- Motivated ✓ — people are making health and business decisions based on AI advice that the evidence suggests is shaped by prompt framing rather than genuine analysis
- Decomposable ✓ — breaks cleanly into: (1) find/review HBR study, (2) related arXiv paper, (3) Nature Digital Medicine study, (4) Anthropic chain-of-thought research, (5) connect to existing repo research, (6) evaluate countermeasures

**Verdict: READY**

**Existing related research identified:**
- `Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md` — directly related; covers Reinforcement Learning from Human Feedback (RLHF) sycophancy mechanisms; the new item extends this with the specific HBR positional bias quantification and medical-context evidence
- `Research/completed/2026-03-12-failure-mode-taxonomy-expansion.md` — covers the sycophancy failure mode taxonomy and goal-drift mechanisms; the new item adds the strategic advice domain evidence

## Mini-Retro

1. **Did the process work?** Yes — the research-question skill process was applied manually from the documented process in `.github/copilot-instructions.md`. The five-test check confirmed the question was ready without revision needed. The existing sycophancy item provides strong context that the research agent should read before conducting this investigation.

2. **What slowed down or went wrong?** The skills submodule is not initialised, so the research-question skill was applied from documented process only. The HBR study URL is unknown at this point and is one of the primary research tasks. Several related paper URLs are also to-be-confirmed: the specific arXiv 2025 "I think/I believe" paper and the Nature Digital Medicine study.

3. **What single change would prevent this next time?** Nothing structural — the process followed correctly. The to-be-confirmed source URLs are appropriate: they are research tasks, not documentation gaps.

4. **Is this a pattern?** Skills submodule unavailability is a known pattern (documented in the Known Recurring Patterns table). Handled correctly — note the gap, apply manually, proceed.

5. **Does any documentation need updating?** No — the process followed the documented workflow for handling a new research request issue.

6. **Do the default instructions need updating?** No new conventions emerged from this session.
