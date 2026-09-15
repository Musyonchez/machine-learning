"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.3 - Summary Tables

Source: data-science-and-machine-learning.pdf, PDF pp. 24-25 (book pp. 6-7)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.3-summary-tables.md

TODO: transcribe the runnable code example(s) from this section here.
"""

# Requires: pandas
# Reading the old .xls format may require the 'xlrd' or 'openpyxl' package
# (pip install xlrd  or  pip install openpyxl).

import pandas as pd

# The book loads the previously restructured and saved 'nutri.csv' (see
# section 1.2). To keep this file standalone, we instead load fresh from the
# original Excel source and recode only the columns needed below.
xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

GENDER_DICT = {1: 'Male', 2: 'Female'}
SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}
FAT_DICT = {1: 'butter', 2: 'margarine', 3: 'peanut', 4: 'sunflower',
            5: 'olive', 6: 'Isio4', 7: 'colza', 8: 'duck'}

nutri['gender'] = nutri['gender'].replace(GENDER_DICT).astype('category')
nutri['situation'] = nutri['situation'].replace(SITUATION_DICT).astype('category')
nutri['fat'] = nutri['fat'].replace(FAT_DICT).astype('category')

print(nutri['fat'].describe())
print(nutri['fat'].value_counts())
# nutri.fat is the same as nutri['fat'] (attribute-style column access).
print(pd.crosstab(nutri.gender, nutri.situation))
print(pd.crosstab(nutri.gender, nutri.situation, margins=True))
