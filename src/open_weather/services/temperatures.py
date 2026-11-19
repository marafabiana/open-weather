from open_weather.api.client import get_coordinates, get_weather

def get_temperatures(*countries):
    
    temperatures = {}
    for country in countries:
        lat, lon = get_coordinates(country)
        weather = get_weather(lat, lon)
        temperatures[country] = weather["main"]["temp"]

    return temperatures


