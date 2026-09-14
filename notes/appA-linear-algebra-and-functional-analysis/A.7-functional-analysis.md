---
appendix: A
section: "A.7"
title: "Functional Analysis"
pdf_pages: "402-408"
---

# A.7 Functional Analysis

Much of the previous theory on Euclidean vector spaces can be generalized to vector spaces of *functions*. Every element of a (real-valued) *function space* $\mathcal{H}$ is a function from some set $\mathcal{X}$ to $\mathbb{R}$, and elements can be added and scalar multiplied as if they were vectors. In other words, if $f \in \mathcal{H}$ and $g \in \mathcal{H}$, then $\alpha f + \beta g \in \mathcal{H}$ for all $\alpha,\beta \in \mathbb{R}$. On $\mathcal{H}$ we can impose an inner product as a mapping $\langle\cdot,\cdot\rangle$ from $\mathcal{H}\times\mathcal{H}$ to $\mathbb{R}$ that satisfies

1. $\langle\alpha f_1+\beta f_2, g\rangle = \alpha\langle f_1,g\rangle + \beta\langle f_2,g\rangle$;
2. $\langle f,g\rangle = \langle g,f\rangle$;
3. $\langle f,f\rangle \ge 0$;
4. $\langle f,f\rangle = 0$ if and only if $f = 0$ (the zero function).

We focus on real-valued function spaces, although the theory for complex-valued function spaces is similar (and sometimes easier), under suitable modifications (e.g., $\langle f,g\rangle = \overline{\langle g,f\rangle}$).

Similar to the linear algebra setting in Section A.2, we say that two elements $f$ and $g$ in $\mathcal{H}$ are *orthogonal* to each other with respect to this inner product if $\langle f,g\rangle = 0$. Given an inner product, we can measure distances between elements of the function space $\mathcal{H}$ using the *norm*

$$\|f\| := \sqrt{\langle f,f\rangle}.$$

For example, the distance between two functions $f_m$ and $f_n$ is given by $\|f_m-f_n\|$. The space $\mathcal{H}$ is said to be *complete* if every sequence of functions $f_1,f_2,\dots \in \mathcal{H}$ for which

$$\|f_m-f_n\| \to 0 \text{ as } m,n\to\infty, \tag{A.28}$$

converges to some $f \in \mathcal{H}$; that is, $\|f-f_n\| \to 0$ as $n\to\infty$. A sequence that satisfies (A.28) is called a *Cauchy sequence*.

A complete inner product space is called a *Hilbert space*. The most fundamental Hilbert space of functions is the space $L^2$. An in-depth introduction to $L^2$ requires some measure theory [6]. For our purposes, it suffices to assume that $\mathcal{X} \subseteq \mathbb{R}^d$ and that on $\mathcal{X}$ a *measure* $\mu$ is defined which assigns to each suitable[^4] set $A$ a positive number $\mu(A) \ge 0$ (e.g., its volume). In many cases of interest $\mu$ is of the form

$$\mu(A) = \int_A w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} \tag{A.29}$$

where $w \ge 0$ is a positive function on $\mathcal{X}$ which is called the *density* of $\mu$ with respect to the Lebesgue measure (the natural volume measure on $\mathbb{R}^d$). We write $\mu(\mathrm{d}\boldsymbol{x}) = w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ to indicate that $\mu$ has density $w$. Another important case is where

$$\mu(A) = \sum_{\boldsymbol{x}\in A\cap\mathbb{Z}^d} w(\boldsymbol{x}), \tag{A.30}$$

where $w \ge 0$ is again called the density of $\mu$, but now with respect to the counting measure on $\mathbb{Z}^d$ (which counts the points of $\mathbb{Z}^d$). Integrals with respect to measures $\mu$ in (A.29) and (A.30) can now be defined as

$$\int f(\boldsymbol{x})\,\mu(\mathrm{d}\boldsymbol{x}) = \int f(\boldsymbol{x})\,w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x},$$

