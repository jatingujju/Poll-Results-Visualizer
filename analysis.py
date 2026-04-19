import pandas as pd

df = pd.read_csv("poll_data.csv")

# Count votes
print(df["Preferred Tool"].value_counts())

# Percentage
percentage = df["Preferred Tool"].value_counts(normalize=True) * 100
print("\nPercentage:\n", percentage)