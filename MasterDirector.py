import director
import database

sortedDict = director.process("stocks","new",100)
database.uploadData(sortedDict,"stocks","10-20")
