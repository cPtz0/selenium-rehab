## Mock 的 side_effect 是什麼？它和 return_value 有什麼不同？
 
在進行單元測試或 API 測試時，為了模擬某些「不容易重現的情境」，我們通常會使用 unittest.mock 提供的工具。
其中一個強大但常被誤解的屬性就是：side_effect。

---
 
## 什麼是 side_effect？
 
在程式設計中，「副作用（side effect）」指的是一個函式除了回傳值外，還有其他行為，
例如：印出東西、修改變數、報錯、進行網路連線等。
 
而在 mock 中，side_effect 指的是：
 
> 你可以指定這個模擬函式「被呼叫時」，會出現什麼副作用（例如：丟錯、回傳多組值、執行某段邏輯）

 
---
 
## 常見用途：

類型       | 說明                            | 實例
-----------|---------------------------------|---------------------------------------
1. 拋出錯誤 | 模擬函式執行時出現錯誤          | mock.side_effect = ValueError("錯誤測試")
2. 一次回傳多個值 | 每次呼叫回傳不同的值       | mock.side_effect = [1, 2, 3]
3. 執行自訂函式 | 呼叫時改為執行指定邏輯       | mock.side_effect = lambda x: x * 2

---
 
## 和 return_value 的差別？
 
屬性          | 行為                     | 適用情境
---------------|--------------------------|-------------------------
return_value   | 永遠回傳固定值           | 模擬簡單函式、API 正常狀態
side_effect    | 可拋錯、多值、或邏輯控制 | 測試異常狀況、流程控制、錯誤捕捉

---
 
## 範例比較：
 
# return_value：每次都回傳 10
mock_func.return_value = 10
print(mock_func())  # 10
print(mock_func())  # 10
 
# side_effect：依序回傳 1、2、3，之後會報錯
mock_func.side_effect = [1, 2, 3]
print(mock_func())  # 1
print(mock_func())  # 2
print(mock_func())  # 3
print(mock_func())  # StopIteration 錯誤
 
 
---
 
## 實務測試應用（API 測試場景）

測試情境       | side_effect 用法                              | 說明
----------------|-----------------------------------------------|-------------------------------------
API 連不上     | side_effect = ConnectionError(...)            | 模擬 requests.get() 報錯
資料來得太快太慢 | side_effect = lambda x: slow_mock(x)        | 自訂延遲邏輯
測試例外捕捉   | side_effect = ValueError(...)                 | 確認函式是否能正確攔截錯誤
 
---
 
## 小結：
 
side_effect 是模擬「副作用」的利器
 
它可以丟錯、執行邏輯、依序輸出多值
 
常與 patch() 搭配，用於 API、網路請求、資料庫等外部依賴測試

---
 