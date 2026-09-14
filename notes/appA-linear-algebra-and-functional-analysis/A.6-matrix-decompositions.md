---
appendix: A
section: "A.6"
title: "Matrix Decompositions"
pdf_pages: "386-402"
---

# A.6 Matrix Decompositions

Matrix decompositions are frequently used in linear algebra to simplify proofs, avoid numerical instability, and to speed up computations. We mention three important matrix decompositions: (P)LU, QR, and SVD.

## A.6.1 (P)LU Decomposition

Every invertible matrix $\mathbf{A}$ can be written as the product of three matrices:

$$\mathbf{A} = \mathbf{PLU}, \tag{A.9}$$

where $\mathbf{L}$ is a lower triangular matrix, $\mathbf{U}$ an upper triangular matrix, and $\mathbf{P}$ a *permutation matrix*. A permutation matrix is a square matrix with a single 1 in each row and column, and zeros otherwise. The matrix product $\mathbf{PB}$ simply permutes the rows of a matrix $\mathbf{B}$ and, likewise, $\mathbf{BP}$ permutes its columns. A decomposition of the form (A.9) is called a *PLU decomposition*. As a permutation matrix is orthogonal, its transpose is equal to its inverse, and so we can write (A.9) as

$$\mathbf{P}^\top\mathbf{A} = \mathbf{LU}.$$

The decomposition is not unique, and in many cases $\mathbf{P}$ can be taken to be the identity matrix, in which case we speak of the *LU decomposition* of $\mathbf{A}$, also called the LR for left–right (triangular) decomposition.

A PLU decomposition of an invertible $n\times n$ matrix $\mathbf{A}_0$ can be obtained recursively as follows. The first step is to swap the rows of $\mathbf{A}_0$ such that the element in the first column and first row of the pivoted matrix is as large as possible in absolute value. Write the resulting matrix as

$$\widetilde{\mathbf{P}}_0\mathbf{A}_0 = \begin{bmatrix}a_1 & \boldsymbol{b}_1^\top\\ \boldsymbol{c}_1 & \mathbf{D}_1\end{bmatrix},$$

where $\widetilde{\mathbf{P}}_0$ is the permutation matrix that swaps the first and $k$-th row, where $k$ is the row that contains the largest element in the first column. Next, add the matrix $-\boldsymbol{c}_1[1, \boldsymbol{b}_1^\top/a_1]$ to the last $n-1$ rows of $\widetilde{\mathbf{P}}_0\mathbf{A}_0$, to obtain the matrix

$$\begin{bmatrix}a_1 & \boldsymbol{b}_1^\top\\ \mathbf{0} & \mathbf{D}_1 - \boldsymbol{c}_1\boldsymbol{b}_1^\top/a_1\end{bmatrix} =: \begin{bmatrix}a_1 & \boldsymbol{b}_1^\top\\ \mathbf{0} & \mathbf{A}_1\end{bmatrix}.$$

In effect, we add some multiple of the first row to each of the remaining rows in order to obtain zeros in the first column, except for the first element.

We now apply the same procedure to $\mathbf{A}_1$ as we did to $\mathbf{A}_0$ and then to subsequent smaller matrices $\mathbf{A}_2,\dots,\mathbf{A}_{n-1}$:

1. Swap the first row with the row having the maximal absolute value element in the first column.
2. Make every other element in the first column equal to 0 by adding appropriate multiples of the first row to the other rows.

Suppose that $\mathbf{A}_t$ has a PLU decomposition $\mathbf{P}_t\mathbf{L}_t\mathbf{U}_t$. Then it is easy to check that

$$\underbrace{\widetilde{\mathbf{P}}_{t-1}^\top\begin{bmatrix}1 & \mathbf{0}^\top\\ \mathbf{0} & \mathbf{P}_t\end{bmatrix}}_{\mathbf{P}_{t-1}}\ \underbrace{\begin{bmatrix}1 & \mathbf{0}^\top\\ \mathbf{P}_t^\top\boldsymbol{c}_t/a_t & \mathbf{L}_t\end{bmatrix}}_{\mathbf{L}_{t-1}}\ \underbrace{\begin{bmatrix}a_t & \boldsymbol{b}_t^\top\\ \mathbf{0} & \mathbf{U}_t\end{bmatrix}}_{\mathbf{U}_{t-1}} \tag{A.10}$$

is a PLU decomposition of $\mathbf{A}_{t-1}$. Since the PLU decomposition for the scalar $\mathbf{A}_{n-1}$ is trivial, by working backwards we obtain a PLU decomposition $\mathbf{P}_0\mathbf{L}_0\mathbf{U}_0$ of $\mathbf{A}$.

**Example A.6 (PLU Decomposition)** Take

$$\mathbf{A} = \begin{bmatrix}0 & -1 & 7\\ 3 & 2 & 0\\ 1 & 1 & 1\end{bmatrix}.$$

Our goal is to modify $\mathbf{A}$ via Steps 1 and 2 above so as to obtain an upper triangular matrix with maximal elements on the diagonal. We first swap the first and second row. Next, we add $-1/3$ times the first row to the third row and $1/3$ times the second row to the third row:

$$\begin{bmatrix}0 & -1 & 7\\3 & 2 & 0\\1 & 1 & 1\end{bmatrix} \longrightarrow \begin{bmatrix}3 & 2 & 0\\0 & -1 & 7\\1 & 1 & 1\end{bmatrix} \longrightarrow \begin{bmatrix}3 & 2 & 0\\0 & -1 & 7\\0 & 1/3 & 1\end{bmatrix} \longrightarrow \begin{bmatrix}3 & 2 & 0\\0 & -1 & 7\\0 & 0 & 10/3\end{bmatrix}.$$

The final matrix is $\mathbf{U}_0$, and in the process we have applied the permutation matrices

$$\widetilde{\mathbf{P}}_0 = \begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix}, \quad \widetilde{\mathbf{P}}_1 = \begin{bmatrix}1&0\\0&1\end{bmatrix}.$$

Using the recursion (A.10) we can now recover $\mathbf{P}_0$ and $\mathbf{L}_0$. Namely, at the final iteration we have $\mathbf{P}_2 = 1, \mathbf{L}_2 = 1$, and $\mathbf{U}_2 = 10/3$. And subsequently,

$$\mathbf{P}_1 = \begin{bmatrix}1&0\\0&1\end{bmatrix}, \quad \mathbf{L}_1 = \begin{bmatrix}1&0\\-1/3&1\end{bmatrix}, \quad \mathbf{P}_0 = \begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix}, \quad \mathbf{L}_0 = \begin{bmatrix}1&0&0\\0&1&0\\1/3&-1/3&1\end{bmatrix},$$

observing that $a_1 = 3, \boldsymbol{c}_1 = [0,1]^\top, a_2 = -1$, and $\boldsymbol{c}_2 = 1/3$. $\blacksquare$

PLU decompositions can be used to solve large systems of linear equations of the form $\mathbf{A}\boldsymbol{x} = \boldsymbol{b}$ efficiently, especially when such an equation has to be solved for many different $\boldsymbol{b}$. This is done by first decomposing $\mathbf{A}$ into $\mathbf{PLU}$, and then solving two triangular systems:

1. $\mathbf{L}\boldsymbol{y} = \mathbf{P}^\top\boldsymbol{b}$.
2. $\mathbf{U}\boldsymbol{x} = \boldsymbol{y}$.

The first equation can be solved efficiently via *forward substitution*, and the second via *backward substitution*, as illustrated in the following example.

**Example A.7 (Solving Linear Equations with an LU Decomposition)** Let $\mathbf{A} = \mathbf{PLU}$ be the same as in Example A.6. We wish to solve $\mathbf{A}\boldsymbol{x} = [1,2,3]^\top$. First, solving

$$\begin{bmatrix}1&0&0\\0&1&0\\1/3&-1/3&1\end{bmatrix}\begin{bmatrix}y_1\\y_2\\y_3\end{bmatrix} = \begin{bmatrix}2\\1\\3\end{bmatrix}$$

gives, $y_1=2, y_2=1$ and $y_3 = 3-2/3+1/3 = 8/3$, by forward substitution. Next,

$$\begin{bmatrix}3&2&0\\0&-1&7\\0&0&10/3\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix} = \begin{bmatrix}2\\1\\8/3\end{bmatrix}$$

gives $x_3 = 4/5, x_2 = -1+28/5 = 23/5$, and $x_1 = 2(1-23/5)/3 = -12/5$, so $\boldsymbol{x} = [-12,23,4]^\top/5$. $\blacksquare$

