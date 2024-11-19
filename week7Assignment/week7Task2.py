import pandas as pd

columns = ['sepal_length' , 'sepal_width' , 'petal_length' , 'petal_width' , 'species']
df = pd.read_csv

print("Basic Statictics: ")
print(df.describe())

grouped_data = df.groupby('species').mean()
print("\nGrouped data(Mean of numerical columns by Species):")
print(grouped_data)