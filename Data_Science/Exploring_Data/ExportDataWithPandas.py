import pandas as pd
import openpyxl

df = pd.read_csv('../Data/MonthlyProductSales.csv', encoding='cp1252')

# Yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export = df_export.rename(columns={'Month of Order Date': 'Year of Order'})
print(df_export)

# Export to csv
df_export.to_csv('../Data/YearlyProductSalesTotals.csv', header=True, index=False, encoding='utf-8')

# Export to json
df_export.to_json('../Data/YearlyProductSalesTotals.json', orient='records')

# Export to Excel
df_export.to_excel('../Data/YearlyProductSalesTotals.xlsx', header=True, index=False)