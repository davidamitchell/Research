# 2026-05-02 -- Research Loop (extension-systems-ai-coding-agents)

**Completed:**

Research item:
- `Research/completed/2026-05-01-extension-systems-ai-coding-agents.md` -- completed; the item concludes that effective extension systems for Artificial Intelligence coding harnesses use a small stable host with explicit extension points, lifecycle-aware reload, and capability-bounded governance. It also finds that live-session extensibility widens the trust surface, so tools, provider overrides, compaction hooks, and execution interception must be treated as governed control surfaces rather than convenience features.

Sources consulted:
- https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md (Pi extension lifecycle, tool overrides, reload, and state model)
- https://code.visualstudio.com/api/advanced-topics/extension-host (Visual Studio Code runtime separation and extension-host governance model)
- https://docs.anthropic.com/en/docs/claude-code/hooks (Claude Code hook lifecycle and allow-or-deny execution controls)

## Mini-Retro

1. **Did the process work?** Yes. The research loop, external review, and targeted second-pass fixes produced a clean completed item.
2. **What slowed down or went wrong?** The first review pass caught comparative wording that overstated what the cited evidence directly supported, so I had to narrow two findings before the final pass.
3. **What single change would prevent this next time?** No additional process change is needed; the existing review rubric already exposed the comparative-claim issue quickly enough to correct it.
4. **Is this a pattern?** Yes. It matches the known comparative-claim coverage pattern already documented in the repo instructions, not a new recurring class.
