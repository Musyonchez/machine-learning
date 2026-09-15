# Chapter 3: Monte Carlo Methods — code

Runnable code examples mirroring [`notes/ch03-monte-carlo-methods/`](../../notes/ch03-monte-carlo-methods/README.md).

| Folder | Files |
|---|---|
| [3.1-introduction/](3.1-introduction/) | 3.1-introduction.py |
| [3.2-monte-carlo-sampling/](3.2-monte-carlo-sampling/) | 3.2.1-generating-random-numbers.py, 3.2.2-simulating-random-variables.py, 3.2.2.1-inverse-transform-method.py, 3.2.2.2-acceptance-rejection-method.py, 3.2.3-simulating-random-vectors-and-processes.py, 3.2.4-resampling.py, 3.2.5.1-metropolis-hastings-sampler.py, 3.2.5.2-gibbs-sampler.py |
| [3.3-monte-carlo-estimation/](3.3-monte-carlo-estimation/) | 3.3.1-crude-monte-carlo.py, 3.3.2-bootstrap-method.py, 3.3.3-variance-reduction.py |
| [3.4-monte-carlo-for-optimization/](3.4-monte-carlo-for-optimization/) | 3.4.1-simulated-annealing.py, 3.4.2-cross-entropy-method.py, 3.4.3-splitting-for-optimization.py, 3.4.4-noisy-optimization.py |
| [exercises/](exercises/) | exercise-01.py, exercise-02.py, exercise-03.py, exercise-04.py, exercise-05.py, exercise-06.py, exercise-07.py, exercise-08.py, exercise-09.py, exercise-10.py, exercise-11.py, exercise-12.py, exercise-13.py, exercise-14.py, exercise-15.py, exercise-16.py, exercise-17.py, exercise-18.py, exercise-19.py, exercise-20.py, exercise-21.py, exercise-22.py, exercise-23.py |

## Coverage notes

- 3.2.1 (random number generation theory), 3.2.2.1 (inverse-transform, purely analytical in this section), and 3.4.3 (splitting for optimization — Example 3.17 is discussed but no code is shown) have no book-given code; those files say so.
- The book chains several of its own scripts via `from X import *`; since files here must be independent, each dependent file inlines the full chain instead:
  - `3.4.2-cross-entropy-method.py` inlines the `wiggly` function from `simann.py` (3.4.1).
  - `3.3.3-variance-reduction.py` inlines the crude-MC setup from `mcint.py` (3.3.1) for its control-variate part.
  - `3.4.4-noisy-optimization.py` inlines both `stochapprox.py`→`stochcounterpart.py` and `Snoisy.py`→`CEnoisy.py` chains (renaming variables to avoid collisions between the two parts sharing one file).
- Exercise 10's Markov chain transition matrix (Figure 3.17) could not be recovered precisely from the source notes (a diagram description) — the file uses a clearly-flagged placeholder matrix (row-stochastic, verified programmatically) rather than fabricated "exact" values.
- Exercises 18 and 19 reference external datasets/files (a Hougen-function dataset, and a downloaded `Sento1.dat` knapsack file) that aren't available in this repo — both use a small synthetic stand-in instance instead, clearly documented in the file.

## Status

**Implemented and verified.** All 39 files (16 section files + 23 exercises) were actually executed end-to-end (`MPLBACKEND=Agg`, exit code checked) — all pass. Two real bugs were caught this way and fixed: a NumPy 2.x array-construction issue in `3.4.1-simulated-annealing.py`, and a shape bug in `3.4.2-cross-entropy-method.py` where averaging over the wrong axis turned scalar `mu`/`sigma` into vectors and broke the convergence check.
