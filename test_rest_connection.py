import json
import requests

# Wczytaj token z pliku
with open("tokens.json", "r") as f:
    tokens = json.load(f)

access_token = tokens["access_token"]

# Endpoint REST z tokenem jako parametr
url = f"https://api.spotware.com/connect/tradingaccounts?oauth_token={access_token}"

# Wysyłamy zapytanie
response = requests.get(url)

# Wyniki
print("✅ Status:", response.status_code)
print("✅ Odpowiedź JSON:")
print(response.text)
