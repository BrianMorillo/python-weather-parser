"""Command line Weather application"""
"""Author: Brian Morillo"""
"""Date: 10/22/2022"""

import requests
from weather_parser import WeatherParser

# Prompts the user for a city
city = input("Enter city:  ")

# Gets inputted city weather data from wttr.in in JSON format
r = requests.get(f"https://wttr.in/{city}?format=j1")
json = r.json()

# Creates Weather Parser
parser = WeatherParser(json)

# Displays a weather summary.
print(
    f"Location:  {parser.get_city_description()}\n"
    f"Currently feels like:  {parser.get_feels_like_f()} degrees F\n"
    f"Current weather is:  {parser.get_weather_description()}\n"
    f"Cloud Cover:  {parser.get_cloud_cover()}%\n"
    f"Sunrise:  {parser.get_sunrise()}\n"
    f"Sunset: {parser.get_sunset()}\n"
)
