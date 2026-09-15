"""
Chapter 3 - Monte Carlo Methods
Exercise 2

Notes: notes/ch03-monte-carlo-methods/exercises.md

Acceptance probability for the "generate a point uniformly in the
d-dimensional hypercube [-1,1]^d and accept if it falls inside the unit
d-ball" rejection sampling method, as a function of the dimension d:

    P(accept) = Vol(unit d-ball) / Vol([-1,1]^d)
              = (pi^(d/2) / Gamma(d/2 + 1)) / 2^d

Plotted for d = 1, ..., 50.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

d_vals = np.arange(1, 51)
prob_accept = (np.pi**(d_vals/2) / gamma(d_vals/2 + 1)) / 2**d_vals

plt.plot(d_vals, prob_accept, 'o-')
plt.yscale('log')
plt.xlabel('dimension $d$')
plt.ylabel('acceptance probability (log scale)')
plt.title('Acceptance probability of ball-in-cube rejection sampling')
plt.show()

print('Acceptance probabilities for d=1..10:', prob_accept[:10])
