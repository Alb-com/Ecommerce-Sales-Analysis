# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script calculates the total e-commerce sales and exports the result as a CSV file for reporting or further analysis.

import pandas as pd

df = pd.read_csv("ecommerce_sales_data_clean2.csv")  

total_sales = df['Total'].sum()  
total_sales_series = pd.Series([total_sales], name="Total_Sales")  

# This export the given Series to a CSV file without the index
def export_summary(series, path):
    series.to_csv(path, index=False)

export_summary(total_sales_series, "total_sales.csv")  

