---
appendix: B
section: "B.1"
title: "Multivariate Differentiation"
pdf_pages: "415-420"
---

> The purpose of this appendix is to review various aspects of multivariate differentiation and optimization. We assume the reader is familiar with differentiating a real-valued function.

# B.1 Multivariate Differentiation

For a multivariate function $f$ that maps a vector $\boldsymbol{x} = [x_1,\dots,x_n]^\top$ to a real number $f(\boldsymbol{x})$, the **partial derivative** with respect to $x_i$, denoted $\frac{\partial f}{\partial x_i}$, is the derivative taken with respect to $x_i$ while all other variables are held constant. We can write all the $n$ partial derivatives neatly using the "scalar/vector" derivative notation:

$$
\text{scalar/vector:}\qquad \frac{\partial f}{\partial \boldsymbol{x}} := \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}. \tag{B.1}
$$

This vector of partial derivatives is known as the **gradient** of $f$ at $\boldsymbol{x}$ and is sometimes written as $\nabla f(\boldsymbol{x})$.

Next, suppose that $\boldsymbol{f}$ is a multivalued (vector-valued) function taking values in $\mathbb{R}^m$, defined by

$$
\boldsymbol{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} \mapsto \begin{bmatrix} f_1(\boldsymbol{x}) \\ f_2(\boldsymbol{x}) \\ \vdots \\ f_m(\boldsymbol{x}) \end{bmatrix} =: \boldsymbol{f}(\boldsymbol{x}).
$$

We can compute each of the partial derivatives $\partial f_i/\partial x_j$ and organize them neatly in a "vector/vector" derivative notation:

$$
\text{vector/vector:}\qquad \frac{\partial \boldsymbol{f}}{\partial \boldsymbol{x}} := \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_2}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_1} \\
\frac{\partial f_1}{\partial x_2} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_2} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial f_1}{\partial x_n} & \frac{\partial f_2}{\partial x_n} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}. \tag{B.2}
$$

The transpose of this matrix is known as the **matrix of Jacobi** of $\boldsymbol{f}$ at $\boldsymbol{x}$ (sometimes called the *Fréchet derivative* of $\boldsymbol{f}$ at $\boldsymbol{x}$); that is,

$$
\mathbf{J}_f(\boldsymbol{x}) := \left[\frac{\partial \boldsymbol{f}}{\partial \boldsymbol{x}}\right]^\top = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}. \tag{B.3}
$$

If we define $\boldsymbol{g}(\boldsymbol{x}) := \nabla f(\boldsymbol{x})$ and take the "vector/vector" derivative of $\boldsymbol{g}$ with respect to $\boldsymbol{x}$, we obtain the matrix of second-order partial derivatives of $f$:

$$
\mathbf{H}_f(\boldsymbol{x}) := \frac{\partial \boldsymbol{g}}{\partial \boldsymbol{x}} = \begin{bmatrix}
\frac{\partial^2 f}{\partial^2 x_1} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_m} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial^2 x_2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_m} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial^2 f}{\partial x_m \partial x_1} & \frac{\partial^2 f}{\partial x_m \partial x_2} & \cdots & \frac{\partial^2 f}{\partial^2 x_m}
\end{bmatrix}, \tag{B.4}
$$

which is known as the **Hessian matrix** of $f$ at $\boldsymbol{x}$, also denoted as $\nabla^2 f(\boldsymbol{x})$. If these second-order partial derivatives are *continuous* in a region around $\boldsymbol{x}$, then $\frac{\partial f}{\partial x_i \partial x_j} = \frac{\partial f}{\partial x_j \partial x_i}$ and, hence, the Hessian matrix $\mathbf{H}_f(\boldsymbol{x})$ is *symmetric*.

Finally, note that we can also define a "scalar/matrix" derivative of $y$ with respect to $\mathbf{X} \in \mathbb{R}^{m\times n}$ with $(i,j)$-th entry $x_{ij}$:

$$
\frac{\partial y}{\partial \mathbf{X}} := \begin{bmatrix}
\frac{\partial y}{\partial x_{11}} & \frac{\partial y}{\partial x_{12}} & \cdots & \frac{\partial y}{\partial x_{1n}} \\
\frac{\partial y}{\partial x_{21}} & \frac{\partial y}{\partial x_{22}} & \cdots & \frac{\partial y}{\partial x_{2n}} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial y}{\partial x_{m1}} & \frac{\partial y}{\partial x_{m2}} & \cdots & \frac{\partial y}{\partial x_{mn}}
\end{bmatrix}
$$

