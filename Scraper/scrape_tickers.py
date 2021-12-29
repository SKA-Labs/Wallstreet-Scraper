import requests
import time
from datetime import datetime
from auth import KEY

# Initial Requests
res = requests.get("https://api.polygon.io/v3/reference/tickers?exchange=XNYS&XNAS&type=CS&market=stocks&active=true&sort=ticker&order=asc&limit=1000&apiKey=" + KEY)
all_stocks = res.json()["results"]
next_url = res.json()["next_url"]

# Gets all remaining stocks if necessary
while len(res.json().keys()) == 5:
    res = requests.get(next_url + "&apiKey=" + KEY)
    if "error" in res.json().keys():
        print(res.json()["error"])
    else:
        for stock in res.json()["results"]:
            all_stocks.append(stock)
        try:
            next_url = res.json()["next_url"]
        except:
            break

# Writes into a text file
with open('tickers.txt', 'w') as f:
    for stock in all_stocks:
        f.write(stock["ticker"] + " " + stock["name"])
        f.write('\n')