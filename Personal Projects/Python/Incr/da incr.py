import pygame, aTools, math
pygame.init()


window = (1080, 640)
display = pygame.display.set_mode(window)

mon = 0
clickMult = 1


class Button:
        colour = "red"
        type = "circle"
        radius = 50
        pos = ([p/2 for p in window])

        def __init__(self):
                self.exec = [self.draw]

        def onClick(self):
                global mon
                mon += 1 * clickMult

        def draw(self):
                pygame.draw.circle(display, self.colour, self.pos, self.radius)

class Cursor:
        pos = [0,0]
        mouseclick = False
        mouseButtons = pygame.mouse.get_pressed()

        def __init__(self):
                self.exec = [self.sim]

        def sim(self):
                self.pos = pygame.mouse.get_pos()
                self.rect = pygame.Rect(self.pos, (2,2))

                if not self.mouseButtons[0] and pygame.mouse.get_pressed()[0]:
                        self.mouseclick = True
                        self.click()
                else:
                        self.mouseclick = False


                self.mouseButtons = pygame.mouse.get_pressed()

        def click(self):
                for obj in clickables:
                        if obj.type == "circle":
                                if math.dist(self.pos, obj.pos) < obj.radius:
                                        obj.onClick()
                        elif obj.type == "rect":
                                if self.rect.collide(obj.rect):
                                        obj.onClick()




cursor = Cursor()
button = Button()
objects = [button, cursor]
clickables = [button]

runtime = True
while runtime:
        pygame.time.delay(20)
        display.fill("black")

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        runtime = False

        for object in objects:
                for command in object.exec:
                        command()



        pygame.display.update()