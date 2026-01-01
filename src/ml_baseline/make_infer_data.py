import pandas as pd

df = pd.read_parquet("data/processed/features.parquet")
df.drop(columns=["grade"], inplace=True)
df.to_csv("data/processed/features_infer.csv", index=False)

