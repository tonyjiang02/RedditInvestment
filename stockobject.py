class stockObject:

    def __init__(self ,symbol,buyprice, buydate, tradetype):
        self.symbol = symbol
        self.buyprice = buyprice
        self.buydate = buydate
        self.tradetype = tradetype
    def toString(self):
        return ""+self.symbol+ " buyprice:" +self.buyprice + " buydate"+self.buydate + " tradetype"+ self.tradetype