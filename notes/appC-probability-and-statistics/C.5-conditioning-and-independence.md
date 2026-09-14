---
appendix: C
section: "C.5"
title: "Conditioning and Independence"
pdf_pages: "446-449"
---

## C.5 Conditioning and Independence

Conditional probabilities and conditional distributions are used to model additional information on a random experiment. Independence is used to model *lack* of such information.

### C.5.1 Conditional Probability

Suppose some event $B \subseteq \Omega$ occurs. Given this fact, event $A$ will occur if and only if $A \cap B$ occurs, and the relative chance of $A$ occurring is therefore $\mathbb{P}[A \cap B]/\mathbb{P}[B]$, provided $\mathbb{P}[B] > 0$. This leads to the definition of the *conditional probability* of $A$ given $B$:

$$\mathbb{P}[A \mid B] = \frac{\mathbb{P}[A \cap B]}{\mathbb{P}[B]}, \quad \text{if } \mathbb{P}[B] > 0. \tag{C.7}$$

The above definition breaks down if $\mathbb{P}[B] = 0$. Such conditional probabilities must be treated with more care [11].

Three important consequences of the definition of conditional probability are:

1. *Product rule*: For any sequence of events $A_1, A_2, \ldots, A_n$,

$$\mathbb{P}[A_1 \cdots A_n] = \mathbb{P}[A_1]\, \mathbb{P}[A_2 \mid A_1]\, \mathbb{P}[A_3 \mid A_1 A_2] \cdots \mathbb{P}[A_n \mid A_1 \cdots A_{n-1}], \tag{C.8}$$

using the abbreviation $A_1 A_2 \cdots A_k := A_1 \cap A_2 \cap \cdots \cap A_k$.

2. *Law of total probability*: If $\{B_i\}$ forms a *partition* of $\Omega$ (that is, $B_i \cap B_j = \emptyset, i \neq j$ and $\cup_i B_i = \Omega$), then for any event $A$

$$\mathbb{P}[A] = \sum_i \mathbb{P}[A \mid B_i]\, \mathbb{P}[B_i]. \tag{C.9}$$

3. *Bayes' rule*: Let $\{B_i\}$ form a partition of $\Omega$. Then, for any event $A$ with $\mathbb{P}[A] > 0$,

$$\mathbb{P}[B_j \mid A] = \frac{\mathbb{P}[A \mid B_j]\, \mathbb{P}[B_j]}{\sum_i \mathbb{P}[A \mid B_i]\, \mathbb{P}[B_i]}. \tag{C.10}$$

### C.5.2 Independence

Two events $A$ and $B$ are said to be *independent* if the knowledge that $B$ has occurred does not change the probability that $A$ occurs. That is, $A, B$ independent $\Leftrightarrow \mathbb{P}[A \mid B] = \mathbb{P}[A]$. Since $\mathbb{P}[A \mid B]\, \mathbb{P}[B] = \mathbb{P}[A \cap B]$, an alternative definition of independence is

$$A, B \text{ independent} \Leftrightarrow \mathbb{P}[A \cap B] = \mathbb{P}[A]\, \mathbb{P}[B].$$

This definition covers the case where $\mathbb{P}[B] = 0$ and can be extended to arbitrarily many events: events $A_1, A_2, \ldots$ are said to be (mutually) independent if for any $k$ and any choice of distinct indices $i_1, \ldots, i_k$,

$$\mathbb{P}[A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}] = \mathbb{P}[A_{i_1}]\, \mathbb{P}[A_{i_2}] \cdots \mathbb{P}[A_{i_k}].$$

The concept of independence can also be formulated for random variables. Random variables $X_1, X_2, \ldots$ are said to be *independent* if the events $\{X_{i_1} \leqslant x_{i_1}\}, \ldots, \{X_{i_n} \leqslant x_{i_n}\}$ are independent for all finite choices of $n$ distinct indices $i_1, \ldots, i_n$ and values $x_{i_1}, \ldots, x_{i_n}$.

An important characterization of independent random variables is the following (for a proof, see [101], for example).

> **Theorem C.1: Independence Characterization**
>
> Random variables $X_1, \ldots, X_n$ with marginal pdfs $f_{X_1}, \ldots, f_{X_n}$ and joint pdf $f$ are independent if and only if
>
> $$f(x_1, \ldots, x_n) = f_{X_1}(x_1) \cdots f_{X_n}(x_n) \quad \text{for all } x_1, \ldots, x_n. \tag{C.11}$$

Many probabilistic models involve random variables $X_1, X_2, \ldots$ that are *independent and identically distributed*, abbreviated as *iid*. We use this abbreviation throughout this book.

### C.5.3 Expectation and Covariance

Similar to the univariate case, the expected value of a real-valued function $h$ of a random vector $\boldsymbol{X} \sim f$ is a weighted average of all values that $h(\boldsymbol{X})$ can take. Specifically, in the continuous case, $\mathbb{E}h(\boldsymbol{X}) = \int h(\boldsymbol{x}) f(\boldsymbol{x})\, \mathrm{d}\boldsymbol{x}$. In the discrete case replace this multidimensional integral with a sum. Using this result, it is not difficult to show that for any collection of dependent or independent random variables $X_1, \ldots, X_n$,

