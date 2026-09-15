"""
Chapter 3 - Monte Carlo Methods
Section 3.2.4 - Resampling (under 3.2 Monte Carlo Sampling)

Notes: notes/ch03-monte-carlo-methods/3.2-monte-carlo-sampling.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
from numpy.random import rand, choice
import matplotlib.pyplot as plt
# Using statsmodels' ECDF, matching the book's implementation (quotunif.py).
# If statsmodels is unavailable, a manual ECDF can be substituted: sort the
# data and plot np.arange(1, len(data)+1) / len(data) against the sorted
# data with plt.step or plt.plot.
from statsmodels.distributions.empirical_distribution import ECDF

# Example 3.7: resample the data x (ratios of two iid U(0,1) variables) to
# compare the empirical cdf of the resampled sample medians against that of
# the resampled sample means.
n = 100
N = 1000
x = rand(n) / rand(n)  # data: ratio of two iid U(0,1) variables
med = np.zeros(N)
ave = np.zeros(N)
for i in range(0, N):
    s = choice(x, n, replace=True)  # resampled data
    med[i] = np.median(s)
    ave[i] = np.mean(s)

med_cdf = ECDF(med)
ave_cdf = ECDF(ave)
plt.plot(med_cdf.x, med_cdf.y, label='resampled medians')
plt.plot(ave_cdf.x, ave_cdf.y, label='resampled means')
plt.xlabel('value')
plt.ylabel('empirical cdf')
plt.legend()
plt.show()
