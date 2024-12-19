global Maxes
Maxes = {
        "r":12,
        "g":13,
        "b":14
}

inputAddress = "CoderDojo/Python/Advent_of_code/2023/Day2/input.txt"
file = open(inputAddress, "r")
lineList = file.readlines()

processedLineList = []

for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)

lineList = processedLineList
processedLineList = []


def polish(line:str):
        newLine = ""
        for char in line:
                if char != " ":
                        newLine += char
        line = newLine
        processedLineList = []
        output = []
        x = 0
        while True:
                if line[x] == ":":
                        line = line[x+1:] + ";"
                        break
                else:
                        x+=1

        x = 0
        y = 0
        tempString = ""
        while x < len(line):

                if line[x] == ";":
                        if y == 0:
                                tempString = line[y:x]
                        else:
                                tempString = line[y+1:x]
                        y = x

                        if tempString[-1] != ",":
                                tempString += ","
                        processedLineList.append(tempString)
                x+=1

        for group in processedLineList:
                formattedGroup = []
                temp = ""
                x = 0
                while x < len(group)-3:
                        temp = group[x:x+3]
                        if temp[0].isdigit():
                                if temp[1].isdigit():
                                        pass
                                else:
                                        temp = temp[:-1]
                                formattedGroup.append(temp)
                                x += 1
                        x+=1

                output.append(formattedGroup)

        return output

def selectionChecker(line):
        r = 0
        g = 0
        b = 0
        possible = False
        for group in line: #['15b', '6r']
                if possible:
                        break
                for element in group: #['15b', '6r']
                        if possible:
                                break
                        elif element[-1] == "r":
                                var = int(element.replace("r", ""))
                                if var > 12:
                                        possible = True

                        elif element[-1] == "g":
                                var = int(element.replace("g", ""))
                                if var > 13:
                                        possible = True

                        elif element[-1] == "b":
                                var = int(element.replace("b", ""))
                                if var > 14:
                                        possible = True

        return possible




for line in lineList:
        processedLineList.append(polish(line))
        print("Polished:",polish(line))

lineList = processedLineList
processedLineList = []

for line in lineList:
        processedLineList.append(selectionChecker(line))

x = 0

outputList = []
while x < len(processedLineList):
        if processedLineList[x] == False:
                outputList.append((x+1))
        x+=1
print(outputList)
y = 0
for number in outputList:
        y += number

print("Result:", y)