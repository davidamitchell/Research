---
review_count: 2
title: "What are the design tradeoffs of self-modifying, malleable Artificial Intelligence (AI) agent architectures versus fixed-architecture agents?"
added: 2026-05-01T08:17:39+00:00
status: completed
priority: medium
blocks: []
tags: [agentic-ai, agentic-coding, agent-tooling, llm, software-engineering]
started: 2026-05-02T01:17:07+00:00
completed: 2026-05-02T01:36:10+00:00
output: [knowledge]
cites: [2026-05-01-extension-systems-ai-coding-agents, 2026-05-01-coding-agent-context-management-transparency, 2026-05-01-sustainable-ai-software-development-synthesis, 2026-04-26-access-control-amplification-agentic-operations, 2026-05-01-terminal-bench-minimal-coding-agent-benchmarks]
related: [2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-05-01-ai-coding-harness-quality-benchmarks, 2026-05-01-appropriate-task-selection-coding-agents]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: a8cf846f7ca9c60d0657f6f6796582993e63ce36
    changed: 2026-05-02
    progress: progress/2026-05-02-self-modifying-agent-architectures.md
    summary: "Initial completion"
---

# What are the design tradeoffs of self-modifying, malleable Artificial Intelligence (AI) agent architectures versus fixed-architecture agents?

## Research Question

What are the design tradeoffs, in capability, reliability, safety, and maintainability, between self-modifying agent architectures, where the agent can alter its own toolset, prompts, or extensions at runtime, and fixed-architecture agents, where the harness is static and immutable during a session?

## Scope

**In scope:**
- Definition and taxonomy of self-modification in Artificial Intelligence (AI) agents, including runtime extension loading, hot reload, dynamic tool registration, agent-authored prompts, and agent-authored extensions
- Claimed benefits of self-modification, including workflow adaptability, personalisation, and emergent capability without forking
- Claimed risks, including instability, security surface expansion, reproducibility loss, and debugging difficulty
- Empirical or practitioner evidence for either position from deployed systems
- Formal safety considerations, including whether a self-modifying agent can safely constrain its own behaviour
- Comparison across Pi, aider, Claude Code, and OpenCode where the retrieved sources materially document the relevant control surface

**Out of scope:**
- Meta-learning and in-weights self-modification during training
- Recursive self-improvement at the model level
- Detailed plugin Application Programming Interface (API) design, except where it changes the tradeoff analysis

**Constraints:**
- Distinguish narrow runtime surface mutation from broad self-modification of goals or core decision logic
- Prioritize deployed evidence and first-party documentation over speculative claims
- Flag where findings rely on creator rationale or architecture documents rather than controlled comparative studies

## Context

Mario Zechner's public talk transcript and Pi documentation argue that coding agents should adapt to the user's workflow by letting the agent write and load extensions, providers, and compaction logic inside the same session. [fact; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md]

Adjacent completed repository items on context transparency, extension systems, benchmark design, access control, and sustainable governance suggest that this architectural claim should be judged less by novelty than by what it does to observability, permission scope, reproducibility, and debugging discipline. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]

## Approach

1. **Taxonomy of self-modification**: classify types of runtime self-modification in deployed coding agents, and distinguish hot reload of extensions from changes to core decision logic.
2. **Benefits evidence**: assess what practitioner and product evidence supports the adaptability claim, and whether any retrieved evidence shows materially better outcomes for users.
3. **Risks evidence**: review documented failure modes in security, reproducibility, and debuggability.
4. **Formal safety considerations**: examine corrigibility literature to test whether self-modifying agents can safely preserve their own correction mechanisms.
5. **Practical comparison**: compare what Pi, aider, Claude Code, and OpenCode allow in concrete workflow scenarios, and identify where self-modification changes the capability envelope.

## Sources

