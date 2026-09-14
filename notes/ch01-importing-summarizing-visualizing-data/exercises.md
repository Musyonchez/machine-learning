---
chapter: 1
section: "Exercises"
title: "Exercises"
pdf_pages: "33-36"
---

Before you attempt these exercises, make sure you have up-to-date versions of the relevant Python packages, specifically `matplotlib`, `pandas`, and `seaborn`. An easy way to ensure this is to update packages via the Anaconda Navigator, as explained in Appendix D.

**1.** Visit the UCI Repository `https://archive.ics.uci.edu/`. Read the description of the data and download the Mushroom data set `agaricus-lepiota.data`. Using `pandas`, read the data into a `DataFrame` called `mushroom`, via `read_csv`.

(a) How many features are in this data set?

(b) What are the initial names and types of the features?

(c) Rename the first feature (index 0) to `'edibility'` and the sixth feature (index 5) to `'odor'` [Hint: the column names in `pandas` are immutable; so individual columns cannot be modified directly. However it is possible to assign the entire column names list via `mushroom.columns = newcols`.]

(d) The 6th column lists the various odors of the mushrooms: encoded as `'a'`, `'c'`, .... Replace these with the names `'almond'`, `'creosote'`, etc. (categories corresponding to each letter can be found on the website). Also replace the `'edibility'` categories `'e'` and `'p'` with `'edible'` and `'poisonous'`.

(e) Make a contingency table cross-tabulating `'edibility'` and `'odor'`.

(f) Which mushroom odors should be avoided, when gathering mushrooms for consumption?

(g) What proportion of odorless mushroom samples were safe to eat?

**2.** Change the type and value of variables in the `nutri` data set according to Table 1.2 and save the data as a CSV file. The modified data should have eight categorical features, three floats, and two integer features.

**3.** It frequently happens that a table with data needs to be restructured before the data can be analyzed using standard statistical software. As an example, consider the test scores in Table 1.3 of 5 students before and after specialized tuition.

**Table 1.3:** Student scores.

| Student | Before | After |
|---|---|---|
| 1 | 75 | 85 |
| 2 | 30 | 50 |
| 3 | 100 | 100 |
| 4 | 50 | 52 |
| 5 | 60 | 65 |

This is not in the standard format described in Section 1.1. In particular, the student scores are divided over two columns, whereas the standard format requires that they are collected in one column, e.g., labelled `'Score'`. Reformat (by hand) the table in standard format, using three features:

- `'Score'`, taking continuous values,
- `'Time'`, taking values `'Before'` and `'After'`,
- `'Student'`, taking values from 1 to 5.

Useful methods for reshaping tables in `pandas` are `melt`, `stack`, and `unstack`.

**4.** Create a similar barplot as in Figure 1.5, but now plot the corresponding *proportions* of males and females in each of the three situation categories. That is, the heights of the bars should sum up to 1 for both barplots with the same `'gender'` value. [Hint: `seaborn` does not have this functionality built in, instead you need to first create a contingency table and use `matplotlib.pyplot` to produce the figure.] (☞ 2)

**5.** The `iris` data set, mentioned in Section 1.1, contains various features, including `'Petal.Length'` and `'Sepal.Length'`, of three species of iris: setosa, versicolor, and virginica.

(a) Load the data set into a `pandas` DataFrame object.

(b) Using `matplotlib.pyplot`, produce boxplots of `'Petal.Length'` for each the three species, in one figure.

(c) Make a histogram with 20 bins for `'Petal.Length'`.

(d) Produce a similar scatterplot for `'Sepal.Length'` against `'Petal.Length'` to that of the left plot in Figure 1.9. Note that the points should be colored according to the `'Species'` feature as per the legend in the right plot of the figure.

(e) Using the `kdeplot` method of the `seaborn` package, reproduce the right plot of Figure 1.9, where kernel density plots for `'Petal.Length'` are given. (☞ 131)

> **Figure 1.9:** Left: scatterplot of `'Sepal.Length'` against `'Petal.Length'`. Right: kernel density estimates of `'Petal.Length'` for the three species of iris. The scatterplot shows three well-separated clusters by species (setosa distinctly separate with short petals; versicolor and virginica overlapping somewhat with longer petals), and the kernel density plot shows three roughly bell-shaped, mostly non-overlapping density curves (setosa peak near Petal.Length ≈ 1.5, versicolor near 4, virginica near 5.5–6).

**6.** Import the data set `EuStockMarkets` from the same website as the `iris` data set above. The data set contains the daily closing prices of four European stock indices during the 1990s, for 260 working days per year.

(a) Create a vector of times (working days) for the stock prices, between 1991.496 and 1998.646 with increments of $1/260$.

(b) Reproduce Figure 1.10. [Hint: Use a dictionary to map column names (stock indices) to colors.]

> **Figure 1.10:** Closing stock indices for various European stock markets. Four line series (DAX in blue, SMI in green, CAC in red, FTSE in cyan) plotted from 1991 to 1999, all trending generally upward over the period, with SMI reaching the highest values (~8000) by 1998 and CAC the lowest (~4000), and all four showing increased volatility toward the end of the period.

**7.** Consider the `KASANDR` data set from the UCI Machine Learning Repository, which can be downloaded from

`https://archive.ics.uci.edu/ml/machine-learning-databases/00385/de.tar.bz2`.

This archive file has a size of 900Mb, so it may take a while to download. Uncompressing the file (e.g., via 7-Zip) yields a directory `de` containing two large CSV files: `test_de.csv` and `train_de.csv`, with sizes 372Mb and 3Gb, respectively. Such large data files can still be processed efficiently in `pandas`, provided there is enough memory. The files contain records of user information from Kelkoo web logs in Germany as well as meta-data on users, offers, and merchants. The data sets have 7 attributes and 1919561 and 15844717 rows, respectively. The data sets are anonymized via hex strings.

(a) Load `train_de.csv` into a `pandas` DataFrame object `de`, using

```python
read_csv('train_de.csv', delimiter = '\t')
```

If not enough memory is available, load `test_de.csv` instead. Note that entries are separated here by tabs, not commas. Time how long it takes for the file to load, using the `time` package. (It took 38 seconds for `train_de.csv` to load on one of our computers.)

(b) How many unique users and merchants are in this data set?

**8.** Visualizing data involving more than two features requires careful design, which is often more of an art than a science.

(a) Go to Vincent Arel-Bundock's website (URL given in Section 1.1) and read the `Orange` data set into a `pandas` DataFrame object called `orange`. Remove its first (unnamed) column.

(b) The data set contains the circumferences of 5 orange trees at various stages in their development. Find the names of the features.

(c) In Python, import `seaborn` and visualize the growth curves (circumference against age) of the trees, using the `regplot` and `FacetGrid` methods.
