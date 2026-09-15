"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 3

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import pandas as pd

# Table 1.3: test scores of 5 students before and after specialized tuition.
scores_wide = pd.DataFrame({
    'Student': [1, 2, 3, 4, 5],
    'Before': [75, 30, 100, 50, 60],
    'After': [85, 50, 100, 52, 65],
})

print("Original (wide) format:")
print(scores_wide)

# Reshape to standard/long format with three features: Score, Time, Student.
scores_long = pd.melt(
    scores_wide,
    id_vars='Student',
    value_vars=['Before', 'After'],
    var_name='Time',
    value_name='Score',
)

print("\nReshaped (long/standard) format:")
print(scores_long)
