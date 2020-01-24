import pandas as pd

df = pd.read_csv('../Data/MonthlyProductSales.csv', encoding='latin-1')

print(df)

# Yearly sales summary
print(df.groupby(df['Month of Order Date'].str[:4]).describe().reset_index()
      .rename(columns={'Month of Order Date': 'Year of Order'}))

# Yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
print(df_export.rename(columns={'Month of Order Date': 'Year of Order'}))

# Overall product sales totals
print(df.groupby('Product Name').sum().reset_index())