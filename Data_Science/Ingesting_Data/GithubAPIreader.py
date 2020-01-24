import requests
import json
from pprint import pprint as pp
import base64

# For CSV handling
import csv
import io

# Request the data from a webpage
response = requests.get('https://api.github.com/repos/bsullins/data/contents/monthlySalesbyCategoryMultiple.json')

# Load the response as JSON and save it
response_json = json.loads(response.text)

# Decode the response with base62 decoding, and save it as value
value = json.loads(base64.b64decode(response_json['content']))
pp(value)


# Print the keys and values at the third level
for a in value['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            print(key + ": ", value)

# Playing around with CSV
response = requests.get('https://api.github.com/repos/bsullins/data/contents/MonthlySales.csv')

# Load the response text into json format
response_json = json.loads(response.text)

# Decode this via Base64
csv_value = base64.b64decode(response_json['content'])

# Using csv.DictReader needs a filestream so we're making an String I/O and passing a unicode string in
# Then reading the stream and adding each dictionary to the dictionary list
#csv_dict = csv.DictReader(io.StringIO(csv_value))
dict_list = []
for a in csv_value['contents']:
    dict_list.append(a)


for a in dict_list:
    print(a)
    print("\n")
