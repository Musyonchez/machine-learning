"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.4 - Summary Statistics

Source: data-science-and-machine-learning.pdf, PDF pp. 25-26 (book pp. 7-8)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.4-summary-statistics.md

TODO: transcribe the runnable code example(s) from this section here.
"""

# Requires: pandas
# Reading the old .xls format may require the 'xlrd' or 'openpyxl' package
# (pip install xlrd  or  pip install openpyxl).

import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)
nutri['height'] = nutri['height'].astype(float)

print(nutri['height'].mean())
print(nutri['height'].quantile(q=[0.25, 0.5, 0.75]))
print(nutri['height'].max() - nutri['height'].min())
print(round(nutri['height'].var(), 2))
print(round(nutri['height'].std(), 2))
print(nutri['height'].describe())
