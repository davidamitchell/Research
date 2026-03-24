# 2026-03-24 — Fix missing backlog directory and add .gitkeep files

**Completed:**

Infrastructure fix:
- Added `Research/backlog/.gitkeep`, `Research/in-progress/.gitkeep`, and `Research/completed/.gitkeep` to prevent Git from dropping empty directories.
- Moved `2026-03-23-software-factory.md` and `2026-03-24-public-sentiment-on-ai-in-banking-and-high-trust-institutions.md` from `Research/in-progress/` back to `Research/backlog/` with `status: backlog` and `started: ~`.
- Added two new rules to `research-prompt.md` Rules section: backlog items must go in `Research/backlog/`, and `.gitkeep` files must never be deleted.

## Mini-Retro

1. **Did the process work?** Yes — all three directories are now protected from disappearing when emptied.
2. **What slowed down or went wrong?** The loop completed the last backlog item and the agent deleted it, causing Git to drop the empty `Research/backlog/` directory. The next workflow run then failed on `find Research/backlog -name '*.md'`.
3. **What single change would prevent this next time?** The `.gitkeep` files added in this session prevent it. The new rule in `research-prompt.md` also instructs agents never to delete `.gitkeep`.
4. **Is this a pattern?** Yes — Git does not track empty directories. Any directory that can be emptied by normal workflow operations needs a `.gitkeep`.
