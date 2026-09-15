"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.2.3 - Empirical Cumulative Distribution Function (under 1.5.2 Plotting Quantitative Variables)

Source: data-science-and-machine-learning.pdf (book pp. 11-12)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

x = np.sort(nutri.age)
y = np.linspace(0, 1, len(nutri.age))
plt.xlabel('age')
plt.ylabel('Fn(x)')
plt.step(x, y)
plt.xlim(x.min(), x.max())
plt.show()
