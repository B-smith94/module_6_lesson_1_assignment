import requests
import json

#Task 2 and 3

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']
            return f"Planet: {name}\n   Mass: {mass}\n   Orbit Period: {orbit_period} days"

def find_heaviest_planet(planet_list):
    pass

planets = fetch_planet_data()

name, mass= find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")