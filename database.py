import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from ticker import Ticker
cred = credentials.Certificate('hshacks-investment-a60cb5d9bfb0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print("init database")


def uploadData(dict,subreddit, date):
    print("upload data")
    doc_ref = db.collection(u''+subreddit).document(u''+ date)
    keys = dict.keys()
    men = [a.mentions for a in dict.values()]
    sent = [a.sentiment for a in dict.values()]
    
    doc_ref.set({
        u'stock':keys,
        u'mentions':men,
        u'sentiment':sent
    })
# uploadData(dictionary, "stocks", "10-20")

def getData(stock, date1, date2):
    doc_ref = db.collection(u''+stock).document(u''+date1)
    doc = doc_ref.get()
    doc_ref2 = db.collection(u''+stock).document(u''+date2)
    doc2 = doc_ref2.get()
    dict1 = doc.to_dict()
    dict2 = doc2.to_dict()
    # print(dict1['stock'])
    return [dict1, dict2]
def getPortfolio():
    doc_ref = db.collection(u'portfolio').document(u'portfolio1')
    history_ref = doc_ref.collection(u'history').get()
    portfolio_ref = doc_ref.collection(u'portfolio').get()
    history_arr = []
    portfolio_arr = []
    for doc in history_ref:
        print("one")
        history_arr.append(doc)
    for doc in portfolio_ref:
        portfolio_arr.append(doc)
    doc = doc_ref.get()
    superdoc = doc.to_dict()
    return [superdoc,history_arr,portfolio_arr]
def uploadPortfolio(stock_object, id):
    doc_ref = db.collection(u'portfolio').document(u'portfolio1').collection(u'portfolio').document(u''+str(id))
    doc_ref.set({
        u'symbol':stock_object.symbol,
        u'quantity':stock_object.quantity,
        u'buyprice':stock_object.buyprice,
        u'buydate':str(stock_object.buydate),
        u'tradetype':stock_object.tradetype
    })
def uploadHistory(sold_stock, id):
    doc_ref = db.collection(u'portfolio').document(u'portfolio1').collection(u'history').document(u''+str(id))
    doc_ref.set({
        u'symbol': sold_stock.symbol,
        u'quantity': sold_stock.quantity,
        u'buyprice': sold_stock.buyprice,
        u'sellprice' :sold_stock.sellprice,
        u'buydate' : str(sold_stock.buydate),
        u'selldate' : str(sold_stock.selldate),
        u'tradetype' : sold_stock.tradetype,
        u'profit' : sold_stock.profit
    })
def updateVars(balance, historyid, portfolioid):
    doc_ref = db.collection(u'portfolio').document(u'portfolio1')
    doc_ref.set({
        u'balance':balance,
        u'historyid':historyid,
        u'portfolioid':portfolioid
    })
def deletePortfolio(id):
    doc_ref = db.collection(u'portfolio').document(u'portfolio1').collection(u'portfolio').document(u''+str(id))
    doc_ref.delete()