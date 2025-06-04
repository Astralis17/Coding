from pygame import draw as pDraw, display, font, Rect as RECT
from random import randint
import random
from math import dist
import utils
import aTools

DATA = utils.initDATA()

class Rect(RECT):
        def textPlacementY(self, size):
                return self.top - size*0.5/16 + 5
        def textPlacementX(self, size):
                return self.left - size*0.5/16 + 5
        def __tuple__(self):
                return (self.left, self.top, self.width, self.height)

class timer:
        def __init__(self, x:int, y:int, moduleID:int, side:int, timerMS, size=120):
                self.data = DATA["moduleData"]["Button"]
                self.x = x
                self.y = y
                self.moduleID = moduleID
                self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-1)]
                self.colourB = tuple(self.data["Colours"][randint(-1, len(self.data["Colours"])-1)])
                self.colourT = (230,230,230)
                self.size = size*2
                self.side = side
                self.timerMilSec = timerMS
                self.timerSecond = int((timerMS / 1000) % 60)
                self.timerMinute = int(timerMS / 1000 / 60)
                self.displayString = str(self.timerMinute) + ":" + str(self.timerSecond)
                self.timerObjMin = aTools.Pygame.font(40).render(str(self.timerMinute), True, (245, 20, 20))
                self.timerObjCol = aTools.Pygame.font(40).render(":", True, (245, 20, 20))
                self.timerObjSec = aTools.Pygame.font(40).render(str(self.timerSecond), True, (245, 20, 20))

        def tick(self, surface:display, timerMS, fails):
                self.timerMilSec = timerMS

                self.timerSecond = int((timerMS / 1000) % 60)
                seconds = str(self.timerSecond)
                seconds = seconds.split(".")[0]
                minutes = str(self.timerMinute)
                minutes = minutes.split(":")[0]
                if len(minutes) == 1:
                        minutes = "0" + minutes
                if len(seconds) == 1:
                        seconds = "0" + seconds
                self.displayString = minutes + ":" + seconds
                if self.timerMilSec % 1000 == 0:
                        pass
                        #print(self.displayString)
                self.timerObjMin = aTools.Pygame.font(40).render(minutes, True, (245, 20, 20))
                self.timerObjSec = aTools.Pygame.font(40).render(seconds, True, (245, 20, 20))
                if self.timerMilSec % 60000 == 0:
                        self.timerMinute = int(timerMS / 1000 / 60) -1

                self.draw(surface, fails)

        def draw(self, surface:display, fails):
                #Backing
                pDraw.rect(surface, (160,160,160), (self.x - self.size*8/15, self.y - self.size*8/15, self.size*16/15, self.size*16/15))

                #Timer Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*7/16, self.size*8/10, self.size*4/16))
                surface.blit(self.timerObjMin, (self.x - self.size*3/10, self.y - self.size*7/16 + 5))
                surface.blit(self.timerObjCol, (self.x - self.size*0.2/16 - 2, self.y - self.size*7/16 + 5))
                surface.blit(self.timerObjSec, (self.x + self.size*1.25/10, self.y - self.size*7/16 + 5))
                #Marks Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*1/8, self.size*8/10, self.size/2))

                if fails >= 1:
                        pDraw.line(surface, (245, 20, 20), (self.x - (self.size*4/10) + 10, self.y - (self.size*1/8) + 10),(self.x -10, self.y + (self.size*3/8) - 10), 5)
                        pDraw.line(surface, (245, 20, 20), (self.x - (self.size*4/10) + 10, self.y + (self.size*3/8) - 10),(self.x -10, self.y - (self.size*1/8) + 10), 5)
                if fails >= 2:
                        pDraw.line(surface, (245, 20, 20), (self.x + (self.size*3/10) + 10, self.y - (self.size*1/8) + 10),(self.x +10, self.y + (self.size*3/8) - 10), 5)
                        pDraw.line(surface, (245, 20, 20), (self.x + (self.size*3/10) + 10, self.y + (self.size*3/8) - 10),(self.x +10, self.y - (self.size*1/8) + 10), 5)

