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

def powerCounter(line):
        r,g,b=0,0,0
        elementList = []
        for group in line:
                for element in group:
                        elementList.append(element)
        for element in elementList:
                if element[-1] == "r" and int(element[:-1])>r:
                        r = int(element[:-1])
                elif element[-1] == "g" and int(element[:-1])>g:
                        g = int(element[:-1])
                elif element[-1] == "b" and int(element[:-1])>b:
                        b = int(element[:-1])
        return r*g*b


for line in lineList:
        processedLineList.append(polish(line))
        print("Polished:",polish(line))

lineList = processedLineList
processedLineList = []


y = 0
for line in lineList:
        y += powerCounter(line)

print("Output:", y)

