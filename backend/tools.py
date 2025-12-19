import requests
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    Get current weather of a city using Open-Meteo (no API key).
    """

    # Step 1: City → Latitude & Longitude
    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        return "City not found."

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Step 2: Get weather using lat/lon
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    weather_res = requests.get(weather_url).json()
    current = weather_res["current_weather"]

    temp = current["temperature"]
    wind = current["windspeed"]

    return (
        f"Current temperature in {city} is {temp}°C "
        f"with wind speed {wind} km/h."
    )