class module:
        debug = True
        tickable = False
        keypresses = False
        fails = 0
        disarmed = False
        disarmedRect = Rect(0,0,0,0)

        def __init__(self, x:int, y:int, module:int, side:int, size=120, debug=False, answers=False):
                self.x = x
                self.y = y
                self.moduleID = module
                self.size = size*2
                self.side = side
                self.moduleRect = Rect(self.x - self.size*8/15,self.y - self.size*8/15, self.size*16/15, self.size*16/15)
                self.debug = debug
                self.answers = answers

                self.colourA = (255,255,255)
                self.colourDT = (255,255,255)

                self.init()
        def init():
                pass
        def press(self, cursor):
                pass
        def drawXtra(self, surface):
                pass
        def draw(self, surface):
                pDraw.rect(surface, (140,140,140), self.moduleRect)
                pDraw.rect(surface, [(40, 40, 40), (40, 225, 40)][self.disarmed], self.disarmedRect)
                self.drawXtra(surface)

class typable(module):
        keypresses = True
        typing = False
        enterText = ""
        typingData = DATA["typingData"]
        textLimit = 999999
        answer = "test"

        def keypress(self, key):
                if self.disarmed:
                        self.keypresses = False
                        self.typing = False
                        return

                charKey = key - self.typingData["alphKeyOffset"]
                numKey = key - self.typingData["numKeyOffset"]
                numpadKey =  key - self.typingData["numpadKeyOffset"]
                if charKey >= 0 and charKey < 26 and len(self.enterText) < self.textLimit:
                        self.enterText += self.typingData["alphabet"][charKey]
                elif numKey >= 0 and numKey < 26 and len(self.enterText) < self.textLimit:
                        self.enterText += str(numKey)
                elif numpadKey >= 0 and numpadKey < 26 and len(self.enterText) < self.textLimit:
                        self.enterText += self.typingData["numpadNumbers"][numpadKey]
                elif key == 8:
                        self.enterText = self.enterText[:-1]
                elif key == 13:
                        self.submit()

        def submit(self):
                if self.enterText == self.answer:
                        print("Submission Correct")
                        self.disarmed = True
                        self.colourA = (40, 225, 40)
                        self.typing = False
                        return True
                else:
                        self.enterText = ""
                        self.fails += 1
                        print(self.fails)


class Button(module):
        def init(self):
                self.data = DATA["moduleData"]["Button"]
                self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-1)]
                self.colourB = tuple(self.data["Colours"][randint(-1, len(self.data["Colours"])-1)])
                self.colourT = (230,230,230)
                self.presses = 0
                self.size /= 2
                self.arrowSize = self.size/6
                self.textObj = aTools.Pygame.font(35, fontWeight=10).render(self.text, True, self.colourT, self.colourB)
                if self.text == "Blank" and list(self.colourB) == self.data["Colours"][0]:
                        self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-3)]
                elif self.text == "Stop" and list(self.colourB) == self.data["Colours"][0]:
                        self.text = self.data["Texts"][randint(0, len(self.data["Texts"])-3)]

                winCondition = []
                if self.colourB == tuple(self.data["Colours"][0]) and self.text == self.data["Texts"][0]:
                        winCondition = [1, 0]
                elif self.colourB == tuple(self.data["Colours"][1]):
                        winCondition = [2, 0]
                elif self.text == self.data["Texts"][1]:
                        winCondition = [3, 1]
                elif self.colourB in [tuple(self.data["Colours"][2]),tuple(self.data["Colours"][3])]:
                        winCondition = [4, 1]
                print(f"{self.moduleID}: {winCondition}")
                self.winCondition = winCondition


        def drawXtra(self, surface:display):
                if self.disarmed:
                        self.textObj = aTools.Pygame.font(35, fontWeight=0).render(self.text, True, self.colourT)
                else:
                        self.colourT = (230,230,230)
                        self.textObj = aTools.Pygame.font(35, fontWeight=0).render(self.text, True, self.colourT)
                if self.colourB == self.colourT:
                        self.colourT = tuple([x * 0.2 for x in self.colourT])
                        self.textObj = aTools.Pygame.font(35, fontWeight=0).render(self.text, True, self.colourT)

                counter = aTools.Pygame.font(35).render(str(self.presses), True, (255,255,255))

                #Backing
                pDraw.rect(surface, (160,160,160), self.moduleRect)

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


        def press(self, cursor):
                mousePos = [cursor.x, cursor.y]
                result = [self.presses]
                if dist(mousePos, (self.x, self.y + self.size*2/3)) < self.arrowSize:
                        result = [self.presses, 0]
                        self.presses = 0

                elif dist(mousePos, (self.x, self.y - self.size*2/3)) < self.arrowSize:
                        result = [self.presses, 1]
                        self.presses = 0

                elif dist(mousePos, (self.x, self.y)) < self.size:
                        if self.presses < 10:
                                self.presses += 1

                if len(result) == 2:
                        if result == self.winCondition:
                                self.disarmed = True
                                self.colourT = (40, 225, 40)
                                self.text = "Disarmed"
                                print("Disarmed")
                                self.textObj = aTools.Pygame.font(35).render(self.text, True, self.colourT, self.colourB)
                        else:
                                self.fails += 1
                                print("Fail")

