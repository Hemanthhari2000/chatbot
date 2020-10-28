import json

data_file = open('data\intents.json').read()
intents = json.loads(data_file)


print(intents)
