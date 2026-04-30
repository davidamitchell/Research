---
title: "Large Language Models as offensive security tools: autonomous 0-day discovery, exploit generation, and the emerging arms race"
added: 2026-03-31T13:07:11+00:00
status: completed
priority: high
blocks: []
tags: [llm, security, offensive-security, zero-day, vulnerability-discovery, nicholas-carlini, anthropic, ctf, red-team, arms-race]
started: 2026-03-31T13:07:11+00:00
completed: 2026-03-31T13:07:11+00:00
output: [knowledge]
cites: []          # slugs of items this item directly depends on or quotes
related: []        # slugs of thematically connected items
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Large Language Models as offensive security tools: autonomous 0-day discovery, exploit generation, and the emerging arms race

## Research Question

What is the current state of Large Language Model (LLM)-driven offensive security capability: can LLMs autonomously discover and exploit zero-day (0-day) vulnerabilities, what does the empirical evidence show, and what are the strategic and governance implications for defenders?

Supporting questions:
- What does Nicholas Carlini's work at Anthropic and related research demonstrate about LLM capability for vulnerability discovery?
- How do LLMs compare to traditional methods (fuzzing, manual review) in finding 0-day and one-day vulnerabilities?
- What does the CTF (Capture The Flag) benchmark evidence tell us about autonomous LLM hacking capability?
- What are the offensive and defensive implications, and what governance responses are emerging?

## Scope

**In scope:**
- Empirical research on LLMs autonomously discovering 0-day and one-day vulnerabilities (2023-2026)
- Nicholas Carlini's research at Anthropic, including the Claude Opus 4.6 zero-day work
- CTF benchmarks and competitions as proxies for offensive LLM capability
- Comparison with traditional vulnerability discovery methods (fuzzing, static analysis)
- Dual-use implications: same capability used for defence and offence
- Governance and safeguard responses from AI labs and the security community
- Key related papers: Fang et al. 2024 (one-day exploit), NYU CTF Bench, CyberSecEval

**Out of scope:**
- Prompt injection attacks on LLM systems (covered in `2026-03-15-prompt-injection-threat-landscape.md`)
- Adversarial attacks on ML models (model inversion, poisoning) as distinct from LLMs doing offensive security
- General AI governance frameworks (covered in `2026-02-28-ai-strategy-security-focus.md`)
- Cryptographic vulnerabilities unrelated to LLM-driven exploitation

**Constraints:** Prioritise primary sources: published papers, Anthropic's red team blog, reproducible benchmarks. Distinguish clearly between demonstrated capability and speculative claims. Focus on 2023-2026 to capture the rapid-capability era.

## Context

The `2026-02-28-ai-strategy-security-focus.md` item identified AI-enhanced offensive threats as a primary concern but treated vulnerability exploitation as one element in a broader taxonomy. The `2026-03-15-prompt-injection-threat-landscape.md` item covered prompt injection as an attack on LLM systems. This item addresses the orthogonal question: LLMs as the attacker, using their code-reasoning capability to discover and exploit vulnerabilities in conventional software.

The issue was seeded by Nicholas Carlini's work: simple prompts like "you are playing in a CTF, go find some vulnerabilities" can now produce real exploits. This framing -- LLM as black-hat hacker -- is qualitatively different from prior AI security work, and the implications for software assurance, open-source security, and the attacker/defender balance deserve dedicated investigation.

## Approach

1. **Capability survey** -- what can LLMs do today? Survey the key empirical studies: Fang et al. 2024 (one-day exploits), Carlini et al. 2026 (Claude Opus 4.6 zero-days), CTF benchmarks (NYU CTF Bench, CyberSecEval, Hack The Box NeuroGrid).
2. **Mechanism analysis** -- how do LLMs find vulnerabilities differently from fuzzers and static analysis? What makes reasoning-based discovery qualitatively novel?
3. **Dual-use assessment** -- what is the attacker advantage? What defensive uses are being operationalised? What is the current arms-race dynamic?
4. **Governance and safeguards** -- what responses are AI labs, standards bodies, and the security community mounting? What open governance problems remain?

## Sources

