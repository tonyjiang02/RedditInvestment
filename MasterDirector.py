import director
import database

sortedDict = director.process("stocks","hot",30)
database.uploadData(sortedDict,"stocks","10-20")