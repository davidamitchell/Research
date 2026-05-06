# 2026-05-06 -- Research Loop (aibom-declared-construction-practice)

**Completed:**

Research item:
- `Research/completed/2026-05-06-aibom-declared-construction-practice.md` -- completed; the item concludes that both Amazon Web Services (AWS) Bedrock Agents and LangGraph support declared design-time Artificial Intelligence Bill of Materials (AIBOM) generation, but through different extraction surfaces. Bedrock is easier to inventory from managed control-plane APIs and Infrastructure as Code (IaC), while LangGraph preserves richer orchestration detail in source code and therefore depends on static-analysis conventions rather than a native export surface.

Sources consulted:
- https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetAgent.html (Bedrock control-plane configuration surface)
- https://docs.langchain.com/oss/python/langgraph/graph-api (LangGraph graph structure, state, nodes, and edges)
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-agent.html (Bedrock IaC declaration surface)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, review workflow, and completion commands worked end to end once the item matched the reviewer's placeholder and Findings-label expectations.
2. **What slowed down or went wrong?** The first review failure surfaced an under-specified rule for embedded JSON artifacts, and the second-pass log exposed a mismatch between the prompt's Findings-label guidance and the reviewer's expectation for `Hypothesis:` phrasing in Findings.
3. **What single change would prevent this next time?** Add an explicit prompt rule that embedded example artifacts must use angle-bracket extraction placeholders or fully sourced observed values, never invented instance identifiers.
4. **Is this a pattern?** Yes. It matches the broader recurring pattern where review-safe output rules are present in reviewer logic before they are made explicit in the working prompt.

## Applied improvements

- Updated `research-prompt.md` with a new representative-artifact placeholder audit rule so future embedded JSON or YAML examples must use explicit extraction placeholders or source-backed observed values.
- Updated `learnings.md` Thread 19 with the extraction-surface corollary from this item: declared AIBOM generation is feasible from both managed control planes and source-controlled orchestration code, but the automation path differs materially.

## Pending skill improvements

- The research-review skill and prompt guidance should be reconciled on Findings-label style. The reviewer currently expects `Hypothesis:` or `Speculation:` phrasing in Findings, while the prompt still instructs suffix-style bracket labels such as `[inference; source: ...]`.
