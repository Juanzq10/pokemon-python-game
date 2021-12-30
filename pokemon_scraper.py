from bs4 import BeautifulSoup
import requests
from models.Constants import *
import json

url = 'https://pokemondb.net/pokedex/all'

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemon_data = []

pokemon_rows = page_content.find_all('tr')
pokemon_dict = {}

for row in pokemon_rows[1:]:
    stats_html = row.find_all('td')[4:]
    stats_array = list(map(lambda data: int(data.text), stats_html))

    types_html = row.find_all('a', attrs={'class': 'type-icon'})
    types_array = list(map(lambda data: TYPE_MAP[data.text], types_html))

    name = row.find('a', attrs={'class': 'ent-name'}).text
    
    mega_html = row.find('small', attrs={'class': 'text-muted'})

    if mega_html: 
        if 'Mega' in mega_html.text or 'Galarian' in mega_html.text:
            name = mega_html.text
        else: 
            name = name + ' ' + mega_html.text

    pokemon_dict[str(name)] = {
        "type1": types_array[0],
        "hp": stats_array[0],
        "attack": stats_array[1],
        "defense": stats_array[2],
        "sp_attack": stats_array[3],
        "sp_defense": stats_array[4],
        "speed": stats_array[5]
    }

    if len(types_array) > 1:
        pokemon_dict[str(name)]["type2"] = types_array[1]
    
with open('pokemon_database/pokemons.json', 'w') as outfile:
    json.dump(pokemon_dict, outfile)