import unittest
from src.math_utils import subtract
#相減類測試
class TestSubtract(unittest.TestCase):
    def test_math_subtract_valid(self):
        self.assertEqual(subtract(3,2),1)
    def test_math_subtract_invalid_input_type(self):
        try:
            subtract('E',2)
            self.fail("觸發錯誤ValueError,但是沒有發生")
        except ValueError as e:
            self.assertIn("數字",str(e))