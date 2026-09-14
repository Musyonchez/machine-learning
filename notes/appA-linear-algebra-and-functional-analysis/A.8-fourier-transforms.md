---
appendix: A
section: "A.8"
title: "Fourier Transforms"
pdf_pages: "408-414"
---

# A.8 Fourier Transforms

We will now briefly introduce the Fourier transform. Before doing so, we will extend the concept of $L^2$ space of real-valued functions as follows (see book p. 385).

**Definition A.5: $L^p$ Space**

> Let $X$ be a subset of $\mathbb{R}^d$ with measure $\mu(\mathrm{d}\boldsymbol{x}) = w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ and $p \in [1,\infty)$. Then $L^p(X,\mu)$ is the linear space of functions from $X$ to $\mathbb{C}$ that satisfy
> $$\int_X |f(\boldsymbol{x})|^p\, w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} < \infty. \tag{A.38}$$
> When $p=2$, $L^2(X,\mu)$ is in fact a Hilbert space equipped with inner product
> $$\langle f,g\rangle = \int_X f(\boldsymbol{x})\,\overline{g(\boldsymbol{x})}\,w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}. \tag{A.39}$$

We are now in a position to define the Fourier transform (with respect to the Lebesgue measure). Note that in the following Definitions A.6 and A.7 we have chosen a particular convention. Equivalent (but not identical) definitions exist that include scaling constants $(2\pi)^d$ or $(2\pi)^{-d}$ and where $-2\pi\boldsymbol{t}$ is replaced with $2\pi\boldsymbol{t}$, $\boldsymbol{t}$, or $-\boldsymbol{t}$.

**Definition A.6: (Multivariate) Fourier Transform**

> The *Fourier transform* $\mathcal{F}[f]$ of a (real- or complex-valued) function $f \in L^1(\mathbb{R}^d)$ is the function $\widetilde f$ defined as
> $$\widetilde f(\boldsymbol{t}) := \int_{\mathbb{R}^d} \mathrm{e}^{-\mathrm{i}\,2\pi \boldsymbol{t}^\top\boldsymbol{x}} f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}, \quad \boldsymbol{t} \in \mathbb{R}^d.$$

The Fourier transform $\widetilde f$ is continuous, uniformly bounded (since $f \in L^1(\mathbb{R}^d)$ implies that $|\widetilde f(\boldsymbol{t})| \le \int_{\mathbb{R}^d} |f(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x} < \infty$), and satisfies $\lim_{\|\boldsymbol{t}\|\to\infty} \widetilde f(\boldsymbol{t}) = 0$ (a result known as the *Riemann–Lebesgue lemma*). However, $|\widetilde f|$ does not necessarily have a finite integral. A simple example in $\mathbb{R}^1$ is the Fourier transform of $f(x) = \mathbb{1}\{-1/2 < x < 1/2\}$. Then $\widetilde f(t) = \sin(\pi t)/(\pi t) = \operatorname{sinc}(\pi t)$, which is not absolutely integrable.

**Definition A.7: (Multivariate) Inverse Fourier Transform**

> The *inverse Fourier transform* $\mathcal{F}^{-1}[\widetilde f]$ of a (real- or complex-valued) function $\widetilde f \in L^1(\mathbb{R}^d)$ is the function $\check f$ defined as
> $$\check f(\boldsymbol{x}) := \int_{\mathbb{R}^d} \mathrm{e}^{\mathrm{i}\,2\pi \boldsymbol{t}^\top\boldsymbol{x}} \widetilde f(\boldsymbol{t})\,\mathrm{d}\boldsymbol{t}, \quad \boldsymbol{x} \in \mathbb{R}^d.$$

As one would hope, it holds that if $f$ and $\mathcal{F}[f]$ are both in $L^1(\mathbb{R}^d)$, then $f = \mathcal{F}^{-1}[\mathcal{F}[f]]$ almost everywhere.

The Fourier transform enjoys many interesting and useful properties, some of which we list below.

1. *Linearity*: For $f,g \in L^1(\mathbb{R}^d)$ and constants $a,b \in \mathbb{R}$,
   $$\mathcal{F}[af+bg] = a\mathcal{F}[f]+b\mathcal{F}[g].$$

