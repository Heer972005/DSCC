import pandas as pd

df = pd.read_excel(r"G:\vs\DSCC\final\hallucination_bias_dataset11.xlsx")

print(df.head())
print(df.columns)
print(df.isnull().sum())

