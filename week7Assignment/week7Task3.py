import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv('path_to_iris.csv', names=columns)

# Set the style of the plots (for better aesthetics)
sns.set(style="whitegrid")

# --- 1. Line Chart (Trends Over Time) ---
# In this case, we don't have time-series data, so we'll use a mock time-series.
# For demonstration, let's assume we are showing the trend of sepal length over a mock time series (just for example purposes).
time = pd.date_range('2023-01-01', periods=len(df), freq='D')
df['time'] = time

plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['sepal_length'], marker='o', color='b', label='Sepal Length')
plt.title('Sepal Length Trend Over Time')
plt.xlabel('Time')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 2. Bar Chart (Comparison of a Numerical Value Across Categories) ---
# Bar chart of the average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# --- 3. Histogram (Distribution of a Numerical Column) ---
# Histogram of the sepal length distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], kde=True, color='purple', bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# --- 4. Scatter Plot (Relationship Between Two Numerical Columns) ---
# Scatter plot of sepal length vs petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species', palette='Set1')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()


