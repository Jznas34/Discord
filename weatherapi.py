import requests
import json

# Function to get the weather of a location
# Returns a string with the temperature and the weather description

def get_weather(location: str) -> str:
    api_key = "e003735d401bfe99e96a7588765f99e5"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != 404:
        main = data["main"]
        temperature = main["temp"]

        return f"Die Temperatur in {location} beträgt {temperature}°C."
    