"""UnitTest class responsible of testing weatherParser class"""
"""Author: Brian Morillo"""
"""Date: 10/22/2022"""

import unittest
import json
from weather_parser import WeatherParser


class TestWeatherParser(unittest.TestCase):
    """Tests for the class WeatherParser"""

    def setUp(self):
        """
        Creates a weatherParser and tests all its methods
        """
        filename = 'london_weather_data.json'

        with open(filename) as file:
            weather_data_json = json.load(file)

        self.parser = WeatherParser(weather_data_json)

    def test_get_feels_like_f(self):
        """
        Tests that 'Feels like F' is returned correctly
        """
        self.assertEqual(self.parser.get_feels_like_f(), "55")

    def test_get_cloud_cover(self):
        """
        Tests that cloud cover is returned correctly
        """
        self.assertEqual(self.parser.get_cloud_cover(), "0")

    def test_get_weather_description(self):
        """
        Tests that the weather description is returned correctly
        """
        self.assertEqual(self.parser.get_weather_description(), "Clear")

    def test_get_sunset(self):
        """
        Tests that the sunset data is returned correctly
        """
        self.assertEqual(self.parser.get_sunset(), "05:47 PM")

    def test_get_sunrise(self):
        """
        Tests that the sunrise data is returned correctly
        """
        self.assertEqual(self.parser.get_sunrise(), "07:42 AM")

    def test_get_city_description(self):
        """
        Tests that the location is returned correctly
        """
        self.assertEqual(self.parser.get_city_description(),
         "London, United Kingdom")    


if __name__ == "__main__":
    unittest.main()