## A.6.2 Woodbury Identity

LU (or more generally PLU) decompositions can also be applied to block matrices. A starting point is the following LU decomposition for a general $2\times 2$ matrix:

$$\begin{bmatrix}a&b\\c&d\end{bmatrix} = \begin{bmatrix}a&0\\c&d-bc/a\end{bmatrix}\begin{bmatrix}1&b/a\\0&1\end{bmatrix},$$

which holds as long as $a \ne 0$; this can be seen by simply writing out the matrix product. The block matrix generalization for matrices $\mathbf{A} \in \mathbb{R}^{n\times n}, \mathbf{B}\in\mathbb{R}^{n\times k}, \mathbf{C}\in\mathbb{R}^{k\times n}, \mathbf{D}\in\mathbb{R}^{k\times k}$ is

$$\boldsymbol{\Sigma} := \begin{bmatrix}\mathbf{A}&\mathbf{B}\\\mathbf{C}&\mathbf{D}\end{bmatrix} = \begin{bmatrix}\mathbf{A}&\mathbf{O}_{n\times k}\\\mathbf{C}&\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B}\end{bmatrix}\begin{bmatrix}\mathbf{I}_n&\mathbf{A}^{-1}\mathbf{B}\\\mathbf{O}_{k\times n}&\mathbf{I}_k\end{bmatrix}, \tag{A.11}$$

provided that $\mathbf{A}$ is invertible (again, write out the block matrix product). Here, we use the notation $\mathbf{O}_{p\times q}$ to denote the $p\times q$ matrix of zeros. We can further rewrite this as:

$$\boldsymbol{\Sigma} = \begin{bmatrix}\mathbf{I}_n&\mathbf{O}_{n\times k}\\\mathbf{CA}^{-1}&\mathbf{I}_k\end{bmatrix}\begin{bmatrix}\mathbf{A}&\mathbf{O}_{n\times k}\\\mathbf{O}_{k\times n}&\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B}\end{bmatrix}\begin{bmatrix}\mathbf{I}_n&\mathbf{A}^{-1}\mathbf{B}\\\mathbf{O}_{k\times n}&\mathbf{I}_k\end{bmatrix}.$$

Thus, inverting both sides, we obtain

$$\boldsymbol{\Sigma}^{-1} = \begin{bmatrix}\mathbf{I}_n&\mathbf{A}^{-1}\mathbf{B}\\\mathbf{O}_{k\times n}&\mathbf{I}_k\end{bmatrix}^{-1}\begin{bmatrix}\mathbf{A}&\mathbf{O}_{n\times k}\\\mathbf{O}_{k\times n}&\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B}\end{bmatrix}^{-1}\begin{bmatrix}\mathbf{I}_n&\mathbf{O}_{n\times k}\\\mathbf{CA}^{-1}&\mathbf{I}_k\end{bmatrix}^{-1}.$$

Inversion of the above block matrices gives (again write out)

$$\boldsymbol{\Sigma}^{-1} = \begin{bmatrix}\mathbf{I}_n&-\mathbf{A}^{-1}\mathbf{B}\\\mathbf{O}_{k\times n}&\mathbf{I}_k\end{bmatrix}\begin{bmatrix}\mathbf{A}^{-1}&\mathbf{O}_{n\times k}\\\mathbf{O}_{k\times n}&(\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B})^{-1}\end{bmatrix}\begin{bmatrix}\mathbf{I}_n&\mathbf{O}_{n\times k}\\-\mathbf{CA}^{-1}&\mathbf{I}_k\end{bmatrix}. \tag{A.12}$$

Assuming that $\mathbf{D}$ is invertible, we could also perform a block UL (as opposed to LU) decomposition:

$$\boldsymbol{\Sigma} = \begin{bmatrix}\mathbf{A}-\mathbf{BD}^{-1}\mathbf{C}&\mathbf{B}\\\mathbf{O}_{k\times n}&\mathbf{D}\end{bmatrix}\begin{bmatrix}\mathbf{I}_n&\mathbf{O}_{n\times k}\\\mathbf{D}^{-1}\mathbf{C}&\mathbf{I}_k\end{bmatrix}, \tag{A.13}$$

which, after a similar calculation as the one above, yields

$$\boldsymbol{\Sigma}^{-1} = \begin{bmatrix}\mathbf{I}_n&\mathbf{O}_{n\times k}\\-\mathbf{D}^{-1}\mathbf{C}&\mathbf{I}_k\end{bmatrix}\begin{bmatrix}(\mathbf{A}-\mathbf{BD}^{-1}\mathbf{C})^{-1}&\mathbf{O}_{n\times k}\\\mathbf{O}_{k\times n}&\mathbf{D}^{-1}\end{bmatrix}\begin{bmatrix}\mathbf{I}_n&-\mathbf{BD}^{-1}\\\mathbf{O}_{k\times n}&\mathbf{I}_k\end{bmatrix}. \tag{A.14}$$

The upper-left block of $\boldsymbol{\Sigma}^{-1}$ from (A.14) must be the same as the upper-left block of $\boldsymbol{\Sigma}^{-1}$ from (A.12), leading to the *Woodbury identity*:

$$(\mathbf{A}-\mathbf{BD}^{-1}\mathbf{C})^{-1} = \mathbf{A}^{-1} + \mathbf{A}^{-1}\mathbf{B}(\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B})^{-1}\mathbf{CA}^{-1}. \tag{A.15}$$

From (A.11) and the fact that the determinant of a product is the product of the determinants, we see that $\det(\boldsymbol{\Sigma}) = \det(\mathbf{A})\det(\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B})$. Similarly, from (A.13) we have $\det(\boldsymbol{\Sigma}) = \det(\mathbf{A}-\mathbf{BD}^{-1}\mathbf{C})\det(\mathbf{D})$, leading to the identity

$$\det(\mathbf{A}-\mathbf{BD}^{-1}\mathbf{C})\det(\mathbf{D}) = \det(\mathbf{A})\det(\mathbf{D}-\mathbf{CA}^{-1}\mathbf{B}). \tag{A.16}$$

The following special cases of (A.16) and (A.15) are of particular importance.

**Theorem A.10: Sherman–Morrison Formula**

> Suppose that $\mathbf{A} \in \mathbb{R}^{n\times n}$ is invertible and $\boldsymbol{x},\boldsymbol{y} \in \mathbb{R}^n$. Then,
> $$\det(\mathbf{A}+\boldsymbol{x}\boldsymbol{y}^\top) = \det(\mathbf{A})(1+\boldsymbol{y}^\top\mathbf{A}^{-1}\boldsymbol{x}).$$
> If in addition $\boldsymbol{y}^\top\mathbf{A}^{-1}\boldsymbol{x} \ne -1$, then the *Sherman–Morrison formula* holds:
> $$(\mathbf{A}+\boldsymbol{x}\boldsymbol{y}^\top)^{-1} = \mathbf{A}^{-1} - \frac{\mathbf{A}^{-1}\boldsymbol{x}\boldsymbol{y}^\top\mathbf{A}^{-1}}{1+\boldsymbol{y}^\top\mathbf{A}^{-1}\boldsymbol{x}}.$$

*Proof:* Take $\mathbf{B}=\boldsymbol{x}, \mathbf{C}=-\boldsymbol{y}^\top$, and $\mathbf{D}=1$ in (A.16) and (A.15). $\square$

One important application of the Sherman–Morrison formula is in the efficient solution of the linear system $\mathbf{A}\boldsymbol{x} = \boldsymbol{b}$, where $\mathbf{A}$ is an $n\times n$ matrix of the form:

$$\mathbf{A} = \mathbf{A}_0 + \sum_{j=1}^p \boldsymbol{a}_j\boldsymbol{a}_j^\top$$

for some column vectors $\boldsymbol{a}_1,\dots,\boldsymbol{a}_p \in \mathbb{R}^n$ and $n\times n$ diagonal (or otherwise easily invertible) matrix $\mathbf{A}_0$. Such linear systems arise, for example, in the context of *ridge regression* (book p. 217) and optimization (book p. 414).

To see how the Sherman–Morrison formula can be exploited, define the matrices $\mathbf{A}_0,\dots,\mathbf{A}_p$ via the recursion:

$$\mathbf{A}_k = \mathbf{A}_{k-1} + \boldsymbol{a}_k\boldsymbol{a}_k^\top, \quad k=1,\dots,p.$$

Application of Theorem A.10 for $k=1,\dots,p$ yields the identities:[^3]

