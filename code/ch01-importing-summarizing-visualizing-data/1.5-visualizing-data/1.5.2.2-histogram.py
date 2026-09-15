"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.2.2 - Histogram (under 1.5.2 Plotting Quantitative Variables)

Source: data-science-and-machine-learning.pdf (book pp. 10-11)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

weights = np.ones_like(nutri.age) / nutri.age.count()
plt.hist(nutri.age, bins=9, weights=weights, facecolor='cyan',
         edgecolor='black', linewidth=1)
plt.xlabel('age')
plt.ylabel('Proportion of Total')
plt.show()
