import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# -----------------------------
# 1️. Matplotlib Line Chart
# -----------------------------
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Report - Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales (in INR)")
plt.grid(True)
plt.show()


# -----------------------------
# 2️. Seaborn Bar Plot
# -----------------------------
plt.figure()
sns.barplot(x=months, y=sales)
plt.title("Monthly Sales Report - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales (in INR)")
plt.grid(True)
plt.show()