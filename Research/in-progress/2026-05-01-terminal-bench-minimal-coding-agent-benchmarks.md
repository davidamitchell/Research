---
title: "What does TerminalBench reveal about minimal toolsets and coding agent performance?"
added: 2026-05-01T08:17:39+00:00
status: reviewing
priority: high
blocks: []
tags: [agentic-ai, agentic-coding, agent-tooling, evaluation, llm]
started: 2026-05-02T00:06:44+00:00
completed: ~
output: []
cites: [2026-04-20-harness-selection-tools-agents-skills-prompts-instructions, 2026-05-01-ai-coding-harness-quality-benchmarks, 2026-05-01-appropriate-task-selection-coding-agents, 2026-05-01-coding-agent-context-management-transparency]
related: [2026-03-08-ai-coding-harnesses-agent-philosophy]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What does TerminalBench reveal about minimal toolsets and coding agent performance?

## Research Question

What does the TerminalBench benchmark reveal about the relationship between toolset minimalism and coding agent performance, and what design principles does it suggest for effective Artificial Intelligence (AI) coding agent harnesses?

## Scope

**In scope:**
- TerminalBench benchmark design: what it measures, how it works, and what the public 1.0 and 2.0 leaderboards expose
- Benchmark-native minimal agents, especially Terminus 1 and Terminus 2, and how they differ from installed product-native agents such as Claude Code and Codex Command Line Interface (CLI)
- Public leaderboard comparisons across model families to test whether minimal terminal-native harnesses consistently outperform richer harnesses
- Design implications for coding-agent harnesses: what appears essential, what appears harmful, and what remains uncertain
- Comparison with Software Engineering Benchmark (SWE-bench) and HumanEval to clarify what TerminalBench captures that those benchmarks do not

**Out of scope:**
- Training methodology of individual models
- Private or non-public leaderboard snapshots that cannot be independently verified
- A full survey of all coding benchmarks
- Claims about graphical user interface (GUI) agents beyond what TerminalBench publicly documents

**Constraints:**
- Prioritize primary sources: the Terminal-Bench paper, repository, leaderboard, and source code
- Treat leaderboard claims as time-sensitive
- Distinguish directly observed benchmark mechanics from causal explanations inferred from surrounding evidence

## Context

