import httpx

payload = {
    "action": "buy",
    "symbol": "XAUUSD",
    "volume": 0.01
}

response = httpx.post(
    "https://df19-2a01-799-1655-6600-713f-283-1367-66d1.ngrok-free.app/webhook",
    json=payload
)

print("Status:", response.status_code)
print("Odpowiedź:", response.text)
