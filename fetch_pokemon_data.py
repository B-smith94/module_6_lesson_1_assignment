import requests
import json
#Task 1: See myenv

#Task 2:
response = requests.get(f'https://www.pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text
pokemon_data = json.loads(json_data)
print(f"Name: {pokemon_data['name']}\n{pokemon_data['abilities']}")

#Task 3:

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://www.pokeapi.co/api/v2/pokemon/{pokemon_name}')
    json_data = response.text
    pokemon_data = json.loads(json_data)
    return pokemon_data['name'], pokemon_data['abilities'], pokemon_data['weight']


def calculate_average_weight(pokemon_list):
    pokemon_weight = []
    for name in pokemon_list:
        pokemon_data = fetch_pokemon_data(name)
        pokemon_weight.append(pokemon_data[-1])
    return sum(pokemon_weight) / len(pokemon_weight)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

print(f"Average Weight of {pokemon_names}: {calculate_average_weight(pokemon_names)}")