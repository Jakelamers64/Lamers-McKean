import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

class bot_machLearn():
    def download_data(self,symbol):
        """downloads HLOCV data from yahoo yfinance and stores it as a csv in
        data folder
        """
        self.data_df = yf.download(symbol, start="2015-05-31", end="2020-05-31")
        self.data_df.to_csv('data\{}.csv'.format(symbol))

    def create_model(self):
        self.training_df = pd.read_csv('Data\TSLA.csv')
        self.training_df = self.training_df.dropna(axis=0)

        self.val_df = pd.read_csv('Data\AAPL.csv')
        self.val_df = self.val_df.dropna(axis=0)

        # training prediction target is tommorows close
        self.training_y = self.training_df.iloc[1:]
        self.training_y = (self.training_y.Close / self.training_y.Close.iloc[0])

        # training features to make prediction are as follows
        self.features = ['Open','High','Low','Close','Volume']
        self.training_X = self.training_df[self.features].iloc[0:-1]

        # validation prediction target is tommorows close
        self.val_y = self.val_df.iloc[1:]
        self.val_y = (self.val_y.Close / self.val_y.Close.iloc[0])

        # validation features to make prediction are as follows
        self.val_X = self.val_df[self.features].iloc[0:-1]

        prices_model = DecisionTreeRegressor(random_state=1)

        # train with historical data
        prices_model.fit(self.training_X,self.training_y)

        # tommorows predicted prices
        self.val_predictions = prices_model.predict(self.val_X)

        self.df = pd.DataFrame({'Actual':self.val_y,'Predicted':self.val_predictions})

        self.df.columns = ['Actual','Predicted']

        plt.plot(self.df)

        plt.show()

        print(mean_absolute_error(self.val_y,self.val_predictions))

    def to_string(self):
        return self.training_df
