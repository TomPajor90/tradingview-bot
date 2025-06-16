import requests
import json
from my_secrets import access_token, account_id

CT_API_URL = "https://api.spotware.com"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

order = {
    "accountId": account_id,
    "symbolName": "XAUUSD",
    "orderType": "MARKET",
    "side": "BUY",              # lub "SELL"
    "quantity": 0.01,
    "timeInForce": "FOK"
}

url = f"{CT_API_URL}/trading/orders"

print("➡️ Wysyłam zlecenie na adres:")
print(url)
print("➡️ Z danymi:")
print(json.dumps(order, indent=2))

response = requests.post(url, headers=headers, json=order)

print("\n📥 Odpowiedź serwera:")
print("Status:", response.status_code)
print(response.text)
