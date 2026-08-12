## 2. TDD, Briefly Recapped

TDD is a disciplined development cycle with three phases:

> **RED** — Write a failing test that describes the desired behavior.
> **GREEN** — Write the minimum code to make the test pass.
> **REFACTOR** — Clean up the code while keeping all tests green.

Kent Beck's "Canon TDD" emphasizes the common mistakes to avoid: don't delete assertions to force a pass, don't copy computed values into your expected results, and don't mix refactoring into the GREEN phase.

### What the evidence says (pre-AI)

A meta-analysis of 27 empirical studies (Rafique & Misic, IEEE TSE) found that, in general, TDD has a **small positive effect on external quality** but **little or no effect on productivity**. Importantly:

- Effects are **larger in industrial studies** than in academic ones.
- TDD's benefit shows up more when test effort and task size are substantial.
- Critics argue the evidence is mixed and context-dependent (see section 6).

So even before AI, TDD was a "good in the right context" practice rather than a universal silver bullet. The AI era changes that calculus.

---
