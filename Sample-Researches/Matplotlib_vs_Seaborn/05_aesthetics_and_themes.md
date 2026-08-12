# Default Aesthetics & Themes

| | Matplotlib | Seaborn |
|---|---|---|
| Default look | Basic style, minimal grid | Polished, statistically-informed defaults |
| Built-in themes | None (manual `rcParams`/`style` sheets) | 5 presets: **darkgrid** (default), whitegrid, dark, white, ticks |
| Customization model | Single, broad `rcParams` system | Separated **style** (look) + **context** (scale for print/talk/poster) via `set_style()`/`set_context()` |

Seaborn's docs note that while matplotlib is highly customizable, *"it can be hard to know what settings to tweak to achieve an attractive plot"* — seaborn's theme functions solve this with sensible, pre-tuned defaults [(Seaborn Aesthetics)](https://seaborn.pydata.org/tutorial/aesthetics.html).
