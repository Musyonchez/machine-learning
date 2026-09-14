---
appendix: B
section: "B.3"
title: "Numerical Root-Finding and Minimization"
pdf_pages: "426-433"
---

# B.3 Numerical Root-Finding and Minimization

In order to minimize a $C^1$ function $f : \mathbb{R}^n \to \mathbb{R}$ one may solve

$$
\nabla f(\boldsymbol{x}) = \boldsymbol{0},
$$

which gives a stationary point of $f$. As a consequence, any technique for root-finding can be transformed into an unconstrained optimization method by attempting to locate roots of the gradient. However, as noted in Section B.2, not all stationary points are minima, and so additional information (such as is contained in the Hessian, if $f$ is $C^2$) needs to be considered in order to establish the type of stationary point.

Alternatively, a root of a continuous function $\boldsymbol{g} : \mathbb{R}^n \to \mathbb{R}^n$ may be found by minimizing the norm of $\boldsymbol{g}(\boldsymbol{x})$ over all $\boldsymbol{x}$; that is, by solving $\min_x f(\boldsymbol{x})$, with $f(\boldsymbol{x}) := \|\boldsymbol{g}(\boldsymbol{x})\|_p$, where for $p \geqslant 1$ the **$p$-norm** of $\boldsymbol{y} = [y_1,\dots,y_n]^\top$ is defined as

$$
\|\boldsymbol{y}\|_p := \left(\sum_{i=1}^n |y_i|^p\right)^{1/p}.
$$

Hence, any (un)constrained optimization method can be transformed into a technique for locating the roots of a function.

Starting with an initial guess $\boldsymbol{x}_0$, most minimization and root-finding algorithms create a sequence $\boldsymbol{x}_0, \boldsymbol{x}_1,\dots$ using the iterative updating rule:

$$
\boldsymbol{x}_{t+1} = \boldsymbol{x}_t + \alpha_t \boldsymbol{d}_t, \quad t=0,1,2,\dots, \tag{B.18}
$$

where $\alpha_t > 0$ is a (typically small) step size, called the **learning rate**, and the vector $\boldsymbol{d}_t$ is the search direction at step $t$. The iteration (B.18) continues until the sequence $\{\boldsymbol{x}_t\}$ is deemed to have converged to a solution, or a computational budget has been exhausted. The performance of all such iterative methods depends crucially on the quality of the initial guess $\boldsymbol{x}_0$.

There are two broad categories of iterative optimization algorithms of the form (B.18):

- Those of **line search** type, where at iteration $t$ we first compute a direction $\boldsymbol{d}_t$ and then determine a reasonable step size $\alpha_t$ along this direction. For example, in the case of minimization, $\alpha_t > 0$ may be chosen to approximately minimize $f(\boldsymbol{x}_t + \alpha \boldsymbol{d}_t)$ for fixed $\boldsymbol{x}_t$ and $\boldsymbol{d}_t$.

- Those of **trust region** type, where at each iteration $t$ we first determine a suitable step size $\alpha_t$ and then compute an approximately optimal direction $\boldsymbol{d}_t$.

In the following sections, we review several widely-used root-finding and optimization algorithms of the line search type.

## B.3.1 Newton-Like Methods

Suppose we wish to find roots of a function $f : \mathbb{R}^n \to \mathbb{R}^n$. If $f$ is in $C^1$, we can approximate $f$ around a point $\boldsymbol{x}_t$ as

$$
f(\boldsymbol{x}) \approx f(\boldsymbol{x}_t) + \mathbf{J}_f(\boldsymbol{x}_t)(\boldsymbol{x}-\boldsymbol{x}_t),
$$

where $\mathbf{J}_f$ is the *matrix of Jacobi* — the matrix of partial derivatives of $f$; see (B.3). When $\mathbf{J}_f(\boldsymbol{x}_t)$ is invertible, this linear approximation has root $\boldsymbol{x}_t - \mathbf{J}_f^{-1}(\boldsymbol{x}_t) f(\boldsymbol{x}_t)$. This gives the iterative updating formula (B.18) for finding roots of $f$ with direction $\boldsymbol{d}_t = -\mathbf{J}_f^{-1}(\boldsymbol{x}_t) f(\boldsymbol{x}_t)$ and learning rate $\alpha_t = 1$. This is known as **Newton's method** (or the **Newton–Raphson method**) for root-finding.

