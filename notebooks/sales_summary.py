# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script summarizes key e-commerce metrics like total sales, average ticket, top products, and category performance, helping me analyze business performance and export results for reporting.

import pandas as pd

# I calculate the total sales by summing the 'Total' column in the DataFrame
def total_sales(df):
    return df['Total'].sum()

# I compute the average ticket size by calculating the mean of the 'Total' column
def average_ticket(df):
    return df['Total'].mean()

# I return the top N best-selling products based on the total quantity sold
def top_products(df, top_n=10):
    return df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(top_n)

# I group and sum total sales by product category, sorting them from highest to lowest
def sales_by_category(df):
    return df.groupby('Category')['Total'].sum().sort_values(ascending=False)

# I export a pandas Series to a CSV file at the specified path
def export_summary(series, path):
    series.to_csv(path)

if __name__ == "__main__":
    # I load my cleaned e-commerce dataset
    df = pd.read_csv("ecommerce_sales_data_clean2.csv")

    print("-----------------")
    print(f"Total Sales: ${total_sales(df):.2f}")  # I display the total revenue
    print("-----------------")
    print(f"Average Ticket: ${average_ticket(df):.2f}")  # I display the average ticket value
    print("-----------------")

    # I show the top products based on quantity sold
    top_product = top_products(df)
    for product, quantity in top_product.items():
        print(f"Sales by {product}: {quantity}")

    print("-----------------")

    # I show the sales by each product category
    category_sales = sales_by_category(df)
    for category, total in category_sales.items():
        print(f"Sales of {category}: ${total:.2f}")

    # I export the summarized results to CSV files
    export_summary(category_sales, "sales_by_category.csv")
    export_summary(top_product, "top_product.csv")

