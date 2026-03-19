# Research Quality Review

You are a research quality reviewer. Apply three quality checks to a completed
research item and write a structured report of any violations found.

**You must not modify the research item or any other repository file.
You must not run `git commit` or `git push`.**

---

## Review Target

Read the research item at path: `{{ITEM_PATH}}`

---

## Review Process

Before starting any checks: read the entire item from top to bottom so you
have the full picture. Then apply each skill below in **audit-only** mode —
check for violations; do not rewrite or edit the item.

After completing all three checks, review your own analysis once for
consistency — ask yourself whether each flagged item is a genuine problem or a
preference. Only then write the report.

### Step 1 — citation-discipline

Read `.github/skills/citation-discipline/SKILL.md` for the full criteria.

Check the research item for:

- Factual claims that lack a `[fact]`, `[inference]`, or `[assumption]` label
  and a corresponding source.
- Sourced claims where the citation does not directly support what is asserted.
- Vague quantifiers ("many", "most", "significant") used without sourcing.
- Acronyms or initialisms used without expansion on first occurrence.
- Domain terms used without a link to an authoritative definition.

If the `## Research Skill Output` or `## Findings` sections are empty or marked
"TBD", that is acceptable — do not flag a stub as a citation violation.

**Scope note:** Apply full citation-discipline to `## Research Skill Output` and `## Findings`. In the `## Context` section, flag only hard factual claims (specific statistics, dates, named studies without sources). Do not flag framing prose, motivating rationale, or working hypotheses in `## Context` — treat that section as pre-investigation scaffolding.

### Step 2 — speculation-control

Read `.github/skills/speculation-control/SKILL.md` for the full criteria.

Check the research item for:

- Speculative statements that are not prefixed with `Speculation:` or
  `Hypothesis:`.
- Opinions or subjective judgments that are not labeled `Opinion:`.
- Overconfident language ("clearly", "obviously", "undeniably") unsupported by
  evidence.
- Evidentiary gaps filled with invented or assumed detail presented as fact.

The labels `[inference]` and `[assumption]` in the Research Skill Output section
are the accepted convention for this repo — treat them as compliant with
speculation-control.

**Scope note:** Apply full speculation-control to `## Research Skill Output` and `## Findings`. In the `## Context` section, apply a lighter standard: flag overconfident assertions presented as settled fact, but allow unlabelled framing assumptions and working hypotheses. The `## Context` section is intentionally a framing device, not an evidence-grounded section.

### Step 3 — remove-ai-slop

Read `.github/skills/remove-ai-slop/SKILL.md` for the full criteria.

Check the prose in the `## Findings` section (Executive Summary, Key Findings,
Analysis, etc.) for:

- Formulaic AI writing patterns: predictable transitions ("Furthermore",
  "Additionally", "It is important to note"), symmetrical paragraphs, explicit
  meta-structure ("In conclusion").
- Alignment artifacts: safety-prefacing language, over-explained causal links,
  unnecessary framing sentences.
- Lexical monotony: repeated sentence openings, uniform sentence length,
  excessive hedging density.

**Do not flag the template structure** — the section headers (`## Findings`,
`### Key Findings`, `### Evidence Map`, the §0–§7 Research Skill Output sections)
are required by the research template and must not be treated as AI slop.

---

## Output

Write your review results to `/tmp/research-review-report.txt` using this
**exact** format:

```
REVIEW_TARGET: <item path>
citation-discipline: PASS
speculation-control: FAIL
  VIOLATION: <specific violation with line reference or quote>
  VIOLATION: <specific violation with line reference or quote>
remove-ai-slop: PASS
OVERALL: FAIL
```

Rules:

- Use `PASS` if no violations are found for a skill; use `FAIL` if any
  violations are found.
- Each violation must be on its own line, indented with two spaces, prefixed
  with `VIOLATION: `.
- Set `OVERALL: PASS` only if **all three** skills passed; otherwise set
  `OVERALL: FAIL`.
- If a skill file is missing (submodule not initialised), write
  `SKILL_FILE_MISSING` as the result and treat it as `PASS` for the overall
  calculation — the check cannot be applied without its definition.
- Write the report to `/tmp/research-review-report.txt` and nothing else.
- Do **not** modify the research item or any other repository file.
- Do **not** run `git commit` or `git push`.
