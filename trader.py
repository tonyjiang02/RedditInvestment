from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from stockobject import stockObject
from stockobject import soldObject
import datetime
import database
arr = database.getPortfolio()
balance = arr[0]["balance"]
historyid = arr[0]["historyid"]
portfolioid = arr[0]["portfolioid"]
print(balance)
print(historyid)
print(portfolioid)
portfolio = arr[2]
history = arr[1]
ts = TimeSeries(key='FEX2ZCRX0XGU1ZL7', output_format='pandas')
def getPrice(ticket):
    try:
        global ts
        data, meta_data = ts.get_intraday(symbol=ticket,interval='1min', outputsize='full')
        return data.head(1)['4. close'][0]
    except ValueError:
        return 0
def buy(symbol, quantity):
    global balance
    global portfolioid
    price = getPrice(symbol)
    if(price!=0):
        stock_object = stockObject(symbol,quantity,price,datetime.date,"buy")
        database.uploadPortfolio(stock_object,portfolioid)
        balance -= quantity*price
        portfolioid=portfolioid+1
        database.updateVars(balance,historyid,portfolioid)
# def short(symbol,quantity):
#     global balance
#     price = getPrice(symbol)
#     stock_object = stockObject(symbol,quantity,price,datetime.datetime,"short")
#     portfolio.append(stock_object)
#     balance-=quantity*price
def sell(id):
    global balance
    global portfolio
    global historyid
    stock_object = {}
    for doc in portfolio:
        if(doc.id == str(id)):
            print("stock")
            stock_object = doc.to_dict()
    price = getPrice(stock_object["symbol"])
    if(price!=0):
        profit = calculateProfit(price,stock_object)
        balance+=profit
        stock_sold = soldObject(stock_object["symbol"],stock_object["quantity"],stock_object["buyprice"],price,stock_object["buydate"],datetime.date,stock_object["tradetype"],profit)
        database.deletePortfolio(id)
        historyid=historyid+1
        database.uploadHistory(stock_sold,historyid)
        database.updateVars(balance,historyid,portfolioid)

def calculateProfit(currPrice, stock_object):
    if(stock_object["tradetype"]=="buy"):
        return currPrice*stock_object["quantity"] - stock_object["buyprice"]*stock_object["quantity"]
    # if(tradeType=="short"):
    #     return stock_object.buyprice*quantity-price*quantity
