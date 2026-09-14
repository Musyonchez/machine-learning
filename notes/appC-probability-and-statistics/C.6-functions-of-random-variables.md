---
appendix: C
section: "C.6"
title: "Functions of Random Variables"
pdf_pages: "449-452"
---

## C.6 Functions of Random Variables

Let $\boldsymbol{x} = [x_1, \ldots, x_n]^\top$ be a column vector in $\mathbb{R}^n$ and $\mathbf{A}$ an $m \times n$ matrix. The mapping $\boldsymbol{x} \mapsto \boldsymbol{z}$, with $\boldsymbol{z} = \mathbf{A}\boldsymbol{x}$, is a linear transformation, as discussed in Section A.1 (p.355). Now consider a random vector $\boldsymbol{X} = [X_1, \ldots, X_n]^\top$ and let $\boldsymbol{Z} := \mathbf{A}\boldsymbol{X}$. Then $\boldsymbol{Z}$ is a random vector in $\mathbb{R}^m$. The following theorem details how the distribution of $\boldsymbol{Z}$ is related to that of $\boldsymbol{X}$.

> **Theorem C.3: Linear Transformation**
>
> If $\boldsymbol{X}$ has an expectation vector $\boldsymbol{\mu}_X$ and covariance matrix $\boldsymbol{\Sigma}_X$, then the expectation vector of $\boldsymbol{Z}$ is
>
> $$\boldsymbol{\mu}_Z = \mathbf{A}\boldsymbol{\mu}_X \tag{C.20}$$
>
> and the covariance matrix of $\boldsymbol{Z}$ is
>
> $$\boldsymbol{\Sigma}_Z = \mathbf{A}\boldsymbol{\Sigma}_X \mathbf{A}^\top. \tag{C.21}$$
>
> If, in addition, $\mathbf{A}$ is an invertible $n \times n$ matrix and $\boldsymbol{X}$ is a continuous random vector with pdf $f_X$, then the pdf of the continuous random vector $\boldsymbol{Z} = \mathbf{A}\boldsymbol{X}$ is given by
>
> $$f_Z(\boldsymbol{z}) = \frac{f_X(\mathbf{A}^{-1}\boldsymbol{z})}{|\det(\mathbf{A})|}, \quad \boldsymbol{z} \in \mathbb{R}^n, \tag{C.22}$$
>
> where $|\det(\mathbf{A})|$ denotes the absolute value of the determinant of $\mathbf{A}$.

*Proof:* We have $\boldsymbol{\mu}_Z = \mathbb{E}\boldsymbol{Z} = \mathbb{E}[\mathbf{A}\boldsymbol{X}] = \mathbf{A}\,\mathbb{E}\boldsymbol{X} = \mathbf{A}\boldsymbol{\mu}_X$ and

$$\boldsymbol{\Sigma}_Z = \mathbb{E}[(\boldsymbol{Z}-\boldsymbol{\mu}_Z)(\boldsymbol{Z}-\boldsymbol{\mu}_Z)^\top] = \mathbb{E}[\mathbf{A}(\boldsymbol{X}-\boldsymbol{\mu}_X)(\mathbf{A}(\boldsymbol{X}-\boldsymbol{\mu}_X))^\top] = \mathbf{A}\,\mathbb{E}[(\boldsymbol{X}-\boldsymbol{\mu}_X)(\boldsymbol{X}-\boldsymbol{\mu}_X)^\top]\mathbf{A}^\top = \mathbf{A}\boldsymbol{\Sigma}_X\mathbf{A}^\top.$$

For $\mathbf{A}$ invertible and $\boldsymbol{X}$ continuous (as opposed to discrete), let $\boldsymbol{z} = \mathbf{A}\boldsymbol{x}$ and $\boldsymbol{x} = \mathbf{A}^{-1}\boldsymbol{z}$. Consider the $n$-dimensional cube $C = [z_1, z_1+h] \times \cdots \times [z_n, z_n+h]$. Then,

$$\mathbb{P}[\boldsymbol{Z} \in C] \approx h^n f_Z(\boldsymbol{z}),$$

by definition of the joint density of $\boldsymbol{Z}$. Let $D$ be the image of $C$ under $\mathbf{A}^{-1}$ — that is, all points $\boldsymbol{x}$ such that $\mathbf{A}\boldsymbol{x} \in C$. Recall from Section A.1 (p.355) that any matrix $B$ linearly transforms an $n$-dimensional rectangle with volume $V$ into an $n$-dimensional parallelepiped with volume $V|\det(B)|$. Thus, in addition to the above expression for $\mathbb{P}[\boldsymbol{Z}\in C]$, we also have

$$\mathbb{P}[\boldsymbol{Z}\in C] = \mathbb{P}[\boldsymbol{X}\in D] \approx h^n |\det(\mathbf{A}^{-1})| f_X(\boldsymbol{x}) = h^n |\det(\mathbf{A})|^{-1} f_X(\boldsymbol{x}).$$

Equating these two expressions for $\mathbb{P}[\boldsymbol{Z}\in C]$, dividing both sides by $h^n$, and letting $h$ go to 0, we obtain (C.22). $\square$

For a generalization of the linear transformation rule (C.22), consider an arbitrary mapping $\boldsymbol{x} \mapsto \boldsymbol{g}(\boldsymbol{x})$, written out:

$$\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} \mapsto \begin{bmatrix} g_1(\boldsymbol{x}) \\ g_2(\boldsymbol{x}) \\ \vdots \\ g_n(\boldsymbol{x}) \end{bmatrix}.$$

> **Theorem C.4: Transformation Rule**
>
> Let $\boldsymbol{X}$ be an $n$-dimensional vector of continuous random variables with pdf $f_X$. Let $\boldsymbol{Z} = \boldsymbol{g}(\boldsymbol{X})$, where $\boldsymbol{g}$ is an invertible mapping with inverse $\boldsymbol{g}^{-1}$ and *matrix of Jacobi* $\mathbf{J}_g$; that is, the matrix of partial derivatives of $\boldsymbol{g}$. Then, at $\boldsymbol{z} = \boldsymbol{g}(\boldsymbol{x})$ the random vector $\boldsymbol{Z}$ has pdf
>
> $$f_Z(\boldsymbol{z}) = \frac{f_X(\boldsymbol{x})}{|\det(\mathbf{J}_g(\boldsymbol{x}))|} = f_X(\boldsymbol{g}^{-1}(\boldsymbol{z}))\, |\det(\mathbf{J}_{g^{-1}}(\boldsymbol{z}))|, \quad \boldsymbol{z} \in \mathbb{R}^n. \tag{C.23}$$

*Proof:* For a fixed $\boldsymbol{x}$, let $\boldsymbol{z} = \boldsymbol{g}(\boldsymbol{x})$; and thus $\boldsymbol{x} = \boldsymbol{g}^{-1}(\boldsymbol{z})$. In the neighborhood of $\boldsymbol{x}$, the function $\boldsymbol{g}$ behaves like a linear function, in the sense that $\boldsymbol{g}(\boldsymbol{x}+\boldsymbol{\delta}) \approx \boldsymbol{g}(\boldsymbol{x}) + \mathbf{J}_g(\boldsymbol{x})\boldsymbol{\delta}$ for small vectors $\boldsymbol{\delta}$; see also Section B.1 (p.397). Consequently, an infinitesimally small $n$-dimensional rectangle at $\boldsymbol{x}$ with volume $V$ is transformed into an infinitesimally small $n$-dimensional parallelepiped at $\boldsymbol{z}$ with volume $V|\det(\mathbf{J}_g(\boldsymbol{x}))|$. Now, as in the proof of the linear case, let $C$ be a small cube around $\boldsymbol{z} = \boldsymbol{g}(\boldsymbol{x})$ with volume $h^n$. Let $D$ be the image of $C$ under $\boldsymbol{g}^{-1}$. Then,

$$h^n f_Z(\boldsymbol{z}) \approx \mathbb{P}[\boldsymbol{Z}\in C] \approx h^n |\det(\mathbf{J}_{g^{-1}}(\boldsymbol{z}))| f_X(\boldsymbol{x}),$$

and since $|\det(\mathbf{J}_{g^{-1}}(\boldsymbol{z}))| = 1/|\det(\mathbf{J}_g(\boldsymbol{x}))|$, (C.23) follows as $h$ goes to 0. $\square$

> Typically, in coordinate transformations it is $\boldsymbol{g}^{-1}$ that is given — that is, an expression for $\boldsymbol{x}$ as a function of $\boldsymbol{z}$.

**Example C.2 (Polar Transform).** Suppose $X, Y$ are independent and have standard normal distribution. The joint pdf is

$$f_{X,Y}(x,y) = \frac{1}{2\pi}\mathrm{e}^{-\frac{1}{2}(x^2+y^2)}, \quad (x,y)\in\mathbb{R}^2.$$

In polar coordinates we have

$$X = R\cos\Theta \quad \text{and} \quad Y = R\sin\Theta, \tag{C.24}$$

where $R \geqslant 0$ is the radius and $\Theta \in [0, 2\pi)$ the angle of the point $(X,Y)$. What is the joint pdf of $R$ and $\Theta$? By the radial symmetry of the bivariate normal distribution, we would expect $\Theta$ to be uniform on $(0, 2\pi)$. But what is the pdf of $R$? To work out the joint pdf, consider the inverse transformation $\boldsymbol{g}^{-1}$, defined by

$$\begin{bmatrix} r \\ \theta \end{bmatrix} \xrightarrow{\ g^{-1}\ } \begin{bmatrix} r\cos\theta \\ r\sin\theta \end{bmatrix} = \begin{bmatrix} x \\ y \end{bmatrix}.$$

The corresponding matrix of Jacobi is

$$\mathbf{J}_{g^{-1}}(r,\theta) = \begin{bmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{bmatrix},$$

which has determinant $r$. Since $x^2 + y^2 = r^2(\cos^2\theta + \sin^2\theta) = r^2$, it follows by the transformation rule (C.23) that the joint pdf of $R$ and $\Theta$ is given by

$$f_{R,\Theta}(r,\theta) = f_{X,Y}(x,y)\, r = \frac{1}{2\pi}\mathrm{e}^{-\frac{1}{2}r^2} r, \quad \theta \in (0, 2\pi), \quad r \geqslant 0.$$

By integrating out $\theta$ and $r$, respectively, we find $f_R(r) = r\, \mathrm{e}^{-r^2/2}$ and $f_\Theta(\theta) = 1/(2\pi)$. Since $f_{R,\Theta}$ is the product of $f_R$ and $f_\Theta$, the random variables $R$ and $\Theta$ are independent. $\blacksquare$
