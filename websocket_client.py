import asyncio
import websockets
import json
import uuid
from utils import load_tokens

# 🔐 Stałe – dane do logowania
ENDPOINT = "wss://live.ctraderapi.com:5035"  # produkcyjny endpoint WebSocket
ACCESS_TOKEN = load_tokens()["access_token"]  # pobierz token z pliku tokens.json
ACCOUNT_ID = 2055957  # ← tutaj wstaw swój realny numer konta cTrader
CLIENT_ID = str(uuid.uuid4())  # losowy identyfikator klienta

# 🔄 Funkcja do wysłania zlecenia
async def send_order(symbol, volume, direction):
    async with websockets.connect(ENDPOINT) as websocket:
        print("✅ Połączono z WebSocket cTrader")

        # 1. Logowanie
        auth_msg = {
            "payloadType": "ProtoOAUthTokenReq",
            "clientMsgId": CLIENT_ID,
            "payload": {
                "accessToken": ACCESS_TOKEN
            }
        }
        await websocket.send(json.dumps(auth_msg))

        # 2. Odbiór odpowiedzi logowania
        response = await websocket.recv()
        print("✅ Odpowiedź logowania:", response)

        # 3. Wysłanie zlecenia
        order_msg = {
            "payloadType": "ProtoOPlaceOrderReq",
            "clientMsgId": str(uuid.uuid4()),
            "payload": {
                "accountId": ACCOUNT_ID,
                "symbolName": symbol,
                "orderType": "MARKET",
                "tradeSide": direction,  # "BUY" lub "SELL"
                "volume": int(volume * 100000),  # 0.01 lota = 1000 mikro
                "isStopLossEnabled": False,
                "isTakeProfitEnabled": False
            }
        }
        await websocket.send(json.dumps(order_msg))
        print(f"📤 Wysłano zlecenie: {direction} {symbol} {volume} lota")

        # 4. Odbiór odpowiedzi
        while True:
            msg = await websocket.recv()
            print("📥 Odpowiedź od serwera:", msg)
            break

# 🔘 Automatyczne uruchomienie testu
if __name__ == "__main__":
    asyncio.run(send_order("XAUUSD", 0.01, "BUY"))
