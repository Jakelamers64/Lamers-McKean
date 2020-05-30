import datetime, os, sys, argparse, requests, config, json
import backtrader as bt
import pandas as pd
import alpaca_trade_api as tradeapi
from Strategies.GoldenCross import GoldenCross

# login to alpaca API
api = tradeapi.REST(config.KEY_ID,config.SECRET_KEY,config.BASE_URL,api_version="v2")

GC = GoldenCross('aapl',api)

GC.next()
