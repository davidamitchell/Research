# 2026-10-23 -- Add backlog item (state-mutation-decision-framework)

**Completed:**
- `Research/backlog/2026-10-23-state-mutation-decision-framework.md` — added a scoped literature-review question linking delivery delay, ownership cost, and change friction, with prior corpus questions and sources identified; research itself remains for the research workflow.

## Mini-Retro

1. **Did the process work?** Yes. The research-question skill and a focused corpus search helped turn three broad questions into a decomposable backlog item.
2. **What slowed down or went wrong?** The skills submodule was initially empty and had to be initialized before applying the required skill.
3. **What single change would prevent this next time?** Initialize `.github/skills/` at session setup when a task depends on one of its skills.
4. **Is this a pattern?** Skill availability can be environment-dependent; repository instructions already provide the initialization step.
5. **Does any documentation need updating?** No. This is a new research item, not a change to repository behavior or documentation.
6. **Do the default instructions need updating?** No new convention emerged; the existing research-request workflow covered this task.

---

# 2026-10-23 -- Research Loop (state-mutation-decision-framework)

**Completed:**

Research item:
- `Research/completed/2026-10-23-state-mutation-decision-framework.md` -- completed; no examined study validates CoD, FCO, or FCC as cost constructs, so the best-supported measures are proxies (elapsed-time metrics, defect-related activity, file size, change count, coupling). Evidence supports a qualitative debt feedback mechanism but no compounding rate, and architecture-style evidence mixes infrastructure cost and code-debt outcomes from different systems.

Sources consulted:
- https://arxiv.org/abs/2203.04374 (Tornhill and Borg, code quality and cycle time in 39 codebases)
- https://www.hbs.edu/ris/Publication%20Files/2016-JSS%20Technical%20Debt_d793c712-5160-4aa9-8761-781b444cc75f.pdf (MacCormack and Sturtevant, coupling and defect-related activity)
- https://www.mn.uio.no/ifi/personer/vit/dagsj/sjoberg.yamashita.anda.mockus.dyba.tse.2013.pdf (Sjøberg et al., code smells and maintenance effort)
- https://arxiv.org/abs/1902.06282 (Lenarduzzi et al., monolith to microservices debt)

## Mini-Retro

1. **Did the process work?** Yes. Review pass 1 failed on em-dashes in seed Sources text and three derived clauses under `[fact]`; pass 2 passed.
2. **What slowed down or went wrong?** Seed Sources lines contained em-dashes I did not scan for before drafting, and I put interpretive "so ..." clauses inside `[fact]` Key Findings. ACM, IEEE, Scholar, and SEI were not queried directly, so coverage is a stated gap.
3. **What single change would prevent this next time?** Run the em-dash grep over the whole file, including seed Sources, right after writing content.
4. **Is this a pattern?** Yes; both failures match known patterns (em-dashes; fact and inference clauses collapsed in Key Findings).
