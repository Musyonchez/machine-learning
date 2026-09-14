---
appendix: A
section: "A.1"
title: "Vector Spaces, Bases, and Matrices"
pdf_pages: "373-378"
---

> **Appendix A overview (book p. 355).** The purpose of this appendix is to review some important topics in linear algebra and functional analysis. We assume that the reader has some familiarity with matrix and vector operations, including matrix multiplication and the computation of determinants.

# A.1 Vector Spaces, Bases, and Matrices

Linear algebra is the study of vector spaces and linear mappings. Vectors are, by definition, elements of some *vector space* $\mathcal{V}$ and satisfy the usual rules of addition and scalar multiplication, e.g.,

$$\text{if } \boldsymbol{x} \in \mathcal{V} \text{ and } \boldsymbol{y} \in \mathcal{V}, \text{ then } \alpha\boldsymbol{x} + \beta\boldsymbol{y} \in \mathcal{V} \text{ for all } \alpha,\beta \in \mathbb{R} \ (\text{or } \mathbb{C}).$$

We will be dealing mostly with vectors in the Euclidean vector space $\mathbb{R}^n$ for some $n$. That is, we view the points of $\mathbb{R}^n$ as objects that can be added up and multiplied with a scalar, e.g., $(x_1,x_2) + (y_1,y_2) = (x_1+y_1, x_2+y_2)$ for points in $\mathbb{R}^2$. Sometimes it is convenient to work with the complex vector space $\mathbb{C}^n$ instead of $\mathbb{R}^n$; see also Section A.3.

Vectors $\boldsymbol{v}_1,\dots,\boldsymbol{v}_k$ are called *linearly independent* if none of them can be expressed as a linear combination of the others; that is, if $\alpha_1\boldsymbol{v}_1 + \cdots + \alpha_n\boldsymbol{v}_n = \boldsymbol{0}$, then it must hold that $\alpha_i = 0$ for all $i = 1,\dots,n$.

**Definition A.1: Basis of a Vector Space**

> A set of vectors $\mathcal{B} = \{\boldsymbol{v}_1,\dots,\boldsymbol{v}_n\}$ is called a *basis* of the vector space $\mathcal{V}$ if every vector $\boldsymbol{x} \in \mathcal{V}$ can be written as a unique linear combination of the vectors in $\mathcal{B}$:
> $$\boldsymbol{x} = \alpha_1 \boldsymbol{v}_1 + \cdots + \alpha_n \boldsymbol{v}_n.$$
> The (possibly infinite) number $n$ is called the *dimension* of $\mathcal{V}$.

Using a basis $\mathcal{B}$ of $\mathcal{V}$, we can thus represent each vector $\boldsymbol{x} \in \mathcal{V}$ as a row or column of numbers

$$[\alpha_1,\dots,\alpha_n] \quad \text{or} \quad \begin{bmatrix}\alpha_1\\ \vdots \\ \alpha_n\end{bmatrix}. \tag{A.1}$$

Typically, vectors in $\mathbb{R}^n$ are represented via the *standard basis*, consisting of unit vectors (points) $\boldsymbol{e}_1 = (1,0,\dots,0),\dots,\boldsymbol{e}_n = (0,0,\dots,0,1)$. As a consequence, any point $(x_1,\dots,x_n) \in \mathbb{R}^n$ can be represented, using the standard basis, as a row or column vector of the form (A.1) above, with $\alpha_i = x_i, i=1,\dots,n$. We will also write $[x_1,x_2,\dots,x_n]^\top$, for the corresponding column vector, where $^\top$ denotes the *transpose*.

> To avoid confusion, we will use the convention from now on that a generic vector $\boldsymbol{x}$ is always represented via the standard basis as a *column* vector. The corresponding row vector is denoted by $\boldsymbol{x}^\top$.

