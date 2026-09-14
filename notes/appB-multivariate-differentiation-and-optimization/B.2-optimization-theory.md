---
appendix: B
section: "B.2"
title: "Optimization Theory"
pdf_pages: "420-426"
---

# B.2 Optimization Theory

Optimization is concerned with finding minimal or maximal solutions of a real-valued **objective function** $f$ in some set $\mathcal{X}$:

$$
\min_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x}) \quad \text{or} \quad \max_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x}). \tag{B.12}
$$

Since any maximization problem can easily be converted into a minimization problem via the equivalence $\max_x f(\boldsymbol{x}) \equiv -\min_x -f(\boldsymbol{x})$, we focus only on minimization problems. We use the following terminology. A **local minimizer** of $f(\boldsymbol{x})$ is an element $\boldsymbol{x}^* \in \mathcal{X}$ such that $f(\boldsymbol{x}^*) \leqslant f(\boldsymbol{x})$ for all $\boldsymbol{x}$ in some neighborhood of $\boldsymbol{x}^*$. If $f(\boldsymbol{x}^*) \leqslant f(\boldsymbol{x})$ for all $\boldsymbol{x} \in \mathcal{X}$, then $\boldsymbol{x}^*$ is called a **global minimizer** or **global solution**. The set of global minimizers is denoted by

$$
\operatorname*{argmin}_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x}).
$$

The function value $f(\boldsymbol{x}^*)$ corresponding to a local/global minimizer $\boldsymbol{x}^*$ is referred to as the **local/global minimum** of $f(\boldsymbol{x})$.

Optimization problems may be classified by the set $\mathcal{X}$ and the objective function $f$. If $\mathcal{X}$ is countable, the optimization problem is called *discrete* or *combinatorial*. If instead $\mathcal{X}$ is a nondenumerable set such as $\mathbb{R}^n$ and $f$ takes values in a nondenumerable set, then the problem is said to be *continuous*. Optimization problems that are neither discrete nor continuous are said to be *mixed*.

The search set $\mathcal{X}$ is often defined by means of **constraints**. A standard setting for constrained optimization (minimization) is the following:

$$
\begin{aligned}
\min_{\boldsymbol{x}\in\mathcal{Y}} \quad & f(\boldsymbol{x}) \\
\text{subject to:} \quad & h_i(\boldsymbol{x}) = 0, \quad i=1,\dots,m, \\
& g_i(\boldsymbol{x}) \leqslant 0, \quad i=1,\dots,k.
\end{aligned} \tag{B.13}
$$

Here, $f$ is the objective function, and $\{g_i\}$ and $\{h_i\}$ are given functions so that $h_i(\boldsymbol{x}) = 0$ and $g_i(\boldsymbol{x}) \leqslant 0$ represent the **equality** and **inequality** constraints, respectively. The region $\mathcal{X} \subseteq \mathcal{Y}$ where the objective function is defined and where all the constraints are satisfied is called the **feasible region**. An optimization problem without constraints is said to be an **unconstrained** problem.

For an unconstrained continuous optimization problem, the search space $\mathcal{X}$ is often taken to be (a subset of) $\mathbb{R}^n$, and $f$ is assumed to be a $C^k$ function for sufficiently high $k$ (typically $k=2$ or $3$ suffices); that is, its $k$-th order derivative is continuous. For a $C^1$ function the standard approach to minimizing $f(\boldsymbol{x})$ is to solve the equation

$$
\nabla f(\boldsymbol{x}) = \boldsymbol{0}, \tag{B.14}
$$

where $\nabla f(\boldsymbol{x})$ is the **gradient** of $f$ at $\boldsymbol{x}$. The solutions $\boldsymbol{x}^*$ to (B.14) are called **stationary points**. Stationary points can be local/global minimizers, local/global maximizers, or **saddle points** (which are neither). If, in addition, the function is $C^2$, the condition

