---
appendix: A
section: "A.5"
title: "Eigenvalues and Eigenvectors"
pdf_pages: "381-386"
---

# A.5 Eigenvalues and Eigenvectors

Let $\mathbf{A}$ be an $n\times n$ matrix. If $\mathbf{A}\boldsymbol{v} = \lambda\boldsymbol{v}$ for some number $\lambda$ and non-zero vector $\boldsymbol{v}$, then $\lambda$ is called an *eigenvalue* of $\mathbf{A}$ with *eigenvector* $\boldsymbol{v}$.

If $(\lambda,\boldsymbol{v})$ is an (eigenvalue, eigenvector) pair, the matrix $\lambda\mathbf{I} - \mathbf{A}$ maps any multiple of $\boldsymbol{v}$ to the zero vector. Consequently, the columns of $\lambda\mathbf{I}-\mathbf{A}$ are linearly *dependent*, and hence its determinant is 0. This provides a way to identify the eigenvalues, namely as the $r \le n$ different roots $\lambda_1,\dots,\lambda_r$ of the *characteristic polynomial*

$$\det(\lambda\mathbf{I}-\mathbf{A}) = (\lambda-\lambda_1)^{\alpha_1}\cdots(\lambda-\lambda_r)^{\alpha_r},$$

where $\alpha_1+\cdots+\alpha_r = n$. The integer $\alpha_i$ is called the *algebraic multiplicity* of $\lambda_i$. The eigenvectors that correspond to an eigenvalue $\lambda_i$ lie in the *kernel* or *null space* of the matrix $\lambda_i\mathbf{I}-\mathbf{A}$; that is, the linear space of vectors $\boldsymbol{v}$ such that $(\lambda_i\mathbf{I}-\mathbf{A})\boldsymbol{v} = \boldsymbol{0}$. This space is called the *eigenspace* of $\lambda_i$. Its dimension, $d_i \in \{1,\dots,n\}$, is called the *geometric multiplicity* of $\lambda_i$. It always holds that $d_i \le \alpha_i$. If $\sum_i d_i = n$, then we can construct a basis for $\mathbb{R}^n$ consisting of eigenvectors, as illustrated next.

**Example A.4 (Linear Transformation (cont.))** We revisit the linear transformation in Figure A.1, where

$$\mathbf{A} = \begin{bmatrix}1 & 1\\ -1/2 & -2\end{bmatrix}.$$

The characteristic polynomial is $(\lambda-1)(\lambda+2) + 1/2$, with roots $\lambda_1 = -1/2 - \sqrt{7}/2 \approx -1.8229$ and $\lambda_2 = -1/2 + \sqrt{7}/2 \approx 0.8229$. The corresponding unit eigenvectors are $\boldsymbol{v}_1 \approx [0.3339, -0.9426]^\top$ and $\boldsymbol{v}_2 \approx [0.9847, -0.1744]^\top$. The eigenspace corresponding to $\lambda_1$ is $\mathcal{V}_1 = \operatorname{Span}\{\boldsymbol{v}_1\} = \{\beta\boldsymbol{v}_1 : \beta \in \mathbb{R}\}$ and the eigenspace corresponding to $\lambda_2$ is $\mathcal{V}_2 = \operatorname{Span}\{\boldsymbol{v}_2\}$. The algebraic and geometric multiplicities are 1 in this case. Any pair of vectors taken from $\mathcal{V}_1$ and $\mathcal{V}_2$ forms a basis for $\mathbb{R}^2$. Figure A.3 shows how $\boldsymbol{v}_1$ and $\boldsymbol{v}_2$ are transformed to $\mathbf{A}\boldsymbol{v}_1 \in \mathcal{V}_1$ and $\mathbf{A}\boldsymbol{v}_2 \in \mathcal{V}_2$, respectively.

> **Figure A.3:** The dashed arrows are the unit eigenvectors $\boldsymbol{v}_1$ (blue) and $\boldsymbol{v}_2$ (red) of matrix $\mathbf{A}$, drawn together with the ellipse image of the unit circle under $\mathbf{A}$. Their transformed values $\mathbf{A}\boldsymbol{v}_1$ and $\mathbf{A}\boldsymbol{v}_2$ (solid arrows) lie along the same directions, illustrating that eigenvectors are mapped to scalar multiples of themselves.

$\blacksquare$

A matrix for which the algebraic and geometric multiplicities of all its eigenvalues are the same is called *semi-simple*. This is equivalent to the matrix being *diagonalizable*, meaning that there is a matrix $\mathbf{V}$ and a diagonal matrix $\mathbf{D}$ such that

$$\mathbf{A} = \mathbf{VDV}^{-1}.$$

To see that this so-called *eigen-decomposition* holds, suppose $\mathbf{A}$ is a semi-simple matrix with eigenvalues

