import random

run = True
gridRef = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25
}
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def createBoard(size:int):
        states = ["M", "B"]
        grid = []
        for x in range(0, size):
                column = []
                for y in range(0, size):
                        value = random.randint(0, 10)
                        if value > 8:
                                value = 0
                        else:
                                value = 1
                        column.append(states[value])
                grid.append(column)
        return grid

def viewBoard(grid):
        topRow = " "
        for i in range(0, len(grid)):
                topRow += "  " + alph[i]
        print(f"{topRow}")

        for x in range(0, len(grid)):
                ROW = ""
                for y in range(0, len(grid)):
                        #cell = grid[x][y]
                        #if cell == "M":
                        #        cell = "\033[31m◄\033[0m"
                        #elif cell == "B":
                        #        cell = "\033[7m■\033[0m"
                        ROW += "  " + grid[x][y]
                displayed = f"{alph[x]}{ROW}"
                print(displayed)
        print("")

def check(x,y, printing):
        global run
        global playerBoard
        x = gridRef[x]
        y = gridRef[y]
        cell = gridXY[x][y]
        if cell == "M": #"\033[31m◄\033[0m"
                if printing == 1:
                        #print("Mine")
                        pass
                playerBoard[y][x] = "\033[31m◄\033[0m"
        elif cell == "B":
                #print("Blank")
                playerBoard[y][x] = "□"


def mark(x,y):
        x = gridRef[x]
        y = gridRef[y]

def setGameState(running=True):
        pass

size = int(input("Size: "))
if size > 25:
        size = 25
        print("Board Size too big,\n Board Size set to 26")



gridXY = createBoard(size)
gridYX = []
for row in range(0, size):
        ROW = []
        for col in range(0, size):
                ROW.append(gridXY[col][row])
        gridYX.append(ROW)

playerBoard = []
for row in range(0, size):
        ROW = []
        for col in range(0, size):
                ROW.append("■")
        playerBoard.append(ROW)
valueBoard = []

def new_func1(y, x, value, dir):
        if y == 0:
                if gridYX[x+dir][y]   == "M":
                        value += 1
                if gridYX[x+dir][y+1] == "M":
                        value += 1
                if gridYX[x][y+1]     == "M":
                        value += 1
        elif y == size -1 :
                if gridYX[x+dir][y]   == "M":
                        value += 1
                if gridYX[x+dir][y-1] == "M":
                        value += 1
                if gridYX[x][y-1]     == "M":
                        value += 1
        else:
                if gridYX[x][y-1]     == "M":
                        value += 1
                if gridYX[x+dir][y-1] == "M":
                        value += 1
                if gridYX[x+dir][y]   == "M":
                        value += 1
                if gridYX[x+dir][y+1] == "M":
                        value += 1
                if gridYX[x][y+1]     == "M":
                        value += 1
        return value

for x in range(0, size):
        ROW = []
        for y in range(0, size):
                if gridYX[x][y] == "M":
                        value = "X"
                        break
                value = 0
                try:
                        if x == 0:
                                value = new_func1(y, x, value, 1)
                        elif x == size - 1:
                                value = new_func1(y, x, value, -1)
                        elif x in range(0, size):
                                if y == 0:
                                        if gridYX[x-1][y] == "M":
                                                value += 1
                                        if gridYX[x-1][y+1] == "M":
                                                value += 1
                                        if gridYX[x+1][y] == "M":
                                                value += 1
                                        if gridYX[x+1][y+1] == "M":
                                                value += 1
                                        if gridYX[x][y+1] == "M":
                                                value += 1
                                elif y == size:
                                        if gridYX[x-1][y] == "M":
                                                value += 1
                                        if gridYX[x-1][y-1] == "M":
                                                value += 1
                                        if gridYX[x+1][y] == "M":
                                                value += 1
                                        if gridYX[x+1][y-1] == "M":
                                                value += 1
                                        if gridYX[x][y-1] == "M":
                                                value += 1
                                else:
                                        if gridYX[x][y-1] == "M":
                                                value += 1
                                        if gridYX[x-1][y-1] == "M":
                                                value += 1
                                        if gridYX[x-1][y] == "M":
                                                value += 1
                                        if gridYX[x+1][y+1] == "M":
                                                value += 1
                                        if gridYX[x][y+1] == "M":
                                                value += 1
                except IndexError:
                        value = 0
                ROW.append(str(value))
        valueBoard.append(ROW)

for row in valueBoard:
        print(row)

#viewBoard(valueBoard)

viewBoard(gridYX)

while run:
        INPUT = input("Option: ").upper()
        if INPUT[0] == "C":
                x = input("Column: ").upper()
                y = input("Row   : ").upper()
                check(x,y, 1)

        elif INPUT[0] == "M":
                x = input("Column: ").upper()
                y = input("Row   : ").upper()
                mark(x,y)
        elif INPUT[0] == "V":
                viewBoard(playerBoard)
        elif INPUT == "RA":
                print("Up the Ra")
                for x in range(1,len(gridXY)+1):
                        if x > size:
                                x = size
                        for y in range(1,len(gridXY)+1):
                                if y > size -1:
                                        y = size
                                X = alph[x-1]
                                Y = alph[y-1]
                                check(X,Y,0)
        print(INPUT)

print("Bang")