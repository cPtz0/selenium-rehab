## API 測試地獄的入口在哪？——當錯誤不再是錯誤的那一刻
 
 
---
 
## 前言：
 
這段紀錄來自一場歷時 4 天的修正，核心問題不在語法、也不在框架，而在於「我們以為程式錯了，但它卻笑著回傳了 200 OK」。

---
 
問題起源：
 
我原先在 `divide_core()` 裡這樣寫：
```python 
try:
    if b == 0:
        raise ValueError("除數不能為 0")
    return {...}
except ValueError as e:
    return JSONResponse(status_code=400, content={"error": str(e)})
``` 
表面上看來一切都好，API 會正常回應錯誤訊息。
 
但在測試時，卻怎麼樣都無法捕捉錯誤：
```python 
with self.assertRaises(ValueError):
    divide_core(10, 0)
``` 
結果永遠是：```ValueError not raised```

---
 
真相：
 
這不是測試寫錯了，而是：
 
我以為我在丟出錯誤，但其實我把錯誤「包起來」當作正常回傳
 
測試無從得知有錯，因為它沒有「冒泡出來」
 
在 ```HTTP``` 世界裡，```return JSONResponse(...)``` 是「一種正常結束」
 
---
 
修正後：
 
我將 ```divide_core()``` 重構為只做邏輯與錯誤丟出：
```python
async def divide_core(a, b):
    if b == 0:
        raise ValueError("除數不能為 0")
    return {"result": a / b}
``` 
錯誤由上層 ```FastAPI route``` 捕捉並包裝成 ```HTTP response```：
```python 
@app.get("/api/divide")
async def divide_route(a: float, b: float):
    try:
        return await divide_core(a, b)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
``` 
測試則得以恢復「乾淨的錯誤判斷」：
```python 
with self.assertRaises(ValueError):
    asyncio.run(divide_core(10, 0))
``` 
 
---
 
## 學到什麼？
| 比較項       | 錯誤拋出（raise）             | 錯誤包裝（return JSON）           |
|--------------|-------------------------------|-----------------------------------|
| 行為本質     | 中斷流程，將錯誤丟給外部處理  | 正常回傳一個 HTTP 回應物件        |
| 測試方式     | `assertRaises` 可正確捕捉錯誤 | 測試需比對 `status_code` 與回傳內容 |
| 適用場合     | 單元測試邏輯層（pure logic）   | FastAPI 路由層（route handler）    |
| 回傳型態     | 沒有（發生例外會中斷）         | 一個包含錯誤訊息的 JSON 結構       |
| 錯誤流向     | 錯誤往上冒泡，由外層決定處理方式 | 錯誤已在內部處理完畢，不會冒泡    |
 
 
---
 
## 小結：
 
> 如果你無法在測試裡抓到錯誤，請先檢查你有沒有「太貼心地把錯誤包裝起來」。
 
 
 
FastAPI 是 web 開發的工具，但測試不該對它讓步。該吶喊就吶喊，該拋錯就拋錯。
 

 