class Wires(module):
        def init(self):
                self.data = DATA["moduleData"]["Wires"]

class Hexadecimal(typable):
        textLimit = 4
        def init(self):
                self.data = DATA["moduleData"]["Hexadecimal"]


                wordKeys = list(self.data["Words"].keys())
                self.disarmedRect = Rect(self.x + self.size*7.5/16, self.y - self.size*8/16, self.size*1/16, self.size*16/16)
                self.answer = wordKeys[randint(0, len(self.data["Words"])-1)]
                self.displayText = self.data["Words"][self.answer]
                self.displayTextObj = aTools.Pygame.font(35).render(self.displayText, True, self.colourDT)
                self.displayTextRect = (self.x - self.size*4/10, self.y - self.size*7/16, self.size*8/10, self.size*4/16)
                self.answerObj = aTools.Pygame.font(35).render(self.enterText, True, self.colourA)
                self.submitObj = aTools.Pygame.font(35).render("Submit", True, self.colourDT)
                print(f"{self.moduleID}: {self.answer}")

        def drawXtra(self, surface):
                self.displayTextObj = aTools.Pygame.font(28).render(self.displayText, True, self.colourDT)
                self.answerObj = aTools.Pygame.font(30).render(self.enterText, True, self.colourA)
                self.submitObj = aTools.Pygame.font(35).render("Submit", True, self.colourDT)

                #Display Box
                pDraw.rect(surface, (10,10,10), self.displayTextRect)

                #Answer Box
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y - self.size*1/8, self.size*8/10, self.size*4/16))

                #Submit Button
                pDraw.rect(surface, (10,10,10), (self.x - self.size*4/10, self.y + self.size*3/16, self.size*8/10, self.size*4/16),)

                #Texts
                surface.blit(self.displayTextObj, (self.x - self.size*4.0/10, self.y - self.size*6.5/16 + 5))
                surface.blit(self.answerObj,      (self.x - self.size*2.0/10, self.y - self.size*2/16  + 5))
                surface.blit(self.submitObj,      (self.x - self.size*2.5/10, self.y + self.size*3.5/16 + 5))
                pDraw.rect(surface, [(40, 40, 40), (40, 225, 40)][self.disarmed], self.disarmedRect)

        def press(self, cursor):
                self.typing = False
                if cursor.Rect.colliderect(Rect(self.x - self.size*4/10, self.y - self.size*2/16, self.size*8/10, self.size*4/16)):
                        self.typing = True
                elif cursor.Rect.colliderect(Rect(self.x - self.size*4/10, self.y + self.size*3/16, self.size*8/10, self.size*4/16)):
                        self.submit()

