import requests
import json
#Task 1: See myenv

#Task 2 and 3:

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://www.pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data = response.text
    pokemon_data = json.loads(json_data)
    return pokemon_data['name'], pokemon_data['abilities'], pokemon_data['weight']


def calculate_average_weight(pokemon_list):
    for name in pokemon_list:
        pokemon_data = fetch_pokemon_data(name)
    return sum(pokemon_data["weight"]) / len(pokemon_data["weight"])

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

print(calculate_average_weight(pokemon_names))

