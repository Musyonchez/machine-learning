"""
Chapter 3 - Monte Carlo Methods
Section 3.2.2.2 - Acceptance-Rejection Method (under 3.2.2 Simulating Random Variables)

Notes: notes/ch03-monte-carlo-methods/3.2-monte-carlo-sampling.md

TODO: transcribe the runnable code example(s) for this section here.
"""

from math import exp, gamma, log
from numpy.random import rand

# Example 3.5: simulate from a Gamma(alpha=1.3, lambda=5.6) density f via
# acceptance-rejection, using an Exp(4) proposal density g and bounding
# constant C such that f(x) <= C * g(x) for all x.
alpha = 1.3
lam = 5.6
f = lambda x: lam**alpha * x**(alpha-1) * exp(-lam*x) / gamma(alpha)
g = lambda x: 4 * exp(-4*x)
C = 1.2

found = False
while not found:
    x = -log(rand()) / 4
    if C * g(x) * rand() <= f(x):
        found = True

print(x)