$$\underbrace{\lambda_1,\dots,\lambda_1}_{d_1},\ \cdots,\ \underbrace{\lambda_r,\dots,\lambda_r}_{d_r}.$$

Let $\mathbf{D}$ be the diagonal matrix whose diagonal elements are the eigenvalues of $\mathbf{A}$, and let $\mathbf{V}$ be a matrix whose columns are linearly independent eigenvectors corresponding to these eigenvalues. Then, for each (eigenvalue, eigenvector) pair $(\lambda,\boldsymbol{v})$, we have $\mathbf{A}\boldsymbol{v} = \lambda\boldsymbol{v}$. Hence, in matrix notation, we have $\mathbf{AV} = \mathbf{VD}$, and so $\mathbf{A} = \mathbf{VDV}^{-1}$.

## A.5.1 Left- and Right-Eigenvectors

The eigenvector as defined in the previous section is called a *right*-eigenvector, as it lies on the right of $\mathbf{A}$ in the equation $\mathbf{A}\boldsymbol{v} = \lambda\boldsymbol{v}$.

If $\mathbf{A}$ is a complex matrix with an eigenvalue $\lambda$, then the eigenvalue's complex conjugate $\bar\lambda$ is an eigenvalue of $\mathbf{A}^*$. To see this, define $\mathbf{B} := \lambda\mathbf{I}-\mathbf{A}$ and $\mathbf{B}^* := \bar\lambda\mathbf{I}-\mathbf{A}^*$. Since $\lambda$ is an eigenvalue, we have $\det(\mathbf{B}) = 0$. Applying the identity $\det(\mathbf{B}) = \overline{\det(\mathbf{B}^*)}$, we see that therefore $\det(\mathbf{B}^*) = 0$, and hence that $\bar\lambda$ is an eigenvalue of $\mathbf{A}^*$. Let $\boldsymbol{w}$ be an eigenvector corresponding to $\bar\lambda$. Then, $\mathbf{A}^*\boldsymbol{w} = \bar\lambda\boldsymbol{w}$ or, equivalently,

$$\boldsymbol{w}^*\mathbf{A} = \lambda\boldsymbol{w}^*.$$

For this reason, we call $\boldsymbol{w}^*$ the *left-eigenvector* of $\mathbf{A}$ for eigenvalue $\lambda$. If $\boldsymbol{v}$ is a (right-) eigenvector of $\mathbf{A}$, then its adjoint $\boldsymbol{v}^*$ is usually *not* a left-eigenvector, unless $\mathbf{A}^*\mathbf{A} = \mathbf{AA}^*$ (such matrices are called *normal*; a real symmetric matrix is normal). However, the important property holds that left- and right-eigenvectors belonging to *different* eigenvalues are *orthogonal*. Namely, if $\boldsymbol{w}^*$ is a left-eigenvalue of $\lambda_1$ and $\boldsymbol{v}$ a right-eigenvector of $\lambda_2 \ne \lambda_1$, then

$$\lambda_1\boldsymbol{w}^*\boldsymbol{v} = \boldsymbol{w}^*\mathbf{A}\boldsymbol{v} = \lambda_2\boldsymbol{w}^*\boldsymbol{v},$$

which can only be true if $\boldsymbol{w}^*\boldsymbol{v} = 0$.

**Theorem A.6: Schur Triangulation**

> For any complex matrix $\mathbf{A}$, there exists a unitary matrix $\mathbf{U}$ such that $\mathbf{T} = \mathbf{U}^{-1}\mathbf{AU}$ is upper triangular.

*Proof:* The proof is by induction on the dimension $n$ of the matrix. Clearly, the statement is true for $n=1$, as $\mathbf{A}$ is simply a complex number and we can take $\mathbf{U}$ equal to 1. Suppose that the result is true for dimension $n$. We wish to show that it also holds for dimension $n+1$. Any matrix $\mathbf{A}$ always has at least one eigenvalue $\lambda$ with eigenvector $\boldsymbol{v}$, normalized to have length 1. Let $\mathbf{U}$ be any unitary matrix whose first column is $\boldsymbol{v}$. Such a matrix can always be constructed[^2]. As $\mathbf{U}$ is unitary, the first row of $\mathbf{U}^{-1}$ is $\boldsymbol{v}^*$, and $\mathbf{U}^{-1}\mathbf{AU}$ is of the form

$$\underbrace{\begin{bmatrix}\boldsymbol{v}^*\\ *\end{bmatrix}}_{\mathbf{U}^{-1}} \mathbf{A} \underbrace{\left[\ \boldsymbol{v}\ \middle|\ *\ \right]}_{\mathbf{U}} = \left[\begin{array}{c|c}\lambda & *\\ \hline \mathbf{0} & \mathbf{B}\end{array}\right],$$

