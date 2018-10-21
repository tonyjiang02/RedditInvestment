class stockObject:

    def __init__(self ,symbol,quantity,buyprice, buydate, tradetype):
        self.symbol = symbol
        self.quantity = quantity
        self.buyprice = buyprice
        self.buydate = buydate
        self.tradetype = tradetype
    def toString(self):
        return ""+self.symbol+ " buyprice:" +self.buyprice + " buydate"+self.buydate + " tradetype"+ self.tradetype
class soldObject:
    def __init__(self,symbol,quantity,buyprice,sellprice,buydate,selldate,tradetype,profit):
        self.symbol = symbol
        self.quantity = quantity
        self.buyprice = buyprice
        self.sellprice = sellprice
        self.buydate = buydate
        self.selldate = selldate
        self.tradetype = tradetype
        self.profit = profit
    def toString(self):
        print(self.symbol + " quantity:"+self.quantity + " buyprice:"+self.buyprice + " sellprice:"+self.sellprice+ " buydate:"+self.buydate+" selldate:"+self.selldate+" tradetype:"+self.tradetype+" profit:"+self.profit)

