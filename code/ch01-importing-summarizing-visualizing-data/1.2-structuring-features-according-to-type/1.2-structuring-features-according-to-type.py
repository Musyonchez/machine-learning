"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.2 - Structuring Features According to Type

Source: data-science-and-machine-learning.pdf, PDF pp. 21-23 (book pp. 3-5)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.2-structuring-features-according-to-type.md

TODO: transcribe the runnable code example(s) from this section here.
"""

# Requires: pandas
# Reading the old .xls format may require the 'xlrd' or 'openpyxl' package
# (pip install xlrd  or  pip install openpyxl).

import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

pd.set_option('display.max_columns', 8)
print(nutri.head(3))
print(nutri.info())

DICT = {1: 'Male', 2: 'Female'}
nutri['gender'] = nutri['gender'].replace(DICT).astype('category')

nutri['height'] = nutri['height'].astype(float)

nutri.to_csv('nutri.csv', index=False)
