# Built-in Statistical Features

This is where seaborn really earns its "auto mode" reputation. Point it at your data and it will, on its own, fit regression lines, estimate probability densities (KDE), and even draw **bootstrapped confidence intervals** around an estimate — no extra statistics code required. It also ships with ready-made ways to plot distributions (histograms, KDEs, ECDFs) and categorical data at several levels of detail [(Seaborn Introduction)](https://seaborn.pydata.org/tutorial/introduction.html).

Matplotlib has no opinion here at all — it has no statistics layer. If you want a regression line or a confidence interval, you calculate it yourself first, usually with NumPy or SciPy, then hand matplotlib the finished numbers to draw. That's a fair trade-off: matplotlib stays simple and predictable, while seaborn spends a little more computation time making smart assumptions for you.
