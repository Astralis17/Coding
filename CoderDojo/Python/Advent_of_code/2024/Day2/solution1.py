inputAddress = "CoderDojo/Python/Advent_of_code/2024/Day2/input.txt"
file = open(inputAddress, "r")
lineList = file.readlines()
processedLineList = []

def refreshLists(lineList, processedLineList):
        lineList = processedLineList
        processedLineList = []
        return lineList, processedLineList

for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)
lineList, processedLineList = refreshLists(lineList, processedLineList)

for line in lineList:
        processedLineList.append(line.split(" "))
lineList, processedLineList = refreshLists(lineList, processedLineList)

for line in lineList:
        increment = 1
        values = [int(x) for x in line]
        if (values[0] - values[1]) > 0:
                increment = -1

        checks = []
        for i in range(len(values)-1):
                if increment > 0:
                        if (values[i+1] - values[i]) < 3:
                                checks.append(True)
                        else:
                                checks.append(False)
                else:
                        if (values[i] - values[i-1]) < 3:
                                checks.append(True)
                        else:
                                checks.append(False)
        if False in checks:
                processedLineList.append(False)
        else:
                processedLineList.append(True)
x = 0
for boolean in processedLineList:
        if boolean:
                x += 1
print(x)