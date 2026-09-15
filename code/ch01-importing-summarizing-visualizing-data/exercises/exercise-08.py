"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 8

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# (a) Read the Orange data set and remove its first (unnamed) column.
orange = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/Orange.csv')
# Rdatasets currently exports the index column as 'rownames' (the book-era
# CSVs left it blank, which pandas auto-names 'Unnamed: 0') -- handle both.
index_col = 'rownames' if 'rownames' in orange.columns else 'Unnamed: 0'
orange = orange.drop(index_col, axis=1)
print("(a) orange head:")
print(orange.head())

# (b) Names of the features.
print("\n(b) Feature names:", orange.columns.tolist())

# (c) Visualize the growth curves (circumference against age) of the trees,
# using seaborn's regplot within a FacetGrid, one facet per tree.
g = sns.FacetGrid(orange, col='Tree')
g.map(sns.regplot, 'age', 'circumference')
plt.show()