2. *Space Shifting and Scaling*: Let $\mathbf{A} \in \mathbb{R}^{d\times d}$ be an invertible matrix and $\boldsymbol{b} \in \mathbb{R}^d$ a constant vector. Let $f \in L^1(\mathbb{R}^d)$ and define $h(\boldsymbol{x}) := f(\mathbf{A}\boldsymbol{x}+\boldsymbol{b})$. Then
   $$\mathcal{F}[h](\boldsymbol{t}) = \mathrm{e}^{\mathrm{i}\,2\pi(\mathbf{A}^{-\top}\boldsymbol{t})^\top\boldsymbol{b}}\,\widetilde f(\mathbf{A}^{-\top}\boldsymbol{t})/|\det(\mathbf{A})|,$$
   where $\mathbf{A}^{-\top} := (\mathbf{A}^\top)^{-1} = (\mathbf{A}^{-1})^\top$.

3. *Frequency Shifting and Scaling*: Let $\mathbf{A} \in \mathbb{R}^{d\times d}$ be an invertible matrix and $\boldsymbol{b} \in \mathbb{R}^d$ a constant vector. Let $f \in L^1(\mathbb{R}^d)$ and define
   $$h(\boldsymbol{x}) := \mathrm{e}^{-\mathrm{i}\,2\pi \boldsymbol{b}^\top\mathbf{A}^{-\top}\boldsymbol{x}} f(\mathbf{A}^{-\top}\boldsymbol{x})/|\det(\mathbf{A})|.$$
   Then $\mathcal{F}[h](\boldsymbol{t}) = \widetilde f(\mathbf{A}\boldsymbol{t}+\boldsymbol{b})$.

4. *Differentiation*: Let $f \in L^1(\mathbb{R}^d) \cap C^1(\mathbb{R}^d)$ and let $f_k := \partial f/\partial x_k$ be the partial derivative of $f$ with respect to $x_k$. If $f_k \in L^1(\mathbb{R}^d)$ for $k=1,\dots,d$, then
   $$\mathcal{F}[f_k](\boldsymbol{t}) = (\mathrm{i}\,2\pi t_k)\,\widetilde f(\boldsymbol{t}).$$

5. *Convolution*: Let $f,g \in L^1(\mathbb{R}^d)$ be real or complex valued functions. Their convolution, $f*g$, is defined as
   $$(f*g)(\boldsymbol{x}) = \int_{\mathbb{R}^d} f(\boldsymbol{y})\,g(\boldsymbol{x}-\boldsymbol{y})\,\mathrm{d}\boldsymbol{y},$$
   and is also in $L^1(\mathbb{R}^d)$. Moreover, the Fourier transform satisfies
   $$\mathcal{F}[f*g] = \mathcal{F}[f]\mathcal{F}[g].$$

6. *Duality*: Let $f$ and $\mathcal{F}[f]$ both be in $L^1(\mathbb{R}^d)$. Then $\mathcal{F}[\mathcal{F}[f]](\boldsymbol{t}) = f(-\boldsymbol{t})$.

7. *Product Formula*: Let $f,g \in L^1(\mathbb{R}^d)$ and denote by $\widetilde f, \widetilde g$ their respective Fourier transforms. Then $\widetilde f g,\ f\widetilde g \in L^1(\mathbb{R}^d)$, and
   $$\int_{\mathbb{R}^d} \widetilde f(\boldsymbol{z})\,g(\boldsymbol{z})\,\mathrm{d}\boldsymbol{z} = \int_{\mathbb{R}^d} f(\boldsymbol{z})\,\widetilde g(\boldsymbol{z})\,\mathrm{d}\boldsymbol{z}.$$

There are many additional properties which hold if $f \in L^2(\mathbb{R}^d)$. In particular, if $f,g \in L^1(\mathbb{R}^d)\cap L^2(\mathbb{R}^d)$, then $\widetilde f,\widetilde g \in L^2(\mathbb{R}^d)$ and $\langle\widetilde f,\widetilde g\rangle = \langle f,g\rangle$, a result often known as *Parseval's formula*. Putting $g=f$ gives the result often referred to as *Plancherel's theorem*.

