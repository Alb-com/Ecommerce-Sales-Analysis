# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script provides a basic exploratory analysis of the raw e-commerce data to understand its structure and prepare it for further processing.

import pandas as pd

# I load the raw dataset to perform basic exploratory analysis.
df = pd.read_csv('ecommerce_sales_data.csv')

separator = "---------------------"

# I display the first five rows to understand the structure and content.
print(df.head())
print(separator)

# I print basic info about the dataset, including data types and non-null counts.
print(df.info())
print(separator)

# I generate basic statistics for the numerical columns.
print(df.describe())
print(separator)

# I check for missing values in each column.
print("Missing values per column:")
print(df.isnull().sum())