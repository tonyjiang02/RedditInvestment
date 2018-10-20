import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import director
dictionary = director.sortedDictionary
cred = credentials.Certificate('hshacks-investment-a60cb5d9bfb0.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
print("init database")


def uploadData(dict,subreddit, date):
    print("upload data")
    doc_ref = db.collection(u''+subreddit).document(u''+ date)
    keys = dict.keys()
    values = dict.values()
    
    doc_ref.set({
        u'keys':keys,
        u'val':values
    })
uploadData(dictionary, "stocks", "10-20")