$$\mathbf{A}_k^{-1} = \mathbf{A}_{k-1}^{-1} - \frac{\mathbf{A}_{k-1}^{-1}\boldsymbol{a}_k\boldsymbol{a}_k^\top\mathbf{A}_{k-1}^{-1}}{1+\boldsymbol{a}_k^\top\mathbf{A}_{k-1}^{-1}\boldsymbol{a}_k}$$

$$|\mathbf{A}_k| = |\mathbf{A}_{k-1}| \times \left(1 + \boldsymbol{a}_k^\top\mathbf{A}_{k-1}^{-1}\boldsymbol{a}_k\right).$$

[^3]: Here $|\mathbf{A}|$ is a shorthand notation for $\det(\mathbf{A})$.

Therefore, by evolving the recursive relationships up until $k=p$, we obtain:

$$\mathbf{A}_p^{-1} = \mathbf{A}_0^{-1} - \sum_{j=1}^p \frac{\mathbf{A}_{j-1}^{-1}\boldsymbol{a}_j\boldsymbol{a}_j^\top\mathbf{A}_{j-1}^{-1}}{1+\boldsymbol{a}_j^\top\mathbf{A}_{j-1}^{-1}\boldsymbol{a}_j}$$

$$|\mathbf{A}_p| = |\mathbf{A}_0| \times \prod_{j=1}^p\left(1+\boldsymbol{a}_j^\top\mathbf{A}_{j-1}^{-1}\boldsymbol{a}_j\right).$$

These expressions will allow us to easily compute $\mathbf{A}^{-1} = \mathbf{A}_p^{-1}$ and $|\mathbf{A}| = |\mathbf{A}_p|$ provided the following quantities are available:

$$\boldsymbol{c}_{k,j} := \mathbf{A}_{k-1}^{-1}\boldsymbol{a}_j, \quad k=1,\dots,p-1,\quad j=k+1,\dots,p.$$

Since, by Theorem A.10, we can write:

$$\mathbf{A}_{k-1}^{-1}\boldsymbol{a}_j = \mathbf{A}_{k-2}^{-1}\boldsymbol{a}_j - \frac{\mathbf{A}_{k-2}^{-1}\boldsymbol{a}_{k-1}\boldsymbol{a}_{k-1}^\top\mathbf{A}_{k-2}^{-1}}{1+\boldsymbol{a}_{k-1}^\top\mathbf{A}_{k-2}^{-1}\boldsymbol{a}_{k-1}}\boldsymbol{a}_j,$$

the quantities $\{\boldsymbol{c}_{k,j}\}$ can be computed from the recursion:

$$\boldsymbol{c}_{1,j} = \mathbf{A}_0^{-1}\boldsymbol{a}_j, \quad j=1,\dots,p$$
$$\boldsymbol{c}_{k,j} = \boldsymbol{c}_{k-1,j} - \frac{\boldsymbol{a}_{k-1}^\top\boldsymbol{c}_{1,j}}{1+\boldsymbol{a}_{k-1}^\top\boldsymbol{c}_{k-1,k-1}}\boldsymbol{c}_{k-1,k-1}, \quad k=2,\dots,p,\quad j=k,\dots,p. \tag{A.17}$$

Observe that this recursive computation takes $O(p^2n)$ time and that once $\{\boldsymbol{c}_{k,j}\}$ are available, we can express $\mathbf{A}^{-1}$ and $|\mathbf{A}|$ as:

$$\mathbf{A}^{-1} = \mathbf{A}_0^{-1} - \sum_{j=1}^p \frac{\boldsymbol{c}_{j,j}\boldsymbol{c}_{j,j}^\top}{1+\boldsymbol{a}_j^\top\boldsymbol{c}_{j,j}}$$

$$|\mathbf{A}| = |\mathbf{A}_0| \times \prod_{j=1}^p\left(1+\boldsymbol{a}_j^\top\boldsymbol{c}_{j,j}\right).$$

In summary, we have proved the following.

**Theorem A.11: Sherman–Morrison Recursion**

> The inverse and determinant of the $n\times n$ matrix $\mathbf{A} = \mathbf{A}_0 + \sum_{k=1}^p \boldsymbol{a}_k\boldsymbol{a}_k^\top$ are given respectively by:
> $$\mathbf{A}^{-1} = \mathbf{A}_0^{-1} - \mathbf{CD}^{-1}\mathbf{C}^\top$$
> $$\det(\mathbf{A}) = \det(\mathbf{A}_0)\det(\mathbf{D}),$$
> where $\mathbf{C} \in \mathbb{R}^{n\times p}$ and $\mathbf{D} \in \mathbb{R}^{p\times p}$ are the matrices
> $$\mathbf{C} := [\boldsymbol{c}_{1,1},\dots,\boldsymbol{c}_{p,p}], \quad \mathbf{D} := \operatorname{diag}\left(1+\boldsymbol{a}_1^\top\boldsymbol{c}_{1,1},\ \cdots,\ 1+\boldsymbol{a}_p^\top\boldsymbol{c}_{p,p}\right),$$
> and all the $\{\boldsymbol{c}_{j,k}\}$ are computed from the recursion (A.17) in $O(p^2n)$ time.

As a consequence of Theorem A.11, the solution to the linear system $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$ can be computed in $O(p^2n)$ time via:

$$\boldsymbol{x} = \mathbf{A}_0^{-1}\boldsymbol{b} - \mathbf{CD}^{-1}[\mathbf{C}^\top\boldsymbol{b}].$$

If $n > p$, the Sherman–Morrison recursion can frequently be much faster than the $O(n^3)$ direct solution via the LU decomposition method in Section A.6.1 (book p. 368).

In summary, the following algorithm computes the matrices $\mathbf{C}$ and $\mathbf{D}$ in Theorem A.11 via the recursion (A.17).

**Algorithm A.6.1: Sherman–Morrison Recursion**

```
input: Easily invertible matrix A0 and column vectors a1, ..., ap.
output: Matrices C and D such that C D^-1 C^T = A0^-1 - (A0 + sum_j aj aj^T)^-1.
1  ck <- A0^-1 ak for k = 1, ..., p (assuming A0 is diagonal or easily invertible matrix)
2  for k = 1, ..., p-1 do
3  |   dk <- 1 + ak^T ck
4  |   for j = k+1, ..., p do
5  |   |   cj <- cj - (ak^T cj / dk) ck
6  dp <- 1 + ap^T cp
7  C <- [c1, ..., cp]
8  D <- diag(d1, ..., dp)
9  return C and D
```

Finally, note that if $\mathbf{A}_0$ is a diagonal matrix and we only store the diagonal elements of $\mathbf{D}$ and $\mathbf{A}_0$ (as opposed to storing the full matrices $\mathbf{D}$ and $\mathbf{A}_0$), then the storage or memory requirements of Algorithm A.6.1 are only $O(p\,n)$.

## A.6.3 Cholesky Decomposition

If $\mathbf{A}$ is a real-valued positive definite matrix (and therefore symmetric), e.g., a covariance matrix, then an LU decomposition can be achieved with matrices $\mathbf{L}$ and $\mathbf{U} = \mathbf{L}^\top$.

**Theorem A.12: Cholesky Decomposition**

> A real-valued positive definite matrix $\mathbf{A} = [a_{ij}] \in \mathbb{R}^{n\times n}$ can be decomposed as
> $$\mathbf{A} = \mathbf{LL}^\top,$$
> where the real $n\times n$ lower triangular matrix $\mathbf{L} = [l_{kj}]$ satisfies the recursive formula
> $$l_{kj} = \frac{a_{kj} - \sum_{i=1}^{j-1} l_{ji}l_{ki}}{\sqrt{a_{jj} - \sum_{i=1}^{j-1} l_{ji}^2}}, \quad \text{where } \sum_{i=1}^0 l_{ji}l_{ki} := 0 \tag{A.18}$$
> for $k=1,\dots,n$ and $j = 1,\dots,k$.

*Proof:* The proof is by inductive construction. For $k=1,\dots,n$, let $\mathbf{A}_k$ be the left-upper $k\times k$ submatrix of $\mathbf{A} = \mathbf{A}_n$. With $\boldsymbol{e}_1 := [1,0,\dots,0]^\top$, we have $\mathbf{A}_1 = a_{11} = \boldsymbol{e}_1^\top\mathbf{A}\boldsymbol{e}_1 > 0$ by the positive-definiteness of $\mathbf{A}$. It follows that $l_{11} = \sqrt{a_{11}}$. Suppose that $\mathbf{A}_{k-1}$ has a Cholesky factorization $\mathbf{L}_{k-1}\mathbf{L}_{k-1}^\top$ with $\mathbf{L}_{k-1}$ having strictly positive diagonal elements, we can construct a Cholesky factorization of $\mathbf{A}_k$ as follows. First write