for some matrix $\mathbf{B}$. By the induction hypothesis, there exists a unitary matrix $\mathbf{W}$ and an upper triangular matrix $\mathbf{T}$ such that $\mathbf{W}^{-1}\mathbf{BW} = \mathbf{T}$. Now, define

$$\mathbf{V} := \left[\begin{array}{c|c}1 & \mathbf{0}^\top\\ \hline \mathbf{0} & \mathbf{W}\end{array}\right].$$

Then,

$$\mathbf{V}^{-1}\left(\mathbf{U}^{-1}\mathbf{AU}\right)\mathbf{V} = \left[\begin{array}{c|c}1 & \mathbf{0}^\top\\ \hline \mathbf{0} & \mathbf{W}^{-1}\end{array}\right]\left[\begin{array}{c|c}\lambda & *\\ \hline \mathbf{0} & \mathbf{B}\end{array}\right]\left[\begin{array}{c|c}1 & \mathbf{0}^\top\\ \hline \mathbf{0} & \mathbf{W}\end{array}\right] = \left[\begin{array}{c|c}\lambda & *\\ \hline \mathbf{0} & \mathbf{W}^{-1}\mathbf{BW}\end{array}\right] = \left[\begin{array}{c|c}\lambda & *\\ \hline \mathbf{0} & \mathbf{T}\end{array}\right],$$

which is upper triangular of dimension $n+1$. Since $\mathbf{UV}$ is unitary, this completes the induction, and hence the result is true for all $n$. $\square$

[^2]: After specifying $\boldsymbol{v}$ we can complete the rest of the unitary matrix via the Gram–Schmidt procedure, for example; see Section A.6.4.

The theorem above can be used to prove an important property of *Hermitian* matrices, i.e., matrices for which $\mathbf{A}^* = \mathbf{A}$.

**Theorem A.7: Eigenvalues of a Hermitian Matrix**

> Any $n\times n$ Hermitian matrix has real eigenvalues. The corresponding matrix of normalized eigenvectors is a unitary matrix.

*Proof:* Let $\mathbf{A}$ be a Hermitian matrix. By Theorem A.6 there exists a unitary matrix $\mathbf{U}$ such that $\mathbf{U}^{-1}\mathbf{AU} = \mathbf{T}$, where $\mathbf{T}$ is upper triangular. It follows that the adjoint $(\mathbf{U}^{-1}\mathbf{AU})^* = \mathbf{T}^*$ is lower triangular. However, $(\mathbf{U}^{-1}\mathbf{AU})^* = \mathbf{U}^{-1}\mathbf{AU}$, since $\mathbf{A}^* = \mathbf{A}$ and $\mathbf{U}^* = \mathbf{U}^{-1}$. Hence, $\mathbf{T}$ and $\mathbf{T}^*$ must be the same, which can only be the case if $\mathbf{T}$ is a *real diagonal* matrix $\mathbf{D}$. Since $\mathbf{AU} = \mathbf{DU}$, the diagonal elements are exactly the eigenvalues and the corresponding eigenvectors are the columns of $\mathbf{U}$. $\square$

In particular, the eigenvalues of a real symmetric matrix are real. We can now repeat the proof of Theorem A.6 with real eigenvalues and eigenvectors, so that there exists an orthogonal matrix $\mathbf{Q}$ such that $\mathbf{Q}^{-1}\mathbf{AQ} = \mathbf{Q}^\top\mathbf{AQ} = \mathbf{D}$. The eigenvectors can be chosen as the columns of $\mathbf{Q}$, which form an orthonormal basis. This proves the following theorem.

**Theorem A.8: Real Symmetric Matrices are Orthogonally Diagonalizable**

> Any real symmetric matrix $\mathbf{A}$ can be written as
> $$\mathbf{A} = \mathbf{QDQ}^\top,$$
> where $\mathbf{D}$ is the diagonal matrix of (real) eigenvalues and $\mathbf{Q}$ is an orthogonal matrix whose columns are eigenvectors of $\mathbf{A}$.

**Example A.5 (Real Symmetric Matrices and Ellipses)** As we have seen, linear transformations map circles into ellipses. We can use the above theory for real symmetric matrices to identify the principal axes. Consider, for example, the transformation with matrix $\mathbf{A} = [1,1;-1/2,-2]$ in (A.1). A point $\boldsymbol{x}$ on the unit circle is mapped to a point $\boldsymbol{y} = \mathbf{A}\boldsymbol{x}$. Since for such points $\|\boldsymbol{x}\|^2 = \boldsymbol{x}^\top\boldsymbol{x} = 1$, we have that $\boldsymbol{y}$ satisfies $\boldsymbol{y}^\top(\mathbf{A}^{-1})^\top\mathbf{A}^{-1}\boldsymbol{y} = 1$, which gives the equation for the ellipse

