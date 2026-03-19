# 2026-03-19 — Research Loop (prompt-injection-threat-landscape)

**Completed:**

Research item:
- `Research/completed/2026-03-15-prompt-injection-threat-landscape.md` — completed; the item concludes that prompt injection is now an operational security problem for tool-using agents, with indirect prompt injection as the dominant practical attack surface. It also finds that current defences are useful but partial, so the strongest near-term pattern is bounded autonomy through least privilege, blast-radius reduction, approval gates, and capability isolation.

Sources consulted:
- https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (OWASP prompt injection taxonomy, impact framing, and mitigation guidance)
- https://arxiv.org/abs/2302.12173 (Greshake et al. foundational paper on indirect prompt injection in real-world Large Language Model-integrated applications)
- https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/ (Unit 42 report on web-based indirect prompt injection observed in the wild)

## Mini-Retro

1. **Did the process work?** Yes. The item resumed cleanly from `status: reviewing`, passed the external research review on the first triggered cycle, and then completed normally.
2. **What slowed down or went wrong?** The local checkout initially lacked the `.github/skills` submodule contents, so the research skill had to be initialized before audit work. The review workflow's `Run quality review` step also took several minutes with little intermediate visibility, which slowed confirmation more than the content fix work itself.
3. **What single change would prevent this next time?** Initialize `.github/skills` at the start of any research-loop session that may need to read skill definitions or review prompts.
4. **Is this a pattern?** Partially. Missing local submodule contents is an environment/setup pattern rather than a research-quality pattern; it matches the repository rule that skills are external and read-only, but it is worth remembering as a recurring operational check.