and a "matrix/scalar" derivative:

$$
\frac{\partial \mathbf{X}}{\partial y} := \begin{bmatrix}
\frac{\partial x_{11}}{\partial y} & \frac{\partial x_{12}}{\partial y} & \cdots & \frac{\partial x_{1n}}{\partial y} \\
\frac{\partial x_{21}}{\partial y} & \frac{\partial x_{22}}{\partial y} & \cdots & \frac{\partial x_{2n}}{\partial y} \\
\vdots & \vdots & \cdots & \vdots \\
\frac{\partial x_{m1}}{\partial y} & \frac{\partial x_{m2}}{\partial y} & \cdots & \frac{\partial x_{mn}}{\partial y}
\end{bmatrix}.
$$

**Example B.1 (Scalar/Matrix Derivative).** Let $y = \boldsymbol{a}^\top \mathbf{X} \boldsymbol{b}$, where $\mathbf{X} \in \mathbb{R}^{m\times n}$, $\boldsymbol{a} \in \mathbb{R}^m$, and $\boldsymbol{b} \in \mathbb{R}^n$. Since $y$ is a scalar, we can write $y = \operatorname{tr}(y) = \operatorname{tr}(\mathbf{X}\boldsymbol{b}\boldsymbol{a}^\top)$, using the cyclic property of the trace (see Theorem A.1). Defining $\mathbf{C} := \boldsymbol{b}\boldsymbol{a}^\top$, we have

$$
y = \sum_{i=1}^m [\mathbf{X}\mathbf{C}]_{ii} = \sum_{i=1}^m \sum_{j=1}^n x_{ij} c_{ji},
$$

so that $\partial y/\partial x_{ij} = c_{ji}$ or, in matrix form,

$$
\frac{\partial y}{\partial \mathbf{X}} = \mathbf{C}^\top = \boldsymbol{a}\boldsymbol{b}^\top.
$$

**Example B.2 (Scalar/Matrix Derivative via the Woodbury Identity).** Let $y = \operatorname{tr}(\mathbf{X}^{-1}\mathbf{A})$, where $\mathbf{X}, \mathbf{A} \in \mathbb{R}^{n\times n}$. We now prove that

$$
\frac{\partial y}{\partial \mathbf{X}} = -\mathbf{X}^{-\top}\mathbf{A}^\top \mathbf{X}^{-\top}.
$$

To show this, apply the Woodbury matrix identity to an infinitesimal perturbation, $\mathbf{X} + \varepsilon \mathbf{U}$, of $\mathbf{X}$, and take $\varepsilon \downarrow 0$ to obtain the following:

$$
\frac{(\mathbf{X}+\varepsilon\mathbf{U})^{-1} - \mathbf{X}^{-1}}{\varepsilon} = -\mathbf{X}^{-1}\mathbf{U}(\mathbf{I}+\varepsilon\mathbf{X}^{-1}\mathbf{U})^{-1}\mathbf{X}^{-1} \longrightarrow -\mathbf{X}^{-1}\mathbf{U}\mathbf{X}^{-1}.
$$

Therefore, as $\varepsilon \downarrow 0$

$$
\frac{\operatorname{tr}((\mathbf{X}+\varepsilon\mathbf{U})^{-1}\mathbf{A}) - \operatorname{tr}(\mathbf{X}^{-1}\mathbf{A})}{\varepsilon} \longrightarrow -\operatorname{tr}(\mathbf{X}^{-1}\mathbf{U}\mathbf{X}^{-1}\mathbf{A}) = -\operatorname{tr}(\mathbf{U}\mathbf{X}^{-1}\mathbf{A}\mathbf{X}^{-1}).
$$

Now, suppose that $\mathbf{U}$ is an all zero matrix with a one in the $(i,j)$-th position. We can write,

$$
\frac{\partial y}{\partial x_{ij}} = \lim_{\varepsilon\downarrow 0} \frac{\operatorname{tr}((\mathbf{X}+\varepsilon\mathbf{U})^{-1}\mathbf{A}) - \operatorname{tr}(\mathbf{X}^{-1}\mathbf{A})}{\varepsilon} = -\operatorname{tr}(\mathbf{U}\mathbf{X}^{-1}\mathbf{A}\mathbf{X}^{-1}) = -\left[\mathbf{X}^{-1}\mathbf{A}\mathbf{X}^{-1}\right]_{ji}.
$$