$$\frac{17y_1^2}{9} + \frac{20y_1y_2}{9} + \frac{8y_2^2}{9} = 1.$$

Let $\mathbf{Q}$ be the orthogonal matrix of eigenvectors of the symmetric matrix $(\mathbf{A}^{-1})^\top\mathbf{A}^{-1} = (\mathbf{AA}^\top)^{-1}$, so $\mathbf{Q}^\top(\mathbf{AA}^\top)^{-1}\mathbf{Q} = \mathbf{D}$ for some diagonal matrix $\mathbf{D}$. Taking the inverse on both sides of the previous equation, we have $\mathbf{Q}^\top\mathbf{AA}^\top\mathbf{Q} = \mathbf{D}^{-1}$, which shows that $\mathbf{Q}$ is also the matrix of eigenvectors of $\mathbf{AA}^\top$. These eigenvectors point precisely in the direction of the principal axes, as shown in Figure A.4. It turns out, see Section A.6.5, that the square roots of the eigenvalues of $\mathbf{AA}^\top$, here approximately 2.4221 and 0.6193, correspond to the sizes of the principal axes of the ellipse, as illustrated in Figure A.4.

> **Figure A.4:** The ellipse (image of the unit circle under $\mathbf{A}$) with its two principal axes drawn as red and blue arrows. The eigenvectors and eigenvalues of $\mathbf{AA}^\top$ determine the directions and half-lengths ($\sqrt{2.4221}$ and $\sqrt{0.6193}$) of these principal axes.

$\blacksquare$

The following definition generalizes the notion of positivity of a real variable to that of a (Hermitian) matrix, providing a crucial concept for multivariate differentiation and optimization; see Appendix B (book p. 397).

**Definition A.3: Positive (Semi)Definite Matrix**

> A Hermitian matrix $\mathbf{A}$ is called *positive semidefinite* (we write $\mathbf{A} \succeq 0$) if $\langle\mathbf{A}\boldsymbol{x},\boldsymbol{x}\rangle \ge 0$ for all $\boldsymbol{x}$. It is called *positive definite* (we write $\mathbf{A} \succ 0$) if $\langle\mathbf{A}\boldsymbol{x},\boldsymbol{x}\rangle > 0$ for all $\boldsymbol{x} \ne \boldsymbol{0}$.

The positive (semi)definiteness of a matrix can be directly related to the positivity of its eigenvalues, as follows:

**Theorem A.9: Eigenvalues of a Positive Semidefinite Matrix**

> All eigenvalues of a positive semidefinite matrix are non-negative and all eigenvalues of a positive definite matrix are strictly positive.

*Proof:* Let $\mathbf{A}$ be a positive semidefinite matrix. By Theorem A.7, the eigenvalues of $\mathbf{A}$ are all *real*. Suppose $\lambda$ is an eigenvalue with eigenvector $\boldsymbol{v}$. As $\mathbf{A}$ is positive semidefinite, we have

$$0 \le \langle\mathbf{A}\boldsymbol{v},\boldsymbol{v}\rangle = \lambda\langle\boldsymbol{v},\boldsymbol{v}\rangle = \lambda\|\boldsymbol{v}\|^2,$$

which can only be true if $\lambda \ge 0$. Similarly, for a positive definite matrix, $\lambda$ must be strictly greater than 0. $\square$

**Corollary A.1** Any real positive semidefinite matrix $\mathbf{A}$ can be written as

$$\mathbf{A} = \mathbf{BB}^\top$$

for some real matrix $\mathbf{B}$. Conversely, for any real matrix $\mathbf{B}$, the matrix $\mathbf{BB}^\top$ is positive semidefinite.

*Proof:* The matrix $\mathbf{A}$ is both Hermitian (by definition) and real (by assumption) and hence it is symmetric. By Theorem A.8, we can write $\mathbf{A} = \mathbf{QDQ}^\top$, where $\mathbf{D}$ is the diagonal matrix of (real) eigenvalues of $\mathbf{A}$. By Theorem A.9 all eigenvalues are non-negative, and thus their square root is real-valued. Now, define $\mathbf{B} = \mathbf{Q}\sqrt{\mathbf{D}}$, where $\sqrt{\mathbf{D}}$ is defined as the diagonal matrix whose diagonal elements are the square roots of the eigenvalues of $\mathbf{A}$. Then, $\mathbf{BB}^\top = \mathbf{Q}\sqrt{\mathbf{D}}(\sqrt{\mathbf{D}})^\top\mathbf{Q}^\top = \mathbf{QDQ}^\top = \mathbf{A}$. The converse statement follows from the fact that $\boldsymbol{x}^\top\mathbf{BB}^\top\boldsymbol{x} = \|\mathbf{B}^\top\boldsymbol{x}\|^2 \ge 0$ for all $\boldsymbol{x}$. $\square$
