# pip install pyarrow
## pyarrow is the Python implementation of Apache Arrow
import pyarrow.parquet as pq

table = pq.read_table('../Data/MonthlyProductSales.parquet')

# Convert the table to a python dictionary
table_dict = dict(table.to_pydict())

# Table dict is more of a columnar dictionary
print(table_dict)

# Going to convert it to a list of dictionaries
items = table_dict.items()
print(items)

# Get the keys
keys = [item[0] for item in items]
print(keys)

# Get the values
values = [item[1] for item in items]
print(values)

# Zip the values together
pivoted_values = zip(*values)
print(pivoted_values)

# Zip the column with the corresponding value then convert
# it into a dictionary then append it to an array
table_dictionary_array = []
for record in pivoted_values:
    table_dictionary_array.append(dict(zip(keys, record)))

# Print out the records
for record in table_dictionary_array:
    print(record)