$$\mathbf{A}_k = \begin{bmatrix}\mathbf{L}_{k-1}\mathbf{L}_{k-1}^\top & \boldsymbol{a}_{k-1}\\ \boldsymbol{a}_{k-1}^\top & a_{kk}\end{bmatrix}$$

and propose $\mathbf{L}_k$ to be of the form

$$\mathbf{L}_k = \begin{bmatrix}\mathbf{L}_{k-1} & \mathbf{0}\\ \boldsymbol{l}_{k-1}^\top & l_{kk}\end{bmatrix}$$

for some vector $\boldsymbol{l}_{k-1} \in \mathbb{R}^{k-1}$ and scalar $l_{kk}$, for which it must hold that

$$\begin{bmatrix}\mathbf{L}_{k-1}\mathbf{L}_{k-1}^\top & \boldsymbol{a}_{k-1}\\ \boldsymbol{a}_{k-1}^\top & a_{kk}\end{bmatrix} = \begin{bmatrix}\mathbf{L}_{k-1} & \mathbf{0}\\ \boldsymbol{l}_{k-1}^\top & l_{kk}\end{bmatrix}\begin{bmatrix}\mathbf{L}_{k-1}^\top & \boldsymbol{l}_{k-1}\\ \mathbf{0}^\top & l_{kk}\end{bmatrix}.$$

To establish that such an $\boldsymbol{l}_{k-1}$ and $l_{kk}$ exist, we must verify that the set of equations

$$\mathbf{L}_{k-1}\boldsymbol{l}_{k-1} = \boldsymbol{a}_{k-1}$$
$$\boldsymbol{l}_{k-1}^\top\boldsymbol{l}_{k-1} + l_{kk}^2 = a_{kk} \tag{A.19}$$

has a solution. The system $\mathbf{L}_{k-1}\boldsymbol{l}_{k-1} = \boldsymbol{a}_{k-1}$ has a unique solution, because (by assumption) $\mathbf{L}_{k-1}$ is lower diagonal with strictly positive entries down the main diagonal and we can solve for $\boldsymbol{l}_{k-1}$ using forward substitution: $\boldsymbol{l}_{k-1} = \mathbf{L}_{k-1}^{-1}\boldsymbol{a}_{k-1}$. We can solve the second equation as $l_{kk} = \sqrt{a_{kk}-\|\boldsymbol{l}_{k-1}\|^2}$, provided that the term within the square root is positive. We demonstrate this using the fact that $\mathbf{A}$ is a positive definite matrix. In particular, for $\boldsymbol{x} \in \mathbb{R}^n$ of the form $[\boldsymbol{x}_1^\top, x_2, \mathbf{0}^\top]^\top$, where $\boldsymbol{x}_1$ is a non-zero $(k-1)$-dimensional vector and $x_2$ a non-zero number, we have

$$0 < \boldsymbol{x}^\top\mathbf{A}\boldsymbol{x} = [\boldsymbol{x}_1^\top,x_2]\begin{bmatrix}\mathbf{L}_{k-1}\mathbf{L}_{k-1}^\top & \boldsymbol{a}_{k-1}\\ \boldsymbol{a}_{k-1}^\top & a_{kk}\end{bmatrix}\begin{bmatrix}\boldsymbol{x}_1\\ x_2\end{bmatrix} = \|\mathbf{L}_{k-1}^\top\boldsymbol{x}_1\|^2 + 2\boldsymbol{x}_1^\top\boldsymbol{a}_{k-1}x_2 + a_{kk}x_2^2.$$

Now take $\boldsymbol{x}_1 = -x_2\mathbf{L}_{k-1}^{-\top}\boldsymbol{l}_{k-1}$ to obtain $0 < \boldsymbol{x}^\top\mathbf{A}\boldsymbol{x} = x_2^2(a_{kk}-\|\boldsymbol{l}_{k-1}\|^2)$. Therefore, (A.19) can be uniquely solved. As we have already solved it for $k=1$, we can solve it for any $k=1,\dots,n$, leading to the recursive formula (A.18) and Algorithm A.6.2 below. $\square$

An implementation of Cholesky's decomposition that uses the notation in the proof of Theorem A.6.3 is the following algorithm, whose running cost is $O(n^3)$.

**Algorithm A.6.2: Cholesky Decomposition**

```
input: Positive-definite n x n matrix An with entries {aij}.
output: Lower triangular Ln such that Ln Ln^T = An.
1  L1 <- sqrt(a11)
2  for k = 2, ..., n do
3  |   a_{k-1} <- [a1k, ..., a_{k-1,k}]^T
4  |   l_{k-1} <- L_{k-1}^{-1} a_{k-1}   (computed in O(k^2) time via forward substitution)
5  |   lkk <- sqrt(akk - l_{k-1}^T l_{k-1})
6  |   Lk <- [[L_{k-1}, 0], [l_{k-1}^T, lkk]]
7  return Ln
```

## A.6.4 QR Decomposition and the Gram–Schmidt Procedure

Let $\mathbf{A}$ be an $n\times p$ matrix, where $p \le n$. Then, there exists a matrix $\mathbf{Q} \in \mathbb{R}^{n\times p}$ satisfying $\mathbf{Q}^\top\mathbf{Q} = \mathbf{I}_p$, and an upper triangular matrix $\mathbf{R} \in \mathbb{R}^{p\times p}$, such that

$$\mathbf{A} = \mathbf{QR}.$$

This is the *QR decomposition* for real-valued matrices. When $\mathbf{A}$ has full column rank, such a decomposition can be obtained via the *Gram–Schmidt* procedure, which constructs an *orthonormal basis* $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_p\}$ of the column space of $\mathbf{A}$ spanned by $\{\boldsymbol{a}_1,\dots,\boldsymbol{a}_p\}$, in the following way (see also Figure A.5):

1. Take $\boldsymbol{u}_1 = \boldsymbol{a}_1/\|\boldsymbol{a}_1\|$.
2. Let $\boldsymbol{p}_1$ be the projection of $\boldsymbol{a}_2$ onto $\operatorname{Span}\{\boldsymbol{u}_1\}$. That is, $\boldsymbol{p}_1 = \langle\boldsymbol{u}_1,\boldsymbol{a}_2\rangle\boldsymbol{u}_1$. Now take $\boldsymbol{u}_2 = (\boldsymbol{a}_2-\boldsymbol{p}_1)/\|\boldsymbol{a}_2-\boldsymbol{p}_1\|$. This vector is perpendicular to $\boldsymbol{u}_1$ and has unit length.
3. Let $\boldsymbol{p}_2$ be the projection of $\boldsymbol{a}_3$ onto $\operatorname{Span}\{\boldsymbol{u}_1,\boldsymbol{u}_2\}$. That is, $\boldsymbol{p}_2 = \langle\boldsymbol{u}_1,\boldsymbol{a}_3\rangle\boldsymbol{u}_1 + \langle\boldsymbol{u}_2,\boldsymbol{a}_3\rangle\boldsymbol{u}_2$. Now take $\boldsymbol{u}_3 = (\boldsymbol{a}_3-\boldsymbol{p}_2)/\|\boldsymbol{a}_3-\boldsymbol{p}_2\|$. This vector is perpendicular to both $\boldsymbol{u}_1$ and $\boldsymbol{u}_2$ and has unit length.
4. Continue this process to obtain $\boldsymbol{u}_4,\dots,\boldsymbol{u}_p$.

> **Figure A.5:** Illustration of the Gram–Schmidt procedure in $\mathbb{R}^2$: $\boldsymbol{a}_1$ is normalized to $\boldsymbol{u}_1$; $\boldsymbol{a}_2$'s projection $\boldsymbol{p}_1$ onto $\boldsymbol{u}_1$ is subtracted off and the remainder $\boldsymbol{a}_2-\boldsymbol{p}_1$ is normalized to give $\boldsymbol{u}_2$, perpendicular to $\boldsymbol{u}_1$.

At the end of the procedure, a set $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_p\}$ of $p$ orthonormal vectors are obtained. Consequently, as a result of Theorem A.3,

$$\boldsymbol{a}_j = \sum_{i=1}^j \underbrace{\langle\boldsymbol{a}_j,\boldsymbol{u}_i\rangle}_{r_{ij}}\boldsymbol{u}_i, \quad j=1,\dots,p,$$