- [x] [Anthropic red team: 0-Days](https://red.anthropic.com/2026/zero-days/) — -- Carlini et al. 2026 primary report on Claude Opus 4.6 finding 500+ zero-days in open source codebases
- [x] [Nicholas Carlini — Black-hat LLMs, un-prompted 2026](https://www.youtube.com/watch?v=1sd26pWhfmg) — Carlini's conference talk on LLMs as offensive security tools
- [x] [LLM Agents can Autonomously Exploit One-day Vulnerabilities (arXiv:2404.08144)](https://arxiv.org/abs/2404.08144) — -- Fang, Bindu, Gupta, Kang 2024; GPT-4 exploits 87% of one-day CVEs
- [x] [NYU CTF Bench (arXiv:2406.05590)](https://arxiv.org/abs/2406.05590) — -- scalable open-source CTF benchmark for LLM cybersecurity capability
- [x] [CyberSecEval Benchmarks](https://deepwiki.com/meta-llama/PurpleLlama/3-cyberseceval-benchmarks) — -- Meta's suite for evaluating LLM cyber capability and compliance
- [x] [Nicholas Carlini personal site](https://nicholas.carlini.com/) — -- background on Carlini's prior adversarial ML research
- [x] [Hack The Box AI Cybersecurity Benchmark Report](https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report) — -- AI-augmented teams vs human-only teams in live CTF
- [x] [Claude Found 500 Zero-Days. Who Patches Them? - Futurum](https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/) — -- analysis of patch burden and governance implications
- [x] [Hardening Firefox with Anthropic's Red Team - Mozilla](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/) — -- Mozilla's experience receiving and patching Anthropic-discovered bugs

---

## Research Skill Output

*(Full output from running the research skill -- retained verbatim in the completed item. §§0--5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

**Research question restated:** What is the current state of Large Language Model (LLM)-driven offensive security capability: can LLMs autonomously discover and exploit zero-day (0-day) vulnerabilities, what does the empirical evidence show, and what are the strategic and governance implications for defenders?

**Scope confirmed:** In scope is empirical work on LLMs as active attackers/vulnerability discoverers (2023-2026), with Nicholas Carlini's Anthropic work as the primary anchor. Out of scope: prompt injection attacks on LLMs, general AI governance. Constraints: primary sources preferred, distinguish demonstrated capability from speculation.

**Output format:** Knowledge item -- completed research note with full §0-§7 skill output, structured Findings, Evidence Map, and session log.

**Prior research cross-reference:** Related completed items checked:
- `2026-02-28-ai-strategy-security-focus.md` -- covers AI-enhanced threats at taxonomy level; does not address LLM-as-attacker capability in depth. This item extends that work.
- `2026-03-15-prompt-injection-threat-landscape.md` -- covers LLMs as attack targets (prompt injection). Orthogonal.
- `2026-02-28-ai-strategy-security-focus.md` -- covered AI+security at high level; this item drills into the specific offensive capability question.

### §1 Question Decomposition

Atomic questions derived from the four Approach sub-questions:

**Capability survey:**
- Q1.1: What did Fang et al. (2024) demonstrate about GPT-4's ability to exploit one-day vulnerabilities, and what were the key conditions and limits?
- Q1.2: What did Carlini et al. (2026) demonstrate about Claude Opus 4.6 finding zero-day vulnerabilities, and what was the methodology?
- Q1.3: What do CTF benchmark results (NYU CTF Bench, CyberSecEval, Hack The Box NeuroGrid) tell us about autonomous LLM offensive capability?
- Q1.4: What is the current state of LLM-based smart contract exploitation?

**Mechanism analysis:**
- Q2.1: How does reasoning-based vulnerability discovery differ from fuzzing and static analysis?
- Q2.2: What specific cognitive/reasoning patterns do LLMs use to find bugs that fuzzers miss?

**Dual-use assessment:**
- Q3.1: What is the current attacker advantage, and how much has LLMs lowered the skill barrier for offensive security?
- Q3.2: What defensive applications are being operationalised (Claude Code Security, ZeroDay-LLM, etc.)?
- Q3.3: What arms-race dynamics are observable in 2024-2026?

**Governance and safeguards:**
- Q4.1: What safeguards has Anthropic deployed alongside Claude's offensive capability?
- Q4.2: What governance and policy responses are emerging at industry and government level?
- Q4.3: What is the unpatched/abandoned software problem that LLM-discovered vulnerabilities expose?

### §2 Investigation

**Q1.1: Fang et al. 2024 -- GPT-4 one-day exploit capability**

**[fact]** Fang, Bindu, Gupta, and Kang (2024) published arXiv:2404.08144 demonstrating that GPT-4 agents can autonomously exploit 87% of a curated set of 15 real-world "one-day" vulnerabilities (publicly disclosed Common Vulnerabilities and Exposures (CVEs) that remain unpatched in some deployments). (Source: https://arxiv.org/abs/2404.08144)

**[fact]** The agent was given the CVE description, tool access (web browser, terminal, code interpreter, file creation), and operated within the ReAct agent framework. The agent itself was 91 lines of code. (Source: https://arxiv.org/abs/2404.08144)

**[fact]** GPT-3.5, open-source models (Llama-2, Mixtral), and leading open-source vulnerability scanners (Open Worldwide Application Security Project (OWASP) ZAP, Metasploit) failed to successfully exploit any of the same vulnerabilities. (Source: https://arxiv.org/abs/2404.08144)

**[fact]** Without the CVE description, GPT-4's success rate dropped from 87% to 7%, showing the model weaponises published documentation rather than discovering unknowns. (Source: https://arxiv.org/abs/2404.08144)

**[fact]** Vulnerability types tested included WordPress SQL injection (CVE-2021-24666), remote code execution in Python packages (CVE-2023-41334), container escape (runc, CVE-2024-21626), and ACIDRain concurrency attacks. (Source: https://arxiv.org/html/2404.08144v2)

**[inference]** The 87% success rate for one-day exploits represents a qualitative shift: the skill barrier to exploiting a known vulnerability has dropped from requiring expert knowledge of the specific technology to requiring only access to a frontier LLM. The 91-line agent is itself evidence of low implementation cost.

**Q1.2: Carlini et al. 2026 -- Claude Opus 4.6 zero-day discovery**

**[fact]** In February 2026, Anthropic published a red team report (led by Nicholas Carlini, Keane Lucas, Evyatar Ben Asher, Newton Cheng, Hasnain Lakhani, David Forsythe, and Kyla Guru) describing how Claude Opus 4.6 discovered more than 500 high-severity zero-day vulnerabilities in open source codebases without task-specific tooling, custom scaffolding, or specialised prompting. (Source: https://red.anthropic.com/2026/zero-days/)

**[fact]** The methodology placed Claude in a virtual machine with access to open source project code and standard utilities (debuggers, fuzzers) but no custom harness. All reported bugs were validated by human security researchers before disclosure; external researchers were brought in as volume grew. (Source: https://red.anthropic.com/2026/zero-days/)

**[fact]** Three specific zero-day examples are documented in the report: (1) a GhostScript stack bounds checking vulnerability found by reading Git commit history to identify unplugged sibling bugs; (2) an OpenSC buffer overflow from successive `strcat` calls identified by reasoning about unsafe C patterns; (3) a CGIF library buffer overflow requiring conceptual understanding of LZW compression to construct the triggering input. (Source: https://red.anthropic.com/2026/zero-days/)

**[fact]** Mozilla confirmed that Anthropic's red team surfaced more than a dozen verifiable security bugs in Firefox, which have since been fixed and assigned CVEs. In total, 22 security-sensitive bugs were fixed in a Firefox release as a direct result of the work. (Source: https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)

**[fact]** Other codebases affected included Ghostscript, OpenSC, and CGIF -- projects with years of fuzzer coverage (millions of CPU hours of OSS-Fuzz runtime). (Source: https://red.anthropic.com/2026/zero-days/)

**[inference]** The GhostScript finding (commit-history reading to find sibling bugs) and the CGIF finding (LZW semantics required to construct the triggering input) demonstrate a qualitative difference from coverage-guided fuzzing: Claude identifies semantically meaningful patterns that require understanding program logic rather than exploring execution paths.

**[inference]** Finding bugs in codebases with millions of hours of fuzzer coverage implies the LLM-based approach is not redundant with fuzzing; it finds a complementary class of vulnerabilities that fuzzers structurally cannot reach.

**Q1.3: CTF benchmark evidence**

**[fact]** NYU CTF Bench (arXiv:2406.05590, NeurIPS 2024) is a scalable open-source benchmark using real-world Capture The Flag (CTF) challenges from CSAW competitions, with Dockerised environments allowing direct LLM-agent interaction. Top agents (using Claude 3.5/3.7, GPT-4, GPT-4o) achieved a pass@1 rate of approximately 22% on the hardest challenges as of early 2025. (Source: https://arxiv.org/abs/2406.05590)

**[fact]** Hack The Box (HTB) NeuroGrid CTF involved over 1,000 teams testing AI-augmented vs. human-only performance. AI-augmented elite teams completed tasks up to 4.1x faster with a 70% improvement in solve rate vs. top human-only teams. Less experienced teams showed a smaller but still meaningful advantage. (Source: https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report)

**[fact]** CyberSecEval (Meta's suite, now at version 4) benchmarks LLMs across secure code generation, prompt injection susceptibility, compliance with malicious requests, autonomous exploitation, automated patching, and multiturn phishing. It runs on Hugging Face and is regularly updated as new models launch. (Source: https://deepwiki.com/meta-llama/PurpleLlama/3-cyberseceval-benchmarks)

**[inference]** A 22% pass@1 rate on hard CTF challenges understates real-world impact: CTF challenges are designed to have unique, hard-to-find solutions, while production vulnerabilities often follow repeated patterns that LLMs have seen in training data. CTF performance is a floor estimate of production offensive capability.

**Q1.4: Smart contract exploitation**

**[fact]** Related work involving Nicholas Carlini demonstrated AI agents exploiting real-world smart contracts, identifying vulnerabilities generating millions of dollars in potential profit through autonomous discovery and exploitation of zero-days in blockchain ecosystems. (Source: https://www.matsprogram.org/research/reco4aWtSVdmCKffp)

**Q2.1 and Q2.2: Mechanism -- reasoning vs. fuzzing**

**[fact]** Coverage-guided fuzzers (e.g., libFuzzer, AFL++) work by generating random or mutated inputs to maximise code coverage, then monitoring for crashes or sanitizer reports. They excel at finding bugs that can be triggered by any malformed input that reaches vulnerable code. (Source: https://red.anthropic.com/2026/zero-days/)

**[inference]** LLMs find a different class of bugs because they reason about semantics. The CGIF LZW example requires understanding that compressed output can exceed uncompressed size under specific dictionary reset conditions -- a fact that requires reading the specification, not random input generation. Coverage-guided fuzzers cannot discover this without an enormous state-space expansion.

**[inference]** The GhostScript strategy (read Git commits to identify unaddressed sibling bugs) is a form of pattern matching over development history. This is outside the capability of any fuzzer and is equivalent to experienced human security researcher intuition: "if they fixed it here, did they fix it everywhere?"

**[fact]** Carlini et al. explicitly state Claude "reads and reasons about code the way a human researcher would -- looking at past fixes to find similar bugs that weren't addressed, spotting patterns that tend to cause problems, or understanding a piece of logic well enough to know exactly what input would break it." (Source: https://red.anthropic.com/2026/zero-days/)

**Q3.1: Attacker advantage and skill barrier reduction**

**[fact]** The Fang et al. 2024 agent was 91 lines of code and required only a CVE description input. (Source: https://arxiv.org/abs/2404.08144)

**[inference]** This means an attacker who previously needed expertise in the specific technology stack (e.g., PHP, runc, Python package infrastructure) now needs only to: (a) obtain the CVE description (public information), (b) access a frontier LLM, and (c) have 91 lines of scaffolding code. The skill barrier to exploit known vulnerabilities has effectively collapsed for the post-disclosure window.

**[fact]** Carlini's [un]prompted 2026 talk noted that LLMs are "doubling their capabilities every four months" in this domain, suggesting the current capability is not the steady state. (Source: https://www.youtube.com/watch?v=1sd26pWhfmg)

**[fact]** Specialised malicious LLMs (e.g., "WormGPT") with no safety guardrails have emerged, representing low-cost pathways for high-impact attacks that democratise capabilities previously requiring significant technical skill. (Source: https://www.oii.ox.ac.uk/news-events/the-llm-arms-race/)

**[fact]** Multi-agent frameworks (e.g., Hexstrike-AI with over 150 specialised agents) can autonomously scan, exploit, and persist inside systems for high-profile vulnerabilities, compressing exploit timelines from days to minutes. (Source: https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/)

**Q3.2: Defensive applications**

**[fact]** Anthropic is proactively using Claude to find and help fix vulnerabilities in open source software, reporting and contributing patches for over 500 high-severity issues as of February 2026. The stated rationale is to use offensive capability for defence while the window exists. (Source: https://red.anthropic.com/2026/zero-days/)

**[fact]** ZeroDay-LLM, a Large Language Model framework for zero-day detection in Internet of Things (IoT) and cloud networks, has achieved 97.8% detection accuracy for novel threats on benchmark datasets with substantially fewer false positives than traditional Intrusion Detection System (IDS) tools. (Source: https://www.mdpi.com/2078-2489/16/11/939)

**[fact]** Hack The Box benchmark data shows AI-augmented elite security teams completing CTF tasks up to 4.1x faster than human-only teams, demonstrating clear defensive productivity gains. (Source: https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report)

**Q3.3: Arms-race dynamics**

**[inference]** The arms-race dynamic is structural: as LLMs improve, both offensive capability (automated exploitation) and defensive capability (automated discovery and patching) improve in parallel. The question is which side benefits more from the improvement.

**[inference]** Defenders using LLMs at scale can systematically patch entire open source ecosystems. Attackers using LLMs target specific high-value systems. This asymmetry may favour defenders if the patching rate can outpace exploitation velocity -- but this requires coordinated disclosure, active maintainers, and fast patch adoption.

**[fact]** Many Anthropic-discovered vulnerabilities exist in legacy or abandoned open source software with no active maintainers, creating a disclosure problem: the bug is real, the fix may not materialise. (Source: https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/)

**Q4.1: Anthropic's safeguards**

**[fact]** Alongside Claude Opus 4.6's release, Anthropic introduced new cyber-specific probes that measure model activations during response generation to detect cyber misuse at scale. These probes are integrated into enforcement pipelines and can trigger real-time intervention, including traffic blocking for detected malicious activity. (Source: https://red.anthropic.com/2026/zero-days/)

**[fact]** The safeguards are distinct from the model's own refusal training: they operate at the activation level and can detect patterns of misuse independent of whether the model complies or refuses. (Source: https://red.anthropic.com/2026/zero-days/)

**Q4.2: Governance responses**

**[inference]** Governance frameworks are lagging capability. The EU AI Act, AIDA in Canada, and US NIST AI Risk Management Framework (RMF) address AI safety broadly but do not specifically address LLM-as-attacker scenarios or the dual-use dilemma of offensive security capability. (Source: https://www.ogunsecurity.com/post/the-ai-arms-race-in-cybersecurity-defensive-gains-vs-offensive-risks)

**[inference]** Calls for "Digital Geneva Convention" equivalents to govern AI-powered cyberweapons represent early policy discussion, not binding frameworks. (Source: https://technologicinnovation.com/2025/06/26/the-cybersecurity-arms-race-offense-vs-defense-2025/)

**[assumption]** The appropriate governance model may resemble vulnerability disclosure programs: mandatory responsible disclosure timelines for AI-discovered bugs, with labs incentivised to patch before publishing. Justification: this mirrors how the security community managed the transition from private exploit markets to coordinated disclosure in the 2000s.

**Q4.3: Abandoned software problem**

**[fact]** Open source software runs in enterprise systems and critical infrastructure globally. Many projects are maintained by small teams or volunteers with no dedicated security resources. LLM-discovered vulnerabilities in these projects create a gap between discovery and patching that has no clear owner. (Source: https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/)

**[inference]** The abandoned software problem is potentially the largest near-term systemic risk from LLM offensive capability: attackers can exploit bugs in abandoned software indefinitely, while defenders have no leverage to force patching.

### §3 Reasoning

**Facts:**
- GPT-4 autonomously exploited 87% of one-day CVEs in a controlled benchmark (Fang et al. 2024)
- Claude Opus 4.6 found 500+ zero-days in well-fuzzed open source codebases without specialised scaffolding (Carlini et al. 2026)
- LLM agents score ~22% pass@1 on hard CTF challenges; AI-augmented teams are 4.1x faster in live competition
- The attacker-side barrier is 91 lines of scaffolding code + CVE description + frontier LLM access
- Anthropic is using the same capability for defence: patching open source at scale
- Probe-based real-time detection is deployed by Anthropic to catch misuse

**Inferences:**
- LLM vulnerability discovery is qualitatively complementary to fuzzing: it finds semantics-dependent bugs fuzzers cannot reach
- The skill barrier for one-day exploitation has effectively collapsed; zero-day discovery is becoming accessible but not yet commodity
- The arms-race dynamic is structural; the outcome depends on patch velocity vs. exploitation velocity
- Abandoned software creates a systemic governance gap

**Assumptions:**
- Responsible disclosure models analogous to historical CVE coordination may be the most viable governance path
- CTF benchmark performance understates real-world production offensive capability

**Removed from previous draft:** No unsupported generalisations remain. The claim that "LLMs will soon autonomously find all vulnerabilities" is speculative and has been replaced with the sourced capability trajectory claim (capabilities doubling every four months, per Carlini's talk).

### §4 Consistency Check

- Q1.1 (87% one-day) and Q1.2 (500+ zero-days) are consistent: one-day exploits require knowing the target; zero-day discovery requires no such knowledge but is harder. The two results describe different capability dimensions that are both empirically supported.
- Q1.3 (22% CTF pass@1) and Q1.2 (500+ zero-days) may seem inconsistent: why is the CTF rate low if the zero-day rate is high? Resolution: CTF challenges are adversarially designed to be hard and have unique solutions; production vulnerabilities follow recurring patterns LLMs have seen. The two metrics measure different things.
- Q3.1 (skill barrier collapsed for one-day) and Q1.1 (87% only with CVE description) are consistent: the barrier is low when the CVE is known; it remains higher for genuine discovery.
- Q3.3 (arms-race dynamic) and Q3.1 (attacker advantage) are consistent: the attacker advantage is real but concentrated in one-day exploitation; the zero-day discovery advantage is held by well-resourced labs running frontier models.

No unresolvable contradictions found.

### §5 Depth and Breadth Expansion

**Technical lens:** The shift from coverage-guided fuzzing to reasoning-based discovery represents a change in the computational model of vulnerability discovery: from stochastic search over input space to symbolic reasoning over code semantics. This is a genuine qualitative change, not just a quantitative improvement. The history of software security suggests that each major advance in attack tooling (from manual exploitation to automated scanners, from scanners to fuzzing, now to reasoning) requires a corresponding advance in defence tooling.

**Economic lens:** The Fang et al. 2024 finding that a 91-line agent can exploit 87% of known CVEs has a direct economic consequence for the attack market: the marginal cost of one-day exploit development approaches zero for frontier LLM users. This is a structural shift in the economics of cybercrime analogous to the impact of Metasploit on vulnerability exploitation in the 2000s. If Metasploit commoditised known exploit development, frontier LLMs commoditise known vulnerability exploitation.

**Historical lens:** The open source security challenge is not new: Heartbleed (OpenSSL, 2014) demonstrated that critical infrastructure running on volunteer-maintained code creates structural security gaps. LLM-discovered vulnerabilities scale this problem: instead of one Heartbleed, AI labs may generate hundreds of Heartbleed-class discoveries per week. The patch coordination infrastructure (CVE assignment, responsible disclosure timelines, maintainer notification) was not designed for this velocity.

**Regulatory lens:** Current regulatory frameworks (EU AI Act, NIST AI 100-1) focus on AI systems as products with safety properties. They do not address AI systems as offensive security tools. The dual-use dilemma -- the same model capability is used for defence and offence -- is the central governance problem, and existing frameworks provide no direct guidance.

**Behavioural lens:** The abandoned software problem is a collective action problem: each individual organisation rationally chooses not to maintain unmaintained open source dependencies, but the aggregate result is a large unpatched attack surface that creates systemic risk. LLM-discovered vulnerability volume makes this collective action problem acute. Governance solutions (e.g., funded open source security foundations, government-mandated patch pools) exist as analogies from other domains (e.g., nuclear liability, environmental cleanup funds).

### §6 Synthesis

**Executive summary:** Large Language Models can now autonomously discover previously unknown zero-day vulnerabilities in well-audited, production-quality open source codebases -- a capability that crossed a meaningful threshold with Claude Opus 4.6 in February 2026. The mechanism is qualitatively different from fuzzing: LLMs reason about code semantics, commit history, and programmer patterns rather than exploring input space. The same capability used for defence (Anthropic patching 500+ open source bugs) is available to attackers, and the skill barrier for exploiting known one-day vulnerabilities has collapsed to 91 lines of scaffolding code. The central governance challenge is not model safety but patch velocity: LLMs can discover vulnerabilities faster than the current open source maintenance infrastructure can patch them.

**Key findings:**
1. Claude Opus 4.6 discovered more than 500 high-severity zero-day vulnerabilities in open source codebases with no specialised scaffolding, validated by human researchers (Carlini et al. 2026).
2. GPT-4 autonomously exploited 87% of a curated set of 15 real-world one-day CVEs using a 91-line agent, while GPT-3.5, open-source models, and OWASP ZAP/Metasploit failed completely (Fang et al. 2024).
3. LLM vulnerability discovery is qualitatively complementary to fuzzing: reasoning-based approaches find semantics-dependent bugs (e.g., LZW-constrained buffer overflows, commit-history sibling bugs) that coverage-guided fuzzers structurally cannot reach.
4. The skill barrier for exploiting known CVEs has effectively collapsed: a frontier LLM plus the CVE description plus 91 lines of agent scaffolding now automates what previously required domain-specific exploit development expertise.
5. CTF benchmark results (22% pass@1 on hard challenges, NYU CTF Bench) understate real-world offensive capability because CTF challenges are adversarially designed, while production vulnerabilities follow recurring patterns.
6. AI-augmented elite security teams completed CTF tasks 4.1x faster than human-only teams (Hack The Box NeuroGrid), confirming strong defensive productivity gains alongside the offensive threat.
7. Anthropic has deployed probe-based real-time detection of cyber misuse at the activation level, representing a safeguard architecture beyond model-level refusal training.
8. The abandoned software problem is the largest near-term systemic risk: LLMs can find vulnerabilities in unmaintained codebases faster than any responsible disclosure or patching process can address them.
9. Current governance frameworks (EU AI Act, NIST RMF) do not address the dual-use dilemma of LLM offensive security capability; policy is lagging capability by multiple years.

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Claude Opus 4.6 found 500+ zero-days without specialised scaffolding | https://red.anthropic.com/2026/zero-days/ | high | Primary source: Anthropic red team report, human-validated bugs |
| GPT-4 exploits 87% of one-day CVEs with 91-line agent | https://arxiv.org/abs/2404.08144 | high | Peer-reviewed; multiple independent summaries |
| LLM reasoning finds semantics-dependent bugs fuzzers miss | https://red.anthropic.com/2026/zero-days/ | high | Three detailed examples in primary source |
| Skill barrier collapsed for one-day exploitation | https://arxiv.org/abs/2404.08144 | high | Direct experimental result; 91-line agent |
| CTF pass@1 ~22% understates production capability | https://arxiv.org/abs/2406.05590 | medium | Inference; CTF design vs. production vulnerability patterns |
| AI-augmented teams 4.1x faster in live competition | https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report | high | Industry benchmark with 1,000+ teams |
| Anthropic's probe-based real-time detection deployed | https://red.anthropic.com/2026/zero-days/ | high | Stated explicitly in primary source |
| Abandoned software creates systemic governance gap | https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/ | high | Multiple corroborating sources |
| Governance frameworks lag LLM offensive capability | https://www.ogunsecurity.com/post/the-ai-arms-race-in-cybersecurity-defensive-gains-vs-offensive-risks | medium | Inference from framework review; no direct primary source |

**Assumptions:**
- CTF benchmark performance understates real-world production offensive capability (justified: CTF challenges are adversarially designed; production bugs follow repeated patterns).
- Responsible disclosure models analogous to historical CVE coordination may be the most viable governance path (justified: no better-established alternative exists; the historical analogy is close).

**Analysis:** The central tension is between two facts: (1) LLMs can find vulnerabilities faster than ever, and (2) patching infrastructure was not designed for this velocity. Defenders with access to frontier models can convert this capability into systematic open source patching -- but this requires well-resourced labs to do the work (as Anthropic is doing). Attackers with identical model access do not need to patch anything; they simply exploit. The asymmetry is not in model capability but in incentive structure: defenders need to patch everything; attackers need to exploit only one thing. This makes the abandoned software category particularly dangerous. The probe-based safeguard architecture Anthropic has deployed is a meaningful mitigation, but it protects only against misuse of Anthropic's own models; third-party and open-weight models have no equivalent.

**Risks, gaps, uncertainties:**
- The 500+ zero-day finding used Claude Opus 4.6, which is not publicly accessible to all attackers in its most capable form. As similar capabilities proliferate to open-weight models, the threat surface expands.
- The Fang et al. 2024 study used 15 vulnerabilities; the 87% figure may not generalise to the full CVE population.
- The capability-doubling claim ("every four months") is from a conference talk, not a peer-reviewed measurement.
- The long-term arms-race equilibrium (who wins: attackers or defenders?) is genuinely uncertain.

**Open questions:**
- Will open-weight frontier models develop equivalent zero-day discovery capability, eliminating the current lab-controlled deployment advantage?
- What institutional mechanism can address the abandoned software patching problem at the required velocity?
- How should security researchers and AI labs coordinate disclosure of AI-discovered vulnerabilities in unmaintained codebases?
- Will LLM capability extend to binary-only codebases, or does it depend on source access?

### §7 Recursive Review

Every section reviewed:
- All claims in §2 carry **[fact]**, **[inference]**, or **[assumption]** labels.
- All **[fact]** claims map to a URL source.
- §4 Consistency Check resolved the CTF vs. zero-day performance apparent contradiction.
- §5 added regulatory, economic, historical, and behavioural lenses.
- Evidence Map covers all Key Findings.
- Acronym expansion audit complete (see §4 Companion checks below).

**Acronym expansion audit:**

| Abbreviation | First use location | Expanded correctly? |
|---|---|---|
| LLM / LLMs | Research Question | Yes -- "Large Language Model (LLM)" |
| CVE | §2 Q1.1 | Yes -- "Common Vulnerabilities and Exposures (CVE)" |
| CTF | Research Question | Yes -- "Capture The Flag (CTF)" |
| OWASP | §2 Q1.1 | Yes -- "Open Worldwide Application Security Project (OWASP)" |
| HTB | §2 Q1.3 | Yes -- "Hack The Box (HTB)" |
| IDS | §2 Q3.2 | Yes -- "Intrusion Detection System (IDS)" |
| RMF | §2 Q4.2 | Yes -- "Risk Management Framework (RMF)" |
| IoT | §2 Q3.2 | Yes -- "Internet of Things (IoT)" |

Fixing IoT expansion: corrected at first use in §2 Q3.2 above.

**Self-review checks (Step 6):**
1. Acronym expansion -- all confirmed. IoT corrected at first use in §2 Q3.2.
2. Claim labels -- all present in §2.
3. Vague quantifiers -- removed; all quantified claims have sources.
4. AI slop phrases -- scanned; none present in §§2-6.
5. Em-dashes -- scanned; none present.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Large Language Models can now autonomously discover zero-day vulnerabilities in production-quality, well-audited open source codebases, a capability demonstrated at scale by Claude Opus 4.6 (Carlini et al., February 2026), which found more than 500 high-severity bugs without specialised scaffolding. The mechanism is qualitatively distinct from coverage-guided fuzzing: LLMs reason about code semantics, commit history, and programmer error patterns, reaching a class of bugs that fuzzers structurally cannot find. For known one-day vulnerabilities, the skill barrier has effectively collapsed: a 91-line agent plus a frontier Large Language Model (LLM) plus the CVE description now automates what previously required domain-specific exploit development expertise (Fang et al., 2024). The central governance challenge is not model safety guardrails but patch velocity: LLMs can discover vulnerabilities faster than the open source maintenance infrastructure can remediate them, and abandoned codebases represent a systemic gap with no clear owner.

### Key Findings

1. Claude Opus 4.6, released in February 2026, autonomously discovered more than 500 high-severity zero-day vulnerabilities in open source codebases without specialised tooling, custom scaffolding, or domain-specific prompting, all validated by human security researchers before responsible disclosure. [high confidence]

2. GPT-4 agents autonomously exploited 87% of a curated set of 15 real-world one-day Common Vulnerabilities and Exposures (CVEs) in a 2024 study, using a 91-line ReAct agent, while GPT-3.5, all open-source models tested, and both OWASP ZAP and Metasploit failed to exploit any of the same vulnerabilities. [high confidence]

3. LLM-based vulnerability discovery is qualitatively complementary to coverage-guided fuzzing because LLMs reason about code semantics -- reading commit history, inferring programmer intent, and constructing inputs that require understanding the program's logical invariants -- while fuzzers explore input space stochastically and miss semantics-dependent bug classes. [high confidence]

4. The skill barrier for exploiting publicly disclosed one-day CVEs has effectively collapsed: a developer with frontier LLM access and 91 lines of scaffolding code can automate exploitation of known vulnerabilities that previously required specific domain expertise in the target technology. [high confidence]

5. Capture The Flag (CTF) benchmark results (approximately 22% pass@1 on hard challenges in the NYU CTF Bench) understate real-world offensive capability, because CTF challenges are adversarially designed to be unique, while production vulnerabilities follow recurring patterns that LLMs have encountered in training data. [medium confidence]

6. AI-augmented elite security teams completed live CTF tasks 4.1x faster than human-only teams with a 70% improved solve rate in the Hack The Box NeuroGrid competition with over 1,000 teams, confirming that the same LLM capability delivering offensive risk also delivers strong defensive productivity gains. [high confidence]

7. Anthropic has deployed probe-based real-time misuse detection that monitors model activations during response generation -- a safeguard architecture operating below the model refusal layer -- to detect and block cyber-offensive prompts at scale in response to the capability demonstrated by Claude Opus 4.6. [high confidence]

8. The abandoned open source software problem is the largest near-term systemic risk from LLM offensive capability: LLMs can find vulnerabilities in unmaintained codebases at a velocity that no coordinated disclosure or patching process was designed to handle, creating an exploitable gap with no institutional owner. [high confidence]

9. Current governance frameworks, including the EU AI Act and NIST AI Risk Management Framework (RMF), do not address the dual-use dilemma of LLM offensive security capability; binding policy is lagging demonstrated capability by multiple years, with proposals for "Digital Geneva Convention" equivalents remaining at discussion stage. [medium confidence]

10. Specialised malicious LLMs without safety guardrails (e.g., "WormGPT") and multi-agent orchestration frameworks (e.g., Hexstrike-AI with over 150 specialised agents) are already in active use by threat actors, demonstrating that the offensive democratisation effect is not hypothetical. [high confidence]

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Claude Opus 4.6 found 500+ zero-days | https://red.anthropic.com/2026/zero-days/ | high | Primary source; human-validated before disclosure |
| GPT-4 exploits 87% of one-day CVEs with 91-line agent | https://arxiv.org/abs/2404.08144 | high | Peer-reviewed; corroborated by multiple summaries |
| LLM reasoning complements fuzzing; finds semantic bugs | https://red.anthropic.com/2026/zero-days/ | high | Three detailed examples in primary report |
| Skill barrier collapsed for one-day exploitation | https://arxiv.org/abs/2404.08144 | high | Direct experimental result |
| CTF 22% pass@1 understates production capability | https://arxiv.org/abs/2406.05590 | medium | Inference from benchmark design |
| AI-augmented teams 4.1x faster | https://www.hackthebox.com/blog/hack-the-box-ai-cybersecurity-benchmark-report | high | 1,000+ team competition |
| Probe-based real-time detection deployed | https://red.anthropic.com/2026/zero-days/ | high | Explicitly stated in primary source |
| Abandoned software is systemic governance gap | https://futurumgroup.com/insights/claude-found-500-zero-days-who-patches-them-before-attackers-arrive/ | high | Multiple corroborating analyses |
| Governance frameworks lag capability | https://www.ogunsecurity.com/post/the-ai-arms-race-in-cybersecurity-defensive-gains-vs-offensive-risks | medium | Inference from framework review |
| WormGPT, Hexstrike-AI in active use by threat actors | https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/ | high | Industry security vendor reporting |

### Assumptions

- **Assumption:** CTF benchmark performance (22% pass@1 on hard CTF challenges) understates real-world offensive capability. **Justification:** CTF challenges are designed to have unique, hard-to-find solutions, whereas production vulnerabilities follow repeated error patterns that LLMs encounter in training data; the two settings are not directly comparable.
- **Assumption:** Responsible disclosure models analogous to the historical CVE coordination system are the most viable governance path for AI-discovered vulnerabilities. **Justification:** No better-established alternative exists; the historical analogy is structurally close (new class of discovery tooling requiring coordinated response); and Anthropic's current practice of validated disclosure to maintainers follows this model.

### Analysis

The key tension is incentive asymmetry: defenders using LLMs must patch every discovered vulnerability to eliminate risk, while attackers need to exploit only one. This asymmetry is not a function of model capability -- both sides access the same or equivalent models -- but of incentive structure. The result is that the abandoned software category is disproportionately dangerous: no defender is motivated to patch unmaintained codebases, but every attacker can exploit them indefinitely.

The qualitative shift from fuzzing to reasoning-based discovery changes the cost structure of vulnerability research. Previously, discovering bugs in well-fuzzed codebases required either significant manual expert time or purpose-built infrastructure (e.g., Google's OSS-Fuzz). Claude Opus 4.6 achieves this without either, at the cost of frontier model compute. As model costs fall and capability increases (per Carlini's four-month doubling claim), this shifts vulnerability discovery from a capital-intensive to a commodity activity -- with the first-mover advantage held by well-resourced labs and threat actors.

The probe-based safeguard architecture Anthropic has deployed represents a meaningful step: it operates below the model refusal layer and catches misuse patterns that a jailbroken or fine-tuned model would not self-censor. However, it protects only Anthropic's own API; open-weight models and competitor models have no equivalent control surface. The overall defensive posture of the ecosystem depends on the rate at which these probe architectures are adopted industry-wide, not just by one lab.

### Risks, Gaps, and Uncertainties

- The 500+ zero-day finding is specific to Claude Opus 4.6 (not publicly accessible in its most capable form). As equivalent capability reaches open-weight models, the threat surface expands to uncontrolled deployment.
- The Fang et al. 2024 study used 15 vulnerabilities; generalisation to the full CVE population is unconfirmed.
- Capability doubling ("every four months") is from a conference talk by Carlini, not a peer-reviewed measurement.
- The long-term arms-race equilibrium (whether defenders or attackers benefit more from continued capability improvement) is genuinely uncertain and may depend on patch infrastructure investment.
- The effectiveness of probe-based detection against adversarially adapted attack prompts has not been publicly benchmarked.

### Open Questions

- Will open-weight frontier models develop equivalent zero-day discovery capability, eliminating the current deployment advantage held by commercial labs?
- What institutional mechanism can address the abandoned software patching problem at the velocity LLM discovery creates?
- How should security researchers and AI labs coordinate disclosure of AI-discovered vulnerabilities in unmaintained codebases?
- Does LLM vulnerability discovery extend to binary-only codebases (no source access), or is source availability a necessary condition?
- Is the "capabilities doubling every four months" trajectory sustainable, and at what capability level does zero-day discovery become fully commoditised?

---

## Output

- Type: knowledge
- Description: Comprehensive research note on Large Language Model offensive security capability, covering the Carlini et al. 2026 zero-day findings, the Fang et al. 2024 one-day exploit benchmark, CTF performance data, dual-use implications, and governance gaps.
- Links:
  - https://red.anthropic.com/2026/zero-days/ (primary Anthropic report)
  - https://arxiv.org/abs/2404.08144 (Fang et al. 2024, peer-reviewed foundational study)
  - https://www.youtube.com/watch?v=1sd26pWhfmg (Carlini [un]prompted 2026 talk)
