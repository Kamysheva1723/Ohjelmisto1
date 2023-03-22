"""
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti.
"""

import json
import requests


query = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(query)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus["value"])

except requests.exceptions.RequestException as e:
    print (f"Hakua ei voitu suorittaa. Virhe {e}")
