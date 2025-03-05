import utils, modules, pygame
pygame.init()
display = pygame.display.set_mode((1000, 700))
weights = {
        "BT" : 4,
        "WR" : 4,
        "HX" : 2,
        "BN" : 3,
        "CC" : 3,
        "MT" : 2,
        "MB" : 2,
        "TM" : 3,
        "KY" : 0
}
DATA = utils.initDATA()
timerMilSec = 4.5 * 1000 * 60
#difficulty = input("Difficulty: ").lower()
timer = modules.timer(500, 350, -1, 0, timerMilSec)
hex1 = modules.button(200, 350, 0, 0)
hex2 = modules.button(800, 350, 1, 0)
mods = [hex1, hex2]
side = 0
mouseDown = False
tempMouseDown = False

run = True
while run:
        timerMilSec -= 5
        pygame.time.delay(0)

        mousePosition = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouseDown = True
                elif event.type == pygame.MOUSEBUTTONUP:
                        mouseDown = False
                        print(timerMilSec/1000/60)

        for mod in mods:
                if mod.side == side:
                        mod.draw(display)
                        if tempMouseDown != mouseDown and mouseDown != False and mod.disarmed == False:
                                mod.press(mousePosition)
        tempMouseDown = mouseDown

        fails = 0

        for module in mods:
                fails += module.fails

        timer.tick(display, timerMilSec, 2)

        pygame.display.update()