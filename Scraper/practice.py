import requests
from auth import KEY

res = requests.get("https://randomuser.me/api/")

all_users = []
all_users.append(res.json()["results"][0]["name"]["first"])

for i in range(10):
    print("Sleeping at…")
    res = requests.get("https://randomuser.me/api/")
    all_users.append(res.json()["results"][0]["name"]["first"])

print(all_users)