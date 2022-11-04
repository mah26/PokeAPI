from main import app
from fastapi.testclient import TestClient
import json

client = TestClient(app)

def test_read_main():
    response = client.get("/pokemons")
    assert response.status_code == 200

def test_given_pokemon_name_when_call_api_then_comprove_if_exists():
    response = client.get("/pokemons/ivysaur")
    assert {
        "id": 2,
        "name": "ivysaur",
        "height": 10,
        "weight":130
    } == response.json()

def test_GIVEN_pokemons_WHEN_call_api_THEN_comprove_get_no_null():
    response = client.get("/pokemons")
    assert [] != response.json()

def test_given_pokemons_when_call_api_then_length_50():
    response = client.get("/pokemons")
    
    assert len(response.json()) == 50