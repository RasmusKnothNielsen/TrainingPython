import csv

MonthlySales = []

# Open the file and save it to our MonthlySales
# via the DictReader
with open('../Data/MonthlySales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        MonthlySales.append(row)


# Iterate through the MonthlySales and print out the values
for a in MonthlySales:
    print(a)

# Print keys
for a in MonthlySales:
    print(a.keys())


# Print keys and values
# Easier for humans to read
for a in MonthlySales:
    for key, value in a.items():
        print(key + ": ", value)
    print('\n')