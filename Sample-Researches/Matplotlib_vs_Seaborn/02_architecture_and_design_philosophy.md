# Architecture & Design Philosophy

| Aspect | Matplotlib | Seaborn |
|---|---|---|
| Philosophy | Low-level, imperative | High-level, declarative |
| Core structure | Figure → Axes → Artists (three-layer stack: scripting, artist, backend) | Wraps matplotlib's Figure/Axes internally |
| Control style | You build the plot piece by piece | You describe *what* you want; seaborn handles *how* |

Matplotlib's architecture separates the **Figure** (the drawable representation) from the **backend** (the rendering device — screen, PNG, PDF, SVG, etc.), enabling it to support many GUI toolkits and file formats through one interface [(AOSA: matplotlib architecture)](https://aosabook.org/en/v2/matplotlib.html).

Seaborn's philosophy is dataset-oriented: it lets users *"focus on what the different elements of your plots mean, rather than on the details of how to draw them"* [(Seaborn Introduction)](https://seaborn.pydata.org/tutorial/introduction.html).
