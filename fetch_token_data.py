import json
import requests

def fetch_and_save_token_data():
    url = "https://api.tokenmetrics.com/v2/coins?limit=1000"
    headers = {
        "accept": "*/*"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        token_data = response.json()
        try:
            with open('C:/Users/bjhof/Documents/crypto_business/bot/token_data.json', 'w') as f:
                json.dump(token_data, f)
            print("Token data fetched and saved successfully.")
        except IOError as e:
            print(f"IOError: {e}")
    else:
        print(f"Failed to fetch token data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_token_data()
