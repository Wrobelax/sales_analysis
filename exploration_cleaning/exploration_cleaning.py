"""
File importing dataset, exploring it and preparing data for use.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""

import pandas as pd

# Importing initial data and loading to DataFrame
url = 'https://raw.githubusercontent.com/Wrobelax/sales_analysis/refs/heads/master/data/data.csv'
df = pd.read_csv(url, encoding ='ISO-8859-1')


"""Data exploration."""
# # Exploring data to asses what needs to be cleaned.
# print(df.info()) # 541909 rows in total.
# print(df.isnull().sum()) # CustomerID column almost empty, Description column missing 1454 entries.
# print(df['InvoiceDate'].dtype) # Date is object, requires conversion.
# print(df['Quantity'].dtype) # Correct dtype (int64)
# print(df['UnitPrice'].dtype) # Correct dtype (float64)
# print(df[df["Quantity"] <= 0]) # 10624 rows with quantity <= 0. Potential purchase return. To be removed.
# print(df[df["UnitPrice"] <= 0]) # 2517 rows with unit price <= 0. To be removed.
# print(df.duplicated().sum()) # 5268 duplicated entries. To be removed.

# # Checking unique data.
# print(df["Description"].unique()) # All written in caps, potential trailing spaces, special characters.
# print(df["Country"].unique()) # Mix of capitalized and all caps (USA,RPA).


"""Data cleaning, filling, converting and removing."""
# Cleaning the data - removing trailing spaces and converting everything to lower letters. Removing special characters.
df["Description"] = df["Description"].str.strip() # Removing trailing spaces.
df["Description"] = df["Description"].str.lower() # Lowering Letters.
df["Description"] = df["Description"].str.replace("[^a-zA-Z0-9 ]", "", regex = True) # Removing special characters.

df["Country"] = df["Country"].str.strip() # Removing trailing spaces.
df["Country"] = df["Country"].str.lower()# Lowering Letters.

# Filling empty data.
df["Description"] = df["Description"].fillna("missing")
df["CustomerID"] = df["CustomerID"].fillna("missing")


# Converting the data.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) # Converting date to proper format.
df["CustomerID"] = df["CustomerID"].astype("str") # Changing type to str because missing data was filled with "missing".
df["InvoiceNo"] = df["InvoiceNo"].astype("str") # Changing to str for easier identification.


# Removing unnecessary data.
df = df[df["Quantity"] > 0] # Removing returned purchases.
df = df[df["UnitPrice"] > 0] # Removing unit price <= 0.
df = df.drop_duplicates()


# Saving cleared data to csv.
df.to_csv("https://github.com/Wrobelax/sales_analysis/blob/e919a7b403f0477965f72d0d7b8525aea97ced49/data/cleaned_data.csv", index = False)