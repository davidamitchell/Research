# 2026-03-15 — Research Loop (chatgpt-actions-memory-integration)

**Completed:**

Research item:
- `Research/completed/2026-03-08-chatgpt-actions-memory-integration.md` — completed; ChatGPT custom GPT Actions can call a self-hosted HTTPS endpoint to write and retrieve memories using static API key auth (custom header), which works reliably on iOS unlike OAuth. OpenAI's native memory system has no programmatic API, making an external shared store the only path to cross-tool portability. The Cloudflare Workers + Fly.io backend from prior research applies without modification.

Sources consulted:
- https://platform.openai.com/docs/actions/introduction (OpenAI GPT Actions official documentation)
- https://platform.openai.com/docs/actions/authentication (GPT Actions authentication options)
- https://help.openai.com/en/articles/8590148-memory-faq (OpenAI Memory FAQ)
- https://community.openai.com/t/custom-gpt-oauth-issue-in-mobile-app/1114136 (OAuth failure on iOS/Android)
- https://community.openai.com/t/how-do-i-enable-or-disable-memory-in-api/703964 (No Memory API in OpenAI API)
- https://help.openai.com/en/articles/8554397-creating-a-gpt (Creating GPTs requires Plus plan)

## Mini-Retro

1. **Did the process work?** Yes — the research skill ran fully, all seven §§0–7 completed, review passed first attempt with no open issue.
2. **What slowed down or went wrong?** Nothing significant. The iOS availability history for custom GPT Actions with Actions had mixed signals (early 2024 "not available" reports vs later resolution), requiring extra source triangulation to confirm the current state.
3. **What single change would prevent this next time?** Nothing to prevent — the process ran cleanly.
4. **Is this a pattern?** The iOS OAuth reliability gap on ChatGPT Actions matches the theme from Claude iOS MCP research (OAuth is consistently the fragile auth path on mobile; static tokens/API keys are more reliable). This is a confirmed cross-item pattern now documented in Thread 5 of learnings.md.
