from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from stockobject import stockObject
import datetime
ts = TimeSeries(key='FEX2ZCRX0XGU1ZL7', output_format='pandas')
balance = 100000
portfolio = []
def getPrice(ticket):
    global ts
    data, meta_data = ts.get_intraday(symbol=ticket,interval='1min', outputsize='full')
    return data.head(1)['4. close'][0]
def buy(symbol, quantity):
    price = getPrice(symbol)
    stock_object = stockObject(symbol,quantity,price,datetime.datetime,"buy")
    portfolio.append(stock_object)