"""
Chapter 3 - Monte Carlo Methods
Section 3.4.1 - Simulated Annealing (under 3.4 Monte Carlo for Optimization)

Notes: notes/ch03-monte-carlo-methods/3.4-monte-carlo-for-optimization.md

Example 3.15: simulated annealing to minimize a "wiggly" function.
"""

import numpy as np
import matplotlib.pyplot as plt


def wiggly(x):
    y = -np.exp(x**2/100)*np.sin(13*x-x**4)**5*np.sin(1-3*x**2)**2
    ind = np.vstack((np.argwhere(x < -2), np.argwhere(x > 2)))
    y[ind] = float('inf')
    return y


S = wiggly
beta = 0.999
sig = 0.5
T = 1
x = np.array([0])
xx = []
Sx = S(x)
while T > 10**(-3):
    T = beta*T
    y = x + sig*np.random.randn()
    Sy = S(y)
    alpha = min(np.exp(-(Sy-Sx)/T).item(), 1)
    if np.random.uniform() < alpha:
        x = y
        Sx = Sy
        xx = np.hstack((xx, x))

print('minimizer = {:3.3f}, minimum ={:3.3f}'.format(x[0], Sx[0]))
plt.plot(xx)
plt.xlabel('accepted iteration')
plt.ylabel('state $x$')
plt.show()
