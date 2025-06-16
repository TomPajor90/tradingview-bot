import asyncio
import websockets
from messages.OpenApiMessages_pb2 import ProtoOAApplicationAuthReq
from messages.OpenApiModelMessages_pb2 import ProtoOAPayloadType
from protobuf_tools import pack, unpack

CLIENT_ID = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
CLIENT_SECRET = "nKd6W0jLV1Wb2mZvJtcwlVigTv4iYYhjK3a1EazxxBCyONpypV"

async def test_app_auth():
    async with websockets.connect("wss://live.ctraderapi.com:5035") as ws:
        print("✅ Połączono z WebSocket")
        auth_msg = ProtoOAApplicationAuthReq(clientId=CLIENT_ID, clientSecret=CLIENT_SECRET)
        await ws.send(pack(auth_msg, ProtoOAPayloadType.PROTO_OA_APPLICATION_AUTH_REQ))
        print("📤 Wysłano ApplicationAuthReq")
        resp = await ws.recv()
        print("📩 Odebrano odpowiedź:", resp)
        unpacked = unpack(resp)
        print("✅ Rozkodowano:", unpacked)

asyncio.run(test_app_auth())
