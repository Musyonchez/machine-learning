"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 7

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import time
import pandas as pd

# The KASANDR data set is a ~900MB compressed archive from the UCI repository:
#   https://archive.ics.uci.edu/ml/machine-learning-databases/00385/de.tar.bz2
# Uncompressed, it contains 'train_de.csv' (~3GB, ~1.9M rows) and 'test_de.csv'
# (~372MB, ~15.8M rows), both tab-delimited with 7 attributes.
#
# This is far too large to download and run automatically here. The code below is
# written to faithfully match what the book asks for, but is guarded behind
# `if __name__ == '__main__':` and is NOT executed automatically. To actually run
# this exercise: download and extract de.tar.bz2 from the URL above into the
# current working directory, then run this script directly.
#
# Column names: the exact attribute names should be checked against the KASANDR
# documentation/readme bundled with the archive; 'userid' and 'merchantid' below
# are a reasonable guess at the user and merchant identifier columns and may need
# to be adjusted to match the actual header of train_de.csv (or test_de.csv).

if __name__ == '__main__':
    # (a) Load train_de.csv, timing how long it takes. If there isn't enough
    # memory, load test_de.csv instead (it is smaller, despite having more rows).
    t0 = time.time()
    de = pd.read_csv('train_de.csv', delimiter='\t')
    # de = pd.read_csv('test_de.csv', delimiter='\t')  # use this instead if memory is limited
    print(f"Loaded in {time.time() - t0:.1f}s")

    # (b) How many unique users and merchants are in this data set?
    n_users = de['userid'].nunique()
    n_merchants = de['merchantid'].nunique()
    print(f"Unique users: {n_users}")
    print(f"Unique merchants: {n_merchants}")
