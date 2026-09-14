# Chapter 5: Regression

Notes transcribed from *Data Science and Machine Learning* (Kroese, Botev, Taimre, Vaisman), Chapter 5.

| File | Section | Title | PDF pages | Summary |
|---|---|---|---|---|
| [5.1-introduction.md](5.1-introduction.md) | 5.1 | Introduction | 185-186 | Chapter overview: regression as supervised learning, framing linear/nonlinear/generalized linear models. |
| [5.2-linear-regression.md](5.2-linear-regression.md) | 5.2 | Linear Regression | 187-188 | Simple and multiple linear regression models; the basic setup of fitting a line/hyperplane to data. |
| [5.3-analysis-via-linear-models.md](5.3-analysis-via-linear-models.md) | 5.3 | Analysis via Linear Models | 189-199 | Least-squares estimation, model/feature selection strategies, cross-validation and PRESS (Theorem 5.1), in-sample risk and AIC, categorical features and design matrices, nested models and ANOVA decomposition, coefficient of determination $R^2$. |
| [5.4-inference-for-normal-linear-models.md](5.4-inference-for-normal-linear-models.md) | 5.4 | Inference for Normal Linear Models | 200-206 | Distributional properties of $\widehat{\boldsymbol{\beta}}$ and $\widehat{\sigma^2}$ under normal errors (Theorem 5.3); comparing nested normal linear models via the F-test (5.4.1); confidence and prediction intervals (5.4.2). |
| [5.5-nonlinear-regression-models.md](5.5-nonlinear-regression-models.md) | 5.5 | Nonlinear Regression Models | 206-209 | Strategies for nonlinear prediction functions: feature maps, response transformations (e.g., log-linearizing exponential decay), and direct nonlinear least-squares (Hougen function example). |
| [5.6-linear-models-in-python.md](5.6-linear-models-in-python.md) | 5.6 | Linear Models in Python | 209-222 | Practical `statsmodels`/`ols` workflow: specifying models with quantitative/categorical variables and interactions (5.6.1); fitting and interpreting summaries (5.6.2); ANOVA tables (5.6.3); confidence/prediction intervals via `get_prediction` (5.6.4); residual diagnostics (5.6.5); forward selection/backward elimination variable selection (5.6.6). |
| [5.7-generalized-linear-models.md](5.7-generalized-linear-models.md) | 5.7 | Generalized Linear Models | 222-225 | GLM definition with activation/link functions; logistic regression as a worked example, including cross-entropy loss, gradient/Hessian, and Newton's method for fitting. |
| [exercises.md](exercises.md) | Exercises | Exercises | 225-232 | 19 end-of-chapter exercises covering Galton/Pearson regression to the mean, Hubble's law, ANOVA model matrices, Tobit regression and EM, PRESS/leverage/Cook's distance derivations, $R^2$ monotonicity, logistic regression via gradient descent, iterative reweighted least squares, and multi-output linear regression. |