Instead of a unit learning rate, sometimes it is more effective to use an $\alpha_t$ that satisfies the **Armijo inexact line search** condition:

$$
\|f(\boldsymbol{x}_t + \alpha_t \boldsymbol{d}_t)\| < (1-\varepsilon_1 \alpha_t)\|f(\boldsymbol{x}_t)\|,
$$

where $\varepsilon_1$ is a small heuristically chosen constant, say $\varepsilon_1 = 10^{-4}$. For $C^1$ functions, such an $\alpha_t$ always exists by continuity and can be computed as in the following algorithm.

> **Algorithm B.3.1: Newton–Raphson for Finding Roots of $f(\boldsymbol{x}) = \boldsymbol{0}$**
>
> **input:** An initial guess $\boldsymbol{x}$ and stopping error $\varepsilon > 0$.
> **output:** The approximate root of $f(\boldsymbol{x}) = \boldsymbol{0}$.
>
> 1. **while** $\|f(\boldsymbol{x})\| > \varepsilon$ and budget is not exhausted **do**
> 2. $\quad$ Solve the linear system $\mathbf{J}_f(\boldsymbol{x})\boldsymbol{d} = -f(\boldsymbol{x})$.
> 3. $\quad \alpha \leftarrow 1$
> 4. $\quad$ **while** $\|f(\boldsymbol{x}+\alpha\boldsymbol{d})\| > (1-10^{-4}\alpha)\|f(\boldsymbol{x})\|$ **do**
> 5. $\quad\quad \alpha \leftarrow \alpha/2$
> 6. $\quad \boldsymbol{x} \leftarrow \boldsymbol{x} + \alpha \boldsymbol{d}$
> 7. **return** $\boldsymbol{x}$

We can adapt a root-finding Newton-like method in order to minimize a differentiable function $f : \mathbb{R}^n \to \mathbb{R}$. We simply try to locate a zero of the gradient of $f$. When $f$ is a $C^2$ function, the function $\nabla f : \mathbb{R}^n \to \mathbb{R}^n$ is continuous, and so the root of $\nabla f$ leads to the search direction

$$
\boldsymbol{d}_t = -\mathbf{H}_t^{-1}\nabla f(\boldsymbol{x}_t), \tag{B.19}
$$

where $\mathbf{H}_t$ is the Hessian matrix at $\boldsymbol{x}_t$ (the matrix of Jacobi of the gradient is the Hessian). When the learning rate $\alpha_t$ is equal to 1, the update $\boldsymbol{x}_t - \mathbf{H}_t^{-1}\nabla f(\boldsymbol{x}_t)$ can alternatively be derived by assuming that $f(\boldsymbol{x})$ is approximately quadratic and convex in the neighborhood of $\boldsymbol{x}_t$, that is,

$$
f(\boldsymbol{x}) \approx f(\boldsymbol{x}_t) + (\boldsymbol{x}-\boldsymbol{x}_t)^\top \nabla f(\boldsymbol{x}_t) + \frac{1}{2}(\boldsymbol{x}-\boldsymbol{x}_t)^\top \mathbf{H}_t (\boldsymbol{x}-\boldsymbol{x}_t), \tag{B.20}
$$

and then minimizing the right-hand side of (B.20) with respect to $\boldsymbol{x}$.

The following algorithm uses an **Armijo inexact line search** for minimization and guards against the possibility that the Hessian may not be positive definite (that is, its Cholesky decomposition does not exist).

