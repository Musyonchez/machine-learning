# Chapter 8: Decision Trees and Ensemble Methods

Transcribed notes from *Data Science and Machine Learning: Mathematical and Statistical Methods* (Kroese, Botev, Taimre, Vaisman), Chapter 8 (book pages 287-322, PDF pages 305-340).

| File | Sections | PDF pages | Description |
|------|----------|-----------|-------------|
| [8.1-introduction.md](8.1-introduction.md) | 8.1 | 305-307 | Motivates tree-based methods via a classification example; defines decision trees, regions, regional prediction functions, and the training-loss decomposition over leaves. |
| [8.2-top-down-construction-of-decision-trees.md](8.2-top-down-construction-of-decision-trees.md) | 8.2 (8.2.1-8.2.4) | 307-315 | The recursive `Construct_Subtree` algorithm; regional prediction functions for regression/classification; splitting rules and impurity measures (misclassification, entropy, Gini); termination criteria; a full from-scratch Python implementation of a regression tree. |
| [8.3-additional-considerations.md](8.3-additional-considerations.md) | 8.3 (8.3.1-8.3.5) | 316-318 | Binary vs. non-binary splits, data preprocessing (PCA), alternative (linear-combination) splitting rules, categorical variable splits, and handling missing values via surrogate splitting rules. |
| [8.4-controlling-the-tree-shape.md](8.4-controlling-the-tree-shape.md) | 8.4 (8.4.1-8.4.2) | 318-323 | Pruning concepts (branches, ancestors/descendants), the pruning algorithm, cost-complexity pruning and its regularization measure, and a list of advantages/limitations of decision trees. |
| [8.5-bootstrap-aggregation.md](8.5-bootstrap-aggregation.md) | 8.5 | 323-327 | Bagging: averaging predictors from bootstrapped training sets, Theorem 8.1 on expected squared-error risk, the bias-variance decomposition rationale, out-of-bag (OOB) loss estimation, and a full regression-tree bagging code example. |
| [8.6-random-forests.md](8.6-random-forests.md) | 8.6 | 327-331 | Motivates decorrelating trees via random feature subsets, the random forest construction algorithm, code examples comparing bagging vs. random forest $R^2$ scores, and the feature-importance measure. |
| [8.7-boosting.md](8.7-boosting.md) | 8.7 | 331-339 | Sequential boosting for regression (squared-error loss), gradient boosting for general differentiable losses, AdaBoost derivation and algorithm for binary classification, code examples, and the chapter's Further Reading notes. |
| [exercises.md](exercises.md) | Exercises 1-13 | 339-340 | End-of-chapter exercises covering tree fitting, impurity calculations, categorical splitting, bootstrap theory, random forests, and gradient boosting/AdaBoost proofs. |
