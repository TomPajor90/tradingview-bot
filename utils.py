import json

def load_tokens():
    with open("tokens.json", "r") as f:
        return json.load(f)