The Fourier transform can be extended in several ways, in the first instance to functions in $L^2(\mathbb{R}^d)$ by continuity. A substantial extension of the theory is realized by replacing integration with respect to the Lebesgue measure (i.e., $\int_{\mathbb{R}^d}\cdots\mathrm{d}\boldsymbol{x}$) with integration with respect to a (finite Borel) measure $\mu$ (i.e., $\int_{\mathbb{R}^d}\cdots\mu(\mathrm{d}\boldsymbol{x})$). Moreover, there is a close connection between the Fourier transform and characteristic functions arising in probability theory (see book p. 441). Indeed, if $\boldsymbol{X}$ is a random vector with pdf $f$, then its characteristic function $\psi$ satisfies
$$\psi(\boldsymbol{t}) := \mathbb{E}\,\mathrm{e}^{\mathrm{i}\,\boldsymbol{t}^\top\boldsymbol{X}} = \mathcal{F}[f](-\boldsymbol{t}/(2\pi)).$$

## A.8.1 Discrete Fourier Transform

Here, we introduce the (univariate) discrete Fourier transform, which can be viewed as a special case of the Fourier transform introduced in Definition A.6, where $d=1$, integration is with respect to the counting measure, and $f(x) = 0$ for $x<0$ and $x>(n-1)$.

**Definition A.8: Discrete Fourier Transform**

> The *discrete Fourier transform* (DFT) of a vector $\boldsymbol{x} = [x_0,\dots,x_{n-1}]^\top \in \mathbb{C}^n$ is the vector $\widetilde{\boldsymbol{x}} = [\widetilde x_0,\dots,\widetilde x_{n-1}]^\top$ whose elements are given by
> $$\widetilde x_t = \sum_{s=0}^{n-1} \omega^{st} x_s, \quad t=0,\dots,n-1, \tag{A.40}$$
> where $\omega = \exp(-\mathrm{i}\,2\pi/n)$.

In other words, $\widetilde{\boldsymbol{x}}$ is obtained from $\boldsymbol{x}$ via the linear transformation
$$\widetilde{\boldsymbol{x}} = \mathbf{F}\boldsymbol{x},$$
where
$$\mathbf{F} = \begin{bmatrix}1&1&1&\dots&1\\1&\omega&\omega^2&\dots&\omega^{n-1}\\1&\omega^2&\omega^4&\dots&\omega^{2(n-1)}\\\vdots&\vdots&\vdots&\ddots&\vdots\\1&\omega^{n-1}&\omega^{2(n-1)}&\dots&\omega^{(n-1)^2}\end{bmatrix}.$$

The matrix $\mathbf{F}$ is a so-called *Vandermonde matrix*, and is clearly symmetric (i.e., $\mathbf{F} = \mathbf{F}^\top$). Moreover, $\mathbf{F}/\sqrt{n}$ is in fact a unitary matrix and hence its inverse is simply its complex conjugate $\overline{\mathbf{F}}/\sqrt{n}$. Thus, $\mathbf{F}^{-1} = \overline{\mathbf{F}}/n$ and we have that the *inverse discrete Fourier transform* (IDFT) is given by
$$x_t = \frac{1}{n}\sum_{s=0}^{n-1} \omega^{-st}\widetilde x_s, \quad t=0,\dots,n-1, \tag{A.41}$$
or in terms of matrices and vectors,
$$\boldsymbol{x} = \overline{\mathbf{F}}\widetilde{\boldsymbol{x}}/n.$$

Observe that the IDFT of a vector $\boldsymbol{y}$ is related to the DFT of its complex conjugate $\overline{\boldsymbol{y}}$, since
$$\overline{\mathbf{F}}\boldsymbol{y}/n = \overline{\mathbf{F}\overline{\boldsymbol{y}}}/n.$$
Consequently, an IDFT can be computed via a DFT.

There is a close connection between circulant matrices $\mathbf{C}$ and the DFT. To make this connection concrete, let $\mathbf{C}$ be the circulant matrix corresponding to the vector $\boldsymbol{c} \in \mathbb{C}^n$ and denote by $\boldsymbol{f}_t$ the $t$-th column of the discrete Fourier matrix $\mathbf{F}$, $t=0,1,\dots,n-1$. Then, the $s$-th element of $\mathbf{C}\boldsymbol{f}_t$ is
$$\sum_{k=0}^{n-1} c_{(s-k)\bmod n}\,\omega^{tk} = \sum_{y=0}^{n-1} c_y\,\omega^{t(s-y)} = \underbrace{\omega^{ts}}_{s\text{-th element of }\boldsymbol{f}_t}\ \underbrace{\sum_{y=0}^{n-1} c_y\,\omega^{-ty}}_{\lambda_s}.$$