and

$$\int f(\boldsymbol{x})\,\mu(\mathrm{d}\boldsymbol{x}) = \sum_{\boldsymbol{x}} f(\boldsymbol{x})\,w(\boldsymbol{x}),$$

respectively. We assume for simplicity that $\mu$ has the form (A.29). For measures of the form (A.30) (so-called discrete measures), replace integrals by sums in what follows.

[^4]: Not all sets have a measure. Suitable sets are Borel sets, which can be thought of as countable unions of rectangles.

**Definition A.4: $L^2$ Space**

> Let $\mathcal{X}$ be a subset of $\mathbb{R}^d$ with measure $\mu(\mathrm{d}\boldsymbol{x}) = w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$. The Hilbert space $L^2(\mathcal{X},\mu)$ is the linear space of functions from $\mathcal{X}$ to $\mathbb{R}$ that satisfy
> $$\int_{\mathcal{X}} f(\boldsymbol{x})^2 w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} < \infty, \tag{A.31}$$
> and with inner product
> $$\langle f,g\rangle = \int_{\mathcal{X}} f(\boldsymbol{x})g(\boldsymbol{x})w(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}. \tag{A.32}$$

Let $\mathcal{H}$ be a Hilbert space. A set of functions $\{f_i, i\in I\}$ is called an *orthonormal system* if

1. the norm of every $f_i$ is 1; that is, $\langle f_i,f_i\rangle = 1$ for all $i\in I$,
2. the $\{f_i\}$ are orthogonal; that is, $\langle f_i,f_j\rangle = 0$ for $i \ne j$.

It follows then that the $\{f_i\}$ are linearly independent; that is, the only linear combination $\sum_j \alpha_j f_j(\boldsymbol{x})$ that is equal to $f_i(\boldsymbol{x})$ for all $\boldsymbol{x}$ is the one where $\alpha_i = 1$ and $\alpha_j = 0$ for $j \ne i$. An orthonormal system $\{f_i\}$ is called an *orthonormal basis* if there is no other $f \in \mathcal{H}$ that is orthogonal to all the $\{f_i, i\in I\}$ (other than the zero function). Although the general theory allows for uncountable bases, in practice[^5] the set $I$ is taken to be countable.

[^5]: The function spaces typically encountered in machine learning and data science are usually *separable spaces*, which allows for the set $I$ to be considered countable; see, e.g., [106].

**Example A.12 (Trigonometric Orthonormal Basis)** Let $\mathcal{H}$ be the Hilbert space $L^2((0,2\pi),\mu)$, where $\mu(\mathrm{d}x) = w(x)\,\mathrm{d}x$ and $w$ is the constant function $w(x) = 1, 0 < x < 2\pi$. Alternatively, take $\mathcal{X} = \mathbb{R}$ and $w$ the indicator function on $(0,2\pi)$. The trigonometric functions

$$g_0(x) = \frac{1}{\sqrt{2\pi}}, \quad g_k(x) = \frac{1}{\sqrt{\pi}}\cos(kx), \quad h_k(x) = \frac{1}{\sqrt{\pi}}\sin(kx), \quad k=1,2,\dots$$

form a countable infinite-dimensional orthonormal basis of $\mathcal{H}$. $\blacksquare$

A Hilbert space $\mathcal{H}$ with an orthonormal basis $\{f_1,f_2,\dots\}$ behaves very similarly to the familiar Euclidean vector space. In particular, every element (i.e., function) $f \in \mathcal{H}$ can be written as a unique linear combination of the basis vectors:

$$f = \sum_i \langle f,f_i\rangle f_i, \tag{A.33}$$

exactly as in Theorem A.3. The right-hand side of (A.33) is called a (generalized) *Fourier expansion* of $f$. Note that such a Fourier expansion does not require a trigonometric basis; any orthonormal basis will do.

