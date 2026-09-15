"""
Chapter 3 - Monte Carlo Methods
Exercise 8

Notes: notes/ch03-monte-carlo-methods/exercises.md

Generate and display 100 random vectors uniformly distributed within the
ellipse 5x^2 + 21xy + 25y^2 = 9.

Hint: generate uniformly in a circle of radius 3, then apply a linear
transform mapping that circle to the ellipse. The quadratic form
5x^2 + 21xy + 25y^2 corresponds to the matrix
    Q = [[5, 10.5], [10.5, 25]]
(x^T Q x = 5x^2 + 21xy + 25y^2, since the off-diagonal entries each
contribute 10.5*x*y + 10.5*y*x = 21xy).

We want A such that A^T Q A = I, i.e. A = Q^{-1/2} (computed via
eigendecomposition). Then points x = A @ u for u uniform in the disc of
radius 3 are uniform within the ellipse {x : x^T Q x <= 9}.
"""

import numpy as np
import matplotlib.pyplot as plt

Q = np.array([[5, 10.5], [10.5, 25]])
eigvals, eigvecs = np.linalg.eigh(Q)
Q_inv_sqrt = eigvecs @ np.diag(1/np.sqrt(eigvals)) @ eigvecs.T  # Q^(-1/2)

n = 100
# uniform points in disc of radius 3 (area-uniform via sqrt of uniform radius)
R = 3*np.sqrt(np.random.rand(n))
Theta = 2*np.pi*np.random.rand(n)
U = np.vstack((R*np.cos(Theta), R*np.sin(Theta)))  # shape (2, n)

points = Q_inv_sqrt @ U  # shape (2, n), uniform within the ellipse

plt.scatter(points[0, :], points[1, :], s=15)
plt.gca().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('100 points uniform within 5x^2 + 21xy + 25y^2 = 9')
plt.show()
