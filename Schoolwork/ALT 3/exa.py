import pandas, aTools

def Filter(sender, length, link, freeWin):
    if sender == "Known":
        if length > 16:
            if link == "Yes":
                spam = True
            elif freeWin == "Yes":
                spam = True
            else:
                spam = False
        else:
            spam = False

    elif sender == "Marketing":
        spam = True

    else: # Unknown
        if length >= 16:
            spam = True
        else:
            spam = False
    return spam




print(aTools.localPath("../ALT 3/ALT 3 Spreadsheet.csv"))
df = pandas.read_csv(aTools.localPath("../ALT 3/ALT 3 Spreadsheet.csv"))
print()
trainingRange = range(len(df["Sender Type"])-10)
testingRange = range(len(df["Sender Type"])-10,len(df["Sender Type"]))
fullRange = range(len(df["Sender Type"]))
print(f"{trainingRange=}\n{testingRange=}")

#Sender Type,Subject Length,Contains Free/Win,Contains Link,Spam

def checkArray(usedRange, flavourText):
    correctCount = 0
    count = 0
    for i in usedRange:
        count += 1
        sender = df["Sender Type"][i]
        length = df["Subject Length"][i]
        containsLink = df["Contains Link"][i]
        containsFreeWin = df["Contains Free/Win"][i]
        isSpam = df["Spam"][i]
    # sender = input("Sender: ")
    # length = int(input("Message Length: "))
    # link = input("Contains link: ")
    # freeWin = input("Contains Free or win: ")
        predictedResult = Filter(sender, length, containsLink, containsFreeWin)
        if predictedResult == isSpam:
            correctCount += 1
        # else:
        #     print(f"\nRow:{i}")
        #     print(f"\t{sender}")
        #     print(f"\t{length}")
        #     print(f"\t{containsLink}")
        #     print(f"\t{containsFreeWin}")
        #     print(f"\tActual Result:{bool(isSpam)}")
        #     print(f"\tPredicted Result:{predictedResult}")

    print(f"{flavourText}\t, Percentage Accuracy: {str(correctCount/count*100)[:4]}%")

checkArray(trainingRange, "Testing Data Only")
checkArray(testingRange, "Training Data Only")
checkArray(fullRange, "Merged Data \t")

#     print (Filter(sender, length, link, freeWin), "\n")