Therefore, $\frac{\partial y}{\partial \mathbf{X}} = -\left(\mathbf{X}^{-1}\mathbf{A}\mathbf{X}^{-1}\right)^\top$.

The following two examples specify multivariate derivatives for the important special cases of linear and quadratic functions.

**Example B.3 (Gradient of a Linear Function).** Let $f(\boldsymbol{x}) = \mathbf{A}\boldsymbol{x}$ for some $m \times n$ constant matrix $\mathbf{A}$. Then, its vector/vector derivative (B.2) is the matrix

$$
\frac{\partial f}{\partial \boldsymbol{x}} = \mathbf{A}^\top. \tag{B.5}
$$

To see this, let $a_{ij}$ denote the $(i,j)$-th element of $\mathbf{A}$, so that

$$
f(\boldsymbol{x}) = \mathbf{A}\boldsymbol{x} = \begin{bmatrix} \sum_{k=1}^n a_{1k}x_k \\ \vdots \\ \sum_{k=1}^n a_{mk}x_k \end{bmatrix}.
$$

To find the $(j,i)$-th element of $\frac{\partial f}{\partial \boldsymbol{x}}$, we differentiate the $i$-th element of $\boldsymbol{f}$ with respect to $x_j$:

$$
\frac{\partial f_i}{\partial x_j} = \frac{\partial}{\partial x_j} \sum_{k=1}^n a_{ik}x_k = a_{ij}.
$$

In other words, the $(i,j)$-th element of $\frac{\partial f}{\partial \boldsymbol{x}}$ is $a_{ji}$, the $(i,j)$-th element of $\mathbf{A}^\top$.

**Example B.4 (Gradient and Hessian of a Quadratic Function).** Let $f(\boldsymbol{x}) = \boldsymbol{x}^\top \mathbf{A}\boldsymbol{x}$ for some $n \times n$ constant matrix $\mathbf{A}$. Then,

$$
\nabla f(\boldsymbol{x}) = (\mathbf{A} + \mathbf{A}^\top)\boldsymbol{x}. \tag{B.6}
$$

It follows immediately that if $\mathbf{A}$ is *symmetric*, that is, $\mathbf{A} = \mathbf{A}^\top$, then $\nabla(\boldsymbol{x}^\top \mathbf{A}\boldsymbol{x}) = 2\mathbf{A}\boldsymbol{x}$ and $\nabla^2(\boldsymbol{x}^\top \mathbf{A}\boldsymbol{x}) = 2\mathbf{A}$.

To prove (B.6), first observe that $f(\boldsymbol{x}) = \boldsymbol{x}^\top \mathbf{A}\boldsymbol{x} = \sum_{i=1}^n \sum_{j=1}^n a_{ij}x_i x_j$, which is a quadratic form in $\boldsymbol{x}$, is real-valued, with

$$
\frac{\partial f}{\partial x_k} = \frac{\partial}{\partial x_k}\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_i x_j = \sum_{j=1}^n a_{kj}x_j + \sum_{i=1}^n a_{ik}x_i.
$$

The first term on the right-hand side is equal to the $k$-th element of $\mathbf{A}\boldsymbol{x}$, whereas the second term equals the $k$-th element of $\boldsymbol{x}^\top \mathbf{A}$, or equivalently the $k$-th element of $\mathbf{A}^\top \boldsymbol{x}$.

## B.1.1 Taylor Expansion

The matrix of Jacobi and the Hessian matrix feature prominently in multidimensional Taylor expansions.

> **Theorem B.1: Multidimensional Taylor Expansions**
>
> Let $\mathcal{X}$ be an open subset of $\mathbb{R}^n$ and let $\boldsymbol{a} \in \mathcal{X}$. If $f : \mathcal{X} \to \mathbb{R}$ is a continuously twice differentiable function with Jacobian matrix $\mathbf{J}_f(\boldsymbol{x})$ and Hessian matrix $\mathbf{H}_f(\boldsymbol{x})$, then for every $\boldsymbol{x} \in \mathcal{X}$ we have the following first- and second-order Taylor expansions:
>
> $$
> f(\boldsymbol{x}) = f(\boldsymbol{a}) + \mathbf{J}_f(\boldsymbol{a})(\boldsymbol{x}-\boldsymbol{a}) + O(\|\boldsymbol{x}-\boldsymbol{a}\|^2) \tag{B.7}
> $$
>
> and
>
> $$
> f(\boldsymbol{x}) = f(\boldsymbol{a}) + \mathbf{J}_f(\boldsymbol{a})(\boldsymbol{x}-\boldsymbol{a}) + \frac{1}{2}(\boldsymbol{x}-\boldsymbol{a})^\top \mathbf{H}_f(\boldsymbol{a})(\boldsymbol{x}-\boldsymbol{a}) + O(\|\boldsymbol{x}-\boldsymbol{a}\|^3) \tag{B.8}
> $$
>
> as $\|\boldsymbol{x}-\boldsymbol{a}\| \to 0$. By dropping the $O$ remainder terms, one obtains the corresponding Taylor approximations.

