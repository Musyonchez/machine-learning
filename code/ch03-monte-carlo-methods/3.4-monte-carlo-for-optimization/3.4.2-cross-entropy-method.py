"""
Chapter 3 - Monte Carlo Methods
Section 3.4.2 - Cross-Entropy Method (under 3.4 Monte Carlo for Optimization)

Notes: notes/ch03-monte-carlo-methods/3.4-monte-carlo-for-optimization.md

Example 3.16: cross-entropy method to minimize the same "wiggly" function used
in Example 3.15 (simulated annealing). The book imports `wiggly` from
simann.py; it is inlined here instead so this file is standalone.
"""

import numpy as np


def wiggly(x):
    y = -np.exp(x**2/100)*np.sin(13*x-x**4)**5*np.sin(1-3*x**2)**2
    ind = np.vstack((np.argwhere(x < -2), np.argwhere(x > 2)))
    y[ind] = float('inf')
    return y


np.set_printoptions(precision=3)
mu, sigma = 0, 3
N, Nel = 100, 10
eps = 10**-5
S = wiggly
while sigma > eps:
    X = np.random.randn(N, 1)*sigma + np.array(np.ones((N, 1)))*mu
    Sx = np.hstack((X, S(X)))
    sortSx = Sx[Sx[:, 1].argsort(), ]
    Elite = sortSx[0:Nel, :]
    mu = np.mean(Elite[:, 0])
    sigma = np.std(Elite[:, 0])
    print('S(mu)= {}, mu: {}, sigma: {}\n'.format(S(np.array([mu]))[0], mu, sigma))
