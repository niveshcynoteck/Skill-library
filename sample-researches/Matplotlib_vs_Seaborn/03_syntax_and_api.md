# Syntax & API Design

Matplotlib exposes **two parallel interfaces**:
- **pyplot** — a stateful, MATLAB-style interface (`plt.plot()`) that implicitly tracks the "current" figure/axes.
- **Object-oriented (OO) API** — explicit `Figure`/`Axes` objects (`fig, ax = plt.subplots()`) you call methods on directly, better for complex or multi-panel figures [(Matplotlib Blog: pyplot vs OO)](https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/).

Seaborn has its own two-tier API:
- **Axes-level functions** (e.g. `sns.scatterplot`) — plot onto a single matplotlib `Axes`, act as "drop-in replacements" for matplotlib functions, and accept an `ax=` parameter for composition.
- **Figure-level functions** (e.g. `sns.relplot`) — manage their own figure via wrapper objects like `FacetGrid`, enabling multi-plot grids and external legends, but are harder to combine with other plots [(Seaborn Function Overview)](https://seaborn.pydata.org/tutorial/function_overview.html).

## Example — a scatter plot with a regression line

```python
# Matplotlib (manual)
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.scatter(x, y)
coeffs = np.polyfit(x, y, 1)
ax.plot(x, np.polyval(coeffs, x), color="red")

# Seaborn (built-in)
import seaborn as sns
sns.regplot(x=x, y=y)
```
