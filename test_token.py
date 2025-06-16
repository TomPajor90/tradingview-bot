import requests
from utils import load_tokens

access_token = load_tokens()["access_token"]

url = f"https://api.spotware.com/connect/tradingaccounts?oauth_token={access_token}"

response = requests.get(url)

print("Status kod:", response.status_code)
print("Odpowiedź JSON:")
print(response.json())


