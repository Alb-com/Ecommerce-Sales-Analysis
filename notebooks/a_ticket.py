# e-commerce_data_analysis_comas_Albert
# contact: albertcomaas@gmail.com
# datascience_project

# This script calculates the average purchase amount (average ticket) from the e-commerce dataset and exports the result for reporting.

import pandas as pd

df = pd.read_csv("ecommerce_sales_data_clean2.csv")

# Calculate average ticket
a_ticket = df['Total'].mean()

# Convert float to a Series
a_ticket_series = pd.Series([a_ticket], name="Average_Ticket")

def export_summary(series, path):
    series.to_csv(path, index=False)


export_summary(a_ticket_series, "a_ticket.csv")


print("Average Ticket:", a_ticket)
print(df)