import requests
import json

# Wczytaj code z latest_code.txt
with open("latest_code.txt", "r") as f:
    code = f.read().strip()

# Dane logowania do NOWEJ aplikacji
client_id = "15584_7Sou0w6RsqFQNVNnnDZjyWj1rxU2KlhPeEXFQyYEuy1eWl29qQ"
client_secret = "3DzCI1VhSUqjzbM1OxcNfRdFOBqtL7i17I0cTzTwITHI0iA1Q2"
redirect_uri = "https://f383-2a01-799-1655-6600-bce0-9e6a-d06a-3514.ngrok-free.app/callback"

token_url = "https://openapi.ctrader.com/apps/token"

payload = {
    "grant_type": "authorization_code",
    "code": code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri
}

response = requests.post(token_url, data=payload)

if response.status_code == 200:
    tokens = response.json()
    with open("tokens.json", "w") as f:
        json.dump(tokens, f, indent=4)
    print("✅ Token uzyskany i zapisany do tokens.json")
    print("Access Token:", tokens.get("access_token") or tokens.get("accessToken"))
else:
    print("❌ Błąd podczas pobierania tokena")
    print("Kod odpowiedzi:", response.status_code)
    print("Treść odpowiedzi:", response.text)
