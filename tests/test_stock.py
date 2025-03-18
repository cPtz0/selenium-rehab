import unittest
from unittest.mock import patch
from src.stock import get_stock_price

class TestStockAPI(unittest.TestCase):
    @patch("src.stock.requests.get")
    def test_get_stock_price_mocked(self,mock_get):
        # 模擬API回傳資料
        mock_get.return_value.json.return_value = {
            "stock_id": "2330",
            "price": 650,
            "currency": "TWD"
        }
        result = get_stock_price("2330")

        self.assertEqual(result["stock_id"],"2330")
        self.assertEqual(result["price"],650)
        self.assertEqual(result["currency"],"TWD")
