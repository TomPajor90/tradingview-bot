import requests

url = "https://205c-2a01-799-1655-6600-c5ec-c171-6871-4d92.ngrok-free.app/webhook"  # Twój adres ngrok
payload = {
    "action": "buy",
    "symbol": "XAUUSD",
    "volume": 0.01
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Odpowiedź serwera:")
print(response.text)
