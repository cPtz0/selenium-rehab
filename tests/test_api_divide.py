import unittest
from api.divide import apiDivide

class TestApiDivide(unittest.TestCase):
    def test_api_divide_valid(self):
        res = apiDivide(10,2)
        print(res)
    #
    def test_api_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:

            apiDivide(10,0)
        self.assertIn("除數必須為",str(context.exception))
    #
    def test_api_divide_by_word(self):
        with self.assertRaises(ValueError) as context:

            apiDivide(10,'E')
        self.assertIn("除數必須為",str(context.exception))