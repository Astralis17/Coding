from __future__ import annotations
import aTools
with open(aTools.localPath("./words.txt")) as dictionaryFile:
        dictionary = dictionaryFile.readlines()
one = "aeilnorstu".upper()
two = "dg".upper()
three = "bcmp".upper()
four = "fhvwy".upper()
five = "k".upper()
eight = "jx".upper()
ten = "zq".upper()

points = {j:1 for i, j in enumerate(one)}
points.update({j:2 for i, j in enumerate(two)})
points.update({j:3 for i, j in enumerate(three)})
points.update({j:4 for i, j in enumerate(four)})
points.update({j:5 for i, j in enumerate(five)})
points.update({j:8 for i, j in enumerate(eight)})
points.update({j:10 for i, j in enumerate(ten)})
sorted(points)
print(points)

class Cell:
        def __init__(self, pos, board, value=" "):
                self.value = value
                self.position = pos
                self.board = board

        def set(self, value):
                self.value = value

        def getNeighbour(self, direction):
                return self.board.get(self.position[0]+direction[0],self.position[1]+direction[1])

        def getNeighbourCount(self)->Cell:
                count = 0
                for nPos in [[1,0],[-1,0],[0,1],[0,-1]]:
                        neighbour = self.getNeighbour(nPos)
                        if neighbour.value != " ":
                                count += 1
                return count

        def __str__(self):
                return self.position
        def __repr__(self):
                return str(self.position)

class Board:
        def __init__(self,size:int):
                self.board = {" ":{str(i):Cell([" ",str(i)], self, str(i)) for i in range(size)}}

                self.board.update({
                        str(y):{
                                str(x):Cell([x,y],self) for x in range(size)
                        } for y in range(size)
                })


        def display(self):
                print(f"  ")
                for row in self.board:
                        rowStr = str(row) + " "
                        for c in self.board[row]:
                                rowStr += self.board[row][c].value + " "
                        print(rowStr)

        def update(self, letter:str, x:int|str,y:int):
                self.get(x,y).set(letter)

        def get(self,x,y):
                return self.board[str(y)][str(x)]

        def place(self, string, startPos:list[int], endPos=None,direction=None):
                string = string.upper()
                if direction:
                        if direction.lower() == "down":
                                positions = [[startPos[0],i] for i in range(startPos[1], startPos[1]+len(string))]
                        else:
                                positions = [[i,startPos[1]] for i in range(startPos[0], startPos[0]+len(string))]
                elif endPos !=None:
                        if startPos[0] == endPos[0]:
                                # print(list(range(startPos[1], endPos[1]+1)))
                                positions = [[startPos[0],i] for i in range(startPos[1], endPos[1]+1)]
                        else:
                                # print(list(range(startPos[0], endPos[0]+1)))
                                positions = [[i, startPos[1]] for i in range(startPos[0], endPos[0]+1)]
                else:
                        positions = [startPos]
                if len(positions) != len(string):
                        print("ERROR: WORD DOES NOT FIT")
                else:
                        for i, [x,y] in enumerate(positions):
                                self.update(string[i],x,y)

        def checkWords(self):
                cellsToProbe = []
                for row in self.board:
                        if row == " ":
                                continue
                        for col in self.board[row]:
                                cell = self.get(col,row)
                                try:
                                        if cell.value != " ":
                                                # print(cell.position)
                                                cellsToProbe.append(cell)
                                except KeyError:
                                        continue

                # apexCells = []

                formedWords= []
                # format: ["word", startCell, endCell]
                for cell in cellsToProbe:
                        down,right = False,False
                        if cell.getNeighbour([0,-1]).value == " " and cell.getNeighbour([0,1]).value != " ":
                                # apexCells.append([cell, "down"])
                                down = True
                        if cell.getNeighbour([-1,0]).value == " " and cell.getNeighbour([1,0]).value != " ":
                                # apexCells.append([cell, "right"])
                                right = True

                        directions = []
                        if down:
                                directions.append([0,1])
                        if right:
                                directions.append([1,0])
                        for direction in directions:
                                validity = False
                                word = ""
                                checking = True
                                currentCell = cell
                                while checking:
                                        word += currentCell.value
                                        try:
                                                nextCell = currentCell.getNeighbour(direction)                                               
                                                if nextCell.value == " ":
                                                        checking = False
                                                else:
                                                        currentCell = nextCell
                                        except KeyError:
                                                checking = False
                                checkedWord = word.lower() + "\n"
                                if checkedWord in dictionary or checkedWord.capitalize() in dictionary:
                                        print(f"{word} found in dictionary")
                                        validity = True
                                wordPoints = 0
                                for letter in word: wordPoints += points[letter]
                                formedWords.append([word, wordPoints, cell, currentCell, validity])


                # print(*[f"{i}\n" for i in formedWords])
                for word in formedWords:
                        print(word)

b = Board(15)

# [b.update(str(i)," ",0) for i in range(10)]

b.place("HERE", [4,3], [7,3])
b.place("HOME", [4,3], [4,6])
b.place("T",[3,3])
b.place("X",[7,4])
b.place("I",[7,5])
b.place("X",[5,4])
b.place("EMITTER",[4,6],direction="right")
b.checkWords()
b.display()

# b.checkWords()
# b.display()

# print(probeCellLine(b.get(4,3),[1,0]))
# b.place("T", [3,3])

while True:
        pass