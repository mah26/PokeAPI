from fastapi import FastAPI
import requests
import json
from typing import Union
from pydantic import BaseModel

class Pokemon:
    def __init__(self, id: int, name : str, height : int, weight : int):
        self.id= id
        self.name = name
        self.height = height
        self.weight = weight

def pokedex_information(pokeapi_pokemons):
    pokemons = list()
    
    for pokemon in pokeapi_pokemons:

        pokemon_url = pokemon['url']
        pokemon_response = requests.get(pokemon_url)
        dict_pokemon_response = pokemon_response.json()

        id = dict_pokemon_response['id']
        name = dict_pokemon_response['name']
        height = dict_pokemon_response['height']
        weight = dict_pokemon_response['weight']

        pokemons.append(Pokemon(id, name, height, weight))
    
        
    return pokemons
        
app = FastAPI()

BASE_URL = "https://pokeapi.co/api/v2/pokemon?limit=50&offset=0"

pokeapi_response = requests.get(BASE_URL)

dict_pokeapi_response = pokeapi_response.json()

pokeapi_pokemons = dict_pokeapi_response['results']

pokemons = list()
pokemons = pokedex_information(pokeapi_pokemons)


@app.get("/pokemons")
def pokedex():
    return pokemons

@app.get("/pokemons/{pokemon_name}")
def pokemon_of_pokedex(pokemon_name : str):
    for pokemon in pokemons:
        if pokemon.name == pokemon_name:
            return pokemon
        
        