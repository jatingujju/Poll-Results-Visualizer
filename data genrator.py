import pandas as pd
import numpy as np

# Number of responses
n = 300

df = pd.DataFrame({
    "Timestamp": pd.date_range(start="2024-04-01", periods=n, freq='H'),
    "Age Group": np.random.choice(["18-24", "25-34", "35-44"], n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Preferred Tool": np.random.choice(["Python", "Excel", "R"], n, p=[0.5, 0.3, 0.2]),
    "Satisfaction": np.random.randint(1, 6, n),
    "Feedback": np.random.choice(
        ["Excellent", "Good", "Average", "Needs Improvement"], n)
})

df.to_csv("poll_data.csv", index=False)

print("✅ Dataset created!")
print(df.head())