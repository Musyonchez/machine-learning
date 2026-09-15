"""
Chapter 3 - Monte Carlo Methods
Section 3.2.5.1 - Metropolis-Hastings Sampler (under 3.2.5 Markov Chain Monte Carlo)

Notes: notes/ch03-monte-carlo-methods/3.2-monte-carlo-sampling.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, exp, sqrt, sin
from numpy.random import rand, randn

# Example 3.8 (rwsamp.py): random walk Metropolis-Hastings sampler that
# draws (approximately) from a 2D target pdf f, proportional to a damped
# radial sine wave restricted to the square (-2*pi, 2*pi)^2.
N = 10000
a = lambda x: -2*pi < x
b = lambda x: x < 2*pi
f = lambda x1, x2: exp(-sqrt(x1**2+x2**2)/4) * (
        sin(2*sqrt(x1**2+x2**2))+1) * a(x1)*b(x1)*a(x2)*b(x2)

xx = np.zeros((N, 2))
x = np.zeros((1, 2))
for i in range(1, N):
    y = x + randn(1, 2)
    alpha = np.amin((f(y[0][0], y[0][1]) / f(x[0][0], x[0][1]), 1))
    r = rand() < alpha
    x = r*y + (1-r)*x
    xx[i, :] = x

plt.scatter(xx[:, 0], xx[:, 1], alpha=0.4, s=2)
plt.axis('equal')
plt.show()
