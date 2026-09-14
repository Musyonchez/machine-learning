---
appendix: A
section: "A.2"
title: "Inner Product"
pdf_pages: "378-379"
---

# A.2 Inner Product

The (Euclidean) *inner product* of two real vectors $\boldsymbol{x} = [x_1,\dots,x_n]^\top$ and $\boldsymbol{y} = [y_1,\dots,y_n]^\top$ is defined as the number

$$\langle \boldsymbol{x}, \boldsymbol{y}\rangle = \sum_{i=1}^n x_i y_i = \boldsymbol{x}^\top \boldsymbol{y}.$$

Here $\boldsymbol{x}^\top\boldsymbol{y}$ is the matrix multiplication of the $(1\times n)$ matrix $\boldsymbol{x}^\top$ and the $(n\times 1)$ matrix $\boldsymbol{y}$. The inner product induces a geometry on the linear space $\mathbb{R}^n$, allowing for the definition of length, angle, and so on. The inner product satisfies the following properties:

1. $\langle \alpha\boldsymbol{x} + \beta\boldsymbol{y}, \boldsymbol{z}\rangle = \alpha\langle\boldsymbol{x},\boldsymbol{z}\rangle + \beta\langle\boldsymbol{y},\boldsymbol{z}\rangle$;
2. $\langle\boldsymbol{x},\boldsymbol{y}\rangle = \langle\boldsymbol{y},\boldsymbol{x}\rangle$;
3. $\langle\boldsymbol{x},\boldsymbol{x}\rangle \ge 0$;
4. $\langle\boldsymbol{x},\boldsymbol{x}\rangle = 0$ if and only if $\boldsymbol{x} = \boldsymbol{0}$.

Vectors $\boldsymbol{x}$ and $\boldsymbol{y}$ are called *perpendicular* (or *orthogonal*) if $\langle\boldsymbol{x},\boldsymbol{y}\rangle = 0$. The *Euclidean norm* (or length) of a vector $\boldsymbol{x}$ is defined as

$$\|\boldsymbol{x}\| = \sqrt{x_1^2 + \cdots + x_n^2} = \sqrt{\langle\boldsymbol{x},\boldsymbol{x}\rangle}.$$

If $\boldsymbol{x}$ and $\boldsymbol{y}$ are perpendicular, then *Pythagoras' theorem* holds:

$$\|\boldsymbol{x}+\boldsymbol{y}\|^2 = \langle \boldsymbol{x}+\boldsymbol{y},\ \boldsymbol{x}+\boldsymbol{y}\rangle = \langle\boldsymbol{x},\boldsymbol{x}\rangle + 2\langle\boldsymbol{x},\boldsymbol{y}\rangle + \langle\boldsymbol{y},\boldsymbol{y}\rangle = \|\boldsymbol{x}\|^2 + \|\boldsymbol{y}\|^2. \tag{A.5}$$

A basis $\{\boldsymbol{v}_1,\dots,\boldsymbol{v}_n\}$ of $\mathbb{R}^n$ in which all the vectors are pairwise perpendicular and have norm 1 is called an *orthonormal* (short for orthogonal and normalized) basis. For example, the standard basis is orthonormal.

**Theorem A.3: Orthonormal Basis Representation**

> If $\{\boldsymbol{v}_1,\dots,\boldsymbol{v}_n\}$ is an orthonormal basis of $\mathbb{R}^n$, then any vector $\boldsymbol{x} \in \mathbb{R}^n$ can be expressed as
> $$\boldsymbol{x} = \langle\boldsymbol{x},\boldsymbol{v}_1\rangle\boldsymbol{v}_1 + \cdots + \langle\boldsymbol{x},\boldsymbol{v}_n\rangle\boldsymbol{v}_n. \tag{A.6}$$

*Proof:* Observe that, because the $\{\boldsymbol{v}_i\}$ form a basis, there exist unique $\alpha_1,\dots,\alpha_n$ such that $\boldsymbol{x} = \alpha_1\boldsymbol{v}_1 + \cdots + \alpha_n\boldsymbol{v}_n$. By the linearity of the inner product and the orthonormality of the $\{\boldsymbol{v}_i\}$ it follows that $\langle\boldsymbol{x},\boldsymbol{v}_j\rangle = \langle \sum_i \alpha_i\boldsymbol{v}_i, \boldsymbol{v}_j\rangle = \alpha_j$. $\square$

An $n\times n$ matrix $\mathbf{V}$ whose columns form an orthonormal basis is called an *orthogonal matrix*.[^1] Note that for an orthogonal matrix $\mathbf{V} = [\boldsymbol{v}_1,\dots,\boldsymbol{v}_n]$, we have

$$\mathbf{V}^\top\mathbf{V} = \begin{bmatrix}\boldsymbol{v}_1^\top\\ \boldsymbol{v}_2^\top\\ \vdots\\ \boldsymbol{v}_n^\top\end{bmatrix}[\boldsymbol{v}_1,\boldsymbol{v}_2,\dots,\boldsymbol{v}_n] = \begin{bmatrix}\boldsymbol{v}_1^\top\boldsymbol{v}_1 & \boldsymbol{v}_1^\top\boldsymbol{v}_2 & \dots & \boldsymbol{v}_1^\top\boldsymbol{v}_n\\ \vdots & \vdots & \vdots & \vdots\\ \boldsymbol{v}_n^\top\boldsymbol{v}_1 & \boldsymbol{v}_n^\top\boldsymbol{v}_2 & \dots & \boldsymbol{v}_n^\top\boldsymbol{v}_n\end{bmatrix} = \mathbf{I}_n.$$

Hence, $\mathbf{V}^{-1} = \mathbf{V}^\top$. Note also that an orthogonal transformation is *length preserving*; that is, $\mathbf{V}\boldsymbol{x}$ has the same length as $\boldsymbol{x}$. This follows from

$$\|\mathbf{V}\boldsymbol{x}\|^2 = \langle \mathbf{V}\boldsymbol{x}, \mathbf{V}\boldsymbol{x}\rangle = \boldsymbol{x}^\top\mathbf{V}^\top\mathbf{V}\boldsymbol{x} = \boldsymbol{x}^\top\boldsymbol{x} = \|\boldsymbol{x}\|^2.$$

[^1]: The qualifier "orthogonal" for such matrices has been fixed by history. A better term would have been "orthonormal".
