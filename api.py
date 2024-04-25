import requests
import json
response_API = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

data = response_API.text
parse_json = json.loads(data)

print(parse_json)