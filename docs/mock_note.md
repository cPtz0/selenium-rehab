# Mock 筆記：使用 unittest.mock 模擬外部依賴
 
本筆記記錄了在 Python 測試中使用 `@patch` 與 `MagicMock` 來模擬外部資源（如 API 請求）的方法與原理。
 
---
 
## 1. 為什麼要使用 Mock？
 
在單元測試時，我們希望：
- 測試執行快速
- 不依賴外部系統（如 API、資料庫、檔案系統）
- 可重現、不會因外部狀態改變導致失敗
 
因此，我們會使用 mock 技術「攔截」這些外部依賴，並回傳模擬的結果。
 
---
 
## 2. 範例場景說明
 
```python
# src/stock.py
import requests
 
def get_stock_price(stock_id: str) -> dict:
    url = f"https://api.stock.example/{stock_id}"
    response = requests.get(url)
    return response.json()
```

---
 
## 3. 使用 @patch 模擬 requests.get
 
# tests/test_stock.py
```
import unittest
from unittest.mock import patch
from src.stock import get_stock_price
 
class TestStockAPI(unittest.TestCase):
 
    @patch("src.stock.requests.get")
    def test_get_stock_price_mocked(self, mock_get):
        mock_get.return_value.json.return_value = {
            "stock_id": "2330",
            "price": 650,
            "currency": "TWD"
        }
 
        result = get_stock_price("2330")
        self.assertEqual(result["stock_id"], "2330")
        self.assertEqual(result["price"], 650)
        self.assertEqual(result["currency"], "TWD")
```
---
 
## 4. patch 的行為解釋
```
@patch("src.stock.requests.get")
```
這表示：

> 將「src.stock 模組中使用的 requests.get」替換成一個 MagicMock 物件。
 
- mock_get()：模擬呼叫 requests.get()
 
- mock_get.return_value：模擬回傳的 Response 物件
 
- mock_get.return_value.json.return_value：模擬 .json() 回傳資料
 
 
 
---
 
## 5. MagicMock 是什麼？
 
MagicMock 是 unittest.mock 提供的萬用物件，可自由設定：
 
- 回傳值 (return_value)
 
- 呼叫時報錯 (side_effect)
 
- 方法 (mock.method())
 
 
範例：
```
mock_get.return_value.status_code = 200
mock_get.side_effect = TimeoutError("API timeout!")
```
 
---
 
## 6. 對照圖表：真實邏輯 vs Mock 模擬邏輯
 
| 真實邏輯                          | Mock 模擬邏輯                                |
|-----------------------------------|---------------------------------------------|
| `requests.get()`                  | `mock_get()`                                |
| `response = requests.get(...)`    | `mock_get.return_value`                     |
| `response.json()`                 | `mock_get.return_value.json()`              |
| `return response.json()`          | `mock_get.return_value.json.return_value`   |


---
 
## 7. 小結語
 
> 被 patch 的物件不會發出真實請求，它們會被 MagicMock 替換掉，
測試者可以精準控制每個步驟的結果，使測試能穩定、安全、快速進行。
 
 
 
Mock 是現代自動化測試中不可或缺的技能，透過這份筆記快速回顧，你將更自在地掌握它！
 
---
 