# Mock 筆記補充（二）：模擬邊界與非預期輸出
 
## 測試情境
 
有些函式本身沒有輸入參數，單純從 `random` 產生結果，例如：
 
```python
# src/random_score.py
import random
 
def generate_random_score() -> int:
    return random.randint(1, 100)
 
這樣的隨機行為需要測試，但：
 
無法控制每次輸出的結果
 
難以確認邏輯是否涵蓋所有邊界（例如 1, 100）
 
無法模擬錯誤或非法值（如 0、-10）
```
---
 
解法：使用 ```@patch``` 模擬 ```random.randint``` 回傳值
 
✅ 範例測試撰寫方式：
```python
# tests/test_random_score.py
import unittest
from unittest.mock import patch
from src.random_score import generate_random_score
 
class TestRandomScore(unittest.TestCase):
 
    @patch("src.random_score.random.randint")
    def test_random_score_upper_boundary(self, mock_randint):
        mock_randint.return_value = 100
        self.assertEqual(generate_random_score(), 100)
 
    @patch("src.random_score.random.randint")
    def test_random_score_lower_boundary(self, mock_randint):
        mock_randint.return_value = 1
        self.assertEqual(generate_random_score(), 1)
 
    @patch("src/random_score.random.randint")
    def test_random_score_zero_case(self, mock_randint):
        mock_randint.return_value = 0
        self.assertEqual(generate_random_score(), 0)
 
    @patch("src/random_score.random.randint")
    def test_random_score_negative_case(self, mock_randint):
        mock_randint.return_value = -10
        self.assertEqual(generate_random_score(), -10)
```
---
 
## 筆記補充 × 測試意圖說明
 
即使我們知道 0 與 -10 並不在預期的數值範圍內，這樣的測試仍然有以下價值：
| 類型         | 用意                                                                 |
|--------------|----------------------------------------------------------------------|
| 邏輯覆蓋     | coverage 工具能標記這行是否執行過                                   |
| 預防未來 bug | 模擬未來程式失控時的例外輸出反應                                     |
| 探索極端值   | 探測非法值傳入後的下游處理行為                                       |
| 提醒開發者   | 表示目前這段程式未設防呆（可加註註解，例如：NOTE: 此段需日後加防呆） |
 
---
 
備註
 
此方法不適用於驗證資料正確性，而是用於設計與邏輯上的極端驗證。
 
若未來加入 ValueError 例外處理，這類測試需要同步調整。

---