> **Algorithm B.3.2: Newton–Raphson for Minimizing $f(\boldsymbol{x})$**
>
> **input:** An initial guess $\boldsymbol{x}$; stopping error $\varepsilon > 0$; line search parameter $\xi \in (0,1)$.
> **output:** An approximate minimizer of $f(\boldsymbol{x})$.
>
> 1. $\mathbf{L} \leftarrow \mathbf{I}_n$ (the identity matrix)
> 2. **while** $\|\nabla f(\boldsymbol{x})\| > \varepsilon$ and budget is not exhausted **do**
> 3. $\quad$ Compute the Hessian $\mathbf{H}$ at $\boldsymbol{x}$.
> 4. $\quad$ **if** $\mathbf{H} > 0$ **then** *// Cholesky is successful*
> 5. $\quad\quad$ Update $\mathbf{L}$ to be the Cholesky factor satisfying $\mathbf{L}\mathbf{L}^\top = \mathbf{H}$.
> 6. $\quad$ **else**
> 7. $\quad\quad$ Do not update the lower triangular $\mathbf{L}$.
> 8. $\quad \boldsymbol{d} \leftarrow -\mathbf{L}^{-1}\nabla f(\boldsymbol{x})$ (computed by forward substitution)
> 9. $\quad \boldsymbol{d} \leftarrow \mathbf{L}^{-\top}\boldsymbol{d}$ (computed by backward substitution)
> 10. $\quad \alpha \leftarrow 1$
> 11. $\quad$ **while** $f(\boldsymbol{x}+\alpha\boldsymbol{d}) > f(\boldsymbol{x}) + \alpha\,10^{-4}\nabla f(\boldsymbol{x})^\top \boldsymbol{d}$ **do**
> 12. $\quad\quad \alpha \leftarrow \alpha \times \xi$
> 13. $\quad \boldsymbol{x} \leftarrow \boldsymbol{x} + \alpha\boldsymbol{d}$
> 14. **return** $\boldsymbol{x}$

A downside with all Newton-like methods is that at each step they require the calculation and inversion of an $n \times n$ Hessian matrix, which has computing time of $O(n^3)$, and is thus infeasible for large $n$. One way to avoid this cost is to use quasi-Newton methods, described next.

## B.3.2 Quasi-Newton Methods

The idea behind quasi-Newton methods is to replace the inverse Hessian in (B.19) at iteration $t$ by an $n \times n$ matrix $\mathbf{C}$ satisfying the **secant condition**:

$$
\mathbf{C}\boldsymbol{g} = \boldsymbol{\delta}, \tag{B.21}
$$

where $\boldsymbol{\delta} \leftarrow \boldsymbol{x}_t - \boldsymbol{x}_{t-1}$ and $\boldsymbol{g} \leftarrow \nabla f(\boldsymbol{x}_t) - \nabla f(\boldsymbol{x}_{t-1})$ are vectors stored in memory at each iteration $t$. The secant condition is satisfied, for example, by the **Broyden's family** of matrices:

$$
\mathbf{A} + \frac{1}{\boldsymbol{u}^\top \boldsymbol{g}}(\boldsymbol{\delta} - \mathbf{A}\boldsymbol{g})\boldsymbol{u}^\top
$$

for some $\boldsymbol{u} \neq \boldsymbol{0}$ and $\mathbf{A}$. Since there is an infinite number of matrices that satisfy the condition (B.21), we need a way to determine a unique $\mathbf{C}$ at each iteration $t$ such that computing and storing $\mathbf{C}$ from one step to the next is fast and avoids any costly matrix inversion. The following examples illustrate how, starting with an initial guess $\mathbf{C} = \mathbf{I}$ at $t=0$, such a matrix $\mathbf{C}$ can be efficiently updated from one iteration to the next.

**Example B.8 (Low-Rank Hessian Update).** The quadratic model (B.20) can be strengthened by further assuming that $\exp(-f(\boldsymbol{x}))$ is proportional to a probability density that can be approximated in the neighborhood of $\boldsymbol{x}_t$ by the pdf of the $\mathcal{N}(\boldsymbol{x}_{t+1}, \mathbf{H}_t^{-1})$ distribution. This normal approximation allows us to measure the **discrepancy** between two pairs $(\boldsymbol{x}_1, \mathbf{H}_0^{-1})$ and $(\boldsymbol{x}_2, \mathbf{H}_1^{-1})$ using the Kullback–Leibler divergence between the pdfs of the $\mathcal{N}(\boldsymbol{x}_1, \mathbf{H}_0^{-1})$ and $\mathcal{N}(\boldsymbol{x}_2, \mathbf{H}_1^{-1})$ distributions (see Exercise 4 on page 351):

