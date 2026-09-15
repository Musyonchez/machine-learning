"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 5

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# (a) Load the iris data set into a pandas DataFrame.
iris = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/iris.csv')
iris = iris.drop('Unnamed: 0', axis=1)
print("(a) iris head:")
print(iris.head())

species_list = iris['Species'].unique().tolist()

# (b) Boxplots of 'Petal.Length' for each of the three species, in one figure.
plt.figure()
petal_length_by_species = [
    iris[iris['Species'] == sp]['Petal.Length'] for sp in species_list
]
plt.boxplot(petal_length_by_species, labels=species_list)
plt.xlabel('Species')
plt.ylabel('Petal.Length')
plt.title('Boxplot of Petal.Length by Species')
plt.show()

# (c) Histogram with 20 bins for 'Petal.Length'.
plt.figure()
plt.hist(iris['Petal.Length'], bins=20)
plt.xlabel('Petal.Length')
plt.ylabel('Frequency')
plt.title('Histogram of Petal.Length (20 bins)')
plt.show()

# (d) Scatterplot of 'Sepal.Length' against 'Petal.Length', colored by 'Species'.
plt.figure()
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for sp in species_list:
    subset = iris[iris['Species'] == sp]
    plt.scatter(
        subset['Petal.Length'],
        subset['Sepal.Length'],
        color=colors.get(sp),
        label=sp,
    )
plt.xlabel('Petal.Length')
plt.ylabel('Sepal.Length')
plt.title('Sepal.Length vs Petal.Length, by Species')
plt.legend(title='Species')
plt.show()

# (e) Kernel density plots for 'Petal.Length' by species, using seaborn's kdeplot.
plt.figure()
sns.kdeplot(data=iris, x='Petal.Length', hue='Species')
plt.title('Kernel density of Petal.Length, by Species')
plt.show()
