import pandas as pd

#Task 1: Merging 12 months of sales data into a single file
df = pd.read_csv('Sales_Data/Sales_April_2019.csv')
print(df.head())