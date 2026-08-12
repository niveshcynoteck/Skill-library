# The Pushback: Where TDD Strains Against AI

The renewed enthusiasm for TDD is not universal, and several credible criticisms recur across 2026 sources:

## "Test theater" from retroactive coverage

When an AI is asked to write tests for code that already exists, it tends to produce tests that simply describe current behavior — bugs included — rather than the behavior that was actually intended. This is sometimes called "retroactive coverage theater": the test suite looks comprehensive but would not catch the very defects it should exist to catch.

## Over-mocked, shallow tests

An empirical study of coding-agent output ("Are Coding Agents Generating Over-Mocked Tests?", arXiv, 2026) found that agents lean heavily on mocks — tests that are cheap to generate automatically but verify far less about real system interactions than an equivalent hand-written integration test would.

## Tautological validation

When the same model writes both the implementation and its tests, the two can share identical blind spots. A test written by the same reasoning process that wrote the bug is unlikely to catch that bug — the core failure mode that test-first ordering is specifically meant to prevent, but which resurfaces if teams skip that ordering under time pressure.

## An organizational, not technical, barrier

Multiple sources converge on the same diagnosis: the obstacle to disciplined TDD in AI-native teams isn't a capability gap in the tools — it's that TDD requires defining behavior *before* writing code, which runs against the speed-first incentives that often drive AI-tool adoption in the first place.
