import requests
import json
from datetime import datetime

# Wczytaj refresh_token z pliku tokens.json
with open("tokens.json", "r") as f:
    tokens = json.load(f)

refresh_token = tokens["refresh_token"]
client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
client_secret = "nKd6W0jLV1Wb2mZvJtcwlVigTv4iYYhjK3a1EazxxBCyONpypV"
redirect_uri = "http://127.0.0.1:8000/callback"

# Endpoint do odświeżania tokena
token_url = "https://connect.spotware.com/apps/token"

payload = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri
}

response = requests.post(token_url, data=payload)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if response.status_code == 200:
    new_tokens = response.json()

    # Dodaj znacznik czasu odświeżenia
    new_tokens["refreshed_at"] = now

    with open("tokens.json", "w") as f:
        json.dump(new_tokens, f, indent=4)

    with open("refresh_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{now}] ✅ Access token odświeżony poprawnie\n")

    print("✅ Access token odświeżony i zapisany do tokens.json")
else:
    with open("refresh_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{now}] ❌ Błąd: {response.status_code} {response.text}\n")

    print("❌ Błąd przy odświeżaniu tokena:", response.status_code)
    print(response.text)
