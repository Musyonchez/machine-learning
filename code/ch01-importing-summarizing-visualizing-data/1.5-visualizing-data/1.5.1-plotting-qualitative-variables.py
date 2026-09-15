"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.1 - Plotting Qualitative Variables

Source: data-science-and-machine-learning.pdf (book pp. 8-9)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd

SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)
nutri['situation'] = nutri['situation'].replace(SITUATION_DICT).astype('category')

width = 0.35  # the width of the bars
x = [0, 0.8, 1.6]  # the bar positions on x-axis
situation_counts = nutri['situation'].value_counts()
# The book's figure assumes exactly 3 situation categories (Couple/Family/Single)
# and hard-codes 3 bar positions in x. If the live data also contains the 'Other'
# category, situation_counts will have 4 entries, not matching len(x) == 3 -- this
# is a known simplification carried over from the book itself, not a bug to fix here.
plt.bar(x, situation_counts, width, edgecolor='black')
plt.xticks(x, situation_counts.index)
plt.show()
