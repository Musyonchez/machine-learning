---
appendix: A
section: "A.4"
title: "Orthogonal Projections"
pdf_pages: "380-381"
---

# A.4 Orthogonal Projections

Let $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\}$ be a set of linearly independent vectors in $\mathbb{R}^n$. The set

$$\mathcal{V} = \operatorname{Span}\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\} = \{\alpha_1\boldsymbol{u}_1 + \cdots + \alpha_k\boldsymbol{u}_k,\ \alpha_1,\dots,\alpha_k \in \mathbb{R}\},$$

is called the *linear subspace spanned by* $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\}$. The *orthogonal complement* of $\mathcal{V}$, denoted by $\mathcal{V}^\perp$, is the set of all vectors $\boldsymbol{w}$ that are orthogonal to $\mathcal{V}$, in the sense that $\langle\boldsymbol{w},\boldsymbol{v}\rangle = 0$ for all $\boldsymbol{v} \in \mathcal{V}$. The matrix $\mathbf{P}$ such that $\mathbf{P}\boldsymbol{x} = \boldsymbol{x}$, for all $\boldsymbol{x} \in \mathcal{V}$, and $\mathbf{P}\boldsymbol{x} = \boldsymbol{0}$, for all $\boldsymbol{x} \in \mathcal{V}^\perp$ is called the *orthogonal projection matrix* onto $\mathcal{V}$. Suppose that $\mathbf{U} = [\boldsymbol{u}_1,\dots,\boldsymbol{u}_k]$ has full rank, in which case $\mathbf{U}^\top\mathbf{U}$ is an invertible matrix. The orthogonal projection matrix $\mathbf{P}$ onto $\mathcal{V} = \operatorname{Span}\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\}$ is then given by

$$\mathbf{P} = \mathbf{U}(\mathbf{U}^\top\mathbf{U})^{-1}\mathbf{U}^\top.$$

Namely, since $\mathbf{PU} = \mathbf{U}$, the matrix $\mathbf{P}$ projects any vector in $\mathcal{V}$ onto itself. Moreover, $\mathbf{P}$ projects any vector in $\mathcal{V}^\perp$ onto the zero vector. Using the pseudo-inverse, it is possible to specify the projection matrix also for the case where $\mathbf{U}$ is not of full rank, leading to the following theorem.

**Theorem A.4: Orthogonal Projection**

> Let $\mathbf{U} = [\boldsymbol{u}_1,\dots,\boldsymbol{u}_k]$. Then, the orthogonal projection matrix $\mathbf{P}$ onto $\mathcal{V} = \operatorname{Span}\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\}$ is given by
> $$\mathbf{P} = \mathbf{U}\mathbf{U}^+, \tag{A.7}$$
> where $\mathbf{U}^+$ is the (right) pseudo-inverse of $\mathbf{U}$.

*Proof:* By Property 1 of Definition A.2 we have $\mathbf{PU} = \mathbf{U}\mathbf{U}^+\mathbf{U} = \mathbf{U}$, so that $\mathbf{P}$ projects any vector in $\mathcal{V}$ onto itself. Moreover, $\mathbf{P}$ projects any vector in $\mathcal{V}^\perp$ onto the zero vector. $\square$

Note that in the special case where $\boldsymbol{u}_1,\dots,\boldsymbol{u}_k$ above form an orthonormal basis of $\mathcal{V}$, then the projection onto $\mathcal{V}$ is very simple to describe, namely we have

$$\mathbf{P}\boldsymbol{x} = \mathbf{U}\mathbf{U}^\top\boldsymbol{x} = \sum_{i=1}^k \langle\boldsymbol{x},\boldsymbol{u}_i\rangle\,\boldsymbol{u}_i. \tag{A.8}$$

For any point $\boldsymbol{x} \in \mathbb{R}^n$, the point in $\mathcal{V}$ that is closest to $\boldsymbol{x}$ is its orthogonal projection $\mathbf{P}\boldsymbol{x}$, as the following theorem shows.

**Theorem A.5: Orthogonal Projection and Minimal Distance**

> Let $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_k\}$ be an orthonormal basis of subspace $\mathcal{V}$ and let $\mathbf{P}$ be the orthogonal projection matrix onto $\mathcal{V}$. The solution to the minimization program
> $$\min_{\boldsymbol{y}\in\mathcal{V}} \|\boldsymbol{x}-\boldsymbol{y}\|^2$$
> is $\boldsymbol{y} = \mathbf{P}\boldsymbol{x}$. That is, $\mathbf{P}\boldsymbol{x} \in \mathcal{V}$ is closest to $\boldsymbol{x}$.

*Proof:* We can write each point $\boldsymbol{y} \in \mathcal{V}$ as $\boldsymbol{y} = \sum_{i=1}^k \alpha_i\boldsymbol{u}_i$. Consequently,

$$\|\boldsymbol{x}-\boldsymbol{y}\|^2 = \left\langle \boldsymbol{x} - \sum_{i=1}^k\alpha_i\boldsymbol{u}_i,\ \boldsymbol{x} - \sum_{i=1}^k\alpha_i\boldsymbol{u}_i \right\rangle = \|\boldsymbol{x}\|^2 - 2\sum_{i=1}^k \alpha_i\langle\boldsymbol{x},\boldsymbol{u}_i\rangle + \sum_{i=1}^k\alpha_i^2.$$

Minimizing this with respect to the $\{\alpha_i\}$ gives $\alpha_i = \langle\boldsymbol{x},\boldsymbol{u}_i\rangle, i = 1,\dots,k$. In view of (A.8), the optimal $\boldsymbol{y}$ is thus $\mathbf{P}\boldsymbol{x}$. $\square$