**Example A.13 (Example A.12 (cont.))** Consider the indicator function $f(x) = \mathbb{1}\{0<x<\pi\}$. As the trigonometric functions $\{g_k\}$ and $\{h_k\}$ form a basis for $L^2((0,2\pi),1\,\mathrm{d}x)$, we can write

$$f(x) = a_0\frac{1}{\sqrt{2\pi}} + \sum_{k=1}^\infty a_k\frac{1}{\sqrt{\pi}}\cos(kx) + \sum_{k=1}^\infty b_k\frac{1}{\sqrt{\pi}}\sin(kx), \tag{A.34}$$

where $a_0 = \int_0^\pi 1/\sqrt{2\pi}\,\mathrm{d}x = \sqrt{\pi/2}$, $a_k = \int_0^\pi \cos(kx)/\sqrt{\pi}\,\mathrm{d}x$ and $b_k = \int_0^\pi \sin(kx)/\sqrt{\pi}\,\mathrm{d}x, k=1,2,\dots$. This means that $a_k = 0$ for all $k$, $b_k=0$ for even $k$, and $b_k = 2/(k\sqrt{\pi})$ for odd $k$. Consequently,

$$f(x) = \frac{1}{2} + \frac{2}{\pi}\sum_{k=1}^\infty \frac{\sin(kx)}{k}. \tag{A.35}$$

Figure A.7 shows several Fourier *approximations* obtained by truncating the infinite sum in (A.35). $\blacksquare$

> **Figure A.7:** Fourier approximations of the unit step function $f$ on the interval $(0,\pi)$, truncating the infinite sum in (A.35) to $i=2,4$, and $14$ terms, giving the dotted blue, dashed red, and solid green curves, respectively — illustrating the Gibbs phenomenon (overshoot near the discontinuities) as more terms are added.

Starting from any countable basis, we can use the Gram–Schmidt procedure (book p. 375) to obtain an orthonormal basis, as illustrated in the following example.

**Example A.14 (Legendre Polynomials)** Take the function space $L^2(\mathbb{R}, w(x)\,\mathrm{d}x)$, where $w(x) = \mathbb{1}\{-1<x<1\}$. We wish to construct an orthonormal basis of polynomial functions $g_0,g_1,g_2,\dots$, starting from the collection of monomials: $\iota_0,\iota_1,\iota_2,\dots$, where $\iota_k : x \mapsto x^k$. Using Gram–Schmidt, the first normalized zero-degree polynomial is $g_0 = \iota_0/\|\iota_0\| = \sqrt{1/2}$. To find $g_1$ (a polynomial of degree 1), project $\iota_1$ (the identity function) onto the space spanned by $g_0$. The resulting projection is $p_1 := \langle g_0,\iota_1\rangle g_0$, written out as

$$p_1(x) = \left(\int_{-1}^1 x\,g_0(x)\,\mathrm{d}x\right)g_0(x) = \frac{1}{2}\int_{-1}^1 x\,\mathrm{d}x = 0.$$

Hence, $g_1 = (\iota_1-p_1)/\|\iota_1-p_1\|$ is a linear function; that is, of the form $g_1(x) = ax$. The constant $a$ is found by normalization:

$$1 = \|g_1\|^2 = \int_{-1}^1 g_1^2(x)\,\mathrm{d}x = a^2\int_{-1}^1 x^2\,\mathrm{d}x = a^2\frac{2}{3},$$

so that $g_1(x) = \sqrt{3/2}\,x$. Continuing the Gram–Schmidt procedure, we find $g_2(x) = \sqrt{5/8}(3x^2-1)$, $g_3(x) = \sqrt{7/8}(5x^3-3x)$ and, in general,

$$g_k(x) = \frac{\sqrt{2k+1}}{2^{k+\frac{1}{2}}k!}\frac{\mathrm{d}^k}{\mathrm{d}x^k}(x^2-1)^k, \quad k=0,1,2,\dots.$$

These are the (normalized) *Legendre polynomials*. The graphs of $g_0,g_1,g_2$, and $g_3$ are given in Figure A.8.

