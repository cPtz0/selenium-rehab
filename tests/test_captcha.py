import unittest
from unittest.mock import patch
from src.captcha import generate_code

class TestCaptcha(unittest.TestCase):
    @patch("src.captcha.random.choice")
    def test_captcha(self,mock_choice):
        #穩定回傳ABC
        mock_choice.side_effect = ["A","B","C"]
        result = generate_code()
        self.assertEqual(result,"ABC")
        