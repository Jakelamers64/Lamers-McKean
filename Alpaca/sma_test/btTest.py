import backtrader as bt
import yfinance as yf

# code to get yahoo finance stuff
# data_df = yf.download("ABIO", start="2015-05-28", end="2020-05-28")
# data_df.to_csv('ABIO.csv')

# code for back testing
cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