> **Figure A.8:** The first 4 normalized Legendre polynomials $g_0$ (constant), $g_1$ (linear), $g_2$ (quadratic), and $g_3$ (cubic) plotted on $(-1,1)$.

As the Legendre polynomials form an orthonormal basis of $L^2(\mathbb{R}, \mathbb{1}\{-1<x<1\}\,\mathrm{d}x)$, they can be used to approximate arbitrary functions in this space. For example, Figure A.9 shows an approximation using the first 51 Legendre polynomials ($k=0,1,\dots,50$) of the Fourier expansion of the indicator function on the interval $(-1/2,1/2)$. These Legendre polynomials form the basis of a 51-dimensional linear subspace onto which the indicator function is orthogonally projected.

> **Figure A.9:** Approximation of the indicator function on the interval $(-1/2,1/2)$, using the Legendre polynomials $g_0,g_1,\dots,g_{50}$ — the truncated series shows Gibbs-phenomenon ripples near the jump discontinuities while closely matching the flat regions.

$\blacksquare$

The Legendre polynomials were produced in the following way: We started with an unnormalized probability density on $\mathbb{R}$ (book p. 424) — in this case the probability density of the uniform distribution on $(-1,1)$. We then constructed a sequence of polynomials by applying the Gram–Schmidt procedure to the monomials $1,x,x^2,\dots$.

By using exactly the same procedure, but with a different probability density, we can produce other such *orthogonal polynomials*. For example, the density of the standard exponential[^6] distribution, $w(x) = \mathrm{e}^{-x}, x \ge 0$, gives the *Laguerre polynomials*, which are defined by the recurrence

[^6]: This can be further generalized to the density of a gamma distribution.

$$(n+1)g_{n+1}(x) = (2n+1-x)g_n(x) - n g_{n-1}(x), \quad n=1,2,\dots,$$

with $g_0(x) = 1$ and $g_1(x) = 1-x$, for $x \ge 0$. The *Hermite polynomials* are obtained when using instead the density of the standard normal distribution: $w(x) = \mathrm{e}^{-x^2/2}/\sqrt{2\pi}, x\in\mathbb{R}$. These polynomials satisfy the recursion

$$g_{n+1}(x) = x g_n(x) - \frac{\mathrm{d}g_n(x)}{\mathrm{d}x}, \quad n=0,1,\dots,$$

with $g_0(x)=1, x\in\mathbb{R}$. Note that the Hermite polynomials as defined above have not been normalized to have norm 1. To normalize, use the fact that $\|g_n\|^2 = n!$.

We conclude with a number of key results in functional analysis. The first one is the celebrated Cauchy–Schwarz inequality.

**Theorem A.15: Cauchy–Schwarz**

> Let $\mathcal{H}$ be a Hilbert space. For every $f,g \in \mathcal{H}$ it holds that
> $$|\langle f,g\rangle| \le \|f\|\,\|g\|.$$

*Proof:* The inequality is trivially true for $g=0$ (zero function). For $g \ne 0$, we can write $f = \alpha g + h$, where $h \perp g$ and $\alpha = \langle f,g\rangle/\|g\|^2$. Consequently, $\|f\|^2 = |\alpha|^2\|g\|^2 + \|h\|^2 \ge |\alpha|^2\|g\|^2$. The result follows after rearranging this last inequality. $\square$

Let $\mathcal{V}$ and $\mathcal{W}$ be two linear vector spaces (for example, Hilbert spaces) on which norms $\|\cdot\|_{\mathcal{V}}$ and $\|\cdot\|_{\mathcal{W}}$ are defined. Suppose $A : \mathcal{V}\to\mathcal{W}$ is a mapping from $\mathcal{V}$ to $\mathcal{W}$. When $\mathcal{W} = \mathcal{V}$, such a mapping is often called an *operator*; when $\mathcal{W}=\mathbb{R}$ it is called a *functional*. Mapping $A$ is said to be *linear* if $A(\alpha f+\beta g) = \alpha A(f)+\beta A(g)$. In this case we write $Af$ instead of $A(f)$. If there exists $\gamma < \infty$ such that