$$
\boldsymbol{y}^\top (\nabla^2 f(\boldsymbol{x}^*))\boldsymbol{y} > 0 \quad \text{for all } \boldsymbol{y} \neq \boldsymbol{0} \tag{B.15}
$$

ensures that the stationary point $\boldsymbol{x}^*$ is a local minimizer of $f$. The condition (B.15) states that the *Hessian* matrix of $f$ at $\boldsymbol{x}^*$ is *positive definite*. Recall that we write $\mathbf{H} > 0$ to indicate that a matrix $\mathbf{H}$ is positive definite.

In Figure B.2 we have a multiextremal objective function on $\mathcal{X} = \mathbb{R}$. There are four stationary points: two are local minimizers, one is a local maximizer, and one is neither a minimizer nor a maximizer, but a saddle point.

> **Figure B.2:** A multiextremal objective function of one variable $x$, plotted as $f(x)$. Moving left to right along the curve, four stationary points are marked: a local minimum, a local maximum, the global minimum (the lowest point on the curve), and a saddle point (a flat inflection where the curve levels off but is neither a local max nor min).

## B.2.1 Convexity and Optimization

An important class of optimization problems is related to the notion of **convexity**. A set $\mathcal{X}$ is said to be **convex** if for all $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathcal{X}$ it holds that $\alpha \boldsymbol{x}_1 + (1-\alpha)\boldsymbol{x}_2 \in \mathcal{X}$ for all $0 \leqslant \alpha \leqslant 1$.

In addition, the objective function $f$ is a **convex function** provided that for each $\boldsymbol{x}$ in the interior of $\mathcal{X}$ there exists a vector $\boldsymbol{v}$ such that

$$
f(\boldsymbol{y}) \geqslant f(\boldsymbol{x}) + (\boldsymbol{y}-\boldsymbol{x})^\top \boldsymbol{v}, \quad \boldsymbol{y} \in \mathcal{X}. \tag{B.16}
$$

The vector $\boldsymbol{v}$ in (B.16) may not be unique and is referred to as a **subgradient** of $f$.

One of the crucial properties of a convex function $f$ is that *Jensen's inequality* holds (see Exercise 14 in Chapter 2):

$$
\mathbb{E} f(X) \geqslant f(\mathbb{E} X),
$$

for any random vector $X$.

**Example B.6 (Convexity and Directional Derivative).** The **directional derivative** of a multivariate function $f$ at $\boldsymbol{x}$ in the direction $\boldsymbol{d}$ is defined as the right derivative of $g(t) := f(\boldsymbol{x}+t\boldsymbol{d})$ at $t=0$:

$$
\lim_{t\downarrow 0} \frac{f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x})}{t} = \lim_{t\uparrow\infty} t\,(f(\boldsymbol{x}+\boldsymbol{d}/t) - f(\boldsymbol{x})).
$$

This right derivative may not always exist. However, if $f$ is a convex function, then the directional derivative of $f$ at $\boldsymbol{x}$ in the interior of its domain always exists (in any direction $\boldsymbol{d}$).

To see this, let $t_1 \geqslant t_2 > 0$. By Jensen's inequality we have for any $\boldsymbol{x}$ and $\boldsymbol{y}$ in the interior of the domain:

$$
\frac{t_2}{t_1}f(\boldsymbol{y}) + \left(1-\frac{t_2}{t_1}\right)f(\boldsymbol{x}) \geqslant f\left(\frac{t_2}{t_1}\boldsymbol{y} + \left(1-\frac{t_2}{t_1}\right)\boldsymbol{x}\right).
$$

Making the substitution $\boldsymbol{y} = \boldsymbol{x} + t_1 \boldsymbol{d}$ and rearranging the last equation yields:

$$
\frac{f(\boldsymbol{x}+t_1\boldsymbol{d}) - f(\boldsymbol{x})}{t_1} \geqslant \frac{f(\boldsymbol{x}+t_2\boldsymbol{d}) - f(\boldsymbol{x})}{t_2}.
$$