for some numbers $r_{ij}, j=1,\dots,i, i=1,\dots,p$. Denoting the corresponding upper triangular matrix $[r_{ij}]$ by $\mathbf{R}$, we have in matrix notation:

$$\mathbf{QR} = [\boldsymbol{u}_1,\dots,\boldsymbol{u}_p]\begin{bmatrix}r_{11}&r_{12}&r_{13}&\dots&r_{1p}\\0&r_{22}&r_{23}&\dots&r_{2p}\\\vdots&0&\ddots&\ddots&\vdots\\0&0&0&\dots&r_{pp}\end{bmatrix} = [\boldsymbol{a}_1,\dots,\boldsymbol{a}_p] = \mathbf{A},$$

which yields a QR decomposition. The QR decomposition can be used to efficiently solve least-squares problems; this will be shown shortly. It can also be used to calculate the determinant of the matrix $\mathbf{A}$, whenever $\mathbf{A}$ is square. Namely, $\det(\mathbf{A}) = \det(\mathbf{Q})\det(\mathbf{R}) = \det(\mathbf{R})$; and since $\mathbf{R}$ is triangular, its determinant is the product of its diagonal elements. There exist various improvements of the Gram–Schmidt process (for example, the *Householder transformation* [52]) that not only improve the numerical stability of the QR decomposition, but also can be applied even when $\mathbf{A}$ is not full rank.

An important application of the QR decomposition is found in solving the least-squares problem in $O(p^2n)$ time:

$$\min_{\boldsymbol{\beta}\in\mathbb{R}^p} \|\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}\|^2$$

for some $\mathbf{X} \in \mathbb{R}^{n\times p}$ (model) matrix. Using the defining properties of the pseudo-inverse in Definition A.2 (book p. 360), one can show that $\|\mathbf{X}\mathbf{X}^+\boldsymbol{y}-\boldsymbol{y}\|^2 \le \|\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}\|^2$ for any $\boldsymbol{\beta}$. In other words, $\widehat{\boldsymbol{\beta}} := \mathbf{X}^+\boldsymbol{y}$ minimizes $\|\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}\|$. If we have the QR decomposition $\mathbf{X} = \mathbf{QR}$, then a numerically stable way to calculate $\widehat{\boldsymbol{\beta}}$ with an $O(p^2n)$ cost is via

$$\widehat{\boldsymbol{\beta}} = (\mathbf{QR})^+\boldsymbol{y} = \mathbf{R}^+\mathbf{Q}^+\boldsymbol{y} = \mathbf{R}^+\mathbf{Q}^\top\boldsymbol{y}.$$

If $\mathbf{X}$ has full column rank, then $\mathbf{R}^+ = \mathbf{R}^{-1}$.

Note that while the QR decomposition is the method of choice for solving the ordinary least-squares regression problem (book p. 372), the *Sherman–Morrison recursion* is the method of choice for solving the regularized least-squares (or ridge) regression problem (book p. 217).

## A.6.5 Singular Value Decomposition

One of the most useful matrix decompositions is the *singular value decomposition* (SVD).

**Theorem A.13: Singular Value Decomposition**

> Any (complex) matrix $m\times n$ matrix $\mathbf{A}$ admits a unique decomposition
> $$\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^*,$$
> where $\mathbf{U}$ and $\mathbf{V}$ are unitary matrices of dimension $m$ and $n$, respectively, and $\boldsymbol{\Sigma}$ is a real $m\times n$ diagonal matrix. If $\mathbf{A}$ is real, then $\mathbf{U}$ and $\mathbf{V}$ are both orthogonal matrices.

*Proof:* Without loss of generality we can assume that $m \ge n$ (otherwise consider the transpose of $\mathbf{A}$). Then $\mathbf{A}^*\mathbf{A}$ is a positive semidefinite Hermitian matrix, because $\langle\mathbf{A}^*\mathbf{A}\boldsymbol{v},\boldsymbol{v}\rangle = \boldsymbol{v}^*\mathbf{A}^*\mathbf{A}\boldsymbol{v} = \|\mathbf{A}\boldsymbol{v}\|^2 \ge 0$ for all $\boldsymbol{v}$. Hence, $\mathbf{A}^*\mathbf{A}$ has non-negative real eigenvalues, $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n \ge 0$. By Theorem A.7 the matrix $\mathbf{V} = [\boldsymbol{v}_1,\dots,\boldsymbol{v}_n]$ of right-eigenvectors is a unitary matrix. Define the $i$-th *singular value* as $\sigma_i = \sqrt{\lambda_i}, i=1,\dots,n$ and suppose $\lambda_1,\dots,\lambda_r$ are all greater than 0, and $\lambda_{r+1},\dots,\lambda_n = 0$. In particular, $\mathbf{A}\boldsymbol{v}_i = \boldsymbol{0}$ for $i = r+1,\dots,n$. Let $\boldsymbol{u}_i = \mathbf{A}\boldsymbol{v}_i/\sigma_i, i=1,\dots,r$. Then, for $i,j \le r$,

$$\langle\boldsymbol{u}_i,\boldsymbol{u}_j\rangle = \boldsymbol{u}_j^*\boldsymbol{u}_i = \frac{\boldsymbol{v}_j^*\mathbf{A}^*\mathbf{A}\boldsymbol{v}_i}{\sigma_i\sigma_j} = \frac{\lambda_i\mathbb{1}\{i=j\}}{\sigma_i\sigma_j} = \mathbb{1}\{i=j\}.$$

We can extend $\boldsymbol{u}_1,\dots,\boldsymbol{u}_r$ to an orthonormal basis $\{\boldsymbol{u}_1,\dots,\boldsymbol{u}_m\}$ of $\mathbb{C}^m$ (e.g., using the Gram–Schmidt procedure). Let $\mathbf{U} = [\boldsymbol{u}_1,\dots,\boldsymbol{u}_n]$ be the corresponding unitary matrix. Defining $\boldsymbol{\Sigma}$ to be the $m\times n$ diagonal matrix with diagonal $(\sigma_1,\dots,\sigma_r,0,\dots,0)$, we have,

$$\mathbf{U}\boldsymbol{\Sigma} = [\mathbf{A}\boldsymbol{v}_1,\dots,\mathbf{A}\boldsymbol{v}_r,\mathbf{0},\dots,\mathbf{0}] = \mathbf{AV},$$

and hence $\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^*$. $\square$

Note that

$$\mathbf{AA}^* = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^*\mathbf{V}\boldsymbol{\Sigma}^\top\mathbf{U}^* = \mathbf{U}\boldsymbol{\Sigma}\boldsymbol{\Sigma}^\top\mathbf{U}^* \quad \text{and} \quad \mathbf{A}^*\mathbf{A} = \mathbf{V}\boldsymbol{\Sigma}^*\mathbf{U}^*\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^* = \mathbf{V}\boldsymbol{\Sigma}^\top\boldsymbol{\Sigma}\mathbf{V}^*.$$

So, $\mathbf{U}$ is a unitary matrix whose columns are eigenvectors of $\mathbf{AA}^*$ and $\mathbf{V}$ is a unitary matrix whose columns are eigenvectors of $\mathbf{A}^*\mathbf{A}$.

The SVD makes it possible to write the matrix $\mathbf{A}$ as a sum of rank-1 matrices, weighted by the singular values $\{\sigma_i\}$:

$$\mathbf{A} = [\boldsymbol{u}_1,\boldsymbol{u}_2,\dots,\boldsymbol{u}_m]\begin{bmatrix}\sigma_1&0&\dots&\dots&0\\0&\ddots&0&\dots&0\\0&\dots&\sigma_r&\dots&0\\0&\dots&\dots&0&0\\0&\dots&\dots&\dots&0\end{bmatrix}\begin{bmatrix}\boldsymbol{v}_1^*\\\boldsymbol{v}_2^*\\\vdots\\\boldsymbol{v}_n^*\end{bmatrix} = \sum_{i=1}^r \sigma_i\boldsymbol{u}_i\boldsymbol{v}_i^*, \tag{A.20}$$

which is called the *dyade* or *spectral representation* of $\mathbf{A}$.

For real-valued matrices, the SVD has a nice geometric interpretation, illustrated in Figure A.6. The linear mapping defined by matrix $\mathbf{A}$ can be thought of as a succession of three linear operations: (1) an orthogonal transformation (i.e., a rotation with a possible flipping of some axes), corresponding to matrix $\mathbf{V}^\top$, followed by (2) a simple scaling of the unit vectors, corresponding to $\boldsymbol{\Sigma}$, followed by (3) another orthogonal transformation, corresponding to $\mathbf{U}$.

