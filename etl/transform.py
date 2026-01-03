import pandas as pd

df = pd.read_csv("data/raw/ibm_hr_raw.csv")
df = df.drop_duplicates()
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

df.to_parquet("data/processed/ibm_hr_dw.parquet", index=False)
print("Transformação concluída")

