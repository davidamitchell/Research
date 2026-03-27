# 2026-03-26 — Research Loop (against-bureaucracy)

**Completed:**

Research item:
- `Research/completed/2026-03-26-against-bureaucracy-dismantling-control-systems-to-focus-on-value-and-opportunit.md` — completed; synthesises the Anti-Bureaucracy Manifesto (PeopleKult) and Burnham's *The Managerial Revolution* (1941) to show that bureaucracy is a control-accumulation mechanism benefiting the managerial class, not merely a process inefficiency; adds Orwell's corrective, Hamel/Zanini's quantified cost ($3 trillion US annually), Laloux's Teal structural alternative, and Value Stream Mapping as the operational instrument; identifies the opportunity cost of bureaucracy (foregone exploration capacity) as a significant unquantified gap.

Sources consulted:
- https://www.peoplekult.com/post/the-anti-bureaucracy-manifesto-how-to-create-a-more-efficient-and-effective-organization (Anti-Bureaucracy Manifesto: diagnostic claims, cost data, toolkit)
- https://en.wikipedia.org/wiki/The_Managerial_Revolution (Burnham 1941 summary: managerial class thesis, separation of ownership and control)
- http://george-orwell.org/James_Burnham_and_the_Managerial_Revolution/0.html (Orwell's 1946 critique: corrective on determinism)
- https://www.garyhamel.com/blog/3-trillion (Hamel: $3 trillion US bureaucracy cost quantification)
- https://www.humanocracy.com/ (Humanocracy governance architecture)
- https://en.wikipedia.org/wiki/Reinventing_Organizations (Laloux: Teal organisations, advice process, Buurtzorg and Morning Star case studies)
- https://kaizen.com/insights/guide-vsm-lean-manufacturing/ (Kaizen: Value Stream Mapping methodology)

## Mini-Retro

1. **Did the process work?** Yes. The two primary sources (PeopleKult Manifesto and Wikipedia on Burnham) were complementary — one operational, one structural — and the additional sources (Orwell, Hamel, Laloux, VSM) filled the gaps cleanly. The synthesis was richer than either primary source alone.
2. **What slowed down or got complicated?** The heredoc approach for writing the large file stalled; switched to a Python script in `/tmp/` which worked reliably. The file also needed to be written to the in-progress location before completing via CLI.
3. **What single change would prevent this next time?** For large research items, always use a Python write script rather than heredoc. Heredoc with large content containing special characters reliably stalls.
4. **Is this a pattern?** Yes — heredoc stalling with large content has occurred before. This is a known limitation; the Python script approach is the established workaround.
