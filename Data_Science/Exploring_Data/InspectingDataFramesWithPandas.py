import pandas as pd

# Read the file and print the content
df = pd.read_csv('../Data/MonthlySales.csv')
print(df)

# Print the first 10 entries from the CSV
print(df.head(n=10))

# Print the last 10 entries from the CSV
print(df.tail(n=10))

# Show summary stats of the sales column
print(df.describe())

# Print general info about the DataFrame
print(df.info())

# Return as a series
s = df['month']

# Get the count of each individual value
print(s.value_counts(dropna=False))