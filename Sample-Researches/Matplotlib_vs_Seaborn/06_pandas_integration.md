# Pandas Integration

- **Matplotlib**: Accepts arrays/Series but has no native DataFrame awareness — you extract columns manually.
- **Seaborn**: Built around DataFrames from the start — you pass `data=df` plus column names as strings (`x="col1", y="col2"`), and seaborn handles the translation to matplotlib arguments [(Seaborn Introduction)](https://seaborn.pydata.org/tutorial/introduction.html).
