# Pandas Integration

If your data already lives in a Pandas DataFrame — and these days, it usually does — this is where the difference shows up most in day-to-day work.

Matplotlib doesn't know what a DataFrame is. It's happy to plot arrays or Series, but you pull the right columns out yourself first:

```python
ax.plot(df["date"], df["revenue"])
```

Seaborn was designed around DataFrames from day one. You hand it the whole table once, then just name the columns you care about:

```python
sns.lineplot(data=df, x="date", y="revenue")
```

Same result, but seaborn quietly handles the translation from column names to the arrays matplotlib actually needs underneath [(Seaborn Introduction)](https://seaborn.pydata.org/tutorial/introduction.html). It's a small syntax difference that adds up fast across a real analysis with a dozen charts.
