# Overview & Background

Think of two photographers sharing the same camera. One shoots entirely in manual mode — setting the aperture, shutter speed, and focus by hand for every single shot. The other leaves the camera in "auto," letting it make smart decisions instantly, while still being free to flip back to manual whenever a shot calls for it. That's roughly the relationship between **Matplotlib** and **Seaborn**.

**Matplotlib** is the manual camera. It's the original Python plotting library, capable of producing almost any static, animated, or interactive chart you can imagine [(Matplotlib Docs)](https://matplotlib.org/stable/index.html). For nearly two decades it has quietly powered most other Python plotting tools under the hood — including seaborn.

**Seaborn** is the auto mode built on top of that same camera. It doesn't replace matplotlib; it sits on top of it. The seaborn team puts it plainly: *"Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics"* [(Seaborn Docs)](https://seaborn.pydata.org/). It's maintained by Michael Waskom and a community of open-source contributors [(Seaborn GitHub)](https://github.com/mwaskom/seaborn).

**The one thing worth remembering:** this was never a rivalry. Seaborn literally cannot run without matplotlib — every seaborn chart is drawn by matplotlib behind the scenes. Comparing them isn't "which one is better," it's "which mode should I be in right now."