class Binary(module):
        conditions = [
                ((2, True),  (7, False)),
                ((1, True),  (2, True)),
                ((1, False), (7, False)),
                ((1, True),  (2, True), (3, True)),
                ((1, True),  (2, True), (3, True), (4, True)),
        ]
        def init(self):
                self.data = DATA["moduleData"]["Binary"]
                self.redRect = Rect(self.x + self.size*1/16, self.y + self.size*5/16, self.size*6/16, self.size*3/16)
                self.greenRect = Rect(self.x - self.size*7/16, self.y + self.size*5/16, self.size*6/16, self.size*3/16)
                self.disarmedRect = Rect(self.x - self.size*8/16, self.y - self.size*8/16, self.size*16/16, self.size/16)

                self.presses = 0
                self.bars = [
                        (
                                Rect(self.x - self.size*(6.5 - (2*i))/16, self.y - self.size*6/16, self.size*1/16, self.size*10/16),
                                random.choice([True,False])
                        ) for i in range(7)
                ]
                self.barLights = [bar[1] for bar in self.bars]
                i = 1
                self.winCondition = 0
                for condition in self.conditions:
                        conditionFound = False
                        if True not in self.barLights:
                                self.winCondition = i
                        else:
                                for condition in self.conditions:
                                        i += 1
                                        conditionFound = True
                                        for req in condition:
                                                if self.barLights[req[0]-1] == req[1]:
                                                        conditionFound = bool(conditionFound and True)
                                                else:
                                                        conditionFound=False
                                        if conditionFound:
                                                self.winCondition = i
                                                break
                                if not conditionFound:
                                        if self.barLights.count(False) > 3:
                                                self.winCondition = 7
                                                conditionFound = True
                                        elif self.barLights.count(True) > 5:
                                                self.winCondition = 8
                                                conditionFound = True
                                        elif False not in self.barLights:
                                                self.winCondition = 9
                                                conditionFound = True
                                        else:
                                                self.winCondition = 10
                                                conditionFound = True
                                if conditionFound:
                                        break
                print(f"{self.moduleID}: {self.winCondition}")

        def drawXtra(self, surface):
                counter = aTools.Pygame.font(35).render(str(self.presses), True, (255,255,255))
                pDraw.rect(surface, (225, 40, 40), self.redRect)
                pDraw.rect(surface, (40, 225, 40), self.greenRect)
                surface.blit(counter, (self.x + self.size*3/16, self.y + self.size*5/16))

                for bar in self.bars:
                        if bar[1]:
                                colour = (225, 225, 225)
                        else:
                                colour = (40,40,40)
                        pDraw.rect(surface, colour, bar[0])

        def press(self, cursor):
                if cursor.Rect.colliderect(self.redRect):
                        self.presses += 1
                        print(self.winCondition)
                elif cursor.Rect.colliderect(self.greenRect):
                        if self.presses == self.winCondition:
                                self.disarmed = True
                        else:
                                self.fails += 1
                                self.presses = 0

class Timing(module):
        tickable = True
        def init(self):
                self.data = DATA["moduleData"]["Timing"]

                self.blackRect = Rect(self.x - self.size*7.5/16, self.y - self.size*7/16, self.size*14/16, self.size*6/16)
                self.lightRect = Rect(self.x - self.size*7.5/16, self.y, self.size*14/16, self.size*3/16)
                self.greenRect = Rect(self.x - self.size*4.5/16, self.y + self.size*4/16, self.size*8/16, self.size*3/16)
                self.disarmedRect = Rect(self.x + self.size*7.5/16, self.y - self.size*8/16, self.size*1/16, self.size*16/16)

                text = [[random.choice(self.data["Letters"]) for i in range(2)]]
                text += [[random.choice(range(1,10)) for i in range(2)]]
                displayText = "".join(text[0]) + " " + str(text[1][0]) + str(text[1][1])

                letterValue = self.data["LetterValues"][text[0][0]] + self.data["LetterValues"][text[0][1]]
                numberValue = text[1][0] + text[1][1]
                value = letterValue * numberValue
                self.orderPosition = 0
                self.winPosition = 0
                while True:
                        var = self.data["Ranges"][self.data["Order"][self.winPosition]]
                        if value in range(var[0], var[1]):
                                break
                        else:
                                self.winPosition += 1

                print(f"{self.moduleID}: " + self.data["Order"][self.winPosition])

                self.displayText = aTools.Pygame.font(40).render(displayText, True, (255,255,255))


        def tick(self, *args):
                gameTime = args[0]
                if gameTime % 1000 == 0:
                        self.orderPosition = (self.orderPosition+1)%5


        def drawXtra(self, surface):
                self.lightColour = [
                        self.data["Colours"][self.data["Order"][self.orderPosition]],
                        self.data["Colours"][self.data["Order"][self.winPosition]]
                ][self.disarmed]
                pDraw.rect(surface, self.lightColour, self.lightRect)
                pDraw.rect(surface, (40, 225, 40), self.greenRect)
                pDraw.rect(surface, (0, 0, 0), self.blackRect)
                surface.blit(self.displayText, (self.x - self.size*4.3/16, self.y - self.size*6/16))

        def press(self, cursor):
                if cursor.Rect.colliderect(self.greenRect):
                        if self.orderPosition == self.winPosition:
                                self.disarmed = True
                        else:
                                self.fails += 1
                                print(self.fails)

