import requests

ALPHA_VANTAGE_API_KEY = "your_api_key"
BASE_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol, interval='1min', outputsize='compact'):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': ALPHA_VANTAGE_API_KEY,
        'outputsize': outputsize
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def fetch_historical_data(symbol, outputsize='full'):
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': ALPHA_VANTAGE_API_KEY,
        'outputsize': outputsize
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data
