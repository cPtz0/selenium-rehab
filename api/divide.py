from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

#FastAPI轉換，這裡可以把型別辨識移除，因為FastAPI已經會自行辨識
@app.get("/api/divide")
async def divide_endpoint(a: float , b: float):
    try:
        if b == 0:
            raise ValueError("除數不能為0!!")
        return {
            "a":a,
            "b":b,
            "result":a/b
        }
    except ValueError as e:
        return JSONResponse(status_code=400,content={"error":str(e)})    

    