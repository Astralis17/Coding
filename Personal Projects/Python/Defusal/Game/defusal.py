import random, pygame, hashlib, datetime, modules
from utils import *
from aTools import *
from unix import time as Time

debug = True
DATA = initDATA()
seed = "DEFUSE THE BOMB"
seed = ""
seedGen(seedInput=seed)
timepoint = Time.time

pygame.init()

display = pygame.display.set_mode((1000, 700), pygame.DOUBLEBUF, 32)
#difficulty = input("Difficulty: ").lower()
difficulty = "easy"
moduleID = {
                "BT" : modules.Button,
                "WR" : modules.Wires,
                "HX" : modules.Hexadecimal,
                "CT" : modules.Tiles,
                "BN" : modules.Binary,
                "CC" : modules.ColourCode,
                "MT" : modules.Mathematics,
                "MB" : modules.MultiButtons,
                "TM" : modules.Timing,
                "KY" : modules.KeyPad,
                "MR" : modules.Morse
}

buttons = []
wires = []
hexadecimal = []
colourTiles = []
binary = []
colourCode = []
mathematics = []
multiButtons = []
timing = []
keypad = []

moduleLists = {
        "BT" : buttons,
        "WR" : wires,
        "HX" : hexadecimal,
        "CT" : colourTiles,
        "BN" : binary,
        "CC" : colourCode,
        "MT" : mathematics,
        "MB" : multiButtons,
        "TM" : timing,
        "KY" : keypad
}

moduleList = [buttons, wires, hexadecimal, binary, colourCode, mathematics, multiButtons, timing, keypad]
modulesInScene = []
timeScale = 1

for i in range(0, DATA["difficulties"][difficulty]["moduleCount"]):
        y = 0
        x = weightedChoice(DATA["difficulties"][difficulty]["weights"])
        modulePos = tuple(DATA["difficulties"][difficulty]["modulePlacement"][str(i)])
        if difficulty == "easy":
                if i > 1:
                        y = 1
        elif difficulty == "medium":
                if i > 4:
                        y = 1
        else:
                if i > 5:
                        y = 1
        moduleLists[x].append(moduleID[x](modulePos[0], modulePos[1], i, y))

for moduleClass in moduleLists.values():
        for module in moduleClass:
                modulesInScene.append(module)

class Cursor:
        def __init__(self):
                self.x = 0
                self.y = 0
                self.Rect = pygame.Rect(self.x - 3, self.y - 3, 6, 6)
                self.colourW = pygame.Color(225, 225, 225, 255)
                self.colourB = pygame.Color(0, 0, 0, 0)


        def draw(self, display, mousePos):
                self.x = mousePos[0]
                self.y = mousePos[1]
                self.Rect = pygame.Rect(self.x - 3, self.y - 3, 6, 6)
                pygame.draw.rect(display, self.colourB, (self.Rect))
                pygame.draw.rect(display, self.colourW, (self.x-2, self.y-2, 4, 4))

cursor = Cursor()

deltaTime = 1
mouseDown = False
tempMouseDown = False
fails = 0
disarmed = 0
side = 0
gametime = 0
frame = 0
frameTimes = [0,0]
timerMilSec = DATA["difficulties"][difficulty]["time"] * 1000 * 60
timer = modules.timer(500, 350, -1, 0, timerMilSec)
run = True
pygame.mouse.set_visible(False)

print(f"Module Count: {len(modulesInScene)}")
game = True
frameStart = timepoint()
while run and game:
        frameEnd = timepoint()
        frameDifference = abs(frameEnd - frameStart)
        print(int((0.021-frameDifference)*1000))
        pygame.time.delay(int((0.021-frameDifference)*1000))
        frameStart = timepoint()
        timerMilSec -= 20 * timeScale
        gametime += 20

        display.fill((0,0,0))
        pygame.draw.rect(display, (100,100,100), (50, 50, 900, 600))
        mousePosition = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouseDown = True
                elif event.type == pygame.MOUSEBUTTONUP:
                        mouseDown = False
                elif event.type == pygame.KEYDOWN:
                        #print(event.key)
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:

                                side = (side+1)%2
                                for module in modulesInScene:
                                        module.typing = False
                        else:
                                for module in modulesInScene:
                                        if module.keypresses and module.typing:
                                                module.keypress(event.key)

        for module in modulesInScene:
                if module.side == side:
                        module.draw(display)
                        if tempMouseDown != mouseDown and mouseDown != False and module.disarmed == False:
                                module.press(cursor)
                if module.tickable:
                        module.tick(gametime)
        tempMouseDown = mouseDown

        disarmed = 0
        for module in modulesInScene:
                fails += module.fails
                module.fails = 0 
                if module.disarmed:
                        disarmed += 1
        timeScale = 2**fails
        if fails > 2 or timerMilSec <= 0:
                game = False
                print("BANG")

        if disarmed >= len(modulesInScene):
                game = False
        timer.tick(display, timerMilSec, fails)

        cursor.draw(display, mousePosition)
        pygame.display.update()

'''
        if gametime % 1000 == 0 and debug:
                for module in modulesInScene:
                        if module.disarmed:
                                print(f"{module.moduleID}: {module.disarmed}")
                print(f"disarms: {disarmed}")
'''
pygame.mouse.set_visible(True)
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        if fails > 2:
                display.fill((225, 40, 40))
        if disarmed >= len(modulesInScene):
                display.fill((40, 225, 40))
        pygame.display.update()


pygame.quit()