"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Section 1.5.3.2 - Plots for Two Quantitative Variables (under 1.5.3 Data Visualization in a Bivariate Setting)

Source: data-science-and-machine-learning.pdf (book pp. 13-14)
Notes:  notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md

TODO: transcribe the runnable code example(s) from this subsection here.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd.read_excel(xls)

plt.scatter(nutri.height, nutri.weight, s=12, marker='o')
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

# Second example: birth weight vs mother's age, colored by smoking status
urlprefix = 'https://vincentarelbundock.github.io/Rdatasets/csv/'
dataname = 'MASS/birthwt.csv'
bwt = pd.read_csv(urlprefix + dataname)
# Rdatasets currently exports the index column as 'rownames' (the book-era
# CSVs left it blank, which pandas auto-names 'Unnamed: 0') -- handle both.
index_col = 'rownames' if 'rownames' in bwt.columns else 'Unnamed: 0'
bwt = bwt.drop(index_col, axis=1)
styles = {0: ['o', 'red'], 1: ['^', 'blue']}
for k in styles:
    grp = bwt[bwt.smoke == k]
    m, b = np.polyfit(grp.age, grp.bwt, 1)  # fit a straight line
    plt.scatter(grp.age, grp.bwt, c=styles[k][1], s=15, linewidth=0,
        marker=styles[k][0])
    plt.plot(grp.age, m * grp.age + b, '-', color=styles[k][1])

plt.xlabel('age')
plt.ylabel('birth weight (g)')
plt.legend(['non-smokers', 'smokers'], prop={'size': 8},
    loc=(0.5, 0.8))
plt.show()
