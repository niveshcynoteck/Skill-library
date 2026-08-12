# From Autocomplete to Autonomous Agents

The core shift isn't "better autocomplete" — it's a change in *who drives the loop*.

See [`visuals/agentic_coding_evolution.png`](visuals/agentic_coding_evolution.png) — a diagram mapping three eras:

1. **Autocomplete (2015–2021)** — human writes every line; AI suggests the next token or single line; accept/reject inline; no awareness of files beyond the open buffer.
2. **Copilot / Chat (2021–2024)** — human writes a prompt or selects code; AI drafts a function or chat-based diff; human reviews and accepts each change; multi-file context, but still one step at a time.
3. **Agentic Coding (2024–2026)** — human sets a goal and reviews the final result; the agent runs an autonomous loop (Plan → Implement → Test → Self-correct) unsupervised in between.

By mid-2026, most large engineering organizations were experimenting with at least one agentic workflow — IDE agents, background coding agents, or PR-review agents. A newer pattern is **multi-agent teams**, where a task is split across specialized agents (Planner → Architect → Implementer → Tester → Reviewer) mirroring a real engineering team, which improves reliability on complex tasks.

Source: [Sourcegraph — Agentic Coding in 2026](https://sourcegraph.com/blog/agentic-coding)

## The New Core Skill: Context Engineering, Not Prompt Engineering

Agents don't fail because they can't reason — they fail because the wrong information is in their context window at the wrong time. For example, a `grep` across a million-line monorepo can return 4,000 irrelevant hits that burn the agent's attention before it reaches the real cause.

**Context engineering** — deliberately curating instructions, retrieved documents, memory, and available tools — has become important enough that "Context Engineer" is now an actual job title at companies like Adobe, Stripe, and Cognizant (which announced plans to deploy ~1,000 of them).

The four pillars of context engineering, per Sourcegraph:
1. **Instructions / system prompt** — behavioral framing
2. **Retrieval** — fetching external data via vector search, structured queries, or code-aware lookups
3. **Memory** — short-term (conversation history) and long-term (persistent preferences/summaries)
4. **Tools** — function-calling capabilities; bloated tool sets waste tokens on deciding between similar options

Sources: [Sourcegraph — Context Engineering](https://sourcegraph.com/blog/context-engineering), [Martin Fowler — Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
