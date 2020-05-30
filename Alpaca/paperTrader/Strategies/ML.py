class ML():
    def __init__(self, api):
        self.api = api

    def order(self):
        self.api.submit_order(
                    symbol='SPCE',
                    qty=1,
                    side='buy',
                    type='market',
                    time_in_force='day',
                )
            
