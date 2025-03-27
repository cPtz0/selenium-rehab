import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestClientRoute(unittest.TestCase):
    def test_valid_division(self):
        response = client.get("/api/divide?a=10&b=2")

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.json(), {"a": 10.0 , "b": 2.0 , "result": 5.0 })

    def test_divide_by_zero(self):
        response = client.get("/api/divide?a=10&b=0")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
 
    def test_invalid_input(self):
        response = client.get("/api/divide?a=abc&b=3")
        self.assertEqual(response.status_code, 422)


