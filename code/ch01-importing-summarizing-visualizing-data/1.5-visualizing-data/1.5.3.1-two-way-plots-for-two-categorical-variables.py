"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.3.1 - Two-way Plots for Two Categorical Variables (under 1.5.3 Data Visualization in a Bivariate Setting)

Source: data-science-and-machine-learning.pdf (book pp. 12-13)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

GENDER_DICT = {1: 'Male', 2: 'Female'}
SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)
nutri['gender'] = nutri['gender'].replace(GENDER_DICT).astype('category')
nutri['situation'] = nutri['situation'].replace(SITUATION_DICT).astype('category')

sns.countplot(x='situation', hue='gender', data=nutri,
    hue_order=['Male', 'Female'], palette=['SkyBlue', 'Pink'],
    saturation=1, edgecolor='black')
plt.legend(loc='upper center')
plt.xlabel('')
plt.ylabel('Counts')
plt.show()
