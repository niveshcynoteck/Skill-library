# Default Aesthetics & Themes

Straight out of the box, a matplotlib chart looks functional but plain — no grid, a fairly basic style, every visual choice left to you. That's deliberate: matplotlib would rather stay neutral than guess what you want. As seaborn's own docs point out, that neutrality has a cost — *"it can be hard to know what settings to tweak to achieve an attractive plot"* [(Seaborn Aesthetics)](https://seaborn.pydata.org/tutorial/aesthetics.html).

Seaborn closes that gap with five ready-made themes — **darkgrid** (the default), **whitegrid**, **dark**, **white**, and **ticks** — each suited to a different situation, from data-dense dashboards to clean presentation slides. It also separates *how a chart looks* from *how big it needs to be*: `set_style()` changes the look, while `set_context()` rescales everything for a paper, a notebook, a talk, or a poster, without you touching a single font size by hand.

| | Matplotlib | Seaborn |
|---|---|---|
| Default look | Plain, minimal grid | Polished, ready to present |
| Themes | None built in — you configure `rcParams` yourself | 5 presets: darkgrid, whitegrid, dark, white, ticks |
| Scaling for context | Manual | One line: `set_context("talk")`, `"poster"`, etc. |
