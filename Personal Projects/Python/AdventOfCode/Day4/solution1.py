file = open("Personal Projects/AdventOfCode/Day4/input.txt", "r")
output = open("Personal Projects/AdventOfCode/Day4/output.txt", "w")
lineList = file.readlines()

processedLineList = []
for line in lineList:
    line = line.removesuffix("\n")
    processedLineList.append(line)

lineList = processedLineList
processedLineList = []
lineList = [line.lower() for line in lineList]
for line in lineList:
    output.write(line+"\n")

up, down, right, left, rightUp, rightDown, leftUp, leftDown = False, False, False, False, False, False, False, False
global directions
directions = [up, down, right, left, rightUp, rightDown, leftUp, leftDown]

def dirCheck(x,y):
    U,D,R,L,RD,RU, LD, LU = directions
    if y > 2:
        U = True
    else:
        U = False

    if y < 135:
        D = True
    else:
        D = False

    if x > 2:
        L = True
    else:
        L = False

    if x < 135:
        R = True
    else:
        R = False

    if R and D:
        RD = True
    else:
        RD = False
    if R and U:
        RU = True
    else:
        RU = False

    if L and D:
        LD = True
    else:
        LD = False
    if L and U:
        LU = True
    else:
        LU = False

    return U,D,R,L,RD,RU,LD,LU

yPos = -1
xPos = -1
for line in lineList:
    yPos += 1
    xPos = -1
    up, down, right, left, rightUp, rightDown, leftUp, leftDown = dirCheck(xPos,yPos)
line = lineList[0]
for character in line:
    xPos += 1
    up, down, right, left, rightUp, rightDown, leftUp, leftDown = dirCheck(xPos,yPos)
    if character == "x":
        if right:
            tempString = line[xPos:xPos+4]
            if tempString == "xmas":
                print(tempString.upper())
        if left:
            tempString = line[xPos-4:xPos]
            if tempString == "xmas":
                print(tempString.upper())