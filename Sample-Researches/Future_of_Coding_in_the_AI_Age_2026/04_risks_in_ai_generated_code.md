# The Real Risks in AI-Generated Code

This is one area with hard empirical data, not just punditry. A large-scale study analyzed **302,600 AI-authored commits across 6,299 GitHub repositories**, covering five major tools (Copilot, Claude, Cursor, Gemini, Devin).

See [`visuals/ai_code_risk_breakdown.png`](visuals/ai_code_risk_breakdown.png) — donut chart of **484,366 total issues found**: 89.3% code smells, 6.0% correctness issues, 4.7% security issues, with **22.7%** of all introduced issues still unresolved in the latest version of the repo.

## Key Findings

- AI assistants are **good at fixing style/structure issues but introduce more correctness and security issues than they resolve** — the opposite of what you'd want from a net-quality standpoint.
- **15–29%** of commits from every major AI coding tool introduce at least one detectable problem (17.4% for Copilot, up to 29.1% for Gemini).
- Separately, Veracode found **40–45%** of AI-generated code contains a vulnerability mapping to the OWASP Top 10 — over **70%** for Java specifically.
- **~20%** of AI-generated code samples reference **hallucinated packages that don't exist** — attackers pre-register these names on npm/PyPI as a supply-chain attack vector ("slopsquatting").

Sources: [arXiv 2603.28592 — Debt Behind the AI Boom](https://arxiv.org/html/2603.28592v2), [Veracode — AI-Generated Code Security Risks](https://www.veracode.com/blog/ai-generated-code-security-risks/), [Cloud Security Alliance — AI-Generated CVE Surge](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/)

This is the empirical counterweight to "AI writes all our code now" — it writes a lot of code, and a meaningful fraction of it is quietly accumulating debt and risk that someone still has to catch.
