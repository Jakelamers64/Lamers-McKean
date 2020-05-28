import requests, config, json
import pandas as pd
import alpaca_trade_api as tradeapi

api = tradeapi.REST(config.KEY_ID,config.SECRET_KEY,config.BASE_URL,api_version="v2")

account = api.get_account()

print(account)