In other words, the function $t \mapsto (f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x}))/t$ is increasing for $t > 0$ and therefore the directional derivative satisfies:

$$
\lim_{t\downarrow 0} \frac{f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x})}{t} = \inf_{t>0} \frac{f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x})}{t}.
$$

Hence, to show existence it is enough to show that $(f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x}))/t$ is bounded from below.

Since $\boldsymbol{x}$ lies in the interior of the domain of $f$, we can choose $t$ small enough so that $\boldsymbol{x}+t\boldsymbol{d}$ also lies in the interior. Therefore, the convexity of $f$ implies that there exists a subgradient vector $\boldsymbol{v}$ such that $f(\boldsymbol{x}+t\boldsymbol{d}) \geqslant f(\boldsymbol{x}) + \boldsymbol{v}^\top(t\boldsymbol{d})$. In other words,

$$
\frac{f(\boldsymbol{x}+t\boldsymbol{d}) - f(\boldsymbol{x})}{t} \geqslant \boldsymbol{v}^\top \boldsymbol{d}
$$

provides a lower bound for all $t > 0$, and the directional derivative of $f$ at an interior $\boldsymbol{x}$ always exists (in any direction).

A function $f$ satisfying (B.16) with strict inequality is said to be **strictly convex**. It is said to be a (strictly) **concave function** if $-f$ is (strictly) convex. Assuming that $\mathcal{X}$ is an open set, convexity for $f \in C^1$ is equivalent to

$$
f(\boldsymbol{y}) \geqslant f(\boldsymbol{x}) + (\boldsymbol{y}-\boldsymbol{x})^\top \nabla f(\boldsymbol{x}) \quad \text{for all } \boldsymbol{x}, \boldsymbol{y} \in \mathcal{X}.
$$

Moreover, for $f \in C^2$ strict convexity is equivalent to the Hessian matrix being positive definite for all $\boldsymbol{x} \in \mathcal{X}$, and convexity is equivalent to the Hessian matrix being **positive semidefinite** for all $\boldsymbol{x}$; that is, $\boldsymbol{y}^\top(\nabla^2 f(\boldsymbol{x}))\boldsymbol{y} \geqslant 0$ for all $\boldsymbol{y}$ and $\boldsymbol{x}$. Recall that we write $\mathbf{H} \geq 0$ to indicate that a matrix $\mathbf{H}$ is positive semidefinite.

**Example B.7 (Convexity and Differentiability).** If $f$ is a continuously differentiable multivariate function, then $f$ is convex if and only if the univariate function

$$
g(t) := f(\boldsymbol{x}+t\boldsymbol{d}), \quad t \in [0,1]
$$

is a convex function for any $\boldsymbol{x}$ and $\boldsymbol{x}+\boldsymbol{d}$ in the interior of the domain of $f$. This property provides an alternative definition for convexity of a multivariate and differentiable function.

To see why it is true, first assume that $f$ is convex and $t_1, t_2 \in [0,1]$. Then, using the subgradient definition of convexity in (B.16), we have $f(\boldsymbol{a}) \geqslant f(\boldsymbol{b}) + (\boldsymbol{a}-\boldsymbol{b})^\top \boldsymbol{v}$ for some subgradient $\boldsymbol{v}$. Substituting with $\boldsymbol{a} = \boldsymbol{x}+t_1\boldsymbol{d}$ and $\boldsymbol{b} = \boldsymbol{x}+t_2\boldsymbol{d}$, we obtain

$$
g(t_1) \geqslant g(t_2) + (t_1-t_2)\boldsymbol{v}^\top\boldsymbol{d}
$$

for any two points $t_1, t_2 \in [0,1]$. Therefore, $g$ is convex, because we have identified the existence of a subgradient $\boldsymbol{v}^\top \boldsymbol{d}$ for each $t_2$.

Conversely, assume that $g$ is convex for $t \in [0,1]$. Since $f$ is differentiable, then so is $g$. Then, the convexity of $g$ implies that there is a subgradient $v$ at $0$ such that: $g(t) \geqslant g(0) + tv$ for all $t \in [0,1]$. Rearranging,

