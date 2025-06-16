from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"status": "working ✅"}

@app.get("/callback")
def oauth_callback(code: str = ""):
    if code:
        with open("latest_code.txt", "w") as f:
            f.write(code)
        print(f"✅ Odebrano code z przeglądarki: {code}")
        return {"status": "Code received ✔", "code": code}
    else:
        return {"status": "❌ No code in request"}
