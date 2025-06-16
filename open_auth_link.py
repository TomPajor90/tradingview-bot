import webbrowser

client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
redirect_uri = "http://127.0.0.1:8000/callback"
auth_url = f"https://connect.spotware.com/apps/auth?client_id={client_id}&redirect_uri={redirect_uri}&scope=trading&response_type=code"

print("Otwieram przeglądarkę z linkiem autoryzacyjnym...")
webbrowser.open(auth_url)