$$\|Af\|_{\mathcal{W}} \le \gamma\|f\|_{\mathcal{V}}, \quad f\in\mathcal{V}, \tag{A.36}$$

then $A$ is said to be a *bounded mapping*. The smallest $\gamma$ for which (A.36) holds is called the *norm* of $A$; denoted by $\|A\|$. A (not necessarily linear) mapping $A : \mathcal{V}\to\mathcal{W}$ is said to be *continuous* at $f$ if for any sequence $f_1,f_2,\dots$ converging to $f$ the sequence $A(f_1),A(f_2),\dots$ converges to $A(f)$. That is, if

$$\forall \varepsilon>0, \exists \delta>0 : \forall g\in\mathcal{V}, \|f-g\|_{\mathcal{V}}<\delta \Rightarrow \|A(f)-A(g)\|_{\mathcal{W}}<\varepsilon. \tag{A.37}$$

If the above property holds for every $f\in\mathcal{V}$, then the mapping $A$ itself is called *continuous*.

**Theorem A.16: Continuity and Boundedness for Linear Mappings**

> For a linear mapping, continuity and boundedness are equivalent.

*Proof:* Let $A$ be linear and bounded. We may assume that $A$ is non-zero (otherwise the statement holds trivially), and that therefore $0 < \|A\| < \infty$. Taking $\delta < \varepsilon/\|A\|$ in (A.37) now ensures that $\|Af-Ag\|_{\mathcal{W}} \le \|A\|\,\|f-g\|_{\mathcal{V}} < \|A\|\,\delta < \varepsilon$. This shows that $A$ is continuous.

Conversely, suppose $A$ is continuous. In particular, it is continuous at $f=0$ (the zero-element of $\mathcal{V}$). Thus, take $f=0$ and let $\varepsilon$ and $\delta$ be as in (A.37). For any $g\ne 0$, let $h = \delta/(2\|g\|_{\mathcal{V}})\,g$. As $\|h\|_{\mathcal{V}} = \delta/2 < \delta$, it follows from (A.37) that

$$\|Ah\|_{\mathcal{W}} = \frac{\delta}{2\|g\|_{\mathcal{V}}}\|Ag\|_{\mathcal{W}} < \varepsilon.$$

Rearranging the last inequality gives $\|Ag\|_{\mathcal{W}} < 2\varepsilon/\delta\,\|g\|_{\mathcal{V}}$, showing that $A$ is bounded. $\square$

**Theorem A.17: Riesz Representation Theorem**

> Any bounded linear functional $\phi$ on a Hilbert space $\mathcal{H}$ can be represented as $\phi(h) = \langle h,g\rangle$, for some $g \in \mathcal{H}$ (depending on $\phi$).

*Proof:* Let $P$ be the projection of $\mathcal{H}$ onto the nullspace $\mathcal{N}$ of $\phi$; that is, $\mathcal{N} = \{g\in\mathcal{H} : \phi(g)=0\}$. If $\phi$ is not the 0-functional, then there exists a $g_0 \ne 0$ with $\phi(g_0)\ne 0$. Let $g_1 = g_0 - Pg_0$. Then $g_1 \perp \mathcal{N}$ and $\phi(g_1) = \phi(g_0)$. Take $g_2 = g_1/\phi(g_1)$. For any $h \in \mathcal{H}$, $f := h - \phi(h)g_2$ lies in $\mathcal{N}$. As $g_2 \perp \mathcal{N}$ it holds that $\langle f,g_2\rangle = 0$, which is equivalent to $\langle h,g_2\rangle = \phi(h)\|g_2\|^2$. By defining $g = g_2/\|g_2\|^2$ we have found our representation. $\square$
