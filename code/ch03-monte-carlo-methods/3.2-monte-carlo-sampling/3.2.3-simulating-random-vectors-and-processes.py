"""
Chapter 3 - Monte Carlo Methods
Section 3.2.3 - Simulating Random Vectors and Processes (under 3.2 Monte Carlo Sampling)

Notes: notes/ch03-monte-carlo-methods/3.2-monte-carlo-sampling.md

TODO: transcribe the runnable code example(s) for this section here.
"""

import numpy as np
import matplotlib.pyplot as plt

# Example 3.6 (MCsim.py): simulate and plot a path of a 4-state Markov
# chain with transition matrix P, starting from state 1 (index 0).
n = 101
P = np.array([[0, 0.2, 0.5, 0.3],
              [0.5, 0, 0.5, 0],
              [0.3, 0.7, 0, 0],
              [0.1, 0, 0, 0.9]])
x = np.array(np.ones(n, dtype=int))
x[0] = 0
for t in range(0, n-1):
    x[t+1] = np.min(np.where(np.cumsum(P[x[t], :]) > np.random.rand()))
x = x + 1  # add 1 to all elements of the vector x (states are 1-4, not 0-3)
plt.plot(np.array(range(0, n)), x, 'o')
plt.plot(np.array(range(0, n)), x, '--')
plt.xlabel('step')
plt.ylabel('state')
plt.show()
