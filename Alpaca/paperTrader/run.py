import time, config
import alpaca_trade_api as tradeapi
from Strategies.bot_trader import bot_machLearn

# login to alpaca API
api = tradeapi.REST(
        config.KEY_ID,
        config.SECRET_KEY,
        config.BASE_URL,
        api_version="v2"
    )

bot = bot_machLearn()

#bot.download_data("TSLA")

print(bot.create_model('AAPL','TSLA'))
print(bot.create_model('ACRE','TSLA'))

def main():
    print("Starting to run...")
    while True:
        # get a clock entity
        clock = api.get_clock()

        #check if the market is open
        if clock.is_open:
            # call the bot
            print()
        # sleep then call the check if markets are open again
        time.sleep(1)
        print("Market is closed")

if __name__ == '__main__':
    main()
