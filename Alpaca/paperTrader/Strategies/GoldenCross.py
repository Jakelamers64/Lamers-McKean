import numpy as np
import matplotlib as plt
import pandas as pd
from datetime import date, timedelta

class GoldenCross():
    def __init__(self,symbol,api):
        self.hist_data = api.alpha_vantage.historic_quotes(symbol, adjusted=True, output_format='pandas')
        self.fast = 50
        self.slow = 200
        self.yesterday = date.today() - timedelta(days=1)

    def calc_sma(self,values,window):
        weights = ( np.repeat(1.0,window) / window )
        return np.convolve(values.loc[self.yesterday:(self.yesterday - timedelta(days=window)),'4. close'],weights)

    def calc_crossover(self):
        

    def next(self):
