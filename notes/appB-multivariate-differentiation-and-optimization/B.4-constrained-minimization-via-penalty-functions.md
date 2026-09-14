---
appendix: B
section: "B.4"
title: "Constrained Minimization via Penalty Functions"
pdf_pages: "433-438"
---

# B.4 Constrained Minimization via Penalty Functions

A constrained optimization problem of the form (B.13) can sometimes be reformulated as a simpler unconstrained problem — for example, the unconstrained set $\mathcal{Y}$ can be transformed to the feasible region $\mathcal{X}$ of the constrained problem via a function $\boldsymbol{\phi} : \mathbb{R}^n \to \mathbb{R}^n$ such that $\mathcal{X} = \boldsymbol{\phi}(\mathcal{Y})$. Then, (B.13) is equivalent to the minimization problem

$$
\min_{\boldsymbol{y}\in\mathcal{Y}} f(\boldsymbol{\phi}(\boldsymbol{y})),
$$

in the sense that a solution $\boldsymbol{x}^*$ of the original problem is obtained from a transformed solution $\boldsymbol{y}^*$ via $\boldsymbol{x}^* = \boldsymbol{\phi}(\boldsymbol{y}^*)$. Table B.2 lists some examples of possible transformations.

**Table B.2: Some transformations to eliminate constraints.**

| Constrained | Unconstrained |
|---|---|
| $x > 0$ | $\exp(y)$ |
| $x \geqslant 0$ | $y^2$ |
| $a \leqslant x \leqslant b$ | $a + (b-a)\sin^2(y)$ |

Unfortunately, an unconstrained minimization method used in combination with these transformations is rarely effective. Instead, it is more common to use penalty functions.

The overarching idea of **penalty functions** is to transform a constrained problem into an unconstrained problem by adding weighted constraint-violation terms to the original objective function, with the premise that the new problem has a solution that is identical or close to the original one.

For example, if there are only equality constraints, then

$$
\widetilde{f}(\boldsymbol{x}) := f(\boldsymbol{x}) + \sum_{i=1}^m a_i |h_i(\boldsymbol{x})|^p
$$

for some constants $a_1,\dots,a_m > 0$ and integer $p \in \{1,2\}$, gives an **exact penalty function**, in the sense that the minimizer of the penalized function $\widetilde{f}$ is equal to the minimizer of $f$ subject to the $m$ equality constraints $h_1,\dots,h_m$. With the addition of inequality constraints, one could use

$$
\widetilde{f}(\boldsymbol{x}) = f(\boldsymbol{x}) + \sum_{i=1}^m a_i |h_i(\boldsymbol{x})|^p + \sum_{j=1}^k b_j \max\{g_j(\boldsymbol{x}), 0\}
$$

for some constants $a_1,\dots,a_m, b_1,\dots,b_k > 0$.

**Example B.11 (Alternating Direction Method of Multipliers).** The Lagrange method is designed to handle convex minimization subject to equality constraints. Nevertheless, some practical algorithms may still use the penalty function approach in combination with the Lagrangian method. An example is the **alternating direction method of multipliers (ADMM)** [17]. The ADMM solves problems of the form:

$$
\min_{\boldsymbol{x}\in\mathbb{R}^n, \boldsymbol{z}\in\mathbb{R}^m} \; f(\boldsymbol{x}) + g(\boldsymbol{z})
$$
$$
\text{subject to: } \mathbf{A}\boldsymbol{x} + \mathbf{B}\boldsymbol{z} = \boldsymbol{c}, \tag{B.29}
$$

where $\mathbf{A} \in \mathbb{R}^{p\times n}$, $\mathbf{B} \in \mathbb{R}^{p\times m}$, and $\boldsymbol{c} \in \mathbb{R}^p$, and $f : \mathbb{R}^n \to \mathbb{R}$ and $g : \mathbb{R}^m \to \mathbb{R}$ are convex functions. The approach is to form an augmented Lagrangian

$$
\mathcal{L}_\varrho(\boldsymbol{x},\boldsymbol{z},\boldsymbol{\beta}) := f(\boldsymbol{x}) + g(\boldsymbol{z}) + \boldsymbol{\beta}^\top(\mathbf{A}\boldsymbol{x}+\mathbf{B}\boldsymbol{z}-\boldsymbol{c}) + \frac{\varrho}{2}\|\mathbf{A}\boldsymbol{x}+\mathbf{B}\boldsymbol{z}-\boldsymbol{c}\|^2,
$$

where $\varrho > 0$ is a penalty parameter, and $\boldsymbol{\beta} \in \mathbb{R}^p$ are dual variables. The ADMM then iterates through updates of the following form:

$$
\boldsymbol{x}^{(t+1)} = \operatorname*{argmin}_{\boldsymbol{x}\in\mathbb{R}^n} \mathcal{L}_\varrho(\boldsymbol{x}, \boldsymbol{z}^{(t)}, \boldsymbol{\beta}^{(t)})
$$
$$
\boldsymbol{z}^{(t+1)} = \operatorname*{argmin}_{\boldsymbol{z}\in\mathbb{R}^m} \mathcal{L}_\varrho(\boldsymbol{x}^{(t+1)}, \boldsymbol{z}, \boldsymbol{\beta}^{(t)})
$$
$$
\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \varrho\left(\mathbf{A}\boldsymbol{x}^{(t+1)} + \mathbf{B}\boldsymbol{z}^{(t+1)} - \boldsymbol{c}\right).
$$

Suppose that (B.13) has inequality constraints only. **Barrier functions** are an important example of penalty functions that can handle inequality constraints. The prototypical example is a **logarithmic barrier function** which gives the unconstrained optimization:

$$
\widetilde{f}(\boldsymbol{x}) = f(\boldsymbol{x}) - \nu \sum_{j=1}^k \ln(-g_j(\boldsymbol{x})), \quad \nu > 0,
$$

such that the minimizer of $\widetilde{f}$ tends to the minimizer of $f$ as $\nu \to 0$. Direct minimization of $\widetilde{f}$ via an unconstrained minimization algorithm is frequently too difficult. Instead, it is common to combine the logarithmic barrier function with the Lagrangian method as follows.

The idea is to introduce $k$ nonnegative auxiliary or **slack variables** $s_1,\dots,s_k$ that satisfy the equalities $g_j(\boldsymbol{x}) + s_j = 0$ for all $j$. These equalities ensure that the inequality constraints are maintained: $g_j(\boldsymbol{x}) = -s_j \leqslant 0$ for all $j$. Then, instead of the unconstrained optimization of $\widetilde{f}$, we consider the unconstrained optimization of the Lagrangian:

$$
\mathcal{L}(\boldsymbol{x},\boldsymbol{s},\boldsymbol{\beta}) = f(\boldsymbol{x}) - \nu \sum_{j=1}^k \ln s_j + \sum_{j=1}^k \beta_j(g_j(\boldsymbol{x}) + s_j), \tag{B.30}
$$

where $\nu > 0$ and $\boldsymbol{\beta}$ are the Lagrange multipliers for the equalities $g_j(\boldsymbol{x})+s_j = 0$, $j=1,\dots,k$.

Observe how the logarithmic barrier function keeps the slack variables positive. In addition, while the optimization of $\widetilde{f}$ is over $n$ dimensions (recall that $\boldsymbol{x} \in \mathbb{R}^n$), the optimization of the Lagrangian function $\mathcal{L}$ is over $n+2k$ dimensions. Despite this enlargement of the search space with the variables $\boldsymbol{s}$ and $\boldsymbol{\beta}$, the optimization of the Lagrangian $\mathcal{L}$ is easier in practice than the direct optimization of $\widetilde{f}$.

**Example B.12 (Interior-Point Method for Nonnegativity).** One of the simplest and most common constrained optimization problems can be formulated as the minimization of $f(\boldsymbol{x})$ subject to nonnegative $\boldsymbol{x}$, that is: $\min_{\boldsymbol{x}\geqslant \boldsymbol{0}} f(\boldsymbol{x})$. In this case, the Lagrangian with logarithmic barrier (B.30) is:

$$
\mathcal{L}(\boldsymbol{x},\boldsymbol{s},\boldsymbol{\beta}) = f(\boldsymbol{x}) - \nu \sum_k \ln s_k + \boldsymbol{\beta}^\top(\boldsymbol{s}-\boldsymbol{x}).
$$

The KKT conditions in Theorem B.2 are a necessary condition for a minimizer, and yield the nonlinear system for $[\boldsymbol{x}^\top, \boldsymbol{s}^\top, \boldsymbol{\beta}^\top]^\top \in \mathbb{R}^{3n}$:

$$
\begin{bmatrix} \nabla f(\boldsymbol{x}) - \boldsymbol{\beta} \\ -\nu/\boldsymbol{s} + \boldsymbol{\beta} \\ \boldsymbol{s}-\boldsymbol{x} \end{bmatrix} = \boldsymbol{0},
$$

where $\nu/\boldsymbol{s}$ is a shorthand notation for a column vector with components $\{\nu/s_j\}$. To solve this system, we can use Newton's method for root finding (see, for example, Algorithm B.3.1), which requires a formula for the matrix of Jacobi of $\mathcal{L}$. Here, this $(3n)\times(3n)$ matrix is:

