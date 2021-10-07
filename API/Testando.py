import requests
import _json

resposta = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow");

for question in resposta.json()["items"]:
    print(question)