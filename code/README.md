# Book Code

Runnable Python code for every code example in *Data Science and Machine Learning: Mathematical and Statistical Methods* (Kroese, Botev, Taimre, Vaisman), organized to mirror [`notes/`](../notes/README.md) one-to-one.

## Convention

- One top-level folder per chapter/appendix, matching the `notes/` folder names exactly (e.g. `ch01-importing-summarizing-visualizing-data/`).
- Inside each chapter folder, one sub-folder per section — matching each `.md` file in that chapter's notes folder (e.g. `notes/.../1.5-visualizing-data.md` → `code/.../1.5-visualizing-data/`).
- Inside each section folder, one `.py` file per subsection (e.g. `1.5.1-plotting-qualitative-variables.py`, `1.5.2.1-boxplot.py`). If a section has no numbered subsections, it gets a single `.py` file named after the section itself, holding all of that section's code.
- Each chapter's `exercises/` folder gets one `.py` file per exercise (`exercise-01.py`, `exercise-02.py`, ...), not one combined file — matching the granularity of everything else.
- Every `.py` file starts with a header comment identifying the chapter/section, the source PDF pages, and a link back to the matching notes file — so code and explanation stay cross-referenced.

This mirrors the book's own numbering exactly, so any code example can be found by its section number alone, in both `notes/` and `code/`.

## Chapters and appendices

| Chapter/Appendix | Folder |
|---|---|
| 1. Importing, Summarizing, and Visualizing Data | [ch01-importing-summarizing-visualizing-data/](ch01-importing-summarizing-visualizing-data/README.md) |
| 2. Statistical Learning | [ch02-statistical-learning/](ch02-statistical-learning/README.md) |
| 3. Monte Carlo Methods | [ch03-monte-carlo-methods/](ch03-monte-carlo-methods/README.md) |
| 4. Unsupervised Learning | [ch04-unsupervised-learning/](ch04-unsupervised-learning/README.md) |
| 5. Regression | [ch05-regression/](ch05-regression/README.md) |
| 6. Regularization and Kernel Methods | [ch06-regularization-and-kernel-methods/](ch06-regularization-and-kernel-methods/README.md) |
| 7. Classification | [ch07-classification/](ch07-classification/README.md) |
| 8. Decision Trees and Ensemble Methods | [ch08-decision-trees-and-ensemble-methods/](ch08-decision-trees-and-ensemble-methods/README.md) |
| 9. Deep Learning | [ch09-deep-learning/](ch09-deep-learning/README.md) |
| A. Linear Algebra and Functional Analysis | [appA-linear-algebra-and-functional-analysis/](appA-linear-algebra-and-functional-analysis/README.md) |
| B. Multivariate Differentiation and Optimization | [appB-multivariate-differentiation-and-optimization/](appB-multivariate-differentiation-and-optimization/README.md) |
| C. Probability and Statistics | [appC-probability-and-statistics/](appC-probability-and-statistics/README.md) |
| D. Python Primer | [appD-python-primer/](appD-python-primer/README.md) |

## Status

Framework complete for all chapters (1-9) and appendices (A-D) — every file is a stub with a source-reference header comment, no code transcribed in yet. Chapter 1 was hand-built as the pilot; the rest were scaffolded the same way directly from the notes' section structure (no PDF reading needed for this step).
