"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan
säätilan tekstin sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi.
Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
"""
import json
import requests

city_name = input("Input city: ")
my_api = "434a73a542c8dfbda0c9feeb6671cb1b"
haku = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={my_api}"


try:
    vastaus = requests.get(haku)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(f"Temperature in {city_name} is {(json_vastaus['main']['temp'] - 273.15):.1f} degrees.")

except requests.exceptions.RequestException as e:
    print (f"Hakua ei voitu suorittaa. Virhe on {e}")

