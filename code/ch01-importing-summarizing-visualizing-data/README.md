# Chapter 1 code — Importing, Summarizing, and Visualizing Data

Runnable code examples from the book, organized to mirror [`notes/ch01-importing-summarizing-visualizing-data/`](../../notes/ch01-importing-summarizing-visualizing-data/README.md).

Each section from the notes gets its own folder here. Inside, `.py` files hold the runnable code for that section's subsections (or for the section as a whole, if it has no numbered subsections).

| Folder | Corresponds to | Files |
|---|---|---|
| [1.1-introduction/](1.1-introduction/) | [1.1-introduction.md](../../notes/ch01-importing-summarizing-visualizing-data/1.1-introduction.md) | `1.1-introduction.py` |
| [1.2-structuring-features-according-to-type/](1.2-structuring-features-according-to-type/) | [1.2-structuring-features-according-to-type.md](../../notes/ch01-importing-summarizing-visualizing-data/1.2-structuring-features-according-to-type.md) | `1.2-structuring-features-according-to-type.py` |
| [1.3-summary-tables/](1.3-summary-tables/) | [1.3-summary-tables.md](../../notes/ch01-importing-summarizing-visualizing-data/1.3-summary-tables.md) | `1.3-summary-tables.py` |
| [1.4-summary-statistics/](1.4-summary-statistics/) | [1.4-summary-statistics.md](../../notes/ch01-importing-summarizing-visualizing-data/1.4-summary-statistics.md) | `1.4-summary-statistics.py` |
| [1.5-visualizing-data/](1.5-visualizing-data/) | [1.5-visualizing-data.md](../../notes/ch01-importing-summarizing-visualizing-data/1.5-visualizing-data.md) | `1.5.1-plotting-qualitative-variables.py`, `1.5.2.1-boxplot.py`, `1.5.2.2-histogram.py`, `1.5.2.3-empirical-cumulative-distribution-function.py`, `1.5.3.1-two-way-plots-for-two-categorical-variables.py`, `1.5.3.2-plots-for-two-quantitative-variables.py`, `1.5.3.3-plots-for-one-qualitative-and-one-quantitative-variable.py` |
| [exercises/](exercises/) | [exercises.md](../../notes/ch01-importing-summarizing-visualizing-data/exercises.md) | `exercise-01.py` ... `exercise-08.py` (one file per exercise) |

## Independence

Every `.py` file here is fully standalone — it does its own imports and its own data loading/preparation (e.g. loading and recoding the `nutri` dataset), and never imports another file in this repo. This means some loading/recoding code is intentionally duplicated across files rather than shared.

Where a section's example uses a dataset (`nutri`, `iris`, `abalone`, `birthwt`, ...), each file loads it directly from its original public URL, so nothing needs to be pre-downloaded to run these scripts (except Exercise 7, which requires a manual ~900MB download and is guarded behind `if __name__ == '__main__':`).

Several files need `nutri`'s categorical columns recoded (the book only demonstrates this partially in 1.2, deferring the rest to Exercise 2). The exact label dictionaries used throughout — derived directly from the book's Table 1.2 and cross-checked against the book's own printed output (verified: `1.3-summary-tables.py`'s output matches the book's `fat.value_counts()` and crosstab numbers exactly) — are:
```python
GENDER_DICT = {1: 'Male', 2: 'Female'}
SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}
FAT_DICT = {1: 'butter', 2: 'margarine', 3: 'peanut', 4: 'sunflower',
            5: 'olive', 6: 'Isio4', 7: 'colza', 8: 'duck'}
FREQ_DICT = {0: 'Never', 1: 'Less than once a week', 2: 'Once a week',
             3: '2-3 times a week', 4: '4-6 times a week', 5: 'Every day'}
```

## Status

**Implemented.** All 19 files (11 section files + 8 exercise files) have working code, verified via syntax check on every file plus live smoke tests: `exercise-03.py` (offline), `1.4-summary-statistics.py` and `1.3-summary-tables.py` (network, output matches the book's printed numbers exactly), and `1.5.2.1-boxplot.py` (plotting, runs clean). Requires `pandas`, `matplotlib`, `seaborn`, `numpy`, and `xlrd` (for the old-format `.xls` file in the `nutri` examples) — install via `pip install pandas matplotlib seaborn numpy xlrd`.
