---
appendix: A
section: "A.3"
title: "Complex Vectors and Matrices"
pdf_pages: "379-380"
---

# A.3 Complex Vectors and Matrices

Instead of the vector space $\mathbb{R}^n$ of $n$-dimensional real vectors, it is sometimes useful to consider the vector space $\mathbb{C}^n$ of $n$-dimensional complex vectors. In this case the *adjoint* or *conjugate transpose* operation ($*$) replaces the transpose operation ($\top$). This involves the usual transposition of the matrix or vector with the additional step that any complex number $z = x + \mathrm{i}\,y$ is replaced by its complex conjugate $\bar z = x - \mathrm{i}\,y$. For example, if

$$\boldsymbol{x} = \begin{bmatrix}a_1 + \mathrm{i}\,b_1\\ a_2 + \mathrm{i}\,b_2\end{bmatrix} \quad \text{and} \quad \mathbf{A} = \begin{bmatrix}a_{11}+\mathrm{i}\,b_{11} & a_{12}+\mathrm{i}\,b_{12}\\ a_{21}+\mathrm{i}\,b_{21} & a_{22}+\mathrm{i}\,b_{22}\end{bmatrix},$$

then

$$\boldsymbol{x}^* = [a_1 - \mathrm{i}\,b_1,\ a_2 - \mathrm{i}\,b_2] \quad \text{and} \quad \mathbf{A}^* = \begin{bmatrix}a_{11}-\mathrm{i}\,b_{11} & a_{21}-\mathrm{i}\,b_{21}\\ a_{12}-\mathrm{i}\,b_{12} & a_{22}-\mathrm{i}\,b_{22}\end{bmatrix}.$$

The (Euclidean) inner product of $\boldsymbol{x}$ and $\boldsymbol{y}$ (viewed as column vectors) is now defined as

$$\langle\boldsymbol{x},\boldsymbol{y}\rangle = \boldsymbol{y}^*\boldsymbol{x} = \sum_{i=1}^n x_i\,\overline{y_i},$$

which is no longer symmetric: $\langle\boldsymbol{x},\boldsymbol{y}\rangle = \overline{\langle\boldsymbol{y},\boldsymbol{x}\rangle}$. Note that this generalizes the real-valued inner product. The determinant of a complex matrix $\mathbf{A}$ is defined exactly as in (A.3). As a consequence, $\det(\mathbf{A}^*) = \overline{\det(\mathbf{A})}$.

A complex matrix is said to be *Hermitian* or *self-adjoint* if $\mathbf{A}^* = \mathbf{A}$, and *unitary* if $\mathbf{A}^*\mathbf{A} = \mathbf{I}$ (that is, if $\mathbf{A}^* = \mathbf{A}^{-1}$). For real matrices "Hermitian" is the same as "symmetric", and "unitary" is the same as "orthogonal".