$$
\mathcal{D}(\boldsymbol{x}_1, \mathbf{H}_0^{-1} \mid \boldsymbol{x}_2, \mathbf{H}_1^{-1}) := \frac{1}{2}\Big(\operatorname{tr}(\mathbf{H}_1\mathbf{H}_0^{-1}) - \ln|\mathbf{H}_1\mathbf{H}_0^{-1}| + (\boldsymbol{x}_2-\boldsymbol{x}_1)^\top \mathbf{H}_1 (\boldsymbol{x}_2-\boldsymbol{x}_1) - n\Big). \tag{B.22}
$$

Suppose that the latest approximation to the inverse Hessian is $\mathbf{C}$ and we wish to compute an updated approximation for step $t$. One approach is to find the symmetric matrix that minimizes its Kullback–Leibler discrepancy from $\mathbf{C}$, as defined above, subject to the constraint (B.21). In other words,

$$
\min_{\mathbf{A}} \; \mathcal{D}(\boldsymbol{0}, \mathbf{C} \mid \boldsymbol{0}, \mathbf{A})
$$
$$
\text{subject to: } \mathbf{A}\boldsymbol{g} = \boldsymbol{\delta}, \; \mathbf{A} = \mathbf{A}^\top.
$$

The solution to this constrained optimization (see Exercise 10 on page 353) yields the **Broyden–Fletcher–Goldfarb–Shanno** or **BFGS formula** for updating the matrix $\mathbf{C}$ from one iteration to the next:

$$
\mathbf{C}_{\text{BFGS}} = \mathbf{C} + \underbrace{\frac{\boldsymbol{g}^\top \boldsymbol{\delta} + \boldsymbol{g}^\top \mathbf{C}\boldsymbol{g}}{(\boldsymbol{g}^\top \boldsymbol{\delta})^2}\boldsymbol{\delta}\boldsymbol{\delta}^\top - \frac{1}{\boldsymbol{g}^\top \boldsymbol{\delta}}\big(\boldsymbol{\delta}\boldsymbol{g}^\top \mathbf{C} + (\boldsymbol{\delta}\boldsymbol{g}^\top \mathbf{C})^\top\big)}_{\text{BFGS update}}. \tag{B.23}
$$

In a practical implementation, we keep a single copy of $\mathbf{C}$ in memory and apply the BFGS update to it at every iteration. Note that if the current $\mathbf{C}$ is symmetric, then so is the updated matrix. Moreover, the BFGS update is a matrix of rank two.

Since the Kullback–Leibler divergence is not symmetric, it is possible to flip the roles of $\mathbf{H}_0$ and $\mathbf{H}_1$ in (B.22) and instead solve

$$
\min_{\mathbf{A}} \; \mathcal{D}(\boldsymbol{0}, \mathbf{A} \mid \boldsymbol{0}, \mathbf{C})
$$
$$
\text{subject to: } \mathbf{A}\boldsymbol{g} = \boldsymbol{\delta}, \; \mathbf{A} = \mathbf{A}^\top.
$$

The solution (see Exercise 10 on page 353) gives the **Davidon–Fletcher–Powell** or **DFP formula** for updating the matrix $\mathbf{C}$ from one iteration to the next:

$$
\mathbf{C}_{\text{DFP}} = \mathbf{C} + \underbrace{\frac{\boldsymbol{\delta}\boldsymbol{\delta}^\top}{\boldsymbol{g}^\top \boldsymbol{\delta}} - \frac{\mathbf{C}\boldsymbol{g}\boldsymbol{g}^\top \mathbf{C}}{\boldsymbol{g}^\top \mathbf{C}\boldsymbol{g}}}_{\text{DFP update}}. \tag{B.24}
$$

