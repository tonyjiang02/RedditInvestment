class Ticker:
    def __init__(self,tag,mentions,sentiment):
        self.tag = tag
        self.mentions = mentions
        self.sentiment = sentiment
    def getMentions(self):
        return self.mentions
    def toString(self):
        print(""+self.tag+" "+str(self.mentions)+ " "+str(self.sentiment))
    def setZScore(self, i):
        self.zscore = i
    def getTag(self):
        return self.tag
    def getSentiment(self):
        return self.sentiment
    def getZScore(self):
        return self.zscore