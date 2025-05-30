"""
Script for creating SQL database out of generated cleaned_data.csv.
"""

import pandas as pd
import sqlite3

# Importing file with cleaned data.
url = "https://raw.githubusercontent.com/Wrobelax/sales_analysis/refs/heads/main/data/cleaned_data.csv"
df = pd.read_csv(url, encoding = "ISO-8859-1", dtype = {"InvoiceNo" : str})

conn = sqlite3.connect("../data/sales_data.db")
# df.to_sql("sales", conn, if_exists = "replace", index = False) # Uncomment to generate database.



"""SQL queries"""
# Check baqsic structure.
query_1 = """
SELECT *
FROM sales
LIMIT 10;
"""


# Number of distinct invoices per country.
query_2 = """
SELECT Country, COUNT(DISTINCT InvoiceNo) as Orders
FROM sales
GROUP BY Country
ORDER BY Orders DESC
LIMIT 10;
"""


# Number of unique clients.
query_3 = """
SELECT COUNT(DISTINCT(CustomerID)) as UniqueClient
FROM sales
WHERE CustomerID IS NOT NULL;
"""


# Average order value.
query_4 = """
SELECT AVG(TotalPerOrder) As AvgOrderValue
FROM (SELECT InvoiceNo, SUM(TotalPrice) AS TotalPerOrder
      FROM sales
      GROUP BY InvoiceNo
);
"""


# Top 10 best-selling products.
query_5 = """
SELECT Description, SUM(Quantity) as TotalSold
FROM sales
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 10;
"""


result = pd.read_sql_query(query, conn) # set proper query number to see results from the base.
print(result)