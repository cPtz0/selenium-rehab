import unittest
from unittest.mock import patch
from src.random_utils import pick_random_word

class TestRandomUtils(unittest.TestCase):
    #這行攔截真正的API發送,改為使用Magic mock發送我們模擬的任何數據
    @patch("src.random_utils.random.choice")
    def test_pick_random_word(self,mock_choice):
        # 強制回傳值為apple
        mock_choice.return_value = "apple"
        # 假定的list
        words = ['apple','juice','ace','fruit']
        result = pick_random_word(words)
        # 測試回傳值是否為apple
        self.assertEqual(result,'apple')