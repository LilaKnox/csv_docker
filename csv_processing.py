import pandas as pd
import os

data_path = "airports.csv"
airport_df = pd.read_csv(data_path, on_bad_lines="skip")

print(type(airport_df))
print(airport_df.head())

print("\n", "-" * 50, "\n")

cleaned_df = airport_df.drop(["state"], axis=1)

print(cleaned_df.head())

print("\n", "-" * 50, "\n")

print(airport_df["city"].head())

print("\n", "-" * 50, "\n")

print(airport_df.sort_values("lat", ascending=False))
