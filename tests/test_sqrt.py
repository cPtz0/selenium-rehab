import unittest
from src.math_utils import sqrt

#開根號類測試
class TestSqrt(unittest.TestCase):
    def test_math_sqrt(self):
        self.assertEqual(sqrt(49),7)
    def test_math_sqrt_invalid_input_negative(self): 
        with self.assertRaises(ValueError):
            sqrt(-1)
    def test_math_sqrt_invalid_input_type(self):
        with self.assertRaises(ValueError):
            sqrt('E')
