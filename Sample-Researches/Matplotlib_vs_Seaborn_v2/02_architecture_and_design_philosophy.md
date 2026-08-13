# Architecture & Design Philosophy

Popping open the back of the camera shows how it actually works. Matplotlib builds every chart from three layers stacked on top of each other: a **Figure** (the whole canvas), one or more **Axes** (an individual plot area inside that canvas), and the **Artists** (every line, dot, label, and tick mark drawn onto an Axes) [(AOSA: matplotlib architecture)](https://aosabook.org/en/v2/matplotlib.html). A separate **backend** decides where the finished picture actually goes — your screen, a PNG file, a PDF — which is why the same code can show a chart on screen or save a print-ready file without any changes.

Seaborn doesn't touch any of this machinery. It just wraps around matplotlib's Figure and Axes objects and makes decisions on your behalf. Where matplotlib asks "what do you want me to draw, piece by piece?", seaborn asks "what story does your data tell?" — its own tutorial describes the goal as letting you *"focus on what the different elements of your plots mean, rather than on the details of how to draw them"* [(Seaborn Introduction)](https://seaborn.pydata.org/tutorial/introduction.html).

| | Matplotlib | Seaborn |
|---|---|---|
| Philosophy | Low-level, imperative — you build the plot piece by piece | High-level, declarative — you describe what you want, seaborn figures out how |
| What it's made of | Figure → Axes → Artists, rendered through a backend | The same Figure/Axes objects, wrapped in a friendlier layer |
| Who's driving | You control every dial | Seaborn picks sensible defaults; you can still take the wheel |
