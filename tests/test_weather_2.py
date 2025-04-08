import unittest
import requests
from unittest.mock import patch
from src.weather_2 import get_weather_2

class TestWeatherAPI_2(unittest.TestCase):
    @patch("src.weather_2.requests.get")
    def test_weather_connected_error(self,mock_get):
        #模擬斷線by side effect
        mock_get.side_effect = requests.exceptions.ConnectionError("無法連接")


        result = get_weather_2("Taipei")

        self.assertIn("error",result)
        self.assertIn("連線失敗",result["error"])