$$\mathbb{E}[a + b_1 X_1 + b_2 X_2 + \cdots + b_n X_n] = a + b_1 \mathbb{E}X_1 + \cdots + b_n \mathbb{E}X_n \tag{C.12}$$

for all constants $a, b_1, \ldots, b_n$. Moreover, for *independent* random variables,

$$\mathbb{E}[X_1 X_2 \cdots X_n] = \mathbb{E}X_1\, \mathbb{E}X_2 \cdots \mathbb{E}X_n. \tag{C.13}$$

We leave the proofs as an exercise.

The *covariance* of two random variables $X$ and $Y$ with expectations $\mu_X$ and $\mu_Y$, respectively, is defined as

$$\mathbb{C}\mathrm{ov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)].$$

This is a measure of the amount of linear dependency between the variables. Let $\sigma_X^2 = \mathbb{V}\mathrm{ar}\,X$ and $\sigma_Y^2 = \mathbb{V}\mathrm{ar}\,Y$. A scaled version of the covariance is given by the *correlation coefficient*,

$$\varrho(X, Y) = \frac{\mathbb{C}\mathrm{ov}(X, Y)}{\sigma_X \sigma_Y}.$$

The following properties follow directly from the definitions of variance and covariance.

1. $\mathbb{V}\mathrm{ar}\,X = \mathbb{E}X^2 - \mu_X^2$.
2. $\mathbb{V}\mathrm{ar}[aX + b] = a^2 \sigma_X^2$.
3. $\mathbb{C}\mathrm{ov}(X, Y) = \mathbb{E}[XY] - \mu_X \mu_Y$.
4. $\mathbb{C}\mathrm{ov}(X, Y) = \mathbb{C}\mathrm{ov}(Y, X)$.
5. $-\sigma_X \sigma_Y \leqslant \mathbb{C}\mathrm{ov}(X, Y) \leqslant \sigma_X \sigma_Y$.
6. $\mathbb{C}\mathrm{ov}(aX + bY, Z) = a\, \mathbb{C}\mathrm{ov}(X, Z) + b\, \mathbb{C}\mathrm{ov}(Y, Z)$.
7. $\mathbb{C}\mathrm{ov}(X, X) = \sigma_X^2$.
8. $\mathbb{V}\mathrm{ar}[X + Y] = \sigma_X^2 + \sigma_Y^2 + 2\, \mathbb{C}\mathrm{ov}(X, Y)$.
9. If $X$ and $Y$ are independent, then $\mathbb{C}\mathrm{ov}(X, Y) = 0$.

As a consequence of Properties 2 and 8 we have that for any sequence of *independent* random variables $X_1, \ldots, X_n$ with variances $\sigma_1^2, \ldots, \sigma_n^2$,

$$\mathbb{V}\mathrm{ar}[a_1 X_1 + a_2 X_2 + \cdots + a_n X_n] = a_1^2 \sigma_1^2 + a_2^2 \sigma_2^2 + \cdots + a_n^2 \sigma_n^2, \tag{C.14}$$

for any choice of constants $a_1, \ldots, a_n$.

For random column vectors, such as $\boldsymbol{X} = [X_1, \ldots, X_n]^\top$, it is convenient to write the expectations and covariances in vector and matrix notation. For a random vector $\boldsymbol{X}$ we define its *expectation vector* as the vector of expectations

$$\boldsymbol{\mu} = [\mu_1, \ldots, \mu_n]^\top = [\mathbb{E}X_1, \ldots, \mathbb{E}X_n]^\top.$$

Similarly, if the expectation of a matrix is the matrix of expectations, then given two random vectors $\boldsymbol{X} \in \mathbb{R}^n$ and $\boldsymbol{Y} \in \mathbb{R}^m$, the $n \times m$ matrix

$$\mathbb{C}\mathrm{ov}(\boldsymbol{X}, \boldsymbol{Y}) = \mathbb{E}[(\boldsymbol{X} - \mathbb{E}\boldsymbol{X})(\boldsymbol{Y} - \mathbb{E}\boldsymbol{Y})^\top] \tag{C.15}$$

has $(i,j)$-th element $\mathbb{C}\mathrm{ov}(X_i, Y_j) = \mathbb{E}[(X_i - \mathbb{E}X_i)(Y_j - \mathbb{E}Y_j)]$. A consequence of this definition is that

$$\mathbb{C}\mathrm{ov}(\mathbf{A}\boldsymbol{X}, \mathbf{B}\boldsymbol{Y}) = \mathbf{A}\, \mathbb{C}\mathrm{ov}(\boldsymbol{X}, \boldsymbol{Y})\, \mathbf{B}^\top,$$

where $\mathbf{A}$ and $\mathbf{B}$ are two matrices with $n$ and $m$ columns, respectively.