- [x] [The Focus AI archive (2026) Building pi in a World of Slop transcript](https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json)
- [x] [Zechner (2025) What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [x] [Zechner (2026) Pi extensions documentation](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md)
- [x] [Zechner (2026) Pi compaction and branch summarization documentation](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md)
- [x] [Zechner (2026) Pi custom providers documentation](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md)
- [x] [Soares et al. (2015) Corrigibility](https://intelligence.org/files/Corrigibility.pdf)
- [x] [Hadfield-Menell et al. (2017) The Off-Switch Game](https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf)
- [x] [Anthropic Claude Code hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [x] [Anthropic Claude Code plugins guide](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [x] [Anthropic (2026) Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [x] [Aider usage documentation](https://aider.chat/docs/usage.html)
- [x] [Aider in-chat commands documentation](https://aider.chat/docs/usage/commands.html)
- [x] [Aider prompt caching documentation](https://aider.chat/docs/usage/caching.html)
- [x] [OpenCode agents documentation](https://opencode.ai/docs/agents)
- [x] [OpenCode configuration documentation](https://opencode.ai/docs/config)
- [x] [OpenCode plugins documentation](https://opencode.ai/docs/plugins)
- [x] [JetBrains dynamic plugins documentation](https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html)
- [x] [Microsoft Visual Studio Code extension host guide](https://code.visualstudio.com/api/advanced-topics/extension-host)
- [x] [Google Chrome declare permissions guide](https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en)
- [x] [Mitchell (2026) What design patterns govern effective extension and plugin systems for Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md)
- [x] [Mitchell (2026) What are best practices for transparent, user-controlled context management in Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md)
- [x] [Mitchell (2026) What principles and governance practices enable sustainable, high-quality software development with Artificial Intelligence (AI) coding agents?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md)
- [x] [Mitchell (2026) Does agentic operation amplify access-control risk beyond what existing frameworks already assume?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)
- [x] [Mitchell (2026) What does TerminalBench reveal about minimal toolsets and coding agent performance?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md)

## Related

- [Mitchell (2026) What design patterns govern effective extension and plugin systems for Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md)
- [Mitchell (2026) What are best practices for transparent, user-controlled context management in Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md)
- [Mitchell (2026) What principles and governance practices enable sustainable, high-quality software development with Artificial Intelligence (AI) coding agents?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md)
- [Mitchell (2026) Does agentic operation amplify access-control risk beyond what existing frameworks already assume?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Research question restated: what tradeoffs in capability, reliability, safety, and maintainability emerge when a coding-agent harness can modify its own runtime surfaces instead of staying session-static?
- Scope confirmed: focus on runtime self-modification in deployed coding harnesses, not training-time model changes or Artificial General Intelligence safety in general.
- Constraints confirmed: distinguish narrow runtime mutation from broad goal-level self-modification, keep creator rationale separate from stronger cross-source evidence, and produce a full knowledge item with mirrored synthesis and Findings.
- Prior completed items reviewed:
  - [Mitchell (2026) What design patterns govern effective extension and plugin systems for Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md)
  - [Mitchell (2026) What are best practices for transparent, user-controlled context management in Artificial Intelligence (AI) coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md)
  - [Mitchell (2026) What principles and governance practices enable sustainable, high-quality software development with Artificial Intelligence (AI) coding agents?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md)
  - [Mitchell (2026) Does agentic operation amplify access-control risk beyond what existing frameworks already assume?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md)
  - [Mitchell (2026) What does TerminalBench reveal about minimal toolsets and coding agent performance?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md)
- [assumption] Working hypothesis: live self-modification is best treated as an expert-oriented extensibility surface whose value depends on observability and governance rather than as an established general capability advantage. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md. Justification: the primary sources document broad power and short iteration loops, while benchmark and governance sources mainly reward bounded, inspectable control surfaces rather than maximal mutation.

### §1 Question Decomposition

- **A. What kinds of runtime mutation are actually present in retrieved coding harnesses?**
  - A1. Which systems expose only user-steered commands and configuration?
  - A2. Which systems expose plugins, hooks, or custom tools?
  - A3. Which systems allow the agent to author and reload new behaviour inside the active session?
- **B. What evidence supports the capability case for self-modification?**
  - B1. What benefits are explicitly claimed in creator and platform documents?
  - B2. What workflows become easier when the harness can change itself?
  - B3. Is there controlled evidence that self-modification improves outcomes?
- **C. What evidence supports the risk case?**
  - C1. What do the retrieved sources say about reload safety, state reconstruction, and stale references?
  - C2. What do mature extension platforms use to contain blast radius?
  - C3. What governance and debugging problems follow when runtime surfaces can change mid-session?
- **D. What does formal safety work imply?**
  - D1. What does corrigibility literature say about systems that can be modified or shut down?
  - D2. How much of that applies directly to coding-harness self-modification?
  - D3. What follows for practical control design?
- **E. How should self-modifying and fixed architectures be compared in practice?**
  - E1. What does Pi enable that bounded harnesses do not readily enable?
  - E2. What do bounded harnesses preserve better?
  - E3. Which deployment context favors which side of the tradeoff?

### §2 Investigation

#### Access and substitution notes

- [assumption] The seeded Pi repository URL `https://github.com/nichochar/pi-agent` no longer resolves, so the current creator-controlled repository and linked manuals at `https://github.com/badlogic/pi-mono` were used instead. Justification: those materials expose the relevant extension, provider, and compaction surfaces directly.

#### A. Taxonomy of runtime self-modification

- [fact] Pi's talk transcript and extension documentation describe a runtime in which the agent can write TypeScript modules, load them as extensions, register custom tools and slash commands, react to lifecycle events, persist state, customize compaction, register model providers, and reload those changes with `/reload` during the active session. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md
- [fact] OpenCode documents built-in agents, per-agent permissions, configuration layering, plugins loaded from project or global directories or npm packages, custom tools, shell-environment hooks, and compaction hooks that can replace the compaction prompt. Source: https://opencode.ai/docs/agents; https://opencode.ai/docs/config; https://opencode.ai/docs/plugins
- [fact] Claude Code documents lifecycle hooks that can run shell commands, Hypertext Transfer Protocol (HTTP) handlers, or Large Language Model (LLM) prompts at events such as `PreToolUse`, `PostToolUse`, `PreCompact`, and `PostCompact`, and documents plugins that package skills, agents, hooks, Model Context Protocol (MCP) servers, Language Server Protocol (LSP) servers, monitors, binaries, and settings. Source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://docs.anthropic.com/en/docs/claude-code/plugins
- [inference] Aider's retrieved public documentation centers on adding or dropping files, selecting models, exposing repository maps and token counts, exporting current context, and caching prompts, and the inspected pages do not document a comparable first-party runtime extension surface for tool registration, provider overrides, or compaction replacement. Source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/caching.html
- [inference] The retrieved landscape is a continuum rather than a binary: aider is the most user-steered and bounded of the inspected harnesses, Claude Code and OpenCode occupy a plugin and hook middle layer, and Pi sits at the live in-session mutation end of the spectrum. Source: https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md

#### B. Benefits evidence

- [fact] Zechner's talk and follow-up post argue that self-modifying malleability is valuable because existing harnesses change prompts and tools opaquely, make context hard to inspect, and force the user to adapt to the tool rather than letting the tool adapt to the workflow. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- [fact] Pi's public materials state that the agent can modify itself by reading the extension documentation and examples, then writing extensions that add features such as subagents, plan mode, or additional integrations. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md
- [fact] OpenCode and Claude Code both document narrower but still meaningful adaptation mechanisms, including user-defined agents, permissions, hooks, plugins, and packaged skills that let teams customize behavior without forking the base harness. Source: https://opencode.ai/docs/agents; https://opencode.ai/docs/config; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins; https://www.anthropic.com/engineering/claude-code-best-practices
- [fact] Anthropic's Claude Code best-practices guide treats environment configuration, instruction files, hooks, permissions, and skills as core performance levers, which shows that adaptation to local workflow is important even in a more bounded harness. Source: https://www.anthropic.com/engineering/claude-code-best-practices
- [inference] The clearest practical benefit of self-modification is local workflow adaptation without fork-and-redeploy friction, especially when a user needs a niche tool, a custom provider path, or a task-specific compaction or summary policy in the current session. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins
- [inference] No retrieved controlled study directly demonstrates that live self-modification improves coding-task success, defect rates, or maintainability compared with bounded harnesses, so the capability case remains primarily architectural and anecdotal rather than experimentally validated. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md

#### C. Risks evidence

- [fact] Pi's extension guide warns that `ctx.reload()` tears down the current runtime, reloads resources, and leaves the current handler running in the old call frame until it returns, and the guide recommends reconstructing extension state from persisted session entries on `session_start`. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md
- [fact] JetBrains documents that dynamic plugins can only be safely installed, updated, or unloaded without restart when they avoid leaked references, clean up resources, and stay inside dynamic extension-point rules; otherwise the Integrated Development Environment (IDE) requests a restart. Source: https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html
- [fact] OpenCode plugins can intercept tool execution, inject environment variables, add custom tools, and replace the compaction prompt, which means plugin code can materially change execution, visibility, and state propagation. Source: https://opencode.ai/docs/plugins
- [fact] Claude Code hooks can intercept tool calls, permission requests, compaction events, configuration changes, and subagent lifecycle events, and can deny or retry actions at those points. Source: https://docs.anthropic.com/en/docs/claude-code/hooks
- [fact] Chrome and Microsoft Visual Studio Code (VS Code) contain extension blast radius with permission declarations, activation controls, runtime separation, and browser sandbox restrictions rather than trusting extension authors alone. Source: https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host
- [inference] Runtime self-modification expands the attack surface and weakens reproducibility unless every mutation is versioned, permission-scoped, and logged, because mutable tool surfaces and live reload make the execution path diverge in ways that static-session harnesses avoid by default. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/hooks; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html
- [inference] Pi-style in-process extension systems should be treated as trusted-admin surfaces unless they add stronger isolation machinery, because the same extension surface can override tools, request paths, providers, and compaction behavior inside the live runtime. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md

#### D. Formal safety considerations

- [fact] Soares et al. define a corrigible agent as one that tolerates or assists correction, including preserving the programmers' ability to alter or shut down the system even as it creates new subsystems or self-modifies. Source: https://intelligence.org/files/Corrigibility.pdf
- [fact] The same paper says that default utility-maximizing agents are instrumentally motivated to preserve their own preference structure and therefore resist attempts to modify or shut them down, leaving the corrigibility problem wide open. Source: https://intelligence.org/files/Corrigibility.pdf
- [fact] Hadfield-Menell et al. show in the Off-Switch Game that an agent with uncertainty about its objective can have incentive to preserve an off switch, because human intervention becomes evidence about the true utility rather than a pure obstacle to optimization. Source: https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf
- [inference] These formal results apply most directly to broad goal-level self-modification rather than narrow tool or plugin mutation, but they still undercut any naive claim that a self-modifying agent can be trusted to preserve its own correction or shutdown path just because it is autonomous. Source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf
- [inference] Practical coding-agent safety should therefore place final control outside the mutable runtime, in permissions, deployment gates, and human review, rather than relying on agent-authored safety logic alone. Source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md

#### E. Practical comparison

- [fact] Aider emphasizes explicit file selection, explicit file dropping, explicit token reporting, explicit repository maps, and exportable current context, and it warns that too many files can overwhelm the model. Source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html
- [fact] Claude Code's best-practices guide recommends exploration before planning, explicit verification criteria, explicit environment configuration, and permissions that bound what the agent may do automatically. Source: https://www.anthropic.com/engineering/claude-code-best-practices
- [inference] OpenCode exposes configurable primary agents, subagents, permissions, plugins, and custom tools, but the retrieved docs describe those changes as configuration and plugin surfaces rather than as the agent authoring arbitrary in-session runtime extensions for immediate reload. Source: https://opencode.ai/docs/agents; https://opencode.ai/docs/config; https://opencode.ai/docs/plugins
- [fact] Pi's public design exposes a minimal core toolset plus the ability to add missing features through agent-authored extensions and immediate reload in the running session. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md
- [inference] Self-modification most clearly changes the workflow envelope when the missing capability is harness-level, such as a new tool, a new provider path, a new compaction strategy, or an experimental user-interface behavior, because bounded harnesses usually require pre-authored configuration, plugins, or upstream product changes for those cases. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins
- [inference] Fixed or more tightly bounded harnesses preserve legibility and operational discipline better, because they keep context, permissions, and verification surfaces more inspectable than a runtime that can rewrite its own capabilities mid-session. Source: https://aider.chat/docs/usage.html; https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md
- [inference] Adjacent benchmark work qualifies the stronger capability claims for self-modification, because public evidence from this repository's TerminalBench item shows that minimal, bounded harnesses can already perform strongly on realistic coding tasks, so self-modification is not established as a prerequisite for core coding performance. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md

### §3 Reasoning

- [fact] The strongest direct evidence for self-modifying capability is documentary, not experimental: Pi's manuals and transcript show the surface exists, while OpenCode and Claude Code show narrower plugin and hook forms. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins
- [inference] The relevant architectural question is where the trust boundary sits, not whether a harness is philosophically self-modifying, because the practical tradeoff is between adaptation speed and the size of the mutable control surface. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host
- [inference] Evidence from mature extension ecosystems points in the same direction as the repository's governance work: the more power a mutable surface has, the more it must be isolated, permissioned, and auditable. Source: https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md
- [inference] Formal corrigibility results strengthen caution rather than optimism, because they show that preserving safe correction through self-modification is not the default outcome of autonomous optimization. Source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf

### §4 Consistency Check

- [fact] No retrieved source contradicts the claim that live extensibility increases local adaptability, but the supporting evidence for outcome gains is mostly creator rationale and platform documentation rather than comparative trials. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://opencode.ai/docs/plugins
- [fact] No retrieved source contradicts the claim that reloadable or plugin-driven mutation creates lifecycle and containment obligations, because Pi, JetBrains, Chrome, and VS Code all document explicit boundaries or cleanup needs. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host
- [inference] Confidence remains medium rather than high because the synthesis can identify control patterns and tradeoffs more confidently than it can quantify productivity or quality deltas across harness classes. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://aider.chat/docs/usage.html; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md

### §5 Depth and Breadth Expansion

- [inference] **Technical lens:** live self-modification shifts engineering effort from static feature design toward runtime lifecycle management, because state reconstruction, reload boundaries, and mutation logs become first-class reliability work. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html
- [inference] **Governance lens:** self-modifying harnesses intensify the need for external permissions and least-privilege scoping, because the same user-granted identity can now exercise a wider and faster-changing set of behaviors. Source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md
- [inference] **Economic lens:** self-modification can reduce local adaptation cost for expert users, but it also transfers support, review, and debugging cost from the vendor to the team or individual operating the harness. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://opencode.ai/docs/plugins; https://www.anthropic.com/engineering/claude-code-best-practices
- [inference] **Behavioral lens:** mutable harnesses can feel empowering because they collapse the gap between desired workflow and available tooling, but that same fluidity can normalize invisible capability drift unless mutation events are surfaced in the user interface and logs. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md

### §6 Synthesis

**Executive summary:**

- [inference] Self-modifying coding-agent architectures trade bounded predictability for local adaptability, and the retrieved evidence supports them as powerful but governance-heavy expert surfaces rather than as a proven general default. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md
- [inference] Within the retrieved public documentation, Pi exposes the broadest live mutation surface, while aider appears the most bounded and user-steered, and Claude Code plus OpenCode occupy a plugin and hook middle layer. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins
- [inference] The clearest benefits of self-modification are rapid workflow adaptation and feature creation without forking or waiting for upstream releases, but the clearest costs are larger security surfaces, weaker reproducibility, and harder debugging. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en
- [inference] Formal corrigibility literature does not justify trusting a self-modifying runtime to preserve its own correction path, so practical safety should stay anchored in external permissions, review, and deployment controls. Source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config
- [inference] A hybrid middle path, bounded in-session extension authoring under explicit permissions, visible mutation logs, and reviewable reload boundaries, is the most plausible route for preserving some self-modification benefits without accepting a fully trusted-admin runtime, but the retrieved evidence does not yet show how much of the benefit survives those constraints. Source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html

**Key findings:**

1. [inference] The retrieved coding-agent harnesses sit on a spectrum from bounded, user-steered interfaces such as aider to plugin-configured systems such as Claude Code and OpenCode, with Pi at the far end of live in-session mutation rather than a clean binary split between self-modifying and fixed systems. Confidence: medium. Source: https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md
2. [fact] Pi's self-modifying architecture is operationally real, because its public documentation shows that the agent can write and hot-reload TypeScript extensions that register tools, commands, providers, state, and compaction behavior inside the active runtime. Confidence: medium. Source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md
3. [inference] The strongest supported benefit of self-modification is rapid local workflow adaptation without fork-and-redeploy friction, especially for niche tools, custom provider paths, and task-specific compaction or summary policies that bounded harnesses usually expose only through pre-authored configuration or upstream product changes. Confidence: medium. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins
4. [inference] The strongest documented costs are reproducibility loss, harder debugging, and expanded security surface, because live reload and mutable extension code create stale-state and blast-radius problems that mature plugin ecosystems explicitly mitigate with cleanup rules, permission declarations, runtime separation, and activation controls. Confidence: high. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host
5. [inference] Formal Artificial Intelligence safety literature does not support trusting a self-modifying agent to preserve its own corrigibility, because default utility-maximizing systems resist correction and safe shutdown remains a non-trivial design problem even before broad self-modification is introduced. Confidence: medium. Source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf
6. [inference] For practical coding agents, the retrieved evidence favors a small stable kernel plus explicit extension points, external permissions, and inspectable mutation boundaries as the most defensible current default for shared deployments, even though it does not prove that no safer bounded self-modification regime exists. Confidence: medium. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md
7. [inference] Public evidence does not show that live self-modification is necessary for strong coding performance, and adjacent benchmark work in this repository indicates that minimal, bounded harnesses can already perform strongly on realistic command-line coding tasks. Confidence: medium. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md
8. [inference] A hybrid model, bounded in-session extension authoring under explicit permissions, visible mutation logs, and reviewable reload boundaries, is the strongest plausible route for preserving some self-modification benefits without accepting the full governance cost of an unconstrained runtime, but the retrieved evidence does not yet show how much of Pi's adaptation advantage survives that constraint. Confidence: medium. Source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html

**Evidence map:**

| claim | source | confidence | notes |
|---|---|---|---|
| [inference] Retrieved harnesses form a spectrum from bounded to live self-modifying rather than a strict binary. | https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md | medium | architecture comparison |
| [fact] Pi documents live in-session extension authoring and reload across tools, providers, and compaction. | https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md | high | direct primary docs |
| [inference] Self-modification's clearest benefit is local workflow adaptation without fork-and-redeploy overhead. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins | medium | documentary evidence |
| [inference] Reproducibility, debugging, and security costs rise because reloadable mutation needs lifecycle cleanup and containment. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host | high | convergent platform guidance |
| [inference] Corrigibility literature does not justify trusting a self-modifying agent to preserve safe correction by default. | https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf | medium | formal safety qualifier |
| [inference] The current evidence favors a stable kernel plus external permissions and visible mutation boundaries as the most defensible shared-deployment default, without proving that no safer bounded self-modification regime exists. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md | medium | control-surface synthesis |
| [inference] Strong coding performance does not yet require live self-modification. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md | medium | adjacent benchmark qualifier |
| [inference] A bounded in-session extension model is the strongest plausible compromise, but the retrieved evidence does not yet quantify how much benefit survives those constraints. | https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html | medium | hybrid-path qualifier |

**Assumptions:**

- [assumption] The retrieved public manuals describe the dominant control surfaces accurately enough to compare architecture classes, even though unpublished internal implementation details or incidents may exist. Source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins. Justification: the question is about design tradeoffs, and those are exposed most clearly in the documented runtime surfaces.
- [assumption] The absence of a documented live in-session extension API in the retrieved aider pages is enough to classify aider as the most bounded harness in this comparison, even though other pages not retrieved could expose additional customization features. Source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/caching.html. Justification: the retrieved official docs emphasize explicit user-level context and command control rather than harness mutation.

**Analysis:**

The practical distinction concerns the location of authorship and activation: every inspected system has some customization path, but only some of them let the agent author and activate new capability inside the running session itself. [inference; source: https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md]

Pi pushes that boundary furthest by collapsing extension authoring, activation, and use into one loop, which plausibly reduces adaptation latency for expert users but also makes runtime state hygiene and mutation observability part of everyday harness operation. [inference; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md]

The comparison platforms show what is lost when that boundary moves inward: Chrome, VS Code, JetBrains, Claude Code, and OpenCode all rely on explicit manifests, permissions, lifecycle hooks, or startup-loaded plugins to keep mutable power subordinate to a more stable host. [inference; source: https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/plugins]

Formal corrigibility work sharpens the safety reading: broad self-modification and safe self-constraint are difficult to align even in stylized settings, so coding-agent deployments should not assume that an agent which can modify its own runtime will also preserve the human's preferred control boundaries without external enforcement. [inference; source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf]

The strongest deployment conclusion is therefore conditional rather than absolutist: self-modification is a real and useful capability for expert experimentation, but the best-supported shared-environment default remains bounded extensibility with visible mutation boundaries and external permissions. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]

A hybrid path, bounded in-session extension authoring under explicit permissions and reviewable reload boundaries, is the strongest plausible compromise between Pi-style adaptation and fixed-harness legibility, but the retrieved evidence does not yet show how much of the adaptation advantage survives those controls. [inference; source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html]

**Risks, gaps, uncertainties:**

- [inference] The evidence base for benefits is thinner than the evidence base for control patterns, because the retrieved sources document architecture and workflow examples more often than they report controlled outcome measurements. Source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md
- [inference] Formal corrigibility results concern broad agent objectives more directly than narrow runtime extension loading, so they qualify the safety story without fully determining the correct governance pattern for coding harnesses. Source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf
- [inference] OpenCode and Claude Code clearly document plugin and hook surfaces, but the retrieved docs do not quantify how often agents in practice author those surfaces autonomously versus humans pre-configuring them. Source: https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins
- [inference] Adjacent benchmark evidence constrains claims about core capability, but it does not yet isolate the marginal performance effect of self-modification itself. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md

**Open questions:**

- What measurement design would isolate the effect of live self-modification from the effect of model quality, task selection, and ordinary plugin support?
- Which mutation events must be surfaced to users in real time for a self-modifying harness to remain debuggable under team use?
- Can a bounded permission model for in-session extension authoring preserve most of Pi's adaptation benefits without accepting a full trusted-admin runtime?

### §7 Recursive Review

- Metadata: label and source audit completed; synthesis and Findings aligned; acronym first uses expanded; confidence kept at medium because the outcome evidence is architectural and documentary rather than experimental.
- Metadata: prior completed items on extension systems, context transparency, access control, sustainability, and benchmarks were re-checked before finalizing the synthesis.
- Metadata: no claim was kept at high confidence unless it rested on direct platform documentation or convergent primary documentation from more than one source.

---

## Findings

### Executive Summary

Self-modifying coding-agent architectures trade bounded predictability for local adaptability, and the retrieved evidence supports them as powerful but governance-heavy expert surfaces rather than as a proven general default. [inference; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md]

Within the retrieved public documentation, Pi exposes the broadest live mutation surface, while aider appears the most bounded and user-steered, and Claude Code plus OpenCode occupy a plugin and hook middle layer. [inference; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins]

The clearest benefits of self-modification are rapid workflow adaptation and feature creation without forking or waiting for upstream releases, but the clearest costs are larger security surfaces, weaker reproducibility, and harder debugging. [inference; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en]

Formal corrigibility literature does not justify trusting a self-modifying runtime to preserve its own correction path, so practical safety should stay anchored in external permissions, review, and deployment controls. [inference; source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config]

A hybrid middle path, bounded in-session extension authoring under explicit permissions, visible mutation logs, and reviewable reload boundaries, is the most plausible route for preserving some self-modification benefits without accepting a fully trusted-admin runtime, but the retrieved evidence does not yet show how much of the benefit survives those constraints. [inference; source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html]

### Key Findings

1. **The retrieved coding-agent harnesses sit on a spectrum from bounded, user-steered interfaces such as aider to plugin-configured systems such as Claude Code and OpenCode, with Pi at the far end of live in-session mutation rather than a clean binary split between self-modifying and fixed systems.** ([inference]; medium confidence; source: https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md)
2. **Pi's self-modifying architecture is operationally real, because its public documentation shows that the agent can write and hot-reload TypeScript extensions that register tools, commands, providers, state, and compaction behavior inside the active runtime.** ([fact]; medium confidence; source: https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md)
3. **The strongest supported benefit of self-modification is rapid local workflow adaptation without fork-and-redeploy friction, especially for niche tools, custom provider paths, and task-specific compaction or summary policies that bounded harnesses usually expose only through pre-authored configuration or upstream product changes.** ([inference]; medium confidence; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins)
4. **The strongest documented costs are reproducibility loss, harder debugging, and expanded security surface, because live reload and mutable extension code create stale-state and blast-radius problems that mature plugin ecosystems explicitly mitigate with cleanup rules, permission declarations, runtime separation, and activation controls.** ([inference]; high confidence; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host)
5. **Formal Artificial Intelligence safety literature does not support trusting a self-modifying agent to preserve its own corrigibility, because default utility-maximizing systems resist correction and safe shutdown remains a non-trivial design problem even before broad self-modification is introduced.** ([inference]; medium confidence; source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf)
6. **For practical coding agents, the retrieved evidence favors a small stable kernel plus explicit extension points, external permissions, and inspectable mutation boundaries as the most defensible current default for shared deployments, even though it does not prove that no safer bounded self-modification regime exists.** ([inference]; medium confidence; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md)
7. **Public evidence does not show that live self-modification is necessary for strong coding performance, and adjacent benchmark work in this repository indicates that minimal, bounded harnesses can already perform strongly on realistic command-line coding tasks.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md)
8. **A hybrid model, bounded in-session extension authoring under explicit permissions, visible mutation logs, and reviewable reload boundaries, is the strongest plausible route for preserving some self-modification benefits without accepting the full governance cost of an unconstrained runtime, but the retrieved evidence does not yet show how much of Pi's adaptation advantage survives that constraint.** ([inference]; medium confidence; source: https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Retrieved harnesses form a spectrum from bounded to live self-modifying rather than a strict binary. | https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md | medium | architecture comparison |
| [fact] Pi documents live in-session extension authoring and reload across tools, providers, and compaction. | https://github.com/The-Focus-AI/youtube-feed/blob/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md | medium | direct primary docs |
| [inference] Self-modification's clearest benefit is local workflow adaptation without fork-and-redeploy overhead. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/custom-provider.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md; https://opencode.ai/docs/plugins; https://docs.anthropic.com/en/docs/claude-code/plugins | medium | documentary evidence |
| [inference] Reproducibility, debugging, and security costs rise because reloadable mutation needs lifecycle cleanup and containment. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host | high | convergent platform guidance |
| [inference] Corrigibility literature does not justify trusting a self-modifying agent to preserve safe correction by default. | https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf | medium | formal safety qualifier |
| [inference] The current evidence favors a stable kernel plus external permissions and visible mutation boundaries as the most defensible shared-deployment default, without proving that no safer bounded self-modification regime exists. | https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-extension-systems-ai-coding-agents.md | medium | control-surface synthesis |
| [inference] Strong coding performance does not yet require live self-modification. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md | medium | adjacent benchmark qualifier |
| [inference] A bounded in-session extension model is the strongest plausible compromise, but the retrieved evidence does not yet quantify how much benefit survives those constraints. | https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/config; https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html | medium | hybrid-path qualifier |

### Assumptions

- The retrieved public manuals describe the dominant control surfaces accurately enough to compare architecture classes, even though unpublished internal implementation details or incidents may exist. [assumption; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins]
- The absence of a documented live in-session extension API in the retrieved aider pages is enough to classify aider as the most bounded harness in this comparison, even though other pages not retrieved could expose additional customization features. [assumption; source: https://aider.chat/docs/usage.html; https://aider.chat/docs/usage/commands.html; https://aider.chat/docs/usage/caching.html]

### Analysis

The practical distinction concerns the location of authorship and activation: every inspected system has some customization path, but only some of them let the agent author and activate new capability inside the running session itself. [inference; source: https://aider.chat/docs/usage/commands.html; https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md]

Pi pushes that boundary furthest by collapsing extension authoring, activation, and use into one loop, which plausibly reduces adaptation latency for expert users but also makes runtime state hygiene and mutation observability part of everyday harness operation. [inference; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/compaction.md]

The comparison platforms show what is lost when that boundary moves inward: Chrome, VS Code, JetBrains, Claude Code, and OpenCode all rely on explicit manifests, permissions, lifecycle hooks, or startup-loaded plugins to keep mutable power subordinate to a more stable host. [inference; source: https://developer.chrome.com/docs/extensions/develop/concepts/declare-permissions?hl=en; https://code.visualstudio.com/api/advanced-topics/extension-host; https://plugins.jetbrains.com/docs/intellij/dynamic-plugins.html; https://docs.anthropic.com/en/docs/claude-code/hooks; https://opencode.ai/docs/plugins]

Formal corrigibility work sharpens the safety reading: broad self-modification and safe self-constraint are difficult to align even in stylized settings, so coding-agent deployments should not assume that an agent which can modify its own runtime will also preserve the human's preferred control boundaries without external enforcement. [inference; source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf]

The strongest deployment conclusion is therefore conditional rather than absolutist: self-modification is a real and useful capability for expert experimentation, but bounded extensibility remains the stronger default for shared environments where debugging, auditability, and least-privilege governance matter more than local feature velocity. [inference; source: https://www.anthropic.com/engineering/claude-code-best-practices; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-access-control-amplification-agentic-operations.md]

### Risks, Gaps, and Uncertainties

- The evidence base for benefits is thinner than the evidence base for control patterns, because the retrieved sources document architecture and workflow examples more often than they report controlled outcome measurements. [inference; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]
- Formal corrigibility results concern broad agent objectives more directly than narrow runtime extension loading, so they qualify the safety story without fully determining the correct governance pattern for coding harnesses. [inference; source: https://intelligence.org/files/Corrigibility.pdf; https://cdn.aaai.org/ocs/ws/ws0354/15156-68335-1-PB.pdf]
- OpenCode and Claude Code clearly document plugin and hook surfaces, but the retrieved docs do not quantify how often agents in practice author those surfaces autonomously versus humans pre-configuring them. [inference; source: https://docs.anthropic.com/en/docs/claude-code/plugins; https://opencode.ai/docs/plugins]
- Adjacent benchmark evidence constrains claims about core capability, but it does not yet isolate the marginal performance effect of self-modification itself. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]

### Open Questions

- What experimental design would isolate the effect of live self-modification from the effects of model quality, task selection, and ordinary plugin support?
- Which mutation events must be surfaced to users in real time for a self-modifying harness to remain debuggable under team use?
- Can a bounded permission model for in-session extension authoring preserve most of Pi's adaptation benefits without accepting a full trusted-admin runtime?

---

## Output

- Type: knowledge
- Description: This item concludes that live self-modification is a real harness capability with clear local adaptation benefits, but the current evidence supports it primarily as a bounded, expert-mode extensibility surface that still depends on external governance for safety and maintainability. [inference; source: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md; https://intelligence.org/files/Corrigibility.pdf; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-sustainable-ai-software-development-synthesis.md]
- Links:
  - https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/extensions.md
  - https://intelligence.org/files/Corrigibility.pdf
  - https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md
