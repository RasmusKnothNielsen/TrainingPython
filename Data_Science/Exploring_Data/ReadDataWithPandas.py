import pandas as pd
import json
from pandas.io.json import json_normalize

# For Parquet
import pyarrow.parquet as pq

# Read the CSV file and save it to df
df = pd.read_csv('../Data/MonthlySales.csv')

print(df)
print("\n")

with open('../Data/monthlySalesByCategoryMultiple.json') as json_data:
    d = json.load(json_data)


# Format the text and append the column names at the top
df = json_normalize(d['contents'], 'monthlySales', ['category', 'region'])

print(df)

# Reading parquet into panda dataframe
table = pq.read_table('../Data/MonthlyProductSales.parquet')

print(table.to_pandas())

# Reading data from a html site
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')

print(df)

# Get part that has the states and abbreviations
df_usa = df[0]
print("\n")
print("Overview of the USA:")
print(df_usa)

# Remove the unnecessary rows and columns
final_df = df_usa.drop(df_usa.index[range(0,11)]).drop(df_usa.columns[range(3,10)], axis=1)

print(final_df)

# Rename columns
final_df.rename(columns={0: 'Region name', 1: 'Region Status', 2: 'ISO', 3: 'ANSI_Letter', 4: 'ANSI_Code'
                         , 5: 'USPS', 6: 'USCG', 7: 'GPO', 8: 'AP', 9: 'Other Abbreviations'}, inplace=True)
# Reset index of rows
final_df.reset_index(drop=True)

print(final_df)