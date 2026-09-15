"""
Chapter 3 - Monte Carlo Methods
Exercise 10

Notes: notes/ch03-monte-carlo-methods/exercises.md

Simulate the 6-state Markov chain shown in Figure 3.17, starting in state 1.
(a) Simulate a path of N=100 steps.
(b) Compute the exact limiting (stationary) probabilities by solving the
    global balance equations pi @ P = pi, sum(pi) = 1.
(c) Verify the empirical long-run visit frequencies against the exact
    limiting probabilities from (b).

NOTE: Figure 3.17's exact transition-graph edges were not fully recoverable
from the source notes available for this repository (the diagram's precise
edge probabilities could not be verified). The matrix P below is therefore a
PLACEHOLDER -- it is row-stochastic (rows sum to 1) and strongly connected so
the simulation and stationary-distribution code below is fully runnable and
correct in method, but it should NOT be taken as a verified transcription of
the book's actual Figure 3.17. Replace P with the exact transition
probabilities from the book if higher fidelity is required.
"""

import numpy as np
import matplotlib.pyplot as plt

# Placeholder transition matrix for states 1-6 (0-indexed 0-5) -- see NOTE above.
P = np.array([
    [0.0, 0.2, 0.0, 0.3, 0.0, 0.5],
    [0.5, 0.0, 0.5, 0.0, 0.0, 0.0],
    [0.3, 0.0, 0.0, 0.7, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [0.5, 0.0, 0.0, 0.3, 0.0, 0.2],
    [0.0, 0.0, 0.1, 0.0, 0.9, 0.0],
])
assert np.allclose(P.sum(axis=1), 1), "rows of P must sum to 1"

n_states = P.shape[0]

# (a) simulate N=100 steps starting in state 1 (index 0)
N = 100
x = np.zeros(N, dtype=int)
x[0] = 0
for t in range(N-1):
    x[t+1] = np.searchsorted(np.cumsum(P[x[t], :]), np.random.rand())

plt.plot(range(N), x+1, 'o--')
plt.xlabel('step')
plt.ylabel('state')
plt.title('Simulated Markov chain path (100 steps)')
plt.show()

# (b) exact limiting probabilities: solve pi @ P = pi, sum(pi) = 1
A = np.vstack((P.T - np.eye(n_states), np.ones(n_states)))
b_vec = np.zeros(n_states + 1)
b_vec[-1] = 1
pi_exact, *_ = np.linalg.lstsq(A, b_vec, rcond=None)
print('Exact limiting probabilities:', pi_exact)

# (c) verify against empirical visit frequencies for a long simulation
N_long = 200000
x_long = np.zeros(N_long, dtype=int)
x_long[0] = 0
for t in range(N_long-1):
    x_long[t+1] = np.searchsorted(np.cumsum(P[x_long[t], :]), np.random.rand())
empirical_freq = np.array([(x_long == s).mean() for s in range(n_states)])
print('Empirical visit frequencies:', empirical_freq)
print('Difference from exact:', np.abs(empirical_freq - pi_exact))