class Tiles(typable):
        textLimit = 2
        def init(self):
                self.data = DATA["moduleData"]["Tiles"]

                self.disarmedRect = Rect(self.x - self.size*8/16, self.y - self.size*8/16, self.size*16/16, self.size/16)
                self.answerRect = Rect(self.x - self.size*6/16, self.y + self.size*1/16, self.size*12/16, self.size*3/16)
                self.submitRect = Rect(self.x - self.size*5/16, self.y + self.size*5/16, self.size*10/16, self.size*3/16)
                self.answerObj = aTools.Pygame.font(35).render(self.enterText, True, self.colourA)
                self.submitObj = aTools.Pygame.font(35).render("Submit", True, self.colourA)

                p = randint(0,5)
                q = randint(0,5)
                self.colours = [self.data["colours"][p], self.data["colours"][q]]
                self.colourRects = [Rect(self.x + (self.size*i/16), self.y - self.size*6/16, self.size*6/16, self.size*6/16) for i in [-7,1]]
                self.answer = str(self.data["colourValues"][p] + self.data["colourValues"][q])

                print(f"{self.moduleID}: {self.answer}")


        def drawXtra(self, surface):
                self.answerObj = aTools.Pygame.font(30).render(self.enterText, True, self.colourA)
                self.submitObj = aTools.Pygame.font(35).render("Submit", True, self.colourDT)

                for i in [0,1]:
                        pDraw.rect(surface, self.colours[i], self.colourRects[i])
                pDraw.rect(surface, (10,10,10), self.answerRect)
                pDraw.rect(surface, (90,90,90), self.submitRect)
                surface.blit(self.answerObj, (self.x - self.size*2.0/10, self.y + self.size*0.5/16 + 5))
                surface.blit(self.submitObj, (self.x - self.size*2.5/10, self.submitRect.top - self.size*0.5/16 + 5))

        def press(self, cursor):
                self.typing = False
                if cursor.Rect.colliderect(self.answerRect):
                        self.typing = True
                elif cursor.Rect.colliderect(self.submitRect):
                        self.submit()

class Mathematics(typable):
        tickable = False
        textLimit = 4
        def init(self):
                self.data = DATA["moduleData"]["Mathematics"]
                x = lambda y: (y[0] + y[1] + y[2] + y[3][0]).upper()
                displayText = x([random.choice(self.data["letters"]) for i in range(4)])
                self.disarmedRect = Rect(self.x + self.size*7.5/16, self.y - self.size*8/16, self.size*1/16, self.size*16/16)
                self.displayTextRect = (self.x - self.size*7.5/16, self.y - self.size*7/16, self.size*14/16, self.size*4/16)
                self.answerRect = Rect(self.x - self.size*7/16, self.y - self.size*1/16, self.size*13/16, self.size*3/16)
                self.submitRect = Rect(self.x - self.size*5.5/16, self.y + self.size*4/16, self.size*10/16, self.size*3/16)

                digits = []
                for letter in displayText:
                        digits.append("abcdefghij".index(letter.lower()))
                self.answer = str((digits[0]*10 + digits[1]) * (digits[2]*10 + digits[3]))
                print(f"{self.moduleID}: {self.answer}")
                displayText = displayText[:2] + " " + displayText[2:]

                self.answerObj = [aTools.Pygame.font(0).render(self.enterText, True, self.colourA), 30]
                self.submitObj = aTools.Pygame.font(35).render("Submit", True, self.colourA)
                self.displayText = aTools.Pygame.font(35).render(displayText, True, self.colourDT)

        def drawXtra(self, surface):
                self.answerObj[0] = aTools.Pygame.font(self.answerObj[1]).render(self.enterText, True, self.colourA)

                #pDraw.rect(surface, (40, 225, 40), self.greenRect)
                pDraw.rect(surface, (0, 0, 0), self.displayTextRect)
                #surface.blit(self.displayText, (self.x - self.size*4.3/16, self.y - self.size*6/16))
                pDraw.rect(surface, (10,10,10), self.answerRect)
                pDraw.rect(surface, (90,90,90), self.submitRect)
                surface.blit(self.answerObj[0], (self.x - self.size*(len(self.enterText)*(1-self.answerObj[1]/100))/16, self.answerRect.textPlacementY(self.size)))
                surface.blit(self.submitObj, (self.x - self.size*4/16, self.submitRect.textPlacementY(self.size)))
                surface.blit(self.displayText, (self.x - self.size*4.3/16, self.y - self.size*6/16))

        def press(self, cursor):
                self.typing = False
                if cursor.Rect.colliderect(self.answerRect):
                        self.typing = True
                elif cursor.Rect.colliderect(self.submitRect):
                        self.submit()

