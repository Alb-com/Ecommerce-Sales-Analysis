# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script extracts sales trends over time from the e-commerce dataset and exports the data for visualization or further analysis.

import pandas as pd

df = pd.read_csv('ecommerce_sales_data.csv')  

trend_serie = df[['Date', 'Total', 'Quantity']] 

trend_serie.to_csv("trend_graphic.csv", index=False)  
