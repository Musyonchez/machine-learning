"""
Chapter 3 - Monte Carlo Methods
Exercise 13

Notes: notes/ch03-monte-carlo-methods/exercises.md

Part (b): use an independence sampler MCMC to simulate from the target
Gamma(2,10) density f(x) = 100*x*exp(-10x), with proposal q(y|x) = g(y)
where g is the Exp(5) pdf (independent of the current state x). Generate
N=500 samples and compare the true Gamma(2,10) cdf with the empirical cdf
of the generated chain.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma as gamma_dist

f = lambda x: 100*x*np.exp(-10*x)
g_pdf = lambda x: 5*np.exp(-5*x)
g_sample = lambda: -np.log(np.random.rand())/5

N = 500
X = np.zeros(N)
X[0] = 0.1  # arbitrary positive start
for t in range(1, N):
    Y = g_sample()
    x_cur = X[t-1]
    if f(x_cur) > 0:
        alpha = min((f(Y)*g_pdf(x_cur)) / (f(x_cur)*g_pdf(Y)), 1)
    else:
        alpha = 1
    if np.random.rand() <= alpha:
        X[t] = Y
    else:
        X[t] = x_cur

# compare true cdf (Gamma(2,10)) with empirical cdf of the MCMC sample
xx = np.linspace(0, 1, 500)
true_cdf = gamma_dist.cdf(xx, a=2, scale=1/10)
X_sorted = np.sort(X)
emp_cdf = np.arange(1, N+1) / N

plt.plot(xx, true_cdf, label='true Gamma(2,10) cdf')
plt.step(X_sorted, emp_cdf, label='empirical cdf (MCMC)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.show()
