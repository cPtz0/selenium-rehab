import requests

def get_weather_2(city:str) -> dict:
    try:
        response = requests.get('https://weather-api.com/api/{city}')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"連線失敗{str(e)}"}