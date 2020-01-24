import json
from pprint import pprint as pp

# Load the json data from the /data folder
with open('../Data/monthlySalesByCategoryMultiple.json') as json_data:
    d = json.load(json_data)

## Print out the context
pp(d)

# Print keys at top level
print(d.keys())

# Print keys at second level
for a in d['contents']:
    print(a.keys())

# Print keys at third level
for a in d['contents']:
    for b in a['monthlySales']:
        print(b.keys())

# Print keys and values at the first level
for key, value in d.items():
    print(key + ': ', pp(value))

# Print the keys and values at the second level
for a in d['contents']:
    for key, value in a.items():
        print(key + ': ', value)

# Print the keys and values at the third level
for a in d['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            print(key + ': ', value)