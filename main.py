from fastapi import FastAPI, Request
from websocket_order_sender import send_ws_order
import json

app = FastAPI()

# ✅ Strona testowa
@app.get("/")
def root():
    return {"status": "OK – serwer działa ✔"}

# ✅ Endpoint webhooka z TradingView
@app.post("/webhook")
async def webhook_listener(request: Request):
    data = await request.json()
    print("📩 Odebrano webhook z TradingView:")
    print(json.dumps(data, indent=2))

    action = data.get("action")
    symbol = data.get("symbol", "XAUUSD")
    volume = float(data.get("volume", 0.01))

    if action in ["buy", "sell"]:
        await send_ws_order(action, symbol, volume)
        return {"status": f"{action.upper()} order sent"}
    elif action == "close":
        return {"status": "❌ CLOSE action not yet implemented – skip"}
    else:
        return {"status": f"Unknown action: {action}"}

# ✅ Endpoint do przechwycenia kodu z przeglądarki
@app.get("/callback")
def oauth_callback(code: str = ""):
    if code:
        with open("latest_code.txt", "w") as f:
            f.write(code)
        print(f"✅ Odebrano code z przeglądarki: {code}")
        return {"status": "Code received ✔", "code": code}
    else:
        return {"status": "❌ No code in request"}
