import requests
from secrets import access_token

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("https://api.spotware.com/connect/tradingaccounts", headers=headers)

print(response.status_code)
print(response.json())