> **Figure A.6:** Four panels showing how the unit circle and unit vectors (first panel) are first rotated (second panel, via $\mathbf{V}^\top$), then scaled (third panel, via $\boldsymbol{\Sigma}$, producing an axis-aligned ellipse), and finally rotated and flipped (fourth panel, via $\mathbf{U}$) to give the final ellipse image of $\mathbf{A}$.

**Example A.8 (Ellipses)** We continue Example A.5. Using the `svd` method of the module `numpy.linalg`, we obtain the following SVD matrices for matrix $\mathbf{A}$:

$$\mathbf{U} = \begin{bmatrix}-0.5430&0.8398\\0.8398&0.5430\end{bmatrix}, \quad \boldsymbol{\Sigma} = \begin{bmatrix}2.4221&0\\0&0.6193\end{bmatrix}, \quad \text{and} \quad \mathbf{V} = \begin{bmatrix}-0.3975&0.9176\\-0.9176&-0.3975\end{bmatrix}.$$

Figure A.4 (book p. 367) shows the columns of the matrix $\mathbf{U}\boldsymbol{\Sigma}$ as the two principal axes of the ellipse that is obtained by applying matrix $\mathbf{A}$ to the points of the unit circle. $\blacksquare$

A practical method to compute the pseudo-inverse of a real-valued matrix $\mathbf{A}$ is via the singular value decomposition $\mathbf{A} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top$, where $\boldsymbol{\Sigma}$ is the diagonal matrix collecting all the positive singular values, say $\sigma_1,\dots,\sigma_r$, as in Theorem A.13. In this case, $\mathbf{A}^+ = \mathbf{V}\boldsymbol{\Sigma}^+\mathbf{U}^\top$, where $\boldsymbol{\Sigma}^+$ is the $n\times m$ diagonal (pseudo-inverse) matrix:

$$\boldsymbol{\Sigma}^+ = \begin{bmatrix}\sigma_1^{-1}&0&\dots&\dots&0\\0&\ddots&0&\dots&0\\0&\dots&\sigma_r^{-1}&\dots&0\\0&\dots&\dots&0&\dots&0\\0&\dots&\dots&\dots&\ddots&0\end{bmatrix}.$$

We conclude with a typical application of the pseudo-inverse for a least-squares optimization problem from data science.

**Example A.9 (Rank-Deficient Least Squares)** Given is an $n\times p$ data matrix

$$\mathbf{X} = \begin{bmatrix}x_{11}&x_{12}&\cdots&x_{1p}\\x_{21}&x_{22}&\cdots&x_{2p}\\\vdots&\vdots&\vdots&\vdots\\x_{n1}&x_{n2}&\cdots&x_{np}\end{bmatrix}.$$

It is assumed that the matrix is of full row rank (all rows of $\mathbf{X}$ are linearly independent) and that the number of rows is less than the number of columns: $n < p$. Under this setting, any solution to the equation $\mathbf{X}\boldsymbol{\beta} = \boldsymbol{y}$ provides a perfect fit to the data and minimizes (to 0) the least-squares problem

$$\widehat{\boldsymbol{\beta}} = \operatorname*{argmin}_{\boldsymbol{\beta}\in\mathbb{R}^p} \|\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}\|^2. \tag{A.21}$$

In particular, if $\boldsymbol{\beta}^*$ minimizes $\|\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}\|^2$ then so does $\boldsymbol{\beta}^*+\boldsymbol{u}$ for all $\boldsymbol{u}$ in the null space $\mathcal{N}_{\mathbf{X}} := \{\boldsymbol{u} : \mathbf{X}\boldsymbol{u}=\boldsymbol{0}\}$, which has dimension $p-n$. To cope with the non-uniqueness of solutions, a possible approach is to solve instead the following optimization problem:

$$\text{minimize}\quad \boldsymbol{\beta}^\top\boldsymbol{\beta}$$
$$\text{subject to}\quad \mathbf{X}\boldsymbol{\beta}-\boldsymbol{y}=\boldsymbol{0}.$$

That is, we are interested in a solution $\boldsymbol{\beta}$ with the smallest squared norm (or, equivalently, the smallest norm). The solution can be obtained via Lagrange's method (see Section B.2.2, book p. 406). Specifically, set $\mathcal{L}(\boldsymbol{\beta},\boldsymbol{\lambda}) = \boldsymbol{\beta}^\top\boldsymbol{\beta} - \boldsymbol{\lambda}^\top(\mathbf{X}\boldsymbol{\beta}-\boldsymbol{y})$, and solve

$$\nabla_{\boldsymbol{\beta}}\mathcal{L}(\boldsymbol{\beta},\boldsymbol{\lambda}) = 2\boldsymbol{\beta}-\mathbf{X}^\top\boldsymbol{\lambda} = \boldsymbol{0}, \tag{A.22}$$

and

$$\nabla_{\boldsymbol{\lambda}}\mathcal{L}(\boldsymbol{\beta},\boldsymbol{\lambda}) = \mathbf{X}\boldsymbol{\beta}-\boldsymbol{y} = \boldsymbol{0}. \tag{A.23}$$

From (A.22) we get $\boldsymbol{\beta} = \mathbf{X}^\top\boldsymbol{\lambda}/2$. By substituting it in (A.23), we arrive at $\boldsymbol{\lambda} = 2(\mathbf{XX}^\top)^{-1}\boldsymbol{y}$, and hence $\boldsymbol{\beta}$ is given by

$$\boldsymbol{\beta} = \frac{\mathbf{X}^\top\boldsymbol{\lambda}}{2} = \frac{\mathbf{X}^\top 2(\mathbf{XX}^\top)^{-1}\boldsymbol{y}}{2} = \mathbf{X}^\top(\mathbf{XX}^\top)^{-1}\boldsymbol{y} = \mathbf{X}^+\boldsymbol{y}.$$

An example Python code is given below.

```python
# svdexample.py
from numpy import diag, zeros, vstack
from numpy.random import rand, seed
from numpy.linalg import svd, pinv
seed(12345)
n = 5
p = 8
X = rand(n, p)
y = rand(n, 1)
U, S, VT = svd(X)
SI = diag(1 / S)
# compute pseudo inverse
pseudo_inv = VT.T @ vstack((SI, zeros((p - n, n)))) @ U.T
b = pseudo_inv @ y
# b = pinv(X) @ y  #remove comment for the built-in pseudo inverse
print(X @ b - y)
```

Output:
```
[[5.55111512e-16]
 [1.11022302e-16]
 [5.55111512e-16]
 [8.60422844e-16]
 [2.22044605e-16]]
```

$\blacksquare$

## A.6.6 Solving Structured Matrix Equations

For a general matrix $\mathbf{A} \in \mathbb{C}^{n\times n}$, performing matrix–vector multiplications takes $O(n^2)$ operations; and solving linear systems $\mathbf{A}\boldsymbol{x}=\boldsymbol{b}$, and carrying out LU decompositions takes $O(n^3)$ operations. However, when $\mathbf{A}$ is *sparse* (i.e., has relatively few non-zero elements) or has a special structure, the computational complexity for these operations can often be reduced. Matrices $\mathbf{A}$ that are "structured" in this way often satisfy a *Sylvester equation*, of the form

$$\mathbf{M}_1\mathbf{A} - \mathbf{AM}_2^* = \mathbf{G}_1\mathbf{G}_2^*, \tag{A.24}$$

where $\mathbf{M}_i \in \mathbb{C}^{n\times n}, i=1,2$ are sparse matrices and $\mathbf{G}_i \in \mathbb{C}^{n\times r}, i=1,2$ are matrices of rank $r \ll n$. The elements of $\mathbf{A}$ must be easy to recover from these matrices, e.g., with $O(1)$ operations. A typical example is a (square) *Toeplitz matrix*, which has the following structure:

$$\mathbf{A} = \begin{bmatrix}a_0&a_{-1}&\cdots&a_{-(n-2)}&a_{-(n-1)}\\a_1&a_0&a_{-1}&&a_{-(n-2)}\\\vdots&a_1&a_0&\ddots&\vdots\\a_{n-2}&&\ddots&\ddots&a_{-1}\\a_{n-1}&a_{n-2}&\cdots&a_1&a_0\end{bmatrix}.$$

