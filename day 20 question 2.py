import pandas as pd

# Create the DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# 1. Filter employees from IT department
it_employees = df[df["Department"] == "IT"]

# 2. Average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()

# 3. Add Salary_Adjusted column (10% increase)
df["Salary_Adjusted"] = df["Salary"] * 1.10

# Print outputs
print("IT Department Employees:")
print(it_employees)

print("\nAverage Salary per Department:")
print(avg_salary)

print("\nFinal DataFrame with Salary_Adjusted:")
print(df)