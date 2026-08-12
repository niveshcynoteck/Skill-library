# Why TDD Matters More, Not Less

The central argument made by practitioners in 2026 is not nostalgic — it is mechanical. When an AI agent writes both the implementation *and* its own tests after the fact, the two are produced by the same reasoning process and can share the same blind spots. An agent can (and, by several accounts, sometimes does) write a test that simply confirms whatever it happened to build, rather than a test that checks the behavior actually intended.

> "Give Claude a way to verify its work... it will 2–3x the quality of the final result."
>
> — Boris Cherny, creator of Claude Code, quoted in Forbes Technology Council (2026)

Writing the test *before* the implementation exists closes that loophole. DevAssure's analysis of the trend describes this as giving the agent "an objective definition of 'done' that the agent cannot quietly redefine to match whatever it happened to build." Because the red phase requires confirming the test fails first, an agent cannot mistake an already-passing (and possibly vacuous) test for success — a documented failure mode Kent Beck has observed directly in his own use of coding agents (see [06 — What Practitioners and Researchers Say](./06-what-practitioners-and-researchers-say.md)).

## Why this is an economic argument, not just a quality one

Forbes Technology Council frames the case in cost terms: debugging AI-generated code in production costs an order of magnitude more than catching the same issue before deployment. Teams report spending roughly a quarter of their work week checking, fixing, and validating AI output (Sonar, 2026) — verification debt that a test-first workflow is designed to pay down earlier and more cheaply.
