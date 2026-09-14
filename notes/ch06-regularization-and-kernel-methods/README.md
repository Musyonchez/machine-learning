# Chapter 6: Regularization and Kernel Methods

Notes transcribed from *Data Science and Machine Learning* (Kroese, Botev, Taimre, Vaisman), Chapter 6. Source PDF pages 233–268.

| Section | Title | File | PDF pages |
|---|---|---|---|
| 6.1 | Introduction | [6.1-introduction.md](6.1-introduction.md) | 233–234 |
| 6.2 | Regularization | [6.2-regularization.md](6.2-regularization.md) | 234–239 |
| 6.3 | Reproducing Kernel Hilbert Spaces | [6.3-reproducing-kernel-hilbert-spaces.md](6.3-reproducing-kernel-hilbert-spaces.md) | 240–242 |
| 6.4 | Construction of Reproducing Kernels | [6.4-construction-of-reproducing-kernels.md](6.4-construction-of-reproducing-kernels.md) | 242–248 |
| 6.5 | Representer Theorem | [6.5-representer-theorem.md](6.5-representer-theorem.md) | 248–253 |
| 6.6 | Smoothing Cubic Splines | [6.6-smoothing-cubic-splines.md](6.6-smoothing-cubic-splines.md) | 253–256 |
| 6.7 | Gaussian Process Regression | [6.7-gaussian-process-regression.md](6.7-gaussian-process-regression.md) | 256–260 |
| 6.8 | Kernel PCA | [6.8-kernel-pca.md](6.8-kernel-pca.md) | 260–263 |
| — | Further Reading & Exercises | [exercises.md](exercises.md) | 263–268 |

## Section summaries

- **6.1 Introduction** — Overview of the chapter: regularization guards against overfitting; kernel methods generalize linear models via reproducing kernel Hilbert spaces (RKHS). Roadmap for the chapter (ridge/lasso, RKHS theory, representer theorem, splines, GP regression, kernel PCA).
- **6.2 Regularization** — Formalizes penalized training loss minimization; introduces ridge regression and the lasso as canonical examples of regularized regression, and the general trade-off between model complexity and fit.
- **6.3 Reproducing Kernel Hilbert Spaces** — Defines RKHS formally, the reproducing property, and Mercer/positive-semidefinite kernel theory linking kernels to unique RKHSs.
- **6.4 Construction of Reproducing Kernels** — Techniques for building valid kernels (sums, products, feature-map constructions), with examples including polynomial and Gaussian kernels.
- **6.5 Representer Theorem** — States and proves the representer theorem: solutions to penalized empirical risk minimization over $\mathcal{H}\oplus\mathcal{H}_0$ are finite linear combinations of kernel evaluations at the training points; worked ridge-regression and *peaks*-function kernel regression examples.
- **6.6 Smoothing Cubic Splines** — Derives the cubic-spline RKHS on $[0,1]$ penalizing $\|g''\|^2$, its reproducing kernel, and the resulting smoothing-spline optimization problem, with a full Python implementation and example.
- **6.7 Gaussian Process Regression** — Bayesian regression using GP priors defined via a kernel/covariance function; derives the predictive mean/variance, discusses hyperparameter estimation via empirical Bayes and the marginal likelihood, with worked examples and bandwidth/noise-level comparisons.
- **6.8 Kernel PCA** — Recasts PCA via the Gram matrix and generalizes it to kernel PCA using the "kernel trick," including the centering correction $\mathbf{H}\mathbf{K}\mathbf{H}$; worked example separating nested disk/annulus data via nonlinear principal components.
- **Exercises** — Further Reading pointers plus 20 exercises covering RKHS theory foundations (Exercises 1–12), kernel constructions and cubic-spline kernel derivation (13–15), Sherman–Morrison-based ridge regression updates and algorithms (16–17), empirical-Bayes/EM-based hyperparameter selection (18–19), and early stopping vs. ridge regularization equivalence (20).
