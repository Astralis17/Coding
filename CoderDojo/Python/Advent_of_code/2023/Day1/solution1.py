i = 0
inputList = []
inputAddress = "CoderDojo/Python/Advent_of_code/2023/Day1/input.txt"

file = open(inputAddress, "r")
lineList = file.readlines()
processedLineList = []
print(lineList)
for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)

lineList = processedLineList
processedLineList = []

for line in lineList:
        characterList = []
        for character in line:
                try:
                        number = int(character)
                        number = str(number)
                        characterList.append(number)
                except:
                        pass
        string = ""
        for num in characterList:
                string += num
        processedLineList.append(string)
integerList = []
for number in processedLineList:
        x = number[0]
        y = number[-1]
        z = int(x+y)
        print(z)
        integerList.append(z)
for integer in integerList:
        i += integer
print("Output: ",i)
