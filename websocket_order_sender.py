import asyncio
import websockets
import json
import uuid

from messages.OpenApiMessages_pb2 import (
    ProtoOAGetAccountListByAccessTokenReq,
    ProtoOAAccountAuthReq,
    ProtoOANewOrderReq,
    ProtoOAExecutionEvent,
    ProtoOAOrderErrorEvent
)
from messages.OpenApiModelMessages_pb2 import (
    ProtoOAPayloadType
)
from protobuf_tools import pack, unpack

print("✅ Wersja LIVE – tylko access_token (bez ApplicationAuthReq)")

# Wczytaj dane z tokens.json
with open("tokens.json") as f:
    tokens = json.load(f)

ACCESS_TOKEN = tokens["access_token"]

async def send_ws_order(action: str, symbol: str, volume: float):
    try:
        async with websockets.connect("wss://live.ctraderapi.com:5035") as ws:
            print("✅ Połączono z WebSocket")

            # 1. GetAccountListByAccessToken
            acc_list_req = ProtoOAGetAccountListByAccessTokenReq(accessToken=ACCESS_TOKEN)
            await ws.send(pack(acc_list_req, ProtoOAPayloadType.PROTO_OA_GET_ACCOUNT_LIST_BY_ACCESS_TOKEN_REQ))
            print("📤 Wysłano GetAccountListByAccessTokenReq")

            resp = unpack(await ws.recv())
            if resp.payloadType != ProtoOAPayloadType.PROTO_OA_GET_ACCOUNT_LIST_BY_ACCESS_TOKEN_RES:
                raise Exception(f"❌ Błąd pobierania konta: {resp.payloadType}")
            print("📩 Odebrano listę kont")

            accounts = resp.message.accounts
            if not accounts:
                raise Exception("❌ Brak kont powiązanych z tokenem!")
            account = accounts[0]
            ACCOUNT_ID = account.ctidTraderAccountId
            print(f"✅ Używamy konto: {ACCOUNT_ID} ({account.accountCurrency})")

            # 2. AccountAuth
            acc_auth_req = ProtoOAAccountAuthReq(
                ctidTraderAccountId=ACCOUNT_ID,
                accessToken=ACCESS_TOKEN
            )
            await ws.send(pack(acc_auth_req, ProtoOAPayloadType.PROTO_OA_ACCOUNT_AUTH_REQ))
            print("📤 Wysłano AccountAuthReq")

            resp = unpack(await ws.recv())
            if resp.payloadType != ProtoOAPayloadType.PROTO_OA_ACCOUNT_AUTH_RES:
                raise Exception(f"❌ Błąd AccountAuth: {resp.payloadType}")
            print("📩 Odebrano AccountAuthRes")

            # 3. Wysyłka zlecenia
            symbol_map = {
                "XAUUSD": 540,
                "EURUSD": 1,
                "GBPUSD": 2,
            }
            symbol_id = symbol_map.get(symbol.upper(), 540)
            order = ProtoOANewOrderReq(
                ctidTraderAccountId=ACCOUNT_ID,
                symbolId=symbol_id,
                volume=int(volume * 100000),
                orderType=1,  # MARKET
                tradeSide=1 if action.lower() == "buy" else 2,
                clientOrderId=str(uuid.uuid4())
            )
            await ws.send(pack(order, ProtoOAPayloadType.PROTO_OA_NEW_ORDER_REQ))
            print(f"📤 Wysłano zlecenie {action.upper()} {symbol} ({volume} lota)")

            # 4. Odbiór odpowiedzi
            resp = unpack(await ws.recv())
            if resp.payloadType == ProtoOAPayloadType.PROTO_OA_EXECUTION_EVENT:
                print("✅ Wykonano zlecenie:", resp.message)
            elif resp.payloadType == ProtoOAPayloadType.PROTO_OA_ORDER_ERROR_EVENT:
                print("❌ Błąd zlecenia:", resp.message)
            else:
                print("ℹ️ Inna odpowiedź:", resp)

    except websockets.exceptions.ConnectionClosed as e:
        print(f"❌ WebSocket closed: code={e.code}, reason={e.reason}")
    except Exception as e:
        print(f"❌ Błąd główny: {e}")


# 🔧 TEST ręczny:
if __name__ == "__main__":
    asyncio.run(send_ws_order("buy", "XAUUSD", 0.01))
