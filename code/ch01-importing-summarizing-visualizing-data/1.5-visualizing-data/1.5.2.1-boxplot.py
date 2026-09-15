"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.2.1 - Boxplot (under 1.5.2 Plotting Quantitative Variables)

Source: data-science-and-machine-learning.pdf (book pp. 9-10)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

width = 0.35
plt.boxplot(nutri['age'], widths=width, vert=False)
plt.xlabel('age')
plt.show()
