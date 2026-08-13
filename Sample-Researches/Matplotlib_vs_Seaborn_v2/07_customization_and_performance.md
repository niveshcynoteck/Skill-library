# Customization Ceiling & Performance

Manual mode still wins on raw control. Every tick mark, every spine, every artist on a matplotlib chart is something you can reach in and adjust — there's no ceiling. Seaborn's high-level functions cover the vast majority of everyday charts, but for a truly bespoke figure, you'll eventually drop down to the matplotlib `Axes` object that seaborn hands back to you, and finish the job there.

Speed tells a similar story. Matplotlib is generally faster and lighter on memory, especially for simple charts or very large datasets, because it isn't doing any statistical work behind the scenes. Seaborn's automatic regressions, density estimates, and styling add a small amount of overhead. For the data sizes most people work with day to day, that difference is small enough to ignore — it only starts to matter at real scale.
