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
            self.fail("觸發ValueError,但是沒有發生")
        except ValueError as e:
            self.assertIn("數值",str(e))
    def test_math_divide_small_number(self): 
        result = divide(1,1e-10)
        self.assertAlmostEqual(result , 1e10)

    def test_math_divide_large_number(self):
        result = divide(1e20,1e10)
        self.assertAlmostEqual(result , 1e10)
    def test_math_divide_near_zero(self):
        # 極小正數 (float但非0)
        result = divide(1,1e-308)
        self.assertTrue(result > 1e-307)
