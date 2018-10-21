from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from stockobject import stockObject
from stockobject import soldObject
import datetime
import database
dictvalues = database.getPortfolio()
balance = dictvalues["balance"]
portfolio = dictvalues["portfolio"]
history = dictvalues["history"]
ts = TimeSeries(key='FEX2ZCRX0XGU1ZL7', output_format='pandas')
def getPrice(ticket):
    global ts
    data, meta_data = ts.get_intraday(symbol=ticket,interval='1min', outputsize='full')
    return data.head(1)['4. close'][0]
def buy(symbol, quantity):
    global balance
    price = getPrice(symbol)
    stock_object = stockObject(symbol,quantity,price,datetime.datetime,"buy")
    portfolio.append(stock_object)
    balance -= quantity*price
# def short(symbol,quantity):
#     global balance
#     price = getPrice(symbol)
#     stock_object = stockObject(symbol,quantity,price,datetime.datetime,"short")
#     portfolio.append(stock_object)
#     balance-=quantity*price
def sell(index, quantity):
    stock_object = portfolio[index]
    stock_sold = None
    price = getPrice(stock_object.symbol)
    if(quantity <=stock_object.quantity):
        portfolio[index].quantity-=quantity
        profit = calculateProfit(price,stock_object,quantity)
        balance+=profit
        stock_sold = soldObject(self,stock_object.symbol,quantity,stock_object.buyprice,price,stock_object.buydate,datetime.datetime,stock_object.tradetype,profit)
        history.append(stock_sold)

def calculateProfit(currPrice, stock_object, quantity):
    if(tradeType=="buy"):
        return price*quantity - stock_object.buyprice*quantity
    # if(tradeType=="short"):
    #     return stock_object.buyprice*quantity-price*quantity
buy("AAPL", 100)
print(balance)