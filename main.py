import os

import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.trinks.com/v1/servicos"

headers = {
    "accept": "application/json",
    "X-Api-Key": os.getenv("X_API_KEY"),
    "estabelecimentoId": os.getenv("ESTABELECIMENTO_ID")
}

response = requests.get(url, headers=headers)

print(response.text)