Hence, the eigenvalues of $\mathbf{C}$ are
$$\lambda_t = \boldsymbol{c}^\top\overline{\boldsymbol{f}}_t, \quad t=0,1,\dots,n-1,$$
with corresponding eigenvectors $\boldsymbol{f}_t$. Collecting the eigenvalues into the vector $\boldsymbol{\lambda} = [\lambda_0,\dots,\lambda_{n-1}]^\top = \overline{\mathbf{F}}\boldsymbol{c}$, we therefore have the eigen-decomposition
$$\mathbf{C} = \mathbf{F}\,\operatorname{diag}(\boldsymbol{\lambda})\,\overline{\mathbf{F}}/n.$$

Consequently, one can compute the *circular convolution* of a vector $\boldsymbol{a} = [a_1,\dots,a_n]^\top$ and $\boldsymbol{c} = [c_0,\dots,c_{n-1}]^\top$ by a series of DFTs as follows. Construct the circulant matrix $\mathbf{C}$ corresponding to $\boldsymbol{c}$. Then, the circular convolution of $\boldsymbol{a}$ and $\boldsymbol{c}$ is given by $\boldsymbol{y} = \mathbf{C}\boldsymbol{a}$. Proceed in four steps:

1. Compute $\boldsymbol{z} = \overline{\mathbf{F}}\boldsymbol{a}/n$.
2. Compute $\boldsymbol{\lambda} = \overline{\mathbf{F}}\boldsymbol{c}$.
3. Compute $\boldsymbol{p} = \boldsymbol{z}\odot\boldsymbol{\lambda} = [z_1\lambda_0,\dots,z_n\lambda_{n-1}]^\top$.
4. Compute $\boldsymbol{y} = \mathbf{F}\boldsymbol{p}$.

Steps 1 and 2 are (up to constants) in the form of an IDFT, and step 4 is in the form of a DFT. These are computable via the FFT (Section A.8.2) in $O(n\ln n)$ time (see book p. 394). Step 3 is a dot product computable in $O(n)$ time. Thus, the circular convolution can be computed with the aid of the FFT in $O(n\ln n)$ time.

One can also efficiently compute the product of an $n\times n$ Toeplitz matrix $\mathbf{T}$ and an $n\times 1$ vector $\boldsymbol{a}$ in $O(n\ln n)$ time by embedding $\mathbf{T}$ into a circulant matrix $\mathbf{C}$ of size $2n\times 2n$. Namely, define
$$\mathbf{C} = \begin{bmatrix}\mathbf{T}&\mathbf{B}\\\mathbf{B}&\mathbf{T}\end{bmatrix},$$
where
$$\mathbf{B} = \begin{bmatrix}0&t_{n-1}&\cdots&t_2&t_1\\t_{-(n-1)}&0&t_{n-1}&&t_2\\\vdots&t_{-(n-1)}&0&\ddots&\vdots\\t_{-2}&&\ddots&\ddots&t_{n-1}\\t_{-1}&t_{-2}&\cdots&t_{-(n-1)}&0\end{bmatrix}.$$

Then a product of the form $\boldsymbol{y} = \mathbf{T}\boldsymbol{a}$ can be computed in $O(n\ln n)$ time, since we may write
$$\mathbf{C}\begin{bmatrix}\boldsymbol{a}\\\boldsymbol{0}\end{bmatrix} = \begin{bmatrix}\mathbf{T}&\mathbf{B}\\\mathbf{B}&\mathbf{T}\end{bmatrix}\begin{bmatrix}\boldsymbol{a}\\\boldsymbol{0}\end{bmatrix} = \begin{bmatrix}\mathbf{T}\boldsymbol{a}\\\mathbf{B}\boldsymbol{a}\end{bmatrix}.$$

The left-hand side is a product of a $2n\times 2n$ circulant matrix with vector of length $2n$, and so can be computed in $O(n\ln n)$ time via the FFT, as previously discussed.

Conceptually, one can also solve equations of the form $\mathbf{C}\boldsymbol{x} = \boldsymbol{b}$ for a given vector $\boldsymbol{b}\in\mathbb{C}^n$ and circulant matrix $\mathbf{C}$ (corresponding to $\boldsymbol{c}\in\mathbb{C}^n$, assuming all its eigenvalues are non-zero) via the following four steps:

