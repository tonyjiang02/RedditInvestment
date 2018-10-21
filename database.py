import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import director
from ticker import Ticker
dictionary = director.dictionarySort
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
    doc = doc_ref.get()
    dict1 = doc.to_dict()
    return dict1
def uploadPortfolio(balance, portfolio, history):
    doc_ref = db.collection(u'portfolio').document(u'portfolio1')
    doc_ref.set({
        u'balance':balance,
        u'portfolio':portfolio,
        u'history':history
    })