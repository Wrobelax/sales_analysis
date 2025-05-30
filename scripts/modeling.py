"""
Script for data modeling and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style = "whitegrid")

# Importing file with cleaned data.
url = "https://raw.githubusercontent.com/Wrobelax/sales_analysis/refs/heads/main/data/cleaned_data.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1", dtype = {"InvoiceNo" : str})



"""Data modeling."""
# Visualisation of average order price - removing outliers.
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors = "coerce")
order_values = df.groupby("InvoiceNo")["TotalPrice"].sum()
order_values = order_values[order_values < 1000]
# print(order_values.describe())

plt.figure(figsize = (10,6))
sns.histplot(order_values, bins = 50, kde = True)
plt.title("Order values")
plt.xlabel("£")
plt.ylabel("Frequency")
plt.xlim(0,1000)
plt.tight_layout()
# plt.savefig("../outputs/average_sale.png") # Saving results to file


# Visualisation of sales per client.
client_values = df.groupby("CustomerID")["TotalPrice"].sum()
# print(client_values.describe())
top_clients = client_values.sort_values(ascending = False).head(10)
customer_total = df.groupby("CustomerID")["TotalPrice"].sum()
customer_orders = df.groupby("CustomerID")["InvoiceNo"].nunique()
avg_basket_val = customer_total / customer_orders
avg_basket_val = avg_basket_val[avg_basket_val < 1000]

plt.figure(figsize = (10,6))
sns.histplot(avg_basket_val, bins = 50, kde = True)
plt.title("Average basket value per customer")
plt.xlabel("£")
plt.ylabel("number of customers")
plt.xlim(0,1000)
plt.tight_layout()
# plt.savefig("../outputs/sale_per_client.png") # Saving results to file


# Visualisation of products per order.
product_per_order = df.groupby("InvoiceNo")["Quantity"].sum()
product_per_order = product_per_order[product_per_order < 1000]

plt.figure(figsize = (10,6))
sns.histplot(product_per_order, bins = 50, kde = True)
plt.title("Number of products per order")
plt.xlabel("Items")
plt.ylabel("Frequency")
plt.xlim(0,1000)
plt.tight_layout()
# plt.savefig("../outputs/product_per_order.png") # Saving results to file


# Visualisation of sales basing on month and country - Separated UK and top 10 countries.
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

df_other = df[df["Country"] != "united kingdom"]

top_other = df_other.groupby("Country")["TotalPrice"].sum().sort_values(ascending = False).head(10).index
df_other_top = df_other[df_other["Country"].isin(top_other)]
other_pivot = df_other_top.pivot_table(index = "Country", columns = "Month", values = "TotalPrice", aggfunc = "sum").fillna(0)

other_table_log = np.log1p(other_pivot) # Using log scale to add 1 and avoid log(0)

plt.figure(figsize = (12,6))
sns.heatmap(other_table_log, cmap = "YlGnBu", linewidths = 0.5, annot = True, fmt = ".1f")
plt.title("Sales per Country/Month - top 10")
plt.xlabel("Month")
plt.ylabel("Country")
plt.tight_layout()
# plt.savefig("../outputs/sales_top_10.png") # Saving results to file


#Visualisation of sales basing on month and country - UK only.
df_uk = df[df["Country"] == "united kingdom"]
uk_monthly_sales = df_uk.groupby("Month")["TotalPrice"].sum().sort_index()

plt.figure(figsize= (12,6))
sns.barplot(x = uk_monthly_sales.index, y = uk_monthly_sales.values, palette = "Blues_d")

plt.title("Sales per Country/Month - UK")
plt.xlabel("Month")
plt.ylabel("£")
plt.xticks(rotation = 45)
plt.tight_layout()
# plt.savefig("../outputs/sales_uk.png") # Saving results to file