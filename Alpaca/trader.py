import requests, config, json
import alpaca_trade_api as tradeapi

def get_account():
    r = requests.get(config.ACCOUNT_URL,headers=config.HEADERS)
    return json.loads(r.content)

def create_order(symbol,qty,side,type,time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r = requests.post(config.ORDERS_URL,json=data,headers=config.HEADERS)

    return json.loads(r.content)

def get_orders():
    r = requests.get(config.ORDERS_URL,headers=config.HEADERS)

    return json.loads(r.content)
