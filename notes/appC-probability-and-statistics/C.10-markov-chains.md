---
appendix: C
section: "C.10"
title: "Markov Chains"
pdf_pages: "469-471"
---

## C.10 Markov Chains

> **Definition C.6: Markov Chain**
>
> A *Markov chain* is a collection $\{X_t, t = 0,1,2,\ldots\}$ of random variables (or random vectors) whose futures are conditionally independent of their pasts given their present values. That is,
>
> $$\mathbb{P}[X_{t+1}\in A \mid X_s, s\leqslant t] = \mathbb{P}[X_{t+1}\in A \mid X_t] \quad \text{for all } t. \tag{C.41}$$

In other words, the conditional distribution of the future variable $X_{t+1}$, given the entire past $\{X_s, s\leqslant t\}$, is the same as the conditional distribution of $X_{t+1}$ given only the present $X_t$. Property (C.41) is called the *Markov property*.

The index $t$ in $X_t$ is usually seen as a "time" or "step" parameter. The index set $\{0,1,2,\ldots\}$ in the definition above was chosen out of convenience. It can be replaced by any countable index set. We restrict ourselves to *time-homogeneous* Markov chains — Markov chains for which the conditional pdfs $f_{X_{t+1}\mid X_t}(y\mid x)$ do not depend on $t$; we abbreviate these as $q(y\mid x)$. The $\{q(y\mid x)\}$ are called the *(one-step) transition densities* of the Markov chain. Note that the random variables or vectors $\{X_t\}$ may be *discrete* (e.g., taking values in some set $\{1,\ldots,r\}$) or *continuous* (e.g., taking values in an interval $[0,1]$ or $\mathbb{R}^d$). In particular, in the discrete case each $q(y\mid x)$ is a probability: $q(y\mid x) = \mathbb{P}[X_{t+1}=y\mid X_t=x]$.

The distribution of $X_0$ is called the *initial distribution* of the Markov chain. The one-step transition densities and the initial distribution completely specify the distribution of the random vector $[X_0, X_1, \ldots, X_t]^\top$. Namely, we have by the product rule (C.17) and the Markov property that the joint pdf is given by

$$
\begin{aligned}
f_{X_0,\ldots,X_t}(x_0,\ldots,x_t) &= f_{X_0}(x_0)\, f_{X_1\mid X_0}(x_1\mid x_0)\cdots f_{X_t\mid X_{t-1},\ldots,X_0}(x_t\mid x_{t-1},\ldots,x_0) \\
&= f_{X_0}(x_0)\, f_{X_1\mid X_0}(x_1\mid x_0)\cdots f_{X_t\mid X_{t-1}}(x_t\mid x_{t-1}) \\
&= f_{X_0}(x_0)\, q(x_1\mid x_0)\, q(x_2\mid x_1)\cdots q(x_t\mid x_{t-1}).
\end{aligned}
$$

A Markov chain is said to be *ergodic* if the probability distribution of $X_t$ converges to a fixed distribution as $t\to\infty$. Ergodicity is a property of many Markov chains. Intuitively, the probability of encountering the Markov chain in a state $x$ at a time $t$ far into the future should not depend on $t$, provided that the Markov chain can reach every state from any other state — such Markov chains are said to be *irreducible* — and does not "escape" to infinity. Thus, for an ergodic Markov chain the pdf $f_{X_t}(x)$ converges to a fixed *limiting pdf* $f(x)$ as $t\to\infty$, irrespective of the starting state. For the discrete case, $f(x)$ corresponds to the long-run fraction of times that the Markov process visits $x$.

Under mild conditions (such as irreducibility) the limiting pdf $f(x)$ can be found by solving the *global balance equations*:

$$
f(x) =
\begin{cases}
\sum_y f(y)\, q(x\mid y) & \text{(discrete case)}, \\[4pt]
\int f(y)\, q(x\mid y)\,\mathrm{d}y & \text{(continuous case)}.
\end{cases}
\tag{C.42}
$$

For the discrete case the rationale behind this is as follows. Since $f(x)$ is the long-run proportion of time that the Markov chain spends in $x$, the proportion of transitions *out of* $x$ is $f(x)$. This should be balanced with the proportion of transitions *into* state $x$, which is $\sum_y f(y)\,q(x\mid y)$.

One is often interested in a stronger type of balance equations. Imagine that we have taken a video of the evolution of the Markov chain, which we may run in forward and reverse time. If we cannot determine whether the video is running forward or backward (we cannot determine any systematic "looping", which would indicate in which direction time is flowing), the chain is said to be time-reversible or simply *reversible*.

Although not every Markov chain is reversible, each ergodic Markov chain, when run backwards, gives another Markov chain — the *reverse Markov chain* — with transition densities $\widetilde{q}(y\mid x) = f(y)\,q(x\mid y)/f(x)$. To see this, first observe that $f(x)$ is the long-run proportion of time spent in $x$ for both the original and reverse Markov chain. Secondly, the "probability flux" from $x$ to $y$ in the reversed chain must be equal to the probability flux from $y$ to $x$ in the original chain, meaning $f(x)\,\widetilde{q}(y\mid x) = f(y)\,q(x\mid y)$, which yields the stated transition probabilities for the reversed chain. In particular, for a *reversible* Markov chain we have

$$f(x)\,q(y\mid x) = f(y)\,q(x\mid y) \quad \text{for all } x,y. \tag{C.43}$$

These are the *detailed (or local) balance equations*. Note that the detailed balance equations imply the global balance equations. Hence, if a Markov chain is irreducible and there exists a pdf such that (C.43) holds, then $f(x)$ must be the limiting pdf. In the discrete state space case an additional condition is that the chain must be *aperiodic*, meaning that the return times to the same state cannot always be a multiple of some integer $\geqslant 2$.

**Example C.9 (Random Walk on a Graph).** Consider a Markov chain that performs a "random walk" on the graph in Figure C.7, at each step jumping from the current vertex (node) to one of the adjacent vertices, with equal probability. Clearly this Markov chain is irreducible and aperiodic. It is also reversible. Let $f(x)$ denote the limiting probability that the chain is in vertex $x$. By symmetry, $f(1)=f(2)=f(7)=f(8)$, $f(4)=f(5)$, and $f(3)=f(6)$. Moreover, by the detailed balance equations, $f(4)/5 = f(1)/3$, and $f(3)/4 = f(1)/3$. It follows that $f(1)+\cdots+f(8) = 4f(1) + 2\times 5/3\,f(1) + 2\times 4/3\,f(1) = 10 f(1) = 1$, so that $f(1) = 1/10$, $f(3) = 2/15$, and $f(4) = 1/6$.

> **Figure C.7:** A graph with 8 vertices (labeled 1, 2, 7, 8 on the outer corners and 3, 4, 5, 6 in the interior), with vertex 1 connected to 2, 3, 4, and 7; vertex 2 connected to 1, 3, 5, and 8; and similar symmetric adjacency among the remaining vertices, forming a symmetric structure. The random walk that jumps to an adjacent vertex with equal probability on this graph is reversible; the figure illustrates the vertex/edge structure used in Example C.9 to compute the limiting probabilities $f(1), f(3), f(4)$, etc., via the detailed balance equations. $\blacksquare$
