import main
import stocks
import nltk
from nltk import word_tokenize 
import operator
symbols = stocks.symbols
names = stocks.names
curr = main.readSub("wallstreetbets","top",10)
tokenize = word_tokenize(curr)
dictionary = {}
for stuff in tokenize:
    if(stuff in symbols and len(stuff)>1):
        if(stuff in dictionary):
            dictionary[stuff]+=1
        else:
            dictionary[stuff]=1
sortedDictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse = True)
print(sortedDictionary)