import datetime, os, sys, argparse
import backtrader as bt
import yfinance as yf
from strategies.sma_test import sma_test

# code to get yahoo finance stuff
# data_df = yf.download("ABIO", start="2015-05-28", end="2020-05-28")
# data_df.to_csv('ABIO.csv')

# dict of strats created
strategies = {
    "sma_test": sma_test
}

# takes strat as arg allows to change up strat from cmd
parser = argparse.ArgumentParser()
parser.add_argument("strategy",help="which strategy to run",type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("invalid strategy, must be one of {}".format(strategies.keys()))
    sys.exit()

# code for back testing
cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000)

# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname='data\ABIO.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2019, 5, 27),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 5, 27),
    reverse=False)

# Add the Data Feed to Cerebro
cerebro.adddata(data)

# Add a strategy to Cerebro
cerebro.addstrategy(strategies[args.strategy])

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
