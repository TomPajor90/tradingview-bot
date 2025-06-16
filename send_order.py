
import json
import requests
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Załaduj tokeny z pliku
with open("tokens.json", "r") as f:
    tokens = json.load(f)

access_token = tokens["access_token"]

@app.post("/webhook")
async def tradingview_webhook(request: Request):
    payload = await request.json()

    action = payload.get("action")
    symbol = payload.get("symbol")
    volume = payload.get("volume")

    print(f"✅ Otrzymano alert: {action} {volume} {symbol}")

    # Przykład logiki: wysłanie zlecenia do cTrader REST API (symulacja POST)
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # W prawdziwej wersji: tu trzeba połączyć się z WebSocket TCP API cTrader
    # Tymczasowo tylko pokazujemy co byśmy wysłali:
    order_payload = {
        "symbol": symbol,
        "action": action,
        "volume": volume
    }

    print("📤 Gotowe do wysłania zlecenie:", json.dumps(order_payload, indent=2))

    # Tu normalnie wysyłasz do API cTrader
    # response = requests.post("https://api.spotware.com/order", headers=headers, json=order_payload)

    return {"message": "Alert odebrany i zlecenie przygotowane ✅"}

if __name__ == "__main__":
    uvicorn.run("send_order:app", host="127.0.0.1", port=8000, reload=True)