1. Compute $\boldsymbol{z} = \overline{\mathbf{F}}\boldsymbol{b}/n$.
2. Compute $\boldsymbol{\lambda} = \overline{\mathbf{F}}\boldsymbol{c}$.
3. Compute $\boldsymbol{p} = \boldsymbol{z}/\boldsymbol{\lambda} = [z_1/\lambda_0,\dots,z_n/\lambda_{n-1}]^\top$.
4. Compute $\boldsymbol{x} = \mathbf{F}\boldsymbol{p}$.

Once again, Steps 1 and 2 are (up to constants) in the form of an IDFT, and Step 4 is in the form of a DFT, all of which are computable via the FFT in $O(n\ln n)$ time, and Step 3 is computable in $O(n)$ time, meaning the solution $\boldsymbol{x}$ can be computed using the FFT in $O(n\ln n)$ time.

## A.8.2 Fast Fourier Transform

The *fast Fourier transform* (FFT) is a numerical algorithm for the fast evaluation of (A.40) and (A.41). By using a divide-and-conquer strategy, the algorithm reduces the computational complexity from $O(n^2)$ (for the naïve evaluation of the linear transformation) to $O(n\ln n)$ [60].

The essence of the algorithm lies in the following observation. Suppose $n = r_1r_2$. Then one can express any index $t$ appearing in (A.40) via a pair $(t_0,t_1)$, with $t = t_1r_1+t_0$, where $t_0\in\{0,1,\dots,r_1-1\}$ and $t_1\in\{0,1,\dots,r_2-1\}$. Similarly, one can express any index $s$ appearing in (A.40) via a pair $(s_0,s_1)$, with $s = s_1r_2+s_0$, where $s_0\in\{0,1,\dots,r_2-1\}$ and $s_1\in\{0,1,\dots,r_1-1\}$.

Identifying $\widetilde x_t \equiv \widetilde x_{t_1,t_0}$ and $x_s \equiv x_{s_1,s_0}$, we may re-express (A.40) as
$$\widetilde x_{t_1,t_0} = \sum_{s_0=0}^{r_2-1} \omega^{s_0t}\sum_{s_1=0}^{r_1-1}\omega^{s_1r_2t}x_{s_1,s_0}, \quad t_0=0,\dots,r_1-1,\ t_1=0,\dots,r_2-1. \tag{A.42}$$

Observe that $\omega^{s_1r_2t} = \omega^{s_1r_2t_0}$ (because $\omega^{r_1r_2}=1$), so that the inner sum over $s_1$ depends only on $s_0$ and $t_0$. Define
$$y_{t_0,s_0} := \sum_{s_1=0}^{r_1-1} \omega^{s_1r_2t_0}x_{s_1,s_0}, \quad t_0=0,\dots,r_1-1,\ s_0=0,\dots,r_2-1.$$

Computing each $y_{t_0,s_0}$ requires $O(nr_1)$ operations. In terms of the $\{y_{t_0,s_0}\}$, (A.42) can be written as
$$\widetilde x_{t_1,t_0} = \sum_{s_0=0}^{r_2-1} \omega^{s_0t}\,y_{t_0,s_0}, \quad t_1=0,1,\dots,r_2-1,\ t_0=0,1,\dots,r_1-1,$$

requiring $O(nr_2)$ operations to compute. Thus, calculating the DFT using this two-step procedure requires $O(n(r_1+r_2))$ operations, rather than $O(n^2)$.

Now supposing $n = r_1r_2\cdots r_m$, repeated application the above divide-and-conquer idea yields an $m$-step procedure requiring $O(n(r_1+r_2+\cdots+r_m))$ operations. In particular, if $r_k = r$ for all $k=1,2,\dots,m$, we have that $n = r^m$ and $m = \log_r n$, so that the total number of operations is $O(rnm) \equiv O(rn\log_r(n))$. Typically, the *radix* $r$ is a small (not necessarily prime) number, for instance $r=2$.

## Further Reading

*(Appendix A closing remarks, book p. 396.)* A good reference book on matrix computations is Golub and Van Loan [52]. A useful list of many common vector and matrix calculus identities can be found in [95]. Strang's introduction to linear algebra [116] is a classic textbook, and his recent book [117] combines linear algebra with the foundations of deep learning. Fast reliable algorithms for matrices with structure can be found in [64]. Kolmogorov and Fomin's masterpiece on the theory of functions and functional analysis [67] still provides one of the best introductions to the topic. A popular choice for an advanced course in functional analysis is Rudin [106].
