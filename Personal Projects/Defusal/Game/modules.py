from pygame import draw as pDraw, display, font
from random import randint
from math import dist
import utils

DATA = utils.initDATA()

class timer:
        def __init__(self, x:int, y:int, module:int, side:int, timerMS, size=120):
                self.data = DATA["moduleData"]["Button"]
                self.x = x
                self.y = y
                self.moduleID = module
                self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-1)]
                self.colourB = tuple(self.data["Colours"][randint(-1, len(self.data["Colours"])-1)])
                self.colourT = (230,230,230)
                self.size = size*2
                self.disarmed = False
                self.side = side
                self.fails = 0
                self.timerMilSec = timerMS
                self.timerSecond = int((timerMS / 1000) % 60)
                self.timerMinute = int(timerMS / 1000 / 60)



        def tick(self, surface:display, timerMS, fails):
                self.timerMilSec = timerMS
                if self.timerMilSec % 1000 == 0:
                        self.timerSecond = int((timerMS / 1000) % 60)
                        seconds = str(self.timerSecond)
                        if len(seconds) == 1:
                                seconds = "0" + seconds
                        print(self.timerMinute, ":", seconds)
                if self.timerMilSec % 60000 == 0:
                        self.timerMinute = int(timerMS / 1000 / 60) -1



                #Backing
                pDraw.rect(surface, (160,160,160), (self.x - self.size*8/15, self.y - self.size*8/15, self.size*16/15, self.size*16/15))

                #Timer Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*7/16, self.size*8/10, self.size/4))
                #Marks Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*1/8, self.size*8/10, self.size/2))

                if fails >= 1:
                        pDraw.line(surface, (245, 20, 20), (self.x - (self.size*4/10) + 10, self.y - (self.size*1/8) + 10),(self.x -10, self.y + (self.size*3/8) - 10), 5)
                        pDraw.line(surface, (245, 20, 20), (self.x - (self.size*4/10) + 10, self.y + (self.size*3/8) - 10),(self.x -10, self.y - (self.size*1/8) + 10), 5)
                if fails >= 2:
                        pDraw.line(surface, (245, 20, 20), (self.x + (self.size*3/10) + 10, self.y - (self.size*1/8) + 10),(self.x +10, self.y + (self.size*3/8) - 10), 5)
                        pDraw.line(surface, (245, 20, 20), (self.x + (self.size*3/10) + 10, self.y + (self.size*3/8) - 10),(self.x +10, self.y - (self.size*1/8) + 10), 5)


