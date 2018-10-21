import director
import database
import numpy
from ticker import Ticker
import trader
import time
sortedDict = director.process("stocks","hot",50)
database.uploadData(sortedDict,"stocks","10-20")
tickers = []
symbols = list(sortedDict.keys())
mentions = [a.mentions for a in sortedDict.values()]
sentiment = [a.sentiment for a in sortedDict.values()]
for i in range(len(symbols)):
    tickers.append(Ticker(str(symbols[i]),mentions[i],sentiment[i]))
stdMentions = numpy.std(mentions)
stdSentiment = numpy.std(sentiment)
sum=0
for i in mentions:
    sum+=i
avg1 = sum/len(mentions)
sum =0
for i in sentiment:
    sum+=i
avg2 = sum/len(sentiment)
for tick in tickers:
    z1 = (tick.mentions-avg1)/stdMentions
    z2 = (tick.sentiment-avg2)/stdSentiment
    tick.setZScore((z1+z2)/2)
tickers.sort(key=lambda x:x.zscore, reverse=True)
staged = []
for i in range(len(symbols)):
    if(tickers[i].getZScore()>1):
        staged.append(tickers[i])
for t in staged:
    print(t.getTag())
    print(t.getZScore())
    trader.buy(t.getTag(), round(t.getZScore()))
    time.sleep(5)