$$
v \geqslant \frac{g(t)-g(0)}{t},
$$

and taking the right limit as $t \downarrow 0$ we obtain $v \geqslant g'(0) = \boldsymbol{d}^\top \nabla f(\boldsymbol{x})$. Therefore,

$$
g(t) \geqslant g(0) + tv \geqslant g(0) + t\boldsymbol{d}^\top \nabla f(\boldsymbol{x})
$$

and substituting $t=1$ yields:

$$
f(\boldsymbol{x}+\boldsymbol{d}) \geqslant f(\boldsymbol{x}) + \boldsymbol{d}^\top \nabla f(\boldsymbol{x}),
$$

so that there exists a subgradient vector, namely $\nabla f(\boldsymbol{x})$, for each $\boldsymbol{x}$. Hence, $f$ is convex by the definition in (B.16).

An optimization program of the form (B.13) is said to be a **convex programming problem** if:

1. The objective $f$ is a **convex function**.
2. The inequality constraint functions $\{g_i\}$ are convex.
3. The equality constraint functions $\{h_i\}$ are **affine**, that is, of the form $\boldsymbol{a}_i^\top \boldsymbol{x} - b_i$. This is equivalent to both $h_i$ and $-h_i$ being convex for all $i$.

Table B.1 summarizes some commonly encountered problems, all of which are convex, with the exception of the quadratic programs with $\mathbf{A} \not\geq 0$.

**Table B.1: Some common classes of optimization problems.**

| Name | $f(\boldsymbol{x})$ | Constraints |
|---|---|---|
| Linear Program (LP) | $\boldsymbol{c}^\top \boldsymbol{x}$ | $\mathbf{A}\boldsymbol{x} = \boldsymbol{b}$ and $\boldsymbol{x} \geqslant \boldsymbol{0}$ |
| Inequality Form LP | $\boldsymbol{c}^\top \boldsymbol{x}$ | $\mathbf{A}\boldsymbol{x} \leqslant \boldsymbol{b}$ |
| Quadratic Program (QP) | $\tfrac{1}{2}\boldsymbol{x}^\top \mathbf{A}\boldsymbol{x} + \boldsymbol{b}^\top \boldsymbol{x}$ | $\mathbf{D}\boldsymbol{x} \leqslant \boldsymbol{d}$, $\mathbf{E}\boldsymbol{x} = \boldsymbol{e}$ |
| Convex QP | $\tfrac{1}{2}\boldsymbol{x}^\top \mathbf{A}\boldsymbol{x} + \boldsymbol{b}^\top \boldsymbol{x}$ | $\mathbf{D}\boldsymbol{x} \leqslant \boldsymbol{d}$, $\mathbf{E}\boldsymbol{x} = \boldsymbol{e}$ ($\mathbf{A} \geq 0$) |
| Convex Program | $f(\boldsymbol{x})$ convex | $\{g_i(\boldsymbol{x})\}$ convex, $\{h_i(\boldsymbol{x})\}$ of the form $\boldsymbol{a}_i^\top \boldsymbol{x} - b_i$ |

Recognizing convex optimization problems or those that can be transformed to convex optimization problems can be challenging. However, once formulated as convex optimization problems, these can be efficiently solved using subgradient [112], bundle [57], and cutting-plane methods [59].

## B.2.2 Lagrangian Method

The main components of the Lagrangian method are the Lagrange multipliers and the Lagrange function. The method was developed by Lagrange in 1797 for the optimization problem (B.13) with only equality constraints. In 1951 Kuhn and Tucker extended Lagrange's method to inequality constraints. Given an optimization problem (B.13) containing only equality constraints $h_i(\boldsymbol{x}) = 0$, $i=1,\dots,m$, the **Lagrange function** is defined as

$$
\mathcal{L}(\boldsymbol{x},\boldsymbol{\beta}) = f(\boldsymbol{x}) + \sum_{i=1}^m \beta_i h_i(\boldsymbol{x}),
$$

