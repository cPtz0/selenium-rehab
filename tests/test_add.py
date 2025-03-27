import unittest
from src.math_utils import add,subtract,divide,sqrt,square,factorial

#相加類測試
class TestAdd(unittest.TestCase):
    def test_math_add_valid(self):
        self.assertEqual(add(1,2),3)
    def test_math_add_invalid_input_type(self):
        try:
            add(1,'E')
            self.fail("觸發錯誤ValueError,但是沒有發生")
        except ValueError as e:
            self.assertIn("數值",str(e))