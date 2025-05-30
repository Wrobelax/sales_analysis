"""
Script for analysing cleaned data.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid")


# Importing file with cleaned data.
url = "https://raw.githubusercontent.com/Wrobelax/sales_analysis/refs/heads/main/data/cleaned_data.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1", dtype = {"InvoiceNo" : str})



"""Data exploration/analysis"""
# # Exploring data to assess how to use them.
# print(df["Description"].nunique()) # 4005 unique descriptions.
# print(df["Country"].nunique()) # 38 unique countries.


# Checking top-selling products.
# print(df.groupby("Description")["Quantity"].sum().sort_values(ascending = False).head(10))
# Three top-selling products: "paper craft  little birdie", "medium ceramic top storage jar", "world war 2 gliders asstd designs".


# Couniting income, average price, looking for trends.
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
# print(df["TotalPrice"].sum()) # Total income 10642110.804.
# print(df.groupby("Country")["TotalPrice"].sum().sort_values(ascending = False)) # Total income per country. Top three: UK, Netherlands, Ireland (Eire).


# Average order price.
# print(df.groupby("InvoiceNo")["TotalPrice"].sum().mean()) # Average order price is around 533.


# Trends seeking by time.
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) # Changing date type.
df["Month"] = df["InvoiceDate"].dt.month
df["DayName"] = df["InvoiceDate"].dt.day_name()
# print(df.groupby("Month")["TotalPrice"].sum()) # Greatest sales are in November and December. Lowest in February and April.
# print(df.groupby("DayName")["TotalPrice"].sum()) # Sales are pretty stable across days of week. Greatest sales in Tuesday and Thursday. Lowest in Sunday.


# Checking clients.
# print(df["CustomerID"].nunique()) # 4339 Unique customer IDs. There is a group of missing IDs categorized as "missing".
# print(df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending = False).head(10))
# "Missing" IDs produce the greatest income. Top three identified customers producing the greatest income: 14646, 18102, 17450.



"""Basic visualisation"""
# Visualising most-purchased products.
top_product_sales = df.groupby("Description")["Quantity"].sum().sort_values(ascending = False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x = top_product_sales.values, y = top_product_sales.index, palette = "viridis")

plt.title("Top 10 best selling products")
plt.xlabel("Total quantity sold")
plt.ylabel("Product description")
plt.tight_layout()
# plt.savefig("data/most_purchased_prod.png")


# Orders per month.
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
monthly_orders = df.groupby("Month")["InvoiceNo"].nunique().sort_index()

plt.figure(figsize = (10,6))
sns.lineplot(data = monthly_orders)

plt.title("Orders per month")
plt.xlabel("Month")
plt.ylabel("Unique orders")
plt.tight_layout()
# plt.savefig("../outputs/orders_per_mth.png") # Saving results to file


# Hourly orders.
df["Hour"] = df["InvoiceDate"].dt.hour
hourly_orders = df.groupby("Hour")["InvoiceNo"].nunique().sort_index()

plt.figure(figsize = (10,6))
sns.lineplot(data = hourly_orders)

plt.title("Orders per hour")
plt.xlabel("Hour")
plt.ylabel("Unique orders")
plt.tight_layout()
# plt.savefig("../outputs/orders_per_hr.png") # Saving results to file


# Orders per country.
countries = df.groupby("Country")["InvoiceNo"].nunique().sort_values(ascending = False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x = countries.index, y = countries.values, palette = "viridis")

plt.title("Top 10 ordering countries")
plt.xlabel("Country")
plt.ylabel("Unique orders")
plt.xticks(rotation = 45)
plt.tight_layout()
# plt.show() # Unncomment to show plots.
# plt.savefig("../outputs/orders_per_country.png") # Saving results to file