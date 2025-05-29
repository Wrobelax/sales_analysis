import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = "whitegrid")

# Importing file with cleaned data.
url = "https://raw.githubusercontent.com/Wrobelax/sales_analysis/refs/heads/main/data/cleaned_data.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1", dtype = {"InvoiceNo" : str})



"""Data modeling."""
# Visualisation of average order price - removing outliers.
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
order_values = df.groupby("InvoiceNo")["TotalPrice"].sum()
order_values = order_values[order_values < 1000]
order_values = order_values[order_values > 1]
# print(order_values.describe())

# plt.figure(figsize = (10,6))
# sns.histplot(order_values, bins = 50, kde = True)
# plt.title("Order values")
# plt.xlabel("£")
# plt.ylabel("Frequency")
# plt.tight_layout()
# plt.savefig("https://github.com/Wrobelax/sales_analysis.git/outputs/average_sale.png") # Saving results to file


# Visualisation of sales per client.
client_values = df.groupby("CustomerID")["TotalPrice"].sum()
# print(client_values.describe())
top_clients = client_values.sort_values(ascending = False).head(10)
customer_total = df.groupby("CustomerID")["TotalPrice"].sum()
customer_orders = df.groupby("CustomerID")["InvoiceNo"].nunique()
avg_basket_val = customer_total / customer_orders
avg_basket_val = avg_basket_val[avg_basket_val > 1]
avg_basket_val = avg_basket_val[avg_basket_val < 1000]

plt.figure(figsize = (10,6))
sns.histplot(avg_basket_val, bins = 50, kde = True)
plt.title("Average basket value per customer")
plt.xlabel("£")
plt.ylabel("number of customers")
plt.tight_layout()
# plt.show()
# plt.savefig("C:\\Users\\adiw\\PycharmProjects\\Kurs\\sales_analysis\\outputs\\sale_per_client.png") # Saving results to file