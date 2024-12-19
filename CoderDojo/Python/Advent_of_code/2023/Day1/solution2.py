i = 0
inputList = []
global numbersD; numbersD = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
global numbersT; numbersT = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

global numberList; numberList = ["zero", "one", "two", "three", "four" "five", "six", "seven", "eight", "nine"]

inputAddress = "CoderDojo/Python/Advent_of_code/2023/Day1/input.txt"
file = open(inputAddress, "r")
lineList = file.readlines()

processedLineList = []

for line in lineList:
        line = line.removesuffix("\n")
        processedLineList.append(line)

lineList = processedLineList
processedLineList = []

def convertStrInt(line):
        passed = False
        x=0
        step1 = []
        output = ""
        #length is the desired number in words
        for character in line:
                if character in numbersD:
                        step1.append(character)
                else:
                        query = character + line[x+1:x+2]
                        if query in numbersT:
                                step1.append(query)
                                passed = True
                        else:
                                query = character + line[x+1:x+3]
                        if query in numbersT and not passed:
                                step1.append(query)
                                passed = True
                        else:
                                query = character + line[x+1:x+4]
                        if query in numbersT and not passed:
                                step1.append(query)
                                passed = True
                        else:
                                query = character + line[x+1:x+5]
                        if query in numbersT and not passed:
                                step1.append(query)
                                passed = True
                x+=1
                passed = False

        for number in step1:
                if number in numbersD:
                        output += number
                else:
                        x = 0
                        for thing in numbersT:
                                if thing == number:
                                        output += str(x)
                                x += 1
        return output

for line in lineList:
        processedLineList.append(convertStrInt(line))
integerList = []

for number in processedLineList:
        x = number[0]
        y = number[-1]
        z = int(x+y)
        integerList.append(z)
for integer in integerList:
        i += integer
print("Output: ",i)