import config
from pyrh import Robinhood

rh = Robinhood(username=config.USERNAME, password=config.PASSWORD)

rh.login()

rh.print_quote("AAPL")
