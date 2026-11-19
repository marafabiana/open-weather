import os
from dotenv import load_dotenv
import requests

# 1. Loads the .env file that Python can read the key
load_dotenv()

# 2. Get the key directly from the API_KEY variable in the .env file
API_KEY = os.getenv("API_KEY")

def get_coordinates(country):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": country,
        "limit": 1,
        "appid": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    lat = data[0]["lat"]
    lon = data[0]["lon"]
    
    return lat, lon

def get_weather(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat, 
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        }
       
    response = requests.get(url, params=params)

    return response.json()