class MultiButtons(module):
        inputOrder = ""
        answer = ""
        def init(self):
                self.data = DATA["moduleData"]["MultiButtons"]

                displayText = str(randint(100000, 999999))
                self.disarmedRect = Rect(self.x + self.size*7.5/16, self.y - self.size*8/16, self.size*1/16, self.size*16/16)
                self.displayText = aTools.Pygame.font(35).render(displayText, True, self.colourDT)
                self.displayTextRect = (self.x - self.size*7.5/16, self.y - self.size*7/16, self.size*14/16, self.size*4/16)

                self.redRect    = Rect(self.x - self.size*7.5/16, self.y -self.size*2/16, self.size*4/16, self.size*4/16)
                self.orangeRect = Rect(self.x - self.size*7.5/16, self.y +self.size*3/16, self.size*4/16, self.size*4/16)
                self.yellowRect = Rect(self.x - self.size*2.5/16, self.y -self.size*2/16, self.size*4/16, self.size*4/16)
                self.greenRect  = Rect(self.x - self.size*2.5/16, self.y +self.size*3/16, self.size*4/16, self.size*4/16)
                self.blueRect   = Rect(self.x + self.size*2.5/16, self.y -self.size*2/16, self.size*4/16, self.size*4/16)
                self.purpleRect = Rect(self.x + self.size*2.5/16, self.y +self.size*3/16, self.size*4/16, self.size*4/16)

                buttons = [self.redRect, self.orangeRect, self.yellowRect, self.greenRect, self.blueRect, self.purpleRect]
                self.buttons = []
                for i in range(6):
                        self.buttons.append([buttons[i], self.data["colours"][i], "ROYGBP"[i], False])

                leftoverButtons = ""
                for x in range(3):
                        if int(displayText[x]) < 6:
                                self.answer += "RYB"[x]
                                leftoverButtons += "OGP"[x]
                        else:
                                self.answer += "OGP"[x]
                                leftoverButtons += "RYB"[x]

                if int(displayText[3]) < 7:
                        for x in [1,2,0]:
                                self.answer += leftoverButtons[x]
                elif int(displayText[4]) < 7:
                        for x in [2,1,0]:
                                self.answer += leftoverButtons[x]
                elif int(displayText[5]) < 5:
                        for x in [0,1,2]:
                                self.answer += leftoverButtons[x]
                else:
                        for x in [0,2,1]:
                                self.answer += leftoverButtons[x]
                print(f"{self.moduleID}: {self.answer}")



        def drawXtra(self, surface):
                pDraw.rect(surface, (0,0,0), self.displayTextRect)
                for button in self.buttons:
                        pDraw.rect(surface, button[1], button[0])
                surface.blit(self.displayText, (self.x - self.size*4.8/16, self.y - self.size*6.3/16))

        def press(self, cursor):
                for button in self.buttons:
                        if cursor.Rect.colliderect(button[0]) and not button[3]:
                                self.inputOrder += button[2]
                                button[3] = True
                                break

                if cursor.Rect.colliderect(self.displayTextRect):
                        print(self.inputOrder)
                if len(self.inputOrder) == 6:
                        if self.inputOrder == self.answer:
                                self.disarmed = True
                        else:
                                fails += 1
                                for button in self.buttons:
                                        button[3] = False

