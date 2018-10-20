import main
import stocks
import nltk
from nltk import word_tokenize 
import operator
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
symbols = stocks.symbols
names = stocks.names
curr = main.readSub("stocks","hot",1)
tokenize = word_tokenize(curr)
dictionary = {}
for stuff in tokenize:
    if(len(stuff)>1 and binarySearch(symbols,stuff,0,None)>0):
        if(stuff in dictionary):
            dictionary[stuff]+=1
        else:
            dictionary[stuff]=1
# for stuff in tokenize:
#     if(len(stuff)>1 and stuff in symbols):
#         if(stuff in dictionary):
#             dictionary[stuff]+=1
#         else:
#             dictionary[stuff]=1

sortedDictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)

