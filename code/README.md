# Book Code

Runnable Python code for every code example in *Data Science and Machine Learning: Mathematical and Statistical Methods* (Kroese, Botev, Taimre, Vaisman), organized to mirror [`notes/`](../notes/README.md) one-to-one.

## Convention

- One top-level folder per chapter/appendix, matching the `notes/` folder names exactly (e.g. `ch01-importing-summarizing-visualizing-data/`).
- Inside each chapter folder, one sub-folder per section — matching each `.md` file in that chapter's notes folder (e.g. `notes/.../1.5-visualizing-data.md` → `code/.../1.5-visualizing-data/`).
- Inside each section folder, one `.py` file per subsection (e.g. `1.5.1-plotting-qualitative-variables.py`, `1.5.2.1-boxplot.py`). If a section has no numbered subsections, it gets a single `.py` file named after the section itself, holding all of that section's code.
- Each chapter's `exercises/` folder gets one `.py` file per exercise (`exercise-01.py`, `exercise-02.py`, ...), not one combined file — matching the granularity of everything else.
- Every `.py` file starts with a header comment identifying the chapter/section, the source PDF pages, and a link back to the matching notes file — so code and explanation stay cross-referenced.

This mirrors the book's own numbering exactly, so any code example can be found by its section number alone, in both `notes/` and `code/`.

## Implementing a chapter (read this before starting one)

This is the playbook Chapter 1 was built with. Follow it for chapters 2-9 and appendices A-D.

1. **Read the chapter's notes files first, fully.** Everything needed (exact code snippets, dataset names/URLs, any tables the book uses for recoding) is already in `notes/<chapter>/*.md` — no need to touch the PDF.
2. **Write code and boilerplate together, in one pass per file.** Don't do a bare-snippets pass now and a "make it runnable" pass later — that means touching every file twice and risks the two versions drifting apart. Each file should be complete and runnable the moment you write it.
3. **Every file must be independent** — its own imports, its own data loading/prep, no importing another file in `code/`. This means repeating boilerplate (e.g. loading and recoding the same dataset) across multiple files in the same section folder is correct, not a smell.
4. **Load datasets from their public URL, not a local pre-download.** Match what the book does when it already uses a URL (Rdatasets, etc.); when the book has the reader manually download a file first (e.g. UCI datasets), substitute the dataset's stable direct-download URL instead so the script needs nothing pre-staged. The only acceptable exception is a dataset genuinely too large to fetch automatically (see Exercise 7 in ch01 — gigabytes, needs a manual download) — guard that code behind `if __name__ == '__main__':` with a clear comment, but still write it out faithfully.
5. **When the book defers something (e.g. "see Exercise 2" for the rest of a recoding scheme) but a later section's demo output depends on it existing, derive it yourself from what the book *does* give** (a table, a formula) — never invent labels or numbers. Then verify by running the code and diffing your output against the book's own printed output/counts. If it doesn't match exactly, your derivation is wrong, not the book's.
6. **Actually run every file before calling it done — syntax-checking is not enough.** `py_compile` only catches syntax errors; it will not catch a dataset's column names having changed upstream, an off-by-one in a generated array, a wrong URL, etc. Run every single file (use a headless matplotlib backend, `MPLBACKEND=Agg`, for plotting files so they don't block) and check the actual output/exit code. This is how the ch01 pass caught that Rdatasets now exports its CSV index column as `rownames` instead of leaving it blank (pandas used to auto-name that `Unnamed: 0`, which is what the book-era code assumes) — 5 files silently would have been broken if only syntax-checked. Handle both names defensively: `index_col = 'rownames' if 'rownames' in df.columns else 'Unnamed: 0'`.
7. **Clean up after verification runs.** Delete any `__pycache__/`, generated `.csv`/`.png` files, etc. before committing — `git status` should show only the `.py`/`.md` files you meant to change.
8. **Update the chapter's own `code/<chapter>/README.md`** (status line, and an "Independence" section if the chapter shares recoding dictionaries or similar across files, following ch01's README as the template) and the chapter row here in the top-level table/Status section.
9. **Commit with a message that says what was actually verified**, not just what was written (e.g. name which files were run, what matched the book's output, what bugs were found and fixed) — then push.

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

- Every `.py` file is fully standalone (its own imports, its own data loading/preparation) and never imports another file in this repo — see [ch01's README](ch01-importing-summarizing-visualizing-data/README.md#independence) for how shared things like dataset recoding are handled without cross-file dependencies.

## Status

**Chapter 1 implemented** (19/19 files, verified via syntax checks and live smoke tests — see its [README](ch01-importing-summarizing-visualizing-data/README.md) for details). Chapters 2-9 and appendices A-D are still framework only — every file a stub with a source-reference header comment, no code transcribed in yet.
