import config
import requests
import alpaca_trade_api as tradeapi

r = requests.get(config.ACCOUNT_URL,headers={'APCA-API-KEY-ID': config.KEY_ID,'APCA-API-SECRET-KEY': config.SECRET_KEY})
print(r.content)

print("Done")
