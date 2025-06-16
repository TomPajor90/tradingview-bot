import webbrowser

client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
redirect_uri = "http://127.0.0.1:8000/callback"
scope = "trade"

auth_url = f"https://connect.spotware.com/apps/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"

print("Otwieram przeglądarkę...")
webbrowser.open(auth_url)