A *matrix* can be viewed as an array of $m$ rows and $n$ columns that defines a *linear transformation* from $\mathbb{R}^n$ to $\mathbb{R}^m$ (or for complex matrices, from $\mathbb{C}^n$ to $\mathbb{C}^m$). The matrix is said to be *square* if $m = n$. If $\boldsymbol{a}_1, \boldsymbol{a}_2,\dots,\boldsymbol{a}_n$ are the columns of $\mathbf{A}$, that is, $\mathbf{A} = [\boldsymbol{a}_1,\boldsymbol{a}_2,\dots,\boldsymbol{a}_n]$, and if $\boldsymbol{x} = [x_1,\dots,x_n]^\top$, then $\mathbf{A}\boldsymbol{x} = x_1\boldsymbol{a}_1 + \cdots + x_n\boldsymbol{a}_n$. In particular, the standard basis vector $\boldsymbol{e}_k$ is mapped to the vector $\boldsymbol{a}_k$, $k=1,\dots,n$. We sometimes use the notation $\mathbf{A} = [a_{ij}]$, to denote a matrix whose $(i,j)$-th element is $a_{ij}$. When we wish to emphasize that a matrix $\mathbf{A}$ is real-valued with $m$ rows and $n$ columns, we write $\mathbf{A} \in \mathbb{R}^{m\times n}$. The *rank* of a matrix is the number of linearly independent rows or, equivalently, the number of linearly independent columns.

**Example A.1 (Linear Transformation)** Take the matrix

$$\mathbf{A} = \begin{bmatrix}1 & 1 \\ -0.5 & -2\end{bmatrix}.$$

It transforms the two basis vectors $[1,0]^\top$ and $[0,1]^\top$, shown in red and blue in the left panel of Figure A.1, to the vectors $[1,-0.5]^\top$ and $[1,-2]^\top$, shown on the right panel. Similarly, the points on the unit circle are transformed to an ellipse.

> **Figure A.1:** Shows a linear transformation of the unit circle. Left panel: the unit circle with basis vectors $[1,0]^\top$ (red) and $[0,1]^\top$ (blue). Right panel: the image under $\mathbf{A}$ — an ellipse with the transformed basis vectors $[1,-0.5]^\top$ (red) and $[1,-2]^\top$ (blue).

Suppose $\mathbf{A} = [\boldsymbol{a}_1,\dots,\boldsymbol{a}_n]$, where the $\mathcal{A} = \{\boldsymbol{a}_i\}$ form a basis of $\mathbb{R}^n$. Take any vector $\boldsymbol{x} = [x_1,\dots,x_n]^\top_{\mathcal{E}}$ with respect to the standard basis $\mathcal{E}$ (we write subscript $\mathcal{E}$ to stress this). Then the representation of this vector with respect to $\mathcal{A}$ is simply

$$\boldsymbol{y} = \mathbf{A}^{-1}\boldsymbol{x},$$

where $\mathbf{A}^{-1}$ is the *inverse* of $\mathbf{A}$; that is, the matrix such that $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}_n$, where $\mathbf{I}_n$ is the $n$-dimensional identity matrix. To see this, note that $\mathbf{A}^{-1}\boldsymbol{a}_i$ gives the $i$-th unit vector representation, for $i = 1,\dots,n$, and recall that each vector in $\mathbb{R}^n$ is a unique linear combination of these basis vectors.

**Example A.2 (Basis Representation)** Consider the matrix

$$\mathbf{A} = \begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix} \quad \text{with inverse} \quad \mathbf{A}^{-1} = \begin{bmatrix}-2 & 1 \\ 3/2 & -1/2\end{bmatrix}. \tag{A.2}$$

The vector $\boldsymbol{x} = [1,1]^\top_{\mathcal{E}}$ in the standard basis has representation $\boldsymbol{y} = \mathbf{A}^{-1}\boldsymbol{x} = [-1,1]^\top_{\mathcal{A}}$ in the basis consisting of the columns of $\mathbf{A}$. Namely,

$$\mathbf{A}\boldsymbol{y} = -\begin{bmatrix}1\\3\end{bmatrix} + \begin{bmatrix}2\\4\end{bmatrix} = \begin{bmatrix}1\\1\end{bmatrix}.$$

$\blacksquare$

The *transpose* of a matrix $\mathbf{A} = [a_{ij}]$ is the matrix $\mathbf{A}^\top = [a_{ji}]$; that is, the $(i,j)$-th element of $\mathbf{A}^\top$ is the $(j,i)$-th element of $\mathbf{A}$. The *trace* of a square matrix is the sum of its diagonal elements. A useful result is the following cyclic property.

**Theorem A.1: Cyclic Property**

> The trace is invariant under cyclic permutations: $\operatorname{tr}(\mathbf{ABC}) = \operatorname{tr}(\mathbf{BCA}) = \operatorname{tr}(\mathbf{CAB})$.

