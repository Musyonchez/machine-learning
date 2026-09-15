"""
Chapter 2 - Statistical Learning
Exercise 13

Notes: notes/ch02-statistical-learning/exercises.md

Reproduce Figure 2.18: a large-sample approximation of the pointwise
variance of the learner (via (2.53)) for different values of u and p,
in the polynomial regression running example (Example 2.1 / 2.2):

    Var[g_T(x)] ~= (l* x^T H_p^{-1} x)/n + (x^T H_p^{-1} M_p H_p^{-1} x)/n

where H_p is the p x p Hilbert matrix, M_p is built from the squared
approximation error of the best-fit polynomial in H_p against the true
cubic h*(u) = 10 - 140u + 400u^2 - 250u^3, and l* = 25 is the irreducible
error variance. M_p = 0 for p >= 4 (the class contains the true model).
"""

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (registers 3D projection)

n = 100
l_star = 25  # irreducible error variance

# true model
beta_star = np.array([10, -140, 400, -250])


def h_star(u):
    return beta_star[0] + beta_star[1] * u + beta_star[2] * u ** 2 + beta_star[3] * u ** 3


# best-fit coefficients within H_p for p = 1, 2, 3 (equation 2.18); H_p = 0 for p >= 4
beta_p = {
    1: np.array([65 / 6]),
    2: np.array([-20 / 3, 35]),
    3: np.array([-5 / 2, 10, 25]),
}


def h_Hp(u, p):
    coeffs = beta_p[p]
    return sum(coeffs[k] * u ** k for k in range(len(coeffs)))


def hilbert_matrix(p):
    return np.array([[1 / (i + j + 1) for j in range(p)] for i in range(p)])


def M_matrix(p):
    M = np.zeros((p, p))
    if p >= 4:
        return M  # h_Hp == h_star exactly, so M_p = 0
    for i in range(p):
        for j in range(p):
            integrand = lambda u, i=i, j=j: (u ** (i + j)) * (h_Hp(u, p) - h_star(u)) ** 2
            M[i, j], _ = quad(integrand, 0, 1)
    return M


p_vals = [1, 3, 5, 7, 9]
u_vals = np.arange(0.05, 1.0, 0.1)

U, P = np.meshgrid(u_vals, p_vals)
Var = np.zeros_like(U)

for pi, p in enumerate(p_vals):
    H_p = hilbert_matrix(p)
    H_p_inv = np.linalg.inv(H_p)
    M_p = M_matrix(p)
    for ui, u in enumerate(u_vals):
        x = np.array([u ** k for k in range(p)])
        var_est = (l_star * (x @ H_p_inv @ x)) / n
        var_approx = (x @ H_p_inv @ M_p @ H_p_inv @ x) / n
        Var[pi, ui] = var_est + var_approx
        print(f'p = {p}, u = {u:.2f}: Var = {Var[pi, ui]:.4f}')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xpos = U.ravel()
ypos = P.ravel()
zpos = np.zeros_like(xpos)
dz = Var.ravel()

ax.bar3d(xpos, ypos, zpos, dx=0.05, dy=0.5, dz=dz, shade=True)
ax.set_xlabel('u')
ax.set_ylabel('p')
ax.set_zlabel('Var[$g_T(x)$]')
plt.show()
