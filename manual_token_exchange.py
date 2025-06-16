import requests
import json

# Kod autoryzacyjny (z pliku auth_code.txt albo z URL)
authorization_code = "1c0472afa9b8113ebfb1153586c420cc1cdcd1d0f3f81608681ca184a7100bf5120ebb1535d839158e92e1"

client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
client_secret = "nKd6W0jLV1Wb2mZvJtcwlVigTv4iYYhjK3a1EazxxBCyONpypV"
redirect_uri = "http://127.0.0.1:8000/callback"

token_url = "https://openapi.ctrader.com/apps/token"

payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
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
