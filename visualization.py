import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs folder automatically
os.makedirs("outputs", exist_ok=True)

# Load data
df = pd.read_csv("poll_data.csv")

# Bar Chart
plt.figure(figsize=(8,5))
df["Preferred Tool"].value_counts().plot(kind='bar')
plt.title("Preferred Tool Distribution")
plt.tight_layout()
plt.savefig("outputs/bar_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
df["Preferred Tool"].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Tool Share")
plt.savefig("outputs/pie_chart.png")
plt.show()
import seaborn as sns

sns.countplot(x="Preferred Tool", hue="Gender", data=df)
plt.title("Tool Preference by Gender")
plt.savefig("outputs/gender_analysis.png")
plt.show()