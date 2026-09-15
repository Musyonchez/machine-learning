"""
Chapter 1 - Importing, Summarizing, and Visualizing Data
Exercise 2

Notes: notes/ch01-importing-summarizing-visualizing-data/exercises.md

TODO: transcribe the runnable code for this exercise here (if it requires code).
"""

import pandas as pd

# Load the nutri data set fresh from its source.
nutri = pd.read_excel('http://www.biostatisticien.eu/springeR/nutrition_elderly.xls')

# Label dictionaries per Table 1.2.
GENDER_DICT = {1: 'Male', 2: 'Female'}
SITUATION_DICT = {1: 'Single', 2: 'Couple', 3: 'Family', 4: 'Other'}
FREQ_DICT = {
    0: 'Never',
    1: 'Less than once a week',
    2: 'Once a week',
    3: '2-3 times a week',
    4: '4-6 times a week',
    5: 'Every day',
}
FAT_DICT = {
    1: 'butter',
    2: 'margarine',
    3: 'peanut',
    4: 'sunflower',
    5: 'olive',
    6: 'Isio4',
    7: 'colza',
    8: 'duck',
}

# Categorical features.
nutri['gender'] = nutri['gender'].replace(GENDER_DICT).astype('category')
nutri['situation'] = nutri['situation'].replace(SITUATION_DICT).astype('category')
nutri['fat'] = nutri['fat'].replace(FAT_DICT).astype('category')

for col in ['meat', 'fish', 'raw_fruit', 'cooked_fruit_veg', 'chocol']:
    nutri[col] = nutri[col].replace(FREQ_DICT).astype('category')

# Float features.
nutri['height'] = nutri['height'].astype(float)
nutri['weight'] = nutri['weight'].astype(float)
nutri['age'] = nutri['age'].astype(float)

# Integer features (no recoding needed).
nutri['tea'] = nutri['tea'].astype(int)
nutri['coffee'] = nutri['coffee'].astype(int)

print("Recoded dtypes:")
print(nutri.dtypes)

n_categorical = (nutri.dtypes == 'category').sum()
n_float = (nutri.dtypes == 'float64').sum()
n_int = (nutri.dtypes == 'int64').sum()
print(
    f"\nSummary: {n_categorical} categorical + {n_float} float + {n_int} int "
    f"= {n_categorical + n_float + n_int} columns"
)

nutri.to_csv('nutri_recoded.csv', index=False)
print("\nSaved recoded data set to 'nutri_recoded.csv'")
