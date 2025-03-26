# FastAPI 基礎筆記
 
## 1. FastAPI 是什麼？
- 輕量、高速的 Python Web 框架
- 類型註解 × 自動轉換 × 自動文件產生
 
## 2. 基本骨架
```python
from fastapi import FastAPI
app = FastAPI()
 
@app.get("/api/hello")
def say_hello():
    return {"msg": "Hello"}
```
 
## 3. 輸入處理
 
```a: float``` 代表 URL 中 ```?a=xx``` 會被轉換為 float
 
若格式不對（如 ```a=abc```），FastAPI 自動回傳 422 錯誤
 
 
## 4. 錯誤處理

```python
from fastapi.responses import JSONResponse
 
try:
    ...
except ValueError as e:
    return JSONResponse(status_code=400, content={"error": str(e)})
```

## 5. 啟動服務

``` 
uvicorn main:app --reload
``` 