$$
\mathbf{J}_{\mathcal{L}}(\boldsymbol{x},\boldsymbol{s},\boldsymbol{\beta}) = \begin{bmatrix} \mathbf{H} & \mathbf{O} & -\mathbf{I} \\ \mathbf{O} & \mathbf{D} & \mathbf{I} \\ -\mathbf{I} & \mathbf{I} & \mathbf{O} \end{bmatrix} = \begin{bmatrix} \mathbf{H} & \mathbf{B} \\ \mathbf{B}^\top & \mathbf{E} \end{bmatrix},
$$

where $\mathbf{H}$ is the $n\times n$ Hessian of $f$ at $\boldsymbol{x}$; $\mathbf{D} := \operatorname{diag}(\nu/(\boldsymbol{s}\odot\boldsymbol{s}))$ is an $n\times n$ diagonal matrix; $\mathbf{B} := [\mathbf{O}, -\mathbf{I}]$ is an $n\times(2n)$ matrix, and[^1]

$$
\mathbf{E} := \begin{bmatrix} \mathbf{D} & \mathbf{I} \\ \mathbf{I} & \mathbf{O} \end{bmatrix} = \begin{bmatrix} \mathbf{O} & \mathbf{I} \\ \mathbf{I} & -\mathbf{D} \end{bmatrix}^{-1}.
$$

Further, we define

$$
\mathbf{H}_\nu := (\mathbf{H} - \mathbf{B}\mathbf{E}^{-1}\mathbf{B}^\top)^{-1} = (\mathbf{H}+\mathbf{D})^{-1}.
$$

Using this notation and applying the matrix blockwise inversion formula (A.14), we obtain the inverse of the matrix of Jacobi:

$$
\begin{bmatrix} \mathbf{H} & \mathbf{B} \\ \mathbf{B}^\top & \mathbf{E} \end{bmatrix}^{-1} = \begin{bmatrix} \mathbf{H}_\nu & -\mathbf{H}_\nu \mathbf{B}\mathbf{E}^{-1} \\ -\mathbf{E}^{-1}\mathbf{B}^\top \mathbf{H}_\nu & \mathbf{E}^{-1} + \mathbf{E}^{-1}\mathbf{B}^\top \mathbf{H}_\nu \mathbf{B}\mathbf{E}^{-1} \end{bmatrix} = \begin{bmatrix} \mathbf{H}_\nu & \mathbf{H}_\nu & -\mathbf{H}_\nu \mathbf{D} \\ \mathbf{H}_\nu & \mathbf{H}_\nu & \mathbf{I}-\mathbf{H}_\nu \mathbf{D} \\ -\mathbf{D}\mathbf{H}_\nu & \mathbf{I}-\mathbf{D}\mathbf{H}_\nu & \mathbf{D}\mathbf{H}_\nu \mathbf{D} - \mathbf{D} \end{bmatrix}.
$$

Therefore, the search direction in Newton's root-finding method is given by:

$$
-\mathbf{J}_{\mathcal{L}}^{-1}\begin{bmatrix} \nabla f(\boldsymbol{x}) - \boldsymbol{\beta} \\ -\nu/\boldsymbol{s}+\boldsymbol{\beta} \\ \boldsymbol{s}-\boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \mathrm{d}\boldsymbol{x} \\ \mathrm{d}\boldsymbol{x}+\boldsymbol{x}-\boldsymbol{s} \\ \nu/\boldsymbol{s} - \boldsymbol{\beta} - \mathbf{D}(\mathrm{d}\boldsymbol{x}+\boldsymbol{x}-\boldsymbol{s}) \end{bmatrix},
$$

where

$$
\mathrm{d}\boldsymbol{x} := -(\mathbf{H}+\mathbf{D})^{-1}\left[\nabla f(\boldsymbol{x}) - 2\nu/\boldsymbol{s} + \mathbf{D}\boldsymbol{x}\right],
$$

and we have assumed that $\mathbf{H}+\mathbf{D}$ is a positive-definite matrix. If at any step of the iteration the matrix $\mathbf{H}+\mathbf{D}$ fails to be positive-definite, then Newton's root-finding algorithm may fail to converge. Thus, any practical implementation will have to include a fail-safe feature to guard against this possibility.

In summary, for a given penalty parameter $\nu > 0$, we can locate the approximate nonnegative minimizer of $f$ using, for example, the version of the Newton–Raphson root-finding method given in Algorithm B.4.1.

