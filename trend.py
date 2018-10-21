import database

arr = database.getData('stocks','10-20','10-30') 
dict1 = arr[0]
dict2 = arr[1]
stocks1 = dict1["stock"]
stocks2 = dict2["stock"]
# dict1["mentions"] = mentions (array)
# dict1["stocks"] = stock(array)
# dict1["sentiment"] = sentiment(array)

dictionary ={}
for i in range(0,len(stocks)):
    symbol = stocks1[i]
    if(symbol in stocks2)
        inc = (dict2['mentions'][i] - dict1['mentions'][i])/dict2['mentions'][i] * 100
        dictionary[symbol] = inc
dictionarySort = OrderedDict(sorted(dictionary.items(), key=lambda i: i[1], reverse = True))
print(dictionarySort)