A general square Toeplitz matrix $\mathbf{A}$ is completely determined by the $2n-1$ elements along its first row and column. If $\mathbf{A}$ is also Hermitian (i.e., $\mathbf{A}^*=\mathbf{A}$), then clearly it is determined by only $n$ elements. If we define the matrices:

$$\mathbf{M}_1 = \begin{bmatrix}0&0&\cdots&0&1\\1&0&0&&0\\\vdots&1&0&\ddots&\vdots\\0&&\ddots&\ddots&0\\0&0&\cdots&1&0\end{bmatrix} \quad \text{and} \quad \mathbf{M}_2 = \begin{bmatrix}0&1&\cdots&0&0\\0&0&1&&0\\\vdots&0&0&\ddots&\vdots\\0&&\ddots&\ddots&1\\-1&0&\cdots&0&0\end{bmatrix},$$

then (A.24) is satisfied with

$$\mathbf{G}_1\mathbf{G}_2^* := \begin{bmatrix}1&0\\0&a_1+a_{-(n-1)}\\0&a_2+a_{-(n-2)}\\\vdots&\vdots\\0&a_{n-1}+a_{-1}\end{bmatrix}\begin{bmatrix}a_{n-1}-a_{-1}&a_{n-2}-a_{-2}&\dots&a_1-a_{-(n-1)}&2a_0\\0&0&\dots&0&1\end{bmatrix}$$

$$= \begin{bmatrix}a_{n-1}-a_{-1}&a_{n-2}-a_{-2}&\dots&a_1-a_{-(n-1)}&2a_0\\0&0&\dots&0&a_1+a_{-(n-1)}\\\vdots&\vdots&\dots&\vdots&a_2+a_{-(n-2)}\\\vdots&\vdots&\dots&\vdots&\vdots\\0&0&\dots&0&a_{n-1}+a_{-1}\end{bmatrix},$$

which has rank $r \le 2$.

**Example A.10 (Discrete Convolution of Vectors)** The convolution of two vectors can be represented as multiplication of one of the vectors by a Toeplitz matrix. Suppose $\boldsymbol{a} = [a_1,\dots,a_n]^\top$ and $\boldsymbol{b} = [b_1,\dots,b_n]^\top$ are two complex-valued vectors. Then, their *convolution* is defined as the vector $\boldsymbol{a}*\boldsymbol{b}$ with $i$-th element

$$[\boldsymbol{a}*\boldsymbol{b}]_i = \sum_{k=1}^n a_k b_{i-k+1}, \quad i=1,\dots,n,$$

where $b_j := 0$ for $j \le 0$. It is easy to verify that the convolution can be written as

$$\boldsymbol{a}*\boldsymbol{b} = \mathbf{A}\boldsymbol{b},$$

where, denoting the $d$-dimensional column vector of zeros by $\boldsymbol{0}_d$, we have that

$$\mathbf{A} = \begin{bmatrix}\boldsymbol{a}&0\\\boldsymbol{0}_{n-1}&\boldsymbol{a}&\ddots\\&\boldsymbol{0}_{n-2}&\ddots&\boldsymbol{0}_{n-2}\\&&\ddots&\boldsymbol{a}&\boldsymbol{0}_{n-1}\\&&&0&\boldsymbol{a}\end{bmatrix}.$$

Clearly, the matrix $\mathbf{A}$ is a (sparse) Toeplitz matrix. $\blacksquare$

A *circulant matrix* is a special Toeplitz matrix which is obtained from a vector $\boldsymbol{c}$ by circularly permuting its indices as follows:

$$\mathbf{C} = \begin{bmatrix}c_0&c_{n-1}&\dots&c_2&c_1\\c_1&c_0&c_{n-1}&&c_2\\\vdots&c_1&c_0&\ddots&\vdots\\c_{n-2}&&\ddots&\ddots&c_{n-1}\\c_{n-1}&c_{n-2}&\dots&c_1&c_0\end{bmatrix}. \tag{A.25}$$

Note that $\mathbf{C}$ is completely determined by the $n$ elements of its first column, $\boldsymbol{c}$.

To illustrate how structured matrices allow for faster matrix computations, consider solving the $n\times n$ linear system:

$$\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{a}_n$$

for $\boldsymbol{x}_n = [x_1,\dots,x_n]^\top$, where $\boldsymbol{a}_n = [a_1,\dots,a_n]^\top$, and

$$\mathbf{A}_n := \begin{bmatrix}1&a_1&\dots&a_{n-2}&a_{n-1}\\a_1&1&\ddots&&a_{n-2}\\\vdots&\ddots&\ddots&\ddots&\vdots\\a_{n-2}&&\ddots&\ddots&a_1\\a_{n-1}&a_{n-2}&\dots&a_1&1\end{bmatrix} \tag{A.26}$$

is a real-valued symmetric positive-definite Toeplitz matrix (so that it is invertible). Note that the entries of $\mathbf{A}_n$ are completely determined by the right-hand side of the linear equation: vector $\boldsymbol{a}_n$. As we shall see shortly in Example A.11, the solution to the more general linear equation $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{b}_n$, where $\boldsymbol{b}_n$ is arbitrary, can be efficiently computed using the solution to this specific system $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{a}_n$, obtained via a special recursive algorithm (Algorithm A.6.3 below).

For every $k=1,\dots,n$ the $k\times k$ Toeplitz matrix $\mathbf{A}_k$ satisfies

$$\mathbf{A}_k = \mathbf{P}_k\mathbf{A}_k\mathbf{P}_k,$$

where $\mathbf{P}_k$ is a permutation matrix that "flips" the order of elements — rows when pre-multiplying and columns when post-multiplying. For example,

$$\begin{bmatrix}1&2&3&4&5\\6&7&8&9&10\end{bmatrix}\mathbf{P}_5 = \begin{bmatrix}5&4&3&2&1\\10&9&8&7&6\end{bmatrix}, \quad \text{where} \quad \mathbf{P}_5 = \begin{bmatrix}0&0&0&0&1\\0&0&0&1&0\\0&0&1&0&0\\0&1&0&0&0\\1&0&0&0&0\end{bmatrix}.$$

Clearly, $\mathbf{P}_k = \mathbf{P}_k^\top$ and $\mathbf{P}_k\mathbf{P}_k = \mathbf{I}_k$ hold, so that in fact $\mathbf{P}_k$ is an orthogonal matrix.

We can solve the $n\times n$ linear system $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{a}_n$ in $O(n^2)$ time recursively, as follows. Assume that we have somehow solved for the upper $k\times k$ block $\mathbf{A}_k\boldsymbol{x}_k = \boldsymbol{a}_k$ and now we wish to solve for the $(k+1)\times(k+1)$ block:

$$\mathbf{A}_{k+1}\boldsymbol{x}_{k+1} = \boldsymbol{a}_{k+1} \iff \begin{bmatrix}\mathbf{A}_k&\mathbf{P}_k\boldsymbol{a}_k\\\boldsymbol{a}_k^\top\mathbf{P}_k&1\end{bmatrix}\begin{bmatrix}\boldsymbol{z}\\\alpha\end{bmatrix} = \begin{bmatrix}\boldsymbol{a}_k\\a_{k+1}\end{bmatrix}.$$

Therefore,

$$\alpha = a_{k+1}-\boldsymbol{a}_k^\top\mathbf{P}_k\boldsymbol{z}$$
$$\mathbf{A}_k\boldsymbol{z} = \boldsymbol{a}_k - \alpha\mathbf{P}_k\boldsymbol{a}_k.$$

Since $\mathbf{A}_k^{-1}\mathbf{P}_k = \mathbf{P}_k\mathbf{A}_k^{-1}$, the second equation above simplifies to

$$\boldsymbol{z} = \mathbf{A}_k^{-1}\boldsymbol{a}_k - \alpha\mathbf{A}_k^{-1}\mathbf{P}_k\boldsymbol{a}_k = \boldsymbol{x}_k - \alpha\mathbf{P}_k\boldsymbol{x}_k.$$

Substituting $\boldsymbol{z} = \boldsymbol{x}_k - \alpha\mathbf{P}_k\boldsymbol{x}_k$ into $\alpha = a_{k+1}-\boldsymbol{a}_k^\top\mathbf{P}_k\boldsymbol{z}$ and solving for $\alpha$ yields:

$$\alpha = \frac{a_{k+1}-\boldsymbol{a}_k^\top\mathbf{P}_k\boldsymbol{x}_k}{1-\boldsymbol{a}_k^\top\boldsymbol{x}_k}.$$

Finally, with the value of $\alpha$ computed above, we have

