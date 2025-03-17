import unittest
from src.math_utils import divide

#相除類測試
class TestDivide(unittest.TestCase):
    def test_math_divide_valid(self):
        self.assertEqual(divide(32,8),4)
    def test_math_divide_invalid_input_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            divide(100,0)
    def test_math_divide_invalid_input_type(self): 
        try:
            divide('100',5)
            self.fail("觸發錯誤ValueError,但是沒有發生")
        except ValueError as e:
            self.assertIn("數字",str(e))
