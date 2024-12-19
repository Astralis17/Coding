inputAddress = "CoderDojo/Python/Advent_of_code/2024/Day1/input.txt"
leftList = []
rightList = []

file = open(inputAddress, "r")
lineList = file.readlines()
processedLineList = []
for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)

lineList = processedLineList
processedLineList = []

def splitLine(line, listL, listR):
        listL.append(line[0:5])
        listR.append(line[8:])

        return listL, listR

for line in lineList:
        leftList, rightList = splitLine(line, leftList, rightList)

leftList.sort()
rightList.sort()

for lineL in leftList:
        x = 0
        if lineL in rightList:
                for lineR in rightList:
                        if lineL == lineR:
                                x += 1
                processedLineList.append((lineL, x))

x = 0
for line in processedLineList:
        y = int(line[0])
        z = line[1]

        x += y*z
print(x)
