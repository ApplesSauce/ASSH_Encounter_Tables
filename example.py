import json
from pprint import pprint

with open('abbica_mere.json') as data_file:
    data = json.load(data_file)

#pprint(data["location"])
#pprint(data["encounter"][0])
#pprint(data["encounter"])

for entry in data['encounter']:
    if entry['roll'] == '3':
        pprint(entry)
        print(json.dumps(entry, sort_keys=True, indent=4))