Note that if the curvature condition $\boldsymbol{g}^\top \boldsymbol{\delta} > 0$ holds and the current $\mathbf{C}$ is symmetric positive definite, then so is its update.

**Example B.9 (Diagonal Hessian Update).** The original BFGS formula requires $O(n^2)$ storage and computation, which may be unmanageable for large $n$. One way to circumvent the prohibitive quadratic cost is to only store and update a diagonal Hessian matrix from one iteration to the next. If $\mathbf{C}$ is diagonal, then we may not be able to satisfy the secant condition (B.21) and maintain positive definiteness. Instead the secant condition (B.21) can be relaxed to the set of inequalities $\boldsymbol{g} \geqslant \mathbf{C}^{-1}\boldsymbol{\delta}$, which are related to the definition of a subgradient for convex functions. We can then find a unique diagonal matrix by minimizing $\mathcal{D}(\boldsymbol{x}_t, \mathbf{C} \mid \boldsymbol{x}_{t+1}, \mathbf{A})$ with respect to $\mathbf{A}$ and subject to the constraints $\mathbf{A}\boldsymbol{g} \geqslant \boldsymbol{\delta}$ and $\mathbf{A}$ is diagonal. The solution (Exercise 15 on page 353) yields the updating formula for a diagonal element $c_i$ of $\mathbf{C}$:

$$
c_i \leftarrow \begin{cases} \dfrac{2c_i}{1+\sqrt{1+4c_i u_i^2}}, & \text{if } \dfrac{2c_i}{1+\sqrt{1+4c_i u_i^2}} \geqslant \delta_i/g_i \\[2mm] \delta_i/g_i, & \text{otherwise,} \end{cases} \tag{B.25}
$$

where $\boldsymbol{u} := \nabla f(\boldsymbol{x}_t)$ and we assume a unit learning rate: $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t - \mathbf{A}\boldsymbol{u}$.

**Example B.10 (Scalar Hessian Update).** If the identity matrix is used in place of the Hessian in (B.19), one obtains **steepest descent** or **gradient descent** methods, in which the iteration (B.18) reduces to $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t - \alpha_t \nabla f(\boldsymbol{x}_t)$.

The rationale for the name *steepest descent* is as follows. If we start from any point $\boldsymbol{x}$ and make an infinitesimal move in some direction, then the function value is reduced by the largest magnitude in the (unit norm) direction: $\boldsymbol{u}^* := -\nabla f(\boldsymbol{x})/\|\nabla f(\boldsymbol{x})\|$. This is seen from the following inequality for all unit vectors $\boldsymbol{u}$ (that is, $\|\boldsymbol{u}\| = 1$):

$$
\frac{\mathrm{d}}{\mathrm{d}t} f(\boldsymbol{x}+t\boldsymbol{u}^*)\Big|_{t=0} \leqslant \frac{\mathrm{d}}{\mathrm{d}t} f(\boldsymbol{x}+t\boldsymbol{u})\Big|_{t=0}.
$$

Observe that equality is achieved if and only if $\boldsymbol{u} = \boldsymbol{u}^*$. This inequality is an easy consequence of the Cauchy–Schwarz inequality:

$$
-\nabla f^\top \boldsymbol{u} \leqslant |\nabla f^\top \boldsymbol{u}| \underbrace{\leqslant}_{\text{Cauchy–Schwarz}} \|\boldsymbol{u}\|\,\|\nabla f\| = \|\nabla f\| = -\nabla f^\top \boldsymbol{u}^*.
$$