class button:
        def __init__(self, x:int, y:int, module:int, side:int, size=120):
                self.data = DATA["moduleData"]["Button"]
                self.x = x
                self.y = y
                self.moduleID = module
                self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-1)]
                self.colourB = tuple(self.data["Colours"][randint(-1, len(self.data["Colours"])-1)])
                self.colourT = (230,230,230)
                self.presses = 0
                self.direction = 0
                self.size = size
                self.arrowSize = self.size/6
                self.disarmed = False
                self.side = side
                self.fails = 0
                self.textObj = utils.my_font.render(self.text, True, self.colourT, self.colourB)
                if self.text == "Blank" and list(self.colourB) == self.data["Colours"][0]:
                        self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-3)]
                elif self.text == "Stop" and list(self.colourB) == self.data["Colours"][0]:
                        self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-3)]

                print(self.colourB)
                print(self.text)

                winCondition = []
                if self.colourB == tuple(self.data["Colours"][0]) and self.text == self.data["Texts"][0]:
                        winCondition = [1, 0]
                elif self.colourB == tuple(self.data["Colours"][1]):
                        winCondition = [2, 0]
                elif self.text == self.data["Texts"][1]:
                        winCondition = [3, 1]
                elif self.colourB in [tuple(self.data["Colours"][2]),tuple(self.data["Colours"][3])]:
                        winCondition = [4, 1]
                print(winCondition)
                self.winCondition = winCondition


        def draw(self, surface:display):
                if self.disarmed:
                        self.textObj = utils.my_font.render(self.text, True, self.colourT, self.colourB)
                else:
                        self.colourT = (230,230,230)
                        self.textObj = utils.my_font.render(self.text, True, self.colourT, self.colourB)
                if self.colourB == self.colourT:
                        self.colourT = tuple([x * 0.2 for x in self.colourT])
                        self.textObj = utils.my_font.render(self.text, True, self.colourT, self.colourB)

                counter = utils.my_font.render(str(self.presses), True, (255,255,255))

                #Backing
                pDraw.rect(surface, (160,160,160), (self.x - self.size*16/15, self.y - self.size*16/15, self.size*32/15, self.size*32/15))

                #Circle & Outline
                pDraw.circle(surface, self.colourB, (self.x, self.y), self.size, 0)
                pDraw.circle(surface, tuple([x * 0.2 for x in (230,230,230)]), (self.x, self.y), self.size, 5)

                #Down Button
                pDraw.circle(surface, tuple([x * 0.6 for x in (255,255,255)]), (self.x, self.y + self.size*2/3), self.size/6, 0)
                pDraw.polygon(surface, tuple([x * 0.9 for x in (255,255,255)]), ((self.x + 10, self.y + self.size*9/15), (self.x - 10, self.y + self.size*9/15), (self.x, self.y + self.size*115/150)), 0)

                #Up Button
                pDraw.circle(surface, tuple([x * 0.6 for x in (255,255,255)]), (self.x, self.y - self.size*2/3), self.size/6, 0)
                pDraw.polygon(surface, tuple([x * 0.9 for x in (255,255,255)]), ((self.x + 10, self.y - self.size*9/15), (self.x - 10, self.y - self.size*9/15), (self.x, self.y - self.size*115/150)), 0)

                #Text
                surface.blit(self.textObj, (self.x + self.data["Offsets"][self.text], self.y - self.size/6))
                surface.blit(counter, (self.x + self.size - 15, self.y - self.size - 15))


        def press(self, mousePos):
                result = [self.presses]
                if dist(mousePos, (self.x, self.y + self.size*2/3)) < self.arrowSize:
                        print("Module", self.moduleID, ": ", "Down")
                        result = [self.presses, 0]
                        self.presses = 0

                elif dist(mousePos, (self.x, self.y - self.size*2/3)) < self.arrowSize:
                        print("Module", self.moduleID, ": ", "Up")
                        result = [self.presses, 1]
                        self.presses = 0

                elif dist(mousePos, (self.x, self.y)) < self.size:
                        if self.presses < 10:
                                self.presses += 1
                                print("Module", self.moduleID, ": ", self.presses)

                if len(result) == 2:
                        if result == self.winCondition:
                                self.disarmed = True
                                self.colourT = (40, 225, 40)
                                self.text = "Disarmed"
                                print("Disarmed")
                                self.textObj = utils.my_font.render(self.text, True, self.colourT, self.colourB)
                        else:
                                self.fails += 1
                                print("Fail")

class Hexadecimal:
        def __init__(self, x:int, y:int, module:int, side:int, size=120, ):
                self.data = DATA["moduleData"]["Hexadecimal"]
                self.x = x
                self.y = y
                self.moduleID = module
                self.size = size*2
                self.disarmed = False
                self.side = side
                self.fails = 0
                self.colourA = (255,255,255)
                self.colourDT = (255,255,255)
                self.enterText = ""



                wordKeys = list(self.data["Words"].keys())
                self.answer = wordKeys[randint(0, len(self.data["Words"])-1)]
                self.displayText = self.data["Words"][self.answer]
                self.displayTextObj = utils.my_font.render(self.displayText, True, self.colourDT)
                self.answerObj = utils.my_font.render(self.enterText, True, self.colourA)
                self.submitObj = utils.my_font.render("Submit", True, self.colourA)

                print(self.displayText)


        def draw(self, surface):
                self.displayTextObj = utils.my_font.render(self.displayText, True, self.colourDT)
                self.answerObj = utils.my_font.render(self.enterText, True, self.colourA)
                self.submitObj = utils.my_font.render("Submit", True, self.colourA)
                #Backing
                pDraw.rect(surface, (160,160,160), (self.x - self.size*8/15, self.y - self.size*8/15, self.size*16/15, self.size*16/15))

                #Display Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*7/16, self.size*8/10, self.size/4))

                #Answer Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*1/8, self.size*8/10, self.size/4))

                #Submit Button
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y + self.size*3/16, self.size*8/10, self.size/4),)

                #Texts
                surface.blit(self.displayTextObj, (self.x - self.size*3.5/10, self.y - self.size*7/16 + 5))
                surface.blit(self.answerObj,      (self.x - self.size*2.0/10, self.y - self.size*1/8  + 5))
                surface.blit(self.submitObj,      (self.x - self.size*2.1/10, self.y + self.size*3/16 + 5))


        def press(self, mousePos):
                if mousePos[0] in range(int(self.x - self.size*4/10), int(self.x - self.size*4/10 + self.size*8/10)):
                        if mousePos[1] in range(int(self.y - self.size*1/8), int(self.y - self.size*1/8 + self.size/4)):
                                print("HexPress")
                        elif mousePos[1] in range(int(self.y + self.size*3/16), int(self.y + self.size*3/16 + self.size/4)):
                                print("Submit!")

