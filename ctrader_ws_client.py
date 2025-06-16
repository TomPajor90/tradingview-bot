import asyncio
import json
import uuid
import websockets

class CtraderWebSocketClient:
    def __init__(self, client_id, access_token, account_id, is_live=True):
        self.client_id = client_id
        self.access_token = access_token
        self.account_id = account_id
        self.is_live = is_live
        self.ws_url = "wss://live.ctraderapi.com:5035" if is_live else "wss://demo.ctraderapi.com:5035"
        self.on_login_ready = None

    async def _connect(self):
        async with websockets.connect(self.ws_url) as ws:
            print("🔌 WebSocket: Połączono z serwerem.")
            await self._authenticate(ws)
            response = await ws.recv()
            print("📥 Odpowiedź logowania:", response)

            if self.on_login_ready:
                self.on_login_ready()

    async def _authenticate(self, ws):
        auth_msg = {
            "payloadType": "ProtoOAUthTokenReq",
            "clientMsgId": str(uuid.uuid4()),
            "payload": {
                "accessToken": self.access_token
            }
        }
        await ws.send(json.dumps(auth_msg))

    def start(self):
        asyncio.run(self._connect())
