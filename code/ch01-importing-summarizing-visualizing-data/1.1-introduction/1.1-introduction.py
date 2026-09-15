"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.1 - Introduction

Source: data-science-and-machine-learning.pdf, PDF pp. 19-20 (book pp. 1-2)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.1-introduction.md

TODO: transcribe the runnable code example(s) from this section here.
"""

# Requires: pandas

import pandas as pd

# The book has the reader manually download abalone.data first. Here we load
# it directly from its stable UCI URL so this script is standalone.
abalone_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
abalone = pd.read_csv(abalone_url, header=None)
print(abalone.head(3))  # prints a table with numeric column headers 0-8

abalone.columns = ['Sex', 'Length', 'Diameter', 'Height',
                    'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight',
                    'Rings']
print(abalone.head(3))

urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'
dataname = 'datasets/iris.csv'
iris = pd.read_csv(urlprefix + dataname)
print(iris.head())
print(iris.columns)
# .drop(..., 1) is deprecated positional-axis syntax; use axis=1 instead.
iris = iris.drop('Unnamed: 0', axis=1)
print(iris.head())
