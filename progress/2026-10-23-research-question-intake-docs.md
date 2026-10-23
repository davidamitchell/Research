# 2026-10-23 -- Clarify research question intake

**Completed:**
- `README.md` and `Research/README.md` — documented issue-to-Copilot intake as the primary owner path, good-question criteria and seeds, and retained direct file/CLI use as the agent/tooling path.

## Mini-Retro

1. **Did the process work?** Yes. The existing skill and workflow verified the intended quality criteria and intake handoff.
2. **What slowed down or went wrong?** The skills submodule was uninitialized, so it had to be initialized before checking the criteria.
3. **What single change would prevent this next time?** Initialize the skills submodule before consulting a skill.
4. **Is this a pattern?** An uninitialized submodule can block skill verification in a fresh checkout.
5. **Does any documentation need updating?** The main and Research READMEs now distinguish the owner issue path from direct tooling; the Copilot instructions already agree and need no change.
6. **Do the default instructions need updating?** No new repository-wide convention emerged.

## Related

- [Main README](../README.md)
- [Research README](../Research/README.md)
- [Copilot instructions](../.github/copilot-instructions.md)
- [Research loop workflow](../.github/workflows/research-loop.yml)