*Proof:* It suffices to show that $\operatorname{tr}(\mathbf{DE})$ is equal to $\operatorname{tr}(\mathbf{ED})$ for any $m\times n$ matrix $\mathbf{D} = [d_{ij}]$ and $n\times m$ matrix $\mathbf{E} = [e_{ij}]$. The diagonal elements of $\mathbf{DE}$ are $\sum_{j=1}^n d_{ij}e_{ji}, i=1,\dots,m$ and the diagonal elements of $\mathbf{ED}$ are $\sum_{i=1}^m e_{ji}d_{ij}, j=1,\dots,n$. They sum up to the same number $\sum_{i=1}^m\sum_{j=1}^n d_{ij}e_{ji}$. $\square$

A square matrix has an inverse if and only if its columns (or rows) are linearly independent. This is the same as the matrix being of *full rank*; that is, its rank is equal to the number of columns. An equivalent statement is that its determinant is not zero. The *determinant* of an $n\times n$ matrix $\mathbf{A} = [a_{i,j}]$ is defined as

$$\det(\mathbf{A}) := \sum_{\pi} (-1)^{\zeta(\pi)} \prod_{i=1}^n a_{\pi_i, i}, \tag{A.3}$$

where the sum is over all permutations $\pi = (\pi_1,\dots,\pi_n)$ of $(1,\dots,n)$, and $\zeta(\pi)$ is the number of pairs $(i,j)$ for which $i < j$ and $\pi_i > \pi_j$. For example, $\zeta(2,3,4,1) = 3$ for the pairs $(1,4),(2,4),(3,4)$. The determinant of a *diagonal matrix* — a matrix with only zero elements off the diagonal — is simply the product of its diagonal elements.

Geometrically, the determinant of a square matrix $\mathbf{A} = [\boldsymbol{a}_1,\dots,\boldsymbol{a}_n]$ is the (signed) *volume* of the parallelepiped ($n$-dimensional parallelogram) defined by the columns $\boldsymbol{a}_1,\dots,\boldsymbol{a}_n$; that is, the set of points $\boldsymbol{x} = \sum_{i=1}^n \alpha_i \boldsymbol{a}_i$, where $0 \le \alpha_i \le 1, i = 1,\dots,n$.

The easiest way to compute a determinant of a general matrix is to apply simple operations to the matrix that potentially reduce its complexity (as in the number of non-zero elements, for example), while retaining its determinant:

- Adding a multiple of one column (or row) to another, does not change the determinant.
- Multiplying a column (or row) with a number multiplies the determinant by the same number.
- Swapping two rows changes the sign of the determinant.

By applying these rules repeatedly one can reduce any matrix to a diagonal matrix. It follows then that the determinant of the original matrix is equal to the product of the diagonal elements of the resulting diagonal matrix multiplied by a known constant.

**Example A.3 (Determinant and Volume)** Figure A.2 illustrates how the determinant of a matrix can be viewed as a signed volume, which can be computed by repeatedly applying the first rule above. Here, we wish to compute the area of red parallelogram determined by the matrix $\mathbf{A}$ given in (A.2). In particular, the corner points of the parallelogram correspond to the vectors $[0,0]^\top, [1,3]^\top, [2,4]^\top$, and $[3,7]^\top$.

> **Figure A.2:** The volume (area) of the red parallelogram can be obtained by a number of shear operations (blue, then green) that do not change the volume.

Adding $-2$ times the first column of $\mathbf{A}$ to the second column gives the matrix

$$\mathbf{B} = \begin{bmatrix}1 & 0 \\ 3 & -2\end{bmatrix},$$

corresponding to the blue parallelogram. The linear operation that transforms the red to the blue parallelogram can be thought of as a succession of two linear transformations. The first is to transform the coordinates of points on the red parallelogram (in standard basis) to the basis formed by the columns of $\mathbf{A}$. Second, relative to this new basis, we apply the matrix $\mathbf{B}$ above. Note that the input of this matrix is with respect to the new basis, whereas the output is with respect to the standard basis. The matrix for the combined operation is now

$$\mathbf{B}\mathbf{A}^{-1} = \begin{bmatrix}1 & 0\\3 & -2\end{bmatrix}\begin{bmatrix}-2 & 1\\3/2 & -1/2\end{bmatrix} = \begin{bmatrix}-2 & 1\\-9 & 4\end{bmatrix},$$