The steepest descent iteration, $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t - \alpha_t \nabla f(\boldsymbol{x}_t)$, still requires a suitable choice of the learning rate $\alpha_t$. An alternative way to think about the iteration is to assume that the learning rate is always unity, and that at each iteration we use an inverse Hessian matrix of the form $\alpha_t \mathbf{I}$ for some positive constant $\alpha_t$. Satisfying the secant condition (B.21) with a matrix of the form $\mathbf{C} = \alpha \mathbf{I}$ is not possible. However, it is possible to choose $\alpha$ so that the secant condition (B.21) is satisfied in the direction of $\boldsymbol{g}$ (or alternatively $\boldsymbol{\delta}$). This gives the **Barzilai–Borwein formulas** for the learning rate at iteration $t$:

$$
\alpha_t = \frac{\boldsymbol{g}^\top \boldsymbol{\delta}}{\|\boldsymbol{g}\|^2} \quad \left(\text{or alternatively } \alpha_t = \frac{\|\boldsymbol{\delta}\|^2}{\boldsymbol{\delta}^\top \boldsymbol{g}}\right). \tag{B.26}
$$

## B.3.3 Normal Approximation Method

Let $\varphi_{\mathbf{H}_t^{-1}}(\boldsymbol{x}-\boldsymbol{x}_{t+1})$ denote the pdf of the $\mathcal{N}(\boldsymbol{x}_{t+1}, \mathbf{H}_t^{-1})$ distribution. As we already saw in Example B.8, the quadratic approximation (B.20) of $f$ in the neighborhood of $\boldsymbol{x}_t$ is equivalent (up to a constant) to the minus of the logarithm of the pdf $\varphi_{\mathbf{H}_t^{-1}}(\boldsymbol{x}-\boldsymbol{x}_{t+1})$. In other words, we use $\varphi_{\mathbf{H}_t^{-1}}(\boldsymbol{x}-\boldsymbol{x}_{t+1})$ as a simple model for the density

$$
\exp(-f(\boldsymbol{x})) \Big/ \int \exp(-f(\boldsymbol{y}))\,\mathrm{d}\boldsymbol{y}.
$$

One consequence of the normal approximation is that for $\boldsymbol{x}$ in the neighborhood of $\boldsymbol{x}_{t+1}$, we can write:

$$
-\nabla f(\boldsymbol{x}) \approx \frac{\partial}{\partial \boldsymbol{x}} \ln \varphi_{\mathbf{H}_t^{-1}}(\boldsymbol{x}-\boldsymbol{x}_{t+1}) = -\mathbf{H}_t(\boldsymbol{x}-\boldsymbol{x}_{t+1}).
$$

In other words, using the fact that $\mathbf{H}_t^\top = \mathbf{H}_t$,

$$
\nabla f(\boldsymbol{x})[\nabla f(\boldsymbol{x})]^\top \approx \mathbf{H}_t(\boldsymbol{x}-\boldsymbol{x}_{t+1})(\boldsymbol{x}-\boldsymbol{x}_{t+1})^\top \mathbf{H}_t,
$$

and taking expectations on both sides with respect to $X \sim \mathcal{N}(\boldsymbol{x}_{t+1}, \mathbf{H}_t^{-1})$ gives:

$$
\mathbb{E}\,\nabla f(X)[\nabla f(X)]^\top \approx \mathbf{H}_t.
$$

This suggests that, given the gradient vectors computed in the past $h$ (where $h$ stands for **h**istory) of Newton iterations:

$$
\boldsymbol{u}_i := \nabla f(\boldsymbol{x}_i), \quad i = t-(h-1),\dots,t,
$$

the Hessian matrix $\mathbf{H}_t$ can be approximated via the average

$$
\frac{1}{h}\sum_{i=t-h+1}^t \boldsymbol{u}_i \boldsymbol{u}_i^\top.
$$

A shortcoming of this approximation is that, unless $h$ is large enough, the Hessian approximation $\sum_{i=t-h+1}^t \boldsymbol{u}_i \boldsymbol{u}_i^\top$ may not be full rank and hence not invertible. To ensure that the Hessian approximation is invertible, we add a suitable diagonal matrix $\mathbf{A}_0$ to obtain the **regularized** version of the approximation:

$$
\mathbf{H}_t \approx \mathbf{A}_0 + \frac{1}{h}\sum_{i=t-h+1}^t \boldsymbol{u}_i \boldsymbol{u}_i^\top.
$$