In practice, one needs to choose a sufficiently small value for $\nu$, so that the output $\boldsymbol{x}_\nu$ of Algorithm B.4.1 is a good approximation to $\boldsymbol{x}^* = \operatorname*{argmin}_{\boldsymbol{x}\geqslant\boldsymbol{0}} f(\boldsymbol{x})$. Alternatively, one can create a decreasing sequence of penalty parameters $\nu_1 > \nu_2 > \cdots$ and compute the corresponding solutions $\boldsymbol{x}_{\nu_1}, \boldsymbol{x}_{\nu_2},\dots$ of the penalized problems. In the so-called **interior-point method**, a given $\boldsymbol{x}_{\nu_i}$ is used as an initial guess for computing $\boldsymbol{x}_{\nu_{i+1}}$ and so on until the approximation to the minimizer $\boldsymbol{x}^* = \operatorname*{argmin}_{\boldsymbol{x}\geqslant\boldsymbol{0}} f(\boldsymbol{x})$ is deemed accurate.

> **Algorithm B.4.1: Approximating $\boldsymbol{x}^* = \operatorname*{argmin}_{\boldsymbol{x}\geqslant\boldsymbol{0}} f(\boldsymbol{x})$ with Logarithmic Barrier**
>
> **input:** An initial guess $\boldsymbol{x}$ and stopping error $\varepsilon > 0$.
> **output:** The approximate nonnegative minimizer $\boldsymbol{x}_\nu$ of $f$.
>
> 1. $\boldsymbol{s} \leftarrow \boldsymbol{x}$, $\boldsymbol{\beta} \leftarrow \nu/\boldsymbol{s}$, $\mathrm{d}\boldsymbol{x} \leftarrow \boldsymbol{\beta}$
> 2. **while** $\|\mathrm{d}\boldsymbol{x}\| > \varepsilon$ and budget is not exhausted **do**
> 3. $\quad$ Compute the gradient $\boldsymbol{u}$ and the Hessian $\mathbf{H}$ of $f$ at $\boldsymbol{x}$.
> 4. $\quad \boldsymbol{s}_1 \leftarrow \nu/\boldsymbol{s}$, $\boldsymbol{s}_2 \leftarrow \boldsymbol{s}_1/\boldsymbol{s}$, $\boldsymbol{w} \leftarrow 2\boldsymbol{s}_1 - \boldsymbol{u} - \boldsymbol{s}_2 \odot \boldsymbol{x}$
> 5. $\quad$ **if** $(\mathbf{H} + \operatorname{diag}(\boldsymbol{s}_2)) > 0$ **then** *// if Cholesky successful*
> 6. $\quad\quad$ Compute the Cholesky factor $\mathbf{L}$ satisfying $\mathbf{L}\mathbf{L}^\top = \mathbf{H}+\operatorname{diag}(\boldsymbol{s}_2)$.
> 7. $\quad\quad \mathrm{d}\boldsymbol{x} \leftarrow \mathbf{L}^{-1}\boldsymbol{w}$ (computed by forward substitution)
> 8. $\quad\quad \mathrm{d}\boldsymbol{x} \leftarrow \mathbf{L}^{-\top}\mathrm{d}\boldsymbol{x}$ (computed by backward substitution)
> 9. $\quad$ **else**
> 10. $\quad\quad \mathrm{d}\boldsymbol{x} \leftarrow \boldsymbol{w}/\boldsymbol{s}_2$ *// if Cholesky fails, do steepest descent*
> 11. $\quad \mathrm{d}\boldsymbol{s} \leftarrow \mathrm{d}\boldsymbol{x}+\boldsymbol{x}-\boldsymbol{s}$, $\quad \mathrm{d}\boldsymbol{\beta} \leftarrow \boldsymbol{s}_1 - \boldsymbol{\beta} - \boldsymbol{s}_2 \odot \mathrm{d}\boldsymbol{s}$, $\quad \alpha \leftarrow 1$
> 12. $\quad$ **while** $\min_j\{s_j + \alpha\, \mathrm{d}s_j\} < 0$ **do**
> 13. $\quad\quad \alpha \leftarrow \alpha/2$ *// ensure nonnegative slack variables*
> 14. $\quad \boldsymbol{x} \leftarrow \boldsymbol{x}+\alpha\,\mathrm{d}\boldsymbol{x}$, $\quad \boldsymbol{s} \leftarrow \boldsymbol{s}+\alpha\,\mathrm{d}\boldsymbol{s}$, $\quad \boldsymbol{\beta} \leftarrow \boldsymbol{\beta}+\alpha\,\mathrm{d}\boldsymbol{\beta}$
> 15. **return** $\boldsymbol{x}_\nu \leftarrow \boldsymbol{x}$

[^1]: Here $\mathbf{O}$ is an $n\times n$ matrix of zeros and $\mathbf{I}$ is the $n\times n$ identity matrix.

## Further Reading

For an excellent introduction to convex optimization and Lagrangian duality see [18]. A classical text on optimization algorithms and, in particular, on quasi-Newton methods is [43]. For more details on the *alternating direction method of multipliers* see [17].
