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
            self.assertIn("數字",str(e))
#相減類測試
class TestSubtract(unittest.TestCase):
    def test_math_subtract_valid(self):
        self.assertEqual(subtract(3,2),1)
    def test_math_subtract_invalid_input_type(self):
        try:
            add('E',2)
            self.fail("觸發錯誤ValueError,但是沒有發生")
        except ValueError as e:
            self.assertIn("數字",str(e))
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
#平方類計算
class TestSquare(unittest.TestCase):
    def test_math_square_valid(self):
        self.assertEqual(square(9),81)
    def test_math_divide_invalid_input_type(self): 
        with self.assertRaises(ValueError):
            square('E')
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

if __name__ == "main":
    unittest.main()