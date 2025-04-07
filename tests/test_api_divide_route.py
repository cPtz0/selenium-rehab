import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestClientRoute(unittest.TestCase):
    def test_valid_division(self):
        response = client.get("/api/divide?a=10&b=2")

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.json(), {"a": 10 , "b": 2 , "result": 5})


