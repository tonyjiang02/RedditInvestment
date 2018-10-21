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
uploadData(dictionary, "stocks", "10-20")