which maps $[1,3]^\top$ to $[1,3]^\top$ (does not change) and $[2,4]^\top$ to $[0,-2]^\top$. We say that we apply a *shear* in the direction $[1,3]^\top$. The significance of such an operation is that a shear *does not alter the volume of the parallelogram*. The second (blue) parallelogram has an easier form, because one of the sides is parallel to the $y$-axis. By applying another shear, in the direction $[0,-2]^\top$, we can obtain a simple (green) rectangle, whose volume is 2. In matrix terms, we add $3/2$ times the second column of $\mathbf{B}$ to the first column of $\mathbf{B}$, to obtain the matrix

$$\mathbf{C} = \begin{bmatrix}1 & 0 \\ 0 & -2\end{bmatrix},$$

which is a diagonal matrix, whose determinant is $-2$, corresponding to the volume 2 of all the parallelograms. $\blacksquare$

Theorem A.2 summarizes a number of useful matrix rules for the concepts that we have discussed so far. We leave the proofs, which typically involves "writing out" the equations, as an exercise for the reader; see also [116].

**Theorem A.2: Useful Matrix Rules**

1. $(\mathbf{AB})^\top = \mathbf{B}^\top \mathbf{A}^\top$
2. $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$
3. $(\mathbf{A}^{-1})^\top = (\mathbf{A}^\top)^{-1} =: \mathbf{A}^{-\top}$
4. $\det(\mathbf{AB}) = \det(\mathbf{A})\det(\mathbf{B})$
5. $\boldsymbol{x}^\top \mathbf{A}\boldsymbol{x} = \operatorname{tr}(\mathbf{A}\boldsymbol{x}\boldsymbol{x}^\top)$
6. $\det(\mathbf{A}) = \prod_i a_{ii}$ if $\mathbf{A} = [a_{ij}]$ is triangular

Next, consider an $n \times p$ matrix $\mathbf{A}$ for which the matrix inverse fails to exist. That is, $\mathbf{A}$ is either non-square ($n \ne p$) or its determinant is 0. Instead of the inverse, we can use its so-called pseudo-inverse, which always exists.

**Definition A.2: Moore–Penrose Pseudo-Inverse**

> The *Moore–Penrose pseudo-inverse* of a real matrix $\mathbf{A} \in \mathbb{R}^{n\times p}$ is defined as the unique matrix $\mathbf{A}^+ \in \mathbb{R}^{p\times n}$ that satisfies the conditions:
>
> 1. $\mathbf{A}\mathbf{A}^+\mathbf{A} = \mathbf{A}$
> 2. $\mathbf{A}^+\mathbf{A}\mathbf{A}^+ = \mathbf{A}^+$
> 3. $(\mathbf{A}\mathbf{A}^+)^\top = \mathbf{A}\mathbf{A}^+$
> 4. $(\mathbf{A}^+\mathbf{A})^\top = \mathbf{A}^+\mathbf{A}$

We can write $\mathbf{A}^+$ explicitly in terms of $\mathbf{A}$ when $\mathbf{A}$ has full column or row rank. For example, we always have

$$\mathbf{A}^\top \mathbf{A}\mathbf{A}^+ = \mathbf{A}^\top(\mathbf{A}\mathbf{A}^+)^\top = ((\mathbf{A}\mathbf{A}^+)\mathbf{A})^\top = (\mathbf{A})^\top = \mathbf{A}^\top. \tag{A.4}$$

If $\mathbf{A}$ has a full column rank $p$, then $(\mathbf{A}^\top\mathbf{A})^{-1}$ exists, so that from (A.4) it follows that $\mathbf{A}^+ = (\mathbf{A}^\top\mathbf{A})^{-1}\mathbf{A}^\top$. This is referred to as the *left pseudo-inverse*, as $\mathbf{A}^+\mathbf{A} = \mathbf{I}_p$. Similarly, if $\mathbf{A}$ has full row rank $n$, that is, $(\mathbf{A}\mathbf{A}^\top)^{-1}$ exists, then it follows from

$$\mathbf{A}^+\mathbf{A}\mathbf{A}^\top = (\mathbf{A}^+\mathbf{A})^\top\mathbf{A}^\top = (\mathbf{A}(\mathbf{A}^+\mathbf{A}))^\top = \mathbf{A}^\top$$

that $\mathbf{A}^+ = \mathbf{A}^\top(\mathbf{A}\mathbf{A}^\top)^{-1}$. This is the *right pseudo-inverse*, as $\mathbf{A}\mathbf{A}^+ = \mathbf{I}_n$. Finally, if $\mathbf{A}$ is of full rank and square, then $\mathbf{A}^+ = \mathbf{A}^{-1}$.
