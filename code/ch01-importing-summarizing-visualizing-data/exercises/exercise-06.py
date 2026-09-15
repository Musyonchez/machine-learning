"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 6

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the EuStockMarkets data set from the same website as iris.
eu_stocks = pd.read_csv(
    'https://vincentarelbundock.github.io/Rdatasets/csv/datasets/EuStockMarkets.csv'
)
# Rdatasets currently exports the index column as 'rownames' (the book-era
# CSVs left it blank, which pandas auto-names 'Unnamed: 0') -- handle both.
if 'rownames' in eu_stocks.columns:
    eu_stocks = eu_stocks.drop('rownames', axis=1)
elif 'Unnamed: 0' in eu_stocks.columns:
    eu_stocks = eu_stocks.drop('Unnamed: 0', axis=1)

print("EuStockMarkets head:")
print(eu_stocks.head())

# (a) Vector of times (working days) between 1991.496 and 1998.646, increments of 1/260.
times = np.arange(1991.496, 1998.646, 1 / 260)
# np.arange's endpoint isn't guaranteed to exactly match the row count (floating
# point step accumulation), so trim both to whichever is shorter before plotting.
n = min(len(times), len(eu_stocks))
times = times[:n]
eu_stocks = eu_stocks.iloc[:n]

# (b) Line plot of the four indices over time, using a dictionary to map columns to colors.
color_map = {'DAX': 'blue', 'SMI': 'green', 'CAC': 'red', 'FTSE': 'cyan'}

plt.figure()
for col, color in color_map.items():
    plt.plot(times, eu_stocks[col], color=color, label=col)

plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.title('EuStockMarkets daily closing prices')
plt.legend()
plt.show()
