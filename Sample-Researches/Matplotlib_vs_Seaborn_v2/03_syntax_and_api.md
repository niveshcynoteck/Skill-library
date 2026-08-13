# Syntax & API Design

Matplotlib actually offers two different ways to hold the "manual" controls:

- **pyplot** — the classic, MATLAB-style approach (`plt.plot()`). It quietly remembers which figure and axes you're "currently" working on, so you don't have to name them every time.
- **Object-oriented (OO) API** — you create the `Figure` and `Axes` objects yourself (`fig, ax = plt.subplots()`) and call methods on them directly. It's more explicit, and it scales much better once a chart has several panels [(Matplotlib Blog: pyplot vs OO)](https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/).

Seaborn mirrors this with its own two tiers:

- **Axes-level functions** (like `sns.scatterplot`) draw onto a single matplotlib `Axes` — you can even hand them an existing `ax=` to slot into a matplotlib figure you already built.
- **Figure-level functions** (like `sns.relplot`) manage their own figure, using helper objects like `FacetGrid` to lay out several related charts side by side. They're great for quick exploration, but harder to combine with other, non-seaborn plots [(Seaborn Function Overview)](https://seaborn.pydata.org/tutorial/function_overview.html).

The difference becomes obvious the moment you try something simple: plot two variables and draw a line showing the trend between them.

```python
# Matplotlib — you compute the trend line yourself
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.scatter(x, y)
coeffs = np.polyfit(x, y, 1)
ax.plot(x, np.polyval(coeffs, x), color="red")

# Seaborn — the trend line is built in
import seaborn as sns
sns.regplot(x=x, y=y)
```

Five lines become one. That single line is the whole seaborn pitch in miniature.
