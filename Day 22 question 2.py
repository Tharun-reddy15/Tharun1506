import pandas as pd
import numpy as np

# Load CSV file
df = pd.read_csv("sales.csv")

print("Original Data:")
print(df)

# Add Total column
df["Total"] = df["Quantity"] * df["Price"]

print("\nData with Total column:")
print(df)

# Convert Total column to NumPy array
daily_sales = np.array(df["Total"])

# Total Sales
total_sales = np.sum(daily_sales)

# Average Daily Sales
average_sales = np.mean(daily_sales)

# Standard Deviation of Daily Sales
std_deviation = np.std(daily_sales)

print("\nSales Statistics:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_sales)
print("Standard Deviation:", std_deviation)

# Group by Product and sum Quantity
product_sales = df.groupby("Product")["Quantity"].sum()

# Get product with maximum quantity sold
best_product = product_sales.idxmax()
best_quantity = product_sales.max()

print("\nBest Selling Product:")
print("Product:", best_product)
print("Total Quantity Sold:", best_quantity)