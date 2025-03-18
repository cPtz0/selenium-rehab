import requests

def get_stock_price(stock_id: str) -> dict:
    url = f'https://api.stock.example/{stock_id}'
    response = requests.get(url)
    return response.json()