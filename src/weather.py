import requests

def get_weather(city:str) -> dict:
    url = f'https://api.weather.example/{city}'
    response = requests.get(url)
    return response.json()