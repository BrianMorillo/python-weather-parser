"""Weather parsing class responsible of obtaining data from JSON String"""
"""Author: Brian Morillo"""
"""Date: 10/22/2022"""


class WeatherParser:
    """Represents a weather data parsing class"""

    def __init__(self, weather_json_data):
        """Weather parser default constructor"""

        self._current_condition = weather_json_data["current_condition"][0]
        weather = weather_json_data["weather"][0]
        self._astronomy = weather["astronomy"][0]
        self._nearest_area = weather_json_data["nearest_area"][0]

    def get_feels_like_f(self):
        """returns the 'Feels Like' in fahrenheit temperature"""
        return self._current_condition["FeelsLikeF"]

    def get_cloud_cover(self):
        """returns the 'cloud cover' data"""
        return self._current_condition["cloudcover"]

    def get_weather_description(self):
        """returns weather description"""
        weather_description = self._current_condition["weatherDesc"][0]
        return weather_description["value"]

    def get_sunset(self):
        """returns sunset data"""
        return self._astronomy["sunset"]

    def get_sunrise(self):
        """returns sunrise data"""
        return self._astronomy["sunrise"]

    def get_city_description(self):
        """returns city description"""
        area_name = self._nearest_area["areaName"][0]
        country = self._nearest_area["country"][0]
        return f'{area_name["value"]}, {country["value"]}'      
