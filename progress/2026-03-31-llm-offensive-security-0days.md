# 2026-03-31 -- Research Loop (llm-offensive-security-0days)

**Completed:**

Research item:
- `Research/completed/2026-03-31-llm-offensive-security-0days.md` -- completed; Large Language Models can now autonomously discover zero-day vulnerabilities in production-quality open source codebases (Claude Opus 4.6 found 500+ in February 2026), and GPT-4 exploits 87% of known one-day CVEs with a 91-line agent. The central governance challenge is patch velocity: LLM discovery outpaces the remediation infrastructure, with abandoned software representing a systemic gap with no clear owner.

Sources consulted:
- https://red.anthropic.com/2026/zero-days/ (Anthropic red team primary report -- Carlini et al. 2026)
- https://arxiv.org/abs/2404.08144 (Fang et al. 2024 -- GPT-4 one-day exploit benchmark)
- https://www.youtube.com/watch?v=1sd26pWhfmg (Carlini [un]prompted 2026 talk)
- https://arxiv.org/abs/2406.05590 (NYU CTF Bench -- NeurIPS 2024)
- https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report (Hack The Box NeuroGrid benchmark)
- https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/ (abandoned software governance analysis)
- https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/ (Mozilla Firefox patching experience)
- https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/ (Hexstrike-AI offensive framework)
- https://nicholas.carlini.com/ (Carlini background and prior work)

## Mini-Retro

1. **Did the process work?** Yes. Web search produced primary sources (Anthropic red team blog, Fang et al. arXiv paper) and corroborating analyses. The research question was well-scoped and the empirical evidence was strong and directly verifiable.
2. **What slowed down or went wrong?** Nothing significant. The primary sources were accessible and detailed. The IoT acronym expansion was caught in the §7 review pass, which is the right point to catch it.
3. **What single change would prevent this next time?** No change needed; the self-review acronym audit in §7 caught the missed expansion as intended.
4. **Is this a pattern?** No new pattern. The IoT expansion miss is a variant of the known acronym-expansion pattern (domain-specific abbreviations are easier to miss than the standard list). The standard review audit handled it correctly.