With this full-rank approximation of the Hessian, the Newton search direction in (B.19) becomes:

$$
\boldsymbol{d}_t = -\left(\mathbf{A}_0 + \frac{1}{h}\sum_{i=t-h+1}^t \boldsymbol{u}_i \boldsymbol{u}_i^\top\right)^{-1} \boldsymbol{u}_t. \tag{B.27}
$$

Thus, $\boldsymbol{d}_t$ can be computed in $O(h^2 n)$ time via the Sherman–Morrison Algorithm A.6.1. Further to this, the search direction (B.27) can be efficiently updated to the next one:

$$
\boldsymbol{d}_{t+1} = -\left(\mathbf{A}_0 + \frac{1}{h}\sum_{i=t-h+2}^{t+1} \boldsymbol{u}_i \boldsymbol{u}_i^\top\right)^{-1} \boldsymbol{u}_{t+1}
$$

in $O(hn)$ time, thus avoiding the usual $O(h^2 n)$ cost (see Exercise 6 on page 352).

## B.3.4 Nonlinear Least Squares

Consider the squared-error training loss in nonlinear regression:

$$
\ell_\tau(g(\cdot\mid\boldsymbol{\beta})) = \frac{1}{n}\sum_{i=1}^n (g(\boldsymbol{x}_i\mid\boldsymbol{\beta}) - y_i)^2,
$$

where $g(\cdot\mid\boldsymbol{\beta})$ is a nonlinear prediction function that depends on the parameter $\boldsymbol{\beta}$ (for example, (5.29) shows the nonlinear logistic prediction function). The training loss can be written as $\frac{1}{n}\|\boldsymbol{g}(\tau\mid\boldsymbol{\beta}) - \boldsymbol{y}\|^2$, where $\boldsymbol{g}(\tau\mid\boldsymbol{\beta}) := [g(\boldsymbol{x}_1\mid\boldsymbol{\beta}),\dots,g(\boldsymbol{x}_n\mid\boldsymbol{\beta})]^\top$ is the vector of outputs.

We wish to minimize the training loss in terms of $\boldsymbol{\beta}$. In the Newton-like methods in Section B.3.1, one derives an iterative minimization algorithm that is inspired by a Taylor expansion of $\ell_\tau(g(\cdot\mid\boldsymbol{\beta}))$. Instead, given a current guess $\boldsymbol{\beta}_t$, we can consider the Taylor expansion of the nonlinear prediction function $\boldsymbol{g}$:

$$
\boldsymbol{g}(\tau\mid\boldsymbol{\beta}) \approx \boldsymbol{g}(\tau\mid\boldsymbol{\beta}_t) + \mathbf{G}_t(\boldsymbol{\beta}-\boldsymbol{\beta}_t),
$$

where $\mathbf{G}_t := \mathbf{J}_g(\boldsymbol{\beta}_t)$ is the matrix of Jacobi of $\boldsymbol{g}(\tau\mid\boldsymbol{\beta})$ at $\boldsymbol{\beta}_t$. Denoting the residual $\boldsymbol{e}_t := \boldsymbol{g}(\tau\mid\boldsymbol{\beta}_t) - \boldsymbol{y}$ and replacing $\boldsymbol{g}(\tau\mid\boldsymbol{\beta})$ with its Taylor approximation in $\ell_\tau(g(\cdot\mid\boldsymbol{\beta}))$, we obtain the approximation to the training loss in the neighborhood of $\boldsymbol{\beta}_t$:

$$
\ell_\tau(g(\cdot\mid\boldsymbol{\beta})) \approx \frac{1}{n}\left\|\mathbf{G}_t(\boldsymbol{\beta}-\boldsymbol{\beta}_t) + \boldsymbol{e}_t\right\|^2.
$$