- Mario Zechner's public Pi post and related tooling posts argue that hidden context injection and large tool menus make coding agents less predictable and harder to debug. [fact; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/]
- Terminal-Bench now exposes both benchmark-native agents such as Terminus and installed product-native agents such as Claude Code and Codex Command Line Interface (CLI) on public leaderboards, which makes harness-level comparison possible without relying only on anecdotes. [fact; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://github.com/laude-institute/terminal-bench]
- The practical question is therefore not whether minimalism is aesthetically appealing, but whether a smaller, more legible tool surface produces better terminal-task outcomes than richer harnesses when both are exposed to the same benchmark. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

## Approach

1. **Benchmark mechanics** - Read the Terminal-Bench paper, repository, docs, and source files for Terminus and installed-agent adapters.
2. **Leaderboard analysis** - Use the official 1.0 and 2.0 leaderboards to compare benchmark-native minimal agents against richer installed agents within the same model families where possible.
3. **Causal hypotheses** - Review public explanations from benchmark code and Mario Zechner's posts for why smaller tool surfaces may help or hurt.
4. **Benchmark comparison** - Compare TerminalBench with SWE-bench and HumanEval to isolate the control surface it measures.
5. **Design principles** - Convert the evidence into concrete harness-design rules.

## Sources

- [x] [Merrill et al. (2026) Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868)
- [x] [Laude Institute (2026) Terminal-Bench repository](https://github.com/laude-institute/terminal-bench)
- [x] [Laude Institute (2026) Terminal-Bench 1.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/1.0)
- [x] [Laude Institute (2026) Terminal-Bench 2.0 leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0)
- [x] [Laude Institute (2026) Terminal-Bench first steps](https://www.tbench.ai/docs/first-steps)
- [x] [Laude Institute (2026) Terminal-Bench submitting guide](https://www.tbench.ai/docs/submitting-to-leaderboard)
- [x] [Laude Institute (2026) TmuxSession implementation](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/terminal/tmux_session.py)
- [x] [Laude Institute (2026) Terminus 1 agent implementation](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py)
- [x] [Laude Institute (2026) Terminus 2 agent implementation](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py)
- [x] [Laude Institute (2026) Abstract installed agent implementation](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py)
- [x] [Laude Institute (2026) Claude Code adapter](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/claude_code/claude_code_agent.py)
- [x] [Laude Institute (2026) Codex adapter](https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/codex/codex_agent.py)
- [x] [Jimenez et al. (2024) SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770)
- [x] [Princeton Natural Language Processing (2026) SWE-bench repository](https://github.com/princeton-nlp/SWE-bench)
- [x] [Chen et al. (2021) Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)
- [x] [OpenAI (2026) HumanEval repository](https://github.com/openai/human-eval)
- [x] [Zechner (2025) What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [x] [Zechner (2025) Model Context Protocol versus Command Line Interface: Benchmarking Tools for Coding Agents](https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/)
- [x] [Zechner (2025) What if you don't need Model Context Protocol at all?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)
- [x] [Prior repo item: Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md)
- [x] [Prior repo item: Artificial Intelligence coding harness quality benchmarks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md)
- [x] [Prior repo item: Task selection criteria for coding agents](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md)
- [x] [Prior repo item: Transparent context management in coding agent harnesses](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md)

## Related

- [Artificial Intelligence coding harness quality benchmarks](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md)
- [Harness-level selection and use of tools, agents, skills, prompts, and instruction files](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md)
- [What criteria define tasks where Artificial Intelligence coding agents reliably add value versus where they introduce systemic risk?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Research question: what does TerminalBench actually show about minimal versus richer coding-agent tool surfaces, and which harness-design principles follow from the public evidence?
- Scope: public Terminal-Bench mechanics, public leaderboard evidence, comparison with SWE-bench and HumanEval, and practical harness implications.
- Constraints: use primary sources first, keep time-sensitive leaderboard claims tied to accessible pages, and separate observed benchmark facts from causal inference.
- Output format: structured investigation plus mirrored Findings.
- [fact] The most relevant prior completed items in this repository are the benchmark-map item, the harness-artifact-selection item, the task-selection item, and the context-transparency item, because this question sits at the intersection of benchmark choice, tool-surface design, and bounded-task reliability. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md]
- [assumption] Working hypothesis: TerminalBench will show that a narrow terminal-native interface is a strong baseline, but not that minimalism alone is sufficient to beat every richer harness. Justification: public leaderboards expose large within-model harness spreads, which suggests harness complexity sometimes hurts and sometimes helps.

### §1 Question Decomposition

- **A. What does TerminalBench measure?**
  - A1. What are the tasks, environments, and verification rules?
  - A2. How does the benchmark expose a terminal to the agent?
  - A3. What counts as a solved task?
- **B. What does "minimal harness" mean in TerminalBench?**
  - B1. What tools do Terminus 1 and Terminus 2 actually use?
  - B2. How are installed agents such as Claude Code and Codex Command Line Interface (CLI) integrated?
  - B3. Does the benchmark itself force all agents through the same minimal interface?
- **C. What do the public leaderboards show?**
  - C1. How much do scores vary across harnesses for the same model family?
  - C2. Do minimal benchmark-native harnesses consistently beat richer native harnesses?
  - C3. What is the strongest claim that the accessible data supports?
- **D. Why might smaller tool surfaces help?**
  - D1. What public evidence exists for context bloat, hidden state, or tool confusion?
  - D2. What alternative explanations might also account for score differences?
- **E. How does TerminalBench differ from SWE-bench and HumanEval?**
  - E1. What does HumanEval measure?
  - E2. What does SWE-bench measure?
  - E3. What extra control surface does TerminalBench add?
- **F. What harness-design principles follow?**
  - F1. What should be kept minimal?
  - F2. What should be explicit rather than hidden?
  - F3. When are richer helpers justified?

### §2 Investigation

#### Search and source notes

- [assumption] Failed primary-source search note: queries `site:github.com/The-Focus-AI/youtube-feed TerminalBench Mario Zechner`, `site:tbench.ai "2025-12" "terminal-bench"`, and `site:github.com/laude-institute/terminal-bench-leaderboard 202512 terminal-bench-core` did not surface a preserved public transcript of the motivating talk or a separate December 2025 1.0 snapshot in this session. Justification: the analysis below therefore relies on the accessible Mario posts, the official public 1.0 leaderboard page, and the live 2.0 leaderboard page that still contains December 2025 rows.
- [assumption] Source substitution note: the initial repository reference pointed indirectly at a non-resolving owner name in one tool path, so the accessible official repository and documentation paths used here are the Laude Institute GitHub repository and the tbench.ai documentation pages. Justification: those are the URLs linked from the accessible README and paper.

#### A. TerminalBench measures end-to-end terminal task completion in real environments

- [fact] The Terminal-Bench paper defines Terminal-Bench 2.0 as a curated hard benchmark of 89 tasks in computer terminal environments, with unique environments, human-written solutions, and comprehensive verification tests, and reports that frontier models and agents score below 65 percent on that release. [source: https://arxiv.org/abs/2601.11868]
- [fact] The repository README describes Terminal-Bench as a dataset of tasks plus an execution harness, where each task includes an English instruction, a test script, and an oracle solution, and where the harness connects a language model to a sandboxed terminal environment. [source: https://github.com/laude-institute/terminal-bench]
- [fact] The public 1.0 leaderboard corresponds to `terminal-bench-core==0.1.1`, while the public 2.0 leaderboard uses `terminal-bench@2.0` via Harbor and reports accuracy as the public score field. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://www.tbench.ai/docs/submitting-to-leaderboard]
- [fact] The benchmark terminal surface is implemented through a tmux-backed session that can send exact keystrokes and capture the pane state, which means the benchmark is evaluating command-line interaction and terminal state management, not only code-diff generation. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/terminal/tmux_session.py]

#### B. In TerminalBench, "minimal harness" refers to benchmark-native agents that act through terminal keystrokes and terminal state

- [fact] Terminus 1 asks the model to return keystrokes, blocking choices, and expected timeouts, then executes those keystrokes through `TmuxSession.send_keys()` and reads the resulting terminal state through `capture_pane()`. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/prompt-templates/terminus.txt]
- [fact] Terminus 2 follows the same benchmark-native pattern, with the model emitting keystrokes plus wait durations, while the harness truncates long terminal output, may summarize context when tokens run low, and still relies on terminal-state reads rather than a broad tool catalog. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/prompt-templates/terminus-json-plain.txt]
- [fact] Terminal-Bench also supports installed product-native agents by installing them into the task container and invoking them through shell commands, and its abstract installed-agent adapter warns that this path is a last resort because extra dependencies and container properties can break runs for reasons other than task-solving ability. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]
- [fact] The Claude Code adapter exposes a large allowed-tools set including Bash, Edit, Write, Read, Glob, Grep, WebFetch, Notebook operations, todo operations, and delegated agents, while the Codex adapter invokes `codex exec` with full-access sandbox flags inside the container. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/claude_code/claude_code_agent.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/codex/codex_agent.py]
- [inference] TerminalBench therefore does not force every submission through one minimal interface; instead, it places benchmark-native terminal agents and richer installed product agents on the same task set, which makes harness architecture itself part of what the leaderboard reveals. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

#### C. The public leaderboards show that harness choice matters a great deal, but they do not show a universal "minimal always wins" pattern

- [fact] On the public 1.0 leaderboard, Claude Sonnet 4 spans from 30.6 percent with Terminus 1 to 54.8 percent with Ante, while Claude Code scores 35.5 percent and OpenHands scores 41.3 percent, which shows a large harness-dependent spread within one model family. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0]
- [fact] On the public 1.0 leaderboard, GPT-5 spans from 30.0 percent with Terminus 1 to 52.5 percent with Droid, with Terminus 2 at 41.3 percent and Apex2 at 49.3 percent, which again shows double-digit harness variation for closely related model entries. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0]
- [fact] On the public 2.0 leaderboard, the accessible December 2025 GPT-5.2 rows show Droid at 64.9 percent, Codex Command Line Interface (CLI) at 62.9 percent, and Terminus 2 at 54.0 percent. [source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [fact] On the public 2.0 leaderboard, the accessible December 2025 Claude Opus 4.5 rows show Droid at 63.1 percent, Letta Code at 59.1 percent, Terminus 2 at 57.8 percent, Claude Code at 52.1 percent, OpenHands at 51.9 percent, and OpenCode at 51.7 percent. [source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [fact] On the public 2.0 leaderboard, the accessible late-2025 Gemini 3 Pro rows show II-Agent at 61.8 percent, Terminus 2 at 56.9 percent, and Letta Code at 56.0 percent. [source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] The strongest leaderboard-supported claim is that minimal benchmark-native agents are competitive and often beat some richer native harnesses, not that they consistently beat the best richer harness for each model family. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] A second supported claim is that harness architecture materially changes observed performance even when the underlying model family stays similar, which means TerminalBench is measuring system design quality as much as raw model capability. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]

#### D. The public evidence supports several plausible reasons why smaller tool surfaces can help, but it does not isolate a single causal mechanism

- [fact] Mario Zechner argues that context engineering is paramount for coding agents, that existing harnesses often inject context behind the user's back, and that larger, shifting system prompts and tool menus make behavior less predictable. [source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]
- [fact] Zechner's CLI-versus-Model Context Protocol (MCP) essay argues that many MCP servers consume unnecessary context, expose too many tools, and often perform worse than direct shell use because standard command-line tools are already well learned and more composable. [source: https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]
- [fact] Zechner's later post argues more generally that many MCP servers are inefficient because large tool menus and lengthy descriptions consume context while hiding a simpler Bash-and-code alternative. [source: https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/]
- [fact] Prior completed work in this repository already found that transparent context control and bounded task structure are recurring control surfaces for coding-agent reliability. [source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-appropriate-task-selection-coding-agents.md]
- [inference] These sources make context pollution, hidden state, and tool-selection burden plausible explanations for why a terminal-native interface can outperform some richer agents, because the benchmark-native agents expose one regular interaction surface instead of many heterogeneous tools. [source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py]
- [inference] An alternative explanation is operational fit rather than pure cognitive simplicity: installed agents carry their own installation, dependency, and sandbox assumptions into the benchmark container, so part of the score spread may come from packaging friction and environment mismatch rather than from tool-count differences alone. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://www.tbench.ai/docs/first-steps]

#### E. TerminalBench measures a control surface that HumanEval and SWE-bench do not fully cover

- [fact] HumanEval is a hand-written evaluation set for code synthesis from docstrings, with pass@k as its central metric, and its repository is an execution harness for functional correctness rather than an end-to-end agent benchmark. [source: https://arxiv.org/abs/2107.03374; https://github.com/openai/human-eval]
- [fact] SWE-bench evaluates whether a model can resolve real GitHub issues by generating patches for codebases and then passing benchmark tests, and its paper emphasizes long contexts, multi-file coordination, and execution environments as the hard part. [source: https://arxiv.org/abs/2310.06770; https://github.com/princeton-nlp/SWE-bench]
- [inference] TerminalBench adds a broader operating-systems and terminal-control layer on top of coding ability, because success may require navigating shell state, interactive programs, process control, build tooling, and environment diagnosis even when the task is not naturally framed as "patch this repository issue." [source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/terminal/tmux_session.py]
- [inference] TerminalBench is therefore a stronger benchmark than HumanEval for harness design and a complementary benchmark to SWE-bench, because it reveals how much an agent depends on terminal fluency, environment control, and harness overhead rather than only patch-generation quality. [source: https://arxiv.org/abs/2107.03374; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2601.11868]

#### F. Provisional design principles

- [inference] The evidence supports keeping the core action surface small, regular, and text-native, because the benchmark-native agents remain competitive across model families even without a large built-in tool catalog. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py]
- [inference] The evidence also supports making any richer helper explicit and inspectable, because hidden context mutation and opaque tool injection are recurring public complaints, while the best richer agents appear to win by being better engineered systems rather than by merely exposing more tools. [source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [assumption] The remaining open design question is where the inflection point sits: how many helpers can a harness add before the extra state and selection burden starts hurting more than it helps? Justification: the public leaderboard exposes outcome differences, but not a controlled ablation over tool-count, hidden prompts, or context volume.

### §3 Reasoning

- [fact] TerminalBench directly observes end-to-end terminal-task outcomes under public harness implementations and public leaderboard rules. [source: https://arxiv.org/abs/2601.11868; https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [fact] Benchmark-native Terminus agents interact through keystrokes plus terminal reads, while installed agents run their own packaged command-line interfaces inside the benchmark container. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]
- [inference] Because the same benchmark hosts both styles, score spreads within model families are evidence about harness design effects, not just model-family effects. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] The public data supports "minimal can be strong and sometimes superior" more strongly than "minimal always wins," because multiple richer harnesses outrank Terminus on both 1.0 and 2.0 while Terminus still outranks some richer harnesses on the same model families. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] Mario Zechner's posts provide a plausible mechanism for the competitive strength of small tool surfaces, namely lower context pollution and fewer hidden mutations, but those posts are explanatory commentary rather than controlled causal proof for TerminalBench itself. [source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]

### §4 Consistency Check

- [fact] The paper, repository, and leaderboard all agree that Terminal-Bench is an end-to-end terminal-environment benchmark rather than a pure code-generation benchmark. [source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench; https://www.tbench.ai/leaderboard]
- [fact] The source code agrees with the documentation that Terminus is benchmark-native and terminal-driven, while Claude Code and Codex are installed agents run inside the container. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/claude_code/claude_code_agent.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/codex/codex_agent.py]
- [fact] The leaderboard examples cited in §2 are all taken from accessible public pages and do not require reconstruction from third-party summaries. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] No internal contradiction remains between the benchmark mechanics and the leaderboard interpretation: the remaining uncertainty is causal, not factual. [source: https://arxiv.org/abs/2601.11868; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

### §5 Depth and Breadth Expansion

- [inference] Technically, TerminalBench is valuable because it exposes whether a harness can maintain situational control over process state, shell state, and interactive terminal flows, which are common failure points in real coding work but weakly exercised by function-level benchmarks. [source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/terminal/tmux_session.py]
- [inference] Methodologically, TerminalBench also reveals that benchmark scores for coding agents are system scores, not model scores, because packaging, installation, permission surfaces, and tool ergonomics all feed into the final outcome. [source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]
- [inference] Economically, a smaller default tool surface is attractive because it lowers context overhead and implementation complexity, but the leaderboard also suggests that teams can justify richer scaffolding when it yields measurable gains for a target model family and task distribution. [source: https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] Behaviorally, the benchmark supports a "minimal-by-default, explicit-by-exception" philosophy more than a purist anti-tooling philosophy, because the winning systems are not tool-free, but they appear to be harnesses whose added structure pays for itself. [source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

### §6 Synthesis

**Executive summary:**

TerminalBench shows that harness design materially changes coding-agent outcomes, but the accessible public leaderboards do not support the stronger claim that minimal terminal-native harnesses consistently beat richer native harnesses across model families. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

TerminalBench measures end-to-end terminal task completion in real environments, including shell-state management, interactive terminal control, and environment diagnosis, which are not central in HumanEval and are only partly covered by SWE-bench. [fact; source: https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374]

Benchmark-native minimal agents such as Terminus 1 and Terminus 2 remain competitive and sometimes outperform richer installed harnesses, which suggests that smaller tool surfaces can reduce context burden and hidden-state failure modes. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

The design lesson is to keep the core action surface small, explicit, and terminal-native, then add richer helpers only when they deliver measured gains on the target workload. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]

**Key findings:**

1. **Terminal-Bench measures end-to-end terminal-task completion rather than isolated code generation, because each task combines an instruction, a sandboxed environment, automated verification, and, in version 2.0, 89 curated terminal tasks with human-written solutions.** ([fact]; high confidence; source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench)
2. **Benchmark-native minimal agents in TerminalBench operate primarily through exact terminal keystrokes and terminal-state reads, while installed product agents are evaluated as packaged systems running inside the benchmark container with their own dependencies and tool surfaces.** ([fact]; high confidence; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py)
3. **Public leaderboard rows show large within-model harness spreads, such as Claude Sonnet 4 on Terminal-Bench 1.0 ranging from 30.6 percent with Terminus 1 to 54.8 percent with Ante, which means harness architecture materially changes observed performance.** ([fact]; high confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0)
4. **The accessible December 2025 and surrounding Terminal-Bench 2.0 rows do not show a universal "minimal beats rich native harnesses" pattern, because GPT-5.2, Claude Opus 4.5, and Gemini 3 Pro all have richer agents above Terminus 2 on the same public leaderboard.** ([fact]; high confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0)
5. **Minimal benchmark-native agents still beat several richer native harnesses on both 1.0 and 2.0, so the public evidence supports minimalism as a strong baseline and a useful diagnostic for harness-induced overhead rather than as a guaranteed path to first place.** ([inference]; medium confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0)
6. **The most plausible public explanation for that competitiveness is lower context pollution and fewer hidden mutations, because Mario Zechner's practitioner evidence argues that oversized tool menus and opaque context injection degrade predictability, and Terminus exposes one regular terminal interaction surface.** ([inference]; medium confidence; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py)
7. **TerminalBench complements HumanEval and SWE-bench by adding shell-state management, interactive terminal control, and environment diagnosis to the evaluation target, which makes it a distinct signal about harness behavior rather than a substitute for function-level or issue-resolution benchmarks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374)
8. **The best-supported harness design rule is minimal-by-default and explicit-by-exception: keep the core terminal interaction surface small and inspectable, and justify every extra helper with measured gains rather than assuming that more built-in tools will automatically improve outcomes.** ([inference]; medium confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Terminal-Bench evaluates end-to-end terminal tasks with automated verification and curated task environments. | https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench | high | Benchmark mechanics |
| [fact] Terminus uses keystrokes plus terminal-state reads, while installed agents run as packaged systems inside the container. | https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py | high | Interface contrast |
| [fact] Harness choice produces large within-model score spreads on Terminal-Bench 1.0. | https://www.tbench.ai/leaderboard/terminal-bench/1.0 | high | Claude Sonnet 4 and GPT-5 examples |
| [fact] Terminal-Bench 2.0 public rows do not show Terminus 2 universally beating richer agents on the same model families. | https://www.tbench.ai/leaderboard/terminal-bench/2.0 | high | GPT-5.2, Claude Opus 4.5, Gemini 3 Pro |
| [inference] Minimal agents remain strong baselines and useful diagnostics for harness-induced overhead. | https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0 | medium | Competitive, not dominant |
| [inference] Lower context pollution and fewer hidden mutations are plausible reasons for minimal harness competitiveness. | https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py | medium | Mechanism, not direct ablation |
| [inference] TerminalBench complements HumanEval and SWE-bench by exposing a distinct harness-behavior signal around terminal control and environment management. | https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374 | medium | Different control surface |
| [inference] The strongest design rule is minimal-by-default and explicit-by-exception. | https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md | medium | Operational synthesis |

**Assumptions:**

- [assumption] The public leaderboard pages are sufficiently representative of the time-sensitive claim even though the original motivating talk snapshot is unavailable. Justification: the analysis cites only accessible official leaderboard rows and flags the missing transcript as a gap.
- [assumption] Richer harnesses above or below Terminus differ on more than tool-count alone. Justification: public pages rarely expose prompt design, retry policy, summarization, or hidden orchestration, so causal claims must stay moderate.
- [assumption] Model-family comparisons across near-identical names are informative but imperfect. Justification: public leaderboard naming sometimes distinguishes closely related variants such as GPT-5, GPT-5.1, GPT-5.2, and GPT-5.3-Codex.

**Analysis:**

TerminalBench shifts the comparison away from isolated code generation and toward whether a full harness can steer a model through a real terminal task. [inference; source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench]

That distinction explains why the public leaderboards reveal harness-design effects: once identical or closely related model families appear under multiple wrappers, the score spread becomes evidence about prompt shape, tool surface, installation friction, context handling, and recovery strategy. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

Several richer systems outrank Terminus 2 on the same model families, so the public leaderboard does not support a universal "simpler is always better" rule. [fact; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]

Smaller, regular, terminal-native interfaces are still competitive enough that every additional helper should earn its place empirically, because more tooling does not guarantee better results. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]

The installed-agent adapter warning matters here, because it shows that product-native scores blend agent intelligence with packaging portability and container fit. [fact; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]

That means TerminalBench should be read as a benchmark of deployable harnesses, not only of abstract reasoning policies, because packaging portability and container fit affect the published outcomes. [inference; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]

**Risks, gaps, uncertainties:**

- [assumption] The motivating talk claim can only be reconstructed from Mario Zechner's later public posts and the accessible official leaderboards, not from a retrievable public transcript of the original talk wording. Justification: the source base used here documents the underlying harness philosophy and the leaderboard outcomes, but not the exact conference phrasing. [source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [assumption] The accessible Terminal-Bench sources do not publish a controlled ablation over tool-count, prompt opacity, or hidden context injection, so the mechanism behind minimal-harness competitiveness remains inferential rather than experimentally isolated. Justification: the paper and public repo document task design and interfaces, not causal feature ablations. [source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench]
- [inference] The live leaderboard remains a moving target, so any cross-harness ranking should be treated as a snapshot rather than as a stable, once-for-all ordering. [source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- [inference] Public agent names do not reveal every hidden prompt, retry, or orchestration choice, so some observed score differences may come from undocumented implementation details rather than from visible tool surfaces alone. [source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]

**Open questions:**

- Which specific harness features explain the gap between Terminus 2 and the top richer systems on Terminal-Bench 2.0 for the same model families?
- Would a controlled benchmark ablation over tool-count, prompt size, and hidden context injection replicate the public leaderboard pattern?
- How much of the installed-agent penalty is due to packaging friction versus cognitive overhead from richer tool surfaces?
- Should a future research item compare benchmark-native minimal wrappers with intentionally transparent richer wrappers to identify the best "small but sufficient" design?

### §7 Recursive Review

- Audit status: complete.
- Acronym check: AI, Terminal User Interface (TUI), Model Context Protocol (MCP), Command Line Interface (CLI), Hypertext Transfer Protocol (HTTP), and other abbreviations used in cited source titles were expanded on first use in body text where they appear as authored prose in this item.
- Claim-label check: all claim-bearing prose in `## Research Skill Output`, `## Context`, and `## Findings` is labeled or written as metadata.
- Source-binding check: every evidentiary claim in Findings has inline URL-backed support, and every Evidence Map row includes URL-backed source cells.
- Parity check: Findings mirror the substantive claims, confidence levels, and sources from §6 Synthesis.
- Overall confidence: medium, because benchmark mechanics and leaderboard rows are strong primary evidence, while the explanation for why minimal surfaces help remains inferential rather than experimentally isolated.

---

## Findings

### Executive Summary

TerminalBench shows that harness design materially changes coding-agent outcomes, but the accessible public leaderboards do not support the stronger claim that minimal terminal-native harnesses consistently beat richer native harnesses across model families. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

TerminalBench measures end-to-end terminal task completion in real environments, including shell-state management, interactive terminal control, and environment diagnosis, which are not central in HumanEval and are only partly covered by SWE-bench. [fact; source: https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374]

Benchmark-native minimal agents such as Terminus remain competitive and sometimes outperform richer installed harnesses, which suggests that smaller tool surfaces can reduce context burden and hidden-state failure modes. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/]

The design lesson is to keep the core action surface small, explicit, and terminal-native, then add richer helpers only when they deliver measured gains on the target workload. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]

### Key Findings

1. **Terminal-Bench measures end-to-end terminal-task completion rather than isolated code generation, because each task combines an instruction, a sandboxed environment, automated verification, and, in version 2.0, 89 curated terminal tasks with human-written solutions.** ([fact]; high confidence; source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench)
2. **Benchmark-native minimal agents in TerminalBench operate primarily through exact terminal keystrokes and terminal-state reads, while installed product agents are evaluated as packaged systems running inside the benchmark container with their own dependencies and tool surfaces.** ([fact]; high confidence; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py)
3. **Public leaderboard rows show large within-model harness spreads, such as Claude Sonnet 4 on Terminal-Bench 1.0 ranging from 30.6 percent with Terminus 1 to 54.8 percent with Ante, which means harness architecture materially changes observed performance.** ([fact]; high confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0)
4. **The accessible December 2025 and surrounding Terminal-Bench 2.0 rows do not show a universal "minimal beats rich native harnesses" pattern, because GPT-5.2, Claude Opus 4.5, and Gemini 3 Pro all have richer agents above Terminus 2 on the same public leaderboard.** ([fact]; high confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0)
5. **Minimal benchmark-native agents still beat several richer native harnesses on both 1.0 and 2.0, so the public evidence supports minimalism as a strong baseline and a useful diagnostic for harness-induced overhead rather than as a guaranteed path to first place.** ([inference]; medium confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0)
6. **The most plausible public explanation for that competitiveness is lower context pollution and fewer hidden mutations, because Mario Zechner's practitioner evidence argues that oversized tool menus and opaque context injection degrade predictability, and Terminus exposes one regular terminal interaction surface.** ([inference]; medium confidence; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py)
7. **TerminalBench complements HumanEval and SWE-bench by adding shell-state management, interactive terminal control, and environment diagnosis to the evaluation target, which makes it a distinct signal about harness behavior rather than a substitute for function-level or issue-resolution benchmarks.** ([inference]; medium confidence; source: https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374)
8. **The best-supported harness design rule is minimal-by-default and explicit-by-exception: keep the core terminal interaction surface small and inspectable, and justify every extra helper with measured gains rather than assuming that more built-in tools will automatically improve outcomes.** ([inference]; medium confidence; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Terminal-Bench evaluates end-to-end terminal tasks with automated verification and curated task environments. | https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench | high | Benchmark mechanics |
| [fact] Terminus uses keystrokes plus terminal-state reads, while installed agents run as packaged systems inside the container. | https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_2/terminus_2.py; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py | high | Interface contrast |
| [fact] Harness choice produces large within-model score spreads on Terminal-Bench 1.0. | https://www.tbench.ai/leaderboard/terminal-bench/1.0 | high | Claude Sonnet 4 and GPT-5 examples |
| [fact] Terminal-Bench 2.0 public rows do not show Terminus 2 universally beating richer agents on the same model families. | https://www.tbench.ai/leaderboard/terminal-bench/2.0 | high | GPT-5.2, Claude Opus 4.5, Gemini 3 Pro |
| [inference] Minimal agents remain strong baselines and useful diagnostics for harness-induced overhead. | https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0 | medium | Competitive, not dominant |
| [inference] Lower context pollution and fewer hidden mutations are plausible reasons for minimal harness competitiveness. | https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/terminus_1.py | medium | Mechanism, not direct ablation |
| [inference] TerminalBench complements HumanEval and SWE-bench by exposing a distinct harness-behavior signal around terminal control and environment management. | https://arxiv.org/abs/2601.11868; https://arxiv.org/abs/2310.06770; https://arxiv.org/abs/2107.03374 | medium | Different control surface |
| [inference] The strongest design rule is minimal-by-default and explicit-by-exception. | https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-20-harness-selection-tools-agents-skills-prompts-instructions.md | medium | Operational synthesis |

### Assumptions

- The public leaderboard pages are sufficiently representative of the time-sensitive claim even though the original motivating talk snapshot is unavailable. [assumption; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- Richer harnesses above or below Terminus differ on more than tool-count alone, so the causal role of minimalism cannot be isolated from packaging and orchestration quality. [assumption; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- Model-family comparisons across near-identical names are informative but imperfect because the public tables distinguish closely related variants such as GPT-5, GPT-5.1, GPT-5.2, and GPT-5.3-Codex. [assumption; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]

### Analysis

TerminalBench shifts evaluation from isolated code generation toward whether a full harness can steer a model through a real terminal task. [inference; source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench]

That shift makes the public leaderboards informative for harness design, because once identical or closely related model families appear under multiple wrappers, the score spread becomes evidence about prompt shape, tool surface, installation friction, context handling, and recovery strategy. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]

Several richer systems outrank Terminus 2 on the same model families, so the public leaderboard does not support a universal "simpler is always better" rule. [fact; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0]

Smaller, regular, terminal-native interfaces are still competitive enough that every additional helper should earn its place empirically, because more tooling does not guarantee better results. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]

The installed-agent adapter warning matters because it shows that product-native scores blend agent intelligence with packaging portability and container fit. [fact; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]

TerminalBench is best read as a benchmark of deployable harnesses, not only of abstract reasoning policies, because packaging portability and container fit affect the published outcomes. [inference; source: https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-ai-coding-harness-quality-benchmarks.md]

### Risks, Gaps, and Uncertainties

- The motivating talk claim can only be reconstructed from Mario Zechner's later public posts and the accessible official leaderboards, not from a retrievable public transcript of the original talk wording. [assumption; source: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- The accessible Terminal-Bench sources do not publish a controlled ablation over tool-count, prompt opacity, or hidden context injection, so the mechanism behind minimal-harness competitiveness remains inferential rather than experimentally isolated. [assumption; source: https://arxiv.org/abs/2601.11868; https://github.com/laude-institute/terminal-bench]
- The live leaderboard remains a moving target, so any cross-harness ranking should be treated as a snapshot rather than as a stable, once-for-all ordering. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/1.0; https://www.tbench.ai/leaderboard/terminal-bench/2.0]
- Public agent names do not reveal every hidden prompt, retry, or orchestration choice, so some observed score differences may come from undocumented implementation details rather than from visible tool surfaces alone. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://github.com/laude-institute/terminal-bench/blob/main/terminal_bench/agents/installed_agents/abstract_installed_agent.py]

### Open Questions

- Which specific harness features explain the gap between Terminus 2 and the top richer systems on Terminal-Bench 2.0 for the same model families?
- Would a controlled benchmark ablation over tool-count, prompt size, and hidden context injection replicate the public leaderboard pattern?
- How much of the installed-agent penalty is due to packaging friction versus cognitive overhead from richer tool surfaces?
- Should a future research item compare benchmark-native minimal wrappers with intentionally transparent richer wrappers to identify the best small-but-sufficient design?

---

## Output

- Type: knowledge
- Description: TerminalBench supports a practical harness-design rule for coding agents: keep the default terminal interaction surface small and inspectable, and treat richer helper layers as features that must prove their value under benchmark conditions. [inference; source: https://www.tbench.ai/leaderboard/terminal-bench/2.0; https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/]
- Links:
  - https://arxiv.org/abs/2601.11868
  - https://www.tbench.ai/leaderboard/terminal-bench/2.0
  - https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
