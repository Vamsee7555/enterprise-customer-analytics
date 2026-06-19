import pandas as pd

df = pd.read_csv("data/fact_customers.csv")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())