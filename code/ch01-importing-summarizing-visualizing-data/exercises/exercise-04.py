"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 4

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the nutri data set fresh from its source.
nutri = pd.read_excel('http://www.biostatisticien.eu/springeR/nutrition_elderly.xls')

GENDER_DICT = {1: 'Male', 2: 'Female'}
SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}

nutri['gender'] = nutri['gender'].replace(GENDER_DICT).astype('category')
nutri['situation'] = nutri['situation'].replace(SITUATION_DICT).astype('category')

# Contingency table of situation (rows) by gender (columns).
ct = pd.crosstab(nutri['situation'], nutri['gender'])
print("Contingency table (counts):")
print(ct)

# Normalize each gender column so it sums to 1 (proportions within each gender).
ct_prop = ct.div(ct.sum(axis=0), axis=1)
print("\nContingency table (proportions within each gender):")
print(ct_prop)

# Grouped bar chart of proportions.
situations = ct_prop.index.tolist()
genders = ct_prop.columns.tolist()

x = np.arange(len(situations))
bar_width = 0.35

fig, ax = plt.subplots()
for i, gender in enumerate(genders):
    offset = (i - (len(genders) - 1) / 2) * bar_width
    ax.bar(x + offset, ct_prop[gender].values, width=bar_width, label=gender)

ax.set_xticks(x)
ax.set_xticklabels(situations)
ax.set_xlabel('Situation')
ax.set_ylabel('Proportion')
ax.set_title('Proportion of situation category, by gender')
ax.legend(title='Gender')

plt.show()
