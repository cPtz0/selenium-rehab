import unittest
import asyncio
import inspect
from api.divide import divide_core
print("[DEBUG] divide core from :" ,inspect.getfile(divide_core))

class TestApiDivide(unittest.TestCase):
    def test_api_divide_valid(self):
        res = asyncio.run(divide_core(10,2))
        self.assertEqual(res["result"],5)
    #
    def test_api_divide_by_zero(self):
        tt = ''
        with self.assertRaises(ValueError) as context:
            asyncio.run(divide_core(10,0))
        self.assertIn("不能為0",str(context.exception)) #
    #
    def test_api_divide_by_word(self):
        aa = ''
        with self.assertRaises(ValueError) as context:
            asyncio.run(divide_core(10,'E'))
        self.assertIn("須為實數",str(context.exception)) #
