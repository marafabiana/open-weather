from open_weather.api.client import get_coordinates, get_weather


def get_weather_data(*countries):
    rows = []

    for country in countries:
        lat, lon = get_coordinates(country)
        weather = get_weather(lat, lon)

        row = {
            "country": country,
            "lat": lat,
            "lon": lon,
            "temperature": weather["main"]["temp"],
            "pressure": weather["main"]["pressure"],
        }
        rows.append(row)

    return rows