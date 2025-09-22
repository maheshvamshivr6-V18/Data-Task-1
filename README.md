# Data-Task-1
Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats)

Customer Personality Analysis - Cleaning Submission

This repository contains a synthetic medium-sized dataset and a cleaning pipeline prepared according to the task instructions.

## Files
raw_customer_personality.csv` - raw generated dataset with issues (nulls, duplicates, inconsistent formats).
`cleaned_customer_personality.csv` - final cleaned dataset produced by the pipeline.
`cleaning_pipeline.py` - Python script that performs the cleaning steps.
`cleaning_pipeline.ipynb` - Jupyter notebook version of the cleaning pipeline.


## Summary of changes made
Renamed all column headers to lowercase and snake_case.
Removed exact duplicate rows (if any).
Standardized `gender` values to 'Male', 'Female', or 'Other'.
Standardized `country` names to common forms (USA, India, UK where possible).
Converted `join_date` to `dd-mm-yyyy` format.
Filled missing `age` with the median age of the dataset.
Filled missing `income` with the median income (or 0 if fully missing).
Ensured correct datatypes: `age` -> int, `income` -> float, `spending_score` -> int. Reset index and ensured `id` is integer type.
