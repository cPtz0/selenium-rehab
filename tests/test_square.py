import unittest
from src.math_utils import square
#平方類計算
class TestSquare(unittest.TestCase):
    def test_math_square_valid(self):
        self.assertEqual(square(9),81)
    def test_math_divide_invalid_input_type(self): 
        with self.assertRaises(ValueError):
            square('E')
