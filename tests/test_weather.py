import unittest
from unittest.mock import patch
from src.weather import get_weather

class TestWeatherAPI(unittest.TestCase):
    @patch("src.weather.requests.get")
    def test_get_weather_mocked(self,mock_get):
        #模擬response
        mock_get.return_value.json.return_value = {
            "city" : "Taipei",
            "temp" : 25,
            "status" : "sunny"
        }


        result = get_weather("Taipei")

        self.assertEqual(result['city'],"Taipei")
        self.assertEqual(result['temp'],25)
        self.assertEqual(result['status'],"sunny")