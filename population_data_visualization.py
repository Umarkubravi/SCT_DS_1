# -----------------------------
# TASK 01 - Population Visualization (Final Clean Version)
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("population.csv", skiprows=4)

# Get all year columns
year_cols = [col for col in df.columns if col.isdigit()]

# Find last valid year (non-empty)
for col in reversed(year_cols):
    if df[col].notna().sum() > 0:
        year = col
        break

print("Using Year:", year)

# Remove missing values
population = df[year].dropna()

# -----------------------------
# Histogram (Log Scale)
# -----------------------------
log_population = np.log10(population)

plt.figure(figsize=(8,5))
sns.histplot(log_population, bins=30, kde=True)
plt.title(f"Log Population Distribution ({year})")
plt.xlabel("Log10 Population")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Bar Chart (Top 10 Countries - in Millions)
# -----------------------------
top10 = df[['Country Name', year]].dropna().sort_values(by=year, ascending=False).head(10)

# Convert to millions
top10['Population (Millions)'] = top10[year] / 1e6

plt.figure(figsize=(10,5))
sns.barplot(x='Population (Millions)', y='Country Name', data=top10)
plt.title(f"Top 10 Countries by Population ({year})")
plt.xlabel("Population (Millions)")
plt.ylabel("Country")
plt.show()

print("\nTask 01 Completed Successfully!")

input("Press Enter to exit...")