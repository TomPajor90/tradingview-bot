from ctrader_ws_client import CtraderWebSocketClient
from my_secrets import client_id, access_token, account_id

client = CtraderWebSocketClient(
    client_id=client_id,
    access_token=access_token,
    account_id=int(account_id),
    is_live=True
)

def on_login_ready():
    print("✅ Połączono z cTrader WebSocket")
    print("🔍 Dane konta:")
    print(f" • ID konta: {client.account_id}")
    print(f" • TOKEN: {client.access_token[:8]}...")

client.on_login_ready = on_login_ready
client.start()
