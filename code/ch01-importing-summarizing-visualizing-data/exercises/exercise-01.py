"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 1

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import pandas as pd

# Load the Mushroom data set directly from the UCI repository.
mushroom = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data',
    header=None,
)

# (a) How many features are in this data set?
print("(a) Number of columns (features):", mushroom.shape[1])

# (b) What are the initial names and types of the features?
print("\n(b) Initial names and dtypes:")
print(mushroom.dtypes)

# (c) Rename the first feature (index 0) to 'edibility' and the sixth (index 5) to 'odor'.
mushroom = mushroom.rename(columns={0: 'edibility', 5: 'odor'})
print("\n(c) Columns after renaming 0 -> 'edibility', 5 -> 'odor':")
print(mushroom.columns.tolist())

# (d) Replace odor codes with descriptive names, and edibility codes with descriptive names.
odor_dict = {
    'a': 'almond',
    'l': 'anise',
    'c': 'creosote',
    'y': 'fishy',
    'f': 'foul',
    'm': 'musty',
    'n': 'none',
    'p': 'pungent',
    's': 'spicy',
}
edibility_dict = {'e': 'edible', 'p': 'poisonous'}

mushroom['odor'] = mushroom['odor'].replace(odor_dict)
mushroom['edibility'] = mushroom['edibility'].replace(edibility_dict)

print("\n(d) Value counts after recoding 'odor':")
print(mushroom['odor'].value_counts())
print("\n(d) Value counts after recoding 'edibility':")
print(mushroom['edibility'].value_counts())

# (e) Contingency table cross-tabulating 'edibility' and 'odor'.
edibility_odor = pd.crosstab(mushroom['edibility'], mushroom['odor'])
print("\n(e) Contingency table of edibility vs odor:")
print(edibility_odor)

# (f) Which odors should be avoided when gathering mushrooms for consumption?
# An odor is "safe" only if it never occurs among poisonous mushrooms (zero in the
# 'poisonous' row); any odor with a nonzero 'poisonous' count should be avoided.
unsafe_odors = edibility_odor.columns[edibility_odor.loc['poisonous'] > 0].tolist()
safe_odors = edibility_odor.columns[edibility_odor.loc['poisonous'] == 0].tolist()
print("\n(f) Odors to avoid (associated with poisonous mushrooms):", unsafe_odors)
print("(f) Odors that never appear on a poisonous mushroom:", safe_odors)

# (g) What proportion of odorless ('none') mushroom samples were safe to eat?
none_odor = mushroom[mushroom['odor'] == 'none']
proportion_edible = (none_odor['edibility'] == 'edible').mean()
print(f"\n(g) Proportion of odorless mushrooms that are edible: {proportion_edible:.4f}")
print(
    "(g) In other words, about "
    f"{proportion_edible * 100:.1f}% of mushrooms with no odor were safe to eat."
)