The result is essentially saying that a smooth enough function behaves locally (in the neighborhood of a point $\boldsymbol{x}$) like a linear and quadratic function. Thus, the gradient or Hessian of an approximating linear or quadratic function is a basic building block of many approximation and optimization algorithms.

**Remark B.1 (Version Without Remainder Terms).** An alternative version of Taylor's theorem states that there exists an $\boldsymbol{a}'$ that lies on the line segment between $\boldsymbol{x}$ and $\boldsymbol{a}$ such that (B.7) and (B.8) hold without remainder terms, with $\mathbf{J}_f(\boldsymbol{a})$ in (B.7) replaced by $\mathbf{J}_f(\boldsymbol{a}')$ and $\mathbf{H}_f(\boldsymbol{a})$ in (B.8) replaced by $\mathbf{H}_f(\boldsymbol{a}')$.

## B.1.2 Chain Rule

Consider the functions $f : \mathbb{R}^k \to \mathbb{R}^m$ and $g : \mathbb{R}^m \to \mathbb{R}^n$. The function $\boldsymbol{x} \mapsto g(f(\boldsymbol{x}))$ is called the **composition** of $g$ and $f$, written as $g \circ f$, and is a function from $\mathbb{R}^k$ to $\mathbb{R}^n$. Suppose $\boldsymbol{y} = f(\boldsymbol{x})$ and $\boldsymbol{z} = g(\boldsymbol{y})$, as in Figure B.1. Let $\mathbf{J}_f(\boldsymbol{x})$ and $\mathbf{J}_g(\boldsymbol{y})$ be the (Fréchet) derivatives of $f$ (at $\boldsymbol{x}$) and $g$ (at $\boldsymbol{y}$), respectively. We may think of $\mathbf{J}_f(\boldsymbol{x})$ as the matrix that describes how, in a neighborhood of $\boldsymbol{x}$, the function $f$ can be approximated by a linear function: $f(\boldsymbol{x}+\boldsymbol{h}) \approx f(\boldsymbol{x}) + \mathbf{J}_f(\boldsymbol{x})\boldsymbol{h}$, and similarly for $\mathbf{J}_g(\boldsymbol{y})$. The well-known **chain rule** of calculus simply states that the derivative of the composition $g \circ f$ is the matrix product of the derivatives of $g$ and $f$; that is,

$$
\mathbf{J}_{g \circ f}(\boldsymbol{x}) = \mathbf{J}_g(\boldsymbol{y})\,\mathbf{J}_f(\boldsymbol{x}).
$$

> **Figure B.1:** Function composition diagram: $\boldsymbol{x} \in \mathbb{R}^k \xrightarrow{f} \boldsymbol{y} \in \mathbb{R}^m \xrightarrow{g} \boldsymbol{z} \in \mathbb{R}^n$, with the composite arrow $g \circ f$ shown going directly from $\boldsymbol{x}$ to $\boldsymbol{z}$. The blue arrows symbolize the linear mappings (i.e., the Jacobians) approximating each function locally.

In terms of our vector/vector derivative notation, we have

$$
\left[\frac{\partial \boldsymbol{z}}{\partial \boldsymbol{x}}\right]^\top = \left[\frac{\partial \boldsymbol{z}}{\partial \boldsymbol{y}}\right]^\top \left[\frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}}\right]^\top
$$

or, more simply,

$$
\frac{\partial \boldsymbol{z}}{\partial \boldsymbol{x}} = \frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}} \frac{\partial \boldsymbol{z}}{\partial \boldsymbol{y}}. \tag{B.9}
$$

In a similar way we can establish a scalar/matrix chain rule. In particular, suppose $\mathbf{X}$ is an $n \times p$ matrix, which is mapped to $\boldsymbol{y} := \mathbf{X}\boldsymbol{\alpha}$ for a fixed $p$-dimensional vector $\boldsymbol{\alpha}$. In turn, $\boldsymbol{y}$ is mapped to a scalar $z := g(\boldsymbol{y})$ for some function $g$. Denote the columns of $\mathbf{X}$ by $\boldsymbol{x}_1,\dots,\boldsymbol{x}_p$. Then,

