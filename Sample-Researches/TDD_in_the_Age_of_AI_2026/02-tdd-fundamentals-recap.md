# TDD, Briefly Recapped

Test-Driven Development is a software practice built on a short, repeating cycle, popularized by Kent Beck in the early 2000s:

- **RED** — Write a test for behavior that doesn't exist yet. It fails, because the code isn't written.
- **GREEN** — Write the smallest amount of code needed to make that test pass.
- **REFACTOR** — Clean up the implementation while the passing test guarantees behavior hasn't changed.

The original justification for TDD was mostly about *design*: writing a test first forces a programmer to think about a piece of code's interface and behavior before its internals. In the AI era, a second justification has become just as important — *verification*: a failing test written before any implementation exists is a target that cannot be quietly redefined by whoever (or whatever) writes the code next.
