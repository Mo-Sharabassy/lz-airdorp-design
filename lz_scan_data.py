import requests
import pandas as pd

url = "https://layerzeroscan.com/api/trpc/messages.list?input=%7B%22filters%22%3A%7B%22stage%22%3A%22mainnet%22%2C%22created%22%3A%7B%7D%7D%7D"

response = requests.get(url)

messages = response.get("result", {}).get("data", {}).get("messages", [])

df = pd.json_normalize(messages)

df['id'] = df.reset_index(drop=True).index

import datetime

df['created'] = df['created'].apply(lambda x: datetime.datetime.fromtimestamp(x))
df['updated'] = df['updated'].apply(lambda x: datetime.datetime.fromtimestamp(x))