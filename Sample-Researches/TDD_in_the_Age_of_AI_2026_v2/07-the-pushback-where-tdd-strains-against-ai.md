## 7. The Pushback: Where TDD Strains Against AI

Not everyone agrees TDD is the answer. The honest picture:

### Arguments against

1. **Context-dependence.** Kent Beck himself described working at Facebook, where teams had **no unit tests** and TDD would have been "a waste of time." TDD fits some contexts, not all ("Is TDD Dead?" debate, Fowler).
2. **Mixed empirical record.** The meta-analysis shows little productivity benefit; some industrial experiments (e.g., the Brunel/Tosun 12-experiment family) found **no significant quality difference** between TDD and test-last approaches.
3. **AI agents skip the RED phase.** If the agent writes test + code together, you get tautological tests. TDD only works if the human genuinely writes the test first — which is discipline most teams don't sustain (~8% practice).
4. **Vibe coding is winning.** "Vibe coding" (Karpathy's term) — iterating with prompts and no tests — is popular because it feels fast. In early 2026 Karpathy himself **retired the term**, saying the industry had moved to **"agentic engineering"** with more rigor, but the "no tests, just vibe" habit persists.
5. **Productivity pressure.** Opsera 2026: AI cuts time-to-PR by up to **58%**, but AI PRs wait **4.6× longer** for review and carry **+15–18% more security vulnerabilities**. The temptation is to skip verification entirely.

### The counter-pushback

The strongest arguments *for* TDD in 2026 are defensive: the cost of unverified AI code is now visible (incidents, rework, vulnerabilities). TDD converts "I think this works" into "these tests prove it works" — and it's the only widely available practice that makes agent-generated code checkable.

---
