import requests
import json

# Function to get the weather of a location
# Returns a string with the temperature of the location 

def get_weather(location: str) -> str:

    """
    Diese Funktion gibt die aktuelle Temperatur für einen gegebenen Ort zurück.

    Parameters:
    location (str): Der Ort, für den das Wetter abgerufen werden soll, als String.

    Returns:
    str: Ein String, der die aktuelle Temperatur am angegebenen Ort in Grad Celsius angibt.

    Die Funktion verwendet die OpenWeatherMap API, um die Wetterdaten abzurufen. 
    Sie sendet eine GET-Anfrage an die API und verarbeitet die JSON-Antwort. 
    Wenn die Antwort gültige Wetterdaten enthält (d.h., der HTTP-Statuscode ist nicht 404), 
    extrahiert die Funktion die Temperatur aus den Daten und gibt sie als formatierten String zurück.
    """

    api_key = "e003735d401bfe99e96a7588765f99e5"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != 404:
        main = data["main"]
        temperature = main["temp"]

        return f"Die Temperatur in {location} beträgt {temperature}°C."
    