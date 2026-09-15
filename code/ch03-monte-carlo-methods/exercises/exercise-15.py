"""
Chapter 3 - Monte Carlo Methods
Exercise 15

Notes: notes/ch03-monte-carlo-methods/exercises.md

Part (b): Gibbs sampler for f(x,y) = c*exp(-(xy+x+y)) for x,y >= 0. Output
1000 points.

Conditional pdfs: f(x|y) is proportional to exp(-x(y+1)), i.e.
(X|Y=y) ~ Exp(rate=y+1); similarly (Y|X=x) ~ Exp(rate=x+1).
"""

import numpy as np
import matplotlib.pyplot as plt

n_samples = 1000
x, y = 1.0, 1.0
samples = np.zeros((n_samples, 2))
for t in range(n_samples):
    x = np.random.exponential(1/(y+1))  # (X|Y=y) ~ Exp(rate=y+1)
    y = np.random.exponential(1/(x+1))  # (Y|X=x) ~ Exp(rate=x+1)
    samples[t] = [x, y]

plt.scatter(samples[:, 0], samples[:, 1], s=8, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gibbs sampler for f(x,y) = c*exp(-(xy+x+y))')
plt.show()
