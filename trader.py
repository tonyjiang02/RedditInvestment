from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='FEX2ZCRX0XGU1ZL7', output_format='pandas')

def getPrice(ticket):
    global ts
    data, meta_data = ts.get_intraday(symbol=ticket,interval='1min', outputsize='full')
    print(data.head(1)['4. close'][0])
getPrice("TSLA")
def buy(symbol, quantity):
    