import json

databaseJS = open(r"Personal Projects\Ciphers\Polybius\Version 2 (Matrix)\customCharacters.json", "r")
databasePY = json.load(databaseJS)

def reverseData(db):
        addressList = list(db)
        dbList = []
        reversedDict = {}
        for obj in addressList:
                dbList.append(db[obj])
        print(dbList)
        for obj in dbList:
                reversedDict[obj] = True

reverseData(databasePY)



x = 12345654321 - 81


print(x/360)