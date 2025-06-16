import requests, json

client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
client_secret = "nKd6W0jLV1Wb2mZvJtcwlVigTv4iYYhjK3a1EazxxBCyONpypV"
redirect_uri = "http://127.0.0.1:8000/callback"
authorization_code = "1c0472afa9b8113ebfb1153586c420cc1cdcd1d0f3f81608681ca184a7100bf5120ebb1535d839158e92e1"

token_url = "https://connect.spotware.com/apps/token"

payload = {
    "grant_type": "authorization_code",
    "client_id": client_id,
    "client_secret": client_secret,
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

response = requests.post(token_url, data=payload)

print("Status HTTP:", response.status_code)
print(json.dumps(response.json(), indent=4))
