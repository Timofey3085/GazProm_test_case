from pprint import pprint

import requests

json_data = requests.get('https://swapi.dev/api/people/').json()

results = json_data['results']

t = []

for character in results:
    tabl = f"{character['name']:20} | {character['birth_year']:10} | {character['eye_color']}"
    t.append(tabl)


pprint(results)
pprint(t)
