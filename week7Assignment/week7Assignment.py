import pandas as pd

df = pd.read_csv('C:\Users\ERC\Downloads\iris')
print(df.head())
print(df.dtypes)
print(df.isnull.sum())

df_cleaned= df.dropna()  
df_cleaned = df.dropna(axis=1)

print(df.isnull.sum())