"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.3.3 - Plots for One Qualitative and One Quantitative Variable (under 1.5.3 Data Visualization in a Bivariate Setting)

Source: data-science-and-machine-learning.pdf (book pp. 14-15)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd

GENDER_DICT = {1: 'Male', 2: 'Female'}

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)
nutri['gender'] = nutri['gender'].replace(GENDER_DICT).astype('category')

males = nutri[nutri.gender == 'Male']
females = nutri[nutri.gender == 'Female']
plt.boxplot([males.coffee, females.coffee], notch=True, widths=(0.5, 0.5))
plt.xlabel('gender')
plt.ylabel('coffee')
plt.xticks([1, 2], ['Male', 'Female'])
plt.show()
