import unittest
from src.math_utils import add,subtract,divide,sqrt,square

class TestMathUtils(unittest.TestCase):
    # 正常數據測試
    def test_math_add(self):
        self.assertEqual(add(1,2),3)
    def test_mat_subtract(self):
        self.assertEqual(subtract(3,2),1)
    def test_math_divide(self):
        self.assertEqual(divide(32,8),4)
    def test_math_sqrt(self):
        self.assertEqual(sqrt(49),7)
    def test_math_square(self):
        self.assertEqual(square(9),81)
    # 異常數據測試
    def test_math_devide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            divide(100,0)
    def test_math_sqrt_less_zero(self): 
        with self.assertRaises(ValueError):
            sqrt(-1)
    def test_math_square_input_wrong_value(self): 
        with self.assertRaises(ValueError):
            square('Word')

if __name__ == "main":
    unittest.main()