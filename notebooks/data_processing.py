# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

import pandas as pd

# I load the data from a CSV file and convert the 'Date' column to datetime format for easier time-based analysis.
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# I export the cleaned DataFrame to a CSV file without including the index column.
def export_clean_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = load_data("ecommerce_sales_data.csv")
    export_clean_data(df, "ecommerce_sales_data_clean2.csv")


