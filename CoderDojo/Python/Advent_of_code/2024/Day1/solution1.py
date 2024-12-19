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
x = 0
for number in range(len(leftList)):
        l = int(leftList[number])
        r = int(rightList[number])
        if l >= r:
                x += l - r
        else:
                x += r - l

print(x)