from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

#FastAPI轉換，這裡可以把型別辨識移除，因為FastAPI已經會自行辨識

async def divide_core(a: float , b: float):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise ValueError("除數與被除數必須為實數!!")
    if b == 0:
        print("DEBUG觸發數字錯誤")
        raise ValueError("除數不能為0")
    return {
        "a":a,
        "b":b,
        "result":a/b
    }    

    