The minimization of the right-hand side is a linear least-squares problem and therefore $\boldsymbol{d}_t := \boldsymbol{\beta}-\boldsymbol{\beta}_t$ satisfies the normal equations: $\mathbf{G}_t^\top \mathbf{G}_t \boldsymbol{d}_t = \mathbf{G}_t^\top(-\boldsymbol{e}_t)$. Assuming that $\mathbf{G}_t^\top \mathbf{G}_t$ is invertible, the normal equations yield the **Gauss–Newton** search direction:

$$
\boldsymbol{d}_t = -(\mathbf{G}_t^\top \mathbf{G}_t)^{-1}\mathbf{G}_t^\top \boldsymbol{e}_t.
$$

Unlike the search direction (B.19) for Newton-like algorithms, the search direction of a Gauss–Newton algorithm does not require the computation of a Hessian matrix.

Observe that in the Gauss–Newton approach we determine $\boldsymbol{d}_t$ by viewing the search direction as coefficients in a linear regression with feature matrix $\mathbf{G}_t$ and response $-\boldsymbol{e}_t$. This suggests that instead of using a linear regression, we can compute $\boldsymbol{d}_t$ via a **ridge regression** with a suitable choice for the regularization parameter $\gamma$:

$$
\boldsymbol{d}_t = -(\mathbf{G}_t^\top \mathbf{G}_t + n\gamma \mathbf{I}_p)^{-1}\mathbf{G}_t^\top \boldsymbol{e}_t.
$$

If we replace $n\mathbf{I}_p$ with the diagonal matrix $\operatorname{diag}(\mathbf{G}_t^\top \mathbf{G}_t)$, we then obtain the **Levenberg–Marquardt** search direction:

$$
\boldsymbol{d}_t = -\left(\mathbf{G}_t^\top \mathbf{G}_t + \gamma\, \operatorname{diag}(\mathbf{G}_t^\top \mathbf{G}_t)\right)^{-1}\mathbf{G}_t^\top \boldsymbol{e}_t. \tag{B.28}
$$

Recall that the ridge regularization parameter $\gamma$ has the following effect on the least-squares solution: When it is zero, then the solution $\boldsymbol{d}_t$ coincides with the search direction of the Gauss–Newton method, and when $\gamma$ tends to infinity, then $\|\boldsymbol{d}_t\|$ tends to zero. Thus, $\gamma$ controls both the magnitude and direction of vector $\boldsymbol{d}_t$. A simple version of the Levenberg–Marquardt algorithm is the following.

> **Algorithm B.3.3: Levenberg–Marquardt for Minimizing $\frac{1}{n}\|\boldsymbol{g}(\tau\mid\boldsymbol{\beta}) - \boldsymbol{y}\|^2$**
>
> **input:** An initial guess $\boldsymbol{\beta}_0$; stopping error $\varepsilon > 0$; training set $\tau$.
> **output:** An approximate minimizer of $\frac{1}{n}\|\boldsymbol{g}(\tau\mid\boldsymbol{\beta}) - \boldsymbol{y}\|^2$.
>
> 1. $t \leftarrow 0$ and $\gamma \leftarrow 0.01$ (or another default value)
> 2. **while** stopping condition is not met **do**
> 3. $\quad$ Compute the search direction $\boldsymbol{d}_t$ via (B.28).
> 4. $\quad \boldsymbol{e}_{t+1} \leftarrow \boldsymbol{g}(\tau\mid\boldsymbol{\beta}_t+\boldsymbol{d}_t) - \boldsymbol{y}$
> 5. $\quad$ **if** $\|\boldsymbol{e}_{t+1}\| < \|\boldsymbol{e}_t\|$ **then**
> 6. $\quad\quad \gamma \leftarrow \gamma/10, \quad \boldsymbol{e}_{t+1} \leftarrow \boldsymbol{e}_t, \quad \boldsymbol{\beta}_{t+1} \leftarrow \boldsymbol{\beta}_t + \boldsymbol{d}_t$
> 7. $\quad$ **else**
> 8. $\quad\quad \gamma \leftarrow \gamma \times 10$
> 9. $\quad t \leftarrow t+1$
> 10. **return** $\boldsymbol{\beta}_t$