$$\boldsymbol{x}_{k+1} = \begin{bmatrix}\boldsymbol{x}_k-\alpha\mathbf{P}_k\boldsymbol{x}_k\\\alpha\end{bmatrix}.$$

This gives the following *Levinson–Durbin* recursive algorithm for solving $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{a}_n$.

**Algorithm A.6.3: Levinson–Durbin Recursion for Solving $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{a}_n$**

```
input: First row [1, a1, ..., a_{n-1}] = [1, a_{n-1}^T] of matrix An.
output: Solution xn = An^-1 an.
1  x1 <- a1
2  for k = 1, ..., n-1 do
3  |   beta_k <- 1 - ak^T xk
4  |   xcheck <- [x_{k,k}, x_{k,k-1}, ..., x_{k,1}]^T
5  |   alpha <- (a_{k+1} - ak^T xcheck) / beta_k
6  |   x_{k+1} <- [xk - alpha * xcheck, alpha]
7  return xn
```

In the algorithm above, we have identified $\boldsymbol{x}_k = [x_{k,1},x_{k,2},\dots,x_{k,k}]^\top$. The advantage of the Levinson–Durbin algorithm is that its running cost is $O(n^2)$, instead of the usual $O(n^3)$.

Using the $\{\boldsymbol{x}_k,\beta_k\}$ computed in Algorithm A.6.3, we construct the following lower triangular matrix recursively, setting $\mathbf{L}_1 = 1$ and

$$\mathbf{L}_{k+1} = \begin{bmatrix}\mathbf{L}_k&\mathbf{0}_k\\-(\mathbf{P}_k\boldsymbol{x}_k)^\top&1\end{bmatrix}, \quad k=1,\dots,n-1. \tag{A.27}$$

Then, we have the following factorization of $\mathbf{A}_n$.

**Theorem A.14: Diagonalization of Toeplitz Correlation Matrix $\mathbf{A}_n$**

> For a real-valued symmetric positive-definite Toeplitz matrix $\mathbf{A}_n$ of the form (A.26), we have
> $$\mathbf{L}_n\mathbf{A}_n\mathbf{L}_n^\top = \mathbf{D}_n,$$
> where $\mathbf{L}_n$ is the lower diagonal matrix (A.27) and $\mathbf{D}_n := \operatorname{diag}(1,\beta_1,\dots,\beta_{n-1})$ is a diagonal matrix.

*Proof:* We give a proof by induction. Obviously, $\mathbf{L}_1\mathbf{A}_1\mathbf{L}_1^\top = 1\cdot1\cdot1 = 1 = \mathbf{D}_1$ is true. Next, assume that the factorization $\mathbf{L}_k\mathbf{A}_k\mathbf{L}_k^\top = \mathbf{D}_k$ holds for a given $k$. Observe that

$$\mathbf{L}_{k+1}\mathbf{A}_{k+1} = \begin{bmatrix}\mathbf{L}_k&\mathbf{0}_k\\-(\mathbf{P}_k\boldsymbol{x}_k)^\top&1\end{bmatrix}\begin{bmatrix}\mathbf{A}_k&\mathbf{P}_k\boldsymbol{a}_k\\\boldsymbol{a}_k^\top\mathbf{P}_k&1\end{bmatrix} = \begin{bmatrix}\mathbf{L}_k\mathbf{A}_k,&\mathbf{L}_k\mathbf{P}_k\boldsymbol{a}_k\\-(\mathbf{P}_k\boldsymbol{x}_k)^\top\mathbf{A}_k+\boldsymbol{a}_k^\top\mathbf{P}_k,&-(\mathbf{P}_k\boldsymbol{x}_k)^\top\mathbf{P}_k\boldsymbol{a}_k+1\end{bmatrix}.$$

It is straightforward to verify that $[-(\mathbf{P}_k\boldsymbol{x}_k)^\top\mathbf{A}_k+\boldsymbol{a}_k^\top\mathbf{P}_k,\ -(\mathbf{P}_k\boldsymbol{x}_k)^\top\mathbf{P}_k\boldsymbol{a}_k+1] = [\mathbf{0}_k^\top,\beta_k]$, yielding the recursion

$$\mathbf{L}_{k+1}\mathbf{A}_{k+1} = \begin{bmatrix}\mathbf{L}_k\mathbf{A}_k&\mathbf{L}_k\mathbf{P}_k\boldsymbol{a}_k\\\mathbf{0}_k^\top&\beta_k\end{bmatrix}.$$

Secondly, observe that

$$\mathbf{L}_{k+1}\mathbf{A}_{k+1}\mathbf{L}_{k+1}^\top = \begin{bmatrix}\mathbf{L}_k\mathbf{A}_k&\mathbf{L}_k\mathbf{P}_k\boldsymbol{a}_k\\\mathbf{0}_k^\top&\beta_k\end{bmatrix}\begin{bmatrix}\mathbf{L}_k^\top&-\mathbf{P}_k\boldsymbol{x}_k\\\mathbf{0}_k^\top&1\end{bmatrix} = \begin{bmatrix}\mathbf{L}_k\mathbf{A}_k\mathbf{L}_k^\top,&-\mathbf{L}_k\mathbf{A}_k\mathbf{P}_k\boldsymbol{x}_k+\mathbf{L}_k\mathbf{P}_k\boldsymbol{a}_k\\\mathbf{0}_k^\top,&\beta_k\end{bmatrix}.$$

By noting that $\mathbf{A}_k\mathbf{P}_k\boldsymbol{x}_k = \mathbf{P}_k\mathbf{P}_k\mathbf{A}_k\mathbf{P}_k\boldsymbol{x}_k = \mathbf{P}_k\mathbf{A}_k\boldsymbol{x}_k = \mathbf{P}_k\boldsymbol{a}_k$, we obtain:

$$\mathbf{L}_{k+1}\mathbf{A}_{k+1}\mathbf{L}_{k+1}^\top = \begin{bmatrix}\mathbf{L}_k\mathbf{A}_k\mathbf{L}_k^\top&\mathbf{0}_k\\\mathbf{0}_k^\top&\beta_k\end{bmatrix}.$$

Hence, the result follows by induction. $\square$

**Example A.11 (Solving $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{b}_n$ in $O(n^2)$ Time)** One application of the factorization in Theorem A.14 is in the fast solution of a linear system $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{b}_n$, where the right-hand side is an arbitrary vector $\boldsymbol{b}_n$. Since the solution $\boldsymbol{x}_n$ can be written as

$$\boldsymbol{x}_n = \mathbf{A}_n^{-1}\boldsymbol{b}_n = \mathbf{L}_n^\top\mathbf{D}_n^{-1}\mathbf{L}_n\boldsymbol{b}_n,$$

we can compute $\boldsymbol{x}_n$ in $O(n^2)$ time, as follows.

**Algorithm A.6.4: Solving $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{b}_n$ for a General Right-Hand Side**

```
input: First row [1, a_{n-1}^T] of matrix An and right-hand side bn.
output: Solution xn = An^-1 bn.
1  Compute Ln in (A.27) and the numbers beta_1, ..., beta_{n-1} via Algorithm A.6.3.
2  [x1, ..., xn]^T <- Ln bn        (computed in O(n^2) time)
3  xi <- xi / beta_{i-1} for i = 2, ..., n   (computed in O(n) time)
4  [x1, ..., xn] <- [x1, ..., xn] Ln   (computed in O(n^2) time)
5  return xn <- [x1, ..., xn]^T
```

$\blacksquare$

Note that it is possible to avoid the explicit construction of the lower triangular matrix in (A.27) via the following modification of Algorithm A.6.3, which only stores an extra vector $\boldsymbol{y}$ at each recursive step of the Levinson–Durbin algorithm.

**Algorithm A.6.5: Solving $\mathbf{A}_n\boldsymbol{x}_n = \boldsymbol{b}_n$ with $O(n)$ Memory Cost**

```
input: First row [1, a_{n-1}^T] of matrix An and right-hand side bn.
output: Solution xn = An^-1 bn.
1  x <- b1
2  y <- a1
3  for k = 1, ..., n-1 do
4  |   xcheck <- [xk, x_{k-1}, ..., x1]
5  |   ycheck <- [yk, y_{k-1}, ..., y1]
6  |   beta <- 1 - ak^T y
7  |   alpha_x <- (b_{k+1} - bk^T xcheck) / beta
8  |   alpha_y <- (a_{k+1} - ak^T ycheck) / beta
9  |   x <- [x - alpha_x * xcheck, alpha_x]
10 |   y <- [y - alpha_y * ycheck, alpha_y]
11 return x
```
