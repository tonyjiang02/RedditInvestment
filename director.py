import main
import stocks
import nltk
from nltk import word_tokenize 
import operator
from collections import OrderedDict
from ticker import Ticker
def binarySearch(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo+hi)//2
        midval = arr[mid]
        if midval < target:
            lo = mid+1
        elif midval > target: 
            hi = mid
        else:
            return mid
    return -1

keypos=["buy", "call", "hold"]
keyneg=["sell", "put"]
symbols = stocks.symbols
names = stocks.names
def process(sub,sort,num):
    curr = main.readSub(sub,sort,num)
    dictionary = {}
    count = 0
    for element in curr:
        tokenize= word_tokenize(element)
        count = 0
        mentions = []
        for item in tokenize:
            if(len(item) > 1 and binarySearch(symbols,item, 0, None) > 0):
                if(item in dictionary):
                    dictionary[item].mentions+=1
                    if(item not in mentions):
                        mentions.append(item)
                else: 
                    dictionary[item] = Ticker(item,1,0)
            elif item in keypos:
                count +=1
            elif item in keyneg:
                count -=1 
        for stuff in mentions:
            if(count>0):
                dictionary[stuff].sentiment+=1
            elif(count <0):
                dictionary[stuff].sentiment-=1
    dictionarySort = OrderedDict(sorted(dictionary.items(), key=lambda i: i[1].mentions, reverse = True))
    return dictionarySort
# tokenize = word_tokenize(curr)
# dictionary = {}
# for stuff in tokenize:
#     if(len(stuff)>1 and binarySearch(symbols,stuff,0,None)>0):
#         if(stuff in dictionary):
#             dictionary[stuff]+=1
#         else:
#             dictionary[stuff]=1


# for stuff in tokenize:
#     if(len(stuff)>1 and stuff in symbols):
#         if(stuff in dictionary):
#             dictionary[stuff]+=1
#         else:
#             dictionary[stuff]=1

# sortedDictionary = OrderedDict(sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True))

