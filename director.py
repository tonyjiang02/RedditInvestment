import main
import stocks
import nltk
from nltk import word_tokenize 
symbols = stocks.symbols
names = stocks.names
curr = main.readSub("stocks","hot",10)
tokenize = word_tokenize(curr)
for stuff in tokenize:
    if(stuff in symbols and len(stuff)>1):
        print(stuff)