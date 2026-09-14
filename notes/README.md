# Data Science and Machine Learning — Study Notes

Full section-by-section transcription of *Data Science and Machine Learning: Mathematical and Statistical Methods* by Dirk P. Kroese, Zdravko I. Botev, Thomas Taimre, and Radislav Vaisman (22 August 2024 edition), sourced from `data-science-and-machine-learning.pdf` in this repo.

Each chapter/appendix has its own folder with one markdown file per top-level section (subsections live inside as `##`/`###` headings), plus a `README.md` index for that folder. This keeps any single file small to read back, while still following the book's own numbering (e.g. section 5.6 → `ch05-regression/5.6-linear-models-in-python.md`, which contains 5.6.1–5.6.6 inside it).

## Main chapters

| # | Chapter | Folder | Topics |
|---|---------|--------|--------|
| 1 | Importing, Summarizing, and Visualizing Data | [ch01-importing-summarizing-visualizing-data/](ch01-importing-summarizing-visualizing-data/README.md) | Feature types, summary tables/statistics, plotting qualitative/quantitative data, bivariate visualization |
| 2 | Statistical Learning | [ch02-statistical-learning/](ch02-statistical-learning/README.md) | Supervised/unsupervised learning, training/test loss, bias-variance tradeoff, cross-validation, normal linear models, Bayesian learning |
| 3 | Monte Carlo Methods | [ch03-monte-carlo-methods/](ch03-monte-carlo-methods/README.md) | Random number/variable generation, MCMC, Monte Carlo estimation & variance reduction, simulated annealing, cross-entropy method |
| 4 | Unsupervised Learning | [ch04-unsupervised-learning/](ch04-unsupervised-learning/README.md) | EM algorithm, density estimation, mixture-model & vector-quantization clustering, hierarchical clustering, PCA |
| 5 | Regression | [ch05-regression/](ch05-regression/README.md) | Linear regression, model selection, inference, nonlinear regression, Python workflows, generalized linear models |
| 6 | Regularization and Kernel Methods | [ch06-regularization-and-kernel-methods/](ch06-regularization-and-kernel-methods/README.md) | Regularization, RKHS, kernel construction, representer theorem, smoothing splines, Gaussian process regression, kernel PCA |
| 7 | Classification | [ch07-classification/](ch07-classification/README.md) | Classification metrics, Bayes' rule, LDA/QDA, logistic/softmax regression, KNN, SVM |
| 8 | Decision Trees and Ensemble Methods | [ch08-decision-trees-and-ensemble-methods/](ch08-decision-trees-and-ensemble-methods/README.md) | Tree construction, pruning, bagging, random forests, boosting |
| 9 | Deep Learning | [ch09-deep-learning/](ch09-deep-learning/README.md) | Feed-forward networks, backpropagation, training methods, Python examples (polynomial regression, image classification) |

## Appendices (mathematical background)

| # | Appendix | Folder | Topics |
|---|----------|--------|--------|
| A | Linear Algebra and Functional Analysis | [appA-linear-algebra-and-functional-analysis/](appA-linear-algebra-and-functional-analysis/README.md) | Vector spaces, eigen/matrix decompositions, functional analysis, Fourier transforms |
| B | Multivariate Differentiation and Optimization | [appB-multivariate-differentiation-and-optimization/](appB-multivariate-differentiation-and-optimization/README.md) | Gradients/Hessians, convexity, Lagrangian/duality, Newton/quasi-Newton methods, penalty functions |
| C | Probability and Statistics | [appC-probability-and-statistics/](appC-probability-and-statistics/README.md) | Probability spaces, distributions, conditioning, multivariate normal, Markov chains, estimation, confidence intervals, hypothesis testing |
| D | Python Primer | [appD-python-primer/](appD-python-primer/README.md) | Core Python, NumPy, Matplotlib, Pandas, Scikit-learn, system calls |

## Not transcribed

The Bibliography (PDF pp. 514–522) and Index (PDF pp. 523–533) were intentionally skipped — they're reference lists with no standalone content value for study notes. Refer to the original PDF for those.