$$
\boldsymbol{y} = \mathbf{X}\boldsymbol{\alpha} = \sum_{j=1}^p \alpha_j \boldsymbol{x}_j,
$$

and, therefore, $\partial \boldsymbol{y}/\partial \boldsymbol{x}_j = \alpha_j \mathbf{I}_n$. It follows by the chain rule (B.9) that

$$
\frac{\partial z}{\partial \boldsymbol{x}_i} = \frac{\partial \boldsymbol{y}}{\partial \boldsymbol{x}_i} \frac{\partial z}{\partial \boldsymbol{y}} = \alpha_i \mathbf{I}_n \frac{\partial z}{\partial \boldsymbol{y}} = \alpha_i \frac{\partial z}{\partial \boldsymbol{y}}.
$$

Therefore,

$$
\frac{\partial z}{\partial \mathbf{X}} = \left[\frac{\partial z}{\partial \boldsymbol{x}_1}, \dots, \frac{\partial z}{\partial \boldsymbol{x}_p}\right] = \left[\alpha_1 \frac{\partial z}{\partial \boldsymbol{y}}, \dots, \alpha_p \frac{\partial z}{\partial \boldsymbol{y}}\right] = \frac{\partial z}{\partial \boldsymbol{y}}\boldsymbol{\alpha}^\top. \tag{B.10}
$$

**Example B.5 (Derivative of the Log-Determinant).** Suppose we are given a positive definite matrix $\mathbf{A} \in \mathbb{R}^{p\times p}$ and wish to compute the scalar/matrix derivative $\frac{\partial \ln|\mathbf{A}|}{\partial \mathbf{A}}$. The result is

$$
\frac{\partial \ln|\mathbf{A}|}{\partial \mathbf{A}} = \mathbf{A}^{-1}.
$$

To see this, we can reason as follows. By Theorem A.8, we can write $\mathbf{A} = \mathbf{Q}\mathbf{D}\mathbf{Q}^\top$, where $\mathbf{Q}$ is an orthogonal matrix and $\mathbf{D} = \operatorname{diag}(\lambda_1,\dots,\lambda_p)$ is the diagonal matrix of eigenvalues of $\mathbf{A}$. The eigenvalues are strictly positive, since $\mathbf{A}$ is positive definite. Denoting the columns of $\mathbf{Q}$ by $(\boldsymbol{q}_i)$, we have

$$
\lambda_i = \boldsymbol{q}_i^\top \mathbf{A}\boldsymbol{q}_i = \operatorname{tr}(\boldsymbol{q}_i \mathbf{A}\boldsymbol{q}_i^\top), \quad i=1,\dots,p. \tag{B.11}
$$

From the properties of determinants, we have $y := \ln|\mathbf{A}| = \ln|\mathbf{Q}\mathbf{D}\mathbf{Q}^\top| = \ln(|\mathbf{Q}|\,|\mathbf{D}|\,|\mathbf{Q}^\top|) = \ln|\mathbf{D}| = \sum_{i=1}^p \ln \lambda_i$. We can thus write

$$
\frac{\partial \ln|\mathbf{A}|}{\partial \mathbf{A}} = \sum_{i=1}^p \frac{\partial \ln \lambda_i}{\partial \mathbf{A}} = \sum_{i=1}^p \frac{\partial \lambda_i}{\partial \mathbf{A}} \frac{\partial \ln \lambda_i}{\partial \lambda_i} = \sum_{i=1}^p \frac{\partial \lambda_i}{\partial \mathbf{A}} \frac{1}{\lambda_i},
$$

where the second equation follows from the chain rule applied to the function composition $\mathbf{A} \mapsto \lambda_i \mapsto y$. From (B.11) and Example B.1 we have $\partial \lambda_i/\partial \mathbf{A} = \boldsymbol{q}_i \boldsymbol{q}_i^\top$. It follows that

$$
\frac{\partial y}{\partial \mathbf{A}} = \sum_{i=1}^p \boldsymbol{q}_i \boldsymbol{q}_i^\top \frac{1}{\lambda_i} = \mathbf{Q}\mathbf{D}^{-1}\mathbf{Q}^\top = \mathbf{A}^{-1}.
$$
