# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script loads raw e-commerce sales data, converts date values to datetime format, and exports a cleaned version for further analysis.

import pandas as pd

# This is the function to load raw e-commerce sales data.
# I load the data from a CSV file and convert the 'Date' column to datetime format for easier time-based analysis.
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date']) 
    return df

# I export the cleaned DataFrame to a CSV file without including the index column.
def export_clean_data(df, path):
    df.to_csv(path, index=False)  

if __name__ == "__main__":
    # Main execution block to run data import and export functions.
    df = load_data("ecommerce_sales_data.csv") 
    export_clean_data(df, "ecommerce_sales_data_clean2.csv")  
