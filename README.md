**Project status**: _In progress_ - data visualisation phase.

This project is a data analysis of a publicly available data from: 
https://www.kaggle.com/datasets/carrie1/ecommerce-data


The project consists of cleaning data, data analysis and data modeling. All data was pushed and managed on Github via Git bash.


**Structure of the project is as follows**:

_Folder "data" consists of files:
- "data.csv" : Input data
- "cleaned_data.csv" : Data after cleaning. Script used for is in scripts/exploration_cleaning.py.
- "sales_data.db" : SQL database generated out of "sql_database.py" script. 


_Folder "scripts" covers scripts written and used for the project. Some of the code was left commented for reference:_
- "exploration_cleaning.py" : Script used for creation of the "cleaned_data.csv". Input data used from "data.csv" file. Removed unnecessary data, modified some data types and explored data for potential use.
- "data_analysis.py" : Script using "cleaned_data.csv" file. Covers data analysis, further exploration and some basic visualisation.
- "modeling.py" : Script for generating outcomes of analysis as charts. Used to generate most of them on the project.
- "sql_database.py" : Script used for generating the SQL database "sales_data.db" and covering SQL queries.

_Folder "outputs" covers charts resulted of analysis:_
- "orders_per_country.png" : Bar chart covering top 10 countries by order volume. Generated from "data_analysis.py" script.
- "orders_per_hr.png" : Line chart showing average number of orders per hour. Generated from "data_analysis.py" script.
- "orders_per_mth.png" : Line chart showing average number of orders per month. Generated from "data_analysis.py" script.
- "average_sale.png" : Histograph showing average order values.
- "product_per_order.png" : Histograph showing number of products per order.
- "sale_per_client.png" : Histograph showing average basket value per client.
- "sales_top_10.png" : Heatmap showing sales per country. Removed UK as it was a significant outlier. Covered separately in "sales_uk.png".
- "sales_uk.png" : Bar chart showing sales per month for UK only as an outlier.