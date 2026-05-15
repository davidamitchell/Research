# Claude Code — Research Repo

All instructions for working in this repository live in
**`.github/copilot-instructions.md`** — read it at the start of every session.
It is the single source of truth for conventions, constraints, credentials,
coding standards, workflows, and the research item lifecycle.

Skills (structured prompts for common tasks such as `research`, `swe`, `tdd`,
`adr`, `code-review`, etc.) live in **`.github/skills/`**.  
If the directory is empty, initialise the submodule first:

```bash
git submodule update --init .github/skills
```

Then open the relevant `SKILL.md` (e.g. `.github/skills/tdd/SKILL.md`) and
follow its process step by step.
