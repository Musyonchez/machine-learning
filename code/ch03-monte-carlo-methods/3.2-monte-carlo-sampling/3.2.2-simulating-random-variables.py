"""
Chapter 3 - Monte Carlo Methods
Section 3.2.2 - Simulating Random Variables (under 3.2 Monte Carlo Sampling)

Notes: notes/ch03-monte-carlo-methods/3.2-monte-carlo-sampling.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

# Example 3.2 (bvnormal.py): draw N samples from a bivariate normal
# distribution with correlation r via a Cholesky factorization of the
# covariance matrix Sigma, then scatter-plot the samples.
N = 1000
r = 0.0   # correlation; change to 0.8 for the other panel of Figure 3.1
Sigma = np.array([[1, r], [r, 1]])
B = np.linalg.cholesky(Sigma)
x = B @ randn(2, N)
plt.scatter([x[0, :]], [x[1, :]], alpha=0.4, s=4)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.axis('equal')
plt.show()
