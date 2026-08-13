# Matplotlib vs Seaborn — Research Report (v2)

A structured comparison of Python's two most widely used data visualization libraries, told through a simple running analogy: **Matplotlib as a manual camera, Seaborn as the auto mode built on top of it.**

This is an improved version of the original report in [`../Matplotlib_vs_Seaborn`](../Matplotlib_vs_Seaborn). The original is preserved untouched; this version:

- Rewrites every section in simpler, more conversational language, with one consistent analogy carried through from the overview to the conclusion.
- Adds small code examples (e.g. Pandas integration) so points are shown, not just stated.
- Refines the comparison graphic (cleaner typography, spacing, and color contrast) after re-checking every row against the source docs.
- Re-validates all 9 references (all still return HTTP 200 as of 2026-08-13) and fixes a CSV formatting bug in `validated_links.csv` where unquoted commas in the "Information" column were breaking column alignment.
- Removes a stray leftover character at the end of the original conclusion file.

No facts were changed — only presentation, clarity, and correctness of the supporting files.

## Contents

| File | Section |
|---|---|
| [01_overview.md](01_overview.md) | Overview & Background |
| [02_architecture_and_design_philosophy.md](02_architecture_and_design_philosophy.md) | Architecture & Design Philosophy |
| [03_syntax_and_api.md](03_syntax_and_api.md) | Syntax & API Design |
| [04_statistical_features.md](04_statistical_features.md) | Built-in Statistical Features |
| [05_aesthetics_and_themes.md](05_aesthetics_and_themes.md) | Default Aesthetics & Themes |
| [06_pandas_integration.md](06_pandas_integration.md) | Pandas Integration |
| [07_customization_and_performance.md](07_customization_and_performance.md) | Customization Ceiling & Performance |
| [08_conclusion.md](08_conclusion.md) | Comparison Summary & Conclusion |

## Assets

- `matplotlib_vs_seaborn_comparison.png` — refined side-by-side feature comparison table (8 dimensions)
- `validated_links.csv` — all 9 references used in this report, each re-validated with an HTTP 200 check

## Sources

All claims are sourced from the official Matplotlib and Seaborn documentation, the official Matplotlib blog, the Architecture of Open Source Applications book, and both projects' GitHub repositories. See `validated_links.csv` for the full reference list.