class KeyPad(module):
        inputOrder = ""
        answer = ""
        def init(self):
                self.data = DATA["moduleData"]["Keypad"]
                self.numbers = [randint(1,80) for x in range(4)]
                self.tileSize = self.size*6/16
                self.colourDT = (40,40,40)


                self.tiles = [
                        [
                                Rect(self.x - self.size*7/16 + (self.size*(8*(i%2))/16), self.y - self.size*7/16 + (self.size*(8*(i//2))/16), self.tileSize, self.tileSize),
                                Rect(self.x - self.size*6/16 + (self.size*(8*(i%2))/16), self.y - self.size*7/16 + (self.size*(8*(i//2))/16), self.size*4/16, self.size*1/16),
                                str(i+1),
                                aTools.Pygame.font(40, fontWeight=2).render(str(self.numbers[i]), True, self.colourDT),
                                False
                        ]for i in range(4)
                ]
                for tile in self.tiles:
                        print(tile[0].__str__())


                self.YVALUE = 0
                self.XVALUE = 0
                for number in enumerate(self.numbers):
                        i = 0
                        for Range in self.data["ranges"]:
                                if number[1] in range(Range[0], Range[1]):
                                        command = self.data["steps"][number[0]][i]
                                        break
                                else:
                                        i += 1
                        exec(command)
                        self.YVALUE += number[1]
                self.YVALUE /= 2
                ZVALUE = self.XVALUE - self.YVALUE
                for Range in enumerate(self.data["zRanges"]):
                        RangeIndex = Range[0]
                        Range = Range[1]
                        if Range[0] <= ZVALUE and ZVALUE <= Range[1]:
                                self.answer = self.data["orders"][RangeIndex]
                                break
                print(f"{self.moduleID}: {self.answer}")

        def drawXtra(self, surface):
                for tile in self.tiles:
                        pressedColour = [(40, 40, 40), (40, 225, 40)][tile[4]]
                        pDraw.rect(surface, (200,200,200), tile[0])
                        pDraw.rect(surface, pressedColour, tile[1])
                        surface.blit(tile[3], (tile[0].left + self.tileSize/4, tile[0].top + self.tileSize/4))

        def press(self, cursor):
                for tile in self.tiles:
                        if cursor.Rect.colliderect(tile[0]) and not tile[4]:
                                self.inputOrder += tile[2]
                                tile[4] = True
                                break

                if len(self.inputOrder) == 4:
                        print("Answer: ", self.answer)
                        print("Input: ", self.inputOrder)
                        if self.inputOrder == self.answer:
                                self.disarmed = True
                        else:
                                self.fails += 1
                                for tile in self.tiles:
                                        tile[4] = False

class ColourCode(module):
        def init(self):
                self.data = DATA["moduleData"]["ColourCode"]

                self.bars = [
                        [
                                Rect(self.x - self.size*8/16, self.y - self.size*(7 -1.5*i)/16, self.size*15/16, self.size*1/16),
                                random.choice(self.data["colours"]),
                        ]for i in range(5)
                ]
                self.text = aTools.list([random.choice(self.data["colours"]) for i in range(5)]).__toString__()

                self.redRect = Rect(self.x + self.size*1/16, self.y + self.size*5/16, self.size*6/16, self.size*4/16)
                self.greenRect = Rect(self.x - self.size*8/16, self.y + self.size*5/16, self.size*6/16, self.size*3/16)
                self.disarmedRect = Rect(self.x + self.size*7.5/16, self.y - self.size*8/16, self.size*1/16, self.size*16/16)
                self.displayText = aTools.Pygame.font(40).render(self.text, True, (255,255,255))

        def drawXtra(self, surface):
                for bar in self.bars:
                        pDraw.rect(surface, self.data["coloursRGB"][bar[1]], bar[0])




class Morse(typable):
        def init(self):
                self.data = DATA["moduleData"]["Morse"]