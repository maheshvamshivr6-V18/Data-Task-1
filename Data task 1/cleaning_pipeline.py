# cleaning_pipeline.py
# This script applies a cleaning pipeline to the raw_customer_personality.csv dataset.
import pandas as pd, numpy as np
df = pd.read_csv("raw_customer_personality.csv")
# Steps: rename columns, drop duplicates, standardize gender/country, format dates, fill missing values, enforce dtypes
df.rename(columns={c: c.strip().lower().replace(" ", "_") for c in df.columns}, inplace=True)
df.drop_duplicates(inplace=True)
gender_map = {'m': 'Male', 'male': 'Male', 'male ': 'Male', 'M': 'Male', 'Male': 'Male', 'f': 'Female', 'female': 'Female', 'F': 'Female', 'Female': 'Female'}
df['gender'] = df['gender'].astype(str).str.strip().str.lower().map(gender_map).fillna("Other")
country_map = {'usa': 'USA', 'u.s.a.': 'USA', 'us': 'USA', 'united states': 'USA', 'india': 'India', 'india ': 'India', 'ind': 'India', 'uk': 'UK', 'united kingdom': 'UK', 'great britain': 'UK'}
df['country'] = df['country'].astype(str).str.strip().str.lower().map(country_map).fillna(df['country'].astype(str).str.title())
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce').dt.strftime('%d-%m-%Y')
median_age = int(df['age'].median(skipna=True)) if df['age'].notna().any() else 30
df['age'] = df['age'].fillna(median_age).astype(int)
if 'income_($)' in df.columns:
    df.rename(columns={'income_($)':'income'}, inplace=True)
if df['income'].isnull().any():
    median_income = float(df['income'].median(skipna=True)) if df['income'].notna().any() else 0.0
    df['income'] = df['income'].fillna(median_income)
df['income'] = df['income'].astype(float)
df.to_csv("cleaned_customer_personality.csv", index=False)
print("Saved cleaned_customer_personality.csv")
