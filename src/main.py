import json

with open('./strings.json') as file:
    data = json.load(file)

print(data["languages"])
