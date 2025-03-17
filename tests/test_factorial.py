import unittest
from src.math_utils import factorial
#階乘類計算
class TestFactorial(unittest.TestCase):
    def test_math_factorial_valid(self): 
        self.assertEqual(factorial(5),120)
    def test_math_factorial_invalid_input_negative(self): 
        with self.assertRaises(ValueError):
            factorial(-3)
    def test_math_factorial_invalid_input_type(self): 
        with self.assertRaises(ValueError):
            factorial('E')