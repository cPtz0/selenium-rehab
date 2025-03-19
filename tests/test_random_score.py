import unittest
from unittest.mock import patch
from src.random_score import generate_random_score

class TestRandomScore(unittest.TestCase):
    @patch('src.random_score.random.randint')
    def test_random_score_upper_boundary(self,mock_randint):
        # 設定回傳值
        mock_randint.return_value = 100
        self.assertEqual(generate_random_score(),100)

    @patch('src.random_score.random.randint')
    def test_random_score_lower_boundary(self,mock_randint):
        # 設定回傳值
        mock_randint.return_value = 1
        self.assertEqual(generate_random_score(),1)
    @patch('src.random_score.random.randint')
    def test_random_score_zero_boundary(self,mock_randint):
        # 設定回傳值
        mock_randint.return_value = 0
        self.assertEqual(generate_random_score(),0)

    @patch('src.random_score.random.randint')
    def test_random_score_negative(self,mock_randint):
        # 設定回傳值
        mock_randint.return_value = -10
        self.assertEqual(generate_random_score(),-10)

        