import json
import requests
from coin_data import coin_data  # Import the coin data list from the module

# Load the token data from the JSON file
with open('token_data.json', 'r') as f:
    token_data = json.load(f)

# Create a mapping from token symbols to their IDs
token_map = {token['TOKEN_SYMBOL']: token['TOKEN_ID'] for token in token_data['data']}

# Replace the token symbols with their corresponding IDs in the URL
token_ids = [str(token_map[symbol]) for symbol in coin_data if symbol in token_map]
token_ids_str = ','.join(token_ids)

# Replace in URL
url = f"https://api.tokenmetrics.com/v2/trader-grades?token_id={token_ids_str}&startDate=2023-10-01&endDate=2023-10-10&symbol={','.join(coin_data)}&category=layer-1,nft&exchange=binance&marketcap=100&fdv=100&volume=100&traderGrade=17&traderGradePercentChange=0.14&limit=10&page=0"

headers = {
    "accept": "application/json",
    "api_key": "tm-********-****-****-****-************"  # Replace with your actual API key
}

response = requests.get(url, headers=headers)
print(response.text)
