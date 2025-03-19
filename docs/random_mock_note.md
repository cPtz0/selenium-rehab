# Mock 筆記補充：模擬 random.choice 的測試方式
 
## 測試情境
 
在某些函式中會使用 `random.choice()`、`random.randint()` 等函式選取隨機值，例如：
 
```python
# src/random_utils.py
import random
 
def pick_random_word(words: list[str]) -> str:
    return random.choice(words)
```

解法：使用 @patch 模擬 random.choice 的回傳值
 
✅ 測試程式撰寫方式

```python
# tests/test_random_utils.py
import unittest
from unittest.mock import patch
from src.random_utils import pick_random_word
 
class TestRandomUtils(unittest.TestCase):
 
    @patch("src.random_utils.random.choice")
    def test_pick_random_word(self, mock_choice):
        mock_choice.return_value = "apple"  # 固定回傳 "apple"
 
        words = ["apple", "banana", "cherry"]
        result = pick_random_word(words)
 
        self.assertEqual(result, "apple")
```

---
 
小結語 × 備忘技巧
 
> 「透過 MagicMock 攔截隨機行為，給定預期結果，在 assertEqual 中驗證假裝隨機但其實可控的邏輯」

 
這種技巧也適用於：
 
- 隨機暱稱生成器

- 隨機抽獎邏輯
 
- 隨機打亂測試案例順序（如 random.shuffle()）
 
---
 
補充
 
未來進階可搭配：
 
- side_effect → 一次模擬多個隨機回傳值
 
- assert_called_once_with(...) → 驗證是否正確呼叫 random.choice 