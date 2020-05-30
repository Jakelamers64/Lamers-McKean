from pytz import timezone

# login information
KEY_ID = ""
SECRET_KEY = ""

# URL stuff
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
# HEADERS = {'APCA-API-KEY-ID': KEY_ID,'APCA-API-SECRET-KEY': SECRET_KEY}

# time config
EASTERN = timezone('US/Eastern')
