import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Load CSV (replace 'sales.csv' with your file name)
df = pd.read_csv('sales.csv')
print(df.head())
print(df.info())

# 2) Basic checks
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 3) Data cleaning example
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.drop_duplicates()
df = df.dropna(subset=['Sales', 'Date'])

# 4) Feature engineering
df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)

# 5) Summaries
total_sales = df['Sales'].sum()
total_qty = df['Quantity'].sum()
n_products = df['Product'].nunique()

print("Total sales:", total_sales)
print("Total quantity:", total_qty)
print("Unique products:", n_products)

# 6) Groupby examples
sales_by_product = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
monthly_sales = df.groupby('YearMonth')['Sales'].sum().sort_index()

# 7) Plots

# Top-10 products
top10 = sales_by_product.head(10)
top10.plot(kind='bar', figsize=(10,5), title='Top 10 Products by Sales')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly sales trend
monthly_sales.plot(kind='line', marker='o', figsize=(10,4), title='Monthly Sales Trend')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by category
sales_by_category.plot(kind='barh', figsize=(8,6), title='Sales by Category')
plt.xlabel('Sales')
plt.tight_layout()
plt.show()

# 8) Save outputs
df.to_csv('cleaned_sales.csv', index=False)
sales_by_product.to_csv('sales_by_product.csv')
print("Analysis completed and files saved.")
