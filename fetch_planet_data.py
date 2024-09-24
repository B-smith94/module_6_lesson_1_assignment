import requests

#Task 2

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}\n   Mass: {mass}\n   Orbit Period: {orbit_period} days")

fetch_planet_data()

#Task 3

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_dict = {}
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            planet_dict.update({name: mass})
    return planet_dict

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key = planets.get)
    return heaviest_planet, planets[heaviest_planet]
            
planets = fetch_planet_data()

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")