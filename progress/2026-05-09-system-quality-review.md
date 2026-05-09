# 2026-05-09 — System Quality Review

## Session objective

Review the current state of the research system. Identify and record what is not working,
what is low quality, and what system-level changes are needed to reach academic-review standard.

## Problems identified

### Workflows

**tag-review.yml** (W-0053 deliverable)
- Last run (2026-05-01) failed at commit step with a push rejection (no git pull before commit).
- The workflow's stated purpose — feeding W-0043 canonical vocabulary work — is moot: W-0043 is done.
- It opens a new GitHub issue every month with no review mechanism and no owner.
- The cluster co-occurrence data it produces is not used by anything.
- Decision: repurpose toward knowledge mining. Fix push bug. Replace issue creation with a
  site page showing synthesis candidates. Feed the synthesis loop. (W-0060, W-0061)

**synthesis-loop.yml** (W-0051 deliverable)
- Requires manual input of comma-separated item slugs and a synthesis question.
- Identifying which items to synthesise and what question to ask is the hard part — the tool does none of it.
- Result: barely used in practice.
- Decision: make cluster detection the primary input; slugs should come from tag co-occurrence
  clusters, not manual entry. (W-0061)

### Research output quality

- Output contains structural repetition: §6 Synthesis is copied into Findings verbatim,
  creating two near-identical sections in the same file.
- Executive Summaries frequently restate the question rather than answering it.
- Findings sections carry boilerplate sentences that add no information.
- The 2-pass auto-pass cap on the reviewer means items can pass regardless of quality.
- No de-duplication pass exists between §6 Synthesis and Findings.
- (W-0064, W-0066)

### Citation quality

- The inline-citation SKILL.md specifies HTML `<a>` tags but research items use Markdown format.
  This is a format mismatch that makes the skill guidance inconsistent with actual practice.
- Citations from external sources do not consistently include author, year, and direct URL
  together at the point of claim.
- The inline-citation skill is referenced in research-prompt.md but as a "verify" step —
  not as a writing discipline integrated into the drafting process.
- All claims sourced from other works require proper attribution. This is non-negotiable for
  academic-quality output.
- (W-0063)

### Tag quality

- Even after W-0043 canonicalisation, tags describe broad domain areas rather than intellectual
  content. A tag of `agentic-ai` on 40 items provides no discriminating signal.
- Tags are assigned at synthesis time by the agent with minimal guidance on granularity or
  specificity.
- No tag hierarchy exists. Tags cannot be used to build meaningful clusters.
- (W-0062)

### Skills

**research-question/SKILL.md**
- The skill exists but is not invoked before investigation starts in the research loop.
- Questions in the backlog may not have passed the 5-test quality gate (specific, answerable,
  scoped, motivated, decomposable).
- A bad question produces a bad item regardless of how well the investigation is executed.
- (W-0065)

**research-reviewer/SKILL.md**
- The 2-pass auto-pass cap (research-review.yml) was added to stop runaway review loops,
  but it turns the reviewer into a formality rather than a gate.
- The reviewer checks citation-discipline, speculation-control, remove-ai-slop, and peer-review.
  But it cannot block completion: after 2 passes the item auto-passes regardless of result.
- Academic peer review does not auto-pass. Quality is the gate.
- (W-0066)

## Work recorded

New backlog items added: W-0060 through W-0067. See BACKLOG.md.

## System-level insight

The research system has accumulated prompt complexity (research-prompt.md is now ~700 lines)
but quality problems persist because the gate is weak. More prompt rules do not substitute for
a real quality gate. The reviewer must be able to block completion.

The knowledge mining goal (W-0034) has a clear path: tag clusters → synthesis candidates →
synthesis loop → Knowledge/ items. The pieces exist but are not connected. W-0060 and W-0061
connect them.

## Mini-Retro

1. **Did the process work?** Yes — systematic review of each component exposed specific,
   fixable problems rather than vague quality concerns.
2. **What slowed down?** Reading large files (research-prompt.md, BACKLOG.md) to understand
   current state before diagnosing problems.
3. **What single change would prevent this next time?** Keep a running `system-health.md`
   that tracks known quality debts so they do not require rediscovery each session.
4. **Is this a pattern?** Yes — quality debt accumulates silently when the review gate is weak.
   Root cause: auto-pass cap. Fix: W-0066.
