import webbrowser

client_id = "15194_Jy1HHuCpKvdTvhwNOfpgv75rl9ElacribnYlgR1smm4PECFNax"
redirect_uri = "http://localhost:8000/callback"
scope = "trade"

auth_url = f"https://connect.spotware.com/apps/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"

print("👉 Skopiuj ten adres i otwórz w przeglądarce:")
print(auth_url)

webbrowser.open(auth_url)