The *covariance matrix* of the vector $\boldsymbol{X}$ is defined as the $n \times n$ matrix $\mathbb{C}\mathrm{ov}(\boldsymbol{X}, \boldsymbol{X})$. The covariance matrix is also denoted as $\mathbb{V}\mathrm{ar}(\boldsymbol{X}) = \mathbb{C}\mathrm{ov}(\boldsymbol{X}, \boldsymbol{X})$, in analogy with the scalar identity $\mathbb{V}\mathrm{ar}(X) = \mathbb{C}\mathrm{ov}(X, X)$.

A useful application of the cyclic property of the trace of a matrix (see Theorem A.1, p.357) is the following.

> **Theorem C.2: Expectation of a Quadratic Form**
>
> Let $\mathbf{A}$ be an $n \times n$ matrix and $\boldsymbol{X}$ an $n$-dimensional random vector with expectation vector $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$. The random variable $Y := \boldsymbol{X}^\top \mathbf{A} \boldsymbol{X}$ has expectation $\mathrm{tr}(\mathbf{A}\boldsymbol{\Sigma}) + \boldsymbol{\mu}^\top \mathbf{A} \boldsymbol{\mu}$.

*Proof:* Since $Y$ is a scalar, it is equal to its trace. Now, using the cyclic property: $\mathbb{E}Y = \mathbb{E}\,\mathrm{tr}(Y) = \mathbb{E}\,\mathrm{tr}(\boldsymbol{X}^\top \mathbf{A} \boldsymbol{X}) = \mathbb{E}\,\mathrm{tr}(\mathbf{A} \boldsymbol{X} \boldsymbol{X}^\top) = \mathrm{tr}(\mathbf{A}\, \mathbb{E}[\boldsymbol{X}\boldsymbol{X}^\top]) = \mathrm{tr}(\mathbf{A}(\boldsymbol{\Sigma} + \boldsymbol{\mu}\boldsymbol{\mu}^\top)) = \mathrm{tr}(\mathbf{A}\boldsymbol{\Sigma}) + \mathrm{tr}(\mathbf{A}\boldsymbol{\mu}\boldsymbol{\mu}^\top) = \mathrm{tr}(\mathbf{A}\boldsymbol{\Sigma}) + \boldsymbol{\mu}^\top \mathbf{A} \boldsymbol{\mu}$. $\square$

### C.5.4 Conditional Density and Conditional Expectation

Suppose $X$ and $Y$ are both discrete or both continuous, with joint pdf $f$, and suppose $f_X(x) > 0$. Then, the *conditional pdf* of $Y$ given $X = x$ is given by

$$f_{Y \mid X}(y \mid x) = \frac{f(x, y)}{f_X(x)} \quad \text{for all } y. \tag{C.16}$$

In the discrete case, the formula is a direct translation of (C.7), with $f_{Y \mid X}(y \mid x) = \mathbb{P}[Y = y \mid X = x]$. In the continuous case, a similar interpretation in terms of densities can be used; see, for example, [101, Page 221]. The corresponding distribution is called the *conditional distribution* of $Y$ given $X = x$. Note that (C.16) implies that

$$f(x, y) = f_X(x)\, f_{Y \mid X}(y \mid x).$$

This is useful when the marginal and conditional pdfs are given, rather than the joint one. More generally, for the $n$-dimensional case we have

$$f(x_1, \ldots, x_n) = f_{X_1}(x_1)\, f_{X_2 \mid X_1}(x_2 \mid x_1) \cdots f_{X_n \mid X_1, \ldots, X_{n-1}}(x_n \mid x_1, \ldots, x_{n-1}), \tag{C.17}$$

which is in essence a rephrasing of the product rule (C.8) (p.428) in terms of probability densities.

As a conditional pdf has all the properties of an ordinary pdf, we may define expectations with respect to it. The *conditional expectation* of a random variable $Y$ given $X = x$ is defined as

$$\mathbb{E}[Y \mid X = x] = \begin{cases} \sum_y y\, f_{Y \mid X}(y \mid x) & \text{discrete case,} \\ \int y\, f_{Y \mid X}(y \mid x)\, \mathrm{d}y & \text{continuous case.} \end{cases} \tag{C.18}$$

Note that $\mathbb{E}[Y \mid X = x]$ is a function of $x$. The corresponding random variable is written as $\mathbb{E}[Y \mid X]$. A similar formalism can be used when conditioning on a sequence of random variables $X_1, \ldots, X_n$. The conditional expectation has similar properties to the ordinary expectation. Other useful properties (see, for example, [127]) are:

1. *Tower property*: If $\mathbb{E}Y$ exists, then

$$\mathbb{E}\,\mathbb{E}[Y \mid X] = \mathbb{E}Y. \tag{C.19}$$

2. *Taking out what is known*: If $\mathbb{E}Y$ exists, then

$$\mathbb{E}[XY \mid X] = X\, \mathbb{E}[Y \mid X].$$
