---
appendix: C
section: "C.1"
title: "Random Experiments and Probability Spaces"
pdf_pages: "439-440"
---

> **Appendix C: Probability and Statistics** — The purpose of this chapter is to establish the baseline probability and statistics background for this book. We review basic concepts such as the sum and product rules of probability, random variables and their probability distributions, expectations, independence, conditional probability, transformation rules, limit theorems, and Markov chains. The properties of the multivariate normal distribution are discussed in more detail. The main ideas from statistics are also reviewed, including estimation techniques (such as maximum likelihood estimation), confidence intervals, and hypothesis testing.

## C.1 Random Experiments and Probability Spaces

The basic notion in probability theory is that of a *random experiment*: an experiment whose outcome cannot be determined in advance. Mathematically, a random experiment is modeled via a triplet $(\Omega, \mathcal{H}, \mathbb{P})$, where:

- $\Omega$ is the set of all possible outcomes of the experiment, called the *sample space*.
- $\mathcal{H}$ is the collection of all subsets of $\Omega$ to which a probability can be assigned; such subsets are called *events*.
- $\mathbb{P}$ is a *probability measure*, which assigns to each event $A$ a number $\mathbb{P}[A]$ between 0 and 1, indicating the likelihood that the outcome of the random experiment lies in $A$.

Any probability measure $\mathbb{P}$ must satisfy the following *Kolmogorov axioms*:

1. $\mathbb{P}[A] \geqslant 0$ for every event $A$.
2. $\mathbb{P}[\Omega] = 1$.
3. For any sequence $A_1, A_2, \ldots$ of events,

$$\mathbb{P}\Big[\bigcup_i A_i\Big] \leqslant \sum_i \mathbb{P}[A_i], \tag{C.1}$$

with strict *equality* whenever the events are *disjoint* (that is, non-overlapping).

When (C.1) holds as an equality, it is often referred to as the *sum rule* of probability. It simply states that if an event can happen in a number of different but not simultaneous ways, the probability of that event is the sum of the probabilities of the comprising events. If the events are allowed to overlap, then the inequality (C.1) is called the *union bound*.

In many applications the sample space is *countable*; that is, $\Omega = \{a_1, a_2, \ldots\}$. In this case the easiest way to specify a probability measure $\mathbb{P}$ is to first assign a number $p_i$ to each *elementary event* $\{a_i\}$, with $\sum_i p_i = 1$, and then to define

$$\mathbb{P}[A] = \sum_{i: a_i \in A} p_i \quad \text{for all } A \subseteq \Omega.$$

Here the collection of events $\mathcal{H}$ can be taken to be equal to the collection of *all* subsets of $\Omega$. The triple $(\Omega, \mathcal{H}, \mathbb{P})$ is called a *discrete probability space*. This idea is graphically represented in Figure C.1. Each element $a_i$, represented by a dot, is assigned a weight (that is, probability) $p_i$, indicated by the size of the dot. The probability of the event $A$ is simply the sum of the weights of all the outcomes in $A$.

> **Figure C.1:** A discrete probability space, depicted as a box $\Omega$ containing dots of varying sizes (each dot an outcome $a_i$ with weight $p_i$), with a shaded region $A$ representing an event; the probability of $A$ is the sum of the weights of the dots that fall inside it.

**Remark C.1 (Equilikely Principle).** A special case of a discrete probability space occurs when a random experiment has finitely many outcomes that are all *equally likely*. In this case the probability measure is given by

$$\mathbb{P}[A] = \frac{|A|}{|\Omega|}, \tag{C.2}$$

where $|A|$ denotes the number of outcomes in $A$ and $|\Omega|$ is the total number of outcomes. Thus, the calculation of probabilities reduces to counting numbers of outcomes in events. This is called the *equilikely principle*. $\blacksquare$
