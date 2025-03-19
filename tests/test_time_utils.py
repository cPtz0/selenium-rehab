import unittest
from unittest.mock import patch
from datetime import datetime
from src.time_utils import is_night_time

class TestTimeUtils(unittest.TestCase):
    @patch("src.time_utils.datetime.datetime")
    def test_time_night_time_true(self,mock_datetime):
        #複製一個晚上的22:00的時間
        mock_now = datetime(2025,3,19,22,0,0)
        mock_datetime.now.return_value = mock_now
        result = is_night_time()
        self.assertTrue(result)
    @patch("src.time_utils.datetime.datetime")
    def test_night_time_false(self,mock_datetime):
        #複製一個早上的10:00的時間
        mock_now = datetime(2025,3,19,10,0,0)
        mock_datetime.now.return_value = mock_now
        result = is_night_time()
        self.assertFalse(result)