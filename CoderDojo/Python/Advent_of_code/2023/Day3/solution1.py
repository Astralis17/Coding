inputAddress = "CoderDojo/Python/Advent_of_code/2023/Day3/input.txt"
file = open(inputAddress, "r")
lineList = file.readlines()
processedLineList = []

global parts
global partsList
parts = {
        "@":0,
        "-":0,
        "+":0,
        "*":0,
        "/":0,
        "=":0,
        "%":0,
        "$":0,
        "#":0,
        "&":0,
}
partsList = ["@", "-", "+", "*", "/", "=", "%", "$", "#", "&"]

def ohGod(lines, lineNumber):
        if lineNumber != 0:
                lineU = lines[lineNumber-1]
        lineM = lines[lineNumber]
        if lineNumber != 139:
                lineD = lines[lineNumber+1]
        print(lineM)
        print(lineD)

        x = 0
        for character in lineM:
                if character in partsList:


                        total = 0
                        parts[character] = total
                x+=1
        return

for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)

lineList = processedLineList
processedLineList = []

print(ohGod(lineList, 0))
