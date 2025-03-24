# Mock 筆記補充（三）：使用 side_effect 模擬多次隨機輸出
 
## 情境背景
 
某函式使用 `random.choice()` 多次產生隨機結果：
 
```python
def generate_code():
    letters = ["A", "B", "C", "D", "E"]
    return random.choice(letters) + random.choice(letters) + random.choice(letters)
```
每次執行結果都不同，不利於驗證與追蹤測試輸出。
 
---
 
## 解法：使用 side_effect 模擬每次回傳值
```python
@patch("src.captcha.random.choice")
def test_generate_code(self, mock_choice):
    mock_choice.side_effect = ["A", "B", "C"]
    result = generate_code()
    self.assertEqual(result, "ABC")
```
此段代表：
 
- 第一次呼叫 → 回傳 "A"
 
- 第二次呼叫 → 回傳 "B"
 
- 第三次呼叫 → 回傳 "C"

---
 
## 額外驗證（呼叫次數）
 
self.assertEqual(mock_choice.call_count, 3)
 
可驗證 random.choice() 是否被正確呼叫了 3 次。
 
 
---
 
## 原理補充
 
Side Effect = 一次性迭代器
 
你可以將 side_effect = [...] 理解為一列「預先排好的回傳值隊列」：
 
- Call #1 → 回傳 "A"
- Call #2 → 回傳 "B"
- Call #3 → 回傳 "C"
 
若呼叫次數超出列表長度，將會拋出 StopIteration 錯誤。
 
 
---
 
## 與 return_value 差異

| 方法          | 適合場景           | 行為                         |
|---------------|--------------------|------------------------------|
| return_value  | 固定回傳同一值     | 每次回傳相同內容             |
| side_effect   | 每次回傳不同值     | 按順序回傳列表內的項目       |
 
---
 
## 補充說明
 
side_effect 特別適合測試「重試」、「輪詢」、「依序處理」等邏輯。
 
也是唯一能模擬「時間進行下的改變」與「多次相依回應」的 mock 工具。

---
 