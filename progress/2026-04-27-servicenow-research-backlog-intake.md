# 2026-04-27 — ServiceNow research backlog intake (issue #416)

**Completed:**
- `Research/backlog/2026-04-27-enterprise-stack-value-distribution-governance-frameworks.md` — added from issue #416; asks what frameworks (seven-layer enterprise data stack, Software Repricing Matrix, Lionus Capital Artificial Intelligence (AI) Threshold Effect, and comparable frameworks from enterprise architecture and investment analysis literature) best explain how durable economic value distributes across enterprise technology stacks as lower-layer resources commoditise, with particular focus on governance as the compounding, non-replicable layer
- `Research/backlog/2026-04-27-servicenow-orchestration-agentic-ai-roadmap.md` — added from issue #416; asks what workflow orchestration and governance capabilities ServiceNow currently provides for AI agent workloads, and what public roadmap signals (earnings calls, Knowledge conference, executive statements) indicate about their strategic direction for agentic AI orchestration
- `Research/backlog/2026-04-27-governance-moat-prior-research-implications.md` — added from issue #416; asks how the governance-as-moat thesis from the LHC ServiceNow analysis validates, challenges, or extends the AI governance architecture frameworks developed in the prior research programme (UELGF, PAP/PDP/PEP, systems capability debt, AI agent identity); this item is blocked by the two above and serves as the synthesis

**Dependency structure:**
- Item 1 (`enterprise-stack-value-distribution`) blocks item 3 (`governance-moat-implications`) — the framework inventory is needed before synthesis
- Item 2 (`servicenow-orchestration`) blocks item 3 (`governance-moat-implications`) — the ServiceNow capability facts are needed before synthesis
- Item 3 (`governance-moat-implications`) is the synthesis item; it can only start when items 1 and 2 are complete

**Issue sub-question mapping:**
- Sub-question 1 (what frameworks are discussed in the video?) → item 1, Approach step 1
- Sub-question 2 (what are other similar frameworks for architecture/value/governance?) → item 1, Approach steps 2–6
- Sub-question 3 (what does governance-as-difference-maker mean for prior research?) → item 3
- Sub-question 4 (what orchestration does ServiceNow provide, what does roadmap show?) → item 2
- Sub-question 5 (anything else?) → item 3 Approach step 6 (open questions and cross-thread learnings), which specifically addresses the "anything else" framing by looking for emergent cross-cutting implications

## Mini-Retro

1. **Did the process work?** Yes. The issue contained five sub-questions that decomposed cleanly into three research items: a frameworks catalogue item (sub-questions 1–2), a ServiceNow capability facts item (sub-question 4), and a synthesis item that connects the external investment thesis to the internal governance research programme (sub-questions 3 and 5). The dependency structure (items 1 and 2 block item 3) is correctly encoded in the `blocks` fields.

2. **What slowed down or went wrong?** The `.github/skills/` submodule was not initialised in this cloud agent environment, so the `research-question` skill could not be applied formally. Items were scoped directly from the issue content following the template structure. This is the documented fallback path and no process failure occurred — it just means the five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) was applied manually rather than through the skill's structured output.

3. **What single change would prevent this next time?** Nothing specific — the submodule-unavailable fallback path is documented and working. The manual quality check is adequate for well-structured issues like this one.

4. **Is this a pattern?** Yes — the submodule not being initialised in the cloud agent environment is a known recurring pattern documented in the MCP configuration table and the previous UELGF intake session log. No new action required.

5. **Does any documentation need updating?** No — the backlog items are self-contained. The `learnings.md` cross-cutting thread on governance-as-transaction-cost (Thread 2) is directly relevant to the governance-as-moat thesis in item 3, and this connection is noted in item 3's Sources section pointing to `learnings.md`. No update to `learnings.md` is needed until item 3 is completed.

6. **Do the default instructions need updating?** No — the instructions correctly specify the fallback path for the research-question skill and the stop-here rule for research request issues.
