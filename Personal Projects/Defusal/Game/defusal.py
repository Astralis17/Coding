import random, pygame, hashlib, modules
from utils import *

DATA = initDATA()
seed = "DEFUSE THE BOMBAS"
seed = ""
random.seed(seedGen(hashlib.md5, seedInput=seed))

pygame.init()
display = pygame.display.set_mode((1000, 700))
#difficulty = input("Difficulty: ").lower()
difficulty = "easy"
moduleID = {
                "BT" : modules.button,
                "WR" : "Wires",
                "HX" : modules.Hexadecimal,
                "CT" : "Colour Tiles",
                "BN" : modules.Binary,
                "CC" : "Colour Code",
                "MT" : "Mathematics",
                "MB" : "Multi Buttons",
                "TM" : "Timing",
                "KY" : "Keypad"
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



moduleList = [buttons, wires, hexadecimal, binary]
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
        moduleLists[x].append(moduleID[x](modulePos[0], modulePos[1], i, y))

for moduleClass in moduleLists.values():
        for module in moduleClass:
                modulesInScene.append(module)

mouseDown = False
tempMouseDown = False
fails = 0
disarmed = 0
side = 0
timerMilSec = DATA["difficulties"][difficulty]["time"] * 1000 * 60
timer = modules.timer(500, 350, -1, 0, timerMilSec)
run = True
pygame.mouse.set_visible(False)
while run:
        timerMilSec -= 5 * timeScale
        pygame.time.delay(4)
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
                        if event.key == pygame.K_RIGHT:
                                side = (side+1)%2
                                print(side)
        for module in modulesInScene:
                if module.side == side:
                        module.draw(display)
                        if tempMouseDown != mouseDown and mouseDown != False and module.disarmed == False:
                                module.press(mousePosition)
        tempMouseDown = mouseDown


        fails = 0
        disarmed = 0
        for moduleClass in moduleList:
                for module in moduleClass:
                        fails += module.fails
                        if module.disarmed:
                                disarmed += 1
        timeScale = 2**fails
        if fails > 2 or timerMilSec <= 0:
                run = False
                print("BANG")

        if disarmed >= len(modulesInScene):
                run = False
        timer.tick(display, timerMilSec, fails)
        pygame.draw.rect(display, "black", (mousePosition[0]-3,mousePosition[1]-3,6,6))
        pygame.draw.rect(display, "white", (mousePosition[0]-2,mousePosition[1]-2,4,4))
        
        pygame.display.update()

pygame.quit()