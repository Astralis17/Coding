import json

basePath = "Testing/Json/"
databasePath = "database.json"
backupPath = "backup.json"

if input("Terminal or VSC: ").capitalize().startswith("T"):
        pass
else:
        databasePath = basePath + databasePath
        backupPath = basePath + backupPath

databaseJS = open(databasePath, "r")
databasePY = json.load(databaseJS)

def reloadDB(dbPath):
        databaseJS = open(dbPath, "r")
        dbPY = json.load(databaseJS)
        return dbPY

def readFormatted(dbPY):
        print("Database Contents")
        keyList = dbPY.keys()
        for key in keyList:
                print(key,":", dbPY[key])
        if str(keyList) == "dict_keys([])":
                print("Database Empty :(")
        print("")
        return bool(str(keyList) != "dict_keys([])")

def addElement(dbPath, dbPY):
        print("Perfect! What do you want to add?")
        print("1:String")
        print("2:Number")
        print("3:Boolean")
        varType = int(input("Choice: "))

        print("What do you want to call it")
        name = input("Name: ")

        print("Great! What do you want it to be?")
        if varType == 1:
                tempVar = input("String: ")

        elif varType == 2:
                tempVar = float(input("Number: "))

        elif varType == 3:
                i = str(input("True or False: "))
                if i.capitalize().startswith("T"):
                        tempVar = True
                else:
                        tempVar = False

        dbPY.update({name:tempVar})

        json.dump(dbPY, open(dbPath, "w"), indent = 0)

def updateElement(dbPath, dbPY):
        check = readFormatted(dbPY)
        if check:
                name = input("What do you want to Update?: ")
                try:
                        varType = str(type(dbPY[name]))
                except:
                        print("Error: Element not found")
                        return

                if varType == "<class 'str'>":
                        tempVar = input("String: ")
                elif varType == "<class 'int'>":
                        tempVar = input("Number: ")
                elif varType == "<class 'float'>":
                        tempVar = input("Number: ")
                elif varType == "<class 'bool'>":
                        tempVar = input("True or False: ")
                        if tempVar.capitalize().startswith("T"):
                                tempVar = True
                        else:
                                tempVar = False

                dbPY.update({name:tempVar})

                json.dump(dbPY, open(dbPath, "w"), indent = 0)
        else:
                print("Database empty, nothing to update")

def deleteElement(dbPath, dbPY):
        check = readFormatted(dbPY)

        if check:
                name = input("What do you want to delete?: ")
                try:
                        varType = str(type(dbPY[name]))
                except:
                        print("Error: Element not found")
                        return

                dbPY.pop(name)
                json.dump(dbPY, open(dbPath, "w"), indent = 0)
        else:
                print("Database empty, nothing to delete")

def cloneDB(databaseIn, databaseOut):

        data = json.load(open(databaseIn, "r"))
        json.dump(data, open(databaseOut, "w"), indent = 0)


while True:
        print("What would you like to do?")
        print("1: Read")
        print("2: Add Stuff")
        print("3: Update Stuff")
        print("4: Delete Stuff")
        print("5: Clear Database")
        print("6: Backup Database")
        print("7: Load Backup")
        print("8: Quit")
        x = int(input("Choice: ")) - 1
        print("")

        databasePY = reloadDB(databasePath)
        if x == 0:
                readFormatted(databasePY)
        elif x == 1:
                addElement(databasePath, databasePY)
        elif x == 2:
                updateElement(databasePath, databasePY)
        elif x == 3:
                deleteElement(databasePath, databasePY)
        elif x == 4:
                print("YOU ARE ABOUT TO CLEAR THE ENTIRE DATABASE ARE YOU SURE YOU WANT TO DO IT")
                print("IF YOU ARE CERTAIN, TYPE DATABASE IN ALL LOWERCASE")
                if input() == "database":
                        databasePY = {}
                        json.dump(databasePY, open(databasePath, "w"), indent = 0)
                print("Database wiped :'(")
        elif x == 5:
                cloneDB(databasePath, backupPath)
        elif x == 6:
                cloneDB(backupPath, databasePath)
        elif x == 7:
                break
        print("")

