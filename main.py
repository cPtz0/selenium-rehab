from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.divide import divide_core

app = FastAPI()

#FastAPI轉換，這裡可以把型別辨識移除，因為FastAPI已經會自行辨識
@app.get("/api/divide")
async def divide_endpoint(a: float , b: float):
    print("開始執行main")
    try:
        result = await divide_core(a , b)
        return result
    except ValueError as e:
        return JSONResponse(status_code=400,content={"error":str(e)})    

    