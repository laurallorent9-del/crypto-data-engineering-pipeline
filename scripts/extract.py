import requests
import pandas as pd

url="https://api.coingecko.com/api/v3/coins/markets"

params={
    "vs_currency": "usd"
}

response=requests.get(url, params=params)

df=pd.DataFrame(response.json())

df.to_csv("data/crypto.csv", index=False)

print("Datos descargados correctamente")