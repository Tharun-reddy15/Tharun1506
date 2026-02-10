import pandas as pd
import numpy as np

# Given data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

# 1. Convert list of dictionaries to DataFrame
df = pd.DataFrame(students)

# 2. Use NumPy to calculate statistics
scores = df["score"].values

mean_score = np.mean(scores)
median_score = np.median(scores)
std_deviation = np.std(scores)   # population standard deviation

# 3. Add above_average column
df["above_average"] = df["score"] > mean_score

# Print results
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Standard Deviation:", std_deviation)
print("\nFinal DataFrame:")
print(df)