where the coefficients $\{\beta_i\}$ are called the **Lagrange multipliers**. A necessary condition for a point $\boldsymbol{x}^*$ to be a local minimizer of $f(\boldsymbol{x})$ subject to the equality constraints $h_i(\boldsymbol{x}) = 0$, $i=1,\dots,m$, is

$$
\nabla_x \mathcal{L}(\boldsymbol{x}^*,\boldsymbol{\beta}^*) = \boldsymbol{0},
$$
$$
\nabla_\beta \mathcal{L}(\boldsymbol{x}^*,\boldsymbol{\beta}^*) = \boldsymbol{0},
$$

for some value $\boldsymbol{\beta}^*$. The above conditions are also sufficient if $\mathcal{L}(\boldsymbol{x},\boldsymbol{\beta}^*)$ is a convex function of $\boldsymbol{x}$.

Given the original optimization problem (B.13), containing both the equality and inequality constraints, the **generalized Lagrange function**, or **Lagrangian**, is defined as

$$
\mathcal{L}(\boldsymbol{x},\boldsymbol{\alpha},\boldsymbol{\beta}) = f(\boldsymbol{x}) + \sum_{i=1}^k \alpha_i g_i(\boldsymbol{x}) + \sum_{i=1}^m \beta_i h_i(\boldsymbol{x}).
$$

> **Theorem B.2: Karush–Kuhn–Tucker (KKT) Conditions**
>
> A necessary condition for a point $\boldsymbol{x}^*$ to be a local minimizer of $f(\boldsymbol{x})$ in the optimization problem (B.13) is the existence of an $\boldsymbol{\alpha}^*$ and $\boldsymbol{\beta}^*$ such that
>
> $$
> \nabla_x \mathcal{L}(\boldsymbol{x}^*,\boldsymbol{\alpha}^*,\boldsymbol{\beta}^*) = \boldsymbol{0},
> $$
> $$
> \nabla_\beta \mathcal{L}(\boldsymbol{x}^*,\boldsymbol{\alpha}^*,\boldsymbol{\beta}^*) = \boldsymbol{0},
> $$
> $$
> g_i(\boldsymbol{x}^*) \leqslant 0, \quad i=1,\dots,k,
> $$
> $$
> \alpha_i^* \geqslant 0, \quad i=1,\dots,k,
> $$
> $$
> \alpha_i^* g_i(\boldsymbol{x}^*) = 0, \quad i=1,\dots,k.
> $$

For **convex** programs we have the following important results [18, 43]:

1. Every local solution $\boldsymbol{x}^*$ to a convex programming problem is a global solution and the set of global solutions is convex. If, in addition, the objective function is strictly convex, then any global solution is unique.
2. For a strictly convex programming problem with $C^1$ objective and constraint functions, the KKT conditions are necessary and sufficient for a unique global solution.

## B.2.3 Duality

The aim of duality is to provide an alternative formulation of an optimization problem which is often more computationally efficient or has some theoretical significance (see [43, Page 219]). The original problem (B.13) is referred to as the **primal** problem whereas the reformulated problem, based on Lagrange multipliers, is called the **dual** problem. Duality theory is most relevant to convex optimization problems. It is well known that if the primal optimization problem is (strictly) convex then the dual problem is (strictly) concave and has a (unique) solution from which the (unique) optimal primal solution can be deduced.

The **Lagrange dual program** (also called the *Wolfe dual*) of the primal program (B.13), is:

$$
\begin{aligned}
\max_{\boldsymbol{\alpha},\boldsymbol{\beta}} \quad & \mathcal{L}^*(\boldsymbol{\alpha},\boldsymbol{\beta}) \\
\text{subject to:} \quad & \boldsymbol{\alpha} \geqslant \boldsymbol{0},
\end{aligned}
$$

where $\mathcal{L}^*$ is the **Lagrange dual function**:

$$
\mathcal{L}^*(\boldsymbol{\alpha},\boldsymbol{\beta}) = \inf_{\boldsymbol{x}\in\mathcal{X}} \mathcal{L}(\boldsymbol{x},\boldsymbol{\alpha},\boldsymbol{\beta}), \tag{B.17}
$$

giving the greatest lower bound (infimum) of $\mathcal{L}(\boldsymbol{x},\boldsymbol{\alpha},\boldsymbol{\beta})$ over all possible $\boldsymbol{x} \in \mathcal{X}$.

It is not difficult to see that if $f^*$ is the minimal value of the primal problem, then $\mathcal{L}^*(\boldsymbol{\alpha},\boldsymbol{\beta}) \leqslant f^*$ for any $\boldsymbol{\alpha} \geqslant \boldsymbol{0}$ and any $\boldsymbol{\beta}$. This property is called **weak duality**. The Lagrangian dual program thus determines the best lower bound on $f^*$. If $d^*$ is the optimal value for the dual problem then $d^* \leqslant f^*$. The difference $f^* - d^*$ is called the **duality gap**.

The duality gap is extremely useful for providing lower bounds for the solutions of primal problems that may be impossible to solve directly. It is important to note that for linearly constrained problems, if the primal is infeasible (does not have a solution satisfying the constraints), then the dual is either infeasible or unbounded. Conversely, if the dual is infeasible then the primal has no solution. Of crucial importance is the **strong duality** theorem, which states that for convex programs (B.13) with linear constrained functions $h_i$ and $g_i$ the duality gap is zero, and any $\boldsymbol{x}^*$ and $(\boldsymbol{\alpha}^*,\boldsymbol{\beta}^*)$ satisfying the KKT conditions are (global) solutions to the primal and dual programs, respectively. In particular, this holds for linear and convex quadratic programs (note that not all quadratic programs are convex).

For a convex primal program with $C^1$ objective and constraint functions, the Lagrangian dual function (B.17) can be obtained by simply setting the gradient (with respect to $\boldsymbol{x}$) of the Lagrangian $\mathcal{L}(\boldsymbol{x},\boldsymbol{\alpha},\boldsymbol{\beta})$ to zero. One can further simplify the dual program by substituting into the Lagrangian the relations between the variables thus obtained.

Further, for a convex primal problem, if there is a **strictly feasible** point $\widetilde{\boldsymbol{x}}$ (that is, a feasible point satisfying all of the inequality constraints with strict inequality), then the duality gap is zero, and strong duality holds. This is known as **Slater's condition** [18, Page 226].

The Lagrange dual problem is an important example of a **saddle-point problem** or **minimax** problem. In such problems the aim is to locate a point $(\boldsymbol{x}^*,\boldsymbol{y}^*) \in \mathcal{X}\times\mathcal{Y}$ that satisfies

$$
\sup_{\boldsymbol{y}\in\mathcal{Y}} \inf_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x},\boldsymbol{y}) = \inf_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x},\boldsymbol{y}^*) = f(\boldsymbol{x}^*,\boldsymbol{y}^*) = \sup_{\boldsymbol{y}\in\mathcal{Y}} f(\boldsymbol{x}^*,\boldsymbol{y}) = \inf_{\boldsymbol{x}\in\mathcal{X}} \sup_{\boldsymbol{y}\in\mathcal{Y}} f(\boldsymbol{x},\boldsymbol{y}).
$$

The equation

$$
\sup_{\boldsymbol{y}\in\mathcal{Y}} \inf_{\boldsymbol{x}\in\mathcal{X}} f(\boldsymbol{x},\boldsymbol{y}) = \inf_{\boldsymbol{x}\in\mathcal{X}} \sup_{\boldsymbol{y}\in\mathcal{Y}} f(\boldsymbol{x},\boldsymbol{y})
$$

is known as the **minimax equality**. Other problems that fall into this framework are zero-sum games in game theory; see also [24] for a number of combinatorial optimization problems that can be